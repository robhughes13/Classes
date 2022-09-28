// Rob Hughes C11411208
// 3220 Project 1
// memory_shim.c

#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdlib.h>
#include <stdio.h>

void __attribute__ ((constructor)) shim_construct(void);
void __attribute__ ((destructor)) shim_destruct(void);
void free(void* ptr);
void* malloc(size_t size);
void *(*original_malloc)(size_t size)= NULL;
void (*original_free)(void* ptr)= NULL;

struct Node{
    int size;
    void* value;
    struct Node* next;
};
struct Node* head= NULL;

void shim_construct(void){
    original_malloc = dlsym(RTLD_NEXT, "malloc");
    original_free = dlsym(RTLD_NEXT, "free");
}

void free(void* ptr){
    original_free(ptr);
    struct Node* traverse= NULL;
    struct Node* previous= NULL;
    for(traverse= head; traverse!= NULL; previous= traverse, traverse= traverse->next){
        if(traverse->value== ptr){
            if(previous!= NULL)
                previous->next= traverse->next;
            else
                head= traverse->next;
            original_free(traverse);
            return;
        }
    }
    return;
}

void* malloc(size_t size){
    struct Node* new= original_malloc(sizeof(struct Node));
    struct Node* traverse;
    void* piece= original_malloc(size);
    new->size= (int) size;
    new->value= piece;
    if(head==NULL)
        head= new;
    else{
        traverse= head;
        while(traverse->next != NULL)
            traverse= traverse->next;
        traverse->next= new;
    }
    
    return piece;
}

void shim_destruct(void){
    struct Node* traverse= NULL;
    int leakSize=0;
    int total=0;
    for(traverse= head; traverse != NULL; traverse= traverse->next){
        total++;
        leakSize+= traverse->size;
        fprintf(stderr, "LEAK\t%d\n", traverse->size);
    }
    fprintf(stderr, "TOTAL\t%d\t%d\n", total, leakSize);
}
