/*
 * Implement a queue using 2 stacks
 */

public class QueueOfTwoStacksFastPop<T> {

    private final Stack<T> put;
    private final Stack<T> take;

    public QueueOfTwoStacksFastPop() {
        put = new Stack<T>();
        take = new Stack<T>();
    }

    public void push(T value) {
        T temp;
        while ((temp = take.pop()) != null) {
            put.push(temp);
        }
        put.push(value);
        while ((temp = put.pop()) != null) {
            take.push(temp);
        }
    }

    public T pop() {
        return take.pop();
    }

    public static void main(String[] args) {
        QueueOfTwoStacksFastPop<String> q = new QueueOfTwoStacksFastPop<String>();
        q.push("Hello, ");
        q.push("world!");
        System.out.print(q.pop());
        q.push(" What day is it?");
        System.out.print(q.pop());
        System.out.print(q.pop());
        System.out.flush();
    }
}
