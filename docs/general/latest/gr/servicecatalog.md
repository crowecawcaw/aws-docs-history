# AWS Service Catalog endpoints and quotas

The following are the service endpoints and service quotas for this
service. To connect programmatically to an AWS service, you use an endpoint. In addition to
the standard AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. For
more information, see [Amazon
service endpoints.](rande.md "rande.md") Service quotas, also referred to as limits, are the maximum
number of service resources or operations for your AWS account. For more information, see
[Amazon
service quotas.](aws_service_limits.md "aws_service_limits.md")

## Service endpoints

| Region Name               | Region         | Endpoint                                                                                      | Protocol       |
| ------------------------- | -------------- | --------------------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)            | us-east-2      | servicecatalog.us-east-2.amazonaws.com<br>servicecatalog-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | servicecatalog.us-east-1.amazonaws.com<br>servicecatalog-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | servicecatalog.us-west-1.amazonaws.com<br>servicecatalog-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | servicecatalog.us-west-2.amazonaws.com<br>servicecatalog-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | servicecatalog.af-south-1.amazonaws.com                                                       | HTTPS          |
| Asia Pacific (Hong Kong)  | ap-east-1      | servicecatalog.ap-east-1.amazonaws.com                                                        | HTTPS          |
| Asia Pacific (Hyderabad)  | ap-south-2     | servicecatalog.ap-south-2.amazonaws.com                                                       | HTTPS          |
| Asia Pacific (Jakarta)    | ap-southeast-3 | servicecatalog.ap-southeast-3.amazonaws.com                                                   | HTTPS          |
| Asia Pacific (Melbourne)  | ap-southeast-4 | servicecatalog.ap-southeast-4.amazonaws.com                                                   | HTTPS          |
| Asia Pacific (Mumbai)     | ap-south-1     | servicecatalog.ap-south-1.amazonaws.com                                                       | HTTPS          |
| Asia Pacific (Osaka)      | ap-northeast-3 | servicecatalog.ap-northeast-3.amazonaws.com                                                   | HTTPS          |
| Asia Pacific (Seoul)      | ap-northeast-2 | servicecatalog.ap-northeast-2.amazonaws.com                                                   | HTTPS          |
| Asia Pacific (Singapore)  | ap-southeast-1 | servicecatalog.ap-southeast-1.amazonaws.com                                                   | HTTPS          |
| Asia Pacific (Sydney)     | ap-southeast-2 | servicecatalog.ap-southeast-2.amazonaws.com                                                   | HTTPS          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | servicecatalog.ap-northeast-1.amazonaws.com                                                   | HTTPS          |
| Canada (Central)          | ca-central-1   | servicecatalog.ca-central-1.amazonaws.com                                                     | HTTPS          |
| Europe (Frankfurt)        | eu-central-1   | servicecatalog.eu-central-1.amazonaws.com                                                     | HTTPS          |
| Europe (Ireland)          | eu-west-1      | servicecatalog.eu-west-1.amazonaws.com                                                        | HTTPS          |
| Europe (London)           | eu-west-2      | servicecatalog.eu-west-2.amazonaws.com                                                        | HTTPS          |
| Europe (Milan)            | eu-south-1     | servicecatalog.eu-south-1.amazonaws.com                                                       | HTTPS          |
| Europe (Paris)            | eu-west-3      | servicecatalog.eu-west-3.amazonaws.com                                                        | HTTPS          |
| Europe (Spain)            | eu-south-2     | servicecatalog.eu-south-2.amazonaws.com                                                       | HTTPS          |
| Europe (Stockholm)        | eu-north-1     | servicecatalog.eu-north-1.amazonaws.com                                                       | HTTPS          |
| Europe (Zurich)           | eu-central-2   | servicecatalog.eu-central-2.amazonaws.com                                                     | HTTPS          |
| Israel (Tel Aviv)         | il-central-1   | servicecatalog.il-central-1.amazonaws.com                                                     | HTTPS          |
| Middle East (Bahrain)     | me-south-1     | servicecatalog.me-south-1.amazonaws.com                                                       | HTTPS          |
| Middle East (UAE)         | me-central-1   | servicecatalog.me-central-1.amazonaws.com                                                     | HTTPS          |
| South America (São Paulo) | sa-east-1      | servicecatalog.sa-east-1.amazonaws.com                                                        | HTTPS          |
| AWS GovCloud (US-East)    | us-gov-east-1  | servicecatalog.us-gov-east-1.amazonaws.com<br>servicecatalog-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | servicecatalog.us-gov-west-1.amazonaws.com<br>servicecatalog-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                                  | Default                      | Adjustable                                                                                                                                                                                       | Description                                                                                |
| ----------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Applications per attribute group                      | Each supported Region: 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-223F4C54 "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-223F4C54") | The maximum number of applications per attribute group                                     |
| Applications per region                               | Each supported Region: 2,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-7C3CEC2B "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-7C3CEC2B") | The maximum number of applications you can create per region                               |
| Attribute groups per application                      | Each supported Region: 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-C533FF9A "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-C533FF9A") | The maximum number of attribute groups per application                                     |
| Attribute groups per region                           | Each supported Region: 2,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-1639038A "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-1639038A") | The maximum number of attribute groups you can create per region                           |
| Delegated administrators per organization             | Each supported Region: 50    | No                                                                                                                                                                                               | The maximum number of delegated administrators you can register per organization           |
| Portfolios per region                                 | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-C6458716 "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-C6458716") | The maximum number of portfolios you can create per region                                 |
| Product versions per product                          | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-A5846085 "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-A5846085") | The maximum number of product versions you can create per product                          |
| Products per portfolio                                | Each supported Region: 150   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-AB79E48B "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-AB79E48B") | The maximum number of products you can create per portfolio                                |
| Products per region                                   | Each supported Region: 350   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-764CF6A1 "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-764CF6A1") | The maximum number of products you can create per region                                   |
| Resources per application                             | Each supported Region: 1,000 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-360CDF2E "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-360CDF2E") | The maximum number of resources per applications                                           |
| Service action associations per provisioning artifact | Each supported Region: 25    | No                                                                                                                                                                                               | The maximum number of service action associations you can create per provisioning artifact |
| Service actions per region                            | Each supported Region: 200   | No                                                                                                                                                                                               | The maximum number of service actions you can create per region                            |
| Shared accounts per portfolio                         | Each supported Region: 5,000 | No                                                                                                                                                                                               | The maximum number of shared accounts per portfolio                                        |
| TagOptions per resource                               | Each supported Region: 25    | No                                                                                                                                                                                               | The maximum number of TagOptions you can associate with a resource                         |
| Tags per portfolio                                    | Each supported Region: 20    | No                                                                                                                                                                                               | The maximum number of tags you can create per portfolio                                    |
| Tags per product                                      | Each supported Region: 20    | No                                                                                                                                                                                               | The maximum number of tags you can create per product                                      |
| Tags per provisioned product                          | Each supported Region: 50    | No                                                                                                                                                                                               | The maximum number of tags you can create per provisioned product                          |
| Users, groups, and roles per portfolio                | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-E8959660 "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-E8959660") | The maximum number of users, groups, and roles you can create per portfolio                |
| Users, groups, and roles per product                  | Each supported Region: 200   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-3BC91705 "https://console.aws.amazon.com/servicequotas/home/services/servicecatalog/quotas/L-3BC91705") | The maximum number of users, groups, and roles you can create per portfolio                |
| Values per TagOption                                  | Each supported Region: 25    | No                                                                                                                                                                                               | The maximum number of different values for each TagOption                                  |

For more information, see [Service Catalog default service quotas](../../../servicecatalog/latest/adminguide/limits.md "../../../servicecatalog/latest/adminguide/limits.md")
in the _Service Catalog Administrator Guide_.
