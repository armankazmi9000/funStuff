// This is a program I made for fun!!

import java.util.Scanner; 

public class FunProject 
{
    public static void main(String[] args) 
    {
    System.out.println("Pythagorean Theorem!");
    System.out.println("");
    
    Scanner A = new Scanner(System.in); 
    System.out.print("Enter your A value: ");
    Double a = A.nextDouble(); 
    Scanner B = new Scanner(System.in); 
    System.out.print("Enter your B value: ");
    Double b = B.nextDouble(); 
    
    Double aSquared = Math.pow(a,2);
    Double bSquared = Math.pow(b,2);
    Double cSquared = aSquared + bSquared;
    
    Double c = Math.sqrt(cSquared);
    
    System.out.println("");
    System.out.println("C is = " + c);  
    
    }//end of main
    
}//end of FirstJava
