# AWS Systems Manager for SAP endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name               | Region         | Endpoint                                                                                                                                           | Protocol                         |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)            | us-east-2      | ssm-sap.us-east-2.amazonaws.com<br>ssm-sap-fips.us-east-2.api.aws<br>ssm-sap-fips.us-east-2.amazonaws.com<br>ssm-sap.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | ssm-sap.us-east-1.amazonaws.com<br>ssm-sap-fips.us-east-1.api.aws<br>ssm-sap-fips.us-east-1.amazonaws.com<br>ssm-sap.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | ssm-sap.us-west-1.amazonaws.com<br>ssm-sap-fips.us-west-1.api.aws<br>ssm-sap-fips.us-west-1.amazonaws.com<br>ssm-sap.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | ssm-sap.us-west-2.amazonaws.com<br>ssm-sap-fips.us-west-2.api.aws<br>ssm-sap-fips.us-west-2.amazonaws.com<br>ssm-sap.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | ssm-sap.af-south-1.amazonaws.com<br>ssm-sap.af-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)  | ap-east-1      | ssm-sap.ap-east-1.amazonaws.com<br>ssm-sap.ap-east-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)  | ap-south-2     | ssm-sap.ap-south-2.amazonaws.com<br>ssm-sap.ap-south-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)    | ap-southeast-3 | ssm-sap.ap-southeast-3.amazonaws.com<br>ssm-sap.ap-southeast-3.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)  | ap-southeast-4 | ssm-sap.ap-southeast-4.amazonaws.com<br>ssm-sap.ap-southeast-4.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)     | ap-south-1     | ssm-sap.ap-south-1.amazonaws.com<br>ssm-sap.ap-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)      | ap-northeast-3 | ssm-sap.ap-northeast-3.amazonaws.com<br>ssm-sap.ap-northeast-3.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)      | ap-northeast-2 | ssm-sap.ap-northeast-2.amazonaws.com<br>ssm-sap.ap-northeast-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)  | ap-southeast-1 | ssm-sap.ap-southeast-1.amazonaws.com<br>ssm-sap.ap-southeast-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)     | ap-southeast-2 | ssm-sap.ap-southeast-2.amazonaws.com<br>ssm-sap.ap-southeast-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)      | ap-northeast-1 | ssm-sap.ap-northeast-1.amazonaws.com<br>ssm-sap.ap-northeast-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Canada (Central)          | ca-central-1   | ssm-sap.ca-central-1.amazonaws.com<br>ssm-sap-fips.ca-central-1.api.aws<br>ssm-sap-fips.ca-central-1.amazonaws.com<br>ssm-sap.ca-central-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | ssm-sap.eu-central-1.amazonaws.com<br>ssm-sap.eu-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Ireland)          | eu-west-1      | ssm-sap.eu-west-1.amazonaws.com<br>ssm-sap.eu-west-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (London)           | eu-west-2      | ssm-sap.eu-west-2.amazonaws.com<br>ssm-sap.eu-west-2.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Milan)            | eu-south-1     | ssm-sap.eu-south-1.amazonaws.com<br>ssm-sap.eu-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Paris)            | eu-west-3      | ssm-sap.eu-west-3.amazonaws.com<br>ssm-sap.eu-west-3.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Spain)            | eu-south-2     | ssm-sap.eu-south-2.amazonaws.com<br>ssm-sap.eu-south-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Stockholm)        | eu-north-1     | ssm-sap.eu-north-1.amazonaws.com<br>ssm-sap.eu-north-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Zurich)           | eu-central-2   | ssm-sap.eu-central-2.amazonaws.com<br>ssm-sap.eu-central-2.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)         | il-central-1   | ssm-sap.il-central-1.amazonaws.com<br>ssm-sap.il-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)     | me-south-1     | ssm-sap.me-south-1.amazonaws.com<br>ssm-sap.me-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Middle East (UAE)         | me-central-1   | ssm-sap.me-central-1.amazonaws.com<br>ssm-sap.me-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| South America (São Paulo) | sa-east-1      | ssm-sap.sa-east-1.amazonaws.com<br>ssm-sap.sa-east-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |

## Service quotas

| Name                                          | Default | Adjustable | Description                                                                                                                          |
| --------------------------------------------- | ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| SAP applications per Region in an AWS account | 10      | Yes        | The maximum number of SAP applications that you can register with<br>AWS Systems Manager for SAP per Region in an AWS account.       |
| Components per SAP application                | 20      | Yes        | The maximum number of `ssm-sap` components that you can<br>register per SAP application registered with AWS Systems Manager for SAP. |
| Databases per component                       | 20      | Yes        | The maximum number of `ssm-sap` databases that you can<br>register per `ssm-sap` component.                                          |
