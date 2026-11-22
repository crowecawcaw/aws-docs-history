

# Dropbox

Dropbox is a cloud file storage and collaboration platform. You can connect a Dropbox account or a Dropbox team as a data source for your managed knowledge base to crawl files and Dropbox Paper documents.

## Supported features
<a name="kb-managed-supported-features-dropbox"></a>

With a Dropbox data source, you can use the following features:
+ File and Dropbox Paper document crawling. Paper documents are exported as HTML.
+ Two authentication types: a single user's Dropbox (`OAUTH2`), or a whole Dropbox team through a team-linked app (`TEAM_ADMIN`)
+ For team crawls, choosing which content to crawl: members' folders (including folders shared with them) and team folders
+ Scoping the crawl with folder path filters, team member filters, MIME type filters, modified date filters, and a maximum file size
+ Document-level access control, using access control lists (ACLs), for team crawls (`TEAM_ADMIN` only)

## Authentication methods
<a name="kb-managed-dropbox-auth-methods"></a>

The Dropbox connector authenticates with an OAuth 2.0 refresh token that you obtain by authorizing your own Dropbox app once, with offline access. You store the app key, app secret, and refresh token in an AWS Secrets Manager secret. On every sync, the connector exchanges the refresh token for a short-lived access token. AWS does not host a consent page or a redirect URL for this step.

You choose one of the following authentication types when you create the data source.


**Dropbox authentication types**  

| Authentication type | Who authorizes the app | What the connector crawls | Document-level access control | 
| --- | --- | --- | --- | 
| OAUTH2 | Any Dropbox user | That user's own Dropbox | Not supported | 
| TEAM\_ADMIN | A Dropbox team admin, granting team scopes | Content across the Dropbox team: members' folders (including folders shared with them) and team folders | Supported | 

Both types use the same secret fields. For setup steps, see [Set up authentication for Dropbox](kb-managed-dropbox-auth-setup.md).

## Prerequisites
<a name="kb-managed-prereqs-dropbox"></a>

In Dropbox, make sure that you complete the following prerequisites:
+ For `OAUTH2`, have a Dropbox account whose content you want to crawl.
+ For `TEAM_ADMIN`, have a Dropbox team plan (such as Business, Business Plus, Advanced, or Enterprise) and a team admin who can authorize an app with team scopes.
+ Have a scoped-access Dropbox app created in the [Dropbox App Console on the Dropbox website](https://www.dropbox.com/developers/apps), with the required scopes granted and a refresh token issued. See [Set up authentication for Dropbox](kb-managed-dropbox-auth-setup.md).

In your AWS account, make sure that you complete the following prerequisites:
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret.
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a Dropbox data source
<a name="kb-managed-dropbox-workflow"></a>

Setting up a Dropbox data source involves the following steps:

1. **Set up authentication.** Create and authorize the Dropbox app, and store the credentials in AWS. See [Set up authentication for Dropbox](kb-managed-dropbox-auth-setup.md).

1. **Connect the data source.** Create the Dropbox data source in the knowledge base using the AWS Management Console or the API. See [Connect a Dropbox data source](kb-managed-ds-dropbox-connect.md).

1. **(Optional) Enable document-level access control.** For team crawls, filter query results by each user's Dropbox permissions. See [Document-level access controls](kb-managed-ds-dropbox-acl.md).

If you run into issues, see [Troubleshoot a Dropbox data source](kb-managed-ds-dropbox-troubleshooting.md).