#include <stdio.h>
#include <string.h>

/* Gnome librqry for standart containers */
#include <glib.h>

void DisplayWelcomeMessage(void)
{
    printf("TaskReminder v0.1\r\n");
}


int main(int argc, char *argv[])
{
    char command[100];
    char* pch;
    DisplayWelcomeMessage();

    gshort test;

    do
    {
        /* Display prompt */
        printf(">>");

        /* get command */
        fgets (command , 100, stdin);
        pch = strtok (command," ");
        while (pch != NULL)
        {
            printf ("%s\r\n",pch);
            pch = strtok (NULL, " ");
        }
    } while (command[0]!='q');
	return 0;
}
