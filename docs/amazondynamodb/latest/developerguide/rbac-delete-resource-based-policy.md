

# Remove a resource-based policy from a DynamoDB table
<a name="rbac-delete-resource-based-policy"></a>

You can delete a resource-based policy from an existing table by using the DynamoDB console, [DeleteResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteResourcePolicy.html) API, the AWS CLI, AWS SDK, or an CloudFormation template.

## AWS CLI
<a name="rbac-delete-policy-CLI"></a>

The following example uses the `delete-resource-policy` AWS CLI command to remove a resource-based policy from a table named {{MusicCollection}}.

Remember to replace the {{italicized}} text with your resource-specific information.

```
aws dynamodb delete-resource-policy \
    --resource-arn arn:aws:dynamodb:us-west-2:{{123456789012}}:table/{{MusicCollection}}
```

## AWS Management Console
<a name="rbac-delete-policy-console"></a>

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. On the DynamoDB console dashboard, choose **Tables** and then select an existing table.

1. Choose **Permissions**.

1. From the **Manage policy** dropdown, choose **Delete policy**.

1. In the **Delete resource-based policy for table** dialog box, type **confirm** to confirm the delete action.

1. Choose **Delete**.