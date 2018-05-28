

import java.io.*;
import java.nio.ByteBuffer;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import net.tinyos.packet.*;
import net.tinyos.util.*;
import net.tinyos.message.*;
import java.util.Timer;

public class PortListener extends Thread {       //this class listen to serial port to get the recived packets

    private PacketSource reader;
    private Frame1 window;
    public static final int AM_TYPE = 6;
    public int rcount;
    MyTask mt;
    Calendar cal;
    public static long lastBTime;
    long STime;

    public PortListener(Frame1 frm, String[] args) {      //create required objects
        window = frm;
        String source = null;
        rcount = 0;
        lastBTime = 0;
        try {
            if (args.length == 2 && args[0].equals("-comm")) {
                source = args[1];
            } else if (args.length > 0) { //check the required parameter count for class
                System.err.println("usage: java net.tinyos.tools.Listen [-comm PACKETSOURCE]");
                System.err.println("(default packet source from MOTECOM environment variable)");
                System.exit(2);
            }
            if (source == null) {
                reader = BuildSource.makePacketSource();  //create a packet reader object
            } else {
                reader = BuildSource.makePacketSource(source);
            }


            if (reader == null) {       //show error message if we can not create  reader object
                System.err.println("Invalid packet source (check your MOTECOM environment variable)");
                System.exit(2);
            }
            reader.open(PrintStreamMessenger.err);
            window.display("Port Opened. Waiting for incoming packets..");
            STime = Calendar.getInstance().getTimeInMillis();
        } catch (Exception ex) {
            window.display(ex.toString());
        }

    }

    public void Close() {        //terminate the thread on closing the window
        try {
            this.stop();
            reader.close();
        } catch (IOException ex) {
            window.display(ex.toString());
        }
    }

    @Override
    public void run() {     //the main thread function
        mt = new MyTask(this);
        Timer timer = new Timer();
        timer.schedule(mt, 1000); //set the rcount flag after 1000 ms
        try {
            Packet p = new Packet();
            while (true) {     //an infinit loop for reading packets
                byte[] packet = reader.readPacket();    //read next incoming packet.
                if (rcount == 1) {  //ignore all recived packets in first 1 second
                    p = generatePacket(packet);  //create packet from recived bytes
                        window.display("[RECV]  " + bytesToHex(packet));
                        window.display("[RECV]  " + p.toString());
                    window.processMessage(p); //send packet to proccessMessage function to update tables
                }
            }
        } catch (Exception e) {
            window.display(e.toString());
        }
    }

    private String bytesToHex(byte[] bytes) { //conver a hex value from byte type to string type
        final char[] hexArray = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
        char[] hexChars = new char[bytes.length * 2];
        int v;
        for (int j = 0; j < bytes.length; j++) {
            v = bytes[j] & 0xFF;
            hexChars[j * 2] = hexArray[v >>> 4];
            hexChars[j * 2 + 1] = hexArray[v & 0x0F];
        }
        return new String(hexChars);
    }

    private Packet generatePacket(byte[] pk) {    //extract the value of fields of packet according to byte address
        int i;
        String p = bytesToHex(pk);    //convert recived bytes to string
        Packet pkt = new Packet();    //create a packet
        // pkt.size=(byte)pk.length;         //set the packet length
        pkt.type = (byte) Integer.parseInt(p.substring(16, 18), 16); //bytes 16-18 are type of packets
        pkt.sender = (byte) Integer.parseInt(p.substring(18, 20), 16);
        pkt.data =  Integer.parseInt(p.substring(20, 24), 16);
        pkt.temp =  Integer.parseInt(p.substring(24, 28), 16);
        return (pkt);
    }
}
