import java.util.*;
public class teha{
 public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
 if(isPrime(n)){
    System.out.print("Prime");
 }
 else{
    System.out.print("Not Prime");
 }


 }
 public static boolean isPrime(int n ){
    if(n<=1){
        return false;
    }
    for(int i=2; i<Math.sqrt(n); i++){
        if(n%i == 0){
            return false;
        }
    }
    return true;
 }


}