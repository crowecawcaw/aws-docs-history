End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Getting information about model packaging jobs

You can use the Amazon Lookout for Vision console and AWS SDK to get information about the model packaging jobs that you create.

###### Topics

- [Getting model packaging job information (Console)](#package-job-info-console "#package-job-info-console")
- [Getting model packaging job information (SDK)](#package-job-info-console-sdk "#package-job-info-console-sdk")

## Getting model packaging job information (Console)

###### To get model packaging job information (console)

1. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
2. Choose **Get started**.
3. In the left navigation pane, choose **Projects**.
4. In the **Projects** section, choose the project that contains the model packaging job you want to view.
5. In the left navigation pane, under the project name, choose **Edge model packages**.
6. In the **Model packaging job** section, choose the model packaging job that you want to view.
   The details page for the model packaging job is shown.

## Getting model packaging job information (SDK)

You can use the AWS SDK to list the model packaging jobs in a project and get information about
a specific model packaging job.

### List model packaging jobs

You can list the model packaging jobs in a project by calling the
[ListModelPackagingJobs](../APIReference/API_ListModelPackagingJobs.md "../APIReference/API_ListModelPackagingJobs.md") API.
The response includes a list of [ModelPackagingJobMetadata](../APIReference/API_ModelPackagingJobMetadata.md "../APIReference/API_ModelPackagingJobMetadata.md")
objects that provides information about each
model packaging job. Also included is a pagination token that you can use to get the next set of results, if the list
is incomplete.

###### To list your model packaging jobs

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following CLI command. Change `project_name` to the name of the project
   that you want to use.

```
aws lookoutvision list-model-packaging-jobs \
  --project-name `project_name` \
  --profile lookoutvision-access
```

### Describe a model packaging job

Use the [DescribeModelPackagingJob](../APIReference/API_DescribeModelPackagingJob.md "../APIReference/API_DescribeModelPackagingJob.md") API to get information about a model packaging job.
The response is a [ModelPackagingDescription](../APIReference/API_ModelPackagingDescription.md "../APIReference/API_ModelPackagingDescription.md")
object that includes the current status of the job and other information.

###### To describe a package

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following CLI command. Change the following:
   - `project_name` to the name of the project that you are using.
   - `job_name` to the name of the job. You get the job name (`JobName`)
     when you call [StartModelPackagingJob](../APIReference/API_StartModelPackagingJob.md "../APIReference/API_StartModelPackagingJob.md").

```
aws lookoutvision describe-model-packaging-job \
    --project-name `project_name` \
    --job-name `job_name` \
    --profile lookoutvision-access
```
