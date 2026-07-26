# CloudWatch pipelines configuration for Wazuh Platform

Collects security event data from Wazuh Platform using Basic authentication through the Wazuh Indexer API.

Configure the Wazuh Platform source with the following parameters:

```
source:
  wazuh_platform:
    host: "https://wazuh-indexer.example.com:9200"
    authentication:
      basic:
        username: "${{aws_secrets:<secret-name>:username}}"
        password: "${{aws_secrets:<secret-name>:password}}"
```

###### Parameters

`host` (required)

The Wazuh Indexer base URL including scheme and port (for example, `https://wazuh-indexer.example.com:9200`).

`authentication.basic.username` (required)

The Wazuh Indexer username, stored in AWS Secrets Manager.

`authentication.basic.password` (required)

The Wazuh Indexer password, stored in AWS Secrets Manager.
