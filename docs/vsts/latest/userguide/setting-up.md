# Setting up the AWS Toolkit for Azure DevOps

To use the AWS Toolkit for Azure DevOps to access AWS, you need an AWS account and AWS credentials. When
build agents run the tasks contained in the tools, the tasks must be configured with, or
have access to, those AWS credentials to enable them to call AWS service APIs. To
increase the security of your AWS account, we recommend that you do not use your root
account credentials. You should create an _IAM user_ to provide access
credentials to the tasks running in the build agent processes.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.
