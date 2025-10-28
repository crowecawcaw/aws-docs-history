# Disabling Detective integration with Security Lake

If you disable Detective integration with Security Lake, you can no longer query log and event data from Security Lake.

###### To disable Detective integration with Security Lake

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Integrations**.
3. Delete the existing stack. For more details, see [Deleting a CloudFormation stack](#delete-stack "#delete-stack").
4. In the **Disable Security Lake integration** pane, choose
   **Disable**.

## Deleting a CloudFormation stack

If you do not delete the existing stack, new stack creation in the same Region will
fail. You can delete a CloudFormation stack by using the CloudFormation console or use the AWS
CLI.

###### To delete the AWS CloudFormation stack (Console)

1. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page in the CloudFormation console, select the
   stack that you want to delete. The stack must be currently running.
3. In the stack details pane, choose **Delete**.
4. Select **Delete stack** when prompted.

###### Note

The stack deletion operation can't be stopped once the stack deletion has
begun. The stack proceeds to the `DELETE_IN_PROGRESS`
state.

After the stack deletion is complete, the stack will be in the
`DELETE_COMPLETE` state.

**Troubleshooting stack deletion errors**

If you are seeing a permission error with the message `Failed to delete
 stack` after clicking the `Delete` button, your IAM role doesn't
have CloudFormation permission to delete a stack. Contact your account administrator to
delete the stack.

**To delete the CloudFormation stack (AWS CLI)**

Enter the following command in the AWS CLI interface:

```
aws cloudformation delete-stack --stack-name your-stack-name --role-arn
      arn:aws:iam::<ACCOUNT ID>:role/CFN-DetectiveSecurityLakeIntegration
```

`CFN-DetectiveSecurityLakeIntegration` is the service role that you created
in the `Creating an AWS CloudFormation Service Role` step.
