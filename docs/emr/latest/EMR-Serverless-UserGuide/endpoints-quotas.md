# Endpoints and quotas for

EMR Serverless

## Service endpoints

To connect programmatically to an AWS service, you use an
_endpoint_. An endpoint is the URL of the entry point for an
AWS web service. In addition to the standard AWS endpoints, some AWS services
offer FIPS endpoints in selected Regions. The following table lists the
service endpoints for EMR Serverless. For more information, refer to [AWS service
endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

| EMR Serverless service endpoints | Region name                                                                                                                     | Region                                                                                    | Endpoint | Protocol |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------- | -------- |
| US East (Ohio)                   | `us-east-2` (limited to the following Availability Zones:<br>`use2-az1`, `use2-az2`, and<br>`use2-az3`)                         | `emr-serverless.us-east-2.amazonaws.com`                                                  | HTTPS    |
| US East (N. Virginia)            | `us-east-1` (limited to the following Availability Zones:<br>`use1-az1`, `use1-az2`, `use1-az4`,<br>`use1-az5`, and `use1-az6`) | `emr-serverless.us-east-1.amazonaws.com`<br>`emr-serverless-fips.us-east-1.amazonaws.com` | HTTPS    |
| US West (N. California)          | `us-west-1`                                                                                                                     | `emr-serverless.us-west-1.amazonaws.com`                                                  | HTTPS    |
| US West (Oregon)                 | `us-west-2`                                                                                                                     | `emr-serverless.us-west-2.amazonaws.com`<br>`emr-serverless-fips.us-west-2.amazonaws.com` | HTTPS    |
| Africa (Cape Town)               | `af-south-1`                                                                                                                    | `emr-serverless.af-south-1.amazonaws.com`                                                 | HTTPS    |
| Asia Pacific (Hong Kong)         | `ap-east-1`                                                                                                                     | `emr-serverless.ap-east-1.amazonaws.com`                                                  | HTTPS    |
| Asia Pacific (Jakarta)           | `ap-southeast-3`                                                                                                                | `emr-serverless.ap-southeast-3.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Melbourne)         | `ap-southeast-4`                                                                                                                | `emr-serverless.ap-southeast-4.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Malaysia)          | `ap-southeast-5`                                                                                                                | `emr-serverless.ap-southeast-5.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Mumbai)            | `ap-south-1`                                                                                                                    | `emr-serverless.ap-south-1.amazonaws.com`                                                 | HTTPS    |
| Asia Pacific (Osaka)             | `ap-northeast-3`                                                                                                                | `emr-serverless.ap-northeast-3.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Seoul)             | `ap-northeast-2`                                                                                                                | `emr-serverless.ap-northeast-2.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Singapore)         | `ap-southeast-1`                                                                                                                | `emr-serverless.ap-southeast-1.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Sydney)            | `ap-southeast-2`                                                                                                                | `emr-serverless.ap-southeast-2.amazonaws.com`                                             | HTTPS    |
| Asia Pacific (Tokyo)             | `ap-northeast-1`                                                                                                                | `emr-serverless.ap-northeast-1.amazonaws.com`                                             | HTTPS    |
| Canada (Central)                 | `ca-central-1` (limited to the following Availability<br>Zones: `cac1-az1` and `cac1-az2`)                                      | `emr-serverless.ca-central-1.amazonaws.com`                                               | HTTPS    |
| Canada West (Calgary)            | `ca-west-1`                                                                                                                     | `emr-serverless.ca-west-1.amazonaws.com`                                                  | HTTPS    |
| Europe (Frankfurt)               | `eu-central-1`                                                                                                                  | `emr-serverless.eu-central-1.amazonaws.com`                                               | HTTPS    |
| Europe (Zurich)                  | `eu-central-2`                                                                                                                  | `emr-serverless.eu-central-2.amazonaws.com`                                               | HTTPS    |
| Europe (Ireland)                 | `eu-west-1`                                                                                                                     | `emr-serverless.eu-west-1.amazonaws.com`                                                  | HTTPS    |
| Europe (London)                  | `eu-west-2`                                                                                                                     | `emr-serverless.eu-west-2.amazonaws.com`                                                  | HTTPS    |
| Europe (Milan)                   | `eu-south-1`                                                                                                                    | `emr-serverless.eu-south-1.amazonaws.com`                                                 | HTTPS    |
| Europe (Paris)                   | `eu-west-3`                                                                                                                     | `emr-serverless.eu-west-3.amazonaws.com`                                                  | HTTPS    |
| Europe (Spain)                   | `eu-south-2`                                                                                                                    | `emr-serverless.eu-south-2.amazonaws.com`                                                 | HTTPS    |
| Europe (Stockholm)               | `eu-north-1`                                                                                                                    | `emr-serverless.eu-north-1.amazonaws.com`                                                 | HTTPS    |
| Israel (Tel Aviv)                | `il-central-1`                                                                                                                  | `emr-serverless.il-central-1.amazonaws.com`                                               | HTTPS    |
| Middle East (Bahrain)            | `me-south-1`                                                                                                                    | `emr-serverless.me-south-1.amazonaws.com`                                                 | HTTPS    |
| Middle East (UAE)                | `me-central-1`                                                                                                                  | `emr-serverless.me-central-1.amazonaws.com`                                               | HTTPS    |
| South America (São Paulo)        | `sa-east-1`                                                                                                                     | `emr-serverless.sa-east-1.amazonaws.com`                                                  | HTTPS    |
| China (Beijing)                  | `cn-north-1` (limited to the following Availability Zones:<br>`cnn1-az1`, `cnn1-az2`)                                           | `emr-serverless.cn-north-1.amazonaws.com.cn`                                              | HTTPS    |
| AWS GovCloud (US-East)           | `us-gov-east-1`                                                                                                                 | `emr-serverless.us-gov-east-1.amazonaws.com`                                              | HTTPS    |
| AWS GovCloud (US-West)           | `us-gov-west-1`                                                                                                                 | `emr-serverless.us-gov-west-1.amazonaws.com`                                              | HTTPS    |

## Service quotas

_Service quotas_, also known as _limits_, are
the maximum number of service resources or operations that your AWS account can use. EMR Serverless collects service quota usage metrics every minute and publishes them in the `AWS/Usage` namespace.

###### Note

New AWS accounts have initial lower quotas that can increase over time.
Amazon EMR Serverless monitors account usage within each AWS Region, and then
automatically increases the quotas based on your usage.

The following table lists the service quotas for EMR Serverless. For more information,
refer to [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

| Name                             | Default limit | Adjustable? | Description                                                                                         |
| -------------------------------- | ------------- | ----------- | --------------------------------------------------------------------------------------------------- |
| Max concurrent vCPUs per account | 16            | Yes         | The maximum number of vCPUs that can concurrently run for the account<br>in the current AWS Region. |
| Max Queued Jobs Per Account      | 2000          | Yes         | The maximum number of queued jobs for the account in the current AWS Region.                        |

## API limits

The following describes the API limits per Region for your AWS account.

| Resource                                                                                                                                                                     | Default quota                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [ListApplications](../../../emr-serverless/latest/APIReference/API_ListApplications.md "../../../emr-serverless/latest/APIReference/API_ListApplications.md")                | 10 transactions per second. Burst of 50 transactions per second. |
| [CreateApplication](../../../emr-serverless/latest/APIReference/API_CreateApplication.md "../../../emr-serverless/latest/APIReference/API_CreateApplication.md")             | 1 transaction per second. Burst of 25 transactions per second.   |
| [DeleteApplication](../../../emr-serverless/latest/APIReference/API_DeleteApplication.md "../../../emr-serverless/latest/APIReference/API_DeleteApplication.md")             | 1 transaction per second. Burst of 25 transactions per second.   |
| [GetApplication](../../../emr-serverless/latest/APIReference/API_GetApplication.md "../../../emr-serverless/latest/APIReference/API_GetApplication.md")                      | 10 transactions per second. Burst of 50 transactions per second. |
| [UpdateApplication](../../../emr-serverless/latest/APIReference/API_UpdateApplication.md "../../../emr-serverless/latest/APIReference/API_UpdateApplication.md")             | 1 transaction per second. Burst of 25 transactions per second.   |
| [ListJobRuns](../../../emr-serverless/latest/APIReference/API_ListJobRuns.md "../../../emr-serverless/latest/APIReference/API_ListJobRuns.md")                               | 1 transaction per second. Burst of 25 transactions per second.   |
| [StartJobRun](../../../emr-serverless/latest/APIReference/API_StartJobRun.md "../../../emr-serverless/latest/APIReference/API_StartJobRun.md")                               | 1 transaction per second. Burst of 25 transactions per second.   |
| [GetDashboardForJobRun](../../../emr-serverless/latest/APIReference/API_GetDashboardForJobRun.md "../../../emr-serverless/latest/APIReference/API_GetDashboardForJobRun.md") | 1 transaction per second. Burst of 2 transactions per second.    |
| [CancelJobRun](../../../emr-serverless/latest/APIReference/API_CancelJobRun.md "../../../emr-serverless/latest/APIReference/API_CancelJobRun.md")                            | 1 transaction per second. Burst of 25 transactions per second.   |
| [GetJobRun](../../../emr-serverless/latest/APIReference/API_GetJobRun.md "../../../emr-serverless/latest/APIReference/API_GetJobRun.md")                                     | 10 transactions per second. Burst of 50 transactions per second. |
| [StartApplication](../../../emr-serverless/latest/APIReference/API_StartApplication.md "../../../emr-serverless/latest/APIReference/API_StartApplication.md")                | 1 transaction per second. Burst of 25 transactions per second.   |
| [StopApplication](../../../emr-serverless/latest/APIReference/API_StopApplication.md "../../../emr-serverless/latest/APIReference/API_StopApplication.md")                   | 1 transaction per second. Burst of 25 transactions per second.   |
