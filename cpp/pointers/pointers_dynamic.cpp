// Dynamic Memory Allocation
// Allocating storage from the heap at runtime
#include <iostream>
using namespace std;

int main() {
	int* int_ptr = nullptr;

	int_ptr = new int;  // storage for integer is going to be allocated in the heap
	// address is stored in int_ptr now
	cout << int_ptr << endl;
	delete int_ptr;

	size_t size = 0;
	double* temp_ptr = nullptr;

	cout << "How many temps: " << endl;
	cin >> size;

	temp_ptr = new double[size];
	cout << temp_ptr << endl;  // output will be the addres of the first element in the array
	delete [] temp_ptr;  // must include "[]" because this is an array
}