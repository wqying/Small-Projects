#include <iostream>
#include <string>
#include <vector>
using namespace std;

// swaps the value of two variables
// use pointers as references in the function to save computational efforts during runtime
void swap_data(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void display(const vector<string> *const v) {
	for (auto str: *v) {
		cout << str << ' ';
	}
}

void display(int* array, int last) {
	while (*array != last) {
		// *array++ reads from right to left: increment the array pointer (move to the next element)
		// and then dereference the pointer to show the value
		cout << *array++ << ' ';
	}
}

int main() {
	int x = 100;
	int y = 200;
	cout << "Original value of x and y: " << x << ' ' << y << endl;
	swap_data(&x, &y);
	cout << "New value of x and y: " << x << ' ' << y << endl;
	vector<string> characters {"Yoy", "Roy", "Troy"};
	display(&characters);
	cout << endl;
	int myArray[] {1, 2, 3, 4, 5, 6};
	display(myArray, 6);  // the value of an array is the address of the first element
	cout << endl;
	return 0;
}

