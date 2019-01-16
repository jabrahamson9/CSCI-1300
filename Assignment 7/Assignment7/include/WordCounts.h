//Jon Abrahamson
//Assignment 7
//CS 1300-108 Tillquist

#ifndef WORDCOUNTS_H
#define WORDCOUNTS_H
#include <iostream>
using namespace std;


class WordCounts
{
    public:
        WordCounts();
        virtual ~WordCounts();

        void tallyWords(string sentence);

        string tally[10000];
        int occurence[10000];

        int getindex(string);
        bool check(string);
        int getTally(string);

        void resetTally();
        int mostTimes(string*, int*, int);

    private:
};

#endif // WORDCOUNTS_H
