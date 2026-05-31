AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Setting up AWS Systems Manager Incident Manager

We recommend setting up AWS Systems Manager Incident Manager in the account that you use to manage your
operations. Before you use Incident Manager for the first time, complete the following
tasks:

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Required role for Incident Manager setup](#iam-prereq-service-role "#iam-prereq-service-role")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Required role for Incident Manager setup

Before you begin, your account must have the IAM permission
`iam:CreateServiceLinkedRole`. Incident Manager uses this permission to create
the `AWSServiceRoleforIncidentManager` in your account. For more information, see [Using service-linked roles for Incident Manager](using-service-linked-roles.md "using-service-linked-roles.md").
