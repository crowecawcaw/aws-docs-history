# Grant authorization and permissions

Authorization and permissions in WorkSpaces Core Managed Instances determine who deploys your WorkSpaces resources. IAM (Identity and Access
Management) controls permissions, allowing administrators to define specific roles and policies that govern user actions and resource access.

AWS recommends using IAM Roles for partners to get access to the customer’s environment. This avoids inputting long-term access keys and secrets
into external systems. For more information on how to set this up, refer to your partner specific guides.

## Customer and WorkSpaces Core Partnership

Customers must grant appropriate IAM permissions to the Core partner software to perform required AWS API calls. These include:

- Existing permissions already used in EC2-based partner integrations.
- New permissions to call the WorkSpaces Core APIs listed above.

## Required IAM permissions

The WorkspacesInstances APIs will be called using an IAM role or user credentials from the WorkSpaces Core partner’s account.
For more information, see [Identity and access management for WorkSpaces Instances](../ag/workspaces-access-control.md "../ag/workspaces-access-control.md")
in the _Amazon WorkSpaces Core Administration Guide_.
