#include "action.h"
#include "main.h"

int countBackN() {
    int *counter = malloc(sizeof(int));
    *counter = 0;
    FILE *file;
    char c;
    file = fopen(CONTACT, "r");
    if (file == NULL) {
        printf("/===== Could not open file %s =====/", CONTACT);
        return 0;
    }
    for (c = getc(file); c != EOF; c = getc(file))
        if (c == '\n')
            *counter = *counter + 1;
    fclose(file);
    return *counter;
}

char *toLowerCase(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] >= 65 && str[i] <= 90)
            str[i] += 32;
    }
    return str;
}

void exitingMenu() {
    int exitChoice;
    printf("\n\n/=== What would you like to do now ? ===/\n/===     1. Back to menu             ===/\n/===     2. Exit                     ===/\n\n/===== Your choice: ");
    scanf("%d", &exitChoice);
    if (exitChoice == 1) {
        menu();
    }
    if (exitChoice == 2) {
        printf("\n/=====  Exiting...  =====/\n");
        exit(1);
    } else {
        printf("\n/===== Invalid choice, retry pls ... =====/\n");
        exitingMenu();
    }
}

void test (int testNum) {
    char firstName[100] = "Test";
    char lastName[100] = "Number";
    char snum[5];
    printf("\n/===== Create contact =====/");
    addContact("Test","Number",testNum);
    printf("\n/===== List of contact(s) =====/");
    listContacts();
    printf("\n/===== Search contact with firstname =====/\n");
    printf("\n/=== Search for : %s ===/\n",firstName);
    searchContacts(firstName);
    printf("\n/===== Search contact with lastname =====/\n");
    printf("\n/=== Search for : %s ===/\n",lastName);
    searchContacts(lastName);
    printf("\n/===== Search contact with age =====/\n");
    printf("\n/=== Search for : %d ===/\n",testNum);
    searchContacts(itoa(testNum, snum, 10));
}