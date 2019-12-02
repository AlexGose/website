Date: 2019-12-2
Title: A Model for Factoring Integers 
Tags: General Audience, Integer Programming, Math, Math Models
Summary: Using a familiar math problem from grade school, we'll show how to model, rather than solve, a much more difficult math problem.  You should be able to follow along with just a background in high school algebra. 

## Introduction

You probably remember math problems like these from grade school:

\begin{matrix}
	& & 1 & 1 & 3 \\
	& \times & 2 & 7 & 1 \\
	\hline
	& & & ? & 
\end{matrix}

You carefully multiplied the digits of the two integer factors and added each column, carrying over quantities when appropriate:

\begin{matrix}
	  &   &      & 1 & 1 & 3 \\
	  & & \times & 2 & 7 & 1 \\
	\hline
	  &   &    & 1 & 1 & 3 \\ 
	  &   & 7  & 9 & 1  &  \\
	+ & 2 & 2  & 6 & & \\
	\hline
	  & 3 & 0  & 6 & 2 & 3
\end{matrix}


And you also probably remember being asked to find the prime factors for a number (e.g., $8 = 2\times 2\times 2$).

However, you certainly weren't given a problem like this:
\begin{matrix}
	  &   &      & ? & ? & ? \\
	  & & \times & ? & ? & ? \\
	\hline
	  &   &    & ? & ? & ? \\ 
	  &   & ?  & ? & ?  &  \\
	+ & ? & ?  & ? & & \\
	\hline
	  & 2 & 9  & 2 & 1 & 3
\end{matrix}

This is the reverse of multiplying two integers.  You are being asked to factor the integer on the bottom, or find two multiplicative factors that produce the number.  There may be more than one answer (e.g., $16 = 4\times 4 = 8 \times 2$), or if the number on the bottom is a prime number, then there may be no answer at all.  (Note: in this case the number is not a prime.)

The discrepancy in difficulty between these two problems suggests that once you multiply two large numbers, the multiplication cannot be undone without a great deal of effort.  A computer can help multiply and factor larger numbers than are possible by hand, but this discrepancy persists.  Perhaps, one day, a clever way to quickly factor large integers will be discovered, but we do not have one today.

For centuries people have studied the properties of the numbers for their own sake, with little or no concern for their wider relevance [1].  However, the irreversible nature of multiplying numbers lies at the heart of modern cryptography [2], which makes browsing on the internet and performing online bank transactions safe.

In this blog post we'll model, rather than solve, the relatively easy problem of multiplying two integers.  This model can be used, with the help of a computer, to solve the harder problem of factoring integers, assuming they are not too large.  Maybe, in the future, someone will find a clever way to use a model like this to factor large integers quickly. 

Specifically, we'll use an [integer programming](https://en.wikipedia.org/wiki/Integer_programming) (IP) model.  For our purposes, an IP model can be thought of as a set of variables as well as equations and inequalities involving those variables.  With the help of a computer, we seek to find a solution, or specific values for all the variables, that satisfy the equations and inequalities.  

A deeper discussion of IP models is outside of the scope of this blog post, but they have practical applications in different industries, including everything from planning activities in a factory to scheduling delivery of packages.  Some aspects of IP models require a background in higher level math, but you should be able to follow this discussion with no more than a background in high school algebra.  

## Models

Before we begin constructing an IP model, let's discuss models more generally.  A model is an abstract representation of real-life developed for a specific purpose.  

For example, a model airplane is an abstract representation of a real-life airplane.  The model is abstract in the sense that it doesn't include all of the details, such as a working jet engine, that we would expect in a real-life airplane.  The details depend on the purpose of the model.  An airplane model designed for testing in a wind tunnel will be different from a child's toy.

A model airplane is an example of a physical model, but we can also use the language of mathematics to model real-life.  For example, if we wish to calculate the time $t$ in seconds for an object to drop a certain known distance of $x$ meters, without any initial push, then we could use the following equation:

$$t = \sqrt{\frac{2x}{9.8}}.$$

With this model, we ignore many details.  Some of those details, like the color of the object, are clearly irrelevant to the stated purpose of calculating the time to drop.  Other details, such as the object's size, are less obviously irrelevant.  If we are dropping baseballs in a vacuum, then this model would be appropriate, but if we were dropping feathers outside on a windy day, then the model would be less appropriate.  So, the context of the real-life situation matters, and there is an art to constructing models appropriate for a given situation.

In our case, we will construct a mathematical model to represent the calculations someone would do when multiplying two integers by hand on a piece of paper.  We could simply model this with the equation $xy = N$, where $N$ is the product of the two numbers $x$ and $y$, but the IP model we will construct will be more complicated.  This model was selected in order to more easily find a solution using a computer, which is the purpose of the model.  

## Variables

We'll revisit the problem in the introduction, using variables with numbered subscripts to represent the individual digits of the two factors as follows:
\begin{matrix}
	  &   &      & F_3 & F_2 & F_1 \\
	  & & \times & S_3 & S_2 & S_1 \\
	\hline
	  &   &    & ? & ? & ? \\ 
	  &   & ?  & ? & ?  &  \\
	+ & ? & ?  & ? & & \\
	\hline
	  & 2 & 9  & 2 & 1 & 3
\end{matrix}

Each of the factor digits must be a whole number between 0 and 9, with the possibility of being equal to 0 or 9. In other words, the variables $F_1,F_2,F_3,S_1,S_2,S_3$ are each a member of the set $\{0,1,2,\ldots,9\}$.

We could write the products of these variables in their appropriate places below the two factors.  Instead, we will use separate variables for those places as follows:

\begin{matrix}
	  &   &      & F_3 & F_2 & F_1 \\
	  & & \times & S_3 & S_2 & S_1 \\
	\hline
	  &   &    & P_{1,3} & P_{1,2} & P_{1,1} \\ 
	  &   & P_{2,3}  & P_{2,2} & P_{2,1}  &  \\
	+ & P_{3,3} & P_{3,2}  & P_{3,1} & & \\
	\hline
	  & 2 & 9  & 2 & 1 & 3
\end{matrix}

Each variable $P_{i,j}$ is a non-negative integer for each of the indices $i$ and $j$ equal to any of the values $1,2,$ or $3$ [3].  

## Constraints

With all of the variables established, we turn our attention to relating the variables to one another.  We will express these relationships using equations or inequalities, referring to each more generally as a constraint. They are called constraints because they limit the possible values that can be taken by the variables.

Relating the new variables to the digits of the factors should be familiar from elementary school.  For example, we would begin by multiplying the least significant digit of both factors and placing the result in the same column below those two digits $P_{2,1}=S_1\times F_1$.  Here are all the relationships between the factor digits and the $P$ variables [4]:

$$P_{1,1} = S_1 \times F_1,$$
$$P_{1,2} = S_1 \times F_2,$$
$$P_{1,3} = S_1 \times F_3,$$
$$P_{2,1} = S_2 \times F_1,$$
$$P_{2,2} = S_2 \times F_2,$$
$$P_{2,3} = S_2 \times F_3,$$
$$P_{3,1} = S_3 \times F_1,$$
$$P_{3,2} = S_3 \times F_2,$$
$$P_{3,3} = S_3 \times F_3.$$

When multiplying two integers by hand, we add the sum of each column of digits.  The value of the least significant digit of that sum is what we write for the corresponding digit in the final product, and we carry over the rest, after dividing by 10, to the next column.  Let $x_i$ represent the quantity carried over from the $i^{th}$ least significant digit column to the next most significant and adjacent column.  For example, the equation for the sum of values in the first column is given below:

$$P_{1,1} = 3 + x_1.$$

The collection of constraints for summing all of the remaining columns follows:

$$\frac{1}{10}x_1 + P_{1,2} + P_{2,1} = 1 + x_2,$$
$$\frac{1}{10}x_2 + P_{1,3} + P_{2,2} + P_{3,1} = 2 + x_3,$$
$$\frac{1}{10}x_3 +  P_{2,3} + P_{3,2} = 9 + x_4,$$
$$\frac{1}{10}x_4 + P_{3,3} = 2.$$

The constraints in this section, along with the variable definitions, define the integer program model below: 

$$P_{1,1} = S_1 \times F_1,$$
$$P_{1,2} = S_1 \times F_2,$$
$$P_{1,3} = S_1 \times F_3,$$
$$P_{2,1} = S_2 \times F_1,$$
$$P_{2,2} = S_2 \times F_2,$$
$$P_{2,3} = S_2 \times F_3,$$
$$P_{3,1} = S_3 \times F_1,$$
$$P_{3,2} = S_3 \times F_2,$$
$$P_{3,3} = S_3 \times F_3.$$
$$P_{1,1} = 3 + x_1,$$
$$\frac{1}{10}x_1 + P_{1,2} + P_{2,1} = 1 + x_2,$$
$$\frac{1}{10}x_2 + P_{1,3} + P_{2,2} + P_{3,1} = 2 + x_3,$$
$$\frac{1}{10}x_3 +  P_{2,3} + P_{3,2} = 9 + x_4,$$
$$\frac{1}{10}x_4 + P_{3,3} = 2,$$

$$P_{i,j}\geq 0 \text{ and } P_{i,j} \text{ is integer for all } i,j=1,2,3,$$
$$x_i \geq 0 \text{ and } x_i \text{ is integer for all } i=1,2,3,$$
$$F_1,F_2,F_3,S_1,S_2,S_3 \text{ are in the set } \{0,1,\ldots,9\}.$$

## Conclusion

The model we defined can be passed to a computer program to find values for the variables.  The values of the $F$ and $S$ variables give us the digits of the two factors, which gives us the two factors we seek.  The variable values can be found using the julia programming language with the [JuMP](http://www.juliaopt.org/JuMP.jl/v0.20.0/) package for example.  

The particular model used here is not typically used for factoring large integers in practice, since there are alternative approaches that lead to more efficient factorizations.  However, since no approach provides an efficient process for factoring large integers at the time this is being written, we can't say one perspective is better than another.  

Hopefully this serves as an interesting example of mixed integer program models and mathematical models more generally.  Perhaps by studying these particular IP models someone will figure out a way to factor large integers quickly.  It is also possible, and maybe more likely, that insights gained from trying to factor large integers without using IP models can provide insights into solving more than just the IP model presented here. 

## Notes

[1] See, e.g., Ore, Øystein. *Number Theory and Its History*. Dover Classics of Science and Mathematics. New York: Dover, 1988.

[2] For an advanced treatment, see, e.g., Crandall, Richard E., and Carl Pomerance. *Prime Numbers: A Computational Perspective*. 2nd ed. New York, NY: Springer, 2005.

[3] In grade school, if the product of two factor digits exceeded $10$, then you would write down the least significant digit of the product and carry over the rest to the next column.  We will avoid this by simply allowing the $P$ variables to take values greater than $10$.  In practice, this isn't an issue if we use a binary number system rather than a decimal number system.  We use decimal numbers here because they are more familiar to a general audience. 

[4] If you have a background in optimization, then you know that a constraint involving the multiplication of two variables has to be treated differently than constraints without variable multiplications.  Alternative constraints, involving inequalities, can be used to avoid such variable multiplications.  The details aren't necessary for this discussion.

