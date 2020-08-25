import java.io.*;
import java.net.*;
import java.lang.*;

class Findcosine {
    public static void main(String args[]) throws Exception {
        ServerSocket server = new ServerSocket(8080);
        boolean run = true;
        String sen;
        double rad,outp;
        int deg;

        while(run) {
            Socket sock = server.accept();
            BufferedReader din = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            PrintWriter dout = new PrintWriter(sock.getOutputStream(),true);
            System.out.println("Waiting for angle input...");
            deg = Integer.parseInt(din.readLine());
            outp=Math.cos(Math.toRadians(deg));
            System.out.println("Cosine of "+deg+" degrees is: "+outp);

            dout.println(outp);
            sock.close();
            run = false;
            System.out.println("Back to python");
        }
        System.exit(0);
    }
}
