# Confluence

Confluence is a collaborative work-management tool designed for sharing, storing, and working on
project planning, software development, and product management. Amazon Kendra supports both
Confluence Server/Data Center and Confluence Cloud. You can use Amazon Kendra to index the following
Confluence entities:

- **Spaces** – Top-level designated areas for organizing
  related content. Each space serves as a container, capable of holding multiple pages, blogs, and
  attachments.
- **Pages** – Individual documents within a space where
  users create and manage content. Pages can contain text, images, tables, and multimedia
  elements, and can have nested sub-pages. Each page is considered a single document.
- **Blogs** – Content similar to pages, typically used
  for updates or announcements. Each blog post is considered as a single document.
- **Comments** – Allows users to give feedback or engage
  in discussions on specific content within pages or blog posts.
- **Attachments** – Files uploaded to pages or blog posts
  in Confluence, such as images, documents, or other file types.
  By default, Amazon Kendra doesn't index Confluence archives and personal spaces. You can
  choose to index them when you create the data source. If you don't want Amazon Kendra to
  index a space, mark it private in Confluence.

You can connect Amazon Kendra to your Confluence data source using either the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md")
API, or the [ConfluenceConfiguration](../APIReference/API_ConfluenceConfiguration.md "../APIReference/API_ConfluenceConfiguration.md")
API.

Amazon Kendra has two versions of the Confluence connector. The following features are supported.

###### \*\*Confluence connector V2.0 / [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md")

API\*\*

- Field mappings
- User access control
- Inclusion/exclusion patterns
- Full and incremental content syncs
- Virtual private cloud (VPC)

###### \*\*Confluence connector V1.0 / [ConfluenceConfiguration](../APIReference/API_ConfluenceConfiguration.md "../APIReference/API_ConfluenceConfiguration.md")

API\*\* (no longer supported)

- Field mappings
- User access control
- Inclusion/exclusion filters
- (Confluence Server only) Virtual private cloud (VPC)

###### Note

Confluence connector V1.0 / ConfluenceConfiguration API ended in 2023. We recommend
migrating to or using Confluence connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Confluence data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [ACLs in Confluence Connector](#data-source-confluence-acls "#data-source-confluence-acls")
- [Confluence connector V2.0](data-source-v2-confluence.md "data-source-v2-confluence.md")
- [Confluence connector V1.0](data-source-v1-confluence.md "data-source-v1-confluence.md")

## ACLs in Confluence Connector

Connectors support crawling Access Control Lists (ACLs) and identifying information where
applicable based on the data source. If you index documents without ACLs, all documents are
considered public. Indexing documents with ACLs ensures data security.

The Amazon Kendra Confluence connector scans spaces to collect pages and blog posts along
with their ACLs. If there is no restriction applied on a page or blog, the connector inherits
permissions from its space. If specific user or group restriction is applied on a page, only
those users will be able to access that page. If page is nested, the nested page inherits the
permissions of parent page if no restrictions are applied. A similar permissions model applies to
blogs; however, Confluence does not support nested blogs.

In addition, Amazon Kendra Confluence connector crawls user principal information (local
user alias, local group and federated group identity configurations) and its permissions for each
configured space.

###### Note

The Confluence Cloud connector does not support crawling macros, whiteboards, or databases.

The Amazon Kendra Confluence connector updates ACL changes each time it crawls your data
source content. To ensure the correct users have access to the correct content, regularly re-sync
your data source to capture any ACL updates.
