#include <stdio.h>
#include <stdlib.h>

/* TODO: How to create the array dynamically sized? */
#define NUMBERS_LEN 200

int main() {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    int numbers[NUMBERS_LEN];
    int c = 0;    

    fp = fopen("day1_input.txt", "r");
    if (fp == NULL)
        exit(1);


    while ((read = getline(&line, &len, fp) != -1)) {
        numbers[c] = atoi(line);
        c++;
    }
    free(line);
    fclose(fp);

    /* PART 1 SOLUTION */

    for (int i = 0; i < NUMBERS_LEN; i++) {
        for (int j = i; j < NUMBERS_LEN; j++) {
            if (numbers[i] + numbers[j] == 2020) {
                printf("Solution to part 1 is: %d\n", numbers[i] * numbers[j]);
                break;
            }
        }
    }

    /* PART 2 SOLUTION */

    for (int i = 0; i < NUMBERS_LEN; i++) {
        for (int j = i; j < NUMBERS_LEN; j++) {
            for (int k = j; k < NUMBERS_LEN; k++) {
                if (numbers[i] + numbers[j] + numbers[k] == 2020) {
                    printf("Solution to part 2 is: %d\n", numbers[i] * numbers[j] * numbers[k]);
                    break;
                }
            }
        }
    }

    return 0;
}

