# Amazon Managed Grafana endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                                               | Protocol       |
| ------------------------ | -------------- | ---------------------------------------------------------------------- | -------------- |
| US East (Ohio)           | us-east-2      | grafana.us-east-2.amazonaws.com<br>grafana.us-east-2.api.aws           | HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | grafana.us-east-1.amazonaws.com<br>grafana.us-east-1.api.aws           | HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | grafana.us-west-2.amazonaws.com<br>grafana.us-west-2.api.aws           | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)     | ap-northeast-2 | grafana.ap-northeast-2.amazonaws.com<br>grafana.ap-northeast-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 | grafana.ap-southeast-1.amazonaws.com<br>grafana.ap-southeast-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Sydney)    | ap-southeast-2 | grafana.ap-southeast-2.amazonaws.com<br>grafana.ap-southeast-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)     | ap-northeast-1 | grafana.ap-northeast-1.amazonaws.com<br>grafana.ap-northeast-1.api.aws | HTTPS<br>HTTPS |
| Europe (Frankfurt)       | eu-central-1   | grafana.eu-central-1.amazonaws.com<br>grafana.eu-central-1.api.aws     | HTTPS<br>HTTPS |
| Europe (Ireland)         | eu-west-1      | grafana.eu-west-1.amazonaws.com<br>grafana.eu-west-1.api.aws           | HTTPS<br>HTTPS |
| Europe (London)          | eu-west-2      | grafana.eu-west-2.amazonaws.com<br>grafana.eu-west-2.api.aws           | HTTPS<br>HTTPS |

## Service quotas

Amazon Managed Grafana has the following quotas.

| Name                                             | Default                              | Adjustable                                                                                                                                                                         | Description                                                                                                                          |
| ------------------------------------------------ | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Number of workspaces                             | Each supported Region: 5             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/grafana/quotas/L-2C2D5119 "https://console.aws.amazon.com/servicequotas/home/services/grafana/quotas/L-2C2D5119") | The maximum number of workspaces that you can have in this account in the current region.                                            |
| Rate of AssociateLicense requests                | Each supported Region: 1 per second  | No                                                                                                                                                                                 | The maximum number of AssociateLicense requests that you can make, per second, in this account in the current region.                |
| Rate of CreateWorkspace requests                 | Each supported Region: 1 per second  | No                                                                                                                                                                                 | The maximum number of CreateWorkspace requests that you can make, per second, in this account in the current region.                 |
| Rate of DeleteWorkspace requests                 | Each supported Region: 1 per second  | No                                                                                                                                                                                 | The maximum number of DeleteWorkspace requests that you can make, per second, in this account in the current region.                 |
| Rate of DescribeWorkspace requests               | Each supported Region: 5 per second  | No                                                                                                                                                                                 | The maximum number of DescribeWorkspace requests that you can make, per second, in this account in the current region.               |
| Rate of DescribeWorkspaceAuthentication requests | Each supported Region: 1 per second  | No                                                                                                                                                                                 | The maximum number of DescribeWorkspaceAuthentication requests that you can make, per second, in this account in the current region. |
| Rate of DisassociateLicense requests             | Each supported Region: 1 per second  | No                                                                                                                                                                                 | The maximum number of DisassociateLicense requests that you can make, per second, in this account in the current region.             |
| Rate of ListPermissions requests                 | Each supported Region: 10 per second | No                                                                                                                                                                                 | The maximum number of ListPermissions requests that you can make, per second, in this account in the current region.                 |
| Rate of ListWorkspaces requests                  | Each supported Region: 5 per second  | No                                                                                                                                                                                 | The maximum number of ListWorkspaces requests that you can make, per second, in this account in the current region.                  |
| Rate of UpdatePermissions requests               | Each supported Region: 10 per second | No                                                                                                                                                                                 | The maximum number of UpdatePermissions requests that you can make, per second, in this account in the current region.               |
| Rate of UpdateWorkspace requests                 | Each supported Region: 10 per second | No                                                                                                                                                                                 | The maximum number of UpdateWorkspace requests that you can make, per second, in this account in the current region.                 |
| Rate of UpdateWorkspaceAuthentication requests   | Each supported Region: 1 per second  | No                                                                                                                                                                                 | The maximum number of UpdateWorkspaceAuthentication requests that you can make, per second, in this account in the current region.   |

Additionally, Amazon Managed Grafana has the following quotas within each workspace

| Resource                                                                                                                               | Adjustable | Default Quota                                     |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------- |
| Alerts<br>The number of rules per workspace in classic alerting, or the number<br>of rule instances per workspace in Grafana alerting. | No         | 100 per workspace.                                |
| Alert evaluation timeout                                                                                                               | No         | 30 seconds.                                       |
| Dashboards                                                                                                                             | No         | 2,000 per workspace.                              |
| Data sources                                                                                                                           | No         | 2,000 per workspace.                              |
| Data source timeout                                                                                                                    | No         | 60 seconds.                                       |
| Users                                                                                                                                  | No         | 10,000 provisioned, 500 concurrent per workspace. |
| API keys                                                                                                                               | No         | 100 per workspace.                                |
| Service accounts                                                                                                                       | No         | 100 per workspace.                                |
| Service account tokens<br>Active tokens and expired tokens count toward this<br>quota. Delete tokens to remove them from the quota.    | No         | 100 per workspace.                                |
| Network access control: Prefix lists                                                                                                   | No         | 5 per workspace.                                  |
| Network access control: IP address ranges                                                                                              | No         | 100 per prefix list.                              |
| Network access control: VPC endpoints                                                                                                  | No         | 5 per workspace.                                  |
