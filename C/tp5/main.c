#include "action.h"
#include "support.h"
#include <unistd.h>
#include <time.h>

void menu() {
    int menuChoice;
    printf("\n\n/=== What would you like to do ? ===/\n/===    1. Create contact        ===/\n/===    2. Show all contacts     ===/\n/===    3. Find a contact        ===/\n/===    4. Test                  ===/\n/===    5. Exit                  ===/\n\n/===== Your choice: ");
    scanf("%d", &menuChoice);
    printf("\n");
    const int MAX = 9999, MIN = 1;
    srand(time(NULL));
    int testNum = (rand() % (MAX - MIN + 1)) + MIN;
    if (menuChoice == 1) {
        char firstname[100];
        char lastname[100];
        int age;
        printf(" /=== Enter contact's firstname: ");
        scanf("%s", firstname);
        printf("/=== Enter contact's lastname: ");
        scanf("%s", lastname);
        printf("/=== Enter contact's age: ");
        scanf("%d", &age);
        if (addContact(firstname, lastname, age) != 0) {
            printf("\n/===== Error while trying to create a contact =====/\n");
        }
    } else if (menuChoice == 2) {
        listContacts();
    } else if (menuChoice == 3) {
        char worDs[100];
        printf("/===== Search for : ");
        scanf("%s", worDs);
        searchContacts(worDs);
    }else if (menuChoice == 4) {
        printf("/=====  Run test...  =====/\n");
        test(testNum);
    } else if (menuChoice == 5) {
        printf("/=====  Exiting...  =====/\n");
        exit(1);
    } else {
        printf("/===== Invalid choice, retry pls ... =====/\n");
        menu();
    }
    sleep(3);
    exitingMenu();
}

int main() {
    printf("\n\n/===== Welcome to contact menu =====/\n");
    menu();
    return 0;
}

