# How Amazon Q Business connector crawls Jira ACLs

Connectors support crawling ACL and identity information where applicable based on the data source.
If you index documents without ACLs, all documents are considered public.
Indexing documents with ACLs ensures data security.

Amazon Q Business supports crawling ACLs for document security by default.

Jira organizes work into Projects, which serve as containers for Issues—the
core tasks, bugs, or stories that teams track. Each issue belongs to a project and can have
Comments, Attachments, and Worklogs to facilitate collaboration, provide context, and track
time spent. Projects can be Team-Managed (private, limited, or open) or Company-Managed,
offering flexibility in workflows and permissions. When you connect an Jira
data source to Amazon Q Business, Amazon Q Business crawls ACL information
attached to a document (user and group information) from your Jira instance.
If you choose to activate ACL crawling, the information can be used to filter chat responses
to your end user's document access level.

## Projects

Jira organizes work into Projects, which serve as containers for
Issues—the core tasks, bugs, or stories that teams track. Each issue belongs to a
project and can have Comments, Attachments, and Worklogs to facilitate collaboration,
provide context, and track time spent. Projects can be Team-Managed (private, limited,
or open) or Company-Managed, offering flexibility in workflows and permissions. When you
connect an Jira data source to Amazon Q Business, Amazon Q Business crawls ACL information attached to a document (user and group
information) from your Jira instance. If you choose to activate ACL
crawling, the information can be used to filter chat responses to your end user's
document access level.

## Identity crawling

The Jira connector extracts project-level permissions based on the
project key. It identifies direct users and group members, capturing their account IDs
and emails. Federated groups, synchronized from external identity providers, appear as
local groups in Jira but are managed externally. The connector respects
Jira’s permission structure, ensuring that permissions remain intact even
when users are removed and later reinstated. Suspended users are included in API
responses but marked as inactive, preventing unauthorized access.

###### Note

For all types of projects, you must have at least 'Browse Projects' permissions
(direct or indirect), and Email visibility must be set to "Anyone" for AWS to
validate permissions correctly. The "Anyone" email visibility setting is required
for proper integration with AWS and other third-party tools due to
Jira's API limitations.

## Permissions inheritance

Global Permissions determine who can access the Jira instance and
perform high-level actions. Project Permissions, governed by permission schemes, define
user access within projects, such as viewing, editing, or assigning issues. In
Company-Managed projects, permissions flow from the Jira instance down to
projects and further to issues, attachments, comments, and worklogs. Issue Security
Schemes further restrict access to specific issues within a project. In Team-Managed
projects, access is defined by project roles and project visibility settings:
**Open** (accessible to all), **Limited**
(viewable by all but editable only by members), and **Private**
(restricted to project members). While permissions in Company-Managed projects follow a
structured hierarchy, Team-Managed projects rely on role-based access. Inheritance
applies at the project level, meaning that issues, comments, attachments, and worklogs
inherit permissions from their parent project. However, Issue Security Levels can
override project permissions by restricting visibility at an issue level.

## ACL mapping

Before enabling ACL-based document access for Jira within Amazon Q Business, it is important to understand how permissions and groups are mapped
between Jira and Amazon Q, especially given the structural
differences between Team-Managed and Company-Managed projects.

**Team-Managed Projects**: For Team-Managed projects in
Jira Software Cloud, ACL mapping is straightforward. The permissions for
such projects are configured on the **Project Settings > Access** tab,
where you will find a list of users and groups along with their associated project
roles. For these projects, a single group is created in Amazon Q Business using
the format `projectKey:[ProjectKey]` (for example,
`projectKey:TestProject`). This group is attached to all documents under
the project, including the project-level document, issues, comments, worklogs, and
attachments. All users listed in the **Access** tab will have
visibility into all project documents, regardless of their roles.

**Company-Managed Projects**: Company-Managed projects
offer more granular access control and therefore require a more complex mapping
strategy. To determine document visibility, it is necessary to review two areas within
the Jira project:

- **Project Settings > People**, which lists users and groups
  along with their project roles. Inclusion in this list does not guarantee
  document access even for Administrator roles.
- **Project Settings > Permissions** The **Browse
  Projects** permission governs who can view the project and its
  issues. This setting can include a variety of grant types, such as specific
  groups, project roles, individual users, or dynamic conditions like issue
  assignees. Ensure users have all necessary permissions listed in [Prerequisites](jira-prereqs.md "jira-prereqs.md").

Jira also supports issue-level security, which can override the broader
**Browse Projects** settings by enforcing granular access rules on
a per-issue basis. You need to consider this label during ACL mapping.

Following is an example of how group mappings in Amazon Q Business for
Company-Managed projects are established:

- **Project**: A group named
  `TestProject` is created, comprising all users who have been
  granted **Browse Projects** permission, regardless of grant
  type.
- **Issue-Level Document**: In the example issue
  `Test1`, group assignments depend on permissions:
- - If a user gains access through project-level permissions, the group
    `ProjectBasedBrowseKey:Test` is used.
  - If access is granted through dynamic conditions such as the user being
    the assignee, the group `IssueBasedBrowseKey:Test1` is
    used.
  - If both types of access mechanisms exist, users may belong to both
    groups.
- **Issue with Issue-Level Security Enabled**:
  Access requires both project/issue-based browse permissions and issue-specific
  security clearance. The condition becomes: `(ProjectBasedBrowseKey:Test OR
IssueBasedBrowseKey:Test1) AND IssueLevelKey:Test1`.
- **Comments, Attachments, and Worklog**s: These
  documents inherit the same access control as the associated issue. Therefore,
  the same issue-level logic applies..

## Change management

Change Log Mode in Amazon Q Business enables incremental updates by capturing
modifications made to content in Jira. Instead of re-indexing all
documents, it indexes only newly added, updated, or deleted items since the last crawl.
Any changes to user or group access permissions are also recorded, ensuring accurate and
up-to-date indexing.

## Failure handling

The Jira connector follows a fail-close approach, skipping documents
from ingestion in case of API failures or permission-related issues. If a document has
no ACLs attached and ACL enforcement is enabled by the admin, it will be ingested and
made publicly accessible to configured users.

## More information

For
more information about ACLs, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding User Store](connector-principal-store.md "connector-principal-store.md")
