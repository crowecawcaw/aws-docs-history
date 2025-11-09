# Troubleshooting for Multi-Account

Multi-Region Data Aggregation for AWS Config

AWS Config might not aggregate data from source accounts for one of the following
reasons:

| If this happens                                                                         | Do this                                                                                                        |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| AWS Config is not enabled in the source account for accounts within an<br>Organization. | Enable AWS Config in the source account and authorize the aggregator account to<br>collect data.               |
| Authorization is not granted to an aggregator account.                                  | Sign in to the source account and grant authorization to the aggregator<br>account to collect AWS Config data. |
| There might be a temporary issue that is preventing data<br>aggregation.                | Data aggregation is subject to delays. Wait for a few minutes.                                                 |

AWS Config might not aggregate data from an organization for one of the following
reasons:

| If this happens                                                                                                                                                                                                               | Do this                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS Config is unable to access your organization details due to invalid IAM<br>role.                                                                                                                                          | Create an IAM role or select a valid IAM role from the IAM role<br>list. NoteIf the IAM role is invalid for more than 7 days, AWS Config deletes<br>data for entire organization.                                                                                        |
| AWS Config service access is disabled in your organization.                                                                                                                                                                   | You can enable integration between AWS Config and AWS Organizations through the<br>`EnableAWSServiceAccess` API. If you choose \*_Add my<br>organization_<br>• in console, AWS Config automatically enables the<br>integration between AWS Config and AWS Organizations. |
| AWS Config is unable to access your organization details because all features<br>is not enabled in your organization.                                                                                                         | [Enable all features](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in AWS Organizations console.                                                   |
| Organizational changes such as adding an account, removing an account,<br>enabling service access, and disabling service access are not updated in<br>Middle East (Bahrain) and Asia Pacific (Hong Kong) regions immediately. | Organizational changes are subject to 2 hour delay. Wait for 2 hours to<br>see all organization changes.                                                                                                                                                                 |
