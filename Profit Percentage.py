import java.util.*;
public class Suraj{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int X=sc.nextInt();
        int Y=sc.nextInt();
        double profit = Y - X;
        double p=(profit/X)*100.00;
        System.out.printf("%.2f",p);
    }
}