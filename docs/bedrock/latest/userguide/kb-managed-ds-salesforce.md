

# Salesforce
<a name="kb-managed-ds-salesforce"></a>

Salesforce is a cloud-based customer relationship management (CRM) platform for managing support, sales, and marketing. You can connect your Salesforce org as a data source for your managed knowledge base to crawl Salesforce Knowledge articles, including their attachments, and documents.

## Supported features
<a name="kb-managed-supported-features-salesforce"></a>

With a Salesforce data source, you can use the following features:
+ Salesforce Knowledge article crawling, including article attachments, and document crawling
+ Archived Knowledge article crawling
+ OAuth 2.0 Client Credentials (2LO) and OAuth 2.0 JWT Bearer authentication
+ Scoping the crawl with a data category filter for Knowledge articles and a folder filter for documents
+ Maximum file size filtering
+ Document-level access control (ACLs), with OAuth 2.0 JWT Bearer authentication

## Authentication methods
<a name="kb-managed-salesforce-auth-methods"></a>

To connect a Salesforce data source, use OAuth 2.0 Client Credentials (2LO) authentication, which Salesforce calls the Client Credentials Flow. You register an External Client App in Salesforce and assign a dedicated Run-As integration user. The connector authenticates as the app and acts as that user, with no interactive sign-in. The Run-As user's permissions govern what the connector can crawl. For setup steps, see [Set up OAuth 2.0 Client Credentials authentication for Salesforce](kb-managed-salesforce-oauth2-setup.md).

To use document-level access control, use the `OAUTH2_WITH_JWT_BEARER` authentication type. The content crawl continues to use the Client Credentials Flow, and the connector also uses the OAuth 2.0 JWT Bearer Flow to check each querying user's access in Salesforce at query time. The `OAUTH2_WITH_JWT_BEARER` authentication type is available only when `aclEnabled` is `true`. Complete the Client Credentials setup first, and then see [Set up OAuth 2.0 JWT Bearer authentication for Salesforce document-level access controls](kb-managed-salesforce-jwt-bearer-setup.md).

## Prerequisites
<a name="kb-managed-prereqs-salesforce"></a>

In Salesforce, make sure that you complete the following prerequisites:
+ Have administrator access to the Salesforce org, with permission to create and manage External Client Apps.
+ Enable My Domain, which is required for the Client Credentials Flow. Your instance URL looks like `https://{{your-domain}}.my.salesforce.com`.
+ Have a dedicated integration user to assign as the Run-As user.
+ Have an External Client App created and configured for the connector to authenticate with. See [Set up OAuth 2.0 Client Credentials authentication for Salesforce](kb-managed-salesforce-oauth2-setup.md).
+ (Optional, for document-level access control) Configure the External Client App for the OAuth 2.0 JWT Bearer Flow. See [Set up OAuth 2.0 JWT Bearer authentication for Salesforce document-level access controls](kb-managed-salesforce-jwt-bearer-setup.md).

In your AWS account, make sure that you complete the following prerequisites:
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret.
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a Salesforce data source
<a name="kb-managed-salesforce-workflow"></a>

Setting up a Salesforce data source involves the following steps:

1. **Set up authentication.** Register and configure the External Client App in Salesforce, and store the credentials in AWS. See [Set up OAuth 2.0 Client Credentials authentication for Salesforce](kb-managed-salesforce-oauth2-setup.md).

1. **Connect the data source.** Create the Salesforce data source in the knowledge base using the AWS Management Console or the API. See [Connect a Salesforce data source](kb-managed-ds-salesforce-connect.md).

1. **(Optional) Enable document-level access control.** Filter query results by each user's Salesforce permissions. Requires OAuth 2.0 JWT Bearer authentication. See [Set up OAuth 2.0 JWT Bearer authentication for Salesforce document-level access controls](kb-managed-salesforce-jwt-bearer-setup.md) and [Document-level access controls](kb-managed-ds-salesforce-acl.md).