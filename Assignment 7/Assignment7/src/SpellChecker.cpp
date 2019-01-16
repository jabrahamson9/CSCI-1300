//Jon Abrahamson
//Assignment 7
//CS 1300-108 Tillquist

#include "SpellChecker.h"
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <string>
using namespace std;

/*This constructor takes no parameters and just initializes all of my arrays to zero
it returns nothing.
*/
SpellChecker::SpellChecker(){
    for(int i = 0; i < 10000; i++){//must initialize all values so I dont get seg faults
        validwords[i] = "";
        mis[i] = "";
        correctedwords[i] = "";
        temp[i] = "";
        sentTemp[i] = "";
    }
}

/*This constructor takes in a string parameter. It also makes sure to initialize all arrays to zero. Im not sure if this is necessary
but it is a safety net. This method then just sets the language in the h file to whatever the input for the parameter is.
*/
SpellChecker::SpellChecker(string lang){
    for(int i = 0; i < 10000; i++){//not sure if i have to do it again here but making sure everything is initialized
        validwords[i] = "";
        mis[i] = "";
        correctedwords[i] = "";
        temp[i] = "";
        sentTemp[i] = "";
    }
    language=lang;
}

//deconstructor
SpellChecker::~SpellChecker(){//ask carter to explain to me
}

//this function also takes a single string parameter and sets this equal to the language in the h file
//it is a void so it returns nothing
void SpellChecker::setlanguage(string olanguage){
    language=olanguage;
}


//this is the last constructor and it takes 3 parameters. all strings but it takes a language and the two files containing
//the necessary words. It again initializes all of my arrays to zero and opens my files.
SpellChecker::SpellChecker(string olangauge, string correctfile, string mispelledfile){
    for(int i = 0; i < 10000; i++){
        validwords[i] = "";
        mis[i] = "";
        correctedwords[i] = "";
        temp[i] = "";
        sentTemp[i] = "";
    }
    language=olangauge;
    readValidWords(correctfile);//open files
    readCorrectedWords(mispelledfile);
}

//function that takes in the file containing the already correct words. It checks to see if the file opened successfully
//It then goes through each line of the file and stores the single word lines texts into an array of valid words. If everything
//is successful then it returns true
bool SpellChecker::readValidWords(string correctfile){
    string word;
    ifstream correct(correctfile);
    if(correct.fail()){//check if opens correctly
        return false;
    }
    int count=0;
    while(!correct.eof()){
        getline(correct, word); //filles array, no parsing needed cuz only one word per line
        validwords[count]=word;
        count++;
    }
    return true;
}

//function that takes in the file containing the misspelled words ad their corrections. It checks to see if the file opened successfully
//It then goes through each line of the file and parses the data twice. Because there are two words per line and i wanted to make
// two different arrays with one word in each, I did two parses, one leaving out the last words and one not and stored them
//into their respected arrays. If everything is successful then it returns true.
bool SpellChecker::readCorrectedWords(string mispelledfile){
    string text;
    ifstream mispelled(mispelledfile);
    if(mispelled.fail()){
        return false;
    }
    int counter=0;
    while(!mispelled.eof()){
        getline(mispelled, text);
        string str="";
        char sep='\t';
        for(int i=0; i<text.length();i++){
            if(text[i]==sep){
                mis[counter]=str;
                str="";
                counter++;}
            else{
                str=str+text[i];
            }
        }
    }
    string ctext;
    mispelled.close();
    ifstream redo(mispelledfile);
    int line = 0;
    while(!redo.eof()){
        getline(redo, ctext);
        ctext=ctext+'\t';
        string cstr="";
        char sep='\t';
        for(int i=0; i<ctext.length();i++){
            if(ctext[i]=='\t'){
                temp[line]=cstr;
                cstr="";
                line++;}
            else{
                cstr=cstr+ctext[i];
            }
        }
    }
    int z=1;
    int j=0;
    while(z<10000 || j<10000){
        if(temp[z].length() > 0){
            correctedwords[j]=temp[z];
        }
        z=z+2;// did this so it would store every other word which would be the corrected word
        j++;
    }
    return true;
}

//function takes in a character and sets it equal to my start marker
bool SpellChecker::setStartMarker(char begin){
    startMarker=begin;
    return true;
}

//function takes in a character and sets it equal to my end marker
bool SpellChecker::setEndMarker(char end){
    endMarker=end;
    return true;
}

//function takes no parameters and solely returns my start marker
char SpellChecker::getStartMarker(){
    return startMarker;
}

//function takes no parameters and solely returns my end marker
char SpellChecker::getEndMarker(){
    return endMarker;
}

//this function does a lot. it takes a string as a parameter. the string is just a sentence with possikble errors to be fixed. it then returns the
//fixed version of the sentence. It begins by stripping the punctiuation from the sentence and making the whole string lower case. it then parses all
//of the string into individual words and stores them as an array. The array then checks to see if they appear as apart of the valid words and des nothing to
//the stored string. it then checks if it is in the mispelled. if it is, then i changes is it to the corrected words at the same index as the misspelled. Finally
//if there is no match it takes the word and adds the end and start markers to the word to indicate that the word is unknown.
string SpellChecker::repair(string sentence){
    string punc=".,?!";
    for(int i=0; i<sentence.length(); i++){
        for(int j=0; j<punc.length(); j++){
            if(sentence[i]==punc[j]){
                if(sentence[i+1]==' ' || sentence[i-1]==' ' || i==sentence.length()-1 || i==0){//makes it so it doesnt take punc out of middle of words
                    sentence.replace(i,1,"");
                    i=0;
                }
            }
        }
    }
    sentence += " ";//so i dont miss the last word in parse
    string str = "";
    int index=0;
    for(int i=0;i<sentence.length();i++){
        char sep=' ';
        if(sentence[i]==sep){
            sentTemp[index]=str;
            str="";
            index++;
        }
        else{
            str=str+sentence[i];
        }
    }

    for(int i=0; i<10000; i++){
        string tempString="";
        string tempStr=sentTemp[i];
        int len=sentTemp[i].length();
        if(len > 0){
            for(int j=0; j<len; j++){//so i can run throuogh each individual character instead of each word to make it lowercase
                tempString+=tolower(tempStr[j]);
            }
            sentTemp[i]=tempString;
        }
    }
    for(int i=0; i<10000; i++){
        if(sentTemp[i].length() > 0){//i have a huge array size this just finds the indexes that actually have values
            for(int j=0; j<10000; j++){
                if(mis[j].length() > 0){//just finding words in array
                    if(sentTemp[i]==mis[j]){
                        sentTemp[i]=correctedwords[j];//switches mispelled for correct
                    }
                }
            }
        }
    }
    bool fix = false; //bool is used for finding when things are NOT true
    for(int i=0; i<sentence.length(); i++){
        if(sentTemp[i].length()>0){
            for(int j=0; j<10000; j++){
                if(sentTemp[i]!=mis[j] && sentTemp[i]==validwords[j] && sentTemp[i]!=correctedwords[j]){
                    sentTemp[i]=validwords[j];
                    fix = true;
                }
            }
        }

    }
    for(int i=0; i<sentence.length(); i++){//when things are not true again use bool
        for(int j=0; j<10000; j++){
            if(sentTemp[i]!=mis[j] && sentTemp[i]!=validwords[j] && sentTemp[i]==correctedwords[j]){
                sentTemp[i]=correctedwords[j];
                fix = true;
            }
        }
    }
    if(fix == false){
        for(int i=0; i<sentence.length(); i++){
            bool change = true;
            if(sentTemp[i].length() > 0){
                for(int j=0; j<10000; j++){
                    if(mis[j].length() > 0){
                        if(sentTemp[i]==mis[j] || sentTemp[i]==validwords[j] || sentTemp[i]==correctedwords[j]){//if all is true but if false then word is unkown
                            change = false;
                        }
                    }
                }
                if(change == true){//word must be unknown
                    sentTemp[i]=startMarker+sentTemp[i]+endMarker;//puts markers around it

                }
            }
        }
    }
    string fixed = "";
    for(int i = 0; i < 10000; i++){
        if(sentTemp[i].length() > 0){
            fixed += sentTemp[i] + " "; //reforms sentence
        }
    }
    fixed.replace(fixed.length()-1, 1, "");

    return fixed;
}


