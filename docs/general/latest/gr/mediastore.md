# AWS Elemental MediaStore endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name           | Region         | Endpoint                                | Protocol |
| --------------------- | -------------- | --------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1      | mediastore.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)      | us-west-2      | mediastore.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Seoul)  | ap-northeast-2 | mediastore.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | mediastore.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)  | ap-northeast-1 | mediastore.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)    | eu-central-1   | mediastore.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)      | eu-west-1      | mediastore.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)       | eu-west-2      | mediastore.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Stockholm)    | eu-north-1     | mediastore.eu-north-1.amazonaws.com     | HTTPS    |

## Service quotas

| Name                                                                                                       | Default                             | Adjustable                                                                                                                                                                               | Description                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Containers                                                                                                 | Each supported Region: 100          | No                                                                                                                                                                                       | The maximum number of containers that you can create in this account.                                                                                                                              |
| Folder levels                                                                                              | Each supported Region: 10           | No                                                                                                                                                                                       | The maximum number of folder levels that you can create in a container. You can create as many folders as you want, as long as they are not nested more than 10 levels within a container.         |
| Object size                                                                                                | Each supported Region: 25 Megabytes | No                                                                                                                                                                                       | The maximum size of a single object.                                                                                                                                                               |
| Rate of DeleteObject API requests                                                                          | Each supported Region: 100          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-2FCDD326 "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-2FCDD326") | The maximum number of DeleteObject requests that you can make per second. Additional requests are throttled.                                                                                       |
| Rate of DescribeObject API requests                                                                        | Each supported Region: 1,000        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-8038710B "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-8038710B") | The maximum number of DescribeObject requests that you can make per second. Additional requests are throttled.                                                                                     |
| Rate of GetObject API requests for standard upload availability                                            | Each supported Region: 1,000        | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-DB1D877F "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-DB1D877F") | The maximum number of GetObject requests that you can make per second, when you use standard upload availability. Additional requests are throttled.                                               |
| Rate of GetObject API requests for streaming upload availability                                           | Each supported Region: 25           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-FA6DBE33 "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-FA6DBE33") | The maximum number of GetObject requests that you can make per second, when you use streaming upload availability. Additional requests are throttled.                                              |
| Rate of ListItems API requests                                                                             | Each supported Region: 5            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-97AEAA6B "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-97AEAA6B") | The maximum number of ListItems requests that you can make per second. Additional requests are throttled.                                                                                          |
| Rate of PutObject API requests for chunked transfer encoding (also known as streaming upload availability) | Each supported Region: 10           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-CAF2EF73 "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-CAF2EF73") | The maximum number of PutObject requests that you can make per second with chunked transfer encoding of the body (also known as streaming upload availability). Additional requests are throttled. |
| Rate of PutObject API requests for standard upload availability                                            | Each supported Region: 100          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-CA39FABB "https://console.aws.amazon.com/servicequotas/home/services/mediastore/quotas/L-CA39FABB") | The maximum number of PutObject requests that you can make per second, when you use standard upload availability. Additional requests are throttled.                                               |

For more information, see [Quotas](../../../mediastore/latest/ug/limits.md "../../../mediastore/latest/ug/limits.md") in the
_AWS Elemental MediaStore User Guide_.
