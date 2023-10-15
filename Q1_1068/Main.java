/*
 * Name = PRABHUPADA MISHRA
 * Regd. No. = 2241013159
 * Problem statement = https://cses.fi/problemset/task/1068
 */

 import java.util.Scanner;

 class Main{
 
     public static void main(String[] args) {
 
         Scanner sc = new Scanner(System.in);
         long n = sc.nextLong();
 
         while (n>1) {
             System.out.print(n+" ");
 
             if(n%2==1) n=(n*3)+1;
             else n=n/2;
 
         }
         System.out.println("1");
         sc.close();
     }
 
 }