// mydict.h
#ifndef MYDICT_H
#define MYDICT_H

typedef struct {
    char** keys;
    int* values;
    int size;
    int capacity;
} MyDict;

MyDict* create_dict();
void destroy_dict(MyDict* dict);
int get_size(MyDict* dict);
int get_value(MyDict* dict, const char* key);
void set_value(MyDict* dict, const char* key, int value);

#endif