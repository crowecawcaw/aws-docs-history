# Deleting a dataset to delete all of its data

To delete all of the data in a dataset, you delete the dataset. You can delete a dataset with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.
Before you delete a dataset, note the following:

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

###### Topics

- [Deleting a dataset
  (console)](#delete-dataset-console "#delete-dataset-console")
- [Deleting a dataset
  (AWS CLI)](#delete-dataset-cli "#delete-dataset-cli")
- [Deleting a dataset (AWS
  SDKs)](#delete-dataset-sdk "#delete-dataset-sdk")

## Deleting a dataset

(console)

To delete a dataset with the Amazon Personalize console, navigate to the dataset details page and choose delete.

###### To delete a dataset

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home").
2. In the navigation pane, choose **Dataset
   groups**.
3. On the **Dataset groups** page, choose your
   dataset group.
4. In the navigation pane, choose
   **Datasets**.
5. Choose the dataset to open its details page.
6. On the dataset's details page, choose **Delete** and confirm dataset deletion.

## Deleting a dataset

(AWS CLI)

The following code shows how to delete a dataset with the AWS CLI and the [DeleteDataset](API_DeleteDataset.md "API_DeleteDataset.md") operation.

```
aws personalize delete-dataset --dataset-arn `dataset-arn`
```

## Deleting a dataset (AWS

SDKs)

The following code shows how to delete a dataset with the AWS SDKs and the [DeleteDataset](API_DeleteDataset.md "API_DeleteDataset.md") operation.

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

response = personalize.delete_dataset(
    datasetArn = '`dataset ARN`'
)
```

SDK for Java 2.x

```
public static void deleteDataset(PersonalizeClient personalizeClient,
                                 String datasetArn) {

    try {
        DeleteDatasetRequest deleteRequest = DeleteDatasetRequest.builder()
                .datasetArn(datasetArn)
                .build();

        int responseCode = personalizeClient.deleteDataset(deleteRequest).sdkHttpResponse().statusCode();
        System.out.println(responseCode);
    } catch (PersonalizeException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
}
```
