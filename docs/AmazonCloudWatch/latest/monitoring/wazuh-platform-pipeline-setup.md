

# CloudWatch pipelines configuration for Wazuh Platform
<a name="wazuh-platform-pipeline-setup"></a>

Collects audit logs from Wazuh Platform using Basic authentication.

Configure the Wazuh Platform source with the following parameters:

```
source:
  wazuh_platform:
    host: "https://<wazuh-indexer-host>:9200"
    authentication:
      username: "${{aws_secrets:wazuh-credentials:username}}"
      password: "${{aws_secrets:wazuh-credentials:password}}"
    acknowledgments: true
```Parameters

`host` (required)  
Wazuh Indexer base URL including scheme and port (for example, `https://<wazuh-indexer-host>:9200`). This is a customer-configured domain – each customer hosts their own Wazuh Indexer instance.

`authentication` (required)  
Block containing Wazuh Indexer authentication settings. Contains the nested parameters listed below.

`authentication.username` (required)  
Wazuh Indexer username for HTTP Basic Authentication. Typically sourced from AWS Secrets Manager using the `${{aws_secrets:<secret-name>:<key>}}` reference syntax.

`authentication.password` (required)  
Wazuh Indexer password for HTTP Basic Authentication. Typically sourced from AWS Secrets Manager using the `${{aws_secrets:<secret-name>:<key>}}` reference syntax.

`acknowledgments` (optional)  
Prevents data loss by only considering logs successfully processed after they are received by the sink. Accepts `true` or `false`. Default: `true`.

**Note**  
The `username` and `password` values are retrieved from AWS Secrets Manager. The above parameter information can be obtained from the Wazuh Indexer installation or user management configuration.