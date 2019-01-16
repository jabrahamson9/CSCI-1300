//Jon Abrahamson
//Assignment 7
//CS 1300-108 Tillquist

#include "SpellChecker.h"
#include "WordCounts.h"
#include <iostream>
using namespace std;

int main(){
    /*string sent="!hAlo";
    WordCounts test;
    test.tallyWords(sent);
    cout<<test.getTally("halo")<<endl;
    test.resetTally();
    test.tallyWords(sent);
    cout<<test.getTally("halo")<<endl;*/


    SpellChecker test("english","correctedfile","mispelledfile");
    //test.setEndMarker('~');
    //test.setStartMarker('~');
    cout<<test.repair("neighbour Halo todayy i am good");


}
