

# Real-Time Casino Player Analytics
<a name="real-time-player-casino-analytics"></a>

Publication date: **April 19, 2022 ([Diagram history](#diagram-history))**

This architecture enables casino customers or game developers to build a real-time analytics pipeline and promote advertising offers to customers during the game session. 

## Real-Time Casino Player Analytics Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing enables casino customers or game developers to build a real-time analytics pipeline and promote advertising offers to customers during the game session.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/real-time-player-casino-analytics/images/real-time-player-casino-analytics.png)


1. Casino slot machine and shuffler data is streamed from the casino floor via a private network into **Amazon API Gateway** and **AWS IoT Core**, respectively. 

1. Data is then streamed into **Amazon Kinesis Data Streams**. 

1. Slot data from **Kinesis Data Streams** is processed by **AWS Lambda** to calculate customer rating and store a raw copy in **Amazon S3** for machine learning (ML) training. 

1. Raw data from slots and shufflers is transformed to identify unique records, and stored in a refined data **Amazon S3** bucket for use by the ML pipeline. 

1. Refined slot data is used to train and update the ML model on **Amazon SageMaker AI**, which can then predict the best offers for the individual customer. 

1. The customer profile, ratings, and offers are updated in **Amazon DynamoDB** for fast retrieval by slot machines or a customer rating application. 

1. Refined shuffler data is stored for aggregation and retrieval in **Amazon Aurora**. 

1. Refined shuffler data is then used to extract metrics and develop an ML model to predict failures. Failure prediction in turn will recommend proactive maintenance. 

1. The customer profile, ratings, and offers are made available to be consumed by games and applications to promote within the game or session. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Games Industry Lens – AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/games-industry-lens.html) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 19, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.