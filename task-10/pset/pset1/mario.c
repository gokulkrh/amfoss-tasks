#include <stdio.h>
#include <cs50.h>

int main(void){
    int h;
    int s;
    int d;

    do
    {
        h = get_int("height :");
    }
    while (h <= 0 || h >= 23);
    for (int i = 1; i <= h; i++){
        for (s = (h - i); s >= 0; s--){
            printf(" ");
        }
        for (d = 1; d <= (i + 1); d++){
            printf("#");
        }
        printf("\n");
    }
    return 0;
}