#include <stdio.h>

void DisplayWelcomeMessage(void)
{
    printf("TaskReminder v0.1\r\n");
}

int main(int argc, char *argv[])
{
    char command[100];
    DisplayWelcomeMessage();
	
    do
    {
        printf(">>");
        fgets (command , 100, stdin);
    } while (command[0]!='q');
	return 0;
}
