#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) because n the number of times the while loop is executed is determined by what n is.

b) O(n(log n)) because of the nested while loop in the for loop and number of iterations of the loop is dependant of j < n

c) 0(1 ^n) because there is one recursive call and the number of times is based of n or bunnies

## Exercise II

we have n stories
floor level is f
if the egg is thrown off > f breaks else it doesn't
come up with a way to minimize dropped to broken ratio

so we can take the n stories in as an input then to define the floor level take n divide it by half and then we can keep dropping the eggs on the halves of the half floor and never break the eggs and then go untill he are out of floors

For the run time complexity its O(log n) because we take n and keep dividing by 2 and probabaly do it recursively untill the base case floor is 0 and that means we are on ground floor and can't through any more eggs.
