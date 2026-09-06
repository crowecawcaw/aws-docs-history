

# Reference architecture
<a name="s1-reference-architecture"></a>

 The following diagram illustrates the solution architecture and its key components for data cataloging, security, compliance, and data access requirements using DataHub. 

![Reference architecture for data discovery](http://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/images/scenario-1-ref.png)


1.  DataHub is an open-source metadata management platform which enables end-to-end discovery, data observability, data governance , data lineage and many more. It runs on an Amazon EKS cluster, using Amazon OpenSearch Service, Amazon Managed Streaming for Apache Kafka (Amazon MSK), and RDS for MySQL as the storage layer for the underlying data model and indexes. 

1.  Pull technical metadata from AWS Glue and Amazon Redshift to DataHub. 

1.  Enrich the technical metadata with a business glossary. 

1.  Run an AWS Glue job to transform the data and observe the data lineage in DataHub. 