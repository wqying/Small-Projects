#include <iostream>
using namespace std;

int* create_array(size_t size, int init_value = 0) {
	int* new_storage = new int[size];  // new_storage is a pointer on the stack in the scope
	// of create_array that points to an int array in the heap with 'size' slots
	// remember if we create a new array in the heap using 'new', must 'delete' it at some point
	// in our program otherwise memory leak
	for (size_t i = 0; i < size; ++i) {
		new_storage[i] = init_value;  // traverse down the array, starting from the 0th element
	}
	return new_storage;  // returns an int pointer new_storage that points to the int array
	// in the heap so that we can access the int array again after exiting this function's scope
}

void display(const int* const array, size_t size) {
	for (size_t i = 0; i < size; ++i) {
		cout << array[i] << ' ';
	}
	cout << endl;
}

int main() {
	int* myArray = nullptr;
	size_t myArray_size;
	int myArray_init_value = 0;

	cout << "How many integers would you like to allocate: " << endl;
	cin >> myArray_size;
	cout << "What value would you like to initialize them to: " << endl;
	cin >> myArray_init_value;

	myArray = create_array(myArray_size, myArray_init_value);
	display(myArray, myArray_size);
	delete [] myArray;
}