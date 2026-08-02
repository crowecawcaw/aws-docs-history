# Custom permissions

###### Important

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
  - `quicksight:DescribeAccountCustomPermissions`
  - `quicksight:UpdateAccountCustomPermissions`
  - `quicksight:DeleteAccountCustomPermissions`
    You can create custom permission profiles to restrict access to any combination of the
    following features. Parent capabilities can be used to restrict access to an entire
    asset's feature sets. When parent capabilities are disabled, all associated child
    features are also disabled.

Features with no parent capabilities cannot be turned off with this mechanism. Instead,
they must be restricted as individual features, or by applying Deny by Default to
their category. For more information, see [Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").

## Quick capabilities and features

The following table lists the capabilities and features that you can restrict
with custom permissions profiles.

| Feature                                                          | Amazon Quick behavior                                                                                                                                                                                    | Parent capability       |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Create Chat Agents                                               | Cannot view or access any chat agents. Agent library and navigation are hidden.                                                                                                                          | ChatAgent               |
| Share Chat Agents                                                | Cannot share chat agents with other users. Chat agents that were previously shared remain accessible to those users.                                                                                     | ChatAgent               |
| Allow creators to share without approval                         | Flows cannot be shared by creators without approval.                                                                                                                                                     | Flow                    |
| Use Bedrock models for output refinement                         | Restricts usage of Bedrock models.                                                                                                                                                                       | Flow                    |
| Enable UI agent to perform browser tasks                         | Restricts Flows UI agent from performing browser tasks.                                                                                                                                                  | Flow                    |
| All eligible users can review and approve Flows sharing requests | Restricts which users can review and approve Flows sharing requests.                                                                                                                                     | Flow                    |
| Create Spaces                                                    | Cannot create new spaces. Existing spaces remain accessible and unchanged.                                                                                                                               | Spaces                  |
| Share Spaces                                                     | Cannot share spaces with other users. Spaces that were previously shared remain accessible to those users.                                                                                               | Spaces                  |
| Use internet to enhance results                                  | Restricts usage of web-based search in Chat Agents and Research.                                                                                                                                         | —                       |
| Sharing analyses                                                 | Access to Share option on the File menu is disabled for analyses.                                                                                                                                        | Analysis                |
| Adding or running anomaly detection                              | Access to the Add anomaly to sheet option on the Insights menu is disabled for analyses. Users will not be able to add anomaly detection to sheets.                                                      | Analysis                |
| Print Sheet                                                      | Access to the Print option on the File menu is disabled for analyses. Access to the Print option on the Export menu is disabled for dashboards.                                                          | —                       |
| Export sheet to PDF                                              | Access to the Export to PDF option on the File menu is disabled for analyses. Access to the Generate PDF option on the Export menu is disabled for dashboards.                                           | —                       |
| Creating or updating themes                                      | Users will not be able to create new custom themes or edit existing themes. Users can still view or apply existing themes.                                                                               | —                       |
| Sharing dashboards                                               | Access to the share icon on the navigation menu is disabled for dashboards.                                                                                                                              | Dashboard               |
| Export visual to CSV                                             | Access to the Export to CSV option on the actions menu for each visual is disabled for both analyses and dashboards.                                                                                     | —                       |
| Export visual to Excel                                           | Access to the Export to Excel option on the actions menu for each table is disabled for both analyses and dashboards.                                                                                    | —                       |
| Creating or updating all datasets                                | Access to creating or updating all datasets will be disabled.                                                                                                                                            | —                       |
| Creating or updating only SPICE datasets                         | Access to creating or updating SPICE datasets will be disabled.                                                                                                                                          | —                       |
| Sharing datasets                                                 | Access to sharing datasets will be disabled.                                                                                                                                                             | —                       |
| Viewing account SPICE capacity                                   | Restricts retrieving the account's SPICE capacity.                                                                                                                                                       | —                       |
| Creating or updating all data sources                            | Access to creating or updating all data sources will be disabled.                                                                                                                                        | —                       |
| Sharing data sources                                             | Access to sharing data sources will be disabled.                                                                                                                                                         | —                       |
| Managing shared folders                                          | Restricts creating, updating, deleting, and viewing shared folders, adding assets to shared folders, and sharing folders. Does not prevent inheriting access to assets shared through folder membership. | —                       |
| Creating shared folders                                          | Restricts creating shared folders.                                                                                                                                                                       | Managing shared folders |
| Renaming shared folders                                          | Restricts renaming shared folders.                                                                                                                                                                       | Managing shared folders |
| Creating or updating scheduled email reports                     | Restricts creating or updating scheduled email reports.                                                                                                                                                  | —                       |
| Browser Extension                                                | Prevents access to Quick through the browser extension for Chrome, Firefox, and Edge.                                                                                                                    | Extensions              |
| Excel Extension                                                  | Prevents access to Quick through the Microsoft Excel add-in.                                                                                                                                             | Extensions              |
| Outlook Extension                                                | Prevents access to Quick through the Microsoft Outlook add-in.                                                                                                                                           | Extensions              |
| PowerPoint Extension                                             | Prevents access to Quick through the Microsoft PowerPoint add-in.                                                                                                                                        | Extensions              |
| Word Extension                                                   | Prevents access to Quick through the Microsoft Word add-in.                                                                                                                                              | Extensions              |

###### Note

The names in this table are the API capability identifiers. Use these values when working with the AWS Command Line Interface or API.

## Action connector features

In addition to the features listed in the preceding sections, you can restrict access to individual action
connectors. Each action connector supports the following permissions:

- **Create and Update action** – Restricts
  the ability to create or update actions for the connector.
- **Share action** – Restricts the ability
  to share actions for the connector.
- **Use action** – Restricts the ability to
  use actions for the connector.

These permissions are available on the **Action Connectors** tab of
the custom permissions profile. For a list of available action connectors, see [Action connectors](action-integrations.md "action-integrations.md").
