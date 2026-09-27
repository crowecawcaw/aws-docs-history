

# Zendesk
<a name="kb-managed-ds-zendesk"></a>

Zendesk is a cloud-based customer service platform that helps businesses manage support tickets, customer communication, and help center content in one place. You can connect your Zendesk instance as a data source for your managed knowledge base to crawl help center articles, including their attachments, and community posts.

**Important**  
Zendesk data sources don't support document-level access control lists (ACLs). All authenticated users who can query the knowledge base can see all crawled content.

## Supported features
<a name="kb-managed-supported-features-zendesk"></a>

With a Zendesk data source, you can use the following features:
+ Help center article crawling, including article attachments, and community post crawling
+ OAuth 2.0 Client Credentials (2LO) authentication
+ Scoping the crawl with article filters (category or section ID), community post filters (topic ID), and label filters

## Authentication method
<a name="kb-managed-zendesk-auth-methods"></a>

To connect a Zendesk data source, use OAuth 2.0 Client Credentials (2LO) authentication. You register an OAuth client in Zendesk, and the connector exchanges the client ID and client secret for an access token. There is no interactive sign-in or per-user consent step. The connector requests the `read` scope and crawls the content that the client can access. For setup steps, see [Set up OAuth 2.0 Client Credentials authentication for Zendesk](kb-managed-zendesk-oauth2-setup.md).

## Prerequisites
<a name="kb-managed-prereqs-zendesk"></a>

In Zendesk, make sure that you complete the following prerequisites:
+ Have a Zendesk Suite (Professional or Enterprise) account with admin access.
+ Have your Zendesk host URL (for example, `https://{{yoursubdomain}}.zendesk.com`). For multi-brand instances, use the subdomain for the specific brand that you want to sync.
+ Have an OAuth client created and configured for the connector to authenticate with. See [Set up OAuth 2.0 Client Credentials authentication for Zendesk](kb-managed-zendesk-oauth2-setup.md).

In your AWS account, make sure that you complete the following prerequisites:
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret.
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a Zendesk data source
<a name="kb-managed-zendesk-workflow"></a>

Setting up a Zendesk data source involves the following steps:

1. **Set up authentication.** Register and configure the OAuth client in Zendesk, and store the credentials in AWS. See [Set up OAuth 2.0 Client Credentials authentication for Zendesk](kb-managed-zendesk-oauth2-setup.md).

1. **Connect the data source.** Create the Zendesk data source in the knowledge base using the AWS Management Console or the API. See [Connect a Zendesk data source](kb-managed-ds-zendesk-connect.md).