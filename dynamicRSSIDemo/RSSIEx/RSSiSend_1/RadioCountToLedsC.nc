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
    interface Read<uint16_t> as ReadRssi;
  }
}

implementation {

  message_t packet;
  uint16_t rrsiVal = 100;

  bool locked;

  event void Boot.booted() {
    call AMControl.start();
  }

event void ReadRssi.readDone(error_t ok, uint16_t val ){
if (ok == SUCCESS ) {
  rssiVal = val;
}
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

  event void MilliTimer.fired() {
   call Leds.led0Toggle()
    if (locked) {
      return;
    }
    else {
      radio_count_msg_t* rcm = (radio_count_msg_t*)call Packet.getPayload(&packet, sizeof(radio_count_msg_t));
      if (rcm == NULL) {
	return;
      }
      rcm->OrgNodeId = (uint8_t)1;
      rcm->RSSI = rssiVal;

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
     call ReadRssi.read(bufPtr)
    }
  }

  event void AMSend.sendDone(message_t* bufPtr, error_t error) {
    if (&packet == bufPtr) {
      locked = FALSE;
    }
  }

}




