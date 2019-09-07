#include <stdio.h>
#include <cs50.h>

//Function declaration
bool valid_triangle(float a, float b, float c); 

int main(void)
{
    //Requests for triangle sides values
    float a = get_float("Give me triangle side A: ");
    float b = get_float("Give me triangle side B: ");
    float c = get_float("Give me triangle side C: ");
    
    //Calculates the validity of the triangle using the valid_triangle function
    bool x = valid_triangle(a, b, c);
    
    //Prints whether the triangle validity is either "true" or "false" 
    printf("%s", x ? "Triangle Validity = true\n" : "Triangle Validity = false\n");
}

//Function definition
bool valid_triangle(float a, float b, float c) 
{
    while (a > 0 && b > 0 && c > 0)
    {
        if ((a + b > c) && (a + c > b) && (b + c > a)) 
        {
            return true; 
        }
        return false;
    }
    return false;
}

//cs50 solution
bool valid_triangle(float x, float y, float z)
{
    //check for all positive sides
    if (x <= 0 || y <= 0 || z <= 0)
    {
        return false;
    }
    
    //check that sum of any two sides is greater than third
    if ((x + y <= z) || (x + z <= y) || (y + z <= x))
    {
        return false;
    }
    
    //if we passed both tests, we're good!
    return true;
}
