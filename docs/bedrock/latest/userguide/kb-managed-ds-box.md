

# Box
<a name="kb-managed-ds-box"></a>

Box is a cloud content management and file sharing service for storing, sharing, and collaborating on files and folders. You can connect your Box enterprise as a data source for your managed knowledge base to crawl files and folders.

## Supported features
<a name="kb-managed-supported-features-box"></a>
+ Crawl files and folders
+ Automatic detection of common document fields (such as title, author, and created or modified dates)
+ Inclusion content filters for specific files and folders (OAuth 2.0 authentication)
+ Maximum file size filtering
+ Incremental content syncs for added, updated, and deleted content
+ Client Credentials Grant (2LO) and OAuth 2.0 (3LO) authentication
+ Document-level access control (ACLs), with Client Credentials Grant authentication

## Authentication methods
<a name="kb-managed-box-auth-methods"></a>

A Box data source supports two authentication methods. Choose one before you begin, because it determines the credentials you create and whether you can use document-level access control. We recommend Client Credentials Grant authentication for new data sources.


**Box authentication methods**  

| Method | How it authenticates | When to use | Setup | 
| --- | --- | --- | --- | 
| Client Credentials Grant (CCG) — recommended | The connector authenticates as a Box app using the Client Credentials Grant (2LO) flow, with enterprise-wide access. No user sign-in. | Crawling content across your Box enterprise, and any data source that uses document-level access control. | [Set up Client Credentials Grant authentication](kb-managed-box-ccg-setup.md) | 
| OAuth 2.0 (OAUTH2) | The connector authenticates as a Box app on behalf of a specific user (3LO), and crawls the content that user can access. | Crawling content for a specific user. Not supported with document-level access control. | [Set up OAuth 2.0 authentication](kb-managed-box-oauth2-setup.md) | 

## Prerequisites
<a name="kb-managed-prereqs-box"></a>

**In Box, make sure you**:
+ Create and configure a Box app for the connector to authenticate with. The app configuration depends on your authentication method — see the setup page for your method: [Set up Client Credentials Grant authentication for Box](kb-managed-box-ccg-setup.md) or [Set up OAuth 2.0 authentication for Box](kb-managed-box-oauth2-setup.md).

**In your AWS account, make sure you**:
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret.
+ For the exact key-value pairs to store in the secret, see the setup page for your authentication method: [Set up Client Credentials Grant authentication for Box](kb-managed-box-ccg-setup.md) or [Set up OAuth 2.0 authentication for Box](kb-managed-box-oauth2-setup.md).
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a Box data source
<a name="kb-managed-box-workflow"></a>

Setting up a Box data source involves the following steps:

1. **Set up authentication.** Follow the page for your chosen method to create the Box app credentials and store them in AWS: [Set up Client Credentials Grant authentication for Box](kb-managed-box-ccg-setup.md) or [Set up OAuth 2.0 authentication for Box](kb-managed-box-oauth2-setup.md).

1. **Connect the data source.** Create the Box data source in the knowledge base using the AWS Management Console or the API. See [Connect a Box data source](kb-managed-ds-box-connect.md).

1. **(Optional) Enable document-level access control.** Filter query results by each user's Box permissions. Requires Client Credentials Grant authentication. See [Document-level access controls](kb-managed-ds-box-acl.md).