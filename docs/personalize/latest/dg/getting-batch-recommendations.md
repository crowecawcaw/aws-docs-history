# Getting batch item recommendations with custom resources

With custom resources, you can get item recommendations with an asynchronous batch flow. For example, you might get
product recommendations for all users on an email list or [item-to-item
similarities](native-recipe-similar-items.md "native-recipe-similar-items.md") across an inventory.

To get batch recommendations for items, you use a batch inference job. A _batch inference job_ is a tool that imports your batch input data
from an Amazon S3 bucket, uses your custom solution version to generate _item recommendations_, and
then exports the item recommendations to an Amazon S3 bucket.
Depending on the recipe, your input data is a list of users, or items, or a list of users each with a collection of items.

If your solution uses the Similar Items recipe and you have an Items dataset with textual data and item title data,
you can generate batch recommendations with themes for each group of items. For more information, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md").

After you create a custom solution version, how new data
influences batch item recommendations depends on its type, the method of import, and the custom recipe you use.
For information about how new data influences batch recommendations, see
[How new data influences batch recommendations (custom resources)](how-new-data-influences-batch-recommendations.md "how-new-data-influences-batch-recommendations.md").

###### Topics

- [Batch workflow](#batch-worfklow-steps "#batch-worfklow-steps")
- [Guidelines and requirements](#batch-permissions-req "#batch-permissions-req")
- [Batch workflow scoring](#batch-scoring "#batch-scoring")
- [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md")
- [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md")
- [Creating a batch inference
  job](creating-batch-inference-job.md "creating-batch-inference-job.md")
- [Batch inference job output examples](batch-inference-job-output-examples.md "batch-inference-job-output-examples.md")

## Batch workflow

The batch workflow is as follows:

1. Prepare and upload your input data in JSON format to an Amazon S3 bucket.
   The format of your input data depends on the recipe you use. See [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md").
2. Create a separate location for your output data, either a folder or a different Amazon S3 bucket.
3. Create a batch inference job. See [Creating a batch inference
   job](creating-batch-inference-job.md "creating-batch-inference-job.md").
4. When the batch inference is complete, retrieve the item recommendations from your output location in Amazon S3.

## Guidelines and requirements

The following are guidelines and requirements for getting batch recommendations:

- Your Amazon Personalize IAM service role must have permission to read and add files to your Amazon S3 buckets. For information on
  granting permissions, see [Service role policy for batch workflows](granting-personalize-s3-access.md#role-policy-for-batch-workflows "granting-personalize-s3-access.md#role-policy-for-batch-workflows").
  For more information on bucket permissions, see [User policy
  examples](../../../AmazonS3/latest/userguide/example-policies-s3.md "../../../AmazonS3/latest/userguide/example-policies-s3.md") in the _Amazon Simple Storage Service Developer Guide_.
  If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
  permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").
- You must create a custom solution and
  solution version before you create a batch inference job. However, you don't need to create an Amazon Personalize campaign. If you created a Domain dataset group, you can still
  create custom resources.
- To generate themes with recommendations, you must use the Similar-Items recipe. And you must have an Items dataset with
  textual data and item title data. For more information about themed recommendations, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md").
- Your input data must be formatted as described in [Preparing input data for user segments](prepare-input-data-user-segment.md "prepare-input-data-user-segment.md").
- You can't get batch recommendations with the Trending-Now or Next-Best-Action recipes.
- If you use a filter with placeholder parameters, you must include the values for the parameters
  in your input data in a `filterValues` object. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values").
- We recommend that you use a different location for your output data (either a folder or a different Amazon S3 bucket) than your input data.
- Batch recommendations might not
  be exactly the same as real-time recommendations. This is because batch inference jobs take longer to complete and only consider data available 15 minutes before the start of the job.

## Batch workflow scoring

Batch recommendations include scores as follows:

- With User-Personalization and Personalized-Ranking recipes, Amazon Personalize calculates batch inference job recommendation
  scores as described in [How recommendation scoring works (custom resources)](recommendations.md#how-recommendation-scoring-works "recommendations.md#how-recommendation-scoring-works") and [How personalized ranking scoring works](rankings.md#how-ranking-scoring-works "rankings.md#how-ranking-scoring-works"). You can view scores in the
  batch inference job's output JSON file.
- With the Similar-Items recipe, if you get themed batch recommendations, Amazon Personalize ranks each set of related items
  based on how relevant the theme is for each item. Each item includes a score from 0 to 1. The higher the score, the more
  closely related the item is to the theme. For more information about recommendations with themes, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md").
