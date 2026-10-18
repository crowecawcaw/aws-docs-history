

# Supported AWS Regions
<a name="kb-managed-regions"></a>

Managed Amazon Bedrock knowledge bases are available in the following AWS Regions:


**Regions where managed Amazon Bedrock knowledge bases are available**  

| Region | Region name | 
| --- | --- | 
| us-east-1 | US East (N. Virginia) | 
| us-west-2 | US West (Oregon) | 
| eu-west-1 | Europe (Ireland) | 
| eu-west-2 | Europe (London) | 
| eu-central-1 | Europe (Frankfurt) | 
| ap-northeast-1 | Asia Pacific (Tokyo) | 
| ap-southeast-2 | Asia Pacific (Sydney) | 
| us-gov-west-1 | AWS GovCloud (US-West) | 

## Feature differences in AWS GovCloud (US-West)
<a name="kb-managed-regions-govcloud"></a>

In AWS GovCloud (US-West) (`us-gov-west-1`), the following features are not supported:
+ **Third-party connector data sources.** Only the Amazon S3 connector and the Custom data source are available. Confluence, Microsoft SharePoint, Microsoft OneDrive, Google Drive, and Web Crawler data sources are not available.
+ **Document-level access control (ACLs).** The `aclEnabled` setting and ACL filtering at query time are not available.
+ **Service-managed embedding, reranking, and agentic retrieval models.** You must provide your own Amazon Bedrock embedding model when you create a knowledge base, and your own reranking model at query time if you want reranking. Agentic retrieval is not available.
+ **Amazon Bedrock AgentCore Gateway integration.** The AgentCore Gateway target for managed knowledge bases is not available.