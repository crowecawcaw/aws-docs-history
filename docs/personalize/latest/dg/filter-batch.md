# Filtering batch recommendations and user segments (custom resources)

Filtering batch recommendations and user segments works nearly the same as filtering
real-time recommendations. It follows the same workflow described
in [Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").
To filter batch recommendations or user segments, you do the following:

1. Create a filter just like you would for real-time recommendations. For more information, see [Filtering real-time recommendations](filter-real-time.md "filter-real-time.md").
2. Prepare your input data and upload it to Amazon S3 as described in [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md")
   or [Preparing input data for user segments](prepare-input-data-user-segment.md "prepare-input-data-user-segment.md").
   If your filter uses placeholder parameters, you must add an additional `filterValues` object.
   For more information, see [Providing filter values in your input JSON](#providing-filter-values "#providing-filter-values").
   If your filter doesn't use placeholder parameters, your input data can follow the examples in [Batch inference job input and output JSON examples](batch-data-upload.md#batch-inference-job-json-examples "batch-data-upload.md#batch-inference-job-json-examples")
   [Batch segment job input and output JSON examples](prepare-input-data-user-segment.md#batch-segment-job-json-examples "prepare-input-data-user-segment.md#batch-segment-job-json-examples")
3. Create a separate location for your output data, either a folder or a different Amazon S3 bucket.
4. Create a [batch inference job](creating-batch-inference-job.md "creating-batch-inference-job.md")
   or a [batch segment job](creating-batch-seg-job.md "creating-batch-seg-job.md"). When you create the job, specify the Amazon Resource Name (ARN) of your filter.
5. When the batch inference or batch segment job is complete, retrieve the recommendations or user segments from your output location in Amazon S3.

###### Topics

- [Providing filter values in your input JSON](#providing-filter-values "#providing-filter-values")
- [Filtering batch workflows
  (console)](#filter-batch-recommendations-console "#filter-batch-recommendations-console")
- [Filtering batch workflows (AWS
  SDKs)](#filter-batch-recommendations-sdk "#filter-batch-recommendations-sdk")

## Providing filter values in your input JSON

For filters with placeholder parameters, such as `$GENRE`, you must provide the values for the parameters
in a `filterValues` object in your input JSON. For a `filterValues`
object, each key is a parameter name. Each value is the criteria that you are passing as a
parameter. Surround each value with escaped quotes: `"filterValues":{"GENRES":"\"drama\""}`.
For multiple values, separate each value with a comma: `"filterValues":{"GENRES":"\"horror\",\"comedy\",\"drama\""}`

**Batch inference job input JSON example**

The following is an example
of the first few lines of a JSON input file for a _batch inference job_. The example includes
the `filterValues` object. The `GENRES` key corresponds to a
`$GENRES` placeholder in the filter expression. The job in this example uses the User-Personalization recipe. For RELATED_ITEMS recipes, provide an itemId
instead of the userId. For PERSONALIZED_RANKING recipes provide the userID and an itemList.

```

{"userId": "5","filterValues":{"GENRES":"\"horror\",\"comedy\",\"drama\""}}
{"userId": "3","filterValues":{"GENRES":"\"horror\",\"comedy\""}}
{"userId": "34","filterValues":{"GENRES":"\"drama\""}}

```

For more examples of batch inference job input data by recipe see [Batch inference job input and output JSON examples](batch-data-upload.md#batch-inference-job-json-examples "batch-data-upload.md#batch-inference-job-json-examples").
You can use these examples as a starting point and add the `filterValues` object from the above example.

**Batch segment job input JSON example**

The following is an example
of the first few lines of a JSON input file with filter values for a _batch segment job_. The `GENRES` key corresponds to a
`$GENRES` placeholder in the filter expression.

```

{"itemAttributes": "ITEMS.genres = \"Comedy\" AND ITEMS.genres = \"Action\"","filterValues":{"COUNTRY":"\"Japan\""}}
{"itemAttributes": "ITEMS.genres = \"Horror\"","filterValues":{"COUNTRY":"\"United States\"\""}}
{"itemAttributes": "ITEMS.genres = \"Action\" AND ITEMS.genres = \"Adventure\"","filterValues":{"COUNTRY":"\"England\""}}

```

For more examples of batch inference job input data by recipe see [Batch segment job input and output JSON examples](prepare-input-data-user-segment.md#batch-segment-job-json-examples "prepare-input-data-user-segment.md#batch-segment-job-json-examples").
You can use these examples as a starting point and add the `filterValues` object from the above example.

## Filtering batch workflows

(console)

To filter batch workflows with the Amazon Personalize console, you create a filter and then you create a batch inference job or batch segment job and choose the filter.
For complete step by step instructions,
see [Creating a batch inference job (console)](creating-batch-inference-job.md#batch-console "creating-batch-inference-job.md#batch-console") and [Creating a batch segment job
(console)](creating-batch-seg-job.md#batch-segment-console "creating-batch-seg-job.md#batch-segment-console").

## Filtering batch workflows (AWS

SDKs)

To filter batch recommendations with the AWS SDKs, create a filter and include the `FilterArn` parameter in the [CreateBatchInferenceJob](API_CreateBatchInferenceJob.md "API_CreateBatchInferenceJob.md") or
[CreateBatchSegmentJob](API_CreateBatchSegmentJob.md "API_CreateBatchSegmentJob.md")
request.

The following code shows how to create a batch inference job with a filter using the AWS SDK for Python (Boto3). We recommend
using a different location for your output data (either a folder or a different Amazon S3 bucket). For complete explanation of all fields, see
see [Creating a batch inference job (AWS SDKs)](creating-batch-inference-job.md#batch-sdk "creating-batch-inference-job.md#batch-sdk").

```
import boto3

personalize = boto3.client("personalize")

personalize_rec.create_batch_inference_job (
    solutionVersionArn = "`Solution version ARN`",
    jobName = "`Batch job name`",
    roleArn = "`IAM role ARN`",
    filterArn = "`Filter ARN`",
    jobInput =
        {"s3DataSource": {"path": "`S3 input path`"}},
    jobOutput =
        {"S3DataDestination": {"path": "`S3 output path`"}}
)

```
