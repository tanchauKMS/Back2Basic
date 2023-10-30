#include "mydictionary.h"
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 10

MyDict* create_dict() {
    MyDict* dict = (MyDict*)malloc(sizeof(MyDict));
    dict->keys = (char**)malloc(sizeof(char*) * INITIAL_CAPACITY);
    dict->values = (int*)malloc(sizeof(int*) * INITIAL_CAPACITY);
    dict->size = 0;
    dict->capacity = INITIAL_CAPACITY;
    return dict;
}
void destroy_dict(MyDict* dict){
    for (int i=0; i< dict->size; i++) {
        free(dict->keys[i]);
    }
    free(dict->values);
    free(dict);
}
int get_size(MyDict* dict) {
    return dict->size;
}

int get_value(MyDict* dict, const char* key) {
    for (int i = 0; i < dict->size; i++) {
        if (strcmp(dict->keys[i], key) == 0) {
            return dict->values[i];
        }
    }
    return -1;
}

void set_value(MyDict* dict, const char* key, int value) {
    for (int i = 0; i < dict->size; i++) {
        if (strcmp(dict->keys[i], key) == 0 ) {
            dict->values[i] = value;
            return;
        }
    }
    
    if (dict->size == dict->capacity) {
        dict->capacity *= 2;
        dict->keys = realloc(dict->keys, sizeof(char*) * dict->capacity );
        dict->values = realloc(dict->values, sizeof(int) * dict->capacity );
    }

    dict->keys[dict->size] = strdup(key);
    dict->values[dict->size] = value;
    dict->size++;
}
