# Configuring datasets

To add labeled training or test data to a flywheel, use the Amazon Comprehend console or API to create a dataset.

You configure each dataset as training data or test data. You associate the dataset with a specific flywheel and
custom model. When you create a dataset, Amazon Comprehend uploads the data to the flywheel's data lake. For details about file
formats for the training data, see [Preparing classifier training data](prep-classifier-data.md "prep-classifier-data.md") or
[Preparing entity recognizer training data](prep-training-data-cer.md "prep-training-data-cer.md").

When you delete the flywheel, Amazon Comprehend deletes the datasets. The uploaded data remains available in the data
lake.

## Creating a dataset (console)

###### Create a dataset

1. Sign in to the AWS Management Console and open the [Amazon Comprehend console](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/").
2. From the left menu, choose **Flywheels** and choose the flywheel where you want to add
   the data.
3. Choose the **Datasets** tab.
4. In the **Training datasets** or **Test datasets** table, choose
   **Create dataset**.
5. Under **Dataset details**, enter a name for the dataset and an optional description.
6. Under **Data specifications**, choose the **Data format** and the
   **Dataset type** configuration fields.
7. (Optional) Under **Input format**, choose the format of the input documents.
8. Under **Annotation location on S3**, enter the Amazon S3 location of the annotations file.
9. Under **Training data location on S3**, enter the Amazon S3 location of the document files.
10. Choose **Create**.

## Creating a dataset (API)

You can use the [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") operation to create a dataset.

```
aws comprehend create-dataset \
    --flywheel-arn "myFlywheel2" \
    --dataset-name "my-training-dataset"
    --dataset-type "TRAIN"
    --description "my training dataset"
    --cli-input-json file://inputConfig.json
}
```

The `inputConfig.json` file contains the following content.

```
{
    "DataFormat": "COMPREHEND_CSV",
    "DocumentClassifierInputDataConfig": {
        "S3Uri": "s3://my-comprehend-datasets/multilabel_train.csv"
    }
}
```

To add or remove tags on the dataset, use the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") and [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operations.

## Describe a dataset

Use the Amazon Comprehend [DescribeDataset](../APIReference/API_DescribeDataset.md "../APIReference/API_DescribeDataset.md") operation to retrieve configured information about a flywheel.

```
aws comprehend describe-dataset \
    --dataset-arn  "datasetARN"
```

The response contains the following content.

```
{
   "DatasetProperties": {
      "DatasetArn": "arn:aws::comprehend:`aws-region`:111122223333:flywheel/myTestFlywheel/dataset/train-dataset",
      "DatasetName": "train-dataset",
      "DatasetType": "TRAIN",
      "DatasetS3Uri": "s3://my-test-datalake/flywheelbasictest/myTestFlywheel/schemaVersion=1/20220801T014326Z/datasets/train-dataset/20220801T194844Z",
      "Description": "Good Dataset",
      "Status": "COMPLETED",
      "NumberOfDocuments": 90,
      "CreationTime": 1659383324.297
  }
}
```
