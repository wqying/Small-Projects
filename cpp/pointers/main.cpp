#include <iostream>
#include <string>
using namespace std;

int* apply_all(int* arr1, int size1, int* arr2, int size2){
    int new_size = size1 * size2;
    int* array12 = new int[new_size];  // allocate a new array in memory
    
    int count = 0;
    
    for (size_t i=0; i<size2; ++i) {
        for (size_t j=0; j<size1; ++j) {
            array12[count] = arr1[j] * arr2[i];
            ++count;
        }
    }
    
    return array12;
}

void print(int* arr, int arr_size) {
    cout << "[ ";
    for (int i=0; i<arr_size; i++) {
        cout << arr[i] << ' ';
    }
    cout << "]";
}

int main()
{
    const size_t array1_size {5};
    const size_t array2_size {3};
    
    int array1[] {1,2,3,4,5};
    int array2[] {10,20,30};
    
    cout << "Array 1: ";
    print(array1,array1_size);
    cout << endl;
    
    cout << "Array 2: ";
    print(array2,array2_size);
    cout << endl;
    
    int *results = apply_all(array1, array1_size, array2, array2_size);
    constexpr size_t results_size {array1_size * array2_size};

    cout << "Result: ";
    print(results, results_size);
    
    cout << endl;

    return 0;
}