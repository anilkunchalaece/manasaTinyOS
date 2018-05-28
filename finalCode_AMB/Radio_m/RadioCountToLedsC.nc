
#include "Timer.h"
#include "RadioCountToLeds.h"
#include "string.h"
#include "stdio.h" 

#define AliceNodeId 1
#define mNodeId 2

module RadioCountToLedsC @safe() {
  uses {
    interface Leds;
    interface Boot;
    interface Receive;
    interface AMSend;
    interface SplitControl as AMControl;
    interface Packet;
  }
}
implementation {

  message_t packet;

  bool locked;
  uint16_t counter = 0;
  uint16_t current_temp;  

  event void Boot.booted() {
    call AMControl.start();
  }

  event void AMControl.startDone(error_t err) {
    if (err == SUCCESS) {
      //call MilliTimer.startPeriodic(250);
    }
    else {
      call AMControl.start();
    }
  }

  event void AMControl.stopDone(error_t err) {
    // do nothing
  }
  
  event message_t* Receive.receive(message_t* bufPtr, void* payload, uint8_t len) {

    if (len != sizeof(radio_count_msg_t)) 
    {
    return bufPtr;
    }
    else 
    {
    radio_count_msg_t* rcm = (radio_count_msg_t*)payload;
	  //printf("t %u t%u l%u i%u \n ",rcm->temp,rcm->humi,rcm->light,rcm->nodeId);

    if (locked) {
      return rcm;
    }
    else {
      radio_count_msg_t* rcmS = (radio_count_msg_t*)call Packet.getPayload(&packet, sizeof(radio_count_msg_t));
      if (rcmS == NULL) {
        return rcmS;
	}
      call Leds.led2Toggle();
      call Leds.led1Toggle();
      call Leds.led0Toggle();
	
      rcmS->nodeId = (uint8_t)mNodeId;
      rcmS->temp = rcm->temp;
      rcmS->humi = rcm->humi;
      rcmS->light = rcm->light;

     if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
        locked = TRUE;
      }


}

    return bufPtr;
    }
  }

  event void AMSend.sendDone(message_t* bufPtr, error_t error) {
    if (&packet == bufPtr) {
      locked = FALSE;
    }
  }

}




