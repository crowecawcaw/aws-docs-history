

# Real-time streaming for RAG

Publication date: **August 12, 2024 ([Diagram history](diagram-history.md))**

This architecture demonstrates the integration of streaming data services on AWS with Retrieval Augmented Generation (RAG) in generative AI applications.

## Real-time streaming for RAG diagram
<a name="exploring-rts-diagram"></a>

![Database changes stream through data services on AWS into a RAG generative AI model.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/exploring-real-time-streaming-for-retrieval-augmented-generation.png)


The following steps describe the architecture:

1. Data sources for change data capture (CDC) include on-premises or AWS databases such as Oracle, SQL Server, MySQL, PostgreSQL, [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), and [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), all funneling data into your Retrieval Augmented Generation (RAG) model.

1. [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) and [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) (Amazon MSK) Connect with the Debezium connector help with one-time data migration of databases and continuous data replication. AWS DMS and Amazon MSK Connect with the Debezium connector capture and stream changes from source databases and apply them in the same order they are captured to the target.

1. Using AWS DMS and Amazon MSK Connect with the Debezium connector enables the streaming of data to [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) Data Streams or Amazon MSK, facilitating the collection and processing of large streams.

1. By using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Spark Streaming and [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/), you can construct specialized data processing pipelines to cater to your data consumption requirements.

1. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), and Amazon MSK Connect, which serve as data sink services, enable the direct transfer of source data into destinations like a data lake and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/), among others.

1. Using Aurora PostgreSQL with pgvector, [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/), and Amazon DocumentDB allows the generation of vector embeddings for streamlined data retrieval, vector representation management, scalability, and real-time inference capabilities.

1. [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) and Amazon Bedrock offer the means to discover pertinent information within a corpus, conduct similarity search on vectorized domain-specific datasets, and use this data as input for generation models.

1. To preserve user profiles and conversation history, Amazon DocumentDB, [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), and [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/) provide suitable options.

1. Use the Amazon Redshift service to ensure data persistence, thereby augmenting the data inputs for the generative AI RAG model.

1. For details on the workings of RAG applications, refer to [Retrieval-Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/).

## Further reading
<a name="exploring-rts-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 