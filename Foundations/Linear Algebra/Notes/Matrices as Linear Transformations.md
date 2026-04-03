* Transformation : a movement function that takes an input vector and spits out some out output vector

* A transformation is LINEAR if it has the following 3 properties:
    1. grid lines are parallel + evenly spaced
    2. Origin must remain fixed in place
    3. All lines must remain lines without getting curved

* A linear transformation will modify all vectors in a space, including the basis vectors
    - However, the property where you represent a vector as a linear combination of the unit vectors does not change, the scalars used in that linear combination do not change after a transformation
    - Therefore, if you know the unit vectors after a transformation, and the vector before a transformation, you can identify the vector after a transformation

* A linear combination in the 2D space, can be more simplify shown as a 2x2 matrix where the columns represent the transformed unit vectors
    * Same concept can be applied to a 3D space, where a 3x3 matrix now shows the linear transformation

* <mark>Matrix vector Multiplication</mark> : [a,b] * [i1, j1] = [a*i1 + b*j1, a*i2 + b*j2]
                                                      [i2, j2]
* Shear Transformation : represented my the matrix [(1,0), (1,1)] --> Here the parentheses are vertical transformed unit vectors, and the comma seperates the columns

* If the columns of a matrix are linearly dependent, in a 2D space, you will squish the transformed space into a 1D line. If it's a 3D space and 2 vectors are linearly dependent, all of the transformed space squished into a 2D space.

* A **composition** of two matrices is simply executing one linear transformation, and then another. 

* To find the final matrix that represents the composition of two matrices is the same as finding the product of those two matrices. This can be represented by the following:
    - Imagine that the first linear transformation matrix is being transformed again. This intuitively means that you need to find the new basis vectors after that transformation. So if you put each column of the first transformation (basis vectors modified once), through the second matrix, you can multiply the two matrixes by splitting it up into 2 vector-matrix multiplcations and then combining the result into 1 matrix.

* Thus matrix multiplication reads right to left (in order of transformations), like function notation.

* Order of matrix multiplication:
    1. NOT COMMUNITIVE, M1\*M2 != M2\*M1 --> because transforming M2 based on M1 is different that transforming M1 based on M2
    2. YES ASSOCIATIVE --> (AB)C = A-->B-->C AND A(BC) = A-->B-->C, so they are equal

* Higher dimension square dimension matrix multiplication follows the same general concept as 2D matrix multiplication.