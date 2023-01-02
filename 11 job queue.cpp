//11. Queues are frequently used in computer programming, and a typical example is the creation of a job queue\
by an operating system. If the operating system does not use priorities, then the jobs are processed in the order\
they enter the system. Write C++ program for simulating job queue. Write functions to add job and delete job from queue.

#include <iostream>
#include <string.h>
using namespace std;

class Job_Queue
{
private:
    string *arr;
    int front, rear;
    int size;

public:
    Job_Queue();
    // ~Job_Queue();
    void enqueue(string);
    void dequeue();
    bool isEmpty();
    string qfront();
};

Job_Queue::Job_Queue()
{
    size = 100;
    arr = new string[size];
    front = rear = 0;
}

void Job_Queue::enqueue(string job)
{
    if (rear == size)
    {
        cout << "Queue is full! :(";
    }

    arr[rear] = job;
    rear++;
}

void Job_Queue::dequeue()
{
    if (front == rear)
        cout << "Queue is empty!\n";

    arr[front] = -1;
    front++;

    if (front == rear)
        front = rear = 0;
}

bool Job_Queue::isEmpty()
{
    if (front == rear)
        return 1;
    else
        return 0;
}

string Job_Queue::qfront()
{
    return arr[front];
}

int main()
{

    Job_Queue j1;
    j1.enqueue("Task 1");
    j1.enqueue("Task 2");
    j1.enqueue("Task 3");

    cout << j1.qfront() << endl;

    j1.dequeue();

    cout << j1.qfront() << endl;

    cout << "\nThanks for using the program. \nProgram by Pranav Mehendale\n";
    return 0;
}