

# Product recommendations with Neo4j

Publication date: **September 20, 2022 ([Diagram history](diagram-history.md))**

With this architecture, you can deliver personalized product recommendations in near real time. The solution uses Neo4j Graph Database (GDB) and Graph Data Science (GDS) on AWS for storing and analyzing connected data, [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for data processing, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for machine learning (ML), and [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) for streaming ingestion.

## Product recommendations with Neo4j diagram
<a name="neo4j-rec-diagram"></a>

![Ingested data is transformed and loaded into Neo4j, with embeddings exported to SageMaker AI to serve recommendations.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/product-recommendations-neo4j.png)


The following steps describe the data pipeline and recommendation engine for this architecture:

1. Ingest customer orders, product data, and clickstream data through [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), Amazon EMR, [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), and Amazon Kinesis.

1. Transform and enrich data by using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), Apache Spark on Amazon EMR, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), or other tools.

1. Load bulk and batch data to Neo4j by using the Neo4j Spark Connector for Amazon EMR or Neo4j APIs running in Lambda.

1. Stream near real-time data from Apache Kafka on AWS through the Neo4j Kafka Connector to the Neo4j database.

1. Flow clickstream data from Amazon Kinesis through the Neo4j Spark Connector running on Amazon EMR to the Neo4j database.

1. Store, query, analyze, and manage highly connected data by using Neo4j GDB and GDS. Deploy Neo4j Aura as a fully managed service on AWS, or run Neo4j Enterprise on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances.

1. Create features on Neo4j GDB and GDS. Export graph embeddings to SageMaker AI for training ML models.

1. Explore data and present findings by using [AWS Quick](https://docs.aws.amazon.com/quick/latest/userguide/) and Neo4j Bloom visualization tools.

1. Access Neo4j by using official drivers from Lambda or any application. Use a low-code approach with GraphQL API and the GRANDStack framework through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/).

1. Run the recommendation services by using Neo4j GDB and GDS at scale in near real time. Apply this framework to build similar recommendation engines for additional use cases.

## Further reading
<a name="neo4j-rec-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 