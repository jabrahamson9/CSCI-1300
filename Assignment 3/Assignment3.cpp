#include <iostream>
using namespace std;

string menu()
{

    cout<< "Which story would you like to play? Enter the number of the story (1, 2, or 3) or type q to quit: " << '\n';
    int n;
    cin>> n;
    if (n!='q' && n!=1 && n!=2 && n!=3)
        cout<< "Valid choice not selected."<<'\n';
    else if (n=='q')
        cout<< "good bye"<<'\n';
    else if (n==1) {
        string a;
        cout<<"Enter a plural noun: ";
        cin>> a;
        cout<< '\n';
        string b;
        cout<<"Enter an occupation: ";
        cin>> b;
        cout<< '\n';
        string c;
        cout<<"Enter an animal name: ";
        cin>> c;
        cout<< '\n';
        string d;
        cout<<"Enter a place: ";
        cin>> d;
        cout<< '\n';
        cout<<"In the book War of the "<<a<<", the main character is an "<<'\n'<<"anonymous "<<b<<" who records the arrival of the "<<c<<"s"<<'\n'<<"in "<<d<<"."<<'\n';
    }
    else if (n==2) {
        string a;
        cout<<"Enter a name: ";
        cin>> a;
        cout<< '\n';
        string b;
        cout<<"Enter a state/country: ";
        cin>> b;
        cout<< '\n';
        cout<<a<<", I've got a feeling we're not in "<<b<<" anymore."<<'\n';
    }
    else if (n==3){
        string a;
        cout<<"Enter a first name: ";
        cin>> a;
        cout<< '\n';
        string b;
        cout<<"Enter a relative: ";
        cin>> b;
        cout<< '\n';
        string c;
        cout<<"Enter a verb: ";
        cin>> c;
        cout<< '\n';
        cout<<"Hello. My name is "<<a<<". You killed my "<<b<<". Prepare to "<<c<<"."<<'\n';
    }
    return menu();

}
int main(void)
{
    cout<< menu();
}
