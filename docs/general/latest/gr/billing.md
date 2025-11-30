# AWS Billing and Cost Management endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

AWS Billing and Cost Management includes the AWS Cost Explorer API, the AWS Cost and Usage Reports API, the
AWS Budgets API, and the AWS Price List API.

## Service endpoints

### AWS Cost Explorer

| Region Name           | Region    | Endpoint                                           | Protocol       |
| --------------------- | --------- | -------------------------------------------------- | -------------- |
| US East (N. Virginia) | us-east-1 | ce.us-east-1.amazonaws.com<br>ce.us-east-1.api.aws | HTTPS<br>HTTPS |

### AWS Cost and Usage Reports

| Region Name | Region | Endpoint | Protocol |
| ----------- | ------ | -------- | -------- |

### AWS Budgets

| Region Name               | Region         | Endpoint                                           | Protocol       |
| ------------------------- | -------------- | -------------------------------------------------- | -------------- |
| US East (Ohio)            | us-east-2      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)     | ap-south-1     | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)      | ap-northeast-2 | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Singapore)  | ap-southeast-1 | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Sydney)     | ap-southeast-2 | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)      | ap-northeast-1 | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Canada (Central)          | ca-central-1   | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Europe (Ireland)          | eu-west-1      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Europe (London)           | eu-west-2      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| Europe (Paris)            | eu-west-3      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |
| South America (São Paulo) | sa-east-1      | budgets.amazonaws.com<br>budgets.us-east-1.api.aws | HTTPS<br>HTTPS |

### AWS Cost Optimization Hub

| Region Name           | Region    | Endpoint                                                                                 | Protocol       |
| --------------------- | --------- | ---------------------------------------------------------------------------------------- | -------------- |
| US East (N. Virginia) | us-east-1 | cost-optimization-hub.us-east-1.amazonaws.com<br>cost-optimization-hub.us-east-1.api.aws | HTTPS<br>HTTPS |

### AWS Data Exports

| Region Name           | Region    | Endpoint                           | Protocol |
| --------------------- | --------- | ---------------------------------- | -------- |
| US East (N. Virginia) | us-east-1 | bcm-data-exports.us-east-1.api.aws |          |

### AWS Free Tier

| Region Name           | Region    | Endpoint                   | Protocol |
| --------------------- | --------- | -------------------------- | -------- |
| US East (N. Virginia) | us-east-1 | freetier.us-east-1.api.aws |          |

### AWS Price List Service

| Region Name           | Region       | Endpoint                               | Protocol |
| --------------------- | ------------ | -------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1    | api.pricing.us-east-1.amazonaws.com    | HTTPS    |
| Asia Pacific (Mumbai) | ap-south-1   | api.pricing.ap-south-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)    | eu-central-1 | api.pricing.eu-central-1.amazonaws.com | HTTPS    |

### Savings Plans

| Region Name               | Region         | Endpoint                   | Protocol |
| ------------------------- | -------------- | -------------------------- | -------- |
| US East (Ohio)            | us-east-2      | savingsplans.amazonaws.com | HTTPS    |
| US East (N. Virginia)     | us-east-1      | savingsplans.amazonaws.com | HTTPS    |
| US West (N. California)   | us-west-1      | savingsplans.amazonaws.com | HTTPS    |
| US West (Oregon)          | us-west-2      | savingsplans.amazonaws.com | HTTPS    |
| Africa (Cape Town)        | af-south-1     | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Hyderabad)  | ap-south-2     | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Malaysia)   | ap-southeast-5 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)  | ap-southeast-4 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Osaka)      | ap-northeast-3 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Thailand)   | ap-southeast-7 | savingsplans.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | savingsplans.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | savingsplans.amazonaws.com | HTTPS    |
| Canada West (Calgary)     | ca-west-1      | savingsplans.amazonaws.com | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | savingsplans.amazonaws.com | HTTPS    |
| Europe (Ireland)          | eu-west-1      | savingsplans.amazonaws.com | HTTPS    |
| Europe (London)           | eu-west-2      | savingsplans.amazonaws.com | HTTPS    |
| Europe (Milan)            | eu-south-1     | savingsplans.amazonaws.com | HTTPS    |
| Europe (Paris)            | eu-west-3      | savingsplans.amazonaws.com | HTTPS    |
| Europe (Spain)            | eu-south-2     | savingsplans.amazonaws.com | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | savingsplans.amazonaws.com | HTTPS    |
| Europe (Zurich)           | eu-central-2   | savingsplans.amazonaws.com | HTTPS    |
| Israel (Tel Aviv)         | il-central-1   | savingsplans.amazonaws.com | HTTPS    |
| Middle East (Bahrain)     | me-south-1     | savingsplans.amazonaws.com | HTTPS    |
| Middle East (UAE)         | me-central-1   | savingsplans.amazonaws.com | HTTPS    |
| South America (São Paulo) | sa-east-1      | savingsplans.amazonaws.com | HTTPS    |
| AWS GovCloud (US-East)    | us-gov-east-1  | savingsplans.amazonaws.com | HTTPS    |
| AWS GovCloud (US-West)    | us-gov-west-1  | savingsplans.amazonaws.com | HTTPS    |

## Service quotas

| Name                                                                                           | Default                               | Adjustable                                                                                                                                                               | Description                                                                                                              |
| ---------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Cost Explorer saved reports                                                                    | Each supported Region: 300            | No                                                                                                                                                                       | The maximum number of reports that you save in an AWS account.                                                           |
| Number of AWS managed linked account, cost category, and cost allocation tag anomaly monitors  | Each supported Region: 1              | No                                                                                                                                                                       | Maximum number of AWS managed anomaly monitors (linked account, cost category, or cost allocation tags) per account      |
| Number of AWS managed services anomaly monitors                                                | Each supported Region: 1              | No                                                                                                                                                                       | The maximum number of AWS managed service anomaly monitors per account                                                   |
| Number of Cost Categories                                                                      | Each supported Region: 50             | No                                                                                                                                                                       | The maximum number of Cost Categories per payer account                                                                  |
| Number of active cost allocation tag keys                                                      | Each supported Region: 500            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ce/quotas/L-FE0E51D7 "https://console.aws.amazon.com/servicequotas/home/services/ce/quotas/L-FE0E51D7") | The maximum number of active cost allocation tag keys per payer account                                                  |
| Number of affected accounts in an organization that can be migrated using Bulk Policy Migrator | Each supported Region: 200            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ce/quotas/L-3B4FC070 "https://console.aws.amazon.com/servicequotas/home/services/ce/quotas/L-3B4FC070") | The maximum number of affected accounts in an organization that you can migrate with Bulk Policy Migrator                |
| Number of affected policies in an organization that can be migrated using Bulk Policy Migrator | Each supported Region: 1,000          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ce/quotas/L-563A19D7 "https://console.aws.amazon.com/servicequotas/home/services/ce/quotas/L-563A19D7") | The maximum number of affected policies in an organization that you can migrate with Bulk Policy Migrator                |
| Number of anomaly alert subscriptions                                                          | Each supported Region: 100            | No                                                                                                                                                                       | The maximum number of anomaly alert subscriptions you can create per account                                             |
| Number of customer managed anomaly monitors                                                    | Each supported Region: 500            | No                                                                                                                                                                       | Maximum number of customer managed anomaly monitors (linked account, cost category, or cost allocation tags) per account |
| Number of refresh requests for Savings Plans recommendations per day                           | Each supported Region: 3 per 24 hours | No                                                                                                                                                                       | The maximum number of daily refresh requests for Savings Plans recommendations per consolidated billing family           |
| Number of rules per Cost Category (API)                                                        | Each supported Region: 500            | No                                                                                                                                                                       | The maximum number of Cost Category rules per Cost Category (API)                                                        |
| Number of rules per Cost Category (UI)                                                         | Each supported Region: 100            | No                                                                                                                                                                       | The maximum number of Cost Category rules per Cost Category (UI)                                                         |
| Number of values tracked by AWS managed anomaly monitors                                       | Each supported Region: 5,000          | No                                                                                                                                                                       | Maximum tracked dimension values per AWS managed anomaly monitor                                                         |

For more information, see [AWS Billing
quotas and restrictions](../../../awsaccountbilling/latest/aboutv2/billing-limits.md "../../../awsaccountbilling/latest/aboutv2/billing-limits.md") and [AWS Cost Management quotas and
restrictions](../../../cost-management/latest/userguide/management-limits.md "../../../cost-management/latest/userguide/management-limits.md").
