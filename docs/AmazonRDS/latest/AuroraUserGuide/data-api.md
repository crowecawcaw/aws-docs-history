# Using the Amazon RDS Data API

By using RDS Data API (Data API), you can work with a web-services interface to your
Aurora DB cluster. Data API doesn't require a persistent connection to the DB cluster.
Instead, it provides a secure HTTP endpoint and integration with AWS SDKs. You can use the
endpoint to run SQL statements without managing connections.

Users don't need to pass credentials with calls to Data API, because Data API
uses database credentials stored in AWS Secrets Manager. To store credentials in Secrets Manager, users
must be granted the appropriate permissions to use Secrets Manager, and also Data API. For more
information about authorizing users, see [Authorizing access to the Amazon RDS Data API](data-api.md "data-api.md").

You can also use Data API to integrate Amazon Aurora with other AWS applications such as
AWS Lambda, AWS AppSync, and AWS Cloud9.

Data API provides a more secure way to use AWS Lambda. It enables you to access your DB
cluster without your needing to configure a Lambda function to access resources in a virtual
private cloud (VPC). For more information, see [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"),
[AWS AppSync](https://aws.amazon.com/appsync/ "https://aws.amazon.com/appsync/"), and [AWS Cloud9](https://aws.amazon.com/cloud9/ "https://aws.amazon.com/cloud9/").

You can enable Data API when you create the Aurora DB cluster. You can also modify the
configuration later. For more information, see [Enabling the Amazon RDS Data API](data-api.md "data-api.md").

After you enable Data API, you can also use the query editor to run ad hoc queries
without configuring a query tool to access Aurora in a VPC. For more information, see [Using the Aurora query editor](query-editor.md "query-editor.md").

###### Topics

- [Region and version availability for the Amazon RDS Data API](data-api.md "data-api.md")
- [Using IPv6 with Amazon RDS Data API](data-api.md "data-api.md")
- [Limitations for the Amazon RDS Data API](data-api.md "data-api.md")
- [Comparing Amazon RDS Data API behaviors for Aurora Serverless v2 and provisioned clusters with Aurora Serverless v1 clusters](data-api.md "data-api.md")
- [Authorizing access to the Amazon RDS Data API](data-api.md "data-api.md")
- [Enabling the Amazon RDS Data API](data-api.md "data-api.md")
- [Creating an Amazon VPC endpoint for the Amazon RDS Data API
  (AWS PrivateLink)](data-api.md "data-api.md")
- [Calling the Amazon RDS Data API](data-api.md "data-api.md")
- [Using the Java client library for RDS
  Data API](data-api.md "data-api.md")
- [Processing Amazon RDS Data API query results in JSON format](data-api-json.md "data-api-json.md")
- [Troubleshooting Amazon RDS Data API](data-api.md "data-api.md")
- [Logging Amazon RDS Data API calls with
  AWS CloudTrail](logging-using-cloudtrail-data-api.md "logging-using-cloudtrail-data-api.md")
- [Monitoring RDS Data API queries with Performance Insights](monitoring-using-performance-insights-data-api.md "monitoring-using-performance-insights-data-api.md")
