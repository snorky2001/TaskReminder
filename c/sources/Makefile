EXEC=hello
SRC= $(wildcard *.c)
OBJ= $(SRC:.c=.o)
CFLAGS= `pkg-config --cflags glib-2.0`
LDFLAGS= `pkg-config --libs glib-2.0`

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
