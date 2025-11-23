# PCUI costs

The PCUI is built on a serverless architecture and you can use it within the AWS Free Tier category for most cases. The following table
lists the AWS services that the PCUI depends on and their free-tier limits. Typical usage is estimated to cost less than one dollar each
month.

| Service                      | AWS Free Tier                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| Amazon Cognito               | 50,000 monthly active users                                                          |
| Amazon API Gateway           | 1 million rest API calls                                                             |
| AWS Lambda                   | 1 million free requests each month and 400,000 GB-seconds of compute time each month |
| EC2 Image Builder            | No cost, except EC2                                                                  |
| Amazon Elastic Compute Cloud | 15-minute one-time container image build                                             |
| CloudFormation               | 5 GB data (ingestion, archive storage, and data scanned by Logs Insights queries)    |
