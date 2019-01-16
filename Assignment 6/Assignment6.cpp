


using namespace std;
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>


float avgCharsPerLine(string file){
  ifstream dataFile(file, ios::in);
  if (dataFile.fail()){
    cout<<"Error "<<file<<endl;
    return 0;
  }
    float chars=0;
    float lines;
    string thisline="";
    while(!dataFile.eof()){
        getline(dataFile, thisline);
        chars+=thisline.length();
        lines+=1.0;
    }
    dataFile.close();
    return chars/lines;
}

int fillArray(string file,float array[][5]){
    stringstream ss;
    ifstream dataFile(file, ios::in);
    if(dataFile.fail()){
        cout<<"Error "<<file<<endl;
        return 0;
    }
    dataFile.ignore(1,'\n');
    int lines=0;
    string thisline="";
    while (!dataFile.eof()){
        getline(dataFile, thisline);
        for(int i=0;i<file.length();i++){
            if(thisline[i]==','){
                ss<< thisline;
                float a;
                ss>>a;
                array[lines][5]=a;
                thisline="";
                lines++;
        }
        else{
            thisline=thisline+file[i];
        }
    if(thisline!=""){
        ss<< thisline;
        float a;
        ss>>a;
        array[lines][5]=a;
        lines++;
    }
    }
    }
    dataFile.close();
    return lines;
}

float arrayStats(string filename, float numbers[][5]){
    int count= fillArray(filename, numbers);
    fillArray(filename, numbers);
    int i=0;
    int r=0;
    float sum1;
    float sum2;
    float total=0;
    float total2=0;
    int lines=0;
    int oddLines=0;
    for (int i=0; i<lines; i++){
    if(lines%2!=0){
        oddLines++;
    }
    }
    while(i%2!=0){
        while(r<=5){
            total+=numbers[i][r];
            float mean= (total)/5;
            sum1+=mean;
            r++;
        }
        i++;
    }
    while(i%2!=0){
        while (r<lines){
            total2+=numbers[r][i];
            float mean2= (total2)/oddLines;
            sum2+=mean2;
        }
        i++;
    }
float totalSum= sum1+sum2;
return totalSum;
}
