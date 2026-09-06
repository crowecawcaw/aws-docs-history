

# Supported catalogs
<a name="catalog-integration-supported-catalogs"></a>

The following table lists the supported catalogs and their capabilities in this preview.


**Supported catalogs and capabilities**  

| Catalog | Capability | What it enables | Authentication | 
| --- | --- | --- | --- | 
| AWS Glue Data Catalog | Agentic discovery, bulk create, semantic inheritance | AI-powered discovery and dataset creation from Glue metadata, with automatic inheritance of table and column descriptions | Service role or AWS IAM Identity Center | 
| AWS Glue Data Catalog | Trusted identity propagation (TIP) | Per-user data permissions enforcement through AWS IAM Identity Center and Lake Formation | AWS IAM Identity Center | 
| Databricks Unity Catalog | Agentic discovery, bulk create, semantic inheritance | AI-powered discovery and dataset creation from Unity Catalog metadata, with automatic inheritance of descriptions and relationships | Personal Access Token (PAT) or OAuth 3LO | 
| Databricks Unity Catalog | Identity propagation (3LO) | Per-user data permissions enforcement through Databricks OAuth | OAuth 3LO | 