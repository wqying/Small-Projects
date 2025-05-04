#include <iostream>
using namespace std;

void swapPointers(int* ptr1, int* ptr2) {
	// int temp = *ptr2;
	// *ptr2 = *ptr1;
	// *ptr1 = temp;
	// Doing this without using additional variables:
	*ptr1 = *ptr1 + *ptr2;
	*ptr2 = *ptr1 - *ptr2;
	*ptr1 = *ptr1 - *ptr2;
}

int main() {
	int a = 5;
	int b = 10;

	int* ptrA = &a;
	int* ptrB = &b;

	swapPointers(ptrA, ptrB);

	cout << "new value of a: " << a << endl;
	cout << "new value of b: " << b << endl;
}