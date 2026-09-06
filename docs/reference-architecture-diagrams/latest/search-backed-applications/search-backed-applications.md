

# Search-Backed Applications
<a name="search-backed-applications"></a>

Publication date: **November 17, 2022 ([Diagram history](#diagram-history))**

This architecture outlines the process to add or improve search for an existing application. It uses [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) for indexing and retrieval, [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) for ML enrichment, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for user interaction data storage.

## Search-Backed Applications
<a name="diagram1"></a>

![Architecture diagram showing search-backed applications with Amazon OpenSearch Service, SageMaker AI, Amazon RDS, and Amazon S3.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/search-backed-applications/images/search-backed-applications.png)


The following steps describe the architecture:

1. An application user sends a query to the web servers.

1. The web servers deliver the query to the query service. The query service can use ML models from SageMaker AI for user segmentation, concept and entity extraction, and query-to-click analysis.

1. The query service enriches or rewrites the query based on user segmentation from SageMaker AI, user preferences from [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), and past query performance. It sends the augmented query to Amazon OpenSearch Service.

1. The user sends only searchable data to Amazon OpenSearch Service, using a relational or NoSQL system as the system of record. The query service retrieves only keys in the search results and fetches the full record from the system of record.

1. The web servers and query service send user interaction data to an Amazon S3 data lake or [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html).

1. An offline process pulls user interaction data from the data lake.

1. The offline process takes data such as clicks to augment the records in the catalog and updates models in SageMaker AI.

1. Records are updated in Amazon OpenSearch Service as needed.

1. The web servers send catalog updates to Amazon OpenSearch Service, or a change data capture process brings those updates to Amazon OpenSearch Service.

1. Business analysts generate reporting and KPIs from the processed user interactions.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 17, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.