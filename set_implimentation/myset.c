#include "myset.h"
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 10

MySet* create_set() {
    MySet* set = (MySet*)malloc(sizeof(MySet));
    set->values = (char**)malloc(sizeof(char*) * INITIAL_CAPACITY);
    set->size = 0;
    set->capacity = INITIAL_CAPACITY;
}

MySet* handle_duplicate(MySet* set) {
    for(int i=0; i < set->size; i++) {
        for(int j=i+1; j < set->size; j++) {
            if(strcmp(set->values[i], set->values[j]) == 0) {
                for(int k = j; k < set->size - 1; k++) {
                    char* temp = set->values[k];
                    set->values[k] = set->values[k+1];
                    set->values[k+1] = temp;
                    }
            set->size--;
            j--; 
                }
            }
        }
    return set;
    }

void destroy_set(MySet* set) {
    for(int i=0; i < set->size; i++) {
        free(set->values[i]);
    }
    free(set);
}
int get_size(MySet* set) {
    return set->size;
}

char** get_values(MySet* set) {
    char** values = (char**)malloc(sizeof(char*) * (set->size + 1));
    for (int i = 0; i < set->size; i++) {
        values[i] = strdup(set->values[i]);
    }
    values[set->size] = NULL;
    return values;
}

MySet* add(MySet* set, const char* key) {
    if(set->size == set->capacity) {
        set->capacity *=2;
        set->values = (char**)realloc(set->values, 
                                      sizeof(char*) * set->capacity);
    }
    set->values[set->size] = strdup(key);
    set->size++;
    return handle_duplicate(set);
}