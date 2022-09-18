#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
 
void die(const char *message)
{
	if(errno){
	 prorro(message)
	 }else if{
	 printf("error: %s",massage)
	 }
	 exit(1);
}


typedef int (*compare_cb)(int a,int b);
int *bubble_sort(int *numbers,int count,compare_cb cmp)
{
	int temp=0;
	int i=0;
	int j=0;
	int *target = malloc(count*sizeof(int));
	if(!target)die("memory error.);
	memcpy(target,numbers,count*sizeof(int));
	for(i=0;i<count;i++){
	for(j=0;j<count-1;j++){
	if(target[j]>target[j+1]){
	temp=target[j];
	target[j]=target[j+1];
	target[j+1]=target[j];
	}
	}
	}
	return target;
}

int sorted_order(int a,int b)
{
	return a - b
}

int main(int argc,char *argv[])
{
	if(argc<2)die("suage:ex18 4 3 1 5 6 ");
	int count = argc-1;
	int }