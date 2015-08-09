#include <iostream>
void greenEggsAndHam()
{
    std::cout << "Reached greenEggsAndHam at 3" << std::endl;
    int c = 0;
    int d = 1;
}

int greenBoysAreBlue()
{
    std::cout << "Reached greenBoysAreBlue at 9" << std::endl;
}

// I'm not here!

 // Still not here!
        /* I shouldn't be here either 
         * (Me neither!)
         * */

int main(void)
{
    std::cout << "Reached main at 20" << std::endl;
    int a = 0;
    int b = 0;
    greenEggsAndHam();
    greenBoysAreBlue();
}
