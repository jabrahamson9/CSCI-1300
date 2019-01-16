// Author: CS1300 Fall 2017
// Recitation: 123 – Favorite TA
//
// Assignment 2

#include <iostream>

using namespace std;

/**
 * Algorithm description for function howMany() goes here
 *
 */
int howMany(int population) {
    return 0;
}

/**
 * Algorithm description for function howLong() goes here
 *
 */
void howLong(int seconds) {
    cout << "" << endl;
    return;
}

/**
 * Algorithm description for function howHot() goes here
 *
 */
int howHot(int temperature) {
    return 0;
}


int main() {
    // Problem 1 test
    // Change value of 'pop' to change value you want to test
    int pop = 0;
    cout << "Given the initial population of " << pop;
    cout << " your estimation finds a population of ";
    cout << howMany(pop) << endl << endl;

    // Problem 2 test
    // Change value 'sec' to change value you want to test
    int sec = 0;
    cout << "Given the seconds value of " << sec;
    cout << " your output is: " << endl;
    howLong(sec);
    cout << endl;

    // Problem 3 test
    // Change value 'temp' to change value you want to test
    int temp = 0;
    cout << "Given temperature " << temp;
    cout << " degrees Celsius you calculate ";
    cout << howHot(temp) << " degrees Fahrenheit" << endl;
    return 0;
}
