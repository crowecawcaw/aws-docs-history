# How PCA Works

Principal Component Analysis (PCA) is a learning algorithm that reduces the
dimensionality (number of features) within a dataset while still retaining as much
information as possible.

PCA reduces dimensionality by finding a new set of features called
_components_, which are composites of the original features, but
are uncorrelated with one another. The first component accounts for the largest possible
variability in the data, the second component the second most variability, and so
on.

It is an unsupervised dimensionality reduction algorithm. In unsupervised learning,
labels that might be associated with the objects in the training dataset aren't
used.

Given the input of a matrix with rows
![x_1,…,x_n](images/PCA-39b.png)
each of dimension `1 * d`, the data is partitioned into
mini-batches of rows and distributed among the training nodes (workers). Each worker
then computes a summary of its data. The summaries of the different workers are then
unified into a single solution at the end of the computation.

**Modes**

The Amazon SageMaker AI PCA algorithm uses either of two modes to calculate these summaries,
depending on the situation:

- **regular**: for datasets with sparse data and a
  moderate number of observations and features.
- **randomized**: for datasets with both a large
  number of observations and features. This mode uses an approximation algorithm.
  As the algorithm's last step, it performs the singular value decomposition on the
  unified solution, from which the principal components are then derived.

## Mode 1: Regular

The workers jointly compute both
![Equation in text-form: \sum x_i^T x_i](images/PCA-1b.png)
and
![Equation in text-form: \sum x_i](images/PCA-2b.png)
.

###### Note

Because
![Equation in text-form: x_i](images/PCA-3b.png)
are `1 * d` row vectors,
![Equation in text-form: x_i^T x_i](images/PCA-4b.png)
is a matrix (not a scalar). Using row vectors within the
code allows us to obtain efficient caching.

The covariance matrix is computed as
![Equation in text-form: \sum x_i^T x_i - (1/n) (\sum x_i)^T \sum x_i](images/PCA-32b.png)
, and its top `num_components` singular vectors form
the model.

###### Note

If `subtract_mean` is `False`, we avoid computing and
subtracting
![Equation in text-form: \sum x_i](images/PCA-2b.png)
.

Use this algorithm when the dimension `d` of the vectors is small
enough so that
![Equation in text-form: d^2](images/PCA-7b.png)
can fit in memory.

## Mode 2: Randomized

When the number of features in the input dataset is large, we use a method to
approximate the covariance metric. For every mini-batch
![Equation in text-form: X_t](images/PCA-23b.png)
of dimension `b * d`, we randomly initialize a
`(num_components + extra_components) * b` matrix that we multiply by
each mini-batch, to create a `(num_components + extra_components) * d`
matrix. The sum of these matrices is computed by the workers, and the servers
perform SVD on the final `(num_components + extra_components) * d`
matrix. The top right `num_components` singular vectors of it are the
approximation of the top singular vectors of the input matrix.

Let
![Equation in text-form: \ell](images/PCA-38b.png)

`= num_components + extra_components`. Given a mini-batch
![Equation in text-form: X_t](images/PCA-23b.png)
of dimension `b * d`, the worker draws a random
matrix
![Equation in text-form: H_t](images/PCA-24b.png)
of dimension
![Equation in text-form: \ell * b](images/PCA-38.png)
. Depending on whether the environment uses a GPU or CPU and
the dimension size, the matrix is either a random sign matrix where each entry is
`+-1` or a _FJLT_ (fast Johnson Lindenstrauss
transform; for information, see [FJLT
Transforms](https://www.cs.princeton.edu/~chazelle/pubs/FJLT-sicomp09.pdf "https://www.cs.princeton.edu/~chazelle/pubs/FJLT-sicomp09.pdf") and the follow-up papers). The worker then computes
![Equation in text-form: H_t X_t](images/PCA-26b.png)
and maintains
![Equation in text-form: B = \sum H_t X_t](images/PCA-27b.png)
. The worker also maintains
![Equation in text-form: h^T](images/PCA-28b.png)
, the sum of columns of
![Equation in text-form: H_1,..,H_T](images/PCA-29b.png)
(`T` being the total number of mini-batches), and
`s`, the sum of all input rows. After processing the entire shard of
data, the worker sends the server `B`, `h`, `s`,
and `n` (the number of input rows).

Denote the different inputs to the server as
![Equation in text-form: B^1, h^1, s^1, n^1,…](images/PCA-30b.png)
The server computes `B`, `h`,
`s`, `n` the sums of the respective inputs. It then
computes
![Equation in text-form: C = B – (1/n) h^T s](images/PCA-31b.png)
, and finds its singular value decomposition. The top-right
singular vectors and singular values of `C` are used as the approximate
solution to the problem.
