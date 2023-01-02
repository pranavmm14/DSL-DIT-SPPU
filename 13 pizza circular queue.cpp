#include <iostream>
#define size 5
using namespace std;

class PizzaQueueCircular
{
private:
    int arr[size];
    int front, rear;

public:
    PizzaQueueCircular()
    {   
        front = rear = -1;
    };
    void enqueueCircular(int element)
    {
        // check if full
        if (rear == (front - 1) % (size - 1) || (front == 0) && (rear == size - 1)){
            element--;
            cout << "Queue is full! :c\n";
        }
        else if (front == -1)
        {
            front = rear = 0;
            cout <<"Front" << front <<endl;
            arr[rear] = element;
            cout << "Order ID is: " << element <<endl ;
        }
        else if (rear == size - 1 && front != 0)
        {
            rear = 0;
            arr[rear] = element;
            cout << "Order ID is: " << element <<endl ;
        }
        else
        {
            rear++;
            arr[rear] = element;
            cout << "Order placed\nOrder ID is: " << element <<endl ;
        }
    }

    bool isEmpty()
    {
        if (front == -1)
            return 1;
        else
            return 0;
    }
    void dequeueCircular()
    {
        if (isEmpty())
            cout << "Queue is empty can't Dequeue!\n";
        else if (front == rear)
        {
            cout << "Order " << arr[front] << " is served!\n";
            front = rear = -1;
        }
        else if (front == size - 1)
        {
            cout << "Order " << arr[front] << " is served!\n";
            front = 0;
        }
        else
        {
            cout << "Order " << arr[front] << " is served!\n";
            front++;
        }
    }

    void displayQueue()
    {
        int i = front;
        for (i = front; i != rear; i=((i+1) % size))
        {
            cout << arr[i] << ", ";
        }
        cout << arr[rear] << endl;
    }
};

int main()
{
    PizzaQueueCircular palace;
    int orderID = 0;
    while (1)
    {
        int ch;
        cout << "1. Order\n2. Serve\n3. Display\n4. Exit\nEnter Your choice: ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            orderID++;
            palace.enqueueCircular(orderID);
            // palace.displayQueue();
            break;
        case 2:
            palace.dequeueCircular();
            break;
        
        case 3:
            palace.displayQueue();
            break;
        
        case 4:
            cout << "\nThanks for using the program. \nProgram by Pranav Mehendale\n";
            exit(1);

        default:
            break;
        }
    }
}
