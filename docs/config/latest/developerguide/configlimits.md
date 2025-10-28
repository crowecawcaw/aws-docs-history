# Service Limits for AWS Config

The following table describes limits within AWS Config. Unless noted otherwise, the quotas can
be increased upon request. You can [request a quota
increase](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home").

For information about other limits in AWS, see [AWS
Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

| Resource tags                                                            | Description | Limit Value | Can be increased                                                                                                                                                                                                                |
| ------------------------------------------------------------------------ | ----------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------- | ---------------- |
| Maximum number of tags per resource                                      | 50          | No          | AWS Config rules                                                                                                                                                                                                                | Description | Limit Value | Can be increased |
| ---                                                                      | ---         | ---         |
| Maximum number of AWS Config Rules per Region per account                | 1000        | No          | Single Account Conformance Packs                                                                                                                                                                                                | Description | Limit Value | Can be increased |
| ---                                                                      | ---         | ---         |
| Maximum number of conformance packs per account                          | 50          | No          |
| Maximum number of AWS Config Rules per conformance pack                  | 130         | No          | ###### Note AWS Config rules in conformance packs count in the limit for the Maximum number of AWS Config Rules per Region per account. Organization Conformance Packs                                                          | Description | Limit Value | Can be increased |
| ---                                                                      | ---         | ---         |
| Maximum number of conformance packs per organization                     | 50          | No          |
| Maximum number of AWS Config Rules per organization conformance pack     | 130         | No          | ###### Note Deploying at the organization level counts in the limit for child accounts. AWS Config rules in conformance packs count in the limit for the Maximum number of AWS Config Rules per Region per account. Aggregators | Description | Limit Value | Can be increased |
| ---                                                                      | ---         | ---         |
| Maximum number of configuration aggregators                              | 50          | Yes         |
| Maximum number of accounts in an aggregator                              | 10000       | No          |
| Maximum number of accounts added or deleted per week for all aggregators | 1000        | Yes         | ###### Note Organization level aggregators and individual account aggregators both count in the limit for the Maximum number of configuration aggregators. Advanced queries                                                     | Description | Limit Value | Can be increased |
| ---                                                                      | ---         | ---         |
| Maximum number of saved queries in a single account and a Region         | 300         | Yes         |
