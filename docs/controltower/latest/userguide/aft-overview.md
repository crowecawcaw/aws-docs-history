# Overview of AWS Control Tower Account Factory for Terraform

(AFT)

Account Factory for Terraform (AFT) sets up a Terraform pipeline to help you provision
and customize accounts in AWS Control Tower. AFT provides you with the advantage of
Terraform-based account provisioning while allowing you to govern your accounts with
AWS Control Tower.

With AFT you create an _account request Terraform file_
to get the input that triggers the AFT workflow for account provisioning. After the account
provisioning stage is complete, AFT automatically runs a series of steps before the account
customizations stage begins. For more information, see [AFT account
provisioning pipeline](aft-provisioning-framework.md "aft-provisioning-framework.md").

AFT supports Terraform Cloud, Terraform Enterprise, and Terraform Community Edition. With
AFT you can initiate account creation using an input file and a simple `git push`
command and customize new or existing accounts. Account creation includes all of the
AWS Control Tower governance benefits and account customizations that help you meet your
organization’s standard security procedures and compliance guidelines.

AFT supports account customization request tracing. Every time you submit an account
customization request, AFT generates a unique tracing token that passes through an AFT
customizations AWS Step Functions state machine, which logs the token as part of its execution. You
can then use Amazon CloudWatch Logs insights queries to search timestamp ranges and retrieve the request
token. As a result, you can see payloads that accompany the token, so you can trace your
account customization request throughout the entire AFT workflow. For information about
CloudWatch Logs and Step Functions, see the following:

- [What is
  Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") in the _Amazon CloudWatch Logs User Guide_
- [What is
  AWS Step Functions?](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") in the _AWS Step Functions Developer Guide_
  AFT combines the capabilities of other AWS services as [Component services](aft-components.md "aft-components.md"), to build a framework, with pipelines that deploy
  Terraform Infrastructure as Code (IaC). AFT enables you to:

- Submit account provisioning and update requests in a GitOps model
- Store account metadata and audit history
- Apply account-level tags
- Add customizations to all accounts, to a set of accounts, or to individual
  accounts
- Enable feature options
  AFT creates a separate account, called the _AFT
  management account_, to deploy AFT capabilities. Before you can set up AFT, you
  must have an existing AWS Control Tower landing zone. The AFT management account is not the same as the
  AWS Control Tower management account.

**AFT offers flexibility**

- **Flexibility for your platform:** AFT supports any
  Terraform Distribution for initial deployment and ongoing operation: Community
  Edition, Cloud, and Enterprise.
- **Flexibility for your version control system:** AFT
  supports AWS CodeCommit, and alternative version control sources through
  AWS CodeConnections.
  **AFT offers feature options**

You can enable several feature options, based on best practices:

- Creating an organization-level CloudTrail for logging data events
- Deleting the AWS default VPC for accounts
- Enrolling provisioned accounts into the AWS Enterprise Support plan

###### Note

The AFT pipeline is not intended for use in deploying resources, such as Amazon EC2
instances, that your accounts require to run your applications. It is intended solely
for automated provisioning and customizing of AWS Control Tower accounts.

## Video Walkthrough

This video (7:33) describes how to deploy accounts with AWS Control Tower Account Factory for
Terraform. For better viewing, select the icon at the lower right corner of the video to
enlarge it to full screen. Captioning is available.
