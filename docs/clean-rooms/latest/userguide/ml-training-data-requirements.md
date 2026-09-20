

# Training data requirements for Clean Rooms ML
<a name="ml-training-data-requirements"></a>

To successfully create a lookalike model, your training data must meet the following requirements:
+ The training data must be in Parquet, CSV, or JSON format.
**Note**  
Zstandard (ZSTD) compressed Parquet data is not supported.
+ Your training data must be cataloged in AWS Glue. For more information, see [Getting started with the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html) in the AWS Glue Developer Guide. We recommend using AWS Glue crawlers to create your tables because the schema is inferred automatically.
+ The Amazon S3 bucket that contains the training data and seed data is in the same AWS region as your other Clean Rooms ML resources.
+ The training data must contain at least 100,000 unique user IDs with at least two item interactions each.
+ The training data must contain at least 1 million records.
+ The schema specified in the [CreateTrainingDataset](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.html) action must align with the schema defined when the AWS Glue table was created.
+ The required fields, as defined in the provided table, are defined in the [CreateTrainingDataset](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.html) action.


<table>
<thead>
  <tr><th>Field type</th><th>Supported data types</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>USER_ID</td><td>string, int, bigint </td><td>Yes</td><td>A unique identifier for each user in the dataset. It should be a non-Personally Identifiable Information (PII) value. This might be a hashed identifier or a customer ID.</td></tr>
  <tr><td>ITEM_ID</td><td>string, int, bigint</td><td>Yes</td><td>A unique identifier for each item a user interacts with.</td></tr>
  <tr><td>TIMESTAMP</td><td>bigint, int, timestamp</td><td>Yes</td><td>The time when a user interacted with the item. Values must be in the Unix epoch time in seconds format.</td></tr>
  <tr><td>CATEGORICAL_FEATURE</td><td>string, int, float, bigint, double, boolean, array</td><td>No</td><td>Captures categorical data related to the user or the item. This can include things like an event type (such as click or purchase), user demographics (age group, gender - anonymized), user location (city, country - anonymized), item category (such as clothing or electronics), or item brand.</td></tr>
  <tr><td>NUMERICAL_FEATURE</td><td>double, float, int, bigint</td><td>No</td><td>Captures numerical data related to the user or the item. This can include things like user purchase history (total amount spent), item price, number of times an item is visited, or user ratings for items.</td></tr>
</tbody>
</table>

+ Optionally, you can provide up to 10 total categorical or numerical features.

Here is an example of a valid training data set in CSV format

```
USER_ID,ITEM_ID,TIMESTAMP,EVENT_TYPE(CATEGORICAL FEATURE),EVENT_VALUE (NUMERICAL FEATURE)
196,242,881250949,click,15
186,302,891717742,click,13
22,377,878887116,click,10
244,51,880606923,click,20
166,346,886397596,click,10
```