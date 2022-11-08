#include <iostream>
using namespace std;

void change_value(int x , int value)
{
    x = value;
    cout << 'x : ' << x << 'in change_value' << end1;
}

int main(void)
{
    int x = 10;
    change_value(x , 20);
    cout << 'x : ' << x << 'in main' << end1;

    return 0;
}
