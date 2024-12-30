import java.util.*;
public class teja{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int last = n%10;
        int first  = n;

        while(n>=10){
            n = n/10;
            
        }
        first  =n;
        System.out.print(last+first);

    }
}