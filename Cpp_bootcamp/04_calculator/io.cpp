#include <iostream>
#include "io.h"

int getUserInput(){
    std::cout << "Enter an integer: ";
    int input{};
    std::cin >> input;

    return input;
}