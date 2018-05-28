
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
	  printf("t%u h%u l%u i%u \n ",rcm->temp,rcm->humi,rcm->light,rcm->nodeId);
	call Leds.led0Toggle();
	call Leds.led1Toggle();
    return bufPtr;
    }
  }

  event void AMSend.sendDone(message_t* bufPtr, error_t error) {
    if (&packet == bufPtr) {
      locked = FALSE;
    }
  }

}




