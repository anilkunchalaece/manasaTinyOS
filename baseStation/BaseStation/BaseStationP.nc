#include "AM.h"
#include "Serial.h"

 typedef nx_struct myMsg {
  nx_uint8_t type;
  nx_uint8_t sender;
  nx_uint16_t data;
  nx_uint16_t temp;
} myMsg;


module BaseStationP @safe() {
  uses {
    interface Boot;
    interface SplitControl as SerialControl;
    interface SplitControl as RadioControl;

    interface AMSend as UartSend[am_id_t id];
    interface Receive as UartReceive[am_id_t id];
    interface Packet as UartPacket;
    interface AMPacket as UartAMPacket;
    
    interface AMSend as RadioSend[am_id_t id];
    interface Receive as RadioReceive[am_id_t id];
    interface Receive as RadioSnoop[am_id_t id];
    interface Packet as RadioPacket;
    interface AMPacket as RadioAMPacket;
	interface Packet;
    interface Leds;
	interface Timer<TMilli> as Timer0;
  }
}

implementation
{
  enum {
    UART_QUEUE_LEN = 2,
    RADIO_QUEUE_LEN = 12,
  };
	message_t mymsg;
	uint16_t CurrentSeqNumber=0;
	uint8_t timeType;
	uint8_t timedata;
  message_t  uartQueueBufs[UART_QUEUE_LEN];
  message_t  * ONE_NOK uartQueue[UART_QUEUE_LEN];
  uint8_t    uartIn, uartOut;
  bool       uartBusy, uartFull;

  message_t  radioQueueBufs[RADIO_QUEUE_LEN];
  message_t  * ONE_NOK radioQueue[RADIO_QUEUE_LEN];
  uint8_t    radioIn, radioOut;
  bool       radioBusy, radioFull;

  task void uartSendTask();


  event void Boot.booted() {
    uint8_t i;
	CurrentSeqNumber=0;
	
    for (i = 0; i < UART_QUEUE_LEN; i++)
      uartQueue[i] = &uartQueueBufs[i];
    uartIn = uartOut = 0;
    uartBusy = FALSE;
    uartFull = TRUE;

    for (i = 0; i < RADIO_QUEUE_LEN; i++)
      radioQueue[i] = &radioQueueBufs[i];
    radioIn = radioOut = 0;
    radioBusy = FALSE;
    radioFull = TRUE;

    call RadioControl.start();
    call SerialControl.start();
	
  }

  event void RadioControl.startDone(error_t error) {
    if (error == SUCCESS) {
      radioFull = FALSE;
	 
    }
  }

  event void SerialControl.startDone(error_t error) {
    if (error == SUCCESS) {
      uartFull = FALSE;
    }
  }

  event void SerialControl.stopDone(error_t error) {}
  event void RadioControl.stopDone(error_t error) {}

  uint8_t count = 0;

  message_t* ONE receive(message_t* ONE msg, void* payload, uint8_t len);
  
  event message_t *RadioSnoop.receive[am_id_t id](message_t *msg,
						    void *payload,
						    uint8_t len) {
    return receive(msg, payload, len);
  }
  
  event message_t *RadioReceive.receive[am_id_t id](message_t *msg,
						    void *payload,
						    uint8_t len) {
    return receive(msg, payload, len);
  }

  message_t* receive(message_t *msg, void *payload, uint8_t len) {
    message_t *ret = msg;
    atomic {
	  ret = uartQueue[0];
	  uartQueue[0] = msg;
      post uartSendTask();
     }
	 call Leds.led0Toggle();
      return ret;
  }

  uint8_t tmpLen;
  
  task void uartSendTask() {
    uint8_t len;
    am_id_t id;
    am_addr_t addr, src;
    message_t* msg;
    atomic
    msg = uartQueue[0];
    tmpLen = len = call RadioPacket.payloadLength(msg);
    id = call RadioAMPacket.type(msg);
    addr = call RadioAMPacket.destination(msg);
    src = call RadioAMPacket.source(msg);
    call UartPacket.clear(msg);
    call UartAMPacket.setSource(msg, src);
    if (call UartSend.send[id](addr, uartQueue[0], len) == SUCCESS){}
  }

  event void UartSend.sendDone[am_id_t id](message_t* msg, error_t error) {
    if (error != SUCCESS){}
      
  }

  event message_t *UartReceive.receive[am_id_t id](message_t *msg,void *payload,uint8_t len) {
	uint8_t *inptr,*outptr;
	message_t *ret = msg;
	call Leds.led1Toggle();
   	inptr = (uint8_t*)call RadioPacket.getPayload(msg, sizeof(myMsg));
	outptr = (uint8_t*)call RadioPacket.getPayload(&mymsg, sizeof(myMsg)+inptr[4]);
	call Leds.set(0);
	call Timer0.startOneShot(100);
    return ret;
  }

  
  event void RadioSend.sendDone[am_id_t id](message_t* msg, error_t error) {
  }

  event void Timer0.fired() {
  }
}  
