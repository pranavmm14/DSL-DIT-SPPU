#include <iostream>
using namespace std;
const int NUM_ROWS = 10;
const int SEATS_PER_ROW = 7;

struct Seat
{
    int row;
    int seat;
    Seat *prev;
    Seat *next;
};

class Cinemax
{
private:
    Seat *rows[NUM_ROWS]; // Array to store pointers to the head of each row

public:
    Cinemax()
    {
        // Initialize the rows array with null pointers
        for (int i = 0; i < NUM_ROWS; i++)
        {
            rows[i] = nullptr;
        }
    }

    // Display the list of available seats
    void displayAvailableSeats()
    {
        cout << "Available seats:" << endl;
        for (int i = 0; i < NUM_ROWS; i++)
        {
            Seat *seat = rows[i];
            if (seat == nullptr)
            {
                cout << "Row " << i + 1 << ": 1 2 3 4 5 6 7" << endl;
            }
            else
            {
                cout << "Row " << i + 1 << ": ";
                for (int j = 1; j <= SEATS_PER_ROW; j++)
                {
                    if (seat == nullptr || seat->seat != j)
                    {
                        cout << j << " ";
                    }
                    else
                    {
                        cout << "* ";
                        seat = seat->next;
                    }
                }
                cout << endl;
            }
        }
    }

    // Book a seat
    void bookSeat(int row, int seat)
    {
        Seat *newSeat = new Seat;
        newSeat->row = row;
        newSeat->seat = seat;
        newSeat->prev = nullptr;
        newSeat->next = nullptr;

        if (rows[row] == nullptr)
        {
            // This is the first seat being booked in this row
            rows[row] = newSeat;
            newSeat->prev = newSeat;
            newSeat->next = newSeat;
        }
        else
        {
            // Insert the new seat between the head and the next available seat
            Seat *next = rows[row];
            while (next->prev != nullptr)
            {
                next = next->next;
            }
            newSeat->prev = next->prev;
            newSeat->next = next;
            next->prev->next = newSeat;
            next->prev = newSeat;
        }
    }

    // Cancel a booking
    void cancelBooking(int row, int seat)
    {
        Seat *toCancel = rows[row];
        if (toCancel == nullptr)
        {
            cout << "No booking found for row " << row << " seat " << seat << endl;
            return;
        }

        do
        {
            if (toCancel->seat == seat)
            {
                // We found the seat to cancel
                if (toCancel->prev == toCancel)
                {
                    // This was the only seat booked in this row
                    rows[row] = nullptr;
                }
                else
                {
                    // There are other booked seats in this row, so we need to update the links
                    toCancel->prev->next = toCancel->next;
                    toCancel->next->prev = toCancel->prev;
                    if (toCancel == rows[row])
                    {
                        // The seat being cancelled is the head, so we need to update the head pointer
                        rows[row] = toCancel->next;
                    }
                }
                delete toCancel;
                cout << "Booking cancelled for row " << row << " seat " << seat << endl;
                return;
            }
            toCancel = toCancel->next;
        } while (toCancel != rows[row]);
        cout << "No booking found for row " << row << " seat " << seat << endl;
    }
};

int main()
{
    Cinemax cinema;

    // Make some random bookings
    cinema.bookSeat(2, 3);
    cinema.bookSeat(3, 6);
    cinema.bookSeat(5, 2);
    cinema.bookSeat(7, 5);
    cinema.bookSeat(0, 5);
    cinema.bookSeat(1, 5);

    // Display the available seats
    cinema.displayAvailableSeats();

    // Cancel a booking
    cinema.cancelBooking(3, 6);
    cinema.cancelBooking(2, 5);
    cinema.cancelBooking(2, 3);

    // Display the available seats again
    cinema.displayAvailableSeats();

    return 0;
}
