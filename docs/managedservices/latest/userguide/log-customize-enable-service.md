# Enabling logging for supported services

Some services do not have logging enabled by default and require explicit enablement.

To enable logging for CloudFront, OpenSearch, Amazon RDS and Route53, submit an RFC with the Management | Other | Other | Create change type
(ct-1e1xtak34nx76) with the following values, replacing `variables` as appropriate:

```
Subject: Enable logging for `SERVICE_NAME`
Description: Service ARN: `SERVICE_ARN`
```
