/*
 * Implement a queue using 2 stacks
 */

public class QueueOfTwoStacksFastPush<T> {

    private final Stack<T> put;
    private final Stack<T> take;

    public QueueOfTwoStacksFastPush() {
        put = new Stack<T>();
        take = new Stack<T>();
    }

    public void push(T value) {
        put.push(value);
    }

    public T pop() {
        T temp;
        while ((temp = put.pop()) != null) {
            take.push(temp);
        }
        T ret = take.pop();
        while ((temp = take.pop()) != null) {
            put.push(temp);
        }
        return ret;
    }

    public static void main(String[] args) {
        QueueOfTwoStacksFastPush<String> q = new QueueOfTwoStacksFastPush<String>();
        q.push("Hello, ");
        q.push("world!");
        System.out.print(q.pop());
        q.push(" What day is it?");
        System.out.print(q.pop());
        System.out.print(q.pop());
        System.out.flush();
    }
}
