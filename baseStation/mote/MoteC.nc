configuration MoteC {}
implementation {
  components MainC,Mote as App, LedsC,RandomC;
  components new DemoSensorC() as Sensor;
  components new AMSenderC(6);
  components new AMReceiverC(6);
  components new TimerMilliC() as T1;
  components new TimerMilliC() as T3;
  components ActiveMessageC;
  components SerialPrintfC;

  App.Boot -> MainC.Boot;
  App.Receive -> AMReceiverC;
  App.AMSend -> AMSenderC;
  App.AMControl -> ActiveMessageC;
  App.Leds -> LedsC;
  App.Packet -> AMSenderC;
  App.BroadCastTimer->T1;
  App.Sender->T3;
  App.Random->RandomC;
  App.TempReader->Sensor;
}


