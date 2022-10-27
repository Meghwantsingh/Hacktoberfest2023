QUESTION : Sandglass Star Pattern

* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
  

CODE : 

#include <stdio.h>
 
int main()
{
  int i, j, k, rows;
 
  printf("Enter the no. of rows: ");
  scanf("%d", &rows);
 
  printf("Output: \n\n");
  //upper half
  for (i = 1; i <= rows; i++)
  {
    for (k = 1; k < i; k++)
      printf(" ");
 
    for (j = i; j <= rows; j++)
      printf("* ");
 
    printf("\n");
  }
 
  //lower half
  for (i = rows - 1; i >= 1; i--)
  {
    for (k = 1; k < i; k++)
      printf(" ");
 
    for (j = i; j <= rows; j++)
      printf("* ");
 
    printf("\n");
  }
 
  return 0;
}
