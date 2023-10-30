// mylist.c
#include "mylist.h"
#include <stdlib.h>

#define INITIAL_CAPACITY 10
MyList* create_list() {
    MyList* list = (MyList*)malloc(sizeof(MyList));
    list->length = 0;
    list->capacity = 1;
    list->array = (int*)malloc(sizeof(int) * list->capacity);
    return list;
}

void destroy_list(MyList* list) {
    free(list->array);
    free(list);
}

int get_length(MyList* list) {
    return list->length;
}

int get_item(MyList* list, int index) {
    if (index < 0 || index >= list->length) {
        // Handle error
    }
    return list->array[index];
}

void append_item(MyList* list, int item) {
    if (list->length == list->capacity) {
        // Resize the array
        list->capacity *= 2;
        list->array = (int*)realloc(list->array, sizeof(int) * list->capacity);
    }
    list->array[list->length] = item;
    list->length++;
}