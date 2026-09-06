

# Set up single sign-on for IAM-based domains
<a name="setting-up-sso-iam-based"></a>

Enable AWS IAM Identity Center single sign-on (SSO) for your IAM-based domain to onboard users from your corporate identity workforce. After you connect to IAM Identity Center, you can add SSO users and groups to projects, enabling them to collaborate on project data and resources.

You can set up IAM Identity Center integration from the Amazon SageMaker Unified Studio domain administration page. To complete this procedure, you must have domain administrator permissions.

## Connecting to IAM Identity Center
<a name="connect-identity-center-iam-based"></a>

Complete the following procedure to connect your IAM-based domain to an IAM Identity Center instance.

1. From the domain administration page, choose **Users** in the left navigation pane.

1. In the **AWS IAM Identity Center connect** section, review the connection status.

1. Choose **Connect**.

1. For the instance type, select one of the following options:
   + **Organization instance** (recommended) — Uses the organization-level IAM Identity Center instance.
   + **Account instance** — Uses an account-level IAM Identity Center instance.

1. Review the user and group assignment setting. By default, assignments are set to *Requires assignment*, which means that users must be explicitly added to the domain. To disable required assignments, use the API during initial Identity Center enablement.

1. Choose **Connect**.

## Viewing SSO connection details
<a name="view-sso-connection-iam-based"></a>

After you connect to an IAM Identity Center instance, a **View SSO connection** button appears on the **Users** page. Choose this button to view the following connection details:
+ **Instance type** — The type of IAM Identity Center instance (organization or account).
+ **User and group assignments** — The current assignment setting for the connection.