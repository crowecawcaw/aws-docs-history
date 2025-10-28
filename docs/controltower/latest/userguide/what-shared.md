# What are the shared accounts?

In AWS Control Tower, the shared accounts in your landing zone are provisioned
during setup: the management account, the log archive account, and the audit
account.

## What is the management account?

This is the account that you created specifically for your landing zone. This account
is used for billing for everything in your landing zone. It's also used for Account Factory
provisioning of accounts, as well as to manage OUs and controls.

###### Note

It is not recommended to run any type of production workloads from an AWS Control Tower
management account. Create a separate AWS Control Tower account to run your workloads.

For more information, see [Management account](special-accounts.md#mgmt-account "special-accounts.md#mgmt-account").

## What is the log archive account?

This account works as a repository for logs of API activities and resource
configurations from all accounts in the landing zone.

For more information, see [Log archive account](special-accounts.md#log-archive-account "special-accounts.md#log-archive-account").

## What is the audit account?

The audit account is a restricted account that's designed to give your security
and compliance teams read and write access to all accounts in your landing zone. From the
audit account, you have programmatic access to review accounts, by means of a role
that is granted to Lambda functions only. The audit account does not allow you to
log in to other accounts manually. For more information about Lambda functions and
roles, see [Configure a Lambda function to assume a role from another AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role").

For more information, see [Audit account](special-accounts.md#audit-account "special-accounts.md#audit-account").
