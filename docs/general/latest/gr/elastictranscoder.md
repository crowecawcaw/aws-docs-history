# Amazon Elastic Transcoder endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                       | Protocol |
| ------------------------ | -------------- | ---------------------------------------------- | -------- |
| US East (N. Virginia)    | us-east-1      | elastictranscoder.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)  | us-west-1      | elastictranscoder.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | elastictranscoder.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Mumbai)    | ap-south-1     | elastictranscoder.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | elastictranscoder.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | elastictranscoder.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | elastictranscoder.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Ireland)         | eu-west-1      | elastictranscoder.eu-west-1.amazonaws.com      | HTTPS    |

## Service quotas

| Name                              | Default                                                                                    | Adjustable                                                                                                                                                                                             | Description                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Burst size of Create Job requests | Each supported Region: 100                                                                 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-25A79362 "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-25A79362") | The maximum number of Create Job requests that you can send in one burst in this account in the current region. |
| Burst size of Read Job requests   | Each supported Region: 50                                                                  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-73E60F57 "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-73E60F57") | The maximum number of Read Job requests that you can send in one burst in this account in the current region.   |
| Concurrent jobs per pipeline      | us-east-1: 20<br>us-west-2: 20<br>eu-west-1: 20<br>Each of the other supported Regions: 12 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-EAE6F7FC "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-EAE6F7FC") | The maximum number of jobs processed simultaneously by each pipeline in the current region.                     |
| Pipelines                         | Each supported Region: 4                                                                   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-B6FAEE7E "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-B6FAEE7E") | The maximum number of pipelines that you can create in this account in the current region.                      |
| Queued jobs per pipeline          | Each supported Region: 1,000,000                                                           | No                                                                                                                                                                                                     | The maximum number of queued jobs per pipeline in the current region.                                           |
| Rate of Create Job requests       | Each supported Region: 2                                                                   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-0BDCC49D "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-0BDCC49D") | The maximum number of Create Job requests per second that you can send in this account in the current region    |
| Rate of Read Job requests         | Each supported Region: 4                                                                   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-301A2D88 "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-301A2D88") | The maximum number of Read Job requests per second that you can send in this account in the current region.     |
| User-defined presets              | Each supported Region: 50                                                                  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-EAB82560 "https://console.aws.amazon.com/servicequotas/home/services/elastictranscoder/quotas/L-EAB82560") | The maximum number of custom output presets that you can create in this account in the current region.          |

For more information, see [Amazon Elastic Transcoder](../../../elastictranscoder/latest/developerguide/limits.md "../../../elastictranscoder/latest/developerguide/limits.md") quotas
in the _Amazon Elastic Transcoder Developer Guide_.
