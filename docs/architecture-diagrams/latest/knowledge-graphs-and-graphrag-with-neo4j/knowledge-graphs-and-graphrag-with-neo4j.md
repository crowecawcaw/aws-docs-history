# Knowledge Graphs and GraphRAG with AWS and Neo4j

Publication date: **November 26, 2024 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture demonstrates how AWS services and Neo4j can be used to create knowledge graphs. Those graphs can then be used in a GraphRAG architecture.

## Knowledge Graphs and GraphRAG with AWS and Neo4j Diagram

![Reference architecture diagram showing how AWS services and Neo4j can be used to create knowledge graphs that can then be used in a GraphRAG architecture.](images/knowledge-graphs-and-graphrag-with-neo4j.png)

1. Structured, unstructured, and semi-structured data exists in a wide variety of systems, including **Amazon Redshift**,
   **Amazon Simple Storage Service** (Amazon S3), and **Amazon Managed Streaming for Apache Kafka** (Amazon MSK).
   Other systems can be accessed through an integration layer such as **AWS Glue**.
   Some subset of this data is highly connected. Insights can be uncovered by modeling it as a graph.
2. Scripts running in **Amazon SageMaker AI** pull connected data from these source systems.
3. Once in **SageMaker AI**, the data is passed to an **Amazon Bedrock**
   process managed by LangChain. Large language models (LLMs) extract entities and format the result as Cypher,
   the Neo4j query language. **SageMaker AI** passes that Cypher to the Neo4j driver.
4. Cypher statements wrapping the extracted data and entities are fed into the Neo4j graph database
   to create a knowledge graph. The Graph Database is one component of Neo4j AuraDB, a Neo4j SaaS
   running on AWS.
5. Users can explore the resulting knowledge graph in Neo4j Bloom, a BI tool designed specifically for graphs.
6. Enrichment can be done with Neo4j Graph Data Science. Entity resolution algorithms resolve
   duplicate entries. Community detection algorithms can be used to identify clusters and
   generate local cluster summaries for GraphRAG. Graph embedding algorithms help map and
   identify topologically similar entities for GraphRAG.
7. With a knowledge graph created, applications can then make use of that graph in a
   GraphRAG architecture to provide grounded results with fewer hallucinations than
   alternative approaches. Those applications can run in a variety of AWS platforms,
   including **AWS Lambda**, **Amazon Elastic Compute Cloud** (Amazon EC2),
   and **Amazon Elastic Kubernetes Service** (Amazon EKS).
8. Client applications can make calls into functions hosted in **SageMaker AI**.
   Those functions query **Amazon Bedrock**.
9. **Amazon Bedrock** responses are grounded using Neo4j Graph Database
   with data gathered from the wider enterprise. Using a graph for grounding provides a vector
   RAG approach with the additional ability to use the structure of the graph to improve responses.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/knowledge-graphs-and-graphrag-with-neo4j.md "samples/knowledge-graphs-and-graphrag-with-neo4j.md") which contains an editable PowerPoint.

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

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | November 26, 2024 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
