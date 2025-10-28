# Setting up Parameter Store

Before setting up parameters in Parameter Store, a tool in AWS Systems Manager, first configure
AWS Identity and Access Management (IAM) policies that provide users in your account with permission to perform
the actions you specify.

This section includes information about how to manually configure these policies using
the IAM console, and how to assign them to users and user groups. You can also create
and assign policies to control which parameter actions can be run on a managed node.

This section also includes information about how to create Amazon EventBridge rules that let you
receive notifications about changes to Systems Manager parameters. You can also use EventBridge rules to
invoke other actions in AWS based on changes in Parameter Store.

###### Contents

- [Restricting access to Parameter Store parameters
  using IAM policies](sysman-paramstore-access.md "sysman-paramstore-access.md")
- [Managing parameter
  tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md")
- [Increasing or resetting Parameter Store
  throughput](parameter-store-throughput.md "parameter-store-throughput.md")
- [Setting up notifications or triggering
  actions based on Parameter Store events](sysman-paramstore-cwe.md "sysman-paramstore-cwe.md")
