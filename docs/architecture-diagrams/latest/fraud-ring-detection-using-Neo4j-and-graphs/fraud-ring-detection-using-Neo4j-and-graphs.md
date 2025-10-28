# Fraud ring detection using Neo4j and graphs

Publication date: **June 10, 2024 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture helps you to set up detection of fraud rings using graphs.
Fraud Detection, graph embeddings, and other graph algorithms can improve ML model
performance beyond what’s possible with more traditional approaches.

## Fraud ring detection using Neo4j and graphs diagram

![Reference architecture diagram showing data sources being ingested into Amazon S3 and Neo4j resources, then analyzed by SageMaker AI, Lambda, Neo4j resources, and customer apps.](images/fraud-ring-detection-using-Neo4j-and-graphs.png)

1. Banking transactions, customer accounts, and banking apps clickstream data flow from input data sources.
2. AWS Glue and Amazon EMR ingest, transform, and enrich batch data. Amazon Kinesis and Amazon MSK read real-time data.
3. Connectors for Spark Datawarehouse and Java Database Connectivity (JDBC)
   load bulk and batch data to Neo4j. You can also use database APIs.
4. Neo4j Kafka Connector or Neo4j Spark Connector streaming APIs ingest clickstream
   and near real-time transaction and application data from Amazon Kinesis or Amazon MSK to the Neo4j database.
5. The Neo4j Aura Graph Database (GDB) and Neo4j Aura Graph Data Science (GDS)
   allow you to store, query, analyze, and manage highly-connected data.
   Neo4j Aura is deployed as a SaaS on AWS.
6. Data scientists create novel graph features using embedding algorithms in GDS via
   Amazon SageMaker AI Studio notebooks. Embeddings are exported to Amazon SageMaker AI for improved accuracy.
   Data scientists can leverage additional graph algorithms, including community detection and similarity in GDS.
   Data scientists can write graph features back to GDB or relational systemsm, where they can be easily visualized and analyzed.
7. Scientists can further enhance predictive results by matching patterns and additional information with the graph data.
   Developers can use Neo4j GraphQL library and drivers to access Neo4j with Java, Node, JavaScript, C#, Python,
   Go, Ruby, PHP, Erlang, and Perl from AWS Lambda or any application.
8. Neo4j Bloom visualization and customer dashboard tools allow analysts to explore data and present findings.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/fraud-ring-detection-using-Neo4j-and-graphs.md "samples/fraud-ring-detection-using-Neo4j-and-graphs.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [About Neo4j](https://aws.amazon.com/marketplace/seller-profile?id=23ec694a-d2af-4641-b4d3-b7201ab2f5f9 "https://aws.amazon.com/marketplace/seller-profile?id=23ec694a-d2af-4641-b4d3-b7201ab2f5f9")
- [Neo4j on AWS](https://neo4j.com/partners/amazon/ "https://neo4j.com/partners/amazon/")
- [Neo4j Use Cases: Fraud Detection and Analytics](https://neo4j.com/use-cases/fraud-detection/ "https://neo4j.com/use-cases/fraud-detection/")
- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | June 10, 2024 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
