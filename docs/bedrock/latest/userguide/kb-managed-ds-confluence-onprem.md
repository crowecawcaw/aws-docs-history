

# Confluence Data Center
<a name="kb-managed-ds-confluence-onprem"></a>

Atlassian Confluence is a collaborative work-management tool for sharing, storing, and working on documents and pages. You can connect your self-managed Confluence Server or Data Center instance as a data source for your managed knowledge base to crawl pages, blog posts, and their attachments. Because a Confluence Data Center instance runs on your own infrastructure, the connector reaches it over a private network path that you define with a VPC configuration.

**Note**  
To connect to a hosted Confluence Cloud (SaaS) instance instead, see [Confluence](kb-managed-ds-confluence.md).

**Important**  
Confluence Data Center data sources don't support document-level access control lists (ACLs). All authenticated users who can query the knowledge base can see all crawled content from Confluence Data Center.

## Supported features
<a name="kb-managed-supported-features-confluence-onprem"></a>

With a Confluence Data Center data source, you can use the following features:
+ Crawl pages, blog posts, and their attachments across spaces
+ Automatic detection of common document fields (such as title, author, and created or modified dates)
+ Inclusion content filters for spaces, pages, and blogs
+ Inclusion or exclusion content filters for MIME types
+ Incremental content syncs for added, updated, and deleted content
+ Basic and personal access token (PAT) authentication
+ Private connectivity to your instance through a VPC configuration

## Authentication methods
<a name="kb-managed-confluence-onprem-auth-methods"></a>

A Confluence Data Center data source supports two authentication methods. Choose one before you begin, because it determines the credentials you create and store in an AWS Secrets Manager secret.


**Confluence Data Center authentication methods**  

| Method | How it authenticates | 
| --- | --- | 
| Basic (BASIC) | The connector signs in with the username and password of a Confluence Data Center user. | 
| Personal access token (PERSONAL\_TOKEN) | The connector authenticates with a Confluence Data Center personal access token (PAT). | 

For setup steps for both methods, see [Set up Basic or PAT authentication for Confluence Data Center](kb-managed-confluence-onprem-auth-setup.md).

## Prerequisites
<a name="kb-managed-prereqs-confluence-onprem"></a>

**In Confluence, make sure you**:
+ Note your Confluence Data Center instance URL (for example, {{https://confluence.example.com}}). If your instance is hosted on a non-default path, note the application context path as well.
+ Make sure the instance is reachable over a private network path from your VPC, such as through an internal load balancer.

**In your AWS account, make sure you**:
+ Create a VPC configuration that reaches your Confluence Data Center instance. See [Configure VPC connectivity for a data source](kb-managed-vpc-configuration.md).
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret. For the exact key-value pairs, see [Set up Basic or PAT authentication for Confluence Data Center](kb-managed-confluence-onprem-auth-setup.md).
+ (Optional, for HTTPS) Store the TLS certificate for your Confluence Data Center instance in an Amazon S3 bucket if you connect over HTTPS.
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a Confluence Data Center data source
<a name="kb-managed-confluence-onprem-workflow"></a>

Setting up a Confluence Data Center data source involves the following steps:

1. **Set up VPC connectivity.** Create a VPC configuration that reaches your Confluence Data Center instance. See [Configure VPC connectivity for a data source](kb-managed-vpc-configuration.md).

1. **Set up authentication.** Create your credentials in Confluence and store them in AWS. See [Set up Basic or PAT authentication for Confluence Data Center](kb-managed-confluence-onprem-auth-setup.md).

1. **Connect the data source.** Create the Confluence Data Center data source in the knowledge base using the AWS Management Console or the API. See [Connect a Confluence Data Center data source](kb-managed-ds-confluence-onprem-connect.md).