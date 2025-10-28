# Known limitations for the Amazon Q Business SharePoint Server 2019 connector

The SharePoint Server 2019 connector has the following known limitations:

- The Amazon Q SharePoint connector supports custom field mappings only for the
  **Files** entity.
- For all SharePoint Server versions, the ACL token must be in lower case. For
  **Email with Domain from IDP** and **Email ID with
  Custom Domain** ACL, for example:
  `user@sharepoint2019.com`. For
  **Domain\User with Domain** ACL, for example:
  `sharepoint2013\user`.
- If an entity name has a `%` character in its name, the connector
  will skip these files due to API limitations.
- OneNote can only be crawled by the connector using a Tenant ID, and with OAuth
  2.0, OAuth 2.0 refresh token, or SharePoint App Only authentication activated
  for SharePoint Online.
- The connector crawls the first section of a OneNote document using its default
  name only, even if the document is renamed.
- The connector crawls links in SharePoint 2019 only if
  **Pages** and **Files** are selected as
  entities to be crawled in addition to **Links**.
- The connector crawls only list attachments and comments when **List
  Data** is selected as an entity to be crawled.
- The connector crawls event attachments only when **Events**
  is also selected as an entity to be crawled.
- To crawl nested groups using **Identity crawler**, you have
  to activate Local as well as AD Group Crawling.
- To use **Identity Crawler** with SharePoint Server 2019 to crawl
  nested groups, you have to enable both Local and AD Group Crawling.
- Query responses based on AD Group ACLs are not supported for
  SharePoint Server 2019. You need to add users and groups directly to your document
  permissions list.
- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to SharePoint Server 2019 API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
