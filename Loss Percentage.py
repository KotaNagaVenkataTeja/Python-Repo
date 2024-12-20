import java.util.*;
public class teja
{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        float sp = sc.nextFloat();
        float cp = sc.nextFloat();
        double loss = ((sp - cp)/sp)*100;
        System.out.printf("%.2f", loss);
        }
}