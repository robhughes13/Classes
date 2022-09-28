// Rob Hughes C11411208
// 3220 Project 1
// sctracer.c


#define SYSCALLS 350
#define LENGTH 1024
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/reg.h>
#include <sys/wait.h>
#include <sys/ptrace.h>
#include <unistd.h>

int main(int argc, char** argv){
    pid_t pid;
    if((pid=fork())==0){
        ptrace(PTRACE_TRACEME);
        kill(getpid(), SIGSTOP);
        return (execvp(argv[0],argv+1));
    }
    else{
        int stat, numCall, max;
        max=0;
        int calls[SYSCALLS]= {0};
        FILE* out;
        ptrace(PTRACE_SETOPTIONS, pid, NULL, PTRACE_O_TRACESYSGOOD);
        for(;;){
            ptrace(PTRACE_SYSCALL, pid, NULL, 0);
            waitpid(pid, &stat, 0);
            if(WIFEXITED(stat))
                break;

            numCall=ptrace(PTRACE_PEEKUSER, pid, sizeof(long)*ORIG_RAX, NULL);
            if(numCall>max)
                max= numCall;
            calls[numCall]++;
            ptrace(PTRACE_SYSCALL, pid, NULL, 0);
            waitpid(pid, &stat, 0);
            if(WIFEXITED(stat))
                break;
        }
        out= fopen(argv[2], "w");
        for(int i=0;i <max+1; i++){
            if(calls[i]>0)
                fprintf(out,"%d\t%d\n", i, calls[i]);
            
        }
        fclose(out);
    }
    return 0;
}
