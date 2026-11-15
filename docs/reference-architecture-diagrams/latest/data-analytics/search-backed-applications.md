

# Search-backed applications
<a name="search-backed-applications"></a>

Publication date: **November 17, 2022 ([Diagram history](diagram-history.md))**

This architecture outlines the process to add or improve search for an existing application. It uses [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) for indexing and retrieval, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for ML enrichment, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for user interaction data storage.

## Search-backed applications diagram
<a name="search-backed-applications-diagram1"></a>

![Query service enriches queries with SageMaker AI and Amazon RDS data, searches OpenSearch Service, and logs to Amazon S3.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/search-backed-applications.png)


The following steps describe the architecture:

1. An application user sends a query to the web servers.

1. The web servers deliver the query to the query service. The query service can use ML models from SageMaker AI for user segmentation, concept and entity extraction, and query-to-click analysis.

1. The query service enriches or rewrites the query based on user segmentation from SageMaker AI, user preferences from [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), and past query performance. It sends the augmented query to Amazon OpenSearch Service.

1. Send only searchable data to Amazon OpenSearch Service, and use a relational or NoSQL system as the system of record. The query service retrieves only keys in the search results and fetches the full record from the system of record.

1. The web servers and query service send user interaction data to an Amazon S3 data lake or [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/).

1. An offline process pulls user interaction data from the data lake.

1. The offline process takes data such as clicks to augment the records in the catalog and updates models in SageMaker AI.

1. Records are updated in Amazon OpenSearch Service as needed.

1. The web servers send catalog updates to Amazon OpenSearch Service, or a change data capture process brings those updates to Amazon OpenSearch Service.

1. Business analysts generate reporting and KPIs from the processed user interactions.

## Further reading
<a name="search-backed-applications-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)