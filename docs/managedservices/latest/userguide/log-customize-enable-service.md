End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Enabling logging for supported services

Some services do not have logging enabled by default and require explicit enablement.

To enable logging for CloudFront, OpenSearch, Amazon RDS and Route53, submit an RFC with the Management | Other | Other | Create change type
(ct-1e1xtak34nx76) with the following values, replacing `variables` as appropriate:

```
Subject: Enable logging for `SERVICE_NAME`
Description: Service ARN: `SERVICE_ARN`
```
