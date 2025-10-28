# How Amazon Q Business connector

crawls GitHub Cloud ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

When you connect an GitHub Cloud data source to Amazon Q Business, Amazon Q Business crawls ACL information
attached to a document
(user and group information) from your GitHub instance. If you choose to activate ACL crawling, the information can
be used to filter chat responses to your end user's document access level.

GitHub Cloud's structure consists of repositories, teams, and projects. When you
connect a GitHub Cloud data source to Amazon Q Business, it crawls
GitHub Cloud repositories as defnied by your configuration, but it does not support
teams or projects, meaning data related to team structures, internal communications, and
project management is not retrieved. The child entities of repositories like Issues, Pull
Requests, Files, and Comments are crawled.

When you connect an GitHub Cloud data source to Amazon Q Business, Amazon Q Business makes a copy of these resources and creates an index that can be used to
respond to user prompts and queries. Additionally, Amazon Q crawls ACL
information attached to a document (user and group information) from your GitHub Cloud
instance. If you choose to activate ACL crawling, the information can be used to filter chat
responses to your end user's document access level.

**Roles/permissions**: GitHub Cloud has three roles:

- > Members - Default. Users with configurable repository and project
  > permissions
- Owners - Users with full administrative control. There should be at least two for
  continuity.
- Outside Collaborators - Users who have restricted access to private repositories
  with managed permissions
  The GitHub Cloud connector translates these roles into Amazon Q Business
  compatible ACLs, supporting View (Read), Edit, and Delete permissions. Since the lowest
  permission level is Read, more granular permissions beyond this do not impact data
  synchronization.

**Identity Crawling**: The connector supports both individual
user and group synchronization. For Users, it maps repository-specific members and outside
collaborators based on usernames, enforcing assigned GitHub Cloud permissions in
Amazon Q. For Groups, it treats each repository as a group and members as
organization group members. The connector retrieves ACL information for shared users based
on repository name.

**Permission Inheritance**: There are three types of
repositories:

- Public - Accessible to everyone; repositories inherit permissions from the
  organization.
- Private - Limited to the owner and explicitly granted collaborators. Does not
  inherit permissions from a parent. However, child entities such as Issues, Pull
  Requests, Files, and Comments inherit permissions from their parent repositories.
  When specific ACLs are definted, they replace the parent ACL.
- Internal - Accessible to all organization members but not to external users;
  repositories inherits permission from the organization
  **Change Management**: Change Log Mode captures and logs any
  updates to access control lists (ACLs). When a user is removed from a private repository or
  deactivated, they are automatically excluded from the access list, and these changes are
  recorded in the change log. Change Log Mode enables incremental updates by indexing only
  newly added, updated, or deleted content since the last crawl, preventing unnecessary
  re-indexing. Any modifications to user access or permissions are also captured, ensuring
  accurate and up-to-date indexing of GitHub Cloud content.

**Failure handling**: The connector implements a fail-close
approach, meaning that if there are permission-related issues or API failures, the document
is skipped from ingestion rather than being made publicly accessible.

For more
information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding
  User Store](connector-principal-store.md "connector-principal-store.md")
