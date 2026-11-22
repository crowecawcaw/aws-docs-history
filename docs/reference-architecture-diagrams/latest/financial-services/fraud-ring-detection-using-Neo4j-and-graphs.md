

# Fraud ring detection using Neo4j and graphs

Publication date: **June 10, 2024 ([Diagram history](diagram-history.md))**

This architecture helps you to set up detection of fraud rings using graphs. Fraud detection, graph embeddings, and other graph algorithms can improve ML model performance beyond what's possible with more traditional approaches.

## Fraud ring detection using Neo4j and graphs diagram
<a name="fraud-ring-diagram"></a>

![Diagram showing data ingested into Neo4j, then analyzed with SageMaker AI, Lambda, and customer apps.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/fraud-ring-detection-using-Neo4j-and-graphs.png)


The following steps describe the architecture:

1. Banking transactions, customer accounts, and banking apps clickstream data flow from input data sources.

1. [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) ingest, transform, and enrich batch data. [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) and [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/) read real-time data.

1. Connectors for Spark Datawarehouse and Java Database Connectivity (JDBC) load bulk and batch data to Neo4j. You can also use database APIs.

1. Neo4j Kafka Connector or Neo4j Spark Connector streaming APIs ingest clickstream and near real-time transaction and application data from Amazon Kinesis or Amazon MSK to the Neo4j database.

1. The Neo4j Aura Graph Database (GDB) and Neo4j Aura Graph Data Science (GDS) allow you to store, query, analyze, and manage highly connected data. Neo4j Aura is deployed as a SaaS on AWS.

1. Data scientists create novel graph features using embedding algorithms in GDS through [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) Studio notebooks. Embeddings are exported to SageMaker AI for improved accuracy. Data scientists can use additional graph algorithms, including community detection and similarity in GDS. Data scientists can write graph features back to GDB or relational systems, where they can be easily visualized and analyzed.

1. Scientists can further enhance predictive results by matching patterns and additional information with the graph data. Developers can use Neo4j GraphQL library and drivers to access Neo4j with Java, Node, JavaScript, C\#, Python, Go, Ruby, PHP, Erlang, and Perl from [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) or any application.

1. Neo4j Bloom visualization and customer dashboard tools allow analysts to explore data and present findings.

## Further reading
<a name="fraud-ring-further-reading"></a>

For additional information, see the following resources:
+  [About Neo4j](https://aws.amazon.com/marketplace/seller-profile?id=23ec694a-d2af-4641-b4d3-b7201ab2f5f9) 
+  [Neo4j on AWS](https://neo4j.com/partners/amazon/) 
+  [Neo4j use cases: fraud detection and analytics](https://neo4j.com/use-cases/fraud-detection/) 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 