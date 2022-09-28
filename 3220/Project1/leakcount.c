// Rob Hughes C11411208
// 3220 Project 1
// leakcount.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dlfcn.h>

int main(int argc, char** argv){
    int length=0;
    for(int a=1; a< argc; a++){
        length+= strlen(argv[a])+1;
    }
    const char* ldLoad= "LD_PRELOAD= ./memory_shim.so";
    length+= strlen(ldLoad)+1;
    char argData[length];
    strcpy(argData, ldLoad);

    for(int b=1; b< argc; b++){
        strcat(argData, " ");
        strcat(argData, argv[b]);
    }
}
