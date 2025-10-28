We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Reading the Batch Prediction Output Files

Perform the following steps to retrieve the batch prediction output
files:

1. Locate the batch prediction manifest file.
2. Read the manifest file to determine the locations of output files.
3. Retrieve the output files that contain the predictions.
4. Interpret the contents of the output files. Contents will vary based
   on the type of ML model that was used to generate predictions.
   The following sections describe the steps in greater detail.

## Locating the Batch Prediction Manifest File

The manifest files of the batch prediction contain the information that
maps your input files to the prediction output files.

To locate the manifest file, start with the output location that you specified when you
created the batch prediction object. You can query a completed batch prediction object to
retrieve the S3 location of this file by using either the [Amazon ML API](../APIReference.md "../APIReference.md")
or the [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").

The manifest file is located in the output location in a path that consists of the
static string `/batch-prediction/` appended to the output location and the name of
the manifest file, which is the ID of the batch prediction, with the extension
`.manifest` appended to that.

For example, if you create a batch prediction object with the ID
`bp-example`, and you specify the S3 location
`s3://examplebucket/output/` as the output location, you will find your manifest
file here:

`s3://examplebucket/output/batch-prediction/bp-example.manifest`

## Reading the Manifest File

The contents of the .manifest file are encoded as a JSON map, where the key is a string
of the name of an S3 input data file, and the value is a string of the associated batch
prediction result file. There is one mapping line for each input/output file pair. Continuing
with our example, if the input for the creation of the `BatchPrediction` object
consists of a single file called data.csv that is located in
`s3://examplebucket/input/`, you might see a mapping string that looks like
this:

```
{"s3://examplebucket/input/data.csv":"
s3://examplebucket/output/batch-prediction/result/bp-example-data.csv.gz"}
```

If the input to the creation of the `BatchPrediction` object consists of
three files called data1.csv, data2.csv, and data3.csv, and they are all stored in the S3
location `s3://examplebucket/input/`, you might see a mapping string that looks
like this:

```
{"s3://examplebucket/input/data1.csv":"s3://examplebucket/output/batch-prediction/result/bp-example-data1.csv.gz",

"s3://examplebucket/input/data2.csv":"
s3://examplebucket/output/batch-prediction/result/bp-example-data2.csv.gz",

"s3://examplebucket/input/data3.csv":"
s3://examplebucket/output/batch-prediction/result/bp-example-data3.csv.gz"}
```

## Retrieving the Batch Prediction Output Files

You can download each batch prediction file obtained from the manifest
mapping and process it locally. The file format is CSV, compressed with
the gzip algorithm. Within that file, there is one line per input
observation in the corresponding input file.

To join the predictions with the input file of the batch prediction, you
can perform a simple record-by-record merge of the two files. The output
file of the batch prediction always contains the same number of records
as the prediction input file, in the same order. If an input observation
fails in processing, and no prediction can be generated, the output file
of the batch prediction will have a blank line in the corresponding
location.

## Interpreting the Contents of Batch Prediction Files for a Binary Classification ML

model

The columns of the batch prediction file for a binary classification model are named
**bestAnswer** and **score**.

The **bestAnswer** column contains the prediction label ("1" or "0") that
is obtained by evaluating the prediction score against the cut-off score. For more information
about cut-off scores, see [Adjusting the Score Cut-off](evaluating_models.md "evaluating_models.md"). You set a cut-off score for the ML model by using
either the Amazon ML API or the model evaluation functionality on the Amazon ML console. If you don't
set a cut-off score,Amazon ML uses the default value of 0.5.

The **score** column contains the raw prediction score assigned by the ML
model for this prediction. Amazon ML uses logistic regression models, so this score attempts to
model the probability of the observation that corresponds to a true ("1") value. Note that the
**score** is reported in scientific notation, so in the first row of the
following example, the value 8.7642E-3 is equal to 0.0087642.

For example, if the cut-off score for the ML model is 0.75, the contents of the batch
prediction output file for a binary classification model might look like this:

```
bestAnswer,score

0,8.7642E-3

1,7.899012E-1


0,6.323061E-3

0,2.143189E-2


1,8.944209E-1
```

The second and fifth observations in the input file have received prediction scores above
0.75, so the bestAnswer column for these observations indicates value "1", while other
observations have the value "0".

## Interpreting the Contents of Batch Prediction Files for a Multiclass Classification ML

Model

The batch prediction file for a multiclass model contains one column for each class found
in the training data. Column names appear in the header line of the batch prediction
file.

When you request predictions from a multiclass model, Amazon ML computes several prediction
scores for each observation in the input file, one for each of the classes defined in the
input dataset. It is equivalent to asking "What is the probability (measured between 0 and 1)
that this observation will fall into this class, as opposed to any of the other classes?" Each
score can be interpreted as a "probability that the observation belongs to this class."
Because prediction scores model the underlying probabilities of the observation belonging to
one class or another, the sum of all the prediction scores across a row is 1. You need to pick
one class as the predicted class for the model. Most commonly, you would pick the class that
has the highest probability as the best answer.

For example, consider attempting to predict a customer's rating of a product, based on a
1-to-5 star scale. If the classes are named `1_star`, `2_stars`,
`3_stars`, `4_stars`, and `5_stars`, the multiclass
prediction output file might look like this:

```
1_star, 2_stars, 3_stars, 4_stars, 5_stars

8.7642E-3, 2.7195E-1, 4.77781E-1, 1.75411E-1, 6.6094E-2

5.59931E-1, 3.10E-4, 2.48E-4, 1.99871E-1, 2.39640E-1

7.19022E-1, 7.366E-3, 1.95411E-1, 8.78E-4, 7.7323E-2

1.89813E-1, 2.18956E-1, 2.48910E-1, 2.26103E-1, 1.16218E-1

3.129E-3, 8.944209E-1, 3.902E-3, 7.2191E-2, 2.6357E-2
```

In this example, the first observation has the highest prediction score for the
`3_stars` class (prediction score = 4.77781E-1), so you would interpret the
results as showing that class `3_stars` is the best answer for this observation.
Note that prediction scores are reported in scientific notation, so a prediction score of
4.77781E-1 is equal to 0.477781.

There may be circumstances when you do not want to choose the class with the highest
probability. For example, you might want to establish a minimum threshold below which you
won't consider a class as the best answer even if it has the highest prediction score. Suppose
you are classifying movies into genres, and you want the prediction score to be at least 5E-1
before you declare the genre to be your best answer. You get a prediction score of 3E-1 for
comedies, 2.5E-1 for dramas, 2.5E-1 for documentaries, and 2E-1 for action movies. In this
case, the ML model predicts that comedy is your most likely choice, but you decide not to
choose it as the best answer. Because none of the prediction scores exceeded your baseline
prediction score of 5E-1, you decide that the prediction is insufficient to confidently
predict the genre and you decide to choose something else. Your application might then treat
the genre field for this movie as "unknown."

## Interpreting the Contents of Batch Prediction Files for a Regression ML Model

The batch prediction file for a regression model contains a single column named
**score**. This column contains the raw numeric prediction for each
observation in the input data. The values are reported in scientific notation, so the
**score** value of -1.526385E1 is equal to -15.26835 in the first row in
the following example.

This example shows an output file for a batch prediction performed on a regression
model:

```
score

-1.526385E1

-6.188034E0

-1.271108E1

-2.200578E1

8.359159E0
```
