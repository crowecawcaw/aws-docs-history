# Importing bulk data into Amazon Personalize with a

dataset import job

After you have formatted your input data (see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md")) and
completed [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"),
you are ready to import your bulk data with a dataset import job.
A _dataset import job_ is a bulk import tool that
populates a dataset with data from Amazon S3.

To import data from Amazon S3, your CSV files must be in an
Amazon S3 bucket and you must give Amazon Personalize permission to access to your Amazon S3 resources:

- For information about uploading files to Amazon S3, see
  [Uploading Files and Folders by Using Drag and Drop](../../../AmazonS3/latest/user-guide/upload-objects.md "../../../AmazonS3/latest/user-guide/upload-objects.md") in the
  Amazon Simple Storage Service User Guide.
- For information about giving Amazon Personalize access to your files in Amazon S3, see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").
You can create a dataset
import job using the Amazon Personalize console, AWS Command Line Interface
(AWS CLI), or AWS SDKs. If you previously created a dataset import job for a dataset, you
can use a new dataset import job to add to or replace the existing bulk
data. For more information, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

If you import an item, user, or action with the same ID as a record that's already in your dataset, Amazon Personalize replaces it
with the new record. If you record two item interaction or action interaction
events with exactly the same timestamp and identical properties, Amazon Personalize keeps only one of the events.

After you import your data, you are ready to create domain recommenders (for Domain dataset groups) or custom resources (for
Custom dataset group) to train a model on your data. You use these resources to generate recommendations. For more
information, see [Domain recommenders in Amazon Personalize](creating-recommenders.md "creating-recommenders.md") or [Custom resources for training and deploying Amazon Personalize models](create-custom-resources.md "create-custom-resources.md").

###### Topics

- [Import modes](#bulk-import-modes "#bulk-import-modes")
- [Creating a dataset import job
  (console)](#bulk-data-import-console "#bulk-data-import-console")
- [Creating a dataset import job (AWS CLI)](#bulk-data-import-cli "#bulk-data-import-cli")
- [Creating a dataset import job (AWS SDKs)](#python-import-ex "#python-import-ex")

## Import modes

If you already created an import job for the dataset, you can configure how Amazon Personalize adds your new records. To do this, you specify
an import mode for your dataset import job. If you haven't imported bulk records, the **Import mode** field is not available in the
console and you can only specify `FULL` in the
`CreateDatasetImportJob` API operation. The default
is a full replacement.

- To overwrite all existing bulk data in your dataset, choose
  **Replace existing data** in the Amazon Personalize console or
  specify `FULL` in the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") API
  operation. This doesn't replace data you imported individually,
  including events recorded in real time.
- To append the records to the existing data in your dataset, choose
  **Add to existing data** or specify
  `INCREMENTAL` in the `CreateDatasetImportJob` API operation.
  Amazon Personalize replaces any record with the same ID with the new one.

###### Note

To append data to an Item interactions dataset or Action interactions dataset with a dataset import job, you must have at
minimum 1000 new item interaction or action interaction records.

## Creating a dataset import job

(console)

###### Important

By default, a dataset import job replaces any existing data in the
dataset that you imported in bulk. If you already imported bulk data, you can append data by changing the job's [import mode](#bulk-import-modes "#bulk-import-modes").

To import bulk records into a dataset with the Amazon Personalize console,
create a dataset import job with a name, the IAM service role, and the
location of your data.

If you just created your dataset in [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"), skip to step 5.

###### To import bulk records (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to
   your account.
2. On the **Dataset groups** page, choose your
   dataset group. The dataset group **Overview**
   displays.
3. In the navigation pane, choose **Datasets**
   and choose the dataset you want to import bulk data into.
4. In **Dataset import jobs**, choose **Create dataset import job**.
5. If this is your first dataset import job, for
   **Data import source** choose **Import
   data from S3**.
6. For **Dataset import job name**, specify a name
   for your import job.
7. If you already imported bulk data, for **Import mode**, choose how to update the dataset. Choose either
   **Replace existing data** or **Add to existing data**.
   data. This option doesn't appear if it's your first job for the dataset.
   For more information, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").
8. In **Data import source**, for **Data
   Location**, specify where your data file is stored in
   Amazon S3. Use the following syntax:

`s3:/amzn-s3-demo-bucket/<folder
 path>/<CSV filename>`

If your CSV files are in a folder in your Amazon S3 bucket and you
want to upload multiple CSV files to a dataset with one dataset
import job, you can specify the path to the folder. Amazon Personalize only uses the files
in the first level of your folder, it doesn't use any data in any sub folders.
Use the following syntax with a `/` after the folder name:

`s3:/amzn-s3-demo-bucket/<folder
 path>/` 9. In **IAM role**, choose to either create a new
role or use an existing one. If you completed the prerequisites,
choose **Use an existing service role** and specify
the role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"). 10. If you created a metric attribution and want to publish metrics related to this job to Amazon S3, in **Publish event metrics to S3**
choose **Publish metrics for this import job**.

If you haven't created one and want to publish metrics for this job, choose **Create metric attribution** to create
a new one on a different tab. After you create the metric attribution, you can return to this screen and finish creating the import job.

For more information on metric attributions, see
[Measuring the impact of Amazon Personalize recommendations](measuring-recommendation-impact.md "measuring-recommendation-impact.md"). 11. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
[Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md"). 12. Choose **Start import**. The data import job starts
and the **Dashboard Overview** page is
displayed. The dataset import is complete when the status shows as ACTIVE. After you import data into an Amazon Personalize dataset, you can [analyze it](analyzing-data.md "analyzing-data.md"), [export it to an Amazon S3 bucket](export-data.md "export-data.md"),
[update it](updating-datasets.md "updating-datasets.md"), or [delete it](delete-dataset.md "delete-dataset.md") by deleting the dataset.

After you import your data, you are ready to create domain recommenders (for Domain dataset groups) or custom resources (for
Custom dataset group) to train a model on your data. You use these resources to generate recommendations. For more
information, see [Domain recommenders in Amazon Personalize](creating-recommenders.md "creating-recommenders.md") or [Custom resources for training and deploying Amazon Personalize models](create-custom-resources.md "create-custom-resources.md").

## Creating a dataset import job (AWS CLI)

###### Important

By default, a dataset import job replaces any existing data in the
dataset that you imported in bulk. If you already imported bulk data, you can append data by changing the job's [import mode](#bulk-import-modes "#bulk-import-modes").

To import bulk records using the AWS CLI, create a dataset import job
using the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") command. If you've
previously created a dataset import job for a dataset, you can use the
import mode parameter to specify how to add the new data. For more information about updating existing bulk data,
see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

###### Import bulk records (AWS CLI)

1. Create a dataset import job by running the following command.
   Provide the Amazon Resource Name (ARN) for your dataset and specify
   the path to your Amazon S3 bucket where you stored the training data. Use
   the following syntax for the path:

`s3:/amzn-s3-demo-bucket/<folder
 path>/<CSV filename>`

If your CSV files are in a folder in your Amazon S3 bucket and you
want to upload multiple CSV files to a dataset with one dataset
import job, you can specify the path to the folder. Amazon Personalize only uses the files
in the first level of your folder, it doesn't use any data in any sub folders.
Use the following syntax with a `/` after the folder name:

`s3:/amzn-s3-demo-bucket/<folder
 path>/`

Provide the AWS Identity and Access Management (IAM) role Amazon Resource Name (ARN)
that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"). The default
`import-mode` is `FULL`. For more
information see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md"). For more information
about the operation, see [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md").

```
aws personalize create-dataset-import-job \
--job-name `dataset import job name` \
--dataset-arn `dataset arn` \
--data-source dataLocation=s3://`amzn-s3-demo-bucket`/`filename` \
--role-arn `roleArn` \
--import-mode `FULL`
```

The dataset import job ARN is displayed, as shown in the
following example.

```
{
  "datasetImportJobArn": "arn:aws:personalize:us-west-2:acct-id:dataset-import-job/DatasetImportJobName"
}
```

2. Check the status by using the
   `describe-dataset-import-job` command. Provide the
   dataset import job ARN that was returned in the previous step. For
   more information about the operation, see [DescribeDatasetImportJob](API_DescribeDatasetImportJob.md "API_DescribeDatasetImportJob.md").

```
aws personalize describe-dataset-import-job \
--dataset-import-job-arn `dataset import job arn`
```

The properties of the dataset import job, including its status,
are displayed. Initially, the `status` shows as CREATE
PENDING.

```
{
  "datasetImportJob": {
      "jobName": "Dataset Import job name",
      "datasetImportJobArn": "arn:aws:personalize:us-west-2:acct-id:dataset-import-job/DatasetImportJobArn",
      "datasetArn": "arn:aws:personalize:us-west-2:acct-id:dataset/DatasetGroupName/INTERACTIONS",
      "dataSource": {
          "dataLocation": "s3://amzn-s3-demo-bucket/ratings.csv"
      },
      "importMode": "FULL",
      "roleArn": "role-arn",
      "status": "CREATE PENDING",
      "creationDateTime": 1542392161.837,
      "lastUpdatedDateTime": 1542393013.377
  }
}
```

The dataset import is complete when the status shows as ACTIVE. After you import data into an Amazon Personalize dataset, you can [analyze it](analyzing-data.md "analyzing-data.md"), [export it to an Amazon S3 bucket](export-data.md "export-data.md"),
[update it](updating-datasets.md "updating-datasets.md"), or [delete it](delete-dataset.md "delete-dataset.md") by deleting the dataset.

After you import your data, you are ready to create domain recommenders (for Domain dataset groups) or custom resources (for
Custom dataset group) to train a model on your data. You use these resources to generate recommendations. For more
information, see [Domain recommenders in Amazon Personalize](creating-recommenders.md "creating-recommenders.md") or [Custom resources for training and deploying Amazon Personalize models](create-custom-resources.md "create-custom-resources.md").

## Creating a dataset import job (AWS SDKs)

###### Important

By default, a dataset import job replaces any existing data in the
dataset that you imported in bulk. If you already imported bulk data, you can append data by changing the job's [import mode](#bulk-import-modes "#bulk-import-modes").

To import data, create a dataset import job with the
[CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation. The following
code shows how to create a dataset import job.

Give the job name, set the `datasetArn` the Amazon
Resource Name (ARN) of your dataset, and set the
`dataLocation` to the path to your Amazon S3 bucket where
you stored the training data. Use the following syntax for the
path:

`s3:/amzn-s3-demo-bucket/<folder
 path>/<CSV filename>.csv`

If your CSV files are in a folder in your Amazon S3 bucket and you
want to upload multiple CSV files to a dataset with one dataset
import job, you can specify the path to the folder. Amazon Personalize only uses the files
in the first level of your folder, it doesn't use any data in any sub folders.
Use the following syntax with a `/` after the folder name:

`s3:/amzn-s3-demo-bucket/<folder
 path>/`

For the `roleArn`, specify the AWS Identity and Access Management (IAM)
role that gives Amazon Personalize permissions to access your S3 bucket.
See [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"). The
default `importMode` is `FULL`. This replaces all bulk data
in the dataset. To append data, set it to `INCREMENTAL`.
For more
information about updating existing bulk data, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

response = personalize.create_dataset_import_job(
    jobName = '`YourImportJob`',
    datasetArn = '`dataset_arn`',
    dataSource = {'dataLocation':'s3://`amzn-s3-demo-bucket`/`filename`.csv'},
    roleArn = '`role_arn`',
    importMode = 'FULL'
)

dsij_arn = response['datasetImportJobArn']

print ('Dataset Import Job arn: ' + dsij_arn)

description = personalize.describe_dataset_import_job(
    datasetImportJobArn = dsij_arn)['datasetImportJob']

print('Name: ' + description['jobName'])
print('ARN: ' + description['datasetImportJobArn'])
print('Status: ' + description['status'])
```

SDK for Java 2.x

```
public static String createPersonalizeDatasetImportJob(PersonalizeClient personalizeClient,
                                                      String jobName,
                                                      String datasetArn,
                                                      String s3BucketPath,
                                                      String roleArn,
                                                      ImportMode importMode) {

  long waitInMilliseconds = 60 * 1000;
  String status;
  String datasetImportJobArn;

  try {
      DataSource importDataSource = DataSource.builder()
              .dataLocation(s3BucketPath)
              .build();

      CreateDatasetImportJobRequest createDatasetImportJobRequest = CreateDatasetImportJobRequest.builder()
              .datasetArn(datasetArn)
              .dataSource(importDataSource)
              .jobName(jobName)
              .roleArn(roleArn)
              .importMode(importMode)
              .build();

      datasetImportJobArn = personalizeClient.createDatasetImportJob(createDatasetImportJobRequest)
              .datasetImportJobArn();

      DescribeDatasetImportJobRequest describeDatasetImportJobRequest = DescribeDatasetImportJobRequest.builder()
              .datasetImportJobArn(datasetImportJobArn)
              .build();

      long maxTime = Instant.now().getEpochSecond() + 3 * 60 * 60;

      while (Instant.now().getEpochSecond() < maxTime) {

          DatasetImportJob datasetImportJob = personalizeClient
                  .describeDatasetImportJob(describeDatasetImportJobRequest)
                  .datasetImportJob();

          status = datasetImportJob.status();
          System.out.println("Dataset import job status: " + status);

          if (status.equals("ACTIVE") || status.equals("CREATE FAILED")) {
              break;
          }
          try {
              Thread.sleep(waitInMilliseconds);
          } catch (InterruptedException e) {
              System.out.println(e.getMessage());
          }
      }
      return datasetImportJobArn;

  } catch (PersonalizeException e) {
      System.out.println(e.awsErrorDetails().errorMessage());
  }
  return "";
}
```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { CreateDatasetImportJobCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({
  region: "REGION"
});

// Set the dataset import job parameters.
export const datasetImportJobParam = {
  datasetArn: 'DATASET_ARN', /* required */
  dataSource: {
    dataLocation: 's3://amzn-s3-demo-bucket/<folderName>/<CSVfilename>.csv'  /* required */
  },
  jobName: 'NAME',           /* required */
  roleArn: 'ROLE_ARN',       /* required */
  importMode: "FULL"         /* optional, default is FULL */
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(new CreateDatasetImportJobCommand(datasetImportJobParam));
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```

The response from the [DescribeDatasetImportJob](API_DescribeDatasetImportJob.md "API_DescribeDatasetImportJob.md") operation includes the
status of the operation.

You must wait until the status changes to ACTIVE before you can use
the data to train a model.

The dataset import is complete when the status shows as ACTIVE. After you import data into an Amazon Personalize dataset, you can [analyze it](analyzing-data.md "analyzing-data.md"), [export it to an Amazon S3 bucket](export-data.md "export-data.md"),
[update it](updating-datasets.md "updating-datasets.md"), or [delete it](delete-dataset.md "delete-dataset.md") by deleting the dataset.

After you import your data, you are ready to create domain recommenders (for Domain dataset groups) or custom resources (for
Custom dataset group) to train a model on your data. You use these resources to generate recommendations. For more
information, see [Domain recommenders in Amazon Personalize](creating-recommenders.md "creating-recommenders.md") or [Custom resources for training and deploying Amazon Personalize models](create-custom-resources.md "create-custom-resources.md").
