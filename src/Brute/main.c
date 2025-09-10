#include <stdio.h>
#include <string.h>

int main() {
    const char *sy[] = {

    
    "123",
    "pass",
    "lile"
    };
    int size = sizeof(sy) / sizeof(sy[0]);

     char input[1024];
     printf("Enter the word: ");
     scanf("%49s", input);

     int found =;
     for (int i = 0; i < size; i++) {
         if (strcmp(input,sy[i]) == 0) {
             found = 1;
             break;
         }
     } 

     if(found) {
         prinf("the word \"%s\" was found.\n", input);
     }
}