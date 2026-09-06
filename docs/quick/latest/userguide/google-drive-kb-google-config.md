

# Configure Google Workspace
<a name="google-drive-kb-google-config"></a>

To connect Amazon Quick to Google Drive, complete the following tasks in the Google Cloud console and Google Workspace Admin Console. You create a Google Cloud project, turn on the required APIs, generate service account credentials, and configure domain-wide delegation. You also create a dedicated admin user for the service account to impersonate.

**Prerequisites**  
Before you begin, make sure that you have the following:  
A Google Workspace account with administrator access
Permission to create projects in the Google Cloud console

## Creating a Google Cloud project
<a name="google-drive-kb-create-project"></a>

1. Open the Google Cloud console.

1. From the project selector at the top of the page, choose **New Project**.

1. Enter a project name, then choose **Create**.

1. After the project is created, choose **Select Project** to switch to it. This might take a few moments.

## Turning on the required APIs
<a name="google-drive-kb-enable-apis"></a>

Amazon Quick requires three Google APIs. Turn on each one from the API Library.

1. In the navigation menu, choose **APIs & Services**, then choose **Library**.

1. Search for each of the following APIs and choose **Enable**:
   + Google Drive API
   + Google Drive Activity API
   + Admin SDK API

## Creating the service account
<a name="google-drive-kb-create-service-account"></a>

1. In the navigation menu, choose **APIs & Services**, then choose **Credentials**.

1. Choose **Create Credentials**, then choose **Service account**.

1. Enter a name and optional description for the service account, then choose **Done**.

## Generating a private key
<a name="google-drive-kb-generate-key"></a>

1. On the **Credentials** page, choose the service account you created.

1. Choose the **Keys** tab, then choose **Add Key**, **Create new key**.

1. Confirm that **JSON** is selected, then choose **Create**.

The browser downloads a JSON file containing the private key. Store this file securely. You upload it to Amazon Quick in a later step.

**Note**  
If you receive an error stating that service account key creation is disabled by an organization policy, see [Resolving organization policy restrictions](#google-drive-kb-admin-troubleshooting-org-policy).

## Recording the service account unique ID
<a name="google-drive-kb-record-unique-id"></a>

1. On the service account detail page, choose the **Details** tab.

1. Copy the value in the **Unique ID** field. You need this value when you configure domain-wide delegation.

## Configuring domain-wide delegation
<a name="google-drive-kb-domain-delegation"></a>

Domain-wide delegation allows the service account to access Google Workspace data on behalf of users in your organization.

1. On the service account detail page, expand **Advanced settings**.

1. Choose **View Google Workspace Admin Console**. The admin console opens in a new tab.

1. In the admin console navigation pane, choose **Security**, **Access and data control**, **API controls**.

1. Choose **Manage Domain Wide Delegation**, then choose **Add new**.

1. For **Client ID**, enter the unique ID you copied earlier.

1. For **OAuth scopes**, enter the following comma-separated values:

   ```
   https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/drive.metadata.readonly,https://www.googleapis.com/auth/admin.directory.user.readonly,https://www.googleapis.com/auth/admin.directory.group.readonly,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/forms.body.readonly
   ```

1. Choose **Authorize**.

## Creating a delegated admin user
<a name="google-drive-kb-create-admin-user"></a>

The service account acts on behalf of a Google Workspace admin user. Create a dedicated user for this purpose and assign the minimum required roles.

1. In the Google Workspace Admin Console, choose **Directory**, then choose **Users**.

1. Choose **Add new user**.

1. Enter a first name, last name, and primary email address for the new user, then choose **Add new user**.

1. Choose **Done**.

1. From the user list, choose the user you created. If the user does not appear, refresh the page.

1. On the user detail page, expand the **Admin roles and privileges** section.

1. Under **Roles**, assign the following roles:
   + Groups Reader
   + User Management Admin
   + Storage Admin

1. Choose **Save**.

Record the email address of this user. You need it when you create the knowledge base in Amazon Quick.

## Troubleshooting the Google Workspace configuration
<a name="google-drive-kb-google-config-troubleshooting"></a>

### Resolving organization policy restrictions
<a name="google-drive-kb-admin-troubleshooting-org-policy"></a>

If you receive the following error when creating a service account key:

```
The organization policy constraint iam.disableServiceAccountKeyCreation
is enforced on your organization.
```

**Note**  
For Google Cloud organizations created on or after May 3, 2024, this constraint is enforced by default.

You must override the policy for your project.

1. Open the Google Cloud console and confirm that the correct project is selected.

1. In the navigation menu, choose **IAM & Admin**, then choose **Organization Policies**.

1. In the **Filter** field, enter `iam.disableServiceAccountKeyCreation`. Then, in the policy list, choose **Disable service account key creation**.

1. Choose **Manage policy**.
**Note**  
If **Manage policy** is unavailable, you need the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. See [Granting the Organization Policy Administrator role](#google-drive-kb-admin-troubleshooting-org-admin-role).

1. In the **Policy source** section, ensure that **Override parent's policy** is selected.

1. Under **Enforcement**, turn off enforcement for this organization policy constraint.

1. Choose **Set policy**.

The change can take several minutes to propagate.

### Granting the Organization Policy Administrator role
<a name="google-drive-kb-admin-troubleshooting-org-admin-role"></a>

The Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) must be granted at the organization level, not the project level. It does not appear in the role list when assigning roles to a project.

To grant this role, select your organization (not a project) from the project selector in the Google Cloud console. Then, choose **IAM & Admin**, **IAM**, and assign the role to your account. For detailed instructions, see [Manage access to projects, folders, and organizations](https://cloud.google.com/iam/docs/granting-changing-revoking-access) in the Google Cloud documentation.

The role assignment can take several minutes to propagate.