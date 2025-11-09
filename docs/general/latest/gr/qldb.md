# Amazon QLDB endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

### QLDB resource management API

| Region Name              | Region         | Endpoint                                                                | Protocol       |
| ------------------------ | -------------- | ----------------------------------------------------------------------- | -------------- |
| US East (Ohio)           | us-east-2      | qldb.us-east-2.amazonaws.com<br>qldb-fips.us-east-2.amazonaws.com       | HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | qldb.us-east-1.amazonaws.com<br>qldb-fips.us-east-1.amazonaws.com       | HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | qldb.us-west-2.amazonaws.com<br>qldb-fips.us-west-2.amazonaws.com       | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)     | ap-northeast-2 | qldb.ap-northeast-2.amazonaws.com                                       | HTTPS          |
| Asia Pacific (Singapore) | ap-southeast-1 | qldb.ap-southeast-1.amazonaws.com                                       | HTTPS          |
| Asia Pacific (Sydney)    | ap-southeast-2 | qldb.ap-southeast-2.amazonaws.com                                       | HTTPS          |
| Asia Pacific (Tokyo)     | ap-northeast-1 | qldb.ap-northeast-1.amazonaws.com                                       | HTTPS          |
| Canada (Central)         | ca-central-1   | qldb.ca-central-1.amazonaws.com<br>qldb-fips.ca-central-1.amazonaws.com | HTTPS<br>HTTPS |
| Europe (Frankfurt)       | eu-central-1   | qldb.eu-central-1.amazonaws.com                                         | HTTPS          |
| Europe (Ireland)         | eu-west-1      | qldb.eu-west-1.amazonaws.com                                            | HTTPS          |
| Europe (London)          | eu-west-2      | qldb.eu-west-2.amazonaws.com                                            | HTTPS          |

### QLDB transactional data API

| Region Name              | Region         | Endpoint                                                                          | Protocol       |
| ------------------------ | -------------- | --------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)           | us-east-2      | session.qldb.us-east-2.amazonaws.com<br>session.qldb-fips.us-east-2.amazonaws.com | HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | session.qldb.us-east-1.amazonaws.com<br>session.qldb-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | session.qldb.us-west-2.amazonaws.com<br>session.qldb-fips.us-west-2.amazonaws.com | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)     | ap-northeast-2 | session.qldb.ap-northeast-2.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Singapore) | ap-southeast-1 | session.qldb.ap-southeast-1.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Sydney)    | ap-southeast-2 | session.qldb.ap-southeast-2.amazonaws.com                                         | HTTPS          |
| Asia Pacific (Tokyo)     | ap-northeast-1 | session.qldb.ap-northeast-1.amazonaws.com                                         | HTTPS          |
| Canada (Central)         | ca-central-1   | session.qldb.ca-central-1.amazonaws.com                                           | HTTPS          |
| Europe (Frankfurt)       | eu-central-1   | session.qldb.eu-central-1.amazonaws.com                                           | HTTPS          |
| Europe (Ireland)         | eu-west-1      | session.qldb.eu-west-1.amazonaws.com                                              | HTTPS          |
| Europe (London)          | eu-west-2      | session.qldb.eu-west-2.amazonaws.com                                              | HTTPS          |

## Service quotas

| Name                    | Default                  | Adjustable                                                                                                                                                                   | Description                                                                            |
| ----------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Ledgers                 | Each supported Region: 5 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/qldb/quotas/L-CD70CADB "https://console.aws.amazon.com/servicequotas/home/services/qldb/quotas/L-CD70CADB") | The maximum number of active ledgers allowed per account in a given region.            |
| QLDB exports per ledger | Each supported Region: 2 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/qldb/quotas/L-22B6E165 "https://console.aws.amazon.com/servicequotas/home/services/qldb/quotas/L-22B6E165") | The maximum number of active exports allowed per ledger per account in a given region. |
| QLDB streams per ledger | Each supported Region: 5 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/qldb/quotas/L-91B08359 "https://console.aws.amazon.com/servicequotas/home/services/qldb/quotas/L-91B08359") | The maximum number of active streams allowed per ledger per account in a given region. |

For more information, see [Quotas in Amazon QLDB](../../../qldb/latest/developerguide/limits.md "../../../qldb/latest/developerguide/limits.md")
in the _Amazon QLDB Developer Guide_.
