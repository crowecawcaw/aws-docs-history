AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with AWS CloudFormation stacks using AWS Toolkit

The AWS Toolkit provides support for [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") stacks. Using the AWS Toolkit, you can delete an CloudFormation stack.

## Deleting CloudFormation stacks

You can use the AWS Toolkit to view and delete CloudFormation stacks.

### Prerequisites

- Ensure that the credentials you're using in the AWS Cloud9 environment include
  appropriate read/write access to the CloudFormation service. If in the
  **AWS Explorer**, under
  **CloudFormation**, you see a message similar to "Error
  loading CloudFormation resources," check the permissions attached to those
  credentials. Changes that you make to permissions take a few minutes to
  affect the **AWS Explorer**.

## To delete an CloudFormation stack

1. In the **AWS Explorer**, open the context (right-click)
   menu of the CloudFormation stack you want to delete.
2. Choose **Delete CloudFormation Stack**.
3. In the message that appears, choose **Yes** to conﬁrm the
   delete.

After the stack is deleted, it's no longer listed in the **AWS Explorer**.
