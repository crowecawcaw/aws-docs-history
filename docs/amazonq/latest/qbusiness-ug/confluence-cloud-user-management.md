# How Amazon Q Business connector crawls Confluence (Cloud) ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect a Confluence (Cloud) data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Confluence (Cloud) instance. If you choose to activate ACL
crawling, the information can be used to filter chat responses based your end
users' document access level.

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
  space. The Confluence (Cloud) connector does not support crawling macros, whiteboards,
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
  For Confluence (Cloud) – The `_user_id` is the account ID of the
  user.

For more information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding User Store](connector-principal-store.md "connector-principal-store.md")
