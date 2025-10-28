# View deleted stacks from the CloudFormation

console

By default, the CloudFormation console doesn't display stacks with a status of
`DELETE_COMPLETE`. To display information about deleted stacks, you must change the
stack view.

###### To view deleted stacks

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region where the
   deleted stack is located.
3. On the **Stacks** page, choose **Deleted** from the
   **Filter status** drop-down.
   CloudFormation lists all your stacks with a status of `DELETE_COMPLETE`.

## See also

- [Delete a stack from the CloudFormation console](cfn-console-delete-stack.md "cfn-console-delete-stack.md")
- [View stack information from the
  CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md")
