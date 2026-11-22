

# AWS Glue support for Pipedrive

AWS Glue supports Pipedrive as follows:

**Supported as a source?**  
Yes. You can use AWS Glue ETL jobs to query data from Pipedrive.

**Supported as a target?**  
No.

**Supported Pipedrive API versions**  
 v1 and v2. AWS Glue uses Pipedrive API v2 for the entities that have a v2 endpoint (Activities, Deals, Organizations, Persons, Pipelines, Products, and Stages) and v1 for all other entities. When a connection is set to v2, any entity that does not have a v2 endpoint automatically falls back to v1. 