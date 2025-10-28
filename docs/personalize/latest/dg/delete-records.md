# Deleting users and their data with a data deletion job

After you import data, you can delete users and their data, including their metadata and interactions data, from a
dataset group. You might delete user data as part of a compliance program, or to address user deletion requests, or to keep
your data current as your user base changes.

After you delete users, Amazon Personalize no longer trains on their data and no longer considers the users when generating user
segments.

To delete references to users in Amazon Personalize datasets and models in a dataset group, you do the following:

1. Prepare a CSV file that lists the userIds of the users to delete in a USER_ID column.
2. Upload the CSV file to an Amazon S3 bucket. Your Amazon Personalize service role must have permission
   to access this bucket.
3. Create a data deletion job. A _data deletion job_ is a batch job that deletes users and their data from
   the models and datasets in a dataset group.

###### Topics

- [Guidelines and requirements](#data-deletion-guidelines-requirements "#data-deletion-guidelines-requirements")
- [Preparing a list of users to delete](#prepare-deletion-input-file "#prepare-deletion-input-file")
- [Creating a data deletion job](#creating-data-deletion-job "#creating-data-deletion-job")

## Guidelines and requirements

The following are guidelines and requirements for deleting users:

- Before you create a data deletion job, make sure no jobs that use your datasets are in progress, such as training jobs, batch jobs,
  or bulk or individual import operations. And avoid creating such jobs while a data deletion job is in progress.
  If any training or import occurs, we can't guarantee that the users' data will be deleted from models and we recommend creating an additional
  data deletion job.
- A data deletion job doesn’t delete references to users outside of Amazon Personalize. For example, it doesn’t delete their userId
  from batch recommendations in your Amazon S3 bucket. You must manually delete these records.
- You can have up to 5 deletion jobs for a dataset group with a status of PENDING.
- The maximum total size of your data deletion input file or files is 100 MB.
  You can reuse the same input file as you create deletion jobs.
- Each data deletion job deletes users and their interaction data in a _dataset group_. To delete their
  data in all dataset groups, you must create a data deletion job for each dataset group.
- After you create a job, it can take up to a day to delete the users' data from datasets and models.
- After a job completes, make sure to update any custom resources. Make sure to create a new solution version
  and, if necessary, update your campaign. If you use automatic training, you can still manually create new solution versions.
- Your Amazon Personalize service role must have permission to access your Amazon S3 bucket with the list of users to delete.
  It needs `GetObject` and `ListBucket` permissions for the bucket and its content.
  These permissions are the same as importing data. For information about granting permissions and policy
  examples, see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").
- You can't use your own AWS Key Management Service key on the Amazon S3 bucket that stores your list of userIds of the users to delete.
- If an item appears only in your Item interactions dataset dataset and only the users you are deleting interacted
  with this item, this item will no longer appear in recommendations.

## Preparing a list of users to delete

Before you delete users from Amazon Personalize, you must prepare a list of users to delete in a CSV file and upload it to Amazon S3.

###### To prepare the list of users to delete and upload it

1. Create a CSV file that lists the userIds of the users to delete. The following shows how your CSV file
   must be formatted.

```
USER_ID
abc
2a
5basc
ab35
123f
a55d
0v22
441fa
efg
```

2. Upload your CSV file to an Amazon Simple Storage Service ( Amazon S3)
   bucket. For more information about uploading files to Amazon S3, see
   [Uploading Files and Folders by Using Drag and Drop](../../../AmazonS3/latest/user-guide/upload-objects.md "../../../AmazonS3/latest/user-guide/upload-objects.md") in the
   Amazon Simple Storage Service User Guide.
3. Give Amazon Personalize access to your bucket and your CSV file.
   Amazon Personalize must have permission to perform the `GetObject` and `ListBucket` Actions on
   your bucket and its contents. These permissions are the same as importing data. For information about granting permissions and policy
   examples, see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

## Creating a data deletion job

After you complete [Preparing a list of users to delete](#prepare-deletion-input-file "#prepare-deletion-input-file"),
you are ready to delete the users with a data deletion job.

A _data deletion job_ is a batch job that deletes users and their data from
the models and datasets in a dataset group.
After you delete users, Amazon Personalize no longer trains on their data and no longer considers the users when generating user
segments.

When you create a data deletion job, you specify the Amazon S3 location of your list of users to delete.

- If your data is in a single file, use the following syntax for the Amazon S3 location:

`s3://amzn-s3-demo-bucket/<folder path>/<CSV filename>.csv`

- If your CSV files are in a folder in your Amazon S3 bucket,
  you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files with the `.csv` file extension in the folder and any sub folder. It ignores files of any other type.
  Use the following syntax with a `/` after the folder
  name:

`s3://amzn-s3-demo-bucket/<folder path>/`

The role you use must have permission to perform the `GetObject` and `ListBucket` Actions on
your Amazon S3 bucket and its contents. For information about granting permissions and policy
examples, see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").

You can create a data deletion job with the Amazon Personalize console, the AWS Command Line Interface (AWS CLI), or AWS SDKs.

To delete users with the Amazon Personalize console, create a data deletion job with a name, the IAM
service role, and the Amazon S3 location of your data.

###### To delete records (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your dataset group. The dataset group
   **Overview** displays.
3. In the navigation pane, choose **Datasets**.
4. In **Data deletion jobs**, choose **Create job**.
5. In **Job details**, give the job a name.
6. In **S3 Input source**, for **S3 Location**,
   specify the Amazon S3 location of the CSV file that stores the list of userIds of the users to delete.
   You prepared this file in [Preparing a list of users to delete](#prepare-deletion-input-file "#prepare-deletion-input-file").
7. In **IAM role**, choose to either create a new role or use an existing one. If you completed the
   prerequisites to create a role for Amazon Personalize and granted this role access to your Amazon S3 bucket,
   choose **Use an existing service role** and specify the role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions").

The role you use must have permission to perform the `GetObject` and `ListBucket` Actions on
your Amazon S3 bucket and its contents. These permissions are the same as importing data. For information about granting permissions and policy
examples, see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md"). 8. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
[Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md"). 9. Choose **Create job**. The job starts and the details page
displays.

After you create a job, it can about a day to delete the users' data from datasets and models.
Until the job completes, Amazon Personalize continues to use the data when training. And the users might appear in user segments.

Data deletion is complete when the status shows as COMPLETED. If the job fails for any reason,
we recommend creating another data deletion job. After a job completes, make sure to update any custom resources. Make sure to create a new solution version
and, if necessary, update your campaign. If you use automatic training, you can still manually create new solution versions.
To delete users with the AWS CLI, use the `create-data-deletion-job` command. This command uses the
CreateDataDeletion API operation. The following code shows how to create a data deletion job. To use the code, update it to
specify the jobs name, the IAM role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"), and the Amazon S3 location of your data.
You prepared this file in [Preparing a list of users to delete](#prepare-deletion-input-file "#prepare-deletion-input-file").

```
aws personalize create-data-deletion-job \
--job-name `deletion job name` \
--dataset-group-arn `dataset group ARN` \
--data-source dataLocation=s3://`amzn-s3-demo-bucket`/`filename`.csv \
--role-arn `roleArn`
```

After you create a job, it can about a day to delete the users' data from datasets and models.
Until the job completes, Amazon Personalize continues to use the data when training. And the users might appear in user segments.

The job is complete when the status is COMPLETED. Check the status by using the `describe-data-deletion-job`
command and specify the data deletion job ARN. For more information about the API
operation, see [DescribeDataDeletionJob](API_DescribeDataDeletionJob.md "API_DescribeDataDeletionJob.md").
To view a history of data deletion jobs sorted by creation time, use the [ListDataDeletionJobs](API_ListDataDeletionJobs.md "API_ListDataDeletionJobs.md")
API operation.

If the job fails for any reason,
we recommend creating another data deletion job. After a job completes, make sure to update any custom resources. Make sure to create a new solution version
and, if necessary, update your campaign. If you use automatic training, you can still manually create new solution versions.

To delete users with the AWS SDKs, use the
[CreateDataDeletionJob](API_CreateDataDeletionJob.md "API_CreateDataDeletionJob.md") API operation. The following code shows how to create a data deletion job. To use the code, update it to
specify the jobs name, the IAM role that you created in [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"), and the Amazon S3 location of your data. You prepared this file in [Preparing a list of users to delete](#prepare-deletion-input-file "#prepare-deletion-input-file").

```
import boto3

personalize = boto3.client('personalize')

response = personalize.create_data_deletion_job(
    jobName = '`Deletion job name`',
    datasetGroupArn = '`Dataset Group ARN`',
    dataSource = {'dataLocation':'s3://`amzn-s3-demo-bucket/file.csv`'},
    roleArn = '`role_arn`'
)

deletion_job_arn = response['dataDeletionJobArn']

print ('Deletion Job arn: ' + deletion_job_arn)

description = personalize.describe_data_deletion_job(
    dataDeletionJobArn = deletion_job_arn)['dataDeletionJob']

print('Name: ' + description['jobName'])
print('ARN: ' + description['dataDeletionJobArn'])
print('Status: ' + description['status'])
```

After you create a job, it can about a day to delete the users' data from datasets and models.
Until the job completes, Amazon Personalize continues to use the data when training. And the users might appear in user segments.

The job is complete when the status is COMPLETED. Check the status by using the [DescribeDataDeletionJob](API_DescribeDataDeletionJob.md "API_DescribeDataDeletionJob.md")
operation and specify the data deletion job ARN.
To view a history of data deletion jobs sorted by creation time, use the [ListDataDeletionJobs](API_ListDataDeletionJobs.md "API_ListDataDeletionJobs.md")
API operation.

If the job fails for any reason,
we recommend creating another data deletion job. After a job completes, make sure to update any custom resources. Make sure to create a new solution version
and, if necessary, update your campaign. If you use automatic training, you can still manually create new solution versions.
