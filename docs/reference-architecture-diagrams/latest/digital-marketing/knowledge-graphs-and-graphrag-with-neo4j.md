

# Knowledge graphs and GraphRAG with AWS and Neo4j

Publication date: **November 26, 2024 ([Diagram history](diagram-history.md))**

With this reference architecture, you can use AWS services and Neo4j to create knowledge graphs, then use those graphs in a GraphRAG architecture.

## Knowledge graphs and GraphRAG with AWS and Neo4j diagram
<a name="knowledge-graphs-and-graphrag-with-neo4j-diagram"></a>

![Amazon SageMaker AI and Amazon Bedrock build Neo4j knowledge graphs that ground GraphRAG applications on AWS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/digital-marketing/images/knowledge-graphs-and-graphrag-with-neo4j.png)


The following steps describe the architecture:

1. Structured, unstructured, and semi-structured data exists in a wide variety of systems, including [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), and [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) (Amazon MSK). Other systems can be accessed through an integration layer such as [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Some subset of this data is highly connected. Insights can be uncovered by modeling it as a graph. 

1.  Scripts running in [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) pull connected data from these source systems. 

1.  Once in SageMaker AI, the data is passed to an [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/) process managed by LangChain. Large language models (LLMs) extract entities and format the result as Cypher, the Neo4j query language. SageMaker AI passes that Cypher to the Neo4j driver. 

1.  Cypher statements wrapping the extracted data and entities are fed into the Neo4j graph database to create a knowledge graph. The Graph Database is one component of Neo4j AuraDB, a Neo4j SaaS running on AWS. 

1.  Users can explore the resulting knowledge graph in Neo4j Bloom, a BI tool designed specifically for graphs. 

1.  Enrichment can be done with Neo4j Graph Data Science. Entity resolution algorithms resolve duplicate entries. Community detection algorithms can be used to identify clusters and generate local cluster summaries for GraphRAG. Graph embedding algorithms help map and identify topologically similar entities for GraphRAG. 

1.  With a knowledge graph created, applications can then make use of that graph in a GraphRAG architecture to provide grounded results with fewer hallucinations than alternative approaches. Those applications can run in a variety of AWS platforms, including [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), and [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) (Amazon EKS). 

1.  Client applications can make calls into functions hosted in SageMaker AI. Those functions query Amazon Bedrock. 

1.  Amazon Bedrock responses are grounded using Neo4j Graph Database with data gathered from the wider enterprise. Using a graph for grounding provides a vector RAG approach with the additional ability to use the structure of the graph to improve responses. 

## Further reading
<a name="knowledge-graphs-and-graphrag-with-neo4j-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 