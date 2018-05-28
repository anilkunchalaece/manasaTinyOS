

import java.net.*;
import java.nio.channels.*;
import javax.swing.JLabel;
import javax.swing.JTextArea;


public class netAccepter extends Thread{
   public InetAddress localAddress; 
   protected ServerSocketChannel serverChannel;
   private int port; 
   private SocketChannel webClient;
   JTextArea output;
    public netAccepter(int prt,JTextArea o){
        try{
            localAddress=InetAddress.getLocalHost();  
            port=prt;
            serverChannel= ServerSocketChannel.open(); 
            serverChannel.configureBlocking(true);  
            serverChannel.socket().bind(new InetSocketAddress(localAddress,port));
            System.out.println("Waiting for connection at "+localAddress.toString()+" #"+port);
            webClient=null;
            output=o;
        }
        catch(Exception e){
              System.out.println("Can not open Server Channel or Binding Error!  "+e.toString());
        }
    }
    public void run(){
        try{
            while(true){
             webClient=serverChannel.accept();
             webClient.socket().setTcpNoDelay(true);
             output.append("Web Client Connected.\n");

            }
        }
        catch(Exception e){
        System.out.println("Error in Accepting !"+e.toString());
        }
    }
    public void send(String msg)
    {
        try{
        if(webClient==null)return;
        if(webClient.isConnected()==false) {webClient=null; return;}
         webClient.socket().getOutputStream().write(msg.getBytes());
         output.append(msg+"\n");
        }
        catch(Exception ex){
            ex.printStackTrace();
        }
    }
}
