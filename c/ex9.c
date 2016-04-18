#include <stdio.h>

int main(int argc, char *argv[])
{
   int numbers[4] = {0};
   char name[4] = {'a'}; 
   
   printf("numbers: %d %d %d %d\n",
           numbers[0], numbers[1], numbers[2], numbers[3]);
   printf("name each: %c %c %c %c %c %c %c\n", 
           name[0], name[1], name[2], name[3], name[4], name[5], name[6]);
   printf("name: %s\n", name);
    
   numbers[0] = 1;
   numbers[1] = 2;
   numbers[2] = 3;
   numbers[3] = 4;

   name[0] = 'A';
   name[1] = 'g';
   name[2] = 'a';
   name[3] = 't';
   name[4] = 'h';
   name[5] = 'a';
   name[6] = '\0';
    
   printf("numbers: %d %d %d %d\n",
           numbers[0], numbers[1], numbers[2], numbers[3]);
   printf("name each: %c %c %c %c %c %c %c\n", 
           name[0], name[1], name[2], name[3], name[4], name[5], name[6]);
   printf("name: %s\n", name);


   char *another = "Barata";
    printf("surname: %s\n", another);
    printf("surname each: %c %c %c %c %c %c %c\n", 
            another[0], another[1], another[2], another[3], another[4],
            another[5], another[6]);
    return 0;
    
}
