// mylist.h
#ifndef MYLIST_H
#define MYLIST_H

typedef struct {
    int length;
    int capacity;
    int* array;
} MyList;

MyList* create_list();
void destroy_list(MyList* list);
int get_length(MyList* list);
int get_item(MyList* list, int index);
void append_item(MyList* list, int item);

#endif