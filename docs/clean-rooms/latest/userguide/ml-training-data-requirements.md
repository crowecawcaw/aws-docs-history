

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-training-data-requirements.html)
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