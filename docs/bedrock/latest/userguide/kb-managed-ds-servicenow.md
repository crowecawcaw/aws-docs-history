

# ServiceNow
<a name="kb-managed-ds-servicenow"></a>

ServiceNow is a cloud-based platform for IT service management, knowledge management, and service catalogs. You can connect your ServiceNow instance as a data source for your managed knowledge base to crawl knowledge articles and service catalog items.

**Important**  
ServiceNow data sources don't support document-level access control lists (ACLs). All authenticated users who can query the knowledge base can see all crawled content.

## Supported features
<a name="kb-managed-supported-features-servicenow"></a>

With a ServiceNow data source, you can use the following features:
+ Knowledge article (`kb_knowledge`) and service catalog item (`sc_cat_item`) crawling, including attachments
+ Automatic detection of common document fields (such as title and author)
+ Incremental content syncs for added, updated, and deleted content, based on the `sys_updated_on` timestamp
+ OAuth 2.0 Client Credentials (2LO) authentication

## Authentication method
<a name="kb-managed-servicenow-auth-methods"></a>

To connect a ServiceNow data source, use OAuth 2.0 Client Credentials (2LO) authentication. The connector uses a dedicated ServiceNow service account with no interactive sign-in. It crawls all published knowledge articles and active catalog items that the account can access. For setup steps, see [Set up OAuth 2.0 Client Credentials authentication for ServiceNow](kb-managed-servicenow-oauth2-setup.md).

## Prerequisites
<a name="kb-managed-prereqs-servicenow"></a>

In ServiceNow, make sure that you complete the following prerequisites:
+ Have a ServiceNow instance running any release with OAuth 2.0 and Table API support, reachable from AWS.
+ Have a ServiceNow user account with the `admin` role to create the OAuth application, assign roles, and configure API access policies.
+ Have a dedicated service account and OAuth application created and configured for the connector to authenticate with. See [Set up OAuth 2.0 Client Credentials authentication for ServiceNow](kb-managed-servicenow-oauth2-setup.md).

In your AWS account, make sure that you complete the following prerequisites:
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret.
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a ServiceNow data source
<a name="kb-managed-servicenow-workflow"></a>

Setting up a ServiceNow data source involves the following steps:

1. **Set up authentication.** Configure the service account and OAuth application in ServiceNow, and store the credentials in AWS. See [Set up OAuth 2.0 Client Credentials authentication for ServiceNow](kb-managed-servicenow-oauth2-setup.md).

1. **Connect the data source.** Create the ServiceNow data source in the knowledge base using the AWS Management Console or the API. See [Connect a ServiceNow data source](kb-managed-ds-servicenow-connect.md).

If you run into issues, see [Troubleshoot a ServiceNow data source](kb-managed-ds-servicenow-troubleshooting.md).