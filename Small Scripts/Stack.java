/*
 * General purpose stack
 */

public class Stack<T> {

    private class Item {

        Item next = null;
        T value;

        public Item(T val) {
            value = val;
        }
    }

    private Item top = null;

    public void push(T value) {
        Item item = new Item(value);
        item.next = top;
        top = item;
    }

    public T pop() {
        if (top == null) {
            return null;
        }
        T ret = top.value;
        top = top.next;
        return ret;
    }
}
