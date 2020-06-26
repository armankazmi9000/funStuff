#include <iostream>

using namespace std;

int main()

{
   float weight;
   
   float height;
   
   float heightsquared;
   
   float weightoverheight;
   
   float bmi;
   
   cout << "BMI Calculator" << endl;
   
   cout << "What is your weight in pounds(lbs)?" << endl;
   
   cin >> weight;
   
   cout << "What is your height in inches(in.)?" << endl;
   
   cin >> height;
   
   heightsquared = height * height;
   
   weightoverheight = weight / heightsquared;
   
   bmi = weightoverheight * 703;
   
   cout << "Your BMI is...." << bmi;
   
   if (bmi<18.5)
   
      cout << ", your underweight!" << endl;
      
   if (bmi>30)
   
      cout << ", your obese!" << endl;
   
   if (bmi>18.5 && bmi<25)
   
      cout << ", your healthy!" << endl;
   
   if (bmi>=25 && bmi<=30)
      
      cout << ", your overweight!" << endl;


   return 0; 
}