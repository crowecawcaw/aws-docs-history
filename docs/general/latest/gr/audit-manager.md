# AWS Audit Manager endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                                                                                                 | Protocol                |
| ------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| US East (Ohio)           | us-east-2      | auditmanager.us-east-2.amazonaws.com<br>auditmanager-fips.us-east-2.api.aws<br>auditmanager-fips.us-east-2.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | auditmanager.us-east-1.amazonaws.com<br>auditmanager-fips.us-east-1.api.aws<br>auditmanager-fips.us-east-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)  | us-west-1      | auditmanager.us-west-1.amazonaws.com<br>auditmanager-fips.us-west-1.api.aws<br>auditmanager-fips.us-west-1.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | auditmanager.us-west-2.amazonaws.com<br>auditmanager-fips.us-west-2.api.aws<br>auditmanager-fips.us-west-2.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | auditmanager.ap-south-1.amazonaws.com                                                                                    | HTTPS                   |
| Asia Pacific (Singapore) | ap-southeast-1 | auditmanager.ap-southeast-1.amazonaws.com                                                                                | HTTPS                   |
| Asia Pacific (Sydney)    | ap-southeast-2 | auditmanager.ap-southeast-2.amazonaws.com                                                                                | HTTPS                   |
| Asia Pacific (Tokyo)     | ap-northeast-1 | auditmanager.ap-northeast-1.amazonaws.com                                                                                | HTTPS                   |
| Canada (Central)         | ca-central-1   | auditmanager.ca-central-1.amazonaws.com                                                                                  | HTTPS                   |
| Europe (Frankfurt)       | eu-central-1   | auditmanager.eu-central-1.amazonaws.com                                                                                  | HTTPS                   |
| Europe (Ireland)         | eu-west-1      | auditmanager.eu-west-1.amazonaws.com                                                                                     | HTTPS                   |
| Europe (London)          | eu-west-2      | auditmanager.eu-west-2.amazonaws.com                                                                                     | HTTPS                   |

## Service quotas

| Name                                     | Default                      | Adjustable                                                                                                                                                                                   | Description                                                               |
| ---------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Accounts in scope across all assessments | Each supported Region: 250   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-BEA222D4 "https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-BEA222D4") | The maximum number of accounts in scope across all assessments per region |
| Controls per framework                   | Each supported Region: 1,400 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-724DD74D "https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-724DD74D") | The maximum number of controls per framework per account per region       |
| Custom controls                          | Each supported Region: 500   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-0255B75F "https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-0255B75F") | The maximum number of custom controls per account per region              |
| Custom frameworks                        | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-8935A6F1 "https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-8935A6F1") | The maximum number of custom frameworks per account per region            |
| Running assessments                      | Each supported Region: 100   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-92B50F18 "https://console.aws.amazon.com/servicequotas/home/services/auditmanager/quotas/L-92B50F18") | The maximum number of running assessments per account per region          |
