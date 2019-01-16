//Jon Abrahamson
//Assignment 7
//CS 1300-108 Tillquist

#include <iostream>
#ifndef SPELLCHECKER_H
#define SPELLCHECKER_H
#include <stdio.h>
#include <ctype.h>
#include <string>
using namespace std;

class SpellChecker
{
    public:
        SpellChecker();
        virtual ~SpellChecker();

        SpellChecker(string);

        void setlanguage(string);
        string getlanguage;

        SpellChecker(string,string,string);

        bool setStartMarker(char);
        char getStartMarker();

        bool setEndMarker(char end);
        char getEndMarker();

        bool readValidWords(string);
        bool readCorrectedWords(string);

        string repair(string sentence);
        string validwords[10000];
        string mis[10000];
        string correctedwords[10000];
        string temp[10000];
        string sentTemp[100000];

        string language;

    private:
         char startMarker;
         char endMarker;


};

#endif // SPELLCHECKER_H
