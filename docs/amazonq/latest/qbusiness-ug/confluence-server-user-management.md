# How Amazon Q Business connector

crawls Confluence (Server/Data Center) ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect a Confluence (Server/Data Center) data source to Amazon Q Business,
Amazon Q crawls ACL information attached to a document (user and group information)
from your Confluence (Server/Data Center) instance. If you choose to activate ACL crawling, the
information can be used to filter chat responses based on your end users' document
access level.

The connector crawls the following Confluence resources:

- **Spaces** – A collection of related
  pages, blogs, and attachments. Space permissions apply to all documents in the
  space by default.
- **Pages** – Documents in a space where
  users create and manage content. Pages can contain text, images, tables, and
  multimedia elements, and can have nested pages. Each page is considered a single
  document. Pages can be restricted to specific users and groups in the space. A
  nested page inherits restrictions from the parent page, and can have its own
  restrictions.
- **Blogs** – Content similar to pages,
  typically used for updates or announcements. Each blog post is considered as a
  single document. Blogs can be restricted to specific users and groups in the
  space.
- **Comments** – Feedback and discussions on
  pages or blog post content. Comments are visible to viewers of the page or
  post.
- **Attachments** – Files uploaded to pages
  or blog posts, such as images and documents.
  The connector also crawls user principal information (local user alias, local group
  and federated group identity configurations) and its permissions for each configured
  space. The Confluence (Server/Data Center) connector does not support crawling macros, whiteboards,
  or databases.

The connector updates ACL changes each time it crawls your data source content. To
ensure that the correct users have access to the correct content, regularly re-sync your
data source to capture any ACL updates.

You configure user and group access to spaces using the space permissions page. For
pages and blogs, you use the restrictions page. For more information about space
permissions, see [Space Permissions Overview](https://confluence.atlassian.com/doc/space-permissions-overview-139521.html "https://confluence.atlassian.com/doc/space-permissions-overview-139521.html") on the Confluence Support website. For more
information about page and blog restrictions, see [Page
Restrictions](https://confluence.atlassian.com/doc/page-restrictions-139414.html "https://confluence.atlassian.com/doc/page-restrictions-139414.html") on the Confluence Support website.

###### Important

For user context filtering to work correctly, users' visibility must be set to
**Anyone**. For more information, see [Set your email visibility](https://support.atlassian.com/confluence-cloud/docs/configure-user-email-visibility/ "https://support.atlassian.com/confluence-cloud/docs/configure-user-email-visibility/") in Atlassian Developer Documentation.

The group and user IDs are mapped as follows:

- `_group_ids` – Group names are present on spaces, pages, and
  blogs where there are restrictions. They're mapped from the name of the group in
  Confluence . Group names are always lower case.
- `_user_id` – User names are present on the space, page, or
  blog where there are restrictions. They're mapped depending on the type of
  Confluence instance that you are using.
- For Confluence (Server/Data Center) – The `_user_id` is the user key of
  the user.

###### Important

To maintain secure access control for Amazon Q Business, each user must have
a unique email address across all connected data sources.

In Confluence Data Center users can share an email address while having a
different application-specific unique identifier. However, in Amazon Q Business email addresses act as unique identifiers.

This means that if a document is shared with a particular user (for example,
arnav\_desai@example.com who is part of pentesters@example.com) on the basis of an
application-specific unique ID, every other user who shares pentesters@example.com
(for example, xiulan\_wang@example.com and efua\_owusu@example.com, both of whom are
part of pentesters@example.com) can receive Amazon Q Business responses with
content from a document that was shared only with Arnav. Similarly, content created
by Arnav that only he should be able to access via Amazon Q Business chat
responses, could also be part of Amazon Q Business chat responses for Xiulan
and Efua, because they share the same email address.

For
more information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding User Store](connector-principal-store.md "connector-principal-store.md")
