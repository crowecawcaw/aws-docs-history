# Real-Time Casino Player Analytics

Publication date: **April 19, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables casino customers or game developers to build a real-time analytics pipeline and promote advertising offers to customers during the game session.

## Real-Time Casino Player Analytics Diagram

![Reference architecture diagram showing enables casino customers or game developers to build a real-time analytics pipeline and promote advertising offers to customers during the game session.](images/real-time-player-casino-analytics.png)

1. Casino slot machine and shuffler data is streamed from the casino floor via a private
   network into **Amazon API Gateway** and **AWS IoT Core**, respectively.
2. Data is then streamed into **Amazon Kinesis Data Streams**.
3. Slot data from **Kinesis Data Streams** is processed by **AWS Lambda** to calculate customer rating and store a raw copy in
   **Amazon S3** for machine learning (ML) training.
4. Raw data from slots and shufflers is transformed to identify unique records, and
   stored in a refined data **Amazon S3** bucket for use by the ML
   pipeline.
5. Refined slot data is used to train and update the ML model on **Amazon SageMaker AI**, which can then predict the best offers for the individual
   customer.
6. The customer profile, ratings, and offers are updated in **Amazon DynamoDB** for fast retrieval by slot machines or a customer rating
   application.
7. Refined shuffler data is stored for aggregation and retrieval in **Amazon Aurora**.
8. Refined shuffler data is then used to extract metrics and develop an ML model to predict failures. Failure prediction in turn will recommend proactive maintenance.
9. The customer profile, ratings, and offers are made available to be consumed by games and applications to promote within the game or session.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/real-time-casino-player-analytics.md "samples/real-time-casino-player-analytics.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Games Industry Lens – AWS Well-Architected Framework](../../../wellarchitected/latest/games-industry-lens/games-industry-lens.md "../../../wellarchitected/latest/games-industry-lens/games-industry-lens.md")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date           |
| ------------------- | ----------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | April 19, 2022 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
