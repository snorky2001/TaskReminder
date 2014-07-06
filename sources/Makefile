EXEC=hello
SRC= $(wildcard *.c)
OBJ= $(SRC:.c=.o)
CFLAGS= -I/usr/include/glib-2.0 -I/usr/lib/i386-linux-gnu/glib-2.0/include
LDFLAGS= -lglib-2.0

all: $(EXEC)

hello: $(OBJ)
	@$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c
	@$(CC) -o $@ -c $< $(CFLAGS)

.PHONY: clean mrproper

clean:
	@rm -rf *.o

mrproper: clean
	@rm -rf $(EXEC)
