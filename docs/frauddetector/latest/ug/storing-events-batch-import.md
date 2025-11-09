Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Store event data using batch import

With the batch import feature, you can quickly and easily upload large historical event datasets in Amazon Fraud Detector using the console,
the API, or the AWS SDK. To use batch import, create an input file in CSV format that contains all your event data, upload the CSV file onto Amazon S3 bucket,
and start an _Import_ job. Amazon Fraud Detector first validates the data based on the event type, and then automatically imports the entire dataset.
After the data is imported, it’s ready to be used for training new models or for re-training existing models.

## Input and output files

The input CSV file must contain headers that match the variables defined in the associated event type plus four mandatory variables. See
[Prepare event data for storage](prepare-storage-event-data.md "prepare-storage-event-data.md") for more information.
The maximum size of the input data file is 20 Gigabytes (GB), or about 50 million events. The number of events will vary by your event size.
If the import job was successful, the output file is empty. If the import was unsuccessful, the output file contains the error logs.

## Create a CSV file

Amazon Fraud Detector imports data only from files that are in the comma-separated values (CSV) format. The first row of your CSV file must contain column
headers that exactly match the variables defined in the associated event type plus four mandatory variables: EVENT_ID, EVENT_TIMESTAMP,
ENTITY_ID, and ENTITY_TYPE. You can also optionally include EVENT_LABEL and LABEL_TIMESTAMP (LABEL_TIMESTAMP is required if EVENT_LABEL
is included).

**Define mandatory variables**

Mandatory variables are considered as event metadata and they must be specified in uppercase. Event metadata are automatically included for model training.
The following table lists the mandatory variables, description of each variable, and required format for the variable.

| Name            | Description                                                                                                                                                                     | Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| EVENT_ID        | An identifier for the event. For example, if your event is an online transaction,<br>the EVENT_ID might be the transaction reference number that was provided to your customer. | • The EVENT_ID is required for batch import jobs.<br>• It must be unique for that event.<br>• It should represent information that’s meaningful to your business.<br>• It must satisfy the regular expression pattern (for example, `^[0-9a-z_-]+$.)`<br>• We don’t recommend that you append a timestamp to the EVENT_ID. Doing so might cause issues when you update the event.<br>This because you must provide the exact same EVENT_ID if you do this.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| EVENT_TIMESTAMP | The timestamp of when the event occurred. The timestamp must be in ISO 8601 standard in UTC.                                                                                    | • The EVENT_TIMESTAMP is required for batch import jobs.<br>• It must be specified in one of the following formats:<br>+ %yyyy-%mm-%ddT%hh:%mm:%ssZ (ISO 8601 standard in UTC only with no milliseconds)<br>Example: 2019-11-30T13:01:01Z<br>+ %yyyy/%mm/%dd %hh:%mm:%ss (AM/PM)<br>Examples: 2019/11/30 1:01:01 PM, or 2019/11/30 13:01:01<br>+ %mm/%dd/%yyyy %hh:%mm:%ss<br>Examples: 11/30/2019 1:01:01 PM, 11/30/2019 13:01:01<br>+ %mm/%dd/%yy %hh:%mm:%ss<br>Examples: 11/30/19 1:01:01 PM, 11/30/19 13:01:01<br>• Amazon Fraud Detector makes the following assumptions when parsing date/timestamp formats for event timestamps:<br>+ If you are using the ISO 8601 standard, it must be an exact match of the preceding specification<br>+ If you are using one of the other formats, there is additional flexibility:<br>• For months and days, you can provide single or double digits. For example, 1/12/2019 is a valid date.<br>• You do not need to include hh:mm:ss if you do not have them (that is, you can simply provide a date). You can also provide a subset<br>of just the hour and minutes (for example, hh:mm). Just providing hour is not supported. Milliseconds are also not supported.<br>• If you provide AM/PM labels, a 12-hour clock is assumed. If there is no AM/PM information, a 24-hour clock is assumed.<br>• You can use “/” or “-” as delimiters for the date elements. “:” is assumed for the timestamp elements. |
| ENTITY_ID       | An identifier for the entity performing the event.                                                                                                                              | • ENTITY_ID is required for batch import jobs<br>• It must follow the regular expression pattern: `^[0-9A-Za-z_.@+-]+$`.<br>• If the entity id isn’t available at the time of evaluation, specify the entity id as _unknown_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ENTITY_TYPE     | The entity that performs the event, such as a merchant or a customer                                                                                                            | ENTITY_TYPE is required for batch import jobs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| EVENT_LABEL     | Classifies the event as `fraudulent` or `legitimate`                                                                                                                            | EVENT_LABEL is required if LABEL_TIMESTAMP is included                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| LABEL_TIMESTAMP | The timestamp when the event label was last populated or updated                                                                                                                | • LABEL_TIMESTAMP is required if EVENT_LABEL is included.<br>• It must follow the timestamp format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Upload CSV file to Amazon S3 for batch import

After you create a CSV file with your data, upload the file to your Amazon Simple Storage Service (Amazon S3) bucket.

###### To upload event data to an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.

The **Create bucket** wizard opens. 3. In **Bucket name**, enter a DNS-compliant name for your
bucket.

The bucket name must:

    * Be unique across all of Amazon S3.
    * Be between 3 and 63 characters long.
    * Not contain uppercase characters.
    * Start with a lowercase letter or number.

After you create the bucket, you can't change its name. For information about naming
buckets, see [Bucket naming rules](../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/userguide/BucketRestrictions.md#bucketnamingrules") in the _Amazon Simple Storage Service User Guide_.

###### Important

Avoid including sensitive information, such as account numbers, in the bucket name.
The bucket name is visible in the URLs that point to the objects in the bucket. 4. In **Region**, choose the AWS Region where you want the bucket to
reside. You must select the same Region in which you are using Amazon Fraud Detector, that is US East (N. Virginia), US East (Ohio),
US West (Oregon), Europe (Ireland), Asia Pacific (Singapore) or Asia Pacific (Sydney). 5. In **Bucket settings for Block Public Access**, choose the Block
Public Access settings that you want to apply to the bucket.

We recommend that you leave all settings enabled. For more information about blocking public access, see
[Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_. 6. Choose **Create bucket**. 7. Upload training data file to your Amazon S3 bucket. Note the Amazon S3 location path for your training file (for example, s3://bucketname/object.csv).

## Batch import event data in Amazon Fraud Detector console

You can easily import large number of your event datasets in Amazon Fraud Detector console, using the `CreateBatchImportJob` API or using AWS SDK.
Before you proceed, make sure that you have followed instructions to prepare your dataset as a CSV file. Make sure that you also uploaded the CSV file to an
Amazon S3 bucket.

**Using Amazon Fraud Detector console**

###### To batch import event data in console

1. Open the AWS Console and sign in to your account, and navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Events**.
3. Choose your event type.
4. Select **Stored events** tab.
5. In the **Stored events details** pane, make sure that the **Event ingestion** is **ON**.
6. In the **Import events data** pane, choose **New Import**.
7. In the **New events import** page, provide the following information:
   - [Recommended] Leave **Enable Smart Data Validation for this dataset - new** set to the default setting.
   - For **IAM role for data**, select the IAM role that you created for the Amazon S3 bucket that holds the CSV file you are planning to import.
   - For **Input data location**, enter the S3 location where you have your CSV file.
   - If you want to specify a separate location to store your import results, click **Separate data location for inputs and results** button and provide a valid Amazon S3 bucket location.

###### Important

Make sure that the IAM role you selected has read permissions to your input Amazon S3 bucket and write permissions to your output Amazon S3 bucket. 8. Choose **Start**. 9. The **Status** column in **Import events data** pane displays the status of your validation and import job.
The banner at the top provides high level description of the status as your dataset first goes through validation and then the import. 10. Follow the guidance provided to [Monitor the progress of dataset validation and import job](#monitor-progress-sdv "#monitor-progress-sdv").

### Monitor the progress of dataset validation and import job

If you are using the Amazon Fraud Detector console to perform a batch import job, by default, Amazon Fraud Detector validates your dataset before import.
You can monitor the progress and status of validation and import jobs in the **New events import** page of the Amazon Fraud Detector
console. A banner at the top of the page provides a brief description of the validation findings and the status of the import job.
Depending on the validation findings and the status of your import job you might be required to take actions to ensure successful
validation and import of your dataset.

The following table provides details of the actions you must take depending on the outcome of validation and import operations.

| Banner message                                                                                                                                                           | Status                                     | What it means                                                                                                                                        | What should I do                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data validation has started                                                                                                                                              | Validation in progress                     | SDV has started validating your dataset                                                                                                              | Wait for the status to change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Data validation cannot proceed due to errors in your dataset.<br>Fix errors in your data file and start a new import job. See the validation report for more information | Validation failed                          | SDV identified issues in your data file. These issues must be addressed for successful import of your dataset.                                       | In the **Import events data\*<br>• pane, select the Job Id and view the validation report. Follow the<br>**Recommendations\*<br>• in the report to address all the errors listed. For more information, see [Using the validation report](#using-sdv-validation-report "#using-sdv-validation-report").                                                                                                                                                                                                                                                   |
| Data import has started. Validation completed successfully                                                                                                               | Import in progress                         | Your dataset passed the validation. AFD has started to import your dataset                                                                           | Wait for the status to change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Validation completed with warnings. Data import has started                                                                                                              | Import in progress                         | Some of the data in your dataset failed validation. However, the data that passed validation meets the minimum data<br>size requirements for import. | Monitor the message in the banner and wait for the status to change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Your data was partially imported. Some of the data failed validation and did not get imported. See validation report for more information.                               | Imported. The status shows a warning icon. | Some of the data in your data file that failed validation did not get imported. The rest of the data that passed validation was imported.            | In the **Import events data\*<br>• pane, select the Job Id and view the validation report. Follow the **Recommendations*<br>• in the \*\*Data level warnings*<br>• table to address the listed warnings.<br>You need not address all the warnings. However, make sure that your dataset has more than 50% of data that passes validation for a successful import.<br>After you have addressed the warnings, start a new import job. For more information, see [Using the validation report](#using-sdv-validation-report "#using-sdv-validation-report"). |
| Data import failed due to a processing error. Start a new data import job                                                                                                | Import failed                              | The import failed due to a transient run-time error                                                                                                  | Start a new import job                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Data was imported successfully                                                                                                                                           | Imported                                   | Both validation and import completed successfully                                                                                                    | Select the Job Id of your import job to view details and then proceed with model training                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

###### Note

We recommend waiting 10 minutes after the dataset has imported successfully into Amazon Fraud Detector to ensure
that they are fully ingested by the system.

### Smart Data Validation report

The Smart Data Validation creates a validation report after validation is complete. The validation report provides details of
all the issues that the SDV has identified in your dataset, with suggested actions to fix the most impactful issues. You can use
the validation report to determine what the issues are, where the issues are located in the dataset, the severity of the issues,
and how to fix them. The validation report is created even when the validation completes successfully. In this case, you can
view the report to see if there are any issues listed and if there are, decide if you want to fix any of those.

###### Note

The current version of SDV scans your dataset for issues that might cause the batch import to fail. If validation and batch
import succeed, your dataset can still have issues that might cause model training to fail. We recommend that you view your
validation report even if validation and import were successful, and address any issues listed in the report for successful model training.
After you have addressed the issues, create a new batch import job.

**Accessing the validation report**

You can access the validation report any time after the validation completes using one of the following options:

1. After the validation completes and while the import job is in progress, in the top banner, choose **View validation report**.
2. After the import job completes, in the **Import events data** pane, choose the Job ID of the import job that just completed.

#### Using the validation report

The validation report page of your import job provides the details of this import job, a list of critical errors if any are found,
a list of warnings about specific events (rows) in your dataset if found, and a brief summary of your dataset that includes information
such as values that are not valid, and missing values for each variable.

- **Import job details**

Provides details of the import job. If your import job has failed or your dataset was partially imported,
choose **Go to results file** to view the error logs of the events that failed to import.

- **Critical errors**

Provides details of the most impactful issues in your dataset identified by SDV. All the issues listed
in this pane are critical and you must address them before you proceed with import. If you try to import your dataset without addressing the critical issues,
your import job might fail.

To address the critical issues, follow the recommendations provided for each warning. After you have addressed all the issues listed in the Critical errors pane,
create a new batch import job.

- **Data level warnings**

Provides a summary of the warnings for specific events (rows) in your dataset. If the
Data level warnings pane is populated, some of the events in your dataset failed validation and were not imported.

For each warning, the **Description** column displays the number of events that has the issue. And the **Sample event IDs**
provides a partial list of sample event IDs you can use as a starting point to locate the rest of the events that have the issue. Use the
**Recommendation** provided for the warning to fix the issue. Also use the error logs from your output file for additional information about the issue.
The error logs are generated for all the events that failed batch import. To access error logs, in the **Import job details** pane,
choose **Go to results file**.

###### Note

If more than 50% of the events (rows) in your dataset failed validation, the import job also fails. In this case, you must fix the data before you start a new import job.

- **Dataset summary**

Provides a summary of the validation report of your dataset. If the Number of warnings column shows more than 0 warnings,
decide if you need to fix those warning. If the **Number of warnings** column shows 0s, continue to train your model.

## Batch import event data using the AWS SDK for Python (Boto3)

The following example shows a sample request for [CreateBatchImportJob](../api/API_CreateBatchImportJob.md "../api/API_CreateBatchImportJob.md") API. A batch import job must include a
**jobID**, **inputPath**, **outputPath**, **eventTypeName** and **iamRoleArn**.
The jobID can’t contain the same ID of a past job, unless the job exists in CREATE_FAILED state. The inputPath and outputPath must be valid S3 paths.
You can opt out of specifying the file name in the outputPath, however, you will still need to provide a valid S3 bucket location. The eventTypeName and iamRoleArn must exist.
The IAM role must grant read permissions to input Amazon S3 bucket and write permissions to output Amazon S3 bucket.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_batch_import_job (
jobId = 'sample_batch_import',
inputPath = 's3://bucket_name/input_file_name.csv',
outputPath = 's3://bucket_name/',
eventTypeName = 'sample_registration',
iamRoleArn: 'arn:aws:iam::************:role/service-role/AmazonFraudDetector-DataAccessRole-*************'
)

```

## Cancel batch import job

You can cancel an in-progress batch import job at any time in the Amazon Fraud Detector console, using the `CancelBatchImportJob` API, or AWS SDK.

###### To cancel a batch import job in console,

1. Open the AWS Console and sign in to your account, and navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Events**.
3. Choose your event type.
4. Select **Stored events** tab.
5. In the **Import events data** pane, choose the job Id of an in-progress import job you want to cancel.
6. In the event job page, click **Actions** and select **Cancel events import**.
7. Choose **Stop events import** to cancel the batch import job.

### Canceling batch import job using the AWS SDK for Python (Boto3)

The following example shows a sample request for the `CancelBatchImportJob` API. The cancel import job must include the
job ID of an in-progress batch import job.

```
import boto3
fraudDetector = boto3.client('frauddetector')
fraudDetector.cancel_batch_import_job (
    jobId = 'sample_batch'
)


```
