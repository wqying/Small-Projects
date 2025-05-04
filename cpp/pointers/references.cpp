#include <string>
#include <iostream>
#include <vector>
using namespace std;



int main() {
	vector<string> head_dancers = {"Paige", "Kaitlen", "Ying"};

	for(auto const &head_str:head_dancers)  // use const bc we don't want to accidentally
	// change the elements in the original vector through alias
		cout << head_str << endl;

	return 0;	
}