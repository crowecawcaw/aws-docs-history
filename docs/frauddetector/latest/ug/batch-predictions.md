Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Batch predictions

You can use a _batch predictions_ job in Amazon Fraud Detector to get
predictions for a set of events that do not require real-time scoring. For example, you
could create a batch predictions job to perform an offline proof-of-concept, or to
retrospectively evaluate the risk of events on an hourly, daily, or weekly basis.

You can create a batch prediction job using the [Amazon Fraud Detector console](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector"), or by calling the
[CreateBatchPredictionJob](../api/API_CreateBatchPredictionJob.md "../api/API_CreateBatchPredictionJob.md")API operation
using the AWS Command Line Interface (AWS CLI) or one of the Amazon Fraud Detector SDKs.

###### Topics

- [How batch predictions work](#how-batch-predictions-works "#how-batch-predictions-works")
- [Input and output files](#input-and-output-files "#input-and-output-files")
- [Getting batch predictions](#getting-batch-predictions "#getting-batch-predictions")
- [Guidance on IAM roles](#guidance-iam-roles "#guidance-iam-roles")
- [Get batch fraud predictions using the AWS SDK for Python (Boto3)](#get-a-batch-fraud-prediction-using-the-aws-python-sdk "#get-a-batch-fraud-prediction-using-the-aws-python-sdk")

## How batch predictions work

The `CreateBatchPredictionJob` API operation uses a specified detector
version to make predictions based on data provided in an input CSV file that is located
in an Amazon S3 bucket. The API then returns the resulting CSV file to an S3 bucket.

Batch prediction jobs calculate model scores and prediction outcomes in the same way
as the `GetEventPrediction` operation. Similar to
`GetEventPrediction`, to create a batch predictions job, you first create
an event type, optionally train a model, and then create a detector version that
evaluates the events in your batch job.

The pricing for event risk scores evaluated by batch prediction jobs is the same as the pricing for scores created by the `GetEventPrediction` API. For details, see [Amazon Fraud Detector pricing](https://aws.amazon.com/fraud-detector/pricing/ "https://aws.amazon.com/fraud-detector/pricing/").

You can only run one batch prediction job at a time.

## Input and output files

The input CSV file should contain headers that match the event type that is
associated with the selected detector version. The maximum size of the input data file
is 1GB. The number of events will vary by your event size.

Amazon Fraud Detector creates the output file in the same bucket as the input file, unless you specify a separate location for the output data. The output file contains the original data from the input file and the following appended columns:

- `MODEL_SCORES` — Details the model scores for the event from each model
  associated with the selected detector version.
- `OUTCOMES` — Details the event outcomes as evaluated by the selected
  detector version and its rules.
- `STATUS` — Indicates whether the event was evaluated successfully. If the
  event was not evaluated successfully, this column shows a reason code for the
  failure.
- `RULE_RESULTS` — A list of all the rules that matched, based on the rule execution mode.

## Getting batch predictions

The following steps assume that you have already created an event type, trained a
model using that event type (optional), and created a detector version for that event
type.

###### To get a batch prediction

1. Sign in to the AWS Management Console and open the Amazon Fraud Detector console at [https://console.aws.amazon.com/frauddetector](https://console.aws.amazon.com/frauddetector "https://console.aws.amazon.com/frauddetector").
2. In the left navigation pane of the Amazon Fraud Detector console, choose **Batch
   Predictions**, and then choose **New batch
   prediction**.
3. In **Job name**, specify a name for your batch prediction job. If you don’t specify a name, Amazon Fraud Detector randomly generates a job name.
4. In **Detector**, choose the detector for this batch
   prediction.
5. In **Detector version**, choose the detector version for this
   batch prediction. You can choose a detector version in any status. If your
   detector has a detector version in `Active` status, that version is
   automatically selected, but you can also change this selection if needed.
6. In **IAM role**, choose or create a role that has read and
   write access to your input and output Amazon S3 buckets. See [Guidance on IAM roles](#guidance-iam-roles "#guidance-iam-roles") for more information.

To get batch predictions, the IAM role that calls the
`CreateBatchPredictionJob` operation must have read permissions
to your input S3 bucket and write permissions to your output S3 bucket. For more
information about bucket permissions, see [User policy examples](../../../AmazonS3/latest/userguide/example-policies-s3.md "../../../AmazonS3/latest/userguide/example-policies-s3.md") in the _Amazon S3 User
Guide_. 7. In **Input data location**, specify the Amazon S3 location of your
input data. If you want the output file in a different S3 bucket, select
**Separate data location for output** and provide the Amazon S3
location for your output data. 8. (Optional) Create tags for your batch prediction job. 9. Choose **Start**.

Amazon Fraud Detector creates the batch prediction job, and the job's status is `In
 progress`. Batch prediction job processing times vary depending on the
number of events and your detector version configuration.

To stop a batch prediction job that is in progress, go to the batch prediction job
detail page, choose **Actions**, and then choose **Stop batch
prediction**. If you stop a batch prediction job, you won't receive any
results for the job.

When the batch prediction job's status changes to `Complete`, you can
retrieve the job's output from the designated output Amazon S3 bucket. The output file's name
is in the format `batch prediction job name_file creation
 timestamp_output.csv`. For example, the output file from a job named
`mybatchjob` is `mybatchjob_
 1611170650_output.csv`.

To search for specific events evaluated by a batch prediction job, in the left navigation pane of the Amazon Fraud Detector console, choose **Search past predictions**.

To delete a batch prediction job that has completed, go to the batch prediction job detail
page, choose **Actions** and then choose **Delete batch
prediction**.

## Guidance on IAM roles

To get batch predictions, the IAM role that calls the [CreateBatchPredictionJob](../api/API_CreateBatchPredictionJob.md "../api/API_CreateBatchPredictionJob.md") operation must have read permissions to your input S3 bucket and
write permissions to your output S3 bucket. For more information about bucket permissions, see User policy examples in the Amazon S3 User Guide. On the
Amazon Fraud Detector console, you have three options for selecting an IAM role for Batch Predictions:

1. Create a role when creating a new Batch Prediction job.
2. Select an existing IAM role that you have previously created in Amazon Fraud Detector console. Make sure to add the `S3:PutObject` permission to the role before you do this step.
3. Enter a custom ARN for a previously created IAM role.

If you receive an error related to your IAM role, verify the following:

1. Your Amazon S3 input and output buckets are in the same region as your detector.
2. The IAM role you are using has the `s3:GetObject` permission for your input S3 bucket and the `s3:PutObject` permission for your output S3 bucket.
3. The IAM role you are using has a trust policy for service principal `frauddetector.amazonaws.com`.

## Get batch fraud predictions using the AWS SDK for Python (Boto3)

The following example shows a sample request for the [CreateBatchPredictionJob](../api/API_CreateBatchPredictionJob.md "../api/API_CreateBatchPredictionJob.md") API. A batch prediction job must include the following existing resources: detector, detector version, and event type name. The following example assumes you have created an event type `sample_registration`, a detector `sample_detector`, and a detector version `1`.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_batch_prediction_job (
   jobId = 'sample_batch',
   inputPath = 's3://bucket_name/input_file_name.csv',
   outputPath = 's3://bucket_name/',
   eventTypeName = 'sample_registration',
   detectorName = 'sample_detector',
   detectorVersion = '1',
   iamRoleArn = 'arn:aws:iam::**:role/service-role/AmazonFraudDetector-DataAccessRole-**'
)


```
