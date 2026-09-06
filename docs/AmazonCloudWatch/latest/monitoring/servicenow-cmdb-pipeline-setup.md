

# CloudWatch pipelines configuration for ServiceNow CMDB Audit Log
<a name="servicenow-cmdb-pipeline-setup"></a>

Collects configuration management database (CMDB) data from ServiceNow using OAuth2 authentication.

Configure the ServiceNow CMDB source with the following parameters:

```
source:
  servicenow_cmdb:
    instance_url: "<example-instance-url>"
    range: "P7D"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```Parameters

`instance_url` (required)  
ServiceNow instance URL.

`authentication.oauth2.client_id` (required)  
OAuth2 client ID for ServiceNow API authentication.

`authentication.oauth2.client_secret` (required)  
OAuth2 client secret for ServiceNow API authentication.

`range` (optional)  
The time range for log collection. Uses ISO 8601 duration format (for example, `P7D` for the last 7 days, `PT21H` for 21 hours). Default is 0 hours, and the maximum is 90 days.