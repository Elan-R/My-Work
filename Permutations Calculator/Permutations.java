/*
 * All permutations of a set
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class Permutations implements Iterable<Object[]> {

    Object[] set;
    int pick;
    int[] indexes;

    public Permutations(Object[] set, int pick) {
        this.set = set;
        this.pick = pick;
        indexes = new int[pick];
        reset();
    }

    // Resets the index array that keeps track of the next permutation
    public void reset() {
        for (int i = 0; i < pick; i++) {
            indexes[i] = 0;
        }
    }

    // Creates a permutation from a given array of indexes
    private Object[] create_perm(int[] indxs) {
        Object[] perm = new Object[pick];
        ArrayList<Object> temp_array = new ArrayList<>(Arrays.asList(set));
        for (int i = 0; i < pick; i++) {
            perm[i] = temp_array.remove(indxs[i]);
        }
        return perm;
    }

    // Creates the current permutation and updates the index array for the next permutation
    public Object[] next() {
        Object[] perm = create_perm(indexes);
        int value;
        for (int i = 0; i < pick; i++) {
            if ((value = indexes[pick - i - 1] + 1) <= set.length - pick + i) {
                indexes[pick - i - 1] = value;
                break;
            } else {
                indexes[pick - i - 1] = 0;
            }
        }
        return perm;
    }

    // Generates a set of indexes based on an integer index
    private int[] gen_indexes(int index) {
        int x = index;
        for (int i = 1; i < pick; i++) {
            x += (Math.pow(10, i) - (i + set.length - pick) * Math.pow(10, i - 1)) * Math.floor(index / (double) (factorial(i + set.length - pick) / Math.round(set.length / (double) pick))); //(set.length - pick ? 0 : 1)
        }

        int[] indxs = new int[pick];
        for (int i = pick - 1; i >= 0; i--) {
            indxs[i] = x - (x = x / 10) * 10;
        }
        return indxs;
    }

    // Creates a permutation based on an index
    public Object[] permutation_at(int index) {
        return create_perm(gen_indexes(index));
    }

    // Sets the next indexes to indexes created by an integer index
    public void set_next(int index) {
        indexes = gen_indexes(index);
    }

    // Creates a random permutation
    public Object[] random() {
        int[] rand_indexes = new int[indexes.length];
        for (int i = 0; i < pick; i++) {
            rand_indexes[i] = (int) ((set.length - i) * Math.random());
        }
        return create_perm(rand_indexes);
    }

    // Iterator class to iterate over all permutations
    public class PermutationsIterable implements Iterator<Object[]> {

        Permutations perms;
        int counter;
        int size;

        public PermutationsIterable() {
            perms = new Permutations(Permutations.this.set, Permutations.this.pick);
            counter = 1;
            size = factorial(perms.set.length) / factorial(perms.set.length - perms.pick);
        }

        @Override
        public boolean hasNext() {
            return counter <= size;
        }

        @Override
        public Object[] next() {
            counter++;
            return perms.next();
        }
    }

    @Override
    public Iterator<Object[]> iterator() {
        return new PermutationsIterable();
    }

    // Finds the factorial of an integer (returns 1 for negative values)
    public static int factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    public static void main(String[] args) {
        Permutations p = new Permutations(new Integer[] {1, 2, 3, 4, 5}, 3);

        System.out.println("\nPermutations one by one:");
        System.out.println(Arrays.toString(p.next()));
        System.out.println(Arrays.toString(p.next()));
        System.out.println(Arrays.toString(p.next()));
        p.reset();

        System.out.println("\nPermutations one by one after calling reset:");
        System.out.println(Arrays.toString(p.next()));
        System.out.println(Arrays.toString(p.next()));

        System.out.println("\nRandom permutations:");
        System.out.println(Arrays.toString(p.random()));
        System.out.println(Arrays.toString(p.random()));

        System.out.println("\nFactorial of -1 and 5:");
        System.out.println(Permutations.factorial(-1));
        System.out.println(Permutations.factorial(5));

        System.out.println("\nIterating over all permutations with a for loop:");
        long time = System.currentTimeMillis();
        for (Object[] obj : p) {
            System.out.println(Arrays.toString(obj));
        }
        time = System.currentTimeMillis() - time;
        System.out.println("\n" + (factorial(p.set.length) / factorial(p.set.length - p.pick))+ " permutations found and printed in seconds: " + time / 1000.0);

        System.out.println("\nPermutations by index:");
        int size = factorial(p.set.length) / factorial(p.set.length - p.pick);
        time = System.currentTimeMillis();
        for (int i = 0; i < size; i++) {
            System.out.println(Arrays.toString(p.permutation_at(i)));
        }
        time = System.currentTimeMillis() - time;
        System.out.println("\n" + (factorial(p.set.length) / factorial(p.set.length - p.pick))+ " permutations found and printed in seconds: " + time / 1000.0);
    }
}
