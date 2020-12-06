#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* TODO: How to create the array dynamically sized? */
#define WORDS_LEN 1000

int index_of_kth(char *str, char to_find, int k);
int is_valid_passphrase_pt1(char *str, char to_contain, int lower, int upper); 
int is_valid_passphrase_pt2(char *str, char to_contain, int lower, int upper); 


int main() {
    FILE *fp;
    size_t len = 0;
    ssize_t read;

    char lines[WORDS_LEN][50];



    fp = fopen("day2_input.txt", "r");
    if (fp == NULL)
        exit(1);

    int c = 0;
    while (fgets(lines[c], 50, fp)) {
        lines[c][strlen(lines[c]) - 1] = '\0';
        c++;
    }

    fclose(fp);

    char chr_to_find, *passphrase;
    int i1, i2, i3, i4;

    int n1, n2;

    char c1, c2[2];

    int sol_count_pt1 = 0;
    int sol_count_pt2 = 0;

    for (int c = 0; c < WORDS_LEN; c++) {
        i1 = index_of_kth(lines[c], '-', 1);
        i2 = index_of_kth(lines[c], ' ', 1);
        i3 = index_of_kth(lines[c], ':', 1);
        i4 = index_of_kth(lines[c], ' ', 2);


        // ROFL this is ugly af - but works :)
        // hacky shit.
        if (i1 == 1) {
            memcpy(&c1, lines[c], 1);
            n1 = atoi(&c1);
        } else {
            memcpy(&c2, lines[c], 2);
            n1 = atoi(c2);
        }
        if (i2 - i1 == 2) {
            memcpy(&c1, &lines[c][i1+1], 1);
            n2 = atoi(&c1);
        } else {
            memcpy(&c2, &lines[c][i1+1], 2);
            n2 = atoi(c2);
        }

        chr_to_find = lines[c][i3-1];
        passphrase = &lines[c][i4+1];
        if (is_valid_passphrase_pt1(passphrase, chr_to_find, n1, n2))
            sol_count_pt1++;
        if (is_valid_passphrase_pt2(passphrase, chr_to_find, n1 - 1, n2 - 1))
            sol_count_pt2++;
    }
    
    printf("Solution to part 1: %d\nSolution to part 2: %d\n", sol_count_pt1, sol_count_pt2);
    return 0;
}

int index_of_kth(char *str, char to_find, int k) {
    /* Returns the index of k-th occurence of `to_char` in `str` */

    int i = 0;
    int j = 0;
    while (*str) {
        if (*str == to_find) {
            j++;
            if (j == k) 
                return i;
        }
        i++;
        str++;
    }

    // Didn't find anything. Oh well.
    return -1;
}

int is_valid_passphrase_pt1(char *str, char to_contain, int lower, int upper) {
    int count = 0;

    while (*str) {
        if (*str == to_contain)
            count++;
        str++;
    }
    if ((lower <= count) && (count <= upper))
        return 1;

    return 0;
}

int is_valid_passphrase_pt2(char *str, char to_contain, int lower, int upper) {
    if (str[lower] == to_contain && str[upper] != to_contain)
        return 1;
    if (str[lower] != to_contain && str[upper] == to_contain)
        return 1;

    return 0;
}
