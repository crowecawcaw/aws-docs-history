

# Exploring Real-Time Streaming for Retrieval Augmented Generation in GenerativeAI
<a name="exploring-real-time-streaming-for-retrieval-augmented-generation"></a>

Publication date: **August 12, 2024 ([Diagram history](#diagram-history))**

This architecture demonstrates the integration of streaming data services on AWS with Retrieval Augmented Generation(RAG) in Generative AI applications.

## Exploring Real-Time Streaming for Retrieval Augmented Generation in GenerativeAI
<a name="diagram1"></a>

![Reference architecture diagram that demonstrates the integration of streaming data services on AWS with Retrieval Augmented Generation(RAG) in Generative AI applications.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/exploring-real-time-streaming-for-retrieval-augmented-generation/images/exploring-real-time-streaming-for-retrieval-augmented-generation.png)


1. Data sources for change data capture(CDC) includes on-premise or AWS databases such as Oracle, SQL Server, MySQL, PostgreSQL, **Amazon Aurora **, and **Amazon RDS**, all funneling data into your Retrieval Augmented Generation(RAG) model.

1. **AWS Database Migration Service** and **Amazon MSK Connect with Debezium connector** help with one-time data migration of databases and continuous data replication. **AWS Database Migration Service **and **Amazon MSK Connect with Debezium connector **captures and stream changes from source databases and applies them in same order they are captured to the target.

1. Utilizing **AWS Database Migration Service** and **Amazon MSK Connect with Debezium connector** enables the streaming of data to **Amazon Kinesis Data Streams** or **Amazon Managed Streaming for Apache Kafka (Amazon MSK)** , facilitating the collection and processing of large streams.

1. By utilizing **AWS Glue **Spark Streaming and** Amazon Managed Service for Apache Flink** , you can construct specialized data processing pipelines to cater to your data consumption requirements.

1. **AWS Lambda** , **Amazon Kinesis Data Firehose** and **Amazon MSK Connect** , which serve as data sink services, enable the direct transfer of source data into destinations like **Data Lake** , **Amazon Redshift**, among others.

1. Leveraging **Amazon Aurora PostgreSQL with pgvector**, **Amazon Opensearch** and **Amazon DocumentDB** allows the generation of vector embeddings for streamlined data retrieval , vector representation management, scalability, and real-time inference capabilities.

1. **Amazon SageMaker** and **Amazon Bedrock** offers the means to discover pertinent information within a corpus, conduct similarity search on vectorized domain specific datasets, and use this data as input for generation models.

1. To preserve user profiles and conversation history, **Amazon DocumentDB**, **Amazon DynamoDB** and **Amazon MemoryDB** provide suitable options.

1. Leverage **Amazon Redshift** service to ensure data persistence, thereby augmenting the data inputs for the Generative AI RAG model.

1. For details on the workings of RAG applications, refer to [Retrieval-Augmented Generation(RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/)

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Jatinder Singh (jsinghtq@), Senior Technical Account Manager 
+  Manpreet Kour (mkour@), Senior Technical Account Manager 
+  Ali Alemi (alialem@), Senior WW SSA Streaming 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 22, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.