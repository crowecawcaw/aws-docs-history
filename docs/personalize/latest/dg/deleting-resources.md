# Requirements for deleting Amazon Personalize resources

Deleting resources can help you avoid unnecessary costs. For example, you incur campaign costs while a campaign is active.
To avoid unnecessary costs, make sure to delete the campaign when you are finished. For a complete list of charges and prices,
see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

To delete resources with the Amazon Personalize
console, you choose **Delete** on the details page for the resource. To delete a resource with Amazon Personalize APIs, you use
the `Delete` APIs with the SDKs or the AWS Command Line Interface (AWS CLI).

For detailed steps for deleting a dataset with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs, see
[Deleting a dataset to delete all of its data](delete-dataset.md "delete-dataset.md"). You can apply the patterns in these steps to other Amazon Personalize resources.
For information about deleting users and their data from your dataset group, see [Deleting users and their data with a data deletion job](delete-records.md "delete-records.md").

You must delete some resources before you can delete others. For example, if you create an event tracker and an Item interactions dataset,
you must delete the event tracker before you can delete the dataset. The following sections provide guidelines and order requirements
for deleting Amazon Personalize resources.

###### Topics

- [Guidelines for deleting resources](#cleaning-up-guidelines "#cleaning-up-guidelines")
- [Recommended order for resource deletion](#deleting-resources-order "#deleting-resources-order")
- [Deleting users and their data with a data deletion job](delete-records.md "delete-records.md")
- [Deleting a dataset to delete all of its data](delete-dataset.md "delete-dataset.md")

## Guidelines for deleting resources

The following are guidelines for deleting resources:

- Deleting a resource in Amazon Personalize is an irreversible action. Deletion can't be stopped after it begins.
- You can't delete a resource whose status is changing from one state to another. For example, you can't delete a resource that is
  CREATE PENDING or IN PROGRESS. The resource status must be ACTIVE or
  CREATE FAILED. This includes the `latestSolutionUpdate` status for a solution.
  You can check the status of a resource using the `Describe` APIs. For example, the [DescribeCampaign](API_DescribeCampaign.md "API_DescribeCampaign.md") API operation.
- For information about deleting training data in Amazon S3, see [How do I
  delete objects from an S3 bucket?](../../../AmazonS3/latest/userguide/delete-objects.md "../../../AmazonS3/latest/userguide/delete-objects.md").
- You aren't charged for dataset import jobs after they complete and you can't delete them.
- You aren't charged for schemas and you can't delete a schema with the Amazon Personalize console. To delete a schema, use the
  [DeleteSchema](API_DeleteSchema.md "API_DeleteSchema.md") API operation.

The following are requirements specific to deleting datasets:

- You must delete all filters before deleting any dataset.
- If you created an event tracker, you must delete it before you delete an Item interactions dataset.
- If you created a metric attribution that references the dataset, you must delete the metric attribution
  first.
- If you use User-Personalization-v2, User-Personalization, or Next-Best-Action recipes or _Top picks for you_ and _Recommended for you_ use cases, deleting a dataset
  halts automatic updates for any associated solution versions or recommenders.
- No associated `DatasetImportJob` can have a status of CREATE PENDING or IN PROGRESS.
- No associated `BatchInferenceJob` or `BatchSegmentJob` can have a status of CREATE PENDING or IN PROGRESS.
- No associated `Recommender`, `SolutionVersion` can have a status of CREATE PENDING or IN
  PROGRESS.
- No associated `Campaign` can have a status of CREATE PENDING or IN
  PROGRESS or ACTIVE.

## Recommended order for resource deletion

To avoid deletion errors, we recommend that you delete resources from a dataset group in the following order. To identify resources in a dataset group, you can
use the List API operations. For example, you can use the [ListFilters](API_ListFilters.md "API_ListFilters.md") API operation to identify all filters in a dataset group.

1. Any campaigns or recommenders – To delete your campaign or recommender with the APIs, use the [DeleteCampaign](API_DeleteCampaign.md "API_DeleteCampaign.md")
   or [DeleteRecommender](API_DeleteRecommender.md "API_DeleteRecommender.md") API operations.
   With recommenders, you can stop a recommender and start it later. This way, you can pause recommender billing and only pay for it when you use it. For more information,
   see [Stopping a recommender](stopping-starting-recommender.md "stopping-starting-recommender.md").
2. Any solutions – To delete your solution with the APIs, use the [DeleteSolution](API_DeleteSolution.md "API_DeleteSolution.md") API operation. To delete a solution, a solution update can't be in progress. Its `latestSolutionUpdate` status
   must be ACTIVE or CREATE FAILED. Deleting a solution deletes all associated solution versions. None of its solution
   versions can have a status of CREATE PENDING or IN PROGRESS.
3. Event tracker – To delete an event tracker with the APIs, use the [DeleteEventTracker](API_DeleteEventTracker.md "API_DeleteEventTracker.md") API operation. You must delete your event tracker before you can delete
   an Item interactions dataset.
4. Metric attribution – To delete a metric attribution with the APIs, use the [DeleteMetricAttribution](API_DeleteMetricAttribution.md "API_DeleteMetricAttribution.md") API operation.
5. All filters – To delete a filter with the APIs, use the [DeleteFilter](API_DeleteFilter.md "API_DeleteFilter.md") API operation. You must delete all filters before deleting a dataset.
6. Any datasets –
   To delete a dataset with the APIs, use the [DeleteDataset](API_DeleteDataset.md "API_DeleteDataset.md") API operation.
7. Dataset group – To delete your dataset group with the APIs, use the [DeleteDatasetGroup](API_DeleteDatasetGroup.md "API_DeleteDatasetGroup.md") API operation.
8. Schemas – To delete a schema, use the [DeleteSchema](API_DeleteSchema.md "API_DeleteSchema.md") API operation.
