# Creating a DynamoDB zero-ETL integration with Amazon SageMaker Lakehouse

After completing integration prerequisites, you can create, modify, or delete the zero-ETL
integration following the guidance below:

## Creating an integration

###### To create an integration

1. Sign in to the AWS Management Console and open the Amazon DynamoDB
   console at [https://console.aws.amazon.com/dynamodbv2](https://console.aws.amazon.com/dynamodbv2 "https://console.aws.amazon.com/dynamodbv2").
2. In the navigation pane, choose **Integrations**.
3. Select **Create zero-ETL integration with Amazon SageMaker Lakehouse**, and
   then choose **Next**.
4. To create an integration, see [Creating an integration](../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-creating "../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-creating").
5. To modify an integration, see [Modifying an integration](../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-modifying "../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-modifying").
6. To delete an integration, see [Deleting an integration](../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-deleting "../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-deleting").
7. To set up a cross-account integration, see [Setting up cross-account integration](../../../glue/latest/dg/zero-etl-prerequisites.md#zero-etl-setup-cross-account-integration "../../../glue/latest/dg/zero-etl-prerequisites.md#zero-etl-setup-cross-account-integration").

## Enabling compaction on target Amazon S3 tables

You can enable compaction to improve query performance in Amazon Athena.

First, complete the prerequisite setup for compaction resources, including
configuring the necessary IAM role. Refer to the Lake Formation documentation for detailed
IAM role configuration steps. See, [Optimizing tables for compaction](../../../lake-formation/latest/dg/data-compaction.md "../../../lake-formation/latest/dg/data-compaction.md").

To enable compaction on the AWS Glue table created during integration, follow the Lake Formation compaction
enabling process. This will help optimize your table's performance and query efficiency.
