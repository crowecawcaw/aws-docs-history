# Prerequisites

Before you can use the AWS Resilience Hub, you must complete the following
prerequisites:

- AWS accounts – Create one or more AWS accounts for each account
  type (primary/secondary/resource accounts) you want use within AWS Resilience Hub. For more information about creating and managing AWS accounts, see the following:
  - First time AWS user – [Getting started: Are you a first-time AWS user?](../../../accounts/latest/reference/welcome-first-time-user.md "../../../accounts/latest/reference/welcome-first-time-user.md")
  - Managing AWS account – [https://docs.aws.amazon.com/accounts/latest/reference/managing-accounts.html](../../../accounts/latest/reference/managing-accounts.md "../../../accounts/latest/reference/managing-accounts.md")

- AWS Identity and Access Management (IAM) permissions – After creating the AWS accounts, you
  must configure the required roles and IAM permissions for each of the accounts
  you have created. For example, if you have created an AWS account to access
  application resources, you must setup a new role and configure the necessary
  IAM permissions for AWS Resilience Hub to access the application resources from your
  account. To learn more about IAM permissions, see [How AWS Resilience Hub works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md") and for more information about
  adding a policy to the role, see [Defining trust policy using JSON file](security-iam-resilience-hub-invoker-role.md#security-iam-resilience-define-policy "security-iam-resilience-hub-invoker-role.md#security-iam-resilience-define-policy").

To get started quickly with adding IAM permissions to users, groups, and
roles, you can use our AWS managed policies ([AWS managed policies for AWS Resilience Hub](security-iam-awsmanpol.md "security-iam-awsmanpol.md")). It is easier to use AWS managed
policies to cover common use cases that are available in your AWS account than
to write policies yourself. AWS Resilience Hub adds additional permissions to an AWS
managed policy to extend support to other AWS services and to include new
features. Hence:

    + If you are an existing customer and if you want your application to
     use the latest enhancements within your assessment, you must publish a
     new version of the application and then run a new assessment. For more
     information, see the following topics:




    	- [Publishing a new AWS Resilience Hub application
    	 version](applications-publish.md "applications-publish.md")
    	- [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md")
    + If you are not using AWS managed policies to assign appropriate
     IAM permissions to users, groups, and roles, you must manually
     configure these permissions. For more information about AWS managed
     policies, see [AWSResilienceHubAsssessmentExecutionPolicy](security-iam-awsmanpol.md#security_iam_aws-assessment-policy "security-iam-awsmanpol.md#security_iam_aws-assessment-policy").
