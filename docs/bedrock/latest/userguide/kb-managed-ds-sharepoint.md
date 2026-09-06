

# Microsoft SharePoint
<a name="kb-managed-ds-sharepoint"></a>

Microsoft SharePoint is a collaborative web-based service for working on documents, web pages, web sites, lists, and more. You can connect your SharePoint Online instance as a data source for your managed knowledge base to crawl files and pages from one or more SharePoint sites.

## Supported features
<a name="kb-managed-supported-features-sharepoint"></a>
+ Crawl files and pages from multiple SharePoint sites
+ Automatic detection of common document fields (such as title, author, and created or modified dates)
+ Inclusion content filters using item paths and date ranges
+ Incremental content syncs for added, updated, and deleted content
+ User-managed (3LO), Microsoft Entra ID App-Only, and OAuth 2.0 authentication
+ Document-level access control (ACLs), with Microsoft Entra ID App-Only authentication

## Use cases and required permissions
<a name="kb-managed-sharepoint-use-cases"></a>

The Microsoft permissions the connector needs depend on your use case. You don't have to grant broad, tenant-wide access unless your use case calls for it — the connector supports least-privilege configurations that limit access to only the sites you choose. Two choices determine which permissions you assign:
+ **Which sites to crawl** — Grant access to only the sites you explicitly choose (`Sites.Selected`, the least-privilege option) or to all SharePoint sites in your tenant (**all sites**).
+ **Whether to enable document-level access control (ACLs)** — Decide whether the data source filters query results by each user's SharePoint permissions. ACL crawling requires additional Microsoft Graph and SharePoint permissions.

These choices combine into four common use cases. The permissions below apply to the recommended Microsoft Entra ID App-Only authentication method; grant only the permissions listed for your use case. The connector authenticates to two Microsoft resources: **Microsoft Graph** (to enumerate sites and, for ACLs, to resolve users and groups) and the **SharePoint** REST API (to read site content and, for ACLs, item-level permissions). For the full setup procedure, see [Set up Microsoft Entra ID App-Only authentication for SharePoint](kb-managed-sharepoint-entra-setup.md).

Select the tab for your use case to see the exact Microsoft Graph and SharePoint permissions to assign.

------
#### [ Sites.Selected, no ACLs ]

**Use this when** you want to crawl only specific sites you choose, without filtering query results by each user's SharePoint permissions. This is the least-privilege configuration.


**Sites.Selected, content only**  

| API | Permission | Purpose | 
| --- | --- | --- | 
| Microsoft Graph | Sites.Selected | Access only the sites you explicitly grant (Microsoft Graph). | 
| SharePoint | Sites.Selected | Access only the sites you explicitly grant (SharePoint REST). Grant the read role per site. | 

------
#### [ Sites.Selected, with ACLs ]

**Use this when** you want to crawl only specific sites you choose and filter query results by each user's SharePoint permissions.


**Sites.Selected, with ACLs**  

| API | Permission | Purpose | 
| --- | --- | --- | 
| Microsoft Graph | Sites.Selected | Access only the sites you explicitly grant (Microsoft Graph). | 
| Microsoft Graph | User.Read.All | Resolve users for document-level ACLs. | 
| Microsoft Graph | GroupMember.Read.All | Resolve group membership for document-level ACLs. | 
| SharePoint | Sites.Selected | Access only the sites you explicitly grant. Grant the fullcontrol role per site (required to read item-level permissions for ACLs). | 

------
#### [ All sites, no ACLs ]

**Use this when** you want to crawl all SharePoint sites in your tenant, without filtering query results by each user's SharePoint permissions.


**All sites, content only**  

| API | Permission | Purpose | 
| --- | --- | --- | 
| Microsoft Graph | Sites.Read.All | Enumerate and read all SharePoint sites. | 
| SharePoint | Sites.Read.All | Read site content through the SharePoint REST API. | 

------
#### [ All sites, with ACLs ]

**Use this when** you want to crawl all SharePoint sites in your tenant and filter query results by each user's SharePoint permissions.


**All sites, with ACLs**  

| API | Permission | Purpose | 
| --- | --- | --- | 
| Microsoft Graph | Sites.Read.All | Enumerate and read all SharePoint sites. | 
| Microsoft Graph | User.Read.All | Resolve users for document-level ACLs. | 
| Microsoft Graph | GroupMember.Read.All | Resolve group membership for document-level ACLs. | 
| SharePoint | Sites.FullControl.All | Read item-level permissions for ACL crawling and verify access at query time. Sites.Read.All is not sufficient for this check. | 

------

**Note**  
`Sites.FullControl.All` grants broad access to every site in the tenant. If your organization requires least privilege, use `Sites.Selected` and grant per-site access. For the per-site grant steps, see [Set up Microsoft Entra ID App-Only authentication for SharePoint](kb-managed-sharepoint-entra-setup.md).

## Authentication methods
<a name="kb-managed-sharepoint-auth-methods"></a>

A SharePoint data source supports three authentication methods. Choose one before you begin, because it determines the credentials you create and whether you can use document-level access control. We recommend Microsoft Entra ID App-Only authentication for new data sources.


**SharePoint authentication methods**  

| Method | How it authenticates | When to use | Setup | 
| --- | --- | --- | --- | 
| User-managed (3LO) (MANAGED\_OAUTH2) | You sign in to SharePoint directly to authorize the connection, and Amazon Bedrock Managed Knowledge Base handles authentication. This is the simplest way to get started. | Getting started quickly, when you do not need document-level access control. Not supported with document-level access control. | [User-managed setup (3LO)](kb-managed-sharepoint-3lo-setup.md) | 
| Microsoft Entra ID App-Only (ENTRA\_ID\_APP\_ONLY) — recommended | A Microsoft Entra application authenticates with a certificate. No user credentials and no interactive sign-in. | Most data sources, and any data source that uses document-level access control. | [Set up Entra ID App-Only authentication](kb-managed-sharepoint-entra-setup.md) | 
| OAuth 2.0 (OAUTH2\_APP) | An application client ID and secret, plus the user name and password of a Microsoft 365 user account that has access to the sites you want to crawl (the resource-owner password credentials, or ROPC, flow). | Use only if you cannot use Microsoft Entra ID App-Only authentication. The account must not require MFA or Conditional Access. Not supported with document-level access control. | [Set up OAuth 2.0 authentication](kb-managed-sharepoint-oauth2-setup.md) | 

**Important**  
The `OAUTH2_APP` method signs in with a user name and password, so it cannot complete a multi-factor authentication (MFA) challenge or satisfy a Conditional Access policy that requires one. If the account enforces MFA or Conditional Access, authentication fails and the data source cannot sync. Use Microsoft Entra ID App-Only authentication unless you have a specific reason to use `OAUTH2_APP`.

## Prerequisites
<a name="kb-managed-prereqs-sharepoint"></a>

**In Microsoft SharePoint, make sure you**:
+ Note the URLs of the SharePoint sites you want to crawl. Each URL is a crawl entry point and must start with `https://` and point to a site, team site, or personal site — the path must begin with `/sites/`, `/teams/`, or `/personal/` followed by the site name (for example, {{https://yourdomain.sharepoint.com/sites/mysite}}). Standard `*.sharepoint.com` domains and custom (vanity) domains are both supported. Within each site, the connector crawls files and pages; you can narrow the crawl to specific items with item path filters when you connect the data source.
+ Copy your Microsoft 365 tenant ID. You can find your tenant ID in the Properties of your Microsoft Entra portal. For details, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id) on the Microsoft Learn website.

**In your AWS account, make sure you**:
+ Store your authentication credentials in an [AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) and note the Amazon Resource Name (ARN) of the secret.
+ For the exact key-value pairs to store in the secret, see the setup page for your authentication method: [Set up Microsoft Entra ID App-Only authentication for SharePoint](kb-managed-sharepoint-entra-setup.md) or [Set up OAuth 2.0 authentication for SharePoint](kb-managed-sharepoint-oauth2-setup.md).
+ Include the necessary permissions to connect to your data source in your AWS Identity and Access Management (IAM) role/permissions policy for your knowledge base. For information on the required permissions, see [Permissions to access your data sources](kb-permissions.md#kb-permissions-access-ds).

## How to set up a SharePoint data source
<a name="kb-managed-sharepoint-workflow"></a>

Setting up a SharePoint data source involves the following steps:

1. **Set up authentication.** Follow the page for your chosen method. With user-managed setup (3LO), you sign in to SharePoint directly — see [User-managed setup (3LO)](kb-managed-sharepoint-3lo-setup.md). For the other methods, you register a Microsoft Entra application, configure permissions, and store your credentials in AWS — see [Set up Microsoft Entra ID App-Only authentication for SharePoint](kb-managed-sharepoint-entra-setup.md) or [Set up OAuth 2.0 authentication for SharePoint](kb-managed-sharepoint-oauth2-setup.md).

1. **Connect the data source.** Create the SharePoint data source in the knowledge base using the AWS Management Console or the API. See [Connect a SharePoint data source](kb-managed-ds-sharepoint-connect.md).

1. **(Optional) Enable document-level access control.** Filter query results by each user's SharePoint permissions. See [Document-level access controls](kb-managed-ds-sharepoint-acl.md).

If you run into problems during setup or syncing, see [Troubleshoot a SharePoint data source](kb-managed-ds-sharepoint-troubleshooting.md).