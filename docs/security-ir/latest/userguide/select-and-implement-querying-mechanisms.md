# Select and implement querying mechanisms for logs

In AWS, the main services you can use to query logs are
[CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md")
for data stored in CloudWatch log groups, and
[Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") and [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/")
for data stored in Amazon S3. You can also use third-party querying tools such as a security information and event management (SIEM).

The process for selecting a log querying tool should consider the people, process, and
technology aspects of your security operations. Select a tool that fulfills operational,
business, and security requirements, and is both accessible and maintainable in the long
term. Keep in mind that log querying tools work optimally when the number of logs to be
scanned is kept within the tool’s limits. It is not uncommon for customers to have
multiple querying tools because of cost or technical constraints. For example, customers
might use a third-party SIEM to perform queries for the last 90 days of data, and use Athena
to perform queries beyond 90 days because of the log ingestion cost of a SIEM. No
matter the implementation, verify that your approach minimizes the number of tools required
to maximize operational efficiency, especially during a security event investigation.
