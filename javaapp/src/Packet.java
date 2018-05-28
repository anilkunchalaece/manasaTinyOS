/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */


import java.util.Calendar;

/**
 *
 * @author acer
 */

public class Packet {       //the packet class
public byte type;
public byte sender;
public int data;
public int temp;

public static byte HELLO=1;
public static byte NGB=2;
public Packet(){}
public Packet(byte type,byte sender,int data,int temp){
    this.type=type;
    this.sender=sender;
    this.data=data;
    this.temp=temp;
}
public String toString(){    //conver the packet data values to string
    String s;
    s="Type:"+type+"   Sender:"+sender+"   Data:"+data+"  Temp:"+temp;
    return s;
}

}

