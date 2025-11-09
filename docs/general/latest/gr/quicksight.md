# Amazon Quick Sight

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

### QuickSight

| Region Name               | Region         | Endpoint                                | Protocol |
| ------------------------- | -------------- | --------------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | quicksight.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | quicksight.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | quicksight.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)        | af-south-1     | quicksight.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | quicksight.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | quicksight.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | quicksight.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | quicksight.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | quicksight.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | quicksight.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | quicksight.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | quicksight.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | quicksight.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | quicksight.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)            | eu-south-1     | quicksight.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)            | eu-west-3      | quicksight.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | quicksight.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | quicksight.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)           | eu-central-2   | quicksight.eu-central-2.amazonaws.com   | HTTPS    |
| Israel (Tel Aviv)         | il-central-1   | quicksight.il-central-1.amazonaws.com   | HTTPS    |
| Middle East (UAE)         | me-central-1   | quicksight.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo) | sa-east-1      | quicksight.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)    | us-gov-east-1  | quicksight.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)    | us-gov-west-1  | quicksight.us-gov-west-1.amazonaws.com  | HTTPS    |

### QuickSight Websites

| Region Name              | Region         | Endpoint                                         |
| ------------------------ | -------------- | ------------------------------------------------ |
| US East (Ohio)           | us-east-2      | https://us-east-2.quicksight.aws.amazon.com      |
| US East (N. Virginia)    | us-east-1      | https://us-east-1.quicksight.aws.amazon.com      |
| US West (Oregon)         | us-west-2      | https://us-west-2.quicksight.aws.amazon.com      |
| Canada (Central)         | ca-central-1   | https://ca-central-1.quicksight.aws.amazon.com   |
| Asia Pacific (Mumbai)    | ap-south-1     | https://ap-south-1.quicksight.aws.amazon.com     |
| Asia Pacific (Singapore) | ap-southeast-1 | https://ap-southeast-1.quicksight.aws.amazon.com |
| Asia Pacific (Sydney)    | ap-southeast-2 | https://ap-southeast-2.quicksight.aws.amazon.com |
| Asia Pacific (Tokyo)     | ap-northeast-1 | https://ap-northeast-1.quicksight.aws.amazon.com |
| Asia Pacific (Seoul)     | ap-northeast-2 | https://ap-northeast-2.quicksight.aws.amazon.com |
| Europe (Frankfurt)       | eu-central-1   | https://eu-central-1.quicksight.aws.amazon.com   |
| Europe (Ireland)         | eu-west-1      | https://eu-west-1.quicksight.aws.amazon.com      |
| Europe (London)          | eu-west-2      | https://eu-west-2.quicksight.aws.amazon.com      |
| Europe (Paris)           | eu-west-3      | https://eu-west-3.quicksight.aws.amazon.com      |
| Europe (Stockholm)       | eu-north-1     | https://eu-north-1.quicksight.aws.amazon.com     |
| AWS GovCloud (US-East)   | us-gov-east-1  | https://quicksight.us-gov-east-1.amazonaws.com   |
| AWS GovCloud (US-West)   | us-gov-west-1  | https://quicksight.us-gov-west-1.amazonaws.com   |
| Israel (Tel Aviv)        | il-central-1   | https://il-central-1.quicksight.aws.amazon.com/  |
| Middle East (UAE)        | me-central-1   | https://me-central-1.quicksight.aws.amazon.com/  |

## Service quotas

| Name                                                                   | Default                                 | Adjustable | Description                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------- | --------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API_CREATE-INGESTION: Calls per 24 hour period from Enterprise edition | Each supported Region: 32               | No         | The maximum number of calls to the createIngestion API function in a floating 24-hour window. The time period is measured starting 24 hours before the current date and time. This maximum applies to AWS accounts that use Amazon QuickSight Enterprise edition. |
| API_CREATE-INGESTION: Calls per 24 hour period from Standard edition   | Each supported Region: 8                | No         | The maximum number of calls to the createIngestion API function in a floating 24-hour window. The time period is measured starting 24 hours before the current date and time. This maximum applies to AWS accounts that use Amazon QuickSight Standard edition.   |
| Amazon Quick Automate Maximum Automation Groups                        | Each supported Region: 200              | No         | Maximum number of Automation Groups allowed per account in Amazon Quick Automate                                                                                                                                                                                  |
| Amazon Quick Automate Maximum Automations                              | Each supported Region: 1,000            | No         | Maximum number of Automations allowed across all Automation Groups in Amazon Quick Automate                                                                                                                                                                       |
| Amazon Quick Automate Maximum Concurrent Executions per Trigger        | Each supported Region: 10               | No         | Maximum number of concurrent executions per trigger in Amazon Quick Automate                                                                                                                                                                                      |
| Amazon Quick Automate Maximum Concurrent Tests and Deployed Executions | Each supported Region: 50               | No         | Maximum number of concurrent tests and executions per account in Amazon Quick Automate                                                                                                                                                                            |
| Amazon Quick Automate Maximum Credentials                              | Each supported Region: 200              | No         | Maximum number of credentials allowed across all Automation Groups in Amazon Quick Automate                                                                                                                                                                       |
| Amazon Quick Automate Maximum Nesting Depth                            | Each supported Region: 6                | No         | Maximum nesting depth allowed in an automation in Amazon Quick Automate                                                                                                                                                                                           |
| Amazon Quick Automate Maximum Triggers per Automation                  | Each supported Region: 30               | No         | Maximum number of triggers allowed per automation in Amazon Quick Automate                                                                                                                                                                                        |
| Amazon Quick Automate Maximum Workflow Execution Time                  | Each supported Region: 48               | No         | Maximum workflow execution time in hours in Amazon Quick Automate                                                                                                                                                                                                 |
| Calculated field expression length                                     | Each supported Region: 250,000          | No         | The maximum number of characters that you can use in an expression for a calculated field.                                                                                                                                                                        |
| Custom action name length                                              | Each supported Region: 256              | No         | The maximum number of characters that you can use in naming a custom action.                                                                                                                                                                                      |
| Custom actions per visual                                              | Each supported Region: 10               | No         | The maximum number of custom actions that you can configure for each visual in an analysis.                                                                                                                                                                       |
| Data Prep: Fields per dataset                                          | Each supported Region: 2,000            | No         | The maximum number of fields that a dataset can contain. File imports and query result sets can contain more than 2,000 columns. However, you must edit the dataset settings and manually exclude fields until there are less than 2,000 selected or included.    |
| Display items per sheet control                                        | Each supported Region: 1,000            | No         | The maximum number of distinct items that a sheet control can display.                                                                                                                                                                                            |
| Email aliases per group for email reports                              | Each supported Region: 5,000            | No         | The maximum number of members in any group that QuickSight sends email reports to. If you try to send reports to larger groups, the report fails.                                                                                                                 |
| Maximum number of characters per specified Control values              | Each supported Region: 200,000          | No         | The maximum number of characters used in the entries that you type in to display inside sheet controls. An example is the values specified for a dropdown. This doesnt apply to values created from a dataset.                                                    |
| Maximum number of reference documents per chat agent                   | Each supported Region: 10               | No         | The maximum number of reference documents that can be attached to a chat agent.                                                                                                                                                                                   |
| Maximum number of resources per chat agent                             | Each supported Region: 20               | No         | The maximum number of resources that can be associated with a chat agent.                                                                                                                                                                                         |
| Maximum number of resources per space                                  | Each supported Region: 100              | No         | The maximum number of resources that can be linked to a space.                                                                                                                                                                                                    |
| Maximum number of uploaded files per space                             | Each supported Region: 10,000           | No         | The maximum number of files that can be uploaded to a space.                                                                                                                                                                                                      |
| Maximum total data capacity of an index                                | Each supported Region: 10,000 Megabytes | No         | The maximum total data capacity in megabytes (MBs) of an index.                                                                                                                                                                                                   |
| Maximum total size of attached reference documents per chat agent      | Each supported Region: 50 Megabytes     | No         | The maximum size in megabytes (MBs) of all reference documents attached to a chat agent.                                                                                                                                                                          |
| Maximum total size of uploaded files per space                         | Each supported Region: 1 Gigabytes      | No         | The maximum size in gigabytes (GBs) of all files uploaded to a space.                                                                                                                                                                                             |
| Query timeout for visuals                                              | Each supported Region: 120 Seconds      | No         | The maximum amount of time that QuickSight waits for a database to finish sending data. This applies to queries initiated by visuals.                                                                                                                             |
| The maximum amount of time to wait for a dataset preview               | Each supported Region: 45 Seconds       | No         | The maximum amount of time that QuickSight waits for a data preview to finish loading.                                                                                                                                                                            |
| URL action hyperlink length                                            | Each supported Region: 2,048            | No         | The maximum number of characters allowed in the hyperlink (URL) of a custom action thats defined as a URL action. This includes all variations of the link for the different parameters you include.                                                              |
