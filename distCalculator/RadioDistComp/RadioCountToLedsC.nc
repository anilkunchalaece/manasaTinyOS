
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
    interface SplitControl as AMControl;
    interface Packet;
  }
}
implementation {

  message_t packet;

  bool locked;
  uint16_t counter = 0;

  event void Boot.booted() {
    call AMControl.start();
  }

  event void AMControl.startDone(error_t err) {
    if (err == SUCCESS) {
      call MilliTimer.startPeriodic(10);
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
    printf("the counter value is %u ",counter);
	//call Leds.led0Toggle();
	//call Leds.led1Toggle();
    return bufPtr;
    }
  }

  event void AMSend.sendDone(message_t* bufPtr, error_t error) {
    if (&packet == bufPtr) {
      locked = FALSE;
    }
  }

}


  event void MilliTimer.fired() {

    counter = counter + 1;

if(counter == 10){

    if (locked) {
      return;
    }
    else {
      radio_count_msg_t* rcm = (radio_count_msg_t*)call Packet.getPayload(&packet, sizeof(radio_count_msg_t));
      if (rcm == NULL) {
  return;
      }
      rcm->nodeId = (uint8_t)1;
      if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
  locked = TRUE;
      }
    }

    }//end of if counter
  }

