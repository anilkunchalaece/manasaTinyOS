/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */


import java.util.TimerTask;
/**
 *
 * @author vaio
 */
 
class MyTask extends TimerTask {        //a class to set a flag of portlsitener after some delay
    
    PortListener pl;
   public MyTask(PortListener p){
       pl=p;
   }
     public void run() {
        pl.rcount=1;            //set the rcount flag to 1 after some delay
    }
}