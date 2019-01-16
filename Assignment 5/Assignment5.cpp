
#include <iostream>
#include <math.h>
using namespace std;

/*Function that takes an array and its size as a parameter. it then ads each array index to the sum. It
returns this as sum. it shuffles through every spot of the array by creating a for loop as long as the index
didnt exceed the size.
*/
float sumArray(float array[],int size){
    int sum = 0;
    for (int i=0; i<size; i++){
        sum= sum + array[i]; //shuffles through index and replaces original array
    }
    return sum;
}

/* the search function takes and array, its size, and a target value for the index to search for. the function
then shuffles through the array and if it is ever equal to the target value than it would return the array value
at that target point. If the target doesnt exist than return -1.
*/
int search (int array[], int size, int target){
    for(int i=0; i<size; i++){
        if (array[i] == target)
            return i;
    }
    for(int i=0; i<size; i++){  //2 for loops to test for both when an array has a target array or else return -01
        if (array[i] != target)
            return -1;
    }

}

/*function that takes 2 arrays and their sizes and then calculates the squared sum, where sum=(a-b)^2.
it then adds all of the sums at each index together with the "+=". It then returns the overall Sum. Uses the
POW function
*/
float calculateDifference(int a[], int b[], int size){
    float sum=0;
    for (int i=0; i<size; i++){
        sum += pow(a[i]-b[i],2); //add all sums together
    }
    return sum;
}

/*Function that takes an array and its size as parameters. It then uses selective sorting to order the code
from smallest value to largest. It then it then identifies a index value. then another index, j, is identified
as another index. Then code then sorts through for the smallest value and if it is smaller tha  the first
index than the second index gets sent to the front.
*/
void sortArray (float unsortedArray[], int size){
    int pos;
    int temp;
    for (int i=0; i<size-1; i++){
        pos=i;
        for(int j=i+1; j<size; j++){
            if (unsortedArray[j]<unsortedArray[pos])
                pos=j;
        }
        if(pos!=i){
            temp=unsortedArray[i];
            unsortedArray[i]=unsortedArray[pos];
            unsortedArray[pos]=temp;
        }
    }
}

/*This function takes a source code, a size, and a destination array to be copied into. The function then
creates a for loop and sets all destination index value to all of the corresponding source array index
values.
*/
void copyArray(float source[], int size, float dest[]){
    for(int i=0; i<size; i++){
        dest[i]=source[i];
    }

}

/*Function takes a rating, a string index, and its size as parameters. Then it creates a for loop that has a
series of if statements. When the rating index was exual to a certain value it would respond with a index
for the string array.
*/
void convert(int rating[],string text[],int size){
    for (int i=0; i<size; i++){
        if(rating[i]==0)
            text[i]="Not-read";
        else if(rating[i]==-5)
            text[i]="Terrible";
        else if(rating[i]==-3)
            text[i]="Disliked";
        else if(rating[i]==1)
            text[i]="Average";
        else if(rating[i]==3)
            text[i]="Good";
        else if(rating[i]==5)
            text[i]="Excellent";
        else
            text[i]="INVALID";
    }
}


/*This function takes an array and size as paramaters. It then uses the copy array to make a new array then the
selective sort function yto put the new array into smallest to largest. Then accounting for odd and even
sizes, it find the median of the ordered array. Returns the median.
*/
float findMedian(float array[],int size){
    float a[size];
    copyArray(array,size,a);
    int pos;
    int temp;
    for (int i=0; i<size-1; i++){
        pos=i;
        for(int j=i+1; j<size; j++){
            if (a[j]<a[pos])
                pos=j;
        }
        if(pos!=i){
            temp=a[i];
            a[i]=a[pos];
            a[pos]=temp;
        }
    }
        if(size%2 != 0){
            int b=((size-1)/2);
            return a[b];
    }
        else{
            float n1= a[size/2 - 1];
            float n2= a[size/2];
            return (n1+n2)/2;
        }
}










