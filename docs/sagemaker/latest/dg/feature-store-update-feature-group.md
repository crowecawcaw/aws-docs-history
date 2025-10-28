# Add features and records to a feature

group

You can use the Amazon SageMaker Feature Store API or the console to update and describe your
feature group as well as add features and records to your feature group. A feature group is
an object that contains your data and a feature describes a column in the table. When you
add a feature to the feature group you are effectively adding a column to the table. When
you add a new record to the feature group you are filling in values for features associated
with a specific record identifier. For more information on Feature Store concepts, see [Feature Store concepts](feature-store-concepts.md "feature-store-concepts.md").

After you successfully add features to a feature group, you cannot remove those features.
The features that you have added do not add any data to your records. You can add new
records to the feature group or overwrite them using the [PutRecord](../APIReference/API_feature_store_PutRecord.md "../APIReference/API_feature_store_PutRecord.md")
API. For examples on updating, describing, and putting records into a feature group, see
[Example code](#feature-store-update-feature-group-example "#feature-store-update-feature-group-example").

You can use the console to add features to a feature group. For more
information on how to update your feature groups using the console, see
[Update a feature group from the
console](feature-store-use-with-studio.md#feature-store-update-feature-group-studio "feature-store-use-with-studio.md#feature-store-update-feature-group-studio").

The following sections provide an overview of using Feature Store APIs to add features to a feature
group followed by examples. With the API, you can also add or overwrite records after you've
updated the feature group.

###### Topics

- [API](#feature-store-update-feature-group-api "#feature-store-update-feature-group-api")
- [Example code](#feature-store-update-feature-group-example "#feature-store-update-feature-group-example")

## API

Use the [`UpdateFeatureGroup`](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md") operation to add features to a feature
group.

You can use the [`DescribeFeatureGroup`](../APIReference/API_DescribeFeatureGroup.md "../APIReference/API_DescribeFeatureGroup.md") operation to see if you've added the
features successfully.

To add or overwrite records, use the [`PutRecord`](../APIReference/API_feature_store_PutRecord.md "../APIReference/API_feature_store_PutRecord.md") operation.

To see the updates that you've made to a record, use the [`GetRecord`](../APIReference/API_feature_store_GetRecord.md "../APIReference/API_feature_store_GetRecord.md") operation. To see the updates that you've made
to multiple records, use the [`BatchGetRecord`](../APIReference/API_feature_store_BatchGetRecord.md "../APIReference/API_feature_store_BatchGetRecord.md") operation. It can take up to five minutes
for the updates that you've made to appear.

You can use the example code in the following section to walk through adding features and
records using the AWS SDK for Python (Boto3).

## Example code

The example code walks you through the following process:

1. Adding features to the feature group
2. Verifying that you've added them successfully
3. Adding a record to the feature group
4. Verifying that you've added it successfully

### Step 1: Add features to

a feature group

The following code uses the [`UpdateFeatureGroup`](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md") operation to add new features to
the feature group. It assumes that you've set up Feature Store and created a feature group.
For more information about getting started, see [Introduction to Feature Store example
notebook](feature-store-introduction-notebook.md "feature-store-introduction-notebook.md").

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

The following code uses the [`DescribeFeatureGroup`](../APIReference/API_DescribeFeatureGroup.md "../APIReference/API_DescribeFeatureGroup.md") operation to check the status of
the update. If the [`LastUpdateStatus`](../APIReference/API_DescribeFeatureGroup.md#sagemaker-DescribeFeatureGroup-response-LastUpdateStatus "../APIReference/API_DescribeFeatureGroup.md#sagemaker-DescribeFeatureGroup-response-LastUpdateStatus") field is `Successful`,
you've added the features successfully.

```

sagemaker_client.describe_feature_group(
    FeatureGroupName=feature_group_name
)

```

### Step 2: Add a new record

to the feature group

The following code uses the [`PutRecord`](../APIReference/API_feature_store_PutRecord.md "../APIReference/API_feature_store_PutRecord.md") operation to add records to the feature
group that you've created.

```

record_identifier_value = `'new_record'`

sagemaker_featurestore_runtime_client = boto3.client("sagemaker-featurestore-runtime")

sagemaker_runtime_client.put_record(
    FeatureGroupName=feature_group_name,
    Record=[
        {
            'FeatureName': `"record-identifier-feature-name"`,
            'ValueAsString': record_identifier_value
        },
        {
            'FeatureName': `"event-time-feature"`,
            'ValueAsString': `"timestamp-that-feature-store-returns"`
        },
        {
            'FeatureName': `"new-feature-1"`,
            'ValueAsString': `"value-as-string"`
        },
        {
            'FeatureName': `"new-feature-2"`,
            'ValueAsString': `"value-as-string"`
        },
        {
            'FeatureName': `"new-feature-3"`,
            'ValueAsString': `"value-as-string"`
        },
    ]
)

```

Use the [`GetRecord`](../APIReference/API_feature_store_GetRecord.md "../APIReference/API_feature_store_GetRecord.md") operation to see which records in your
feature group don't have data for the features that you've added. You can use the
[`PutRecord`](../APIReference/API_feature_store_PutRecord.md "../APIReference/API_feature_store_PutRecord.md") operation to overwrite the records that
don't have data for the features that you've added.
