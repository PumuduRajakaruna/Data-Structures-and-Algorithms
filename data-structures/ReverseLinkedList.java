package LinkedList;

import java.util.Stack;

class Node {
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = null;
    }

}

public class LinkedList{

    public static Node reverse(Node head){
        Node previous = null;
        Node current = head;
        Node next = null;

        while(current != null){
             next = current.next;
             current.next = previous;
             previous = current;
             current = next;
        }
        head = previous;
        return head;
    }

    public static Node reverse_stack(Node head){
        Node current = head;
        Stack<Node> stack = new Stack<>();
        while(current.next != null){
             stack.add(current);
             current = current.next;
        }
        head = current;
        while(!stack.isEmpty()){
            current.next = stack.peek();
            stack.pop();
            current = current.next;
        }
        current.next = null;
        return head;
    }

    public static void printList(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Creating a sample list: 1 -> 2 -> 3 -> 4 -> 5
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

        System.out.println("Original List:");
        printList(head);

        head = reverse_stack(head);

        System.out.println("Reversed List:");
        printList(head);
    }
}
