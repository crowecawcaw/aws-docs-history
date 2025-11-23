# Cancel a stack update

After a stack update has begun, you can cancel the stack update if the stack is still in
the `UPDATE_IN_PROGRESS` state. After an update has finished, you can't cancel it.
You can, however, update a stack again with any previous settings.

If you cancel a stack update, the stack is rolled back to the stack configuration that
existed before initiating the stack update.

###### Topics

- [To cancel a stack update
  (console)](#using-cfn-stack-update-cancel-console "#using-cfn-stack-update-cancel-console")
- [To cancel a stack update
  (AWS CLI)](#using-cfn-stack-update-cancel-cli "#using-cfn-stack-update-cancel-cli")

## To cancel a stack update

(console)

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region where the
   stack is located.
3. On the **Stacks** page, choose the stack that's currently being
   updated. Its status must be `UPDATE_IN_PROGRESS`.
4. Choose **Stack actions** and then **Cancel update
   stack**.
5. To continue canceling the update, choose **Cancel update**.
   Otherwise, choose **Cancel** to resume the update.

The stack proceeds to the `UPDATE_ROLLBACK_IN_PROGRESS` state. After the
update cancellation is complete, the stack is set to
`UPDATE_ROLLBACK_COMPLETE`.

## To cancel a stack update

(AWS CLI)

Use the command [cancel-update-stack](../../../cli/latest/reference/cloudformation/cancel-update-stack.md "../../../cli/latest/reference/cloudformation/cancel-update-stack.md") to cancel an update. For more
information, see [Cancel a stack update](service_code_examples.md#cancel-update-stack-sdk "service_code_examples.md#cancel-update-stack-sdk").
