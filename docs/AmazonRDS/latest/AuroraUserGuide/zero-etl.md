# Deleting Aurora zero-ETL integrations

When you delete a zero-ETL integration, Amazon Aurora removes it from the source Aurora DB cluster. Your
transactional data isn't deleted from Amazon Aurora or the analytics destination, but Aurora doesn't send new data to
Amazon Redshift or Amazon SageMaker.

You can only delete an integration when it has a status of `Active`,
`Failed`, `Syncing`, or `Needs attention`.

You can delete zero-ETL integrations using the AWS Management Console, the AWS CLI, or the RDS API.

###### To delete a zero-ETL integration

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. From the left navigation pane, choose **Zero-ETL integrations**.
3. Select the zero-ETL integration that you want to delete.
4. Choose **Actions**, **Delete**, and
   confirm deletion.
   To delete a zero-ETL integration, use the [delete-integration](../../../cli/latest/reference/rds/delete-integration.md "../../../cli/latest/reference/rds/delete-integration.md")
   command and specify the `--integration-identifier` option.

For Linux, macOS, or Unix:

```
aws rds delete-integration \
    --integration-identifier `ee605691-6c47-48e8-8622-83f99b1af374`
```

For Windows:

```
aws rds delete-integration ^
    --integration-identifier `ee605691-6c47-48e8-8622-83f99b1af374`
```

To delete a zero-ETL integration using the Amazon RDS API, use the [`DeleteIntegration`](../APIReference/API_DeleteIntegration.md "../APIReference/API_DeleteIntegration.md") operation with the
`IntegrationIdentifier` parameter.
