

# AWS service integrations with Security Lake
<a name="aws-integrations"></a>

Amazon Security Lake integrates with other AWS services. A service may either operate as a *source integration*, a *subscriber integration*, or both.

Source integrations have the following properties:
+ Send data to Security Lake
+ Data arrives in the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md) schema
+ Data arrives in Apache Parquet format

Subscriber integrations can access Security Lake data in one of the following ways:
+ Read source data from Security Lake through an HTTPS endpoint
+ Read source data from Security Lake through an Amazon Simple Queue Service (Amazon SQS)
+ By directly querying source data using AWS Lake Formation

The following table provides a list of AWS service integrations that Security Lake supports.


| AWS service | Integration type | Description | How integration works | 
| --- | --- | --- | --- | 
| [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) | Subscriber | Generate AI-powered insights to analyze Security Lake data. | [Amazon Bedrock integration](bedrock-integration.md) | 
| [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html)  | Subscriber | Analyze, investigate, and quickly identify the root cause of security findings or suspicious activities by querying Security Lake. | [Amazon Detective integration](detective-integration.md) | 
| [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)  | Subscriber | Generate security insights from Security Lake data by using OpenSearch Service ingestion. | [Amazon OpenSearch Service integration](opensearch-integration.md) | 
| [Amazon OpenSearch Service ingestion pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html)  | Subscriber, Source | Stream logs, metrics, and trace data to OpenSearch Service and Security Lake. | [Amazon OpenSearch Service Ingestion pipeline integration](opensearch-ingestion-pipeline-integration.md) | 
| [Amazon OpenSearch Service zero-ETL](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query.html)  | Subscriber (Query) | Query data in Security Lake with zero-ETL. | [Amazon OpenSearch Service zero-ETL direct query integration](opensearch-datasource-integration.md) | 
| [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)  | Subscriber | Visualize, explore, and interpret logs in Security Lake with Quick. | [Quick integration](quicksight-integration.md) | 
| [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)  | Subscriber | Generate AI-powered insights to analyze Security Lake data. | [Amazon SageMaker AI integration](sagemaker-integration.md) | 
| [AWS AppFabric](https://docs.aws.amazon.com/appfabric/latest/adminguide/what-is-appfabric.html)  | Source | Ingests and normalize software as a service (SaaS) application logs into Security Lake standard format. | [AWS AppFabric integration](appfabric-integration.md) | 
| [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)  | Source | Centralize and store security findings from Security Hub CSPM in Security Lake standard format. | [AWS Security Hub CSPM integration](securityhub-integration.md) | 