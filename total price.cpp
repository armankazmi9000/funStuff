#include <iostream>

using namespace std;

int main()
{
   float units;
   
   float price;
   
   string county;
   
   float tax;
   
   float taxactual;
   
   float unitprice;
   
   float taxtotal;
   
   float total;
   
   cout << "Total Price Calculator" << endl;
   
   cout << "How many items did you buy?" << endl;
   
   cin >> units;
   
   cout << "What was the price of each item($)?" << endl;
   
   cin >> price;
   
   cout << "Which county do you live in, Sacramento or Placer" << endl;
   
   cin >>county;
   
   if (county == "sacramento")
   
      tax = 7.75;
   
   if (county == "placer")
   
      tax = 7.25;
      
   else if (county == "Sacramento")
   
      tax = 7.75;
      
   else if (county == "Placer")
   
      tax = 7.25;
      
   taxactual = tax / 100;
   
   unitprice = units * price;
   
   taxtotal = unitprice * taxactual;
   
   total = unitprice + taxtotal;
   
   cout << "Your total price including tax is.....$" << total;
   
   return 0;

}
