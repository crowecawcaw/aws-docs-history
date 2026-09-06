

# Add features and records to a feature group
<a name="feature-store-update-feature-group"></a>

You can use the Amazon SageMaker Feature Store API or the console to update and describe your feature group as well as add features and records to your feature group. A feature group is an object that contains your data and a feature describes a column in the table. When you add a feature to the feature group you are effectively adding a column to the table. When you add a new record to the feature group you are filling in values for features associated with a specific record identifier. For more information on Feature Store concepts, see [Feature Store concepts](feature-store-concepts.md). 

After you successfully add features to a feature group, you cannot remove those features. The features that you have added do not add any data to your records. You can add new records to the feature group or overwrite them using the [PutRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html) or [BatchWriteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchWriteRecord.html) API operations. For examples on updating, describing, and putting records into a feature group, see [Example code](#feature-store-update-feature-group-example).

You can use the console to add features to a feature group. For more information on how to update your feature groups using the console, see [Update a feature group from the console](feature-store-use-with-studio.md#feature-store-update-feature-group-studio).

The following sections provide an overview of using Feature Store APIs to add features to a feature group followed by examples. With the API, you can also add or overwrite records after you have updated the feature group. 

**Topics**
+ [API](#feature-store-update-feature-group-api)
+ [Example code](#feature-store-update-feature-group-example)

## API
<a name="feature-store-update-feature-group-api"></a>

Use the [`UpdateFeatureGroup`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureGroup.html) operation to add features to a feature group.

You can use the [`DescribeFeatureGroup`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html) operation to see if you have added the features successfully.

To add or overwrite records, use the [PutRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html) operation. To write up to 25 records in a single request, use the `BatchWriteRecord` operation.

To see the updates that you have made to a record, use the [GetRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html) operation. To see the updates that you have made to multiple records, use the [BatchGetRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchGetRecord.html) operation. It can take up to five minutes for the updates to appear.

You can use the example code in the following section to walk through adding features and records using the AWS SDK for Python (Boto3).

## Example code
<a name="feature-store-update-feature-group-example"></a>

The example code walks you through the following process: 

1. Adding features to the feature group

1. Verifying that you have added them successfully

1. Adding a record to the feature group

1. Adding multiple records in bulk to the feature group

1. Verifying that you have added them successfully

### Step 1: Add features to a feature group
<a name="feature-store-update-feature-group-step-1"></a>

The following code uses the [`UpdateFeatureGroup`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureGroup.html) operation to add new features to the feature group. It assumes that you have set up Feature Store and created a feature group. For more information about getting started, see [Introduction to Feature Store example notebook](feature-store-introduction-notebook.md).

```
import boto3

sagemaker_client = boto3.client("sagemaker")

sagemaker_client.update_feature_group(
    FeatureGroupName=feature_group_name,
    FeatureAdditions=[
        {"FeatureName": "new-feature-1", "FeatureType": "Integral"},
        {"FeatureName": "new-feature-2", "FeatureType": "Fractional"},
        {"FeatureName": "new-feature-3", "FeatureType": "String"}
    ]
)
```

The following code uses the [`DescribeFeatureGroup`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html) operation to check the status of the update. If the [`LastUpdateStatus`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html#sagemaker-DescribeFeatureGroup-response-LastUpdateStatus) field is `Successful`, you have added the features successfully.

```
sagemaker_client.describe_feature_group(
    FeatureGroupName=feature_group_name
)
```

### Step 2: Add a new record to the feature group
<a name="feature-store-update-feature-group-step-2"></a>

The following code uses the [`PutRecord`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html) operation to add records to the feature group that you have created.

```
record_identifier_value = {{'new_record'}}

sagemaker_featurestore_runtime_client = boto3.client("sagemaker-featurestore-runtime")

sagemaker_runtime_client.put_record(
    FeatureGroupName=feature_group_name,
    Record=[
        {
            'FeatureName': {{"record-identifier-feature-name"}},
            'ValueAsString': record_identifier_value
        },
        {
            'FeatureName': {{"event-time-feature"}},
            'ValueAsString': {{"timestamp-that-feature-store-returns"}}
        },
        {
            'FeatureName': {{"new-feature-1"}}, 
            'ValueAsString': {{"value-as-string"}}
        },
        {
            'FeatureName': {{"new-feature-2"}}, 
            'ValueAsString': {{"value-as-string"}}
        },
        {
            'FeatureName': {{"new-feature-3"}}, 
            'ValueAsString': {{"value-as-string"}}
        },
    ]
)
```

Use the [`GetRecord`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html) operation to see which records in your feature group do not have data for the features that you have added. You can use the [`PutRecord`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html) operation to overwrite the records that do not have data for the features that you have added.

### Step 3: Add multiple records in bulk using BatchWriteRecord
<a name="feature-store-update-feature-group-step-3"></a>

To add or overwrite multiple records, use the [BatchWriteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchWriteRecord.html) operation. To automatically expire records, specify a `TtlDuration`:

```
response = sagemaker_featurestore_runtime_client.batch_write_record(
    Entries=[
        {
            'FeatureGroupName': feature_group_name,
            'Record': [
                {'FeatureName': {{"record-identifier-feature-name"}}, 'ValueAsString': {{'record_1'}}},
                {'FeatureName': {{"event-time-feature"}}, 'ValueAsString': {{"2024-01-01T00:00:00Z"}}},
                {'FeatureName': {{"new-feature-1"}}, 'ValueAsString': {{"value-1"}}},
            ],
            'TtlDuration': {'Unit': 'Hours', 'Value': 24}
        },
        {
            'FeatureGroupName': feature_group_name,
            'Record': [
                {'FeatureName': {{"record-identifier-feature-name"}}, 'ValueAsString': {{'record_2'}}},
                {'FeatureName': {{"event-time-feature"}}, 'ValueAsString': {{"2024-01-01T00:00:00Z"}}},
                {'FeatureName': {{"new-feature-1"}}, 'ValueAsString': {{"value-2"}}},
            ]
        }
    ]
)

# Check for failed records.
if response['Errors']:
    for error in response['Errors']:
        print(f"Error: {error['ErrorCode']} - {error['ErrorMessage']}")

# Retry unprocessed entries.
unprocessed = response.get('UnprocessedEntries', [])
while unprocessed:
    response = sagemaker_featurestore_runtime_client.batch_write_record(Entries=unprocessed)
    unprocessed = response.get('UnprocessedEntries', [])
```

The response includes an `Errors` list for records that failed and an `UnprocessedEntries` list for records that can be retried.

**Note**  
The `TtlDuration` is calculated relative to the record's `EventTime`. If the `EventTime` plus the `TtlDuration` is in the past, Amazon SageMaker Feature Store does not store the record in the online store.