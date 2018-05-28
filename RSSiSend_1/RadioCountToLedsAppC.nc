#include "RadioCountToLeds.h"

configuration RadioCountToLedsAppC {}
implementation {
  components MainC, RadioCountToLedsC as App, LedsC;
  components new AMSenderC(AM_RADIO_COUNT_MSG);
  components new AMReceiverC(AM_RADIO_COUNT_MSG);
  components new TimerMilliC();
  components ActiveMessageC;
  components SerialPrintfC;
  //components new DemoSensorC() as Sensor;
  components new TimerMilliC() as T1;
  components new TimerMilliC() as T3;
  components new AMSenderC(AM_RSSIMSG) as RssiMsgSender;
  
  components CC2420ControlC;

  App.Boot -> MainC.Boot;
  
  App.Receive -> AMReceiverC;
  App.AMSend -> AMSenderC;
  App.AMControl -> ActiveMessageC;
  App.Leds -> LedsC;
  App.MilliTimer -> TimerMilliC;
  App.Packet -> AMSenderC;
  
  TestRssiC.ReadRssi -> CC2420ControlC.ReadRssi;

}


