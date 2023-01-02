// 10.  In any language program mostly syntax error occurs due to unbalancing delimiter such as (),{},[].\
Write C++ program using stack to check whether given expression is well parenthesized or not.

#include <iostream>
#include <stack>
using namespace std;

bool areParanthesisBalanced(string expr)
{
    stack<char> s;
    char x;

    // Traversing the Expression
    for (int i = 0; i < expr.length(); i++)
    {
        if (expr[i] == '(' || expr[i] == '[' || expr[i] == '{')
        {
            // Push the element in the stack
            s.push(expr[i]);
            continue;
        }

        // IF current current character is not opening bracket, then it must be closing. So stack\
        cannot be empty at this point.

        if (s.empty()){
            if( ( (int)expr[i] >= 97 && (int)expr[i] <=122 ) || ( (int)expr[i] >= 65 && (int)expr[i] <=90 )){
                continue;
            }
            return false;
        }

        switch (expr[i])
        {
        case ')':

            // Store the top element in a
            x = s.top();
            s.pop();
            if (x == '{' || x == '[')
                return false;
            break;

        case '}':

            // Store the top element in b
            x = s.top();
            s.pop();
            if (x == '(' || x == '[')
                return false;
            break;

        case ']':

            // Store the top element in c
            x = s.top();
            s.pop();
            if (x == '(' || x == '{')
                return false;
            break;
        }
    }

    // Check Empty Stack
    return (s.empty());
}

// Driver program to test above function
int main()
{
    string expr;
    cout << "Enter Code: ";
    cin >> expr;

    if (areParanthesisBalanced(expr))
        cout << "Balanced";
    else
        cout << "Not Balanced";

    cout << "\nThanks for using the program. \nProgram by Pranav Mehendale\n";
    return 0;
}