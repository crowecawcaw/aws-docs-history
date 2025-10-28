# Getting user segments with a batch segment job

If you used a USER_SEGMENTATION recipe, you can create batch segment
jobs to get user segments with your solution version. Each user segment is
sorted in descending order based on the probability that each user will
interact with items in your inventory. Depending on the recipe, your input
data must be a list of items ([Item-Affinity recipe](item-affinity-recipe.md "item-affinity-recipe.md")) or item attributes ([Item-Attribute-Affinity recipe](item-attribute-affinity-recipe.md "item-attribute-affinity-recipe.md")) in JSON format. You can
create a batch segment job with the Amazon Personalize console, the AWS Command Line Interface (AWS CLI),
or AWS SDKs.

When you create a batch segment job, you specify the Amazon S3 paths to your input and output locations.
Amazon S3 is prefix based. If you provide a prefix for the input data location, Amazon Personalize uses all files matching that prefix as input data.
For example, if you provide `s3://amzn-s3-demo-bucket/folderName` and your bucket also has a folder with a path of `s3://amzn-s3-demo-bucket/folderName_test`,
Amazon Personalize uses all files in both folders as input data. To use only the files within a specific folder as input data,
end the Amazon S3 path with a prefix delimiter, such as `/`: `s3://amzn-s3-demo-bucket/folderName/`
For more information about how Amazon S3 organizes objects, see [Organizing, listing, and working with your objects](../../../AmazonS3/latest/userguide/organizing-objects.md "../../../AmazonS3/latest/userguide/organizing-objects.md").

###### Topics

- [Creating a batch segment job
  (console)](#batch-segment-console "#batch-segment-console")
- [Creating a batch segment job (AWS CLI)](#batch-segment-cli "#batch-segment-cli")
- [Creating a batch segment job (AWS SDKs)](#batch-segment-sdk "#batch-segment-sdk")

## Creating a batch segment job

(console)

After you have completed [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md"), you are ready to create a batch
segment job. This procedure assumes that you have already created a
solution and a solution version (trained model) with a USER_SEGEMENTATION recipe.

###### To get create a batch segment job (console)

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Datasets group** page, choose your dataset group.
3. Choose **batch segment jobs** in the navigation pane,
   then choose **Create batch segment job**.
4. In **batch segment job details**, for **Batch segment job name**, specify a name for your batch
   segment job.
5. For **Solution**, choose the solution and then choose the **Solution version ID** that you want to
   use to generate the recommendations. You can create batch segment jobs only if you used a USER_SEGEMENTATION recipe.
6. For **Number of users**, optionally specify the number of users Amazon Personalize generates for each user segment. The default is 25.
   The maximum is 5 million.
7. For **Input source**, specify the Amazon S3 path
   to your input file or use the **Browse S3** to choose your Amazon S3 bucket.

Use the following syntax: `s3://amzn-s3-demo-bucket/<folder name>/<input JSON file name>.json`

Your input data must be in the correct
format for the recipe your solution uses. For input data examples see
[Batch segment job input and output JSON examples](prepare-input-data-user-segment.md#batch-segment-job-json-examples "prepare-input-data-user-segment.md#batch-segment-job-json-examples"). 8. For **Output destination**,
specify the path to your output location or use the **Browse S3** to choose your Amazon S3 bucket. We recommend
using a different location for your output data (either a folder or a different Amazon S3 bucket).

Use the following syntax: `s3://amzn-s3-demo-bucket/<output folder name>/` 9. For **IAM role**, choose one of the following:

    * Choose **Create and use new service role**
     and enter the **Service role name** to create a new role, or
    * If you've already created a role with the correct permissions,
     choose **Use an existing service role** and choose the IAM role.

The role you use must have read and write access to your input and output Amazon S3 buckets
respectively. 10. For **Filter configuration** optionally choose a filter to
apply a filter to the user segments. If your filter uses placeholder parameters,
make sure the values for the parameters are included in your input JSON. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values"). 11. For **Tags**, optionally add any tags. For more information about tagging Amazon Personalize resources, see
[Tagging Amazon Personalize resources](tagging-resources.md "tagging-resources.md"). 12. Choose **Create batch segment job**. Batch segment job creation starts and the **Batch segment jobs** page
appears with the **Batch segment job detail** section
displayed. 13. When the batch segment job's status changes to **Active**, you can retrieve the job's output from the designated output Amazon S3
bucket. The output file's name will be of the format
``input-name`.out`.

## Creating a batch segment job (AWS CLI)

After you have completed [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md"), you are ready to
create a batch segment job using the following `create-batch-segment-job` code.
Specify a job name, replace `Solution version ARN` with the Amazon Resource Name (ARN) of your solution version,
and replace the `IAM service role ARN` with the ARN of the IAM service role you created for Amazon Personalize during set up. This role must have read and write access to your input and output Amazon S3 buckets
respectively. For `num-results` specify the number of users you want Amazon Personalize to predict for each line of input data. The default is 25.
The maximum is 5 million.
Optionally provide a `filter-arn` to filter user segments. If your filter uses placeholder parameters,
make sure the values for the parameters are included in your input JSON. For more information, see [Filtering batch recommendations and user segments (custom resources)](filter-batch.md "filter-batch.md").

Replace `S3 input path` and `S3 output path` with the Amazon S3 path to your input file and output locations. We recommend
using a different location for your output data (either a folder or a different Amazon S3 bucket).
Use the following syntax for input and output locations:
`s3://amzn-s3-demo-bucket/<folder name>/<input JSON file name>.json` and `s3://amzn-s3-demo-bucket/<output folder name>/`.

```
`aws personalize create-batch-segment-job \
 --job-name `Job name` \
 --solution-version-arn `Solution version ARN` \
 --num-results `The number of predicted users` \
 --filter-arn `Filter ARN` \
 --job-input s3DataSource={path=s3://`S3 input path`} \
 --job-output s3DataDestination={path=s3://`S3 output path`} \
 --role-arn `IAM service role ARN``
`{
 "batchSegmentJobArn": "arn:aws:personalize:us-west-2:acct-id:batch-segment-job/batchSegmentJobName"
}`
```

## Creating a batch segment job (AWS SDKs)

After you have completed [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md"), you are ready to
create a batch segment job with the `CreateBatchSegmentJob` operation. The following code shows how to create a batch segment job.
Give the job a name, specify the Amazon Resource Name (ARN) of the solution version to use,
specify the ARN for your Amazon Personalize IAM role, and specify the Amazon S3 path to your input file and output locations. Your IAM service role must have read and write access to your input and output Amazon S3 buckets
respectively.

We recommend
using a different location for your output data (either a folder or a different Amazon S3 bucket). Use the following syntax for input and output locations:
`s3://amzn-s3-demo-bucket/<folder name>/<input JSON file name>.json` and `s3://amzn-s3-demo-bucket/<output folder name>/`.

For `numResults`, specify the number of users you want Amazon Personalize to predict for each line of input data. The default is 25.
The maximum is 5 million.
Optionally provide a `filterArn` to filter user segments. If your filter uses placeholder parameters,
make sure the values for the parameters are included in your input JSON. For more information, see [Filtering batch recommendations and user segments (custom resources)](filter-batch.md "filter-batch.md").

SDK for Python (Boto3)

```
import boto3

personalize_rec = boto3.client(service_name='personalize')

personalize_rec.create_batch_segment_job (
    solutionVersionArn = "`Solution version ARN`",
    jobName = "`Job name`",
    numResults = `25`,
    filterArn = "`Filter ARN`",
    roleArn = "`IAM service role ARN`",
    jobInput =
       {"s3DataSource": {"path": "`s3://amzn-s3-demo-bucket/<folder name>/<input JSON file name>.json`"}},
    jobOutput =
       {"s3DataDestination": {"path": "`s3://amzn-s3-demo-bucket/<output folder name>/`"}}
)
```

SDK for Java 2.x

```
public static String createBatchSegmentJob(PersonalizeClient personalizeClient,
                                                        String solutionVersionArn,
                                                        String jobName,
                                                        String filterArn,
                                                        int numResults,
                                                        String s3InputDataSourcePath,
                                                        String s3DataDestinationPath,
                                                        String roleArn,
                                                        String explorationWeight,
                                                        String explorationItemAgeCutOff) {

  long waitInMilliseconds = 60 * 1000;
  String status;
  String batchSegmentJobArn;

  try {
      // Set up data input and output parameters.
      S3DataConfig inputSource = S3DataConfig.builder()
              .path(s3InputDataSourcePath)
              .build();
      S3DataConfig outputDestination = S3DataConfig.builder()
              .path(s3DataDestinationPath)
              .build();

      BatchSegmentJobInput jobInput = BatchSegmentJobInput.builder()
              .s3DataSource(inputSource)
              .build();
      BatchSegmentJobOutput jobOutputLocation = BatchSegmentJobOutput.builder()
              .s3DataDestination(outputDestination)
              .build();


      CreateBatchSegmentJobRequest createBatchSegmentJobRequest = CreateBatchSegmentJobRequest.builder()
              .solutionVersionArn(solutionVersionArn)
              .filterArn(filterArn)
              .jobInput(jobInput)
              .jobOutput(jobOutputLocation)
              .jobName(jobName)
              .numResults(numResults)
              .roleArn(roleArn)
              .build();

      batchSegmentJobArn = personalizeClient.createBatchSegmentJob(createBatchSegmentJobRequest)
              .batchSegmentJobArn();
      DescribeBatchSegmentJobRequest describeBatchSegmentJobRequest = DescribeBatchSegmentJobRequest.builder()
              .batchSegmentJobArn(batchSegmentJobArn)
              .build();

      long maxTime = Instant.now().getEpochSecond() + 3 * 60 * 60;

      // wait until the batch segment job is complete.
      while (Instant.now().getEpochSecond() < maxTime) {

          BatchSegmentJob batchSegmentJob = personalizeClient
                  .describeBatchSegmentJob(describeBatchSegmentJobRequest)
                  .batchSegmentJob();

          status = batchSegmentJob.status();
          System.out.println("batch segment job status: " + status);

          if (status.equals("ACTIVE") || status.equals("CREATE FAILED")) {
              break;
          }
          try {
              Thread.sleep(waitInMilliseconds);
          } catch (InterruptedException e) {
              System.out.println(e.getMessage());
          }
      }
      return batchSegmentJobArn;

  } catch (PersonalizeException e) {
      System.out.println(e.awsErrorDetails().errorMessage());
  }
  return "";
}
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { CreateBatchSegmentJobCommand } from "@aws-sdk/client-personalize";
import { personalizeClient } from "./libs/personalizeClients.js";

// Or, create the client here.
// const personalizeClient = new PersonalizeClient({ region: "REGION"});

// Set the batch segment job's parameters.

export const createBatchSegmentJobParam = {
  jobName: "NAME",
  jobInput: {
    s3DataSource: {
      path: "INPUT_PATH",
    },
  },
  jobOutput: {
    s3DataDestination: {
      path: "OUTPUT_PATH",
    },
  },
  roleArn: "ROLE_ARN",
  solutionVersionArn: "SOLUTION_VERSION_ARN",
  numResults: 20,
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new CreateBatchSegmentJobCommand(createBatchSegmentJobParam),
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```

Processing the batch job might take a while to complete. You can check a job's status by
calling [DescribeBatchSegmentJob](API_DescribeBatchSegmentJob.md "API_DescribeBatchSegmentJob.md") and passing a
`batchSegmentJobArn` as the input parameter. You can also list all
Amazon Personalize batch segment jobs in your AWS environment by calling [ListBatchSegmentJobs](API_ListBatchSegmentJobs.md "API_ListBatchSegmentJobs.md").
