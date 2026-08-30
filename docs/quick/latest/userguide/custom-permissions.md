# Custom permissions

###### Applies to

Applies to: Enterprise Edition

Intended audience: Administrators and Amazon Quick developers

In Enterprise edition, you can use custom permissions profiles to restrict the capabilities
and features that people can access in Amazon Quick. Custom permissions is a scope-down
policy. It can only restrict what a user has access to based on the default set of
capabilities available to their role. It cannot be used to grant capabilities that a user
does not already have.

You can configure custom permissions at the account, role (admin, author, reader), and user
levels for all identity types in Quick. You can assign custom permissions profiles to users
and roles directly in the Amazon Quick admin console, or by using the Amazon Quick API and
AWS Command Line Interface. The admin console also provides a Check permissions feature that lets you verify
which profile is active for any user and at which level (user, role, or account) it applies.

## Permissions precedence

If a user has custom permissions assigned at multiple levels, Quick evaluates them in the
following order of precedence. The most specific level wins.

1. **User-level** – Custom permissions assigned directly to a user take highest priority.
2. **Role-level** – Custom permissions assigned to a role (Admin, Author, Reader) apply
   to all users in that role unless overridden by a user-level assignment.
3. **Account-level** – Custom permissions assigned at the account level apply to all users
   unless overridden by a role-level or user-level assignment.

The first match wins. A user with a user-level allow-by-default profile is not subject to an
account-level Deny by Default profile. Assign Deny by Default profiles at the appropriate
level for your requirements.

###### Tip

For an in-depth explanation of using custom permissions to establish enterprise
controls in Quick, see [Establishing enterprise governance in Amazon Quick using custom
permissions](https://aws.amazon.com/blogs/business-intelligence/establishing-enterprise-governance-in-amazon-quick-using-custom-permissions/ "https://aws.amazon.com/blogs/business-intelligence/establishing-enterprise-governance-in-amazon-quick-using-custom-permissions/") on the AWS Business Intelligence Blog.

The following limitations apply to custom permissions.

- You can't grant permissions that are above a user's default role. For
  example, if a user has reader access, you can't grant permissions for that user
  to edit dashboards.
- To customize user or role permissions, you need to be a Quick
  administrator with the following IAM permissions:

  - `quicksight:CreateCustomPermissions`
  - `quicksight:DeleteCustomPermissions`
  - `quicksight:DescribeCustomPermissions`
  - `quicksight:ListCustomPermissions`
  - `quicksight:UpdateCustomPermissions`
  - `quicksight:DeleteAccountCustomPermission`
  - `quicksight:DeleteRoleCustomPermission`
  - `quicksight:DeleteUserCustomPermission`
  - `quicksight:DescribeAccountCustomPermission`
  - `quicksight:DescribeRoleCustomPermission`
  - `quicksight:ListCustomPermissionAssignments`
  - `quicksight:UpdateAccountCustomPermission`
  - `quicksight:UpdateRoleCustomPermission`
  - `quicksight:UpdateUserCustomPermission`
    You can create custom permission profiles to restrict access to any combination of the
    following features. Parent capabilities let you restrict an entire asset's feature
    set. When you deny a parent capability, all of its child features are also denied. The
    reverse isn't true: denying every child feature doesn't deny the parent
    capability. This is because a parent can control functionality that isn't exposed
    as a separate child feature. To restrict a capability completely, deny the parent.

###### Parent capability overrides child features

You can't allow an individual child feature while its parent capability is
denied. If you set a parent capability to `DENY` and one of its child
features to `ALLOW`, the child feature remains restricted.
Quick accepts this combination without an error, so verify the result
in the console after you apply it. To allow specific child features, leave the
parent capability allowed and deny only the child features you want to
restrict.

Features that show **Not applicable** in the **Parent capability**
column have no parent capability. Restrict them individually, or restrict their whole
category. For more information, see [Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").

## Quick capabilities and features

The following tables list the capabilities and features that you can restrict
with custom permissions profiles. Capabilities are organized into four groups that
match the console layout.

The **Badge** column indicates the governance category
for each capability. **AI** means the capability belongs
to the AI governance category, which is the category that you can restrict wholesale
with Deny by Default. **Contains AI** means the parent
capability is not itself in the AI category but has children that are.

### AI capabilities

Use this group to control access to AI-powered features such as natural language
Q&A, executive summaries, anomaly detection, and AI-generated insights.

| Feature                                                                    | Amazon Quick behavior                                                                                                     | Badge | Parent capability |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----- | ----------------- |
| Apps                                                                       | Restricts all app capabilities, including creating, updating, sharing, and using apps.                                    | AI    | Not applicable    |
| Access apps native data store when using existing apps                     | Restricts apps from accessing their native data store when users run existing apps.                                       | AI    | Apps              |
| Create and update apps                                                     | Users can't create or update apps.                                                                                        | AI    | Apps              |
| Invoke AI inference when using existing apps                               | Restricts apps from invoking AI inference when users run existing apps.                                                   | AI    | Apps              |
| Share apps                                                                 | Users can't share apps with other users. Apps that were previously shared remain accessible to those users.               | AI    | Apps              |
| Automate                                                                   | Restricts access to Automate. Users can't create, update, or run automations.                                             | AI    | Not applicable    |
| Chat agents                                                                | Users can't view or access any chat agents. The agent library and navigation are hidden.                                  | AI    | Not applicable    |
| Create chat agents                                                         | Users can't create new chat agents.                                                                                       | AI    | Chat agents       |
| Share chat agents                                                          | Users can't share chat agents with other users. Chat agents that were previously shared remain accessible to those users. | AI    | Chat agents       |
| Extensions                                                                 | Restricts access to Quick through all browser and Microsoft Office extensions.                                            | AI    | Not applicable    |
| Browser extension                                                          | Prevents access to Quick through the browser extension for Chrome, Firefox, and Edge.                                     | AI    | Extensions        |
| Excel extension                                                            | Prevents access to Quick through the Microsoft Excel add-in.                                                              | AI    | Extensions        |
| Outlook extension                                                          | Prevents access to Quick through the Microsoft Outlook add-in.                                                            | AI    | Extensions        |
| PowerPoint extension                                                       | Prevents access to Quick through the Microsoft PowerPoint add-in.                                                         | AI    | Extensions        |
| Word extension                                                             | Prevents access to Quick through the Microsoft Word add-in.                                                               | AI    | Extensions        |
| Flows                                                                      | Restricts all Flows capabilities, including creating, sharing, and running flows.                                         | AI    | Not applicable    |
| (Preview) Enable UI agent to perform browser tasks                         | Restricts the Flows UI agent from performing browser tasks.                                                               | AI    | Flows             |
| All eligible users can review and approve flow sharing requests            | Restricts which users can review and approve flow sharing requests.                                                       | AI    | Flows             |
| Allow creators to share without approval                                   | Creators can't share flows without approval.                                                                              | AI    | Flows             |
| Enable Bedrock model usage in General knowledge step for output refinement | Restricts usage of Bedrock models.                                                                                        | AI    | Flows             |
| Quick desktop                                                              | Restricts all Quick desktop capabilities.                                                                                 | AI    | Not applicable    |
| Automate browser actions                                                   | Restricts Quick desktop from automating browser actions.                                                                  | AI    | Quick desktop     |
| Build and manage engrams                                                   | Users can't build or manage engrams in Quick desktop.                                                                     | AI    | Quick desktop     |
| Create and access knowledge memory                                         | Users can't create or access knowledge memory in Quick desktop.                                                           | AI    | Quick desktop     |
| Execute code locally                                                       | Restricts Quick desktop from running code locally.                                                                        | AI    | Quick desktop     |
| Generate images with AI                                                    | Users can't generate images with AI in Quick desktop.                                                                     | AI    | Quick desktop     |
| Manage agents                                                              | Users can't manage agents in Quick desktop.                                                                               | AI    | Quick desktop     |
| Manage tasks                                                               | Users can't manage tasks in Quick desktop.                                                                                | AI    | Quick desktop     |
| Receive chat notifications                                                 | Restricts chat notifications in Quick desktop.                                                                            | AI    | Quick desktop     |
| Use coding agents (ACP)                                                    | Users can't use coding agents (ACP) in Quick desktop.                                                                     | AI    | Quick desktop     |
| Research                                                                   | Restricts access to Research.                                                                                             | AI    | Not applicable    |
| Skills                                                                     | Restricts access to skills, including sharing skills.                                                                     | AI    | Not applicable    |
| Share skills with individuals                                              | Users can't share skills with individuals.                                                                                | AI    | Skills            |
| Spaces                                                                     | Restricts all Spaces capabilities, including creating and sharing spaces.                                                 | AI    | Not applicable    |
| Create spaces                                                              | Users can't create new spaces. Existing spaces remain accessible and unchanged.                                           | AI    | Spaces            |
| Share spaces                                                               | Users can't share spaces with other users. Spaces that were previously shared remain accessible to those users.           | AI    | Spaces            |
| Triggers                                                                   | Restricts all trigger capabilities.                                                                                       | AI    | Not applicable    |
| Inbound email triggers                                                     | Users can't create or use inbound email triggers.                                                                         | AI    | Triggers          |
| Quick event triggers                                                       | Users can't create or use Quick event triggers.                                                                           | AI    | Triggers          |
| Schedule triggers                                                          | Users can't create or use schedule triggers.                                                                              | AI    | Triggers          |
| Use internet to enhance results                                            | Restricts usage of web-based search in Chat agents and Research.                                                          | AI    | Not applicable    |

### BI capabilities

Use this group to control creation and management of core business intelligence
assets: dashboards, analyses, datasets, SPICE capacity, and scheduled
reports.

| Feature                                      | Amazon Quick behavior                                                                                                                                                                                   | Badge          | Parent capability                 |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------- |
| Analyses                                     | Restricts all analysis capabilities.                                                                                                                                                                    | Contains AI    | Not applicable                    |
| Build calculation with AI                    | Users can't build calculated fields with AI.                                                                                                                                                            | AI             | Analyses                          |
| Edit visual with AI                          | Users can't edit visuals with AI.                                                                                                                                                                       | AI             | Analyses                          |
| Generate analyses                            | Users can't generate analyses with AI.                                                                                                                                                                  | AI             | Analyses                          |
| Sharing analyses                             | Access to the Share option on the File menu is disabled for analyses.                                                                                                                                   | Not applicable | Analyses                          |
| Adding or running anomaly detection          | Access to the Add anomaly to sheet option on the Insights menu is disabled for analyses. Users can't add anomaly detection to sheets.                                                                   | AI             | Not applicable                    |
| Content within scheduled email reports       | Restricts including content within scheduled email reports.                                                                                                                                             | Not applicable | Not applicable                    |
| Creating or updating scheduled email reports | Restricts creating or updating scheduled email reports.                                                                                                                                                 | Not applicable | Not applicable                    |
| Creating or updating themes                  | Users can't create new custom themes or edit existing themes. Users can still view or apply existing themes.                                                                                            | Not applicable | Not applicable                    |
| CSV attachments in scheduled email reports   | Restricts including CSV attachments in scheduled email reports.                                                                                                                                         | Not applicable | Not applicable                    |
| Dashboards                                   | Restricts all dashboard capabilities.                                                                                                                                                                   | Contains AI    | Not applicable                    |
| Create executive summary                     | Users can't create executive summaries with AI for dashboards.                                                                                                                                          | AI             | Dashboards                        |
| Sharing dashboards                           | Access to the share icon on the navigation menu is disabled for dashboards.                                                                                                                             | Not applicable | Dashboards                        |
| Subscribing to scheduled email reports       | Users can't subscribe to scheduled email reports.                                                                                                                                                       | Not applicable | Dashboards                        |
| Creating or updating all datasets            | Access to creating or updating all datasets is disabled.                                                                                                                                                | Not applicable | Not applicable                    |
| Creating or updating only SPICE datasets     | Access to creating or updating SPICE datasets is disabled.                                                                                                                                              | Not applicable | Creating or updating all datasets |
| Sharing datasets                             | Access to sharing datasets is disabled.                                                                                                                                                                 | Not applicable | Not applicable                    |
| Excel attachments in scheduled email reports | Restricts including Excel attachments in scheduled email reports.                                                                                                                                       | Not applicable | Not applicable                    |
| Export sheet to PDF                          | Access to the Export to PDF option on the File menu is disabled for analyses. Access to the Generate PDF option on the Export menu is disabled for dashboards.                                          | Not applicable | Not applicable                    |
| Export visual to CSV                         | Access to the Export to CSV option on the actions menu for each visual is disabled for both analyses and dashboards.                                                                                    | Not applicable | Not applicable                    |
| Export visual to Excel                       | Access to the Export to Excel option on the actions menu for each table is disabled for both analyses and dashboards.                                                                                   | Not applicable | Not applicable                    |
| PDF attachments in scheduled email reports   | Restricts including PDF attachments in scheduled email reports.                                                                                                                                         | Not applicable | Not applicable                    |
| Print sheet                                  | Access to the Print option on the File menu is disabled for analyses. Access to the Print option on the Export menu is disabled for dashboards.                                                         | Not applicable | Not applicable                    |
| Scenarios                                    | Restricts access to scenarios.                                                                                                                                                                          | AI             | Not applicable                    |
| Managing shared folders                      | Restricts creating, updating, deleting, and viewing shared folders, adding assets to shared folders, and sharing folders. Doesn't prevent inheriting access to assets shared through folder membership. | Not applicable | Not applicable                    |
| Creating shared folders                      | Restricts creating shared folders.                                                                                                                                                                      | Not applicable | Managing shared folders           |
| Renaming shared folders                      | Restricts renaming shared folders.                                                                                                                                                                      | Not applicable | Managing shared folders           |
| Stories                                      | Restricts access to stories.                                                                                                                                                                            | AI             | Not applicable                    |
| Creating or updating threshold alerts        | Users can't create or update threshold alerts.                                                                                                                                                          | Not applicable | Not applicable                    |
| Topics                                       | Restricts access to topics.                                                                                                                                                                             | AI             | Not applicable                    |
| Viewing account SPICE capacity               | Restricts retrieving the account's SPICE capacity.                                                                                                                                                      | Not applicable | Not applicable                    |

### Connectors

Use this group to control data source connections, including adding, editing, and
removing third-party integrations such as Salesforce, Google Sheets, and
databases.

| Feature                                  | Amazon Quick behavior                                        | Badge          | Parent capability |
| ---------------------------------------- | ------------------------------------------------------------ | -------------- | ----------------- |
| Actions                                  | Restricts all action connector capabilities.                 | AI             | Not applicable    |
| Creating or updating all data sources    | Access to creating or updating all data sources is disabled. | Not applicable | Not applicable    |
| Sharing data sources                     | Access to sharing data sources is disabled.                  | Not applicable | Not applicable    |
| Knowledge base                           | Restricts all knowledge base capabilities.                   | AI             | Not applicable    |
| Creating or updating all knowledge bases | Users can't create or update knowledge bases.                | AI             | Knowledge base    |
| Share all knowledge bases                | Users can't share knowledge bases with other users.          | AI             | Knowledge base    |

### Action connector features

In addition to the features listed in the preceding sections, you can restrict
access to individual action connectors. Each action connector supports the
following permissions:

- **Create and Update action** –
  Restricts the ability to create or update actions for the
  connector.
- **Share action** – Restricts the
  ability to share actions for the connector.
- **Use action** – Restricts the
  ability to use actions for the connector.

These permissions are available under **Actions**, in the
**Connectors** group of the **Capabilities &
features** section. For a list of available action connectors, see
[Action connectors](action-integrations.md "action-integrations.md").

### Knowledge base connectors

You can restrict access to individual knowledge base connectors. Each knowledge
base connector supports the following permissions:

- **Create and Update** – Restricts
  the ability to create or update knowledge bases for the
  connector.
- **Share** – Restricts the ability
  to share knowledge bases for the connector.
- **Use** – Restricts the ability to
  use knowledge bases for the connector.

These permissions are available under **Knowledge base**, in
the **Connectors** group of the **Capabilities &
features** section. For a list of available knowledge base connectors,
see [Knowledge bases](knowledge-base-integrations.md "knowledge-base-integrations.md").

### Administration

Use this group to control account-level settings, including user management,
permission sets, billing, audit logs, and governance policies.

| Feature                                    | Amazon Quick behavior                                         | Badge          | Parent capability |
| ------------------------------------------ | ------------------------------------------------------------- | -------------- | ----------------- |
| Allow users to upgrade or request upgrades | Users can't upgrade their own role or request a role upgrade. | Not applicable | Not applicable    |
