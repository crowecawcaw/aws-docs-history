# Microsoft OneDrive

Microsoft OneDrive is a cloud storage service that lets you store, share, and
collaborate on files. You can connect your OneDrive for Business instance as a data source
for your managed knowledge base to crawl the personal drives of users in your Microsoft 365
tenant.

## Supported features

- Crawl users' personal drives. The set of drives crawled depends on the authentication method — see [Authentication methods](#kb-managed-onedrive-auth-methods "#kb-managed-onedrive-auth-methods").
- Automatic detection of common document fields (such as title, author, and created or modified dates)
- Inclusion and exclusion content filters using user email addresses, drive item paths, MIME types, and date ranges
- Incremental content syncs for added, updated, and deleted content
- User-managed (3LO), Microsoft Entra App ID, and OAuth 2.0 authentication
- Document-level access control (ACLs), with Microsoft Entra App ID authentication

###### Note

OneNote notebooks are not currently supported.

## Authentication methods

A OneDrive data source supports three authentication methods. Choose one before you begin, because it determines the credentials you create and whether you can use document-level access control. We recommend Microsoft Entra App ID authentication for new data sources.

OneDrive authentication methods| Method | How it authenticates | When to use | Setup |
| --- | --- | --- | --- |
| User-managed (3LO) (`MANAGED_OAUTH2`) | You sign in to OneDrive directly to authorize the connection, and Amazon Bedrock Managed Knowledge Base handles authentication. This is the simplest way to get started. | Getting started quickly, when you do not need document-level access control. Not supported with document-level access control. | [User-managed setup (3LO)](kb-managed-onedrive-3lo-setup.md "kb-managed-onedrive-3lo-setup.md") |
| Microsoft Entra App ID (`ENTRA_APP_ID`) — recommended | A Microsoft Entra application authenticates with an application client ID and secret, using the OAuth 2.0 client-credentials (application-only) flow. No user sign-in. When document-level access control is enabled, the application additionally authenticates to SharePoint with a certificate. | Most data sources, and any data source that uses document-level access control. | [Set up Entra App ID authentication](kb-managed-onedrive-entra-setup.md "kb-managed-onedrive-entra-setup.md") |
| OAuth 2.0 (`OAUTH2`) | An application client ID and secret together with a delegated refresh token that you obtain through a user sign-in. The connector uses the refresh token to obtain access tokens for crawling. | Use when a single Microsoft 365 user has access to all the OneDrive content you want to crawl — their own drive, plus any drives shared with them or where they have SharePoint admin access. Microsoft Entra App ID authentication is required to crawl every user's OneDrive in your tenant uniformly. | [Set up OAuth 2.0 authentication](kb-managed-onedrive-oauth2-setup.md "kb-managed-onedrive-oauth2-setup.md") |

###### Important

The `OAUTH2` method requires a refresh token. Refresh tokens have a finite Microsoft-side lifetime and must be re-minted before they expire. `OAUTH2` also does not support document-level access control. Use Microsoft Entra App ID authentication if you need document-level access control or you need to crawl every user's OneDrive in your tenant.

## Prerequisites

**In Microsoft 365, make sure you**:

- Copy your Microsoft 365 tenant ID. You can find your tenant ID in the
  Properties of your Microsoft Entra portal. For details, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id "https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id") on the Microsoft Learn website.

**In your AWS account, make sure you**:

- Store your authentication credentials in an [AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md")
  and note the Amazon Resource Name (ARN) of the secret.
- For the exact key-value pairs to store in the secret, see the setup page for
  your authentication method: [Set up Microsoft Entra App ID authentication for OneDrive](kb-managed-onedrive-entra-setup.md "kb-managed-onedrive-entra-setup.md") or [Set up OAuth 2.0 authentication for OneDrive](kb-managed-onedrive-oauth2-setup.md "kb-managed-onedrive-oauth2-setup.md").
- Include the necessary permissions to connect to your data source in your
  AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For
  information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds "kb-permissions.md#kb-permissions-access-ds").

## How to set up a OneDrive data source

Setting up a OneDrive data source involves the following steps:

1. **Set up authentication.** Follow the page for your chosen method. With user-managed setup (3LO), you sign in to OneDrive directly — see [User-managed setup (3LO)](kb-managed-onedrive-3lo-setup.md "kb-managed-onedrive-3lo-setup.md"). For the other methods, you register a Microsoft Entra application, configure permissions, and store your credentials in AWS — see [Set up Microsoft Entra App ID authentication for OneDrive](kb-managed-onedrive-entra-setup.md "kb-managed-onedrive-entra-setup.md") or [Set up OAuth 2.0 authentication for OneDrive](kb-managed-onedrive-oauth2-setup.md "kb-managed-onedrive-oauth2-setup.md").
2. **Connect the data source.** Create the OneDrive data source in the knowledge base using the AWS Management Console or the API. See [Connect a OneDrive data source](kb-managed-ds-onedrive-connect.md "kb-managed-ds-onedrive-connect.md").
3. **(Optional) Enable document-level access control.** Filter query results by each user's OneDrive permissions. See [Document-level access controls](kb-managed-ds-onedrive-acl.md "kb-managed-ds-onedrive-acl.md").

If you run into problems during setup or syncing, see [Troubleshoot a OneDrive data source](kb-managed-ds-onedrive-troubleshooting.md "kb-managed-ds-onedrive-troubleshooting.md").
