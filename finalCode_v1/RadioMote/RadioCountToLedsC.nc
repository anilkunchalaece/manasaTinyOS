#include "Timer.h"
#include "RadioCountToLeds.h"
#include "string.h"
#include "stdio.h" 


module RadioCountToLedsC @safe() {
  uses {
    interface Leds;
    interface Boot;
    interface Receive;
    interface AMSend;
    interface Timer<TMilli> as MilliTimer;
    interface SplitControl as AMControl;
    interface Packet;
    interface Read<uint16_t> as TempReader;
    interface Read<uint16_t> as LightReader;
    interface Read<uint16_t> as HumiReader;
  }
}

implementation {

  message_t packet;

  bool locked;
  uint16_t counter = 0;
  uint16_t current_temp;
  uint16_t current_light;
  uint16_t current_humi;  

  event void Boot.booted() {
    call AMControl.start();
  }

  event void AMControl.startDone(error_t err) {
    if (err == SUCCESS) {
      call MilliTimer.startPeriodic(250);
    }
    else {
      call AMControl.start();
    }
  }

  event void AMControl.stopDone(error_t err) {
    // do nothing
  }


event void TempReader.readDone(error_t result, uint16_t val){
	if(result == SUCCESS){
	current_temp = val;
	}

  //temp = -39.6 + (0.04 * val)
}


event void LightReader.readDone(error_t result, uint16_t val){
  if(result == SUCCESS){
  current_light = val
  }

  // lumi = 2.5 * (val/4096.0)*6250.0
}


 event void HumiReader.readDone(error_t result, uint16_t val){
  if(result == SUCCESS){
      current_humi = val;
  }
  //humi =  -2.0468 +  (0.0367 * val) +  ((-1.5955/100000) * val * val)
  //ref : https://www.advanticsys.com/wiki/index.php?title=Sensirion%C2%AE_SHT11
 }
  
  event void MilliTimer.fired() {
   call TempReader.read();
   call LightReader.read();
   call HumiReader.read();

    counter++;
    dbg("RadioCountToLedsC", "RadioCountToLedsC: timer fired, counter is %hu.\n", counter);
    if (locked) {
      return;
    }
    else {
      radio_count_msg_t* rcm = (radio_count_msg_t*)call Packet.getPayload(&packet, sizeof(radio_count_msg_t));
      if (rcm == NULL) {
	return;
      }
      rcm->nodeId = (uint8_t)1;
      rcm->counter = counter;
      rcm->temp = current_temp;
      rcm->humi = current_humi;
      rcm->light = current_light;

      if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
	locked = TRUE;
      }
    }
  }

  event message_t* Receive.receive(message_t* bufPtr, 
				   void* payload, uint8_t len) {
    dbg("RadioCountToLedsC", "Received packet of length %hhu.\n", len);
    if (len != sizeof(radio_count_msg_t)) {return bufPtr;}
    else {
      radio_count_msg_t* rcm = (radio_count_msg_t*)payload;
	     //printf("received msg is %u",rcm->counter);
      return bufPtr;
    }
  }

  event void AMSend.sendDone(message_t* bufPtr, error_t error) {
    if (&packet == bufPtr) {
      locked = FALSE;
    }
  }

}




