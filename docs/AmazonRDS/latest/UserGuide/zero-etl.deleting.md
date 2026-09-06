

# Deleting Amazon RDS zero-ETL integrations
<a name="zero-etl.deleting"></a>

When you delete a zero-ETL integration, Amazon RDS removes it from the source database. Your transactional data isn't deleted from Amazon RDS or the analytics destination, but Amazon RDS doesn't send new data to Amazon Redshift or Amazon SageMaker.

You can only delete an integration when it has a status of `Active`, `Failed`, `Syncing`, or `Needs attention`.

You can delete zero-ETL integrations using the AWS Management Console, the AWS CLI, or the RDS API.

## Console
<a name="zero-etl.deleting-console"></a>

**To delete a zero-ETL integration**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. From the left navigation pane, choose **Zero-ETL integrations**. 

1. Select the zero-ETL integration that you want to delete. 

1. Choose **Actions**, **Delete**, and confirm deletion.

## AWS CLI
<a name="zero-etl.deleting-cli"></a>

To delete a zero-ETL integration, use the [delete-integration](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-integration.html) command and specify the `--integration-identifier` option.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds delete-integration \
    --integration-identifier {{ee605691-6c47-48e8-8622-83f99b1af374}}
```
For Windows:  

```
aws rds delete-integration ^
    --integration-identifier {{ee605691-6c47-48e8-8622-83f99b1af374}}
```

## RDS API
<a name="zero-etl.deleting-api"></a>

To delete a zero-ETL integration using the Amazon RDS API, use the [`DeleteIntegration`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteIntegration.html) operation with the `IntegrationIdentifier` parameter.