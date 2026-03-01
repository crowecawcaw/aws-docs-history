# Remove a resource-based policy from a DynamoDB table

You can delete a resource-based policy from an existing table by using the DynamoDB console,
[DeleteResourcePolicy](../APIReference/API_DeleteResourcePolicy.md "../APIReference/API_DeleteResourcePolicy.md") API, the AWS CLI, AWS SDK, or an CloudFormation template.

The following example uses the `delete-resource-policy` AWS CLI command to
remove a resource-based policy from a table named
`MusicCollection`.

Remember to replace the `italicized` text with your resource-specific information.

```
aws dynamodb delete-resource-policy \
    --resource-arn arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection`
```

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. On the DynamoDB console dashboard, choose **Tables** and then select
   an existing table.
3. Choose **Permissions**.
4. From the **Manage policy** dropdown, choose **Delete
   policy**.
5. In the **Delete resource-based policy for table** dialog box,
   type `confirm` to confirm the delete action.
6. Choose **Delete**.
