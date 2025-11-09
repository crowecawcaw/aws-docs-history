# Amazon Translate endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                                                                                                                                       | Protocol                         |
| ------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)           | us-east-2      | translate.us-east-2.amazonaws.com<br>translate.us-east-2.api.aws<br>translate-fips.us-east-2.api.aws<br>translate-fips.us-east-2.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | translate.us-east-1.amazonaws.com<br>translate-fips.us-east-1.amazonaws.com<br>translate-fips.us-east-1.api.aws<br>translate.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)  | us-west-1      | translate.us-west-1.amazonaws.com<br>translate-fips.us-west-1.api.aws<br>translate.us-west-1.api.aws<br>translate-fips.us-west-1.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | translate.us-west-2.amazonaws.com<br>translate-fips.us-west-2.amazonaws.com<br>translate.us-west-2.api.aws<br>translate-fips.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Hong Kong) | ap-east-1      | translate.ap-east-1.amazonaws.com<br>translate.ap-east-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)    | ap-south-1     | translate.ap-south-1.amazonaws.com<br>translate.ap-south-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)     | ap-northeast-2 | translate.ap-northeast-2.amazonaws.com<br>translate.ap-northeast-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore) | ap-southeast-1 | translate.ap-southeast-1.amazonaws.com<br>translate.ap-southeast-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)    | ap-southeast-2 | translate.ap-southeast-2.amazonaws.com<br>translate.ap-southeast-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)     | ap-northeast-1 | translate.ap-northeast-1.amazonaws.com<br>translate.ap-northeast-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Canada (Central)         | ca-central-1   | translate.ca-central-1.amazonaws.com<br>translate.ca-central-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)       | eu-central-1   | translate.eu-central-1.amazonaws.com<br>translate.eu-central-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Europe (Ireland)         | eu-west-1      | translate.eu-west-1.amazonaws.com<br>translate.eu-west-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (London)          | eu-west-2      | translate.eu-west-2.amazonaws.com<br>translate.eu-west-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Paris)           | eu-west-3      | translate.eu-west-3.amazonaws.com<br>translate.eu-west-3.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Stockholm)       | eu-north-1     | translate.eu-north-1.amazonaws.com<br>translate.eu-north-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)   | us-gov-west-1  | translate.us-gov-west-1.amazonaws.com<br>translate-fips.us-gov-west-1.api.aws<br>translate.us-gov-west-1.api.aws<br>translate-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Name                              | Default                      | Adjustable                                                                                                                                                                             | Description                                                                                         |
| --------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Concurrent batch translation jobs | Each supported Region: 10    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/translate/quotas/L-10DB0BCF "https://console.aws.amazon.com/servicequotas/home/services/translate/quotas/L-10DB0BCF") | The maximum number of concurrent batch translation jobs in this account in the current Region.      |
| Custom terminology files          | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/translate/quotas/L-4011ABD8 "https://console.aws.amazon.com/servicequotas/home/services/translate/quotas/L-4011ABD8") | The maximum number of custom terminology files you can store in this account in the current Region. |
| Parallel data resources           | Each supported Region: 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/translate/quotas/L-2B2DC880 "https://console.aws.amazon.com/servicequotas/home/services/translate/quotas/L-2B2DC880") | The maximum number of parallel data resources in this account in the current Region.                |

For more information, see [Guidelines
and Quotas](../../../translate/latest/dg/what-is-limits.md "../../../translate/latest/dg/what-is-limits.md") in the _Amazon Translate Developer Guide_.
