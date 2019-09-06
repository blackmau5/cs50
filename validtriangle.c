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
        if (a + b > c && a + c > b && b + c > a) 
        {
            return true; 
        }
        return false;
    }
    return false;
}
