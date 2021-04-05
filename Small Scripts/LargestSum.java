/*
 * For a given array of integers (positive and negative) find the largest sum of a contiguous sequence
 */

import java.util.Arrays;

public class LargestSum {

    public static int find(int[] array) {
        int largest = Integer.MIN_VALUE;
        int sum = 0;
        int buffer = 0;
        int greatest_neg = Integer.MIN_VALUE;
        boolean sum_changed = false;
        for (int x : array) {
            if (buffer != 0 || x < 0) {
                if (x < 0 && x > greatest_neg) {
                    greatest_neg = x;
                }
                buffer += x;
                if (buffer > 0) {
                    sum += buffer;
                    buffer = 0;
                } else if (sum + buffer <= 0) {
                    sum = 0;
                    buffer = 0;
                }
            } else {
                sum += x;
                sum_changed = true;
            }
            if (sum > largest && sum_changed) {
                largest = sum;
            }
        }
        return Math.max(greatest_neg, largest);
    }

    public static void main(String[] args) throws Exception {
        int[][] testCases = {
                {1,1,1,-2,-1,1,1,1,1,1}, // 5
                {1,1,1,-2,-1,1,1,0,1,1,-1}, // 4
                {-8,-3,-2,-1,-6}, // -1
                {-8,-3,-2,0,-1,-6}, // 0
                {0,-8,-3,-2,-1,-6}, // 0
                {-8,-3,-2,-1,-6,0}, // 0
                {1,2,3,-4,-1,0,1,1,1,1}, // 6
                {99,-1,99}, // 197
                {99,-1,99,-1000,2000}, // 2000
                {-1000,2000,99,-1,99}, // 2197
                {100,-3,1,-2,-1,99,0,-1,-1,3}, // 195
                {99,0,-1,-1,3,100,-3,1,-2,-1}, // 200
                {100,-3,1,-2,-1000,99,0,-1,-1,3}, // 100
                {99,0,-1,-1,3,100,-3,1,-2,-1000}, // 200
                {100,-3,1,3,-1000,99,0,-1,-1,3}, // 101
                {99,-1,99,-1000,2000,1000}, // 3000
                {99,-1,99,-1000,2000,1000, -1, -1000}, // 3000
                {99,-1,99,-1000,2000,1000, -1, -1, 3}, // 3001
        };
        int[] expectedResults = {5,4,-1,0,0,0,6, 197, 2000, 2197, 195, 200, 100, 200, 101, 3000, 3000, 3001};

        int actualResult;
        for (int i = 0; i < testCases.length; i++) {
            actualResult = LargestSum.find(testCases[i]);

            if (actualResult == expectedResults[i]) {
                System.out.println("Array: " + Arrays.toString(testCases[i]) + " Expected: " + expectedResults[i] + " Actual Result: " + actualResult + " Test PASSED");
            } else {
                System.err.println("Array: " + Arrays.toString(testCases[i]) + " Expected: " + expectedResults[i] + " Actual Result: " + actualResult + " Test FAILED\n");
            }
        }
    }
}
