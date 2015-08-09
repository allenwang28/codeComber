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
    {
        std::cout << "Reached greenBoysAreBlue at 10" << std::endl;
    }
}

// I'm not here!

 // Still not here!
        /* I shouldn't be here either 
         * (Me neither!)
         * */

int main(void)
{
    std::cout << "Reached main at 22" << std::endl;
    int a = 0;
    int b = 0;
    greenEggsAndHam();
    greenBoysAreBlue();
    if (a == b)
    {
        std::cout << "Reached main at 28" << std::endl;
        a = 1;
    }
}
