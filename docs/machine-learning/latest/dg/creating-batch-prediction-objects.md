We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Creating a Batch Prediction

To create a batch prediction, you create a `BatchPrediction` object using either
the Amazon Machine Learning (Amazon ML) console or API. A `BatchPrediction` object describes a set of
predictions that Amazon ML generates by using your ML model and a set of input observations. When you
create a `BatchPrediction` object, Amazon ML starts an asynchronous workflow that computes
the predictions.

You must use the same schema for the datasource that you use to obtain batch predictions and
the datasource that you used to train the ML model that you query for predictions. The one
exception is that the datasource for a batch prediction doesn't need to include the target
attribute because Amazon ML predicts the target. If you provide the target attribute, Amazon ML ignores
its value.

## Creating a Batch Prediction (Console)

To create a batch prediction using the Amazon ML console, use the Create Batch Prediction
wizard.

###### To create a batch prediction (console)

1. Sign in to the AWS Management Console and open the Amazon Machine Learning console at
   [https://console.aws.amazon.com/machinelearning/](https://console.aws.amazon.com/machinelearning/ "https://console.aws.amazon.com/machinelearning/").
2. On the Amazon ML dashboard, under **Objects**, choose **Create
   new...**, and then choose **Batch prediction**.
3. Choose the Amazon ML model that you want to use to create the batch prediction.
4. To confirm that you want to use this model, choose
   **Continue**.
5. Choose the datasource that you want to create predictions for. The datasource must
   have the same schema as your model, although it doesn't need to include the target
   attribute.
6. Choose **Continue**.
7. For **S3 destination**, type the name of your S3 bucket.
8. Choose **Review**.
9. Review your settings and choose **Create batch prediction**.

## Creating a Batch Prediction (API)

To create a `BatchPrediction` object using the Amazon ML API, you must provide the
following parameters:

**Datasource ID**

The ID of the datasource that points to the observations for which you want
predictions. For example, if you want predictions for data in a file called
`s3://examplebucket/input.csv`, you would create a datasource object that
points to the data file, and then pass in the ID of that datasource with this
parameter.

**BatchPrediction ID**

The ID to assign to the batch prediction.

**ML Model ID**

The ID of the ML model that Amazon ML should query for the predictions.

**Output Uri**

The URI of the S3 bucket in which to store the output of the prediction. Amazon ML must
have permissions to write data to this bucket.

The `OutputUri` parameter must refer to an S3 path that ends with a
forward slash ('/') character, as shown in the following example:

s3://examplebucket/examplepath/

For information about configuring S3 permissions , see [Granting Amazon ML Permissions to Output Predictions to Amazon S3](granting-amazon-ml-permissions-to-output-predictions-to-amazon-s3.md "granting-amazon-ml-permissions-to-output-predictions-to-amazon-s3.md").

**(Optional) BatchPrediction Name**

(Optional) A human-readable name for your batch prediction.
