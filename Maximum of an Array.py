import java.util.*;
public class teja{
    public static void main(String[]  args){
        Scanner sc = new Scanner(System.in);
        int maxvalue = Integer.MIN_VALUE;
        int a = sc.nextInt();
        int[] b=new int[a];
        for(int i=0; i<a; i++){
            b[i] =sc.nextInt();
        } 

        for(int i=0; i<b.length; i++){
            if(b[i] > maxvalue ){
               maxvalue = b[i]; 
            }
        }
        System.out.print(maxvalue);
    }
} 