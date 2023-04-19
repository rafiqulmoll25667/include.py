#include <stdio.h>

int main() {
   float P, S, I;

   printf("Введите мощность лампы (в Вт): ");
   scanf("%f", &P);

   printf("Введите площадь поверхности, на которую падает свет (в м2): ");
   scanf("%f", &S);

   I = P / S;

   printf("Интенсивность света: %.2f люкс\n", I);

   return 0;
}
