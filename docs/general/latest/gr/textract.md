# Amazon Textract endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                                                                                                                                   | Protocol                         |
| ------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)           | us-east-2      | textract.us-east-2.amazonaws.com<br>textract-fips.us-east-2.api.aws<br>textract-fips.us-east-2.amazonaws.com<br>textract.us-east-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)    | us-east-1      | textract.us-east-1.amazonaws.com<br>textract-fips.us-east-1.api.aws<br>textract-fips.us-east-1.amazonaws.com<br>textract.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)  | us-west-1      | textract.us-west-1.amazonaws.com<br>textract-fips.us-west-1.api.aws<br>textract-fips.us-west-1.amazonaws.com<br>textract.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | textract.us-west-2.amazonaws.com<br>textract-fips.us-west-2.api.aws<br>textract-fips.us-west-2.amazonaws.com<br>textract.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | textract.ap-south-1.amazonaws.com<br>textract.ap-south-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)     | ap-northeast-2 | textract.ap-northeast-2.amazonaws.com<br>textract.ap-northeast-2.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore) | ap-southeast-1 | textract.ap-southeast-1.amazonaws.com<br>textract.ap-southeast-1.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)    | ap-southeast-2 | textract.ap-southeast-2.amazonaws.com<br>textract.ap-southeast-2.api.aws                                                                                   | HTTPS<br>HTTPS                   |
| Canada (Central)         | ca-central-1   | textract.ca-central-1.amazonaws.com<br>textract-fips.ca-central-1.api.aws<br>textract-fips.ca-central-1.amazonaws.com<br>textract.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)       | eu-central-1   | textract.eu-central-1.amazonaws.com<br>textract.eu-central-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Ireland)         | eu-west-1      | textract.eu-west-1.amazonaws.com<br>textract.eu-west-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (London)          | eu-west-2      | textract.eu-west-2.amazonaws.com<br>textract.eu-west-2.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Paris)           | eu-west-3      | textract.eu-west-3.amazonaws.com<br>textract.eu-west-3.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Spain)           | eu-south-2     | textract.eu-south-2.amazonaws.com<br>textract.eu-south-2.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)   | us-gov-east-1  | textract.us-gov-east-1.amazonaws.com<br>textract-fips.us-gov-east-1.api.aws<br>textract-fips.us-gov-east-1.amazonaws.com<br>textract.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)   | us-gov-west-1  | textract.us-gov-west-1.amazonaws.com<br>textract-fips.us-gov-west-1.api.aws<br>textract-fips.us-gov-west-1.amazonaws.com<br>textract.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

## Service quotas

| Resources                                                                      | Regions               |
| ------------------------------------------------------------------------------ | --------------------- | --------------------- | ---------------- | -------------- | ---------------- | --------------------- | ------------- |
| Synchronous Operations                                                         | API                   | US East (N. Virginia) | US West (Oregon) | US East (Ohio) | Europe (Ireland) | Asia Pacific (Mumbai) | Other Regions |
| Transactions per second per account for synchronous operations                 | AnalyzeDocument       | 10                    | 10               | 10             | 5                | 5                     | 1             |
| DetectDocumentText                                                             | 25                    | 25                    | 10               | 5              | 5                | 1                     |
| AnalyzeExpense                                                                 | 5                     | 5                     | 1                | 1              | 1                | 1                     |
| AnalyzeID                                                                      | 5                     | 5                     | 1                | 1              | 1                | 1                     |
| Asynchronous Operations                                                        | API                   | US East (N. Virginia) | US West (Oregon) | US East (Ohio) | Europe (Ireland) | Asia Pacific (Mumbai) | Other Regions |
| Transactions per second per account for all start<br>(asynchronous) operations | StartDocumentAnalysis | 10                    | 10               | 10             | 5                | 5                     | 2             |
| StartDocumentTextDetection                                                     | 15                    | 15                    | 5                | 5              | 5                | 1                     |
| StartExpenseAnalysis                                                           | 5                     | 5                     | 1                | 1              | 1                | 1                     |
| StartLendingAnalysis                                                           | 5                     | 5                     | 1                | 1              | 1                | 1                     |
| Transactions per second per account for all get<br>(asynchronous) operations   | GetDocumentAnalysis   | 10                    | 10               | 10             | 5                | 5                     | 5             |
| GetDocumentTextDetection                                                       | 25                    | 25                    | 10               | 5              | 5                | 5                     |
| GetExpenseAnalysis                                                             | 5                     | 5                     | 5                | 5              | 5                | 5                     |
| GetLendingAnalysis                                                             | 25                    | 25                    | 5                | 5              | 5                | 5                     |
| GetLendingAnalysisSummary                                                      | 5                     | 5                     | 1                | 1              | 1                | 1                     |
| Maximum number of asynchronous jobs per account that can simultaneously exist  |                       | 600                   | 600              | 100            | 100              | 100                   | 100           |

For more information, see [Amazon Textract
Quotas](../../../textract/latest/dg/limits.md "../../../textract/latest/dg/limits.md") in the _Amazon Textract Developer Guide_.

## Adapters quotas

- Maximum number of adapters - Total number of adapters allowed are 10.
  You can have a several adapter versions under a single adapter.
- Maximum AdapterVersions created per month - Number of successful adapter
  versions that can be created per AWS account per month is 10 which will be reset
  at the start of every month. Use the Service Quotas console to raise a service
  quota increase request.
- Maximum in-progress AdapterVersions (analogous to adapter training)
  per account - 3

For more information, see [Amazon Textract
Quotas](../../../textract/latest/dg/limits.md "../../../textract/latest/dg/limits.md") in the _Amazon Textract Developer Guide_.
