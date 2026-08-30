# Player Churn Prediction and Retention

Publication date: **January 8, 2021 ([Diagram history](#churn-history "#churn-history"))**

This architecture uses [Amazon SageMaker AI](../../../sagemaker/latest/dg.md "../../../sagemaker/latest/dg.md") to build, train, and deploy a churn prediction
model. You can use the model for batch or real-time inference to predict which players are likely
to leave and trigger targeted retention actions.

## Player Churn Prediction and Retention diagram

![Reference architecture diagram showing how to use SageMaker AI to predict player churn and trigger retention actions in free-to-play games.](images/player-churn-prediction-retention.png)

The following steps describe the architecture:

1. The mobile client sends player events through a game analytics pipeline to an [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") bucket.
2. [AWS Glue](../../../glue/latest/dg.md "../../../glue/latest/dg.md") transforms player
   data and marks players as **ACTIVE**, **INACTIVE**, or
   **CHURN** for data scientists.
3. Data scientists prepare player data, test algorithms, and build a model with a subset
   of the dataset in an SageMaker AI notebook.
4. Data scientists launch model training on 80% of the dataset and store the trained
   model in Amazon S3. The remaining 20% is used to test model accuracy.
5. The mobile client asks which in-game player retention action should be triggered, such
   as a promotional offer or bonus items.

The architecture supports two inference paths:

6. **Real-time inference:** An [AWS Lambda](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md") function checks the player profile and
   evaluates churn probability from the SageMaker AI endpoint to choose the most appropriate
   retention action.
7. **Batch inference:** A periodic AWS Glue job triggers a
   batch transformation job on the entire dataset and copies the results to a player profile
   table in [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide.md "../../../amazondynamodb/latest/developerguide.md"). The Lambda function checks
   the player profile churn prediction and chooses the retention action.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | January 8, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are
using.
