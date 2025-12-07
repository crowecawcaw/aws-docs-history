# CloudWatch pipelines configuration for ServiceNow CMDB

Audit Log

Collects configuration management database (CMDB) data from ServiceNow using
OAuth2 authentication.

Configure the ServiceNow CMDB source with the following parameters:

```
source:
  servicenow_cmdb:
    instance_url: "<example-instance-url>"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`instance_url` (required)

ServiceNow instance URL.

`authentication.oauth2.client_id` (required)

OAuth2 client ID for ServiceNow API authentication.

`authentication.oauth2.client_secret` (required)

OAuth2 client secret for ServiceNow API authentication.
