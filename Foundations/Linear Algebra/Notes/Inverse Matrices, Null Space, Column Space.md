* System of linear equations can be represented as one matrix*vector equals a constant vector equation
    - We can denote the coefficent matrix as A, the variable vector as x, and the constant vector as v
    - So if we apply the geometric concept, we are looking for a vector x that after applying a transformation A, gets us v. Ax = v
* To actually calculate this, we must apply the <mark>inverse transformation of A</mark> to v to find x
    - Inverse transformation defined as $A^-1$. $A^-1 * A = $ unit matrix
    - To calculate the inverse matrix of any 2x2 or 3x3 matrix easily, the formula is $A^-1 = 1/(det(A)) * adj(A)$ where adj is simply an operation where convert the matrix into minors,apply a "checkerboard" of signs and finally transpose the matrix by swapping the rows and columns
* **Rank**: how many dimensions the transformed matrix transforms all vectors onto. If it is a line, the rank is 1, a plane is 2, etc.
    - If the rank is the same as the number of dimensions in the original matrix, it is called **full rank**
* The *span* of the columns of a matrix are called the **column space**
    - Therefore, rank can also be defined as the # of dimensions in the column space
* The **null space/kernal** of a linear transformation are all the vectors,planes,etc. that land on the origin of the graph. Techincally, in a full rank transformation, the origin is the only "null space" of a linear transformation, but in non-full rank transformations, it could be a lot more
    - In the context of *inverse transformations*, if the constant vector v is the origin, the null space of the transformation gives you the solution(s) of the vector x.