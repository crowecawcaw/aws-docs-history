We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Training Parameters

The Amazon ML learning algorithm accepts parameters, called
hyperparameters
or training parameters, that allow you to control the quality of the resulting model.
Depending on the hyperparameter, Amazon ML auto-selects settings or provides static defaults for
the hyperparameters. Although default hyperparameter settings generally produce useful
models, you might be able to improve the predictive performance of your models by changing
hyperparameter values. The following sections describe common
hyperparameters
associated with learning algorithms for linear models, such as those created by Amazon ML.

## Learning Rate

The learning rate is a constant value used in the Stochastic Gradient Descent (SGD)
algorithm. Learning rate affects the speed at which the algorithm reaches (converges to)
the optimal weights. The SGD algorithm makes updates to
the weights of the linear model for every data
example it sees. The size of these updates is controlled by the learning rate. Too large a
learning rate might prevent the weights from approaching the optimal solution. Too small a
value results in the algorithm requiring many passes to approach the optimal
weights.

In Amazon ML, the learning rate is auto-selected based on your data.

## Model Size

If you have many input features, the number of possible patterns in the data can result
in a large model. Large models have practical implications, such as
requiring more RAM to hold the model while training and when generating
predictions. In
Amazon ML, you can reduce the model size by using L1 regularization or by specifically
restricting the model size by specifying the maximum size. Note that if you reduce the
model size too much, you could reduce your model's predictive power.

For information about the default model size, see [Training Parameters: Types and
Default Values](training-parameters.md#training-parameters-types-and-default-values "training-parameters.md#training-parameters-types-and-default-values"). For more information
about regularization, see [Regularization](#regularization "#regularization").

## Number of Passes

The SGD algorithm makes sequential passes over the training data. The `Number of
 passes` parameter controls the number of passes that the algorithm makes over the
training data. More passes result in a model that
fits
the data better (if the learning rate is not too large), but the benefit diminishes with
an increasing number of passes. For smaller data sets, you can significantly increase the
number of passes, which allows the learning algorithm to effectively fit the data more
closely. For extremely large datasets, a single pass might suffice.

For information about the default number of passes, see [Training Parameters: Types and
Default Values](training-parameters.md#training-parameters-types-and-default-values "training-parameters.md#training-parameters-types-and-default-values").

## Data Shuffling

In Amazon ML, you must shuffle your data because the
SGD algorithm is influenced by the order of the rows in the training data. Shuffling your training data results in
better ML models because it helps the SGD algorithm avoid solutions that are optimal for
the first type of data it sees, but not for the full range of data.
Shuffling mixes up the order of your data so that the SGD algorithm doesn't encounter one
type of data for too many observations in succession. If it sees only one type of data for
many successive weight updates, the algorithm might not be able to correct the model
weights for a new data type because the update might be too large. Additionally,
when the data isn't presented randomly, it's difficult for the algorithm to find the
optimal solution for all of the data types quickly; in some cases, the algorithm might
never find the optimal solution. Shuffling the training data helps the algorithm to
converge on the optimal solution sooner.

For example, say you want to train an ML model to predict a product type, and your
training data includes movie, toy, and video game product types. If you sort the data by
the product type column before uploading the data to Amazon S3, then the algorithm sees the
data alphabetically by product type. The algorithm sees all of your data for movies first,
and your ML model begins to learn patterns for movies. Then, when your model encounters
data on toys, every update that the algorithm makes would fit the model to the toy product
type, even if those updates degrade the patterns that fit movies. This sudden switch from
movie to toy type can produce a model that doesn't learn how
to predict product types accurately.

For information about the default shuffling type, see [Training Parameters: Types and
Default Values](training-parameters.md#training-parameters-types-and-default-values "training-parameters.md#training-parameters-types-and-default-values").

## Regularization

Regularization helps prevent linear models from overfitting training data examples (that is,
memorizing patterns instead of generalizing them) by
penalizing extreme weight values. L1 regularization has the effect of reducing the number
of features used in the model by pushing to zero the weights of features that would
otherwise have small weights. As a result, L1 regularization results in sparse models and
reduces the amount of noise in the model. L2 regularization results in smaller overall
weight values, and stabilizes the weights when there is high correlation between the input
features. You control the amount of L1 or L2 regularization applied by using the
`Regularization type` and `Regularization amount` parameters. An
extremely large regularization value could result in all
features having zero weights, preventing a model from learning patterns.

For information about the default regularization values, see [Training Parameters: Types and
Default Values](training-parameters.md#training-parameters-types-and-default-values "training-parameters.md#training-parameters-types-and-default-values").
