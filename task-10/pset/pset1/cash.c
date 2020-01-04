#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void) {
    int change;
    int q;
    int d;
    int n;
    int p;
    do {
        float money = get_float("change owed: ");
        change = round( money * 100);
    }
    while (change <= 0);

    q = change / 25;
    d = (change % 25) / 10;
    n = ((change % 25) % 10) / 5;
    p = ((change % 25) % 10) % 5;

    printf("%d\n", q + d + n + p);
}