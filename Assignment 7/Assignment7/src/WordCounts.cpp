//Jon Abrahamson
//Assignment 7
//CS 1300-108 Tillquist

#include "WordCounts.h"
#include <iostream>
#include <stdio.h>
#include <ctype.h>
using namespace std;

//this constructor takes no parameters and just initializes all of my arrays to zero
WordCounts::WordCounts()
{
    for(int i=0;i<10000;i++){
    tally[i]="";
    occurence[i]=0;}
}

//deconstructor
WordCounts::~WordCounts(){
}

//this fucntion takes in one string parameter. It then strips the punctuation and converts the whole string to lower case.
//it then parses the string into words and stores them in the array. If the index of the array had alkready been seen it
//doesnt add to the tally array but it adds to the occurence array which corresponds with the tally array to count the ammount of times each string appears
//it returns nothing
int index=0;
void WordCounts::tallyWords(string sentence){
    string punc=".,?!";
    for(int i=0; i<sentence.length(); i++){
        for(int j=0; j<punc.length(); j++){
            if(sentence[i]==punc[j]){
                if(sentence[i+1]==' ' || sentence[i-1]==' ' || i==sentence.length()-1 || i==0){ //makes sure punc isnt inside a word
                    sentence.replace(i,1,"");
                    i=0;
                }
            }
        }
    }
    string tempsent="";
    for (int i=0; i<sentence.length(); i++){
        tempsent+=tolower(sentence[i]);//lower case
    }
    tempsent += " ";
    string str = "";
    int index=0;
    char sep=' ';
    for(int i=0;i<tempsent.length();i++){
        if(tempsent[i]==sep){
            if(check(str)==true){
                occurence[getindex(str)]++;//makes it so the occurence and tally arrays correspond and adds one if it was seen again
            }
            else{
                tally[index]=str;
                occurence[index] = 1;
                index++;
            }
            str="";//resets the string
        }
        else{
            str=str+tempsent[i];
        }
    }
}

//this function return the index in which the words is found so you can correspond the tally array with the occurence array.
int WordCounts::getindex(string word){
    for(int i=0;i<10000;i++){
        if(tally[i]==word)
            return i;
    }
    return -1;
}

//this function takes one string as a paramter. it checks to see if the tally at index i is ever equal to the input string
//it it is then it returns truw which then allows me to not store it again in the tally array
bool WordCounts::check(string str){
    for(int i=0;i<10000;i++){
        if(tally[i]==str){
            return true;
        }
    }
    return false;
}

//This functions takes one string of a word as a parameter. It then checks to see if the tally array is equal to a given word. it then returns
//the corresponding value at the same index in the occurence array to see how many times that word showed up. if not it returns 0 becouse the word
//shows up zero time/
int WordCounts::getTally(string givenWord){
    for(int i=0;i<10000;i++){
        if(tally[i]==givenWord){
            return occurence[i];
        }
    }
    return 0;
}

//this function takes no parameters it just resets all of the occurence values back to zero
void WordCounts::resetTally(){
    for(int i=0;i<10000;i++){
        occurence[i]=0;
    }
}

//this function takes in two arrays and an integer value as parameters. The n value is how many times
//the outer for loop runs through. if it is 4 hypothetically then the function finds the 4 highest occuring words.
//it uses a sort method and then stores then one by oe into the new arrays. it just returns zero after arrays are filled.
int WordCounts::mostTimes(string words[], int counts[], int n){
    for(int i=0;i<n;i++){
        int biggest=0;//initializes
        int spot=0;
        for(int j=0;j<10000;j++){
            if(occurence[j]>biggest){
                biggest=occurence[j];//keeps updatating the biggest value
                spot=j;
            }
        }
        counts[i]=biggest;//stores it as the first value of i and goes up to n values
        words[i]=tally[spot];
        occurence[spot]=0;
    }
    return 0;
}

