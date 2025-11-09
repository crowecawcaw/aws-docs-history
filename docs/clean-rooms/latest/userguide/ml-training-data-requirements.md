# Training data requirements for

Clean Rooms ML

To successfully create a lookalike model, your training data must meet the
following requirements:

- The training data must be in Parquet, CSV, or JSON format.

###### Note

Zstandard (ZSTD) compressed Parquet data is not supported.

- Your training data must be cataloged in AWS Glue. For more information, see
  [Getting started with the
  AWS Glue Data Catalog](../../../glue/latest/dg/start-data-catalog.md "../../../glue/latest/dg/start-data-catalog.md") in the AWS Glue Developer Guide. We recommend
  using AWS Glue crawlers to create your tables because the schema is inferred
  automatically.
- The Amazon S3 bucket that contains the training data and seed data is in the
  same AWS region as your other Clean Rooms ML resources.
- The training data must contain at least 100,000 unique user IDs with at
  least two item interactions each.
- The training data must contain at least 1 million records.
- The schema specified in the [CreateTrainingDataset](../../../cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.md "../../../cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.md") action must align with the schema defined
  when the AWS Glue table was created.
- The required fields, as defined in the provided table, are defined in the
  [CreateTrainingDataset](../../../cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.md "../../../cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.md") action.

| Field type          | Supported data types                                  | Required | Description                                                                                                                                                                                                                                                                                                          |
| ------------------- | ----------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USER_ID             | string, int, bigint                                   | Yes      | A unique identifier for each user in the dataset. It<br>should be a non-Personally Identifiable Information (PII)<br>value. This might be a hashed identifier or a customer<br>ID.                                                                                                                                   |
| ITEM_ID             | string, int, bigint                                   | Yes      | A unique identifier for each item a user interacts<br>with.                                                                                                                                                                                                                                                          |
| TIMESTAMP           | bigint, int, timestamp                                | Yes      | The time when a user interacted with the item. Values<br>must be in the Unix epoch time in seconds format.                                                                                                                                                                                                           |
| CATEGORICAL_FEATURE | string, int, float, bigint, double, boolean,<br>array | No       | Captures categorical data related to the user or the<br>item. This can include things like an event type (such as<br>click or purchase), user demographics (age group, gender -<br>anonymized), user location (city, country<br>• anonymized),<br>item category (such as clothing or electronics), or item<br>brand. |
| NUMERICAL_FEATURE   | double, float, int, bigint                            | No       | Captures numerical data related to the user or the item.<br>This can include things like user purchase history (total<br>amount spent), item price, number of times an item is<br>visited, or user ratings for items.                                                                                                |

- Optionally, you can provide up to 10 total categorical or numerical
  features.
  Here is an example of a valid training data set in CSV format

```
`USER_ID,ITEM_ID,TIMESTAMP,EVENT_TYPE(CATEGORICAL FEATURE),EVENT_VALUE (NUMERICAL FEATURE)
196,242,881250949,click,15
186,302,891717742,click,13
22,377,878887116,click,10
244,51,880606923,click,20
166,346,886397596,click,10`

```
