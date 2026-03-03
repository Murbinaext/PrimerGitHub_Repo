#include <iostream>
#include "io.h"

int main(){

    //Pedimos primer numero
    int x {getUserInput() };
    std::cout << x << '\n';

    //Pedimos operacion matematica al usuario

    //Pedimos segundo numero
    int y {getUserInput() };
    std::cout << y << '\n';

    //Calculamos resultado
// std::cerr << "Prueba de codigo de error antes de result. \n";
    int result = x + y;

    //Imprimir resultado
    std::cout << "El resultado de la suma es : " << result << '\n';

    return 0;
}