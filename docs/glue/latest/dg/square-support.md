

# AWS Glue support for Square

AWS Glue supports Square as follows:

**Supported as a source?**  
Yes. You can use AWS Glue ETL jobs to query data from Square.

**Supported as a target?**  
No.

**Supported Square API versions**  
The connector uses the Square API v2 and sends the `Square-Version` header `2026-09-16` on every request. The API version is not configurable.