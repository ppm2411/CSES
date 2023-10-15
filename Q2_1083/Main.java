/*
 * Name = PRABHUPADA MISHRA
 * Regd. No. = 2241013159
 * Problem statement = https://cses.fi/problemset/task/1083
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int expectedXOR = 0;
        
        for (int i = 1; i <= n; i++) {
            expectedXOR ^= i;
        }
        
        int actualXOR = 0;
        for (int i = 1; i < n; i++) {
            int a = sc.nextInt();
            actualXOR ^= a;
        }
        
        int missingNumber = expectedXOR ^ actualXOR;
        System.out.println(missingNumber);
        sc.close();
    }
}