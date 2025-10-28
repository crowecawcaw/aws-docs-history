We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Training Parameters

Typically, machine learning algorithms accept parameters that can be used to control
certain properties of the training process and of the resulting ML model. In Amazon Machine Learning, these are
called _training parameters_. You can set these parameters using the Amazon ML
console, API, or command line interface (CLI). If you do not set any parameters, Amazon ML will use default
values that are known to work well for a large range of machine learning tasks.

You can specify values for the following training parameters:

- Maximum model size
- Maximum number of passes over training data
- Shuffle
  type
- Regularization type
- Regularization amount
  In the Amazon ML console, the training parameters are set by default. The default settings are
  adequate for most ML problems, but you can choose other values to fine-tune the performance.
  Certain other training parameters, such as the learning rate, are configured for you based on
  your data.

The following sections provide more information about the training parameters.

## Maximum Model Size

The maximum model size is the total size, in units of bytes, of patterns that Amazon ML
creates during the training of an ML model.

By default, Amazon ML creates a 100 MB model. You can instruct Amazon ML to create a smaller or
larger model by specifying a different size. For the range of available sizes, see [Types of ML Models](types-of-ml-models.md "types-of-ml-models.md")

If Amazon ML can't find enough patterns to fill the model size, it creates a smaller model.
For example, if you specify a maximum model size of 100 MB, but Amazon ML finds patterns that total
only 50 MB, the resulting model will be 50 MB. If Amazon ML finds more patterns than will fit into
the specified size, it enforces a maximum cut-off by trimming the patterns that least affect
the quality of the learned model.

Choosing the model size allows you to control the trade-off between a model's predictive
quality and the cost of use. Smaller models can cause Amazon ML to remove many patterns to fit
within the maximum size limit, affecting the quality of predictions. Larger
models, on the other hand, cost more to query for real-time predictions.

###### Note

If you use an ML model to generate real-time predictions, you will incur a small
capacity reservation charge that is determined by the model's size. For more information,
see [Pricing for Amazon ML](pricing.md "pricing.md").

Larger input data sets do not necessarily result in larger models because models store
patterns, not input data; if the patterns are few and simple, the resulting model will be
small. Input data that has a large number of raw attributes (input columns) or derived
features (outputs of the Amazon ML data transformations) will likely have more patterns
found and stored during the training process. Picking the correct model size for your data
and problem is best approached with a few experiments. The Amazon ML model training log (which you
can download from the console or through the API) contains messages about how much model
trimming (if any) occurred during the training process, allowing you to estimate the potential
hit-to-prediction quality.

## Maximum Number of Passes over the Data

For best results, Amazon ML may need to make multiple passes over your data to discover
patterns. By default, Amazon ML makes 10 passes, but you can change the default by setting a
number up to 100. Amazon ML keeps track of the quality of patterns (model convergence) as it goes
along, and automatically stops the training when there are no more data points or patterns to
discover. For example, if you set the number of passes to 20, but Amazon ML discovers that no new
patterns can be found by the end of 15 passes, then it will stop the training at 15 passes.

In general, data sets with only a few observations typically require more passes over the
data to obtain higher model quality. Larger data sets often contain many similar data points,
which eliminates the need for a large number of passes. The impact of choosing more data passes
over your data is two-fold: model training takes longer, and it costs more.

## Shuffle Type for Training Data

In Amazon ML, you must shuffle your training data. Shuffling mixes up the order of your data so
that the SGD algorithm doesn't encounter one type of data for too many observations in
succession. For example, if you are training an ML model to predict a product type, and your
training data includes movie, toy, and video game product types, if you sorted the data by the
product type column before uploading it, the algorithm sees the data alphabetically by product
type. The algorithm sees all of your data for movies first, and your ML model begins to learn
patterns for movies. Then, when your model encounters data on toys, every update that the
algorithm makes would fit the model to the toy product type, even if those updates degrade the
patterns that fit movies. This sudden switch from movie to toy type can produce a model that
doesn't learn how to predict product types accurately.

You must shuffle your training data even if you chose the random split option when you
split the input datasource into training and evaluation portions. The random split strategy
chooses a random subset of the data for each datasource, but it doesn't change the order of
the rows in the datasource. For more information about splitting your data, see [Splitting Your Data](splitting-types.md "splitting-types.md").

When you create an ML model using the console, Amazon ML defaults to shuffling the data with a
pseudo-random shuffling technique. Regardless of the number of passes requested, Amazon ML shuffles
the data only once before training the ML model. If you shuffled your data before providing it
to Amazon ML and don't want Amazon ML to shuffle your data again, you can set the **Shuffle
type** to `none`. For example, if you randomly shuffled the records in
your .csv file before uploading it to Amazon S3, used the `rand()` function in your
MySQL SQL query when creating your datasource from Amazon RDS, or used the `random()`
function in your Amazon Redshift SQL query when creating your datasource from Amazon Redshift, setting
**Shuffle type** to `none` won't impact the predictive accuracy
of your ML model. Shuffling your data only once reduces the run-time and cost for creating an
ML model.

###### Important

When you create an ML model using the Amazon ML API, Amazon ML doesn't shuffle your data by
default. If you use the API instead of the console to create your ML model, we strongly
recommend that you shuffle your data by setting the `sgd.shuffleType` parameter
to
`auto`.

## Regularization Type and Amount

The predictive performance of complex ML models (those having many input attributes)
suffers when the data contains too many patterns. As the number of patterns
increases, so does the likelihood that the model learns unintentional data artifacts, rather
than true data patterns. In such a case, the model does very well on the training data, but
can’t generalize well on new data. This phenomenon is
known as _overfitting_ the training data.

Regularization helps prevent linear models from overfitting training data examples by
penalizing extreme weight values. L1 regularization reduces the number of
features used in the model by pushing the weight of features that would otherwise have
very small weights to zero. L1 regularization produces sparse models and reduces the amount of
noise in the model. L2 regularization results in smaller overall weight values, which stabilizes
the weights when there is high correlation between the features. You can
control the amount of L1 or L2 regularization by using the `Regularization amount`
parameter. Specifying an extremely large `Regularization 
 amount` value can cause all features to have zero weight.

Selecting and tuning the optimal regularization value is an active subject in machine
learning research. You will probably benefit from selecting a moderate amount of L2
regularization, which is the default in the Amazon ML console. Advanced users can choose between
three types of regularization (none, L1, or L2) and amount. For more information about
regularization, go to [Regularization (mathematics)](<http://en.wikipedia.org/wiki/Regularization_(mathematics)> "http://en.wikipedia.org/wiki/Regularization_(mathematics)").

## Training Parameters: Types and

Default Values

The following table lists the Amazon ML training parameters, along with the
default values and the allowable range for each.

| **Training Parameter**     | **Type** | **Default Value**                                                | **Description**                                                                                                                                                                                                                               |
| -------------------------- | -------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| maxMLModelSizeInBytes      | Integer  | 100,000,000 bytes (100 MiB)                                      | Allowable range: 100,000 (100 KiB) to 2,147,483,648 (2 GiB) Depending on the input data, the model size might affect the performance.                                                                                                         |
| sgd.maxPasses              | Integer  | 10                                                               | Allowable range: 1-100                                                                                                                                                                                                                        |
| sgd.shuffleType            | String   | auto                                                             | Allowable values: `auto` or `none`                                                                                                                                                                                                            |
| sgd.l1RegularizationAmount | Double   | 0 (By default, L1 isn't used)                                    | Allowable range: 0 to MAX_DOUBLE L1 values between 1E-4 and 1E-8 have been found to produce good results. Larger values are likely to produce models that aren't very useful. You can't set both L1 and L2. You must choose one or the other. |
| sgd.l2RegularizationAmount | Double   | 1E-6 (By default, L2 is used with this amount of regularization) | Allowable range: 0 to MAX_DOUBLE L2 values between 1E-2 and 1E-6 have been found to produce good results. Larger values are likely to produce models that aren't very useful. You can't set both L1 and L2. You must choose one or the other. |
