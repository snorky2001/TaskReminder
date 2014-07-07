#include <stdio.h>
#include <string.h>

/* Gnome librqry for standart containers */
#include <glib.h>

void DisplayWelcomeMessage(void)
{
    printf("TaskReminder v0.1\r\n");
}

void ParseParameters(char* cmd, GSList** params)
{
    char* pch;
	pch = strtok (cmd," ");
	gpointer param;
	GSList* parameters = NULL;

	while (pch != NULL)
	{
	    printf ("%s\r\n",pch);
		param = g_slice_alloc( strlen(pch) );
		memcpy(param, pch, strlen(pch));
		parameters = g_slist_append( parameters, pch );
	    pch = strtok (NULL, " ");
	}
	*params = parameters;

}

int main(int argc, char *argv[])
{
    char command[100];

    DisplayWelcomeMessage();

    GSList* params = NULL;

    do
    {
        /* Display prompt */
        printf(">>");

        /* get command */
        fgets (command , 100, stdin);
		ParseParameters(command, &params);

		/* proceed with cmd */

		/* free list */

    } while (command[0]!='q');
	return 0;
}
