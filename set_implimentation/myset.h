// myset.h
#ifndef MYSET_H
#define MYSET_H

typedef struct {
    char** values;
    int size;
    int capacity;
} MySet;

MySet* create_set();
MySet* handle_duplicate(MySet* set);

void destroy_set(MySet* set);
int get_size(MySet* set);
char** get_values(MySet* set);
MySet* add(MySet* set, const char* key);

#endif