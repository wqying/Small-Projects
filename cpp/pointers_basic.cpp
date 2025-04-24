/*some simple examples to refresh on pointers*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int num = 10;
	cout << "The value of num is: " << num << endl;
	cout << "sizeof num is: " << sizeof num << endl;  // don't confuse the size of num with pointer
	cout << "Address of num is: "<< &num << endl;

	int *p;  // not initialized, points to garbage rn but still exists in memory so has an address
	cout << "The value of p is: " << p << endl;
	cout << "sizeof p is: " << sizeof p << endl;  // don't confuse the size of num with pointer
	cout << "Address of p is: "<< &p << endl;

	p = nullptr;
	cout << "The value of p is: " << p << endl;

	int score = 100;
	// double high_temp = 100.7;

	int* score_ptr = &score;  // score_ptr points towards the address of score
	cout << "The value of ptr: " << score_ptr << endl;
	cout << "The value of the mem add that ptr is pointing to: " << *score_ptr << endl;  // dereference

	*score_ptr = 200;  // deference score ptr and change the value of the mem add
	cout << score << endl;

	string name = "Frank";
	string* string_ptr = &name;

	cout << "Originial name: " <<*string_ptr << endl;  // *string_ptr = name
	name = "James";
	cout << "New name: " <<*string_ptr << endl;

	vector<string> stoogers = {"Larry", "Moe", "Curly"};
	vector<string>* vector_ptr = nullptr;

	vector_ptr = &stoogers;
	// cannot index thru pointers:
	// stoogers[0] is allowed, but *vector_ptr[0] is not
	// instead, if we want to use pointers we would use .at()
	cout << "First stooge: " << (*vector_ptr).at(0) << endl;

	cout << "Stoogers: ";
	for (auto stooge : *vector_ptr) {  // same as: for (auto stooge : stoogers)
		cout << stooge << " ";
	}
	cout << endl;
}
