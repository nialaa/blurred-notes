#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("------> hey! pon argumentos, que te los divido!! :D\n");
    int i = 0;
    for(i = 1; i < argc; i++) {
        printf("arg %d: %s\n", i, argv[i]);
    }

    char *states[] = {
        "Connecticut", "Washington", "New York", "Oregon"
    };
    int num_states = 4;
    
    for(i = 0; i < num_states; i++) {
        printf("state %d: %s\n", i, states[i]);
    }
    return 0;

}
