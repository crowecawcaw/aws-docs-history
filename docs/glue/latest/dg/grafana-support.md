

# AWS Glue support for Grafana

AWS Glue supports Grafana as follows:

**Supported as a source?**  
Yes. You can use AWS Glue ETL jobs to query data from Grafana.

**Supported as a target?**  
No.

**Supported Grafana API versions**  
The connector uses the Grafana HTTP API under `/api`, including the alerting provisioning API under `/api/v1/provisioning`. The API version is not configurable.