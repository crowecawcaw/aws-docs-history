

# Organizations
<a name="organizations-storefront"></a>

Manage your organization's global settings, team members, security policies, and reusable storefront templates.

## Organization settings
<a name="organization-settings"></a>

Organization settings control the global configuration for your AWS Marketplace Storefront account, including your organization name and general preferences.

The Organization Settings page contains the following tabs: General, Team, Security, SSO Configuration, Advanced, Connectors, and Storefront Template. The SSO Configuration tab is visible only to Owners.

### To access organization settings
<a name="organization-settings-access"></a>

1. In the top-right corner, choose your profile avatar, then choose **Organization Settings**.

1. Choose the **General** tab.

### Configurable settings
<a name="organization-settings-configurable"></a>


| Setting | Description | 
| --- | --- | 
| Organization name | Your company or team name displayed across the console | 
| Enable Custom Timezone (toggle) | Turn on to configure a custom timezone for your organization | 
| Timezone (dropdown) | Timezone used for reports and notifications | 

### To update organization settings
<a name="organization-settings-update"></a>

1. In the organization settings page, modify the desired fields.

1. Choose **Save**.

Changes take effect immediately across the console.

### Organization structure
<a name="organization-structure"></a>

Your organization is the top-level container for:
+ **Team members** - People who manage storefronts and accounts
+ **Marketplace accounts** - Connected AWS Marketplace seller accounts
+ **Storefronts** - The branded catalogs you build and deploy
+ **Connectors** - Integrations with external systems (CRM, ITSM, etc.)
+ **Storefront Templates** - Reusable storefront configurations

### Related topics
<a name="organization-settings-related"></a>
+ [Managing team members](#managing-team-members)
+ [Security settings](#security-settings)
+ Notification settings
+ [Storefront templates](#storefront-templates)

## Managing team members
<a name="managing-team-members"></a>

You can add, remove, and manage team members in your organization. Team members are the people who administer storefronts, manage marketplace accounts, and configure settings.

### Organization roles
<a name="organization-roles"></a>

Roles are assigned per scope in the Edit User dialog. A user can hold roles in more than one scope. The dialog shows separate sections for Organization, Accounts, and Storefronts. When you select an admin role, the implied roles auto-select and the system disables the implied checkboxes. A user who self-registers receives the Viewer role by default.


| Role | Capabilities | 
| --- | --- | 
| Owner | Full access to the organization. Highest role. At least one Owner must remain in the organization. | 
| Admin | Full administrative access at the organization level. | 
| Viewer | Read-only access at the organization level. | 

### To add a team member
<a name="team-add-member"></a>

1. In the top-right corner, choose your profile avatar, choose **Organization Settings**, then choose the **Team** tab.

1. Choose **\+ Add User**.

1. Enter the team member's **Email address**.

1. In the Edit User dialog, assign roles for the relevant scopes. To grant organization access, choose Owner, Admin, or Viewer. To grant access to a specific marketplace account or storefront, assign roles in those sections.

1. Choose **Invite**.

The team member receives an email invitation. They must create an account (or sign in with SSO) to accept the invitation.

### To change a team member's role
<a name="team-change-role"></a>

1. In the **Team** page, locate the team member.

1. Choose the **Role** dropdown for that member.

1. Choose the new role.

1. The change takes effect on the member's next action.

### To remove a team member
<a name="team-remove-member"></a>

1. In the **Team** page, locate the team member.

1. Choose the actions menu and choose **Remove**.

1. Confirm the removal.

The member immediately loses access to the organization. Their active sessions are terminated.

### Notes
<a name="team-notes"></a>
+ At least one Owner must remain in the organization at all times.
+ Removing a member does not delete data they created (storefronts, listings, etc.).
+ Team members can belong to one organization. To grant access to multiple organizations, use separate email addresses.
+ Pending invitations that have not been accepted can be revoked from the Team page.

### Related topics
<a name="team-related"></a>
+ [Organization settings](#organization-settings)
+ [Setting up single sign-on for your organization](setting-up-sso.md)
+ RBAC and custom roles

## Security settings
<a name="security-settings"></a>

Security settings let you configure two-factor authentication for your organization.

### To access security settings
<a name="security-access"></a>

1. In the top-right corner, choose your profile avatar, choose **Organization Settings**, then choose the **Security** tab.

### Available settings
<a name="security-available-settings"></a>

#### Two-factor authentication
<a name="security-two-factor"></a>

Enforce two-factor authentication for all team members:

1. Enable **Require Two-Factor Authentication for users**.

1. All team members are prompted to configure two-factor authentication on their next sign-in.

Team members can complete setup with Google Authenticator or Microsoft Authenticator in about a minute.

### Notes
<a name="security-notes"></a>
+ Security settings apply to the management console only. They do not affect buyer access to published storefronts.
+ Changes to security settings take effect immediately for new sign-in attempts. Existing sessions continue until they expire.

### Related topics
<a name="security-related"></a>
+ [Setting up single sign-on for your organization](setting-up-sso.md)
+ [Managing team members](#managing-team-members)

## Storefront templates
<a name="storefront-templates"></a>

Storefront templates allow you to save a storefront's configuration as a reusable template. You can then create new storefronts from a template to replicate design settings, product selections, and configurations without manual setup.

### What is saved in a template
<a name="templates-what-is-saved"></a>

A template captures:
+ Layout type and design settings (colors, logo, theme)
+ Product selection criteria
+ Tag structure
+ BWA configuration
+ Vendor settings

A template does not capture:
+ Deployment state or URL
+ Analytics data
+ Order history
+ Storefront SSO configuration. For setup, see [Setting up single sign-on for a storefront](sso-storefront.md).
+ Governance policies (groups, segments)

### To create a template from a storefront
<a name="templates-create-from-storefront"></a>

1. Navigate to the Storefronts list page.

1. Hover over the storefront tile you want to use as the basis for the template.

1. Choose the three vertical dots (more options) in the top-right corner of the tile.

1. Choose **Clone**.

1. In the Clone dialog, from the **What would you like to do?** dropdown, choose **Create storefront template**.

1. Enter a name for the template.

1. Choose **Create**.

The template is saved to your organization's template library using the configuration of the selected storefront.

### To create a storefront from a template
<a name="templates-create-storefront-from-template"></a>

1. Choose your profile avatar in the top-right corner, choose **Organization Settings**, then choose the **Storefront Templates** tab.

1. Choose the template you want to use.

1. Enter a name for the new storefront.

1. Choose **Create**.

The new storefront is created with all template settings pre-applied. You can modify any settings before deploying.

### Sharing templates
<a name="templates-sharing"></a>

You can share templates with other organizations or team members by email invite.

#### To share a template
<a name="templates-share"></a>

1. In the **Storefront Template** page, locate the template.

1. Choose the actions menu and choose **Send Invite**.

1. In the **Share Storefront Template** dialog, enter the recipient's email address.

1. Choose **Send Invite**.

The recipient receives an email with a link to import the template.

#### To import a shared template
<a name="templates-import"></a>

1. Open the shared template link from the email invitation.

1. Sign in to your organization (if not already signed in).

1. Choose **Import Template**.

1. The template is added to your organization's template library.

### To edit a template name
<a name="templates-edit"></a>

1. In the Storefront Template page, find the template you want to edit.

1. Choose the edit button.

1. Modify the name. You can also add a description.

1. Choose **Save**.

### To delete a template
<a name="templates-delete"></a>

1. In the **Storefront Template** page, locate the template.

1. Choose the actions menu and choose **Delete**.

1. Confirm the deletion.

Deleting a template does not affect storefronts that were created from it.

### Related topics
<a name="templates-related"></a>
+ Creating a storefront
+ Cloning a storefront
+ [Organization settings](#organization-settings)