# Use service accounts to authenticate with the

Grafana HTTP APIs

You can use a service account to run automated workloads in Grafana, such as
dashboard provisioning, configuration, or report generation. Create service accounts
and tokens to authenticate applications, such as Terraform, with the Grafana console
or the [Amazon Managed Grafana API](../APIReference/API_CreateWorkspaceServiceAccount.md "../APIReference/API_CreateWorkspaceServiceAccount.md").

###### Note

Service accounts are available in Grafana 9.x and newer, and are
replacing API keys as the primary way to authenticate applications
that interact with Grafana.

A common use case for creating a service account is to perform operations on
automated or triggered tasks. You can use service accounts to:

- Define alerts in your system to be used in Grafana
- Interact with Grafana without signing in as a user

###### Note

Each service account is considered a user for billing purposes.

## Service account tokens

A service account token is a generated string that acts as a key
to authenticate with Grafana’s HTTP API.

When you create a service account, you can associate one or more access tokens
with it. You can use service access tokens the same way as API Keys, for example
to access Grafana HTTP APIs programmatically.

You can create multiple tokens for the same service account. You might want to
do this if:

- multiple applications use the same permissions, but you would like
  to audit or manage their actions separately.
- you need to rotate or replace a compromised token.

Service account access tokens inherit permissions from the service
account.

Amazon Managed Grafana has a [quota](AMG_quotas.md "AMG_quotas.md") on the number of
service account tokens you can have at one time. This includes active and
expired tokens. You must delete tokens to remove them from your quota.

## Service account benefits

The added benefits of service accounts to API keys include:

- Service accounts resemble Grafana users and can be
  enabled/disabled, granted specific permissions, and remain active
  until they are deleted or disabled. API keys are only valid until
  their expiry date.
- Service accounts can be associated with multiple tokens.
- Unlike API keys, service account tokens are not associated with a
  specific user, which means that applications can be authenticated
  even if a Grafana user is deleted.
- You can grant permissions to service accounts in the same way that you
  grant permissions to users.

For more information about permissions, see [Using permissions](Grafana-permissions.md "Grafana-permissions.md").

## Creating a service account

###### Note

The user who creates a service account is also able to read,
update and delete the service account that they created, as well as
permissions associated with that service account.

**Prerequisite**

Ensure you have permission to create and edit service accounts. By default,
the organization administrator role is required to create and edit service
accounts. For more information about permissions, see [Using permissions](Grafana-permissions.md "Grafana-permissions.md").

###### To create a service account

1. Sign in to your Amazon Managed Grafana workspace and select
   **Administration** from the left-side menu.
2. Select **Service accounts**.
3. Select **Add service account**.
4. Enter a **Display name**.
5. The display name must be unique as it determines the ID
   associated with the service account.
   - We recommend that you use a consistent naming
     convention when you name service accounts. A
     consistent naming convention can help you scale and
     maintain service accounts in the future.
   - You can change the display name at any
     time.

6. Choose **Create**.

###### Note

You can also create service accounts using the Amazon Managed Grafana AWS APIs. Use
the [CreateWorkspaceServiceAccount](../APIReference/API_CreateWorkspaceServiceAccount.md "../APIReference/API_CreateWorkspaceServiceAccount.md") to create a service account
programmatically.

## Adding a token to a service

account

A service account token is a generated random string that acts as an
alternative to a password when authenticating with Grafana’s HTTP API.

**Prerequisite**

Ensure you have permission to create and edit service accounts. By default,
the organization administrator role is required to create and edit service
accounts. For more information about permissions, see [Using permissions](Grafana-permissions.md "Grafana-permissions.md").

###### To add a token to a service account

1. Sign in to your Grafana workspace and choose
   **Administration** in the left-side menu.
2. Expand the **Users and Access** menu.
3. Choose **Service accounts**.
4. Select the service account to which you want to add a
   token.
5. Choose **Add service account token**.
6. Enter a name for the token.
7. Select **Set expiration date** and
   enter an expiration date for the token.
   - The expiration date specifies how long you want the
     key to be valid.
   - You can set an expiration date up to 30 days in the
     future.
   - If you are unsure of an expiration date, we
     recommend that you set the token to expire after a
     short time, such as a few hours or less. This limits
     the risk associated with a token that is valid for a
     long time.

8. Choose **Generate token**.

###### Note

You can also create service account tokens using the Amazon Managed Grafana AWS
APIs. Use the [CreateWorkspaceServiceAccountToken](../APIReference/API_CreateWorkspaceServiceAccountToken.md "../APIReference/API_CreateWorkspaceServiceAccountToken.md") to create a service account
token programmatically.

## Delete a service token

When you are done with a service token, you must delete it to remove it from
your workspace. Expired, but not yet deleted, tokens count toward your [quota](AMG_quotas.md "AMG_quotas.md") of service account tokens.

**Prerequisite**

Ensure you have permission to create and edit service accounts. By default,
the organization administrator role is required to create and edit service
accounts. For more information about permissions, see [Using permissions](Grafana-permissions.md "Grafana-permissions.md").

###### To remove a token to a service account

1. Sign in to your Grafana workspace and choose
   **Administration** in the left-side menu.
2. Expand the **Users and Access** menu.
3. Choose **Service accounts**.
4. Select the service account from which you want to delete a
   token.
5. In the list of tokens, select the red icon with an
   **x** next to the service account token you wish to
   delete.
6. Select **Delete**.

Your token is deleted.

###### Note

You can also delete service account tokens using the Amazon Managed Grafana AWS
APIs. Use the [DeleteWorkspaceServiceAccountToken](../APIReference/API_DeleteWorkspaceServiceAccountToken.md "../APIReference/API_DeleteWorkspaceServiceAccountToken.md") to delete a service account
token programmatically.

## Assign roles to a service account

You can assign roles to a Grafana service account to control access for the
associated service account tokens. You can assign roles to a service account
using the Grafana UI or via the API.

**Prerequisite**

Ensure you have permission to create and edit service accounts. By default,
the organization administrator role is required to create and edit service
accounts. For more information about permissions, see [Using permissions](Grafana-permissions.md "Grafana-permissions.md").

###### To assign a role to a service account

1. Sign in to Grafana and choose
   **Administration** in the left-side menu.
2. Choose **Service accounts**.
3. Select the service account to which you want to assign a role.
   As an alternative, find the service account in the list
   view.
4. Assign a role using the role picker to update.
