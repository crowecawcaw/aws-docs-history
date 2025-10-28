# Creating a dataset export job in Amazon Personalize

You can create a dataset export job with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

## Creating a dataset export job (console)

After you import your data into a dataset and create an output Amazon S3 bucket, you can export the data to the bucket for
analysis. To export a dataset using the Amazon Personalize console, you create a dataset export job. For
information about creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.

Before you export a dataset, make sure that your Amazon Personalize service role can access and write to your output Amazon S3 bucket.
See [Dataset export job permissions requirements](export-permissions.md "export-permissions.md").

###### To create a dataset export job (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home").
2. In the navigation pane, choose **Dataset groups**.
3. On the **Dataset groups** page, choose your dataset group.
4. In the navigation pane, choose **Datasets**.
5. Choose the dataset that you want to export to an Amazon S3 bucket.
6. In **Dataset export jobs**, choose **Create dataset export job**.
7. In **Dataset export job details**, for **Dataset export job name**, enter a name
   for the export job.
8. For **IAM service role**, choose the Amazon Personalize service role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions").
9. For **Amazon S3 data output path**, enter the destination Amazon S3 bucket. Use the following syntax:

`s3://amzn-s3-demo-bucket/<folder path>` 10. If you are using AWS KMS for encryption, for **KMS key ARN**, enter the Amazon Resource Name (ARN)
for the AWS KMS key. 11. For **Export data type**, choose the type data to export based on how you originally imported the
data.

    * Choose **Bulk** to export only data that you imported in bulk using a dataset import job.
    * Choose **Incremental** to export only data that you imported individually using the console or
     the `PutEvents`, `PutUsers`, or `PutItems` operations.
    * Choose **Both** to export all of the data in the dataset.

12. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
    [Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md").
13. Choose **Create dataset export job**.

On the **Dataset overview** page, in **Dataset export jobs**, the job is listed
with an **Export job status**. The dataset export job is complete when the status is
**ACTIVE**. You can then download the data from the output Amazon S3 bucket. For information on
downloading objects from an Amazon S3 bucket, see [Downloading an object](../../../AmazonS3/latest/userguide/download-objects.md "../../../AmazonS3/latest/userguide/download-objects.md") in the _Amazon Simple Storage Service User Guide._.

## Creating a dataset export job (AWS CLI)

After you import your data into the dataset and create an output Amazon S3 bucket, you can export the dataset to the bucket
for analysis. To export a dataset using the AWS CLI, create a dataset export job using the
`create-dataset-export-job` AWS CLI command. For information about creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the
_Amazon Simple Storage Service User Guide_.

Before you export a dataset, make sure that the Amazon Personalize service role can access and write to your output Amazon S3 bucket. See
[Dataset export job permissions requirements](export-permissions.md "export-permissions.md").

The following is an example of the `create-dataset-export-job` AWS CLI command. Give the job a name, replace
`dataset arn` with the Amazon Resource Name (ARN) of the dataset that you want to export, and replace
`role ARN` with the ARN of the Amazon Personalize service role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"). In
`s3DataDestination`, for the `kmsKeyArn`, optionally provide the ARN for your AWS KMS key, and for the
`path` provide the path to your output Amazon S3 bucket.

For `ingestion-mode`, specify the data to export from the following options:

- Specify `BULK` to export only data that you imported in bulk using a dataset import job.
- Specify `PUT` to export only data that you imported individually using the console or the
  `PutEvents`, PutUsers, or `PutItems` operations.
- Specify `ALL` to export all of the data in the dataset.

For more information, see [CreateDatasetExportJob](API_CreateDatasetExportJob.md "API_CreateDatasetExportJob.md").

```
aws personalize create-dataset-export-job \
  --job-name `job name` \
  --dataset-arn `dataset ARN` \
  --job-output "{\"s3DataDestination\":{\"kmsKeyArn\":\"`kms key ARN`\",\"path\":\"s3://`amzn-s3-demo-bucket`/`folder-name`/\"}}" \
  --role-arn `role ARN` \
  --ingestion-mode `PUT`
```

The dataset export job ARN is displayed.

```
{
  "datasetExportJobArn": "arn:aws:personalize:us-west-2:acct-id:dataset-export-job/DatasetExportJobName"
}
```

Use the `DescribeDatasetExportJob` operation to check the status.

```
aws personalize describe-dataset-export-job \
  --dataset-export-job-arn `dataset export job ARN`
```

## Creating a dataset export job (AWS SDKs)

After you import your data into the dataset and create an output Amazon S3 bucket, you can export the dataset to the bucket
for analysis. To export a dataset using the AWS SDKs, create a dataset export job using the [CreateDatasetExportJob](API_CreateDatasetExportJob.md "API_CreateDatasetExportJob.md") operation. For information about
creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.

The following code shows how to create a dataset export job using the SDK for Python (Boto3) or the SDK for Java 2.x SDK.

Before you export a dataset, make sure that the Amazon Personalize service role can access and write to your output Amazon S3 bucket. See
[Dataset export job permissions requirements](export-permissions.md "export-permissions.md").

SDK for Python (Boto3)
Use the following `create_dataset_export_job` to export the data in a dataset to an Amazon S3 bucket. Give
the job a name, replace `dataset arn` with the Amazon Resource Name (ARN) of the dataset that you want to
export, and replace `role ARN` with the ARN of the Amazon Personalize service role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"). In
`s3DataDestination`, for the `kmsKeyArn`, optionally provide the ARN for your AWS KMS key, and
for the `path` provide the path to your output Amazon S3 bucket.

For `ingestionMode`, specify the data to export from the following options:

- Specify `BULK` to export only data that you imported in bulk using a dataset import job.
- Specify `PUT` to export only data that you imported individually using the console or the
  `PutEvents`, PutUsers, or `PutItems` operations.
- Specify `ALL` to export all of the data in the dataset.

```
import boto3

personalize = boto3.client('personalize')

response = personalize.create_dataset_export_job(
    jobName = '`job name`',
    datasetArn = '`dataset ARN`',
    jobOutput = {
      "s3DataDestination": {
        "kmsKeyArn": "`kms key ARN`",
        "path": "s3://`amzn-s3-demo-bucket/folder-name/`"
      }
    },
    roleArn = '`role ARN`',
    ingestionMode = '`PUT`'
)

dsej_arn = response['datasetExportJobArn']

print ('Dataset Export Job arn: ' + dsej_arn)

description = personalize.describe_dataset_export_job(
    datasetExportJobArn = dsej_arn)['datasetExportJob']

print('Name: ' + description['jobName'])
print('ARN: ' + description['datasetExportJobArn'])
print('Status: ' + description['status'])
```

SDK for Java 2.x
Use the following `createDatasetExportJob` method to create a dataset export job. Pass the following as
parameters: a PersonalizeClient, the name for your export job, the ARN of the dataset you want to export, the
ingestion mode, the path for the output Amazon S3 bucket, and the ARN for your AWS KMS key.

The `ingestionMode` can be one of the following options:

- Use `IngestionMode.BULK` to export only data that you imported in bulk using a dataset import job.
- Use `IngestionMode.PUT` to export only data that you imported individually using the console or the
  `PutEvents`, PutUsers, or `PutItems` operations.
- Use `IngestionMode.ALL` to export all of the data in the dataset.

```
public static void createDatasetExportJob(PersonalizeClient personalizeClient,
                                        String jobName,
                                        String datasetArn,
                                        IngestionMode ingestionMode,
                                        String roleArn,
                                        String s3BucketPath,
                                        String kmsKeyArn) {

    long waitInMilliseconds = 30 * 1000; // 30 seconds
    String status = null;

    try {
        S3DataConfig exportS3DataConfig = S3DataConfig.builder()
            .path(s3BucketPath)
            .kmsKeyArn(kmsKeyArn)
            .build();

        DatasetExportJobOutput jobOutput = DatasetExportJobOutput.builder()
            .s3DataDestination(exportS3DataConfig)
            .build();

        CreateDatasetExportJobRequest createRequest = CreateDatasetExportJobRequest.builder()
            .jobName(jobName)
            .datasetArn(datasetArn)
            .ingestionMode(ingestionMode)
            .jobOutput(jobOutput)
            .roleArn(roleArn)
            .build();

        String datasetExportJobArn = personalizeClient.createDatasetExportJob(createRequest).datasetExportJobArn();

        DescribeDatasetExportJobRequest describeDatasetExportJobRequest = DescribeDatasetExportJobRequest.builder()
            .datasetExportJobArn(datasetExportJobArn)
            .build();

        long maxTime = Instant.now().getEpochSecond() + 3 * 60 * 60;

        while (Instant.now().getEpochSecond() < maxTime) {

            DatasetExportJob datasetExportJob = personalizeClient.describeDatasetExportJob(describeDatasetExportJobRequest)
                .datasetExportJob();

            status = datasetExportJob.status();
            System.out.println("Export job status: " + status);

            if (status.equals("ACTIVE") || status.equals("CREATE FAILED")) {
                break;
            }
            try {
                Thread.sleep(waitInMilliseconds);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    } catch (PersonalizeException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
}
```
