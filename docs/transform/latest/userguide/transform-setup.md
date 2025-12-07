# Setting up AWS Transform

## Before you begin

Before you set up AWS Transform make sure you have an AWS account with administrator access

###### Note

If you want to try out AWS Transform as a proof-of-concept or for test environments see [Quick start: Trying AWS Transform](transform-setup.md#transform-app-admin-starting-standalone "transform-setup.md#transform-app-admin-starting-standalone").

## Getting started with AWS Organizations

Follow these steps to set up AWS Transform:

1. Sign in to your AWS Organizations management account.
2. Navigate to the AWS Transform service.
3. Choose **Enable service** for your organization to use AWS Transform.
4. Configure the necessary permissions for organizational member accounts.
5. Access the AWS Transform web experience from your member accounts.

###### Note

To use the Landing Zone Accelerator (LZA) on AWS solution to build your landing zone together with
AWS Transform for migration capabilities, your AWS Transform account and LZA installation must be in the
same AWS Organization. Using separate Organizations IDs for LZA and AWS Transform deployments is
not supported because this can cause inconsistencies in organizational management and resource
deployments. To learn how to set up your LZA installation using Organizations see [Deploy a cloud foundation to support highly-regulated workloads and complex compliance requirements](../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md "../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md") in the _Landing Zone Accelerator on AWS
Implementation Guide user guide_.

## Getting started with AWS IAM Identity Center

Follow these steps to use IAM Identity Center for AWS Transform and to add users and groups.

###### Note

By default, no users have access to AWS Transform when you first enable it.

1. Set up IAM Identity Center following the instructions in [To enable an instance of IAM Identity Center](../../../singlesignon/latest/userguide/enable-identity-center.md#to-enable-identity-center-instance "../../../singlesignon/latest/userguide/enable-identity-center.md#to-enable-identity-center-instance").

Configure IAM Identity Center to use an external enterprise identity provider, and replicate its user and group info into IAM Identity Center. 2. In the AWS console, select AWS Transform and choose **Get started**. 3. Choose **Enable service** for your organization to use AWS Transform. 4. Select an encryption key. The default selection is an AWS managed key. To use a custom key:

    1. Under **Encryption key**, choose **Customize encryption settings**.
    2. Select **Use an AWS KMS key**.
    3. Choose an existing key or create a new one.
    4. Choose **Submit** to apply your changes, and then choose **Enable AWS Transform**.Click **View profile** to view the configuration. The Web application URL is used by your users to access the AWS Transform unified web experience.

5. Select **Users** in the navigation pane and select **Assign users or groups**.
6. Search for the name of the user or groups you want to authorize to use AWS Transform. The search references users and groups propagated from your identity provider.
7. Select a group or user, select **Done**, and then, **Assign**. These users are authorized to use the AWS Transform unified web interface.

## Using third-party identity providers

AWS Transform supports integration with third-party identity providers (IdPs) such as Azure Active
Directory (Entra ID) and Okta Workforce Identity. This allows you to use your existing identity management system
for user authentication.

### Prerequisites

Before configuring third-party identity provider integration, ensure that users in your identity provider have name, email, and username attributes configured

### Stored Information

When you use AWS Transform with IdPs, AWS stores minimal user information that is
encrypted and secured:

Stored User Information

AWS Transform stores basic user profile information upon first login, including display
name, email address, username (preferred_username), and a unique user identifier. This
information is encrypted using either a customer-owned KMS key or a service-owned key,
depending on the customer's AWS Transform profile configuration. The data is stored in AWS Transform's authentication database and is only collected during the initial login session.
This populates the search results when inviting other users to a workspace.

Data Lifecycle

User information is stored only for users who have logged in to the AWS Transform web
app at least once, and may become stale if users update their information in their identity
provider without logging back into AWS Transform. All stored user information is deleted
when the AWS Transform profile is deleted.

Client Secret Storage

The client secret provided during setup is stored using AWS Secrets Manager via a Service Linked Secret (SLS) in your account.

### User Identifier Handling

Entra

Uses the "oid" (object identifier) claim as the unique user identifier, which is immutable and uniquely identifies users across the Microsoft tenant. This value is visible to customers in the Entra console and appears in CloudTrail logs.

Okta Workforce Identity

Uses different claims for user identification depending on token type - the "sub" claim in ID tokens and the "uid" claim in Access tokens. AWS Transform validates that both claims contain the same value during authentication. This value is visible to customers in the Okta console and appears in CloudTrail logs.

### Setting up Azure Active Directory (Entra ID)

To configure Azure Active Directory integration with AWS Transform:

1. Navigate to the Azure portal and select **Azure Active Directory**.
2. In the left navigation pane, choose **Manage** > **App
   registrations**.
3. Choose **+ New registration**.
4. Enter an application name, choose your supported account type, leave the redirect URI blank, and choose **Register**.
5. In the left navigation, choose **Manage** > **Manifest**.
6. Update `requestedAccessTokenVersion` from `null` to `2` and choose **Save**.
7. Choose **Manage** > **Expose an API** and choose **Add a scope**.
8. Create an Application ID URI using the default structure `api://<client-id>`.
9. Add the scope `transform:read_write`.
10. Choose **Add a certificate or secret** and create a new client secret. Save this value as it's needed for profile creation.
11. Find the Issuer URL by choosing **Endpoints** and selecting the OpenID Connect metadata document. The "issuer" field in the metadata is your Issuer URL.
12. Create a profile in the AWS Transform console using the Client ID, Client Secret, and Issuer URL.
13. After profile creation, add a redirect URI by choosing **Add a platform**, selecting **Web**, and entering `<web-application-url>/login/callback`.

### Setting up Okta Workforce Identity

To configure Okta Workforce Identity integration with AWS Transform:

1. Navigate to your Okta Workforce Identity console.
2. Choose **Applications** > **Applications** and select **Create App Integration**.
3. Select **OIDC - OpenID Connect** and **Web Application**, then choose **Next**.
4. Name your application, leave the Grant Type as _Authorization
   Code_, leave redirect URIs blank, configure user assignments, and choose
   **Save**.
5. Navigate to the **Sign On** tab and set the Issuer to **Okta URL** instead of Dynamic.
6. Copy the Client ID and configure it as the Audience for your Authorization Server by going to **Security** > **API** and adding an Authorization Server.
7. In the Authorization Server, add the scope `transform:read_write` under the **Scopes** tab.
8. Add an Access Policy that allows the OIDC Application to use this Authorization Server and configure a rule for the policy.
9. On the Authorization Server Settings page, note the Issuer URL for profile creation in AWS Transform.
10. Create a profile in AWS Transform using the Issuer URL, Client ID, and Client Secret from the application settings.
11. After profile creation, add `<web-application-url>/login/callback` as a redirect URL in the application's General tab.

###### Note

If you would like to be redirected back to the AWS Transform webapp after logout, you’ll need to
configure your web application URL as a trusted origin under **Security** > **API**.

## User onboarding

This section describes the experience for users who have been granted access to AWS Transform.

### Accepting the invitation

When a user is added to AWS Transform, they receive an email invitation containing:

- A greeting and information about the invitation
- The AWS Transform web application URL
- Their username
- A link to accept the invitation and set up their password

To set up their account:

1. The user clicks the "Accept invitation" link in the email.
2. On the "New user sign up" page, they enter and confirm a password.
3. The password must meet security requirements, including:
   - At least 8 characters
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one number
   - At least one special character

4. After creating a password, they see a confirmation that their account was successfully created.

### Signing in to AWS Transform

To sign in to AWS Transform:

1. Navigate to the AWS Transform web application URL provided in the invitation email.
2. Enter the username.
3. Choose **Next**.
4. Enter the password.
5. Choose **Sign in**.

### Welcome experience

Upon first login, users see the AWS Transform welcome page with:

- A personalized greeting
- Available transformation capabilities
- Option to create a workspace

The welcome page provides information about the transformation capabilities available in AWS Transform, including:

- Modernize IBM z/OS migrations to AWS
- Migrate VMware workloads to Amazon EC2
- Modernize .NET applications to Linux-ready cross-platform .NET
- Assess workloads for migration readiness

Users can start by creating a workspace or asking their team to add them to an existing workspace.
