# Organizations

Manage your organization's global settings, team members, security policies, and reusable
storefront templates.

## Organization settings

Organization settings control the global configuration for your AWS Marketplace
Storefront account, including your organization name and general
preferences.

The Organization Settings page contains the following tabs: General, Team, Security, SSO Configuration, Advanced, Connectors, and Storefront Template. The SSO Configuration tab is visible only to Owners.

### To access organization settings

1. In the top-right corner, choose your profile avatar, then choose
   **Organization Settings**.
2. Choose the **General** tab.

### Configurable settings

| Setting                         | Description                                                     |
| ------------------------------- | --------------------------------------------------------------- |
| Organization name               | Your company or team name displayed across the console          |
| Enable Custom Timezone (toggle) | Turn on to configure a custom timezone for your<br>organization |
| Timezone (dropdown)             | Timezone used for reports and notifications                     |

### To update organization settings

1. In the organization settings page, modify the desired fields.
2. Choose **Save**.

Changes take effect immediately across the console.

### Organization structure

Your organization is the top-level container for:

- **Team members** - People who manage
  storefronts and accounts
- **Marketplace accounts** - Connected AWS
  Marketplace seller accounts
- **Storefronts** - The branded catalogs you
  build and deploy
- **Connectors** - Integrations with external
  systems (CRM, ITSM, etc.)
- **Storefront Templates** - Reusable storefront
  configurations

### Related topics

- [Managing team members](#managing-team-members "#managing-team-members")
- [Security settings](#security-settings "#security-settings")
- Notification settings
- [Storefront templates](#storefront-templates "#storefront-templates")

## Managing team members

You can add, remove, and manage team members in your organization. Team members are
the people who administer storefronts, manage marketplace accounts, and configure
settings.

### Organization roles

Roles are assigned per scope in the Edit User dialog. A user can hold roles in more than one scope. The dialog shows separate sections for Organization, Accounts, and Storefronts. When you select an admin role, the implied roles auto-select and the system disables the implied checkboxes. A user who self-registers receives the Viewer role by default.

| Role   | Capabilities                                                                                       |
| ------ | -------------------------------------------------------------------------------------------------- |
| Owner  | Full access to the organization. Highest role. At least one Owner must remain in the organization. |
| Admin  | Full administrative access at the organization level.                                              |
| Viewer | Read-only access at the organization level.                                                        |

### To add a team member

1. In the top-right corner, choose your profile avatar, choose
   **Organization Settings**, then choose the
   **Team** tab.
2. Choose **+ Add User**.
3. Enter the team member's **Email
   address**.
4. In the Edit User dialog, assign roles for the relevant scopes. To grant organization access, choose Owner, Admin, or Viewer. To grant access to a specific marketplace account or storefront, assign roles in those sections.
5. Choose **Invite**.

The team member receives an email invitation. They must create an account (or sign
in with SSO) to accept the invitation.

### To change a team member's role

1. In the **Team** page, locate the team
   member.
2. Choose the **Role** dropdown for that
   member.
3. Choose the new role.
4. The change takes effect on the member's next action.

### To remove a team member

1. In the **Team** page, locate the team
   member.
2. Choose the actions menu and choose **Remove**.
3. Confirm the removal.

The member immediately loses access to the organization. Their active sessions are
terminated.

### Notes

- At least one Owner must remain in the organization at all times.
- Removing a member does not delete data they created (storefronts,
  listings, etc.).
- Team members can belong to one organization. To grant access to multiple
  organizations, use separate email addresses.
- Pending invitations that have not been accepted can be revoked from the
  Team page.

### Related topics

- [Organization settings](#organization-settings "#organization-settings")
- [Setting up single sign-on for your organization](setting-up-sso.md "setting-up-sso.md")
- RBAC and custom roles

## Security settings

Security settings let you configure two-factor authentication for your
organization.

### To access security settings

1. In the top-right corner, choose your profile avatar, choose
   **Organization Settings**, then choose the
   **Security** tab.

### Available settings

#### Two-factor authentication

Enforce two-factor authentication for all team members:

1. Enable **Require Two-Factor Authentication for
   users**.
2. All team members are prompted to configure two-factor authentication
   on their next sign-in.

Team members can complete setup with Google Authenticator or Microsoft
Authenticator in about a minute.

### Notes

- Security settings apply to the management console only. They do not affect
  buyer access to published storefronts.
- Changes to security settings take effect immediately for new sign-in
  attempts. Existing sessions continue until they expire.

### Related topics

- [Setting up single sign-on for your organization](setting-up-sso.md "setting-up-sso.md")
- [Managing team members](#managing-team-members "#managing-team-members")

## Storefront templates

Storefront templates allow you to save a storefront's configuration as a reusable
template. You can then create new storefronts from a template to replicate design
settings, product selections, and configurations without manual setup.

### What is saved in a template

A template captures:

- Layout type and design settings (colors, logo, theme)
- Product selection criteria
- Tag structure
- BWA configuration
- Vendor settings

A template does not capture:

- Deployment state or URL
- Analytics data
- Order history
- Storefront SSO configuration. For setup, see [Setting up single sign-on for a storefront](sso-storefront.md "sso-storefront.md").
- Governance policies (groups, segments)

### To create a template from a storefront

1. Navigate to the Storefronts list page.
2. Hover over the storefront tile you want to use as the basis for the template.
3. Choose the three vertical dots (more options) in the top-right corner of the tile.
4. Choose **Clone**.
5. In the Clone dialog, from the **What would you like to do?** dropdown, choose **Create storefront template**.
6. Enter a name for the template.
7. Choose **Create**.

The template is saved to your organization's template library using the configuration of the selected storefront.

### To create a storefront from a template

1. Choose your profile avatar in the top-right corner, choose **Organization Settings**, then choose the **Storefront Templates** tab.
2. Choose the template you want to use.
3. Enter a name for the new storefront.
4. Choose **Create**.

The new storefront is created with all template settings pre-applied. You can modify any settings before deploying.

### Sharing templates

You can share templates with other organizations or team members by email
invite.

#### To share a template

1. In the **Storefront Template** page,
   locate the template.
2. Choose the actions menu and choose **Send
   Invite**.
3. In the **Share Storefront Template**
   dialog, enter the recipient's email address.
4. Choose **Send Invite**.

The recipient receives an email with a link to import the template.

#### To import a shared template

1. Open the shared template link from the email invitation.
2. Sign in to your organization (if not already signed in).
3. Choose **Import Template**.
4. The template is added to your organization's template library.

### To edit a template name

1. In the Storefront Template page, find the template you want to edit.
2. Choose the edit button.
3. Modify the name. You can also add a description.
4. Choose **Save**.

### To delete a template

1. In the **Storefront Template** page, locate
   the template.
2. Choose the actions menu and choose **Delete**.
3. Confirm the deletion.

Deleting a template does not affect storefronts that were created from it.

### Related topics

- Creating a storefront
- Cloning a storefront
- [Organization settings](#organization-settings "#organization-settings")
