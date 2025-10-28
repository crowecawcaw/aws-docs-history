# Getting batch user segments with custom resources

To get _user segments_, you use a batch segment job. A _batch segment
job_ is a tool that imports your batch input data from an Amazon S3 bucket and uses your solution version trained with
a USER_SEGMENTATION recipe to generate _user segments_ for each row of input data.

Depending on the
recipe, the input data is a list of items or item metadata attributes in JSON format. For item attributes, your input data can
include expressions to create user segments based on multiple metadata attributes. A batch segment job exports user segments to
an output Amazon S3 bucket. Each user segment is sorted in descending order based on the probability that each user will interact
with the item in your input data.

When generating user segments, Amazon Personalize considers data in datasets from bulk and individual imports:

- For bulk data, Amazon Personalize generates segments using only the bulk data present at the last full solution version training. And
  it uses only bulk data that you imported with an import mode of FULL (replacing existing data).
- For data from individual data import operations, Amazon Personalize generates user segments using the data present at the last full solution version
  training. To have newer records impact user segments, create a new solution version and then create a batch segment job.
  Generating user segments works as follows:

1. Prepare and upload your input data in JSON format to an Amazon S3 bucket.
   The format of your input data depends on the recipe you use and the job you are creating.
   See [Preparing input data for user segments](prepare-input-data-user-segment.md "prepare-input-data-user-segment.md").
2. Create a separate location for your output data, either a different folder or a different Amazon S3 bucket.
3. Create a batch segment job. See [Getting user segments with a batch segment job](creating-batch-seg-job.md "creating-batch-seg-job.md").
4. When the batch segment job is complete, retrieve the user segments from your output location in Amazon S3.

###### Topics

- [Guidelines and requirements for getting user segments](#batch-seg-permissions-req "#batch-seg-permissions-req")
- [Preparing input data for user segments](prepare-input-data-user-segment.md "prepare-input-data-user-segment.md")
- [Getting user segments with a batch segment job](creating-batch-seg-job.md "creating-batch-seg-job.md")
- [Batch segment job output format examples](batch-segment-job-output-examples.md "batch-segment-job-output-examples.md")

## Guidelines and requirements for getting user segments

The following are guidelines and requirements for batch getting batch segments:

- You must use a USER_SEGMENTATION recipe.
- Your Amazon Personalize IAM service role needs permission to read and add files to your Amazon S3 buckets. For information on
  granting permissions, see [Service role policy for batch workflows](granting-personalize-s3-access.md#role-policy-for-batch-workflows "granting-personalize-s3-access.md#role-policy-for-batch-workflows").
  For more information on bucket permissions, see [User policy
  examples](../../../AmazonS3/latest/userguide/example-policies-s3.md "../../../AmazonS3/latest/userguide/example-policies-s3.md") in the _Amazon Simple Storage Service Developer Guide_.

If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").

- You must create a custom solution and
  solution version before you create a batch inference job. However, you don't need to create an Amazon Personalize campaign. If you created a Domain dataset group, you can still
  create custom resources.
- Your input data must be formatted as described in [Preparing input data for user segments](prepare-input-data-user-segment.md "prepare-input-data-user-segment.md").
- If you use the Item-Attribute-Affinity recipe, the attributes in your input data can't include unstructured textual item metadata, such as a product description.
- If you use a filter with placeholder parameters, you must include the values for the parameters
  in your input data in a `filterValues` object. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values").
- We recommend that you use a different location for your output data (either a folder or a different Amazon S3 bucket)
  than your input data.
