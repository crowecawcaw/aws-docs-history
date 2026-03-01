# Deleting DynamoDB zero-ETL integrations with Amazon Redshift

When you delete a zero-ETL integration, your data isn't deleted from DynamoDB or
Amazon Redshift, but DynamoDB stops sending data from your source table to the Amazon Redshift
target.

###### To delete a zero-ETL integration

1. Sign in to the AWS Management Console and open the Amazon DynamoDB console at
   [https://console.aws.amazon.com/dynamodbv2](https://console.aws.amazon.com/dynamodbv2 "https://console.aws.amazon.com/dynamodbv2").
2. In the DynamoDB console, choose **Integrations**.
3. In the **Zero-ETL integration** pane, select the
   zero-ETL integration you want to delete.
4. Choose **Manage**. This will take you to the integration
   details page.
5. To confirm the deletion, choose **Delete**.
