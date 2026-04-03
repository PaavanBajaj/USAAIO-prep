* Any linear transformation is changed by a specific factor known as the <mark>determinant</mark> of that linear transformation
* If you imagine the area formed by the basis vectors in a regular 2D plane, and apply something like [(3,0),(0,2)], the area for all figures present in that original plane will change by a factor/determinant of 6
* Any linear transformation that squishes all vector values to a line (occurs when the columns are linearly dependent), will always have a determinant value of 0 in a 2D space. In a 3D space, if there is any linear dependence between columns, the determinant value is 0 as well.
* So following the same logic, if the determinant of a matrix is negative, that simply means that the linear transformation associated with that matrix inverts space
    - think about a sheet of paper to represent a 2D space. Flipping the paper over is adjacent to "inverting space" and thus, the determinant of the matrix that dictates that linear transformation will be 0
    - Can also be thought of using the unit vectors j hat and i hat. Normally, the y-axis basis vector j hat is to the left of the x-axis basic vector i hat. If a linear transformation changes that fact and j hat is transformed to be the the right of i hat, the matrix will have a negative determinant. How to see that fact in 3D space however?
    - the absolute value of the determinant still dictates the scale by which the area of any shape has changed

* Another way to think about determinants:
    - Imagine a graph that shows the value of the determinant as i hat rotates counter clockwise and approaches j hat. Because the unit vectors are getting closer and closer to being linearly dependent, the value of the determinant will slope down from 1 to 0. Once they occupy the same vector, the determinant is 0, and as i hat keeps moving counterclockwise, the value of the determinant should keep decreasing --> thus being negative

* In a 3 dimensional space, the solid object formed after a linear transformation of a 1x1x1 cube is called a <mark>parellelepiped</mark> or a solid object with parellelograms for each face of the object

* **Key Point**: In a 2D or 3D space, if you apply a linear transformation to any 2D or 3D unit shape, the area or volume of the resulting shape (or parellelepiped in a 3D space), will be the DETERMINANT of that matrix
    - Thus to find the determinant of a square matrix, simply compute the area formed by the transformed basis vectors AKA the columns of the matrix

* The determinant of two matrices multiplied is equivalent to the determinant of one matrix multiplied by the determinant of the second
    - This property is true because if you think about it intuitively, start with a unit box. If you transform it with a matrix with determinant 2, it's volume becomes 2. Transform it again with a matrix of determinant 3, its area becomes 2*3 = 6. This is the same as first finding the composition of the two matrices and then finding the determinant of that. 