#include "Timer.h"
#include "string.h"
#include "stdio.h"
//---------------------------------------------------------
#define HELLO (uint8_t)1
typedef nx_struct MESSAGE {
  nx_uint8_t type;
  nx_uint8_t sender;
  nx_uint16_t data;
  nx_uint16_t temp;
} MESSAGE_t;

 module Mote @safe() {
  uses {
    interface Leds;
    interface Boot;
    interface Receive;
    interface AMSend;
	interface Timer<TMilli> as BroadCastTimer;
    interface SplitControl as AMControl;
    interface Packet;
	interface Random;
	interface Timer<TMilli> as Sender;
	interface Read<uint16_t> as TempReader;
  }
}

implementation {
  bool radioBusy;
  message_t neighbor_list_packet;
  message_t out_packet;
  uint16_t current_temp;

//---------------------------------------------------------------------------
  event void Boot.booted() {
	call Leds.set(1);
	call AMControl.start();
  }


//------------------------------------------------------------------------------
  event void AMControl.startDone(error_t err) {
      if (err != SUCCESS)  call AMControl.start();
	     call Leds.set(0);
	     call BroadCastTimer.startPeriodic(1000);
  }

//----------------------------------------
event message_t* Receive.receive(message_t* bufPtr,void* pkt, uint8_t len) {
	return bufPtr;
  }

//-----------------------------------------
event void TempReader.readDone(error_t result, uint16_t val){
	if (result == SUCCESS){
		current_temp=  val;
    printf("current temp is : %d \r\n",current_temp);
    }
	 else 
   {
   call Leds.set(0);
   }
  }

 //---------------------------------------------------------------------------
void send(uint8_t typ,uint16_t Data,uint8_t sender){
    MESSAGE_t* out_msg = (MESSAGE_t*)call Packet.getPayload(&out_packet, sizeof(MESSAGE_t));
    out_msg->type=typ;
    out_msg->sender=sender;
	out_msg->data=Data;
	out_msg->temp=0;
	call Sender.startOneShot(call Random.rand16()%500);
}
//---------------------------------------------------------------------------
event void BroadCastTimer.fired() {

	call TempReader.read();
	send(HELLO,current_temp,TOS_NODE_ID);
}

 //------------------------------------------------------------------------------
 event void Sender.fired() {
	if(radioBusy==TRUE){
		return;
	}
    if (call AMSend.send(AM_BROADCAST_ADDR, &out_packet, sizeof(MESSAGE_t)) == SUCCESS) {
	     radioBusy = TRUE;
		 call Leds.led0Toggle();
	}
  }

//-------------------------------------------------------------------------------------
  event void AMControl.stopDone(error_t err) { }
  event void AMSend.sendDone(message_t* bufPtr, error_t error){radioBusy = FALSE;}
}
