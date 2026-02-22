# Amazon Quick user interaction with

extensions

Amazon Quick extensions enable different user roles to collaborate effectively in
creating, managing, and utilizing AI-powered analytics tools. Each role—administrators,
authors, and end users—has distinct responsibilities and capabilities when working with
extensions. Understanding these role-based interactions ensures proper governance,
security, and optimal user experience across your organization's Amazon Quick
deployment.

###### Topics

- [User capabilities and
  permissions](#extension-user-capabilities "#extension-user-capabilities")
- [Amazon Quick administrator
  responsibilities](#admin-extension-role "#admin-extension-role")
- [Amazon Quick author capabilities](#author-extension-role "#author-extension-role")
- [Amazon Quick end user access](#user-extension-role "#user-extension-role")
- [Extension access troubleshooting](#extension-troubleshooting "#extension-troubleshooting")

## User capabilities and

permissions

Amazon Quick implements a hierarchical permission model for extensions that
balances organizational control with user productivity. Administrators establish the
foundational policies and infrastructure, authors manage the deployment and
configuration of specific extension instances, and readers benefit from the
AI-powered assistance within their authorized scope. The following table shows how
each user type in Amazon Quick interacts with extensions.

| User Type                 | Capabilities                                                                                                                                                                                                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrators            | • Enable/remove extension access to their organization's<br>workspaces and organizations<br>• Create extensions for Slack,<br>Teams, Word, and<br>Outlook<br>• Assign owners for extensions created<br>• Control whether extensions are available for users in<br>Amazon Quick<br>• Use all enabled extensions |
| Authors                   | • Create and install extensions using administrator<br>enabled extension access<br>• Edit/delete extensions for which they are<br>owners<br>• Use all enabled extensions                                                                                                                                       |
| Readers (Reader Pro only) | • Use all enabled extensions                                                                                                                                                                                                                                                                                   |

Beyond the broad user type categories, Amazon Quick implements granular permission
controls that determine specific actions users can perform with individual
extensions. These permissions operate independently of user types, allowing
administrators to fine-tune access based on organizational needs and security
requirements. The following table outlines how user permissions determine what you
can do with a extension:

| Permissions Type | Permissions                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owners           | • Edit extension name and description<br>• Install the extension in a workspace or<br>organization<br>• Grant ownership and editing permissions to specific<br>users and groups |
| Viewers          | • View extension name and description<br>• Access links to open in Slack,<br>M365, and browser<br>• Use the extensions                                                          |

###### Important

The Amazon Quick browser extension extension doesn't need any admin setup to
install and use.

These permission structures ensure that extension access aligns with your
organization's security requirements while enabling appropriate levels of
functionality for each user role. Administrators maintain control over extension
availability and initial setup, authors handle deployment and configuration, and all
users can benefit from the AI-powered assistance once extensions are properly
configured.

## Amazon Quick administrator

responsibilities

Amazon Quick administrators, or users granted admin privileges, establish the
foundational infrastructure that enables extension functionality across the
organization. They handle the critical setup and security configurations that allow
Amazon Quick authors to deploy extensions and end users to access them
safely.

###### Note

Creating and adjusting extension access requires IAM administrator
privileges. All administrators will see the extension links, but if not [signed in with IAM credentials](../../../quicksuite/latest/userguide/iam-credentials.md "../../../quicksuite/latest/userguide/iam-credentials.md"), you will need to sign in with
appropriate IAM permissions to manage extension access. This must be an IAM
user who is an Amazon Quick administrator and not non-IAM admin users.

| Responsibility area     | Administrator capabilities                                                                                                                                                                                                                                                                            |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Infrastructure setup    | • Connect extension applications to organizational<br>systems (Slack workspaces,<br>Microsoft 365 tenants)<br>• Handle OAuth authorization and tenant-level<br>permissions<br>• Manage platform-specific installation methods:<br>manifest-only for<br>Word/Outlook,<br>OAuth-only for<br>Slack/Teams |
| Security and compliance | • Manage enterprise security and compliance<br>settings<br>• Control which extension types are available to the<br>organization                                                                                                                                                                       |

## Amazon Quick author capabilities

Authors bridge the gap between administrative infrastructure and end-user access
by creating, configuring, and deploying specific extension instances. They manage
the day-to-day operational aspects of extension deployment and maintenance.

Author capabilities depend on the permission level granted by administrators.
There are two permission types that determine what authors can do:

- **Viewers:** Can view extension name and
  description, access links to open extensions, and use the extensions.
- **Owners:** Can edit extension name and
  description, install extensions in workspaces or organizations, and share
  ownership permissions with users and groups.

This translates to two main setup flows:

- **Limited permissions (view, share, delete
  only):** Authors can only use the basic landing page
  functionality to view, share, and delete extensions after admin completes
  all setup.
- **Full permissions (deploy, view, share, delete,
  edit):** Authors can download manifests or use OAuth
  deployments to complete app setup, rename extensions, and access editing
  features.

| Capability area              | Author functions                                                                                                                                                                                                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration and deployment | • Download and manage installation manifests for<br>deployment (with full permissions)<br>• Deploy extension instances using OAuth or<br>manifest-based methods (with full permissions)<br>• Complete app setup and installation (with full<br>permissions) |
| Management and sharing       | • Manage extension sharing and access permissions<br>• View, share, and delete deployed extensions<br>• Edit extensions and access creation features (with<br>full permissions)                                                                             |

## Amazon Quick end user access

End users represent the primary beneficiaries of extension functionality,
accessing AI-powered assistance directly within their existing workflow
applications. Their interaction with extensions focuses on daily productivity and
seamless integration with organizational knowledge.

| Access level                 | User capabilities                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Daily usage and productivity | • Access extensions directly within existing workflow<br>applications<br>• Use extensions for knowledge access, document<br>analysis, and action taking<br>• Benefit from seamless integration without context<br>switching between applications                                                                                                                                                    |
| Knowledge and actions        | • Access organizational knowledge bases and custom<br>agents through extension interfaces<br>• Perform external actions in third-party applications<br>using configured [action<br>connectors](../../../quicksuite/latest/userguide/action-connectors.md "../../../quicksuite/latest/userguide/action-connectors.md")<br>• Receive permissions-aware responses based on<br>individual access levels |

The following table shows how each user type in Amazon Quick interacts with
extensions.

| User Type                 | Capabilities                                                                                                                                                                                                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrators            | • Enable/remove extension access to their organization's<br>workspaces and organizations<br>• Create extensions for Slack,<br>Teams, Word, and<br>Outlook<br>• Assign owners for extensions created<br>• Control whether extensions are available for users in<br>Amazon Quick<br>• Use all enabled extensions |
| Authors                   | • Create and install extensions using administrator enabled<br>extension access<br>• Edit/delete extensions for which they are owners<br>• Use all enabled extensions                                                                                                                                          |
| Readers (Reader Pro only) | • Use all enabled extensions                                                                                                                                                                                                                                                                                   |

The following table outlines how user permissions determine what you can do with a
extension:

| Permissions Type | Permissions                                                                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owners           | • Edit extension name and description<br>• Install the extension in a workspace or<br>organization<br>• Grant ownership and editing permissions to specific users<br>and groups |
| Viewers          | • View extension name and description<br>• Access links to open in Slack,<br>M365, and browser<br>• Use the extensions                                                          |

###### Important

The Amazon Quick browser extension extension doesn't need any admin setup to
install and use.

## Extension access troubleshooting

If you encounter issues accessing or creating extensions:

- **Cannot create extensions:** Your IAM user
  who is a Amazon Quick administrator must first configure extension access
  for the extension type you want to use. Other administrators will not be
  able to create/edit/delete extension access.
- **Cannot find my extensions:** Check that
  extension access has been configured by your administrator and that you have
  the appropriate permissions to view extensions.
- **Extensions appear but cannot edit:** You
  have view-only access. Ask your administrator or extension owner to share
  edit permissions with you.
- **No extensions visible:** Contact your
  administrator to set up extension access and create default extensions for
  your organization.
