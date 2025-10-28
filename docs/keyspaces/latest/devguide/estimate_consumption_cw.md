# Estimate read and write capacity consumption with Amazon CloudWatch in Amazon Keyspaces

To estimate and monitor read and write capacity consumption, you can use a CloudWatch dashboard. For more
information about available metrics for Amazon Keyspaces, see [Amazon Keyspaces metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md").

To monitor read and write capacity units consumed by a specific statement with CloudWatch, you can follow these steps.

1. Create a new table with sample data
2. Configure a Amazon Keyspaces CloudWatch dashboard for the table. To get started, you can use a dashboard template available on [Github](https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates "https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates").
3. Run the CQL statement, for example using the `ALLOW FILTERING` option, and check the read capacity
   units consumed for the full table scan in the dashboard.
