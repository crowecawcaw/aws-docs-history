# Replacing a dataset's schema to add new columns

After you create an Items or Users dataset, you can replace its schema with a new or existing one. You might replace a dataset's
schema if your data structure changed after you created the dataset. For example, you might have a new column of item metadata
that you want Amazon Personalize to consider during training. Or you might want to add a column of data to use only when filtering
recommendations.

When you replace a dataset's schema, you must keep all fields in the previous schema and you can’t change their data
types or attributes. After you replace a dataset's schema, Amazon Personalize automatically excludes any new columns from training for any
existing recommenders or custom solutions. For more guidelines and requirements, see [Guidelines and requirements](#replace-schema-guidelines "#replace-schema-guidelines").

You can replace a dataset's schema with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), and AWS SDKs.

###### Topics

- [Guidelines and requirements](#replace-schema-guidelines "#replace-schema-guidelines")
- [Replacing a dataset's schema (console)](#updating-dataset-schema-console "#updating-dataset-schema-console")
- [Replacing a dataset's schema (AWS CLI)](#updating-dataset-schema-cli "#updating-dataset-schema-cli")
- [Replacing a dataset's schema (AWS SDKs)](#updating-dataset-schema-sdk "#updating-dataset-schema-sdk")

## Guidelines and requirements

Before you replace the schema for a dataset, make sure that you're aware of the following guidelines and
requirements:

- You can't replace the schema of an Item interactions dataset, Action interactions dataset or Actions dataset.
- You can add new fields to your replacement schema, but you must keep all fields in the previous schema. And you
  can’t change their data types or attributes. For example, if the previous schema includes a
  `MEMBERSHIP_STATUS` field for categorical string data, the new schema you use must include a
  `MEMBERSHIP_STATUS` field with these attributes and data types.
- If the current schema has a field that you want to rename, or if you want to change its data types or attributes,
  you can add a new field with a new name and modified types or attributes. Then include the new field in training and
  exclude the old field. Any new fields must support `null` data. If the old field did not support null data,
  when you import data, you can use placeholder data to make sure your import matches the schema. For information about
  configuring the columns used by a recommender, see [Updating a recommender](updating-recommender.md "updating-recommender.md"). For information about configuring the columns used by a solution, see [Configuring columns used when training](custom-config-columns.md "custom-config-columns.md").
- Any new fields must support `null` data. For information about adding a null type to a field, see [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes").
- After you replace a dataset's schema, Amazon Personalize automatically excludes any new columns from training for any existing
  recommenders or custom solutions. Using the modified dataset involves the following actions:
  - To use any new columns in training, import data that aligns with the new schema. Then update any recommenders to
    use any new columns, or create a new custom solution and configure the columns that it uses when training.

  For information about updating the columns used by a recommender, see [Updating a recommender](updating-recommender.md "updating-recommender.md"). For information about configuring the columns used by a solution, see
  [Configuring columns used when training](custom-config-columns.md "custom-config-columns.md").
  - To use any columns only when filtering, import data that aligns with the new schema, create a filter that uses the new data, and apply
    your filter to your recommendation requests. You don't need to update any recommenders, or create or update
    any custom resources.

## Replacing a dataset's schema (console)

To replace a dataset's schema with the Amazon Personalize console, you choose the dataset to modify
and choose to replace with a new schema or use an existing one.

###### To replace a dataset's schema

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your dataset group.
3. In the navigation pane, choose **Datasets**, and choose the radio button for the dataset that you want to modify.
4. Choose **Actions**, and choose **Replace schema**.
5. In **Schema details**, choose to replace with a new schema or a previously created one.
6. Specify the new schema to use. If you have chosen to:
   - Replace with a new schema, then give the schema a name, and in **Schema definition**, make your
     changes to the schema JSON.
   - Use a previously created schema, then for **Previously created schema**, choose the schema that you
     want to use. Only eligible schemas are listed. For information about schema requirements, see [Guidelines and requirements](#replace-schema-guidelines "#replace-schema-guidelines").

7. Choose **Replace**. When the dataset is active, you can start importing data that aligns
   with the new schema. For more information, see [Importing training data into Amazon Personalize datasets](import-data.md "import-data.md").

## Replacing a dataset's schema (AWS CLI)

To replace a dataset's schema with the AWS CLI, you use the `update-dataset` command, specify the Amazon
Resource Name (ARN) of the dataset to update and the ARN of the new schema to use. You can't update the schema of an
Item interactions dataset, Action interactions dataset or Actions dataset.

The following code shows how to update a dataset's schema with the AWS CLI. To replace a dataset's schema with a new one,
first use the `create-schema` command. Then use the following code to replace the current schema with the new
one. For information about creating a schema with the AWS CLI, see [Creating a dataset and a schema (AWS CLI)](data-prep-creating-datasets.md#data-prep-creating-ds-cli "data-prep-creating-datasets.md#data-prep-creating-ds-cli"). For information about datasets and schema requirements, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

```
aws personalize update-dataset \
--dataset-arn `Dataset ARN` \
--schema-arn `New schema ARN`

```

When the dataset is active, you can start importing data that aligns with the new schema. For more information, see
[Importing training data into Amazon Personalize datasets](import-data.md "import-data.md"). For information about the latest update to the dataset, you can use
the [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") operation.

## Replacing a dataset's schema (AWS SDKs)

To replace a dataset's schema with the AWS SDKs, you use the `UpdateDataset` API operation.
Specify the Amazon Resource Name (ARN) of the dataset to update and the new schema to use. You can't update the schema of an
Item interactions dataset, Action interactions dataset or Actions dataset.

The following code shows how to replace a dataset's schema with the SDK for Python (Boto3). To replace a dataset's schema with a new
one, first use the [CreateSchema](API_CreateSchema.md "API_CreateSchema.md") operation. Then use the following
code to replace the current schema with the new one. For information about creating a schema with the AWS SDKs, see [Creating a dataset and a schema (AWS SDKs)](data-prep-creating-datasets.md#data-prep-creating-ds-sdk "data-prep-creating-datasets.md#data-prep-creating-ds-sdk"). For information on dataset and schema
requirements, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

```
import boto3

personalize = boto3.client('personalize')

update_dataset_response = personalize.update_dataset(
    datasetArn = '`dataset_arn`',
    schemaArn = '`new_schema_arn`'
)

print(update_dataset_response)
```

When the dataset is active, you can start importing data that aligns with the new schema. For more information, see
[Importing training data into Amazon Personalize datasets](import-data.md "import-data.md"). For information about the latest update to the dataset, you can use
the [DescribeDataset](API_DescribeDataset.md "API_DescribeDataset.md") operation.
