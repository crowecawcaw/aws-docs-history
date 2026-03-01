# DynamoDB zero-ETL integration with Amazon SageMaker Lakehouse

Setting up an integration between the DynamoDB table and Amazon SageMaker Lakehouse require
prerequisites such as configuring IAM roles which AWS Glue uses to access data from the
source and write to the target, and the use of KMS keys to encrypt the data in
intermediate or the target location.

###### Topics

- [Prerequisites before creating a DynamoDB zero-ETL integration with Amazon SageMaker Lakehouse](#amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-prereqs "#amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-prereqs")
- [Creating a DynamoDB zero-ETL integration with Amazon SageMaker Lakehouse](amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-getting-started.md "amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-getting-started.md")
- [Viewing CloudWatch metrics for integration](#amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-cloudwatch-metrics "#amazon-sagemaker-lakehouse-for-DynamoDB-zero-etl-cloudwatch-metrics")

## Prerequisites before creating a DynamoDB zero-ETL integration with Amazon SageMaker Lakehouse

To configure a zero-ETL integration with an DynamoDB source, you need to set up a
Resource-Based Access (RBAC) policy that allows AWS Glue to access and export data from
the DynamoDB table. The policy should include specific permissions like
`ExportTableToPointInTime`, `DescribeTable`, and
`DescribeExport` with conditions restricting access to a specific
AWS account and region. See, [Configuring an Amazon DynamoDB source](../../../glue/latest/dg/zero-etl-sources.md#zero-etl-config-source-dynamodb "../../../glue/latest/dg/zero-etl-sources.md#zero-etl-config-source-dynamodb") for more information.

Point-in-time recovery (PITR) must be enabled for the table, and you can apply
the policy using AWS CLI commands. The policy can be further refined by specifying the
full integration ARN for more restrictive access control. For more information, see
[Prerequisites for setting up a zero-ETL integration](../../../glue/latest/dg/zero-etl-prerequisites.md "../../../glue/latest/dg/zero-etl-prerequisites.md").

## Viewing CloudWatch metrics for integration

Once an integration completes, you can see these CloudWatch metrics and EventBridge
notifications generated in your account for each AWS Glue job. For more information,
see [Monitoring an integration](../../../glue/latest/dg/zero-etl-monitoring.md "../../../glue/latest/dg/zero-etl-monitoring.md").
