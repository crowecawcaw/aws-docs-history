# Known limitations for the SharePoint (Online) connector

The SharePoint (Online) connector has the following known limitations:

- The Amazon Q SharePoint (Online) connector supports custom field
  mappings only for the [**Files**](sharepoint-cloud-field-mappings.md#sharepoint-field-mappings-files "sharepoint-cloud-field-mappings.md#sharepoint-field-mappings-files") entity.
- If an entity name has a `%` character in its name, the connector
  will skip these files due to API limitations.
- OneNote can only be crawled by the connector using a Tenant ID, and with OAuth
  2.0, OAuth 2.0 refresh token, or SharePoint (Online) App Only authentication
  activated for SharePoint (Online) Online.
- The connector crawls the first section of a OneNote document using its default
  name only, even if the document is renamed.
- The connector crawls event attachments only when **Events**
  is also selected as an entity to be crawled.
- The User Principal Name in your Azure Portal is a combination of upper case
  and lower case, the SharePoint (Online) API internally converts it to lower case.
  Because of this, the Amazon Q SharePoint (Online) connector sets ACL
  in lower case.

For example, if **User principal name** is
`MaryMajor@domain.com` in Azure portal, the ACL
token in the SharePoint Connector will be
`marymajor@domain.com`.

- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to SharePoint (Online) API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
- If you want to crawl nested groups using **Identity
  crawler**, you have to activate Local as well as AD Group
  Crawling.
- To use **Identity Crawler** with SharePoint (Online) to crawl
  nested groups, you have to enable both Local and AD Group Crawling.
- Query responses based on AD Group ACLs are not supported for
  SharePoint (Online). You need to add users and groups directly to your document
  permissions list.
- Microsoft requires granting the "Sites.FullControl.All" permission to the
  application in order to ingest the source ACLs from SharePoint
