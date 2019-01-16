#include <iostream>
#include <string>
using namespace std;

float similarityScore (string sequence1, string sequence2){
    float score;
    int i = 0;
    float hamming=0;
    while (sequence1.length()==sequence2.length() && i<sequence1.length() ){
            if (sequence1[i]!=sequence2[i])
                {hamming++;}
        i++;
    }
    if (sequence1.length()!=sequence2.length())
        {return 0;}
    score = (sequence1.length() - hamming ) / sequence1.length();
    return score;

}


int countMatches(string genome, string sequence1, float min_score){
    int value = 0;
    int i = 0;
        for (i=0;i<(genome.length()-(sequence1.length()-1));i++){
           string subG = genome.substr(i,sequence1.length());
            if (similarityScore(subG, sequence1) >= min_score)
                value++;
        }
    return value;
}


float findBestMatch(string genome, string seq){
    int i = 0;
    float largest =0;
        for (i=0;i<(genome.length()-(seq.length()-1));i++){
           string subG = genome.substr(i,seq.length());
           float score = similarityScore(subG, seq) ;
            if ( score>largest)
            {
                largest = score;
            }
        }
    return largest;
}


int findBestGenome(string genome1, string genome2, string genome3, string seq){
    float score1= findBestMatch(genome1,seq);
    float score2= findBestMatch(genome2,seq);
    float score3= findBestMatch(genome3,seq);
    if (score1>score2 && score1>score3)
        return 1;
    else if (score2>score1 && score2>score3)
        return 2;
    else if (score3>score2 && score3>score1)
        return 3;
    else if (score1==score2||score1==score3||score2==score3){
        return 0;}
}







int main(){
    int a=7;
    int count=1;
    for(int i; i<a;i++){
        for(int j=0;j<count;j++){
            cout<<'*';
        }
        cout<<endl;
        count++;
    }
}



