

# Setting up AWS Transform
<a name="transform-setup"></a>

## Before you begin
<a name="transform-prerequisites"></a>

Before you set up AWS Transform make sure you have an AWS account with administrator access

**Note**  
If you want to try out AWS Transform as a proof-of-concept or for test environments see [Quick start: Trying AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html#transform-app-admin-starting-standalone).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Getting started with IAM-only access
<a name="transform-iam-only-access"></a>

With IAM-only access, users authenticate with their existing AWS credentials.

To set up IAM-only access:

1. In the AWS console, navigate to AWS Transform and choose **Get started**.

1. Complete the account settings configuration.

1. Under **User access**, select **IAM-only access**.

1. Choose **Enable** to create your profile.

Users log in to the AWS Transform web application through [AWS Sign-In](https://docs.aws.amazon.com/signin/latest/userguide/what-is-sign-in.html). Their user identifier in the web application is based on their IAM principal.

**Important**  
You cannot add an identity provider after setup is complete. To manage users with IAM Identity Center or an existing identity provider, choose one of those options during initial setup.

With IAM-only access, any IAM principal with the `transform:AccessTransformProfile` permission on the profile resource can access AWS Transform. You manage user access through IAM policies rather than through identity provider user assignments.

The `transform:AccessTransformProfile` action only grants access to AWS Transform. Once inside AWS Transform, workspace roles control what actions a user can perform. These roles include Admin, Contributor, Approver, and Read-only. Workspace roles apply regardless of how the user authenticated.

## Using IAM credentials
<a name="transform-iam-access"></a>

### User information handling
<a name="transform-iam-user-information"></a>

When IAM principals access AWS Transform, the service handles user identity differently than with identity provider-based access.

User identity  
IAM users are identified by their [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html).

Dual identity  
A user who has both an identity provider identity (such as IAM Identity Center) and an IAM session appears as two separate users in AWS Transform. Their work is not linked between the two identities.

Email notifications  
Email notifications are only enabled for SSO users. IAM principals can still be added to workspaces but they will not receive email notifications.

Audit  
IAM API calls are logged in AWS CloudTrail with the caller's IAM identity. Actions performed by IAM users in a job are also traceable in AWS Transform worklogs.

### Enabling IAM access alongside an identity provider
<a name="transform-iam-alongside-idp"></a>

If you set up AWS Transform with IAM Identity Center or a third-party identity provider, you can also enable IAM access as an additional way to authenticate. This allows IAM principals to access AWS Transform alongside your existing identity provider users.

IAM access is enabled by default when you create a profile with IAM Identity Center or a third-party identity provider. To enable or disable IAM access at any time:

1. In the AWS Transform console, navigate to **Settings**.

1. Under **Access AWS Transform with IAM credentials**, toggle **Enable IAM access** on or off.

When IAM access is enabled, both identity provider users and IAM principals can use AWS Transform. IAM users and identity provider users can collaborate in the same workspace.

## Getting started with AWS Organizations
<a name="transform-app-admin-starting-orgs"></a>

Follow these steps to set up AWS Transform:

1. Sign in to your AWS Organizations management account.

1. Navigate to the AWS Transform service.

1. Choose **Enable service** for your organization to use AWS Transform.

1. Configure the necessary permissions for organizational member accounts.

1. Access the AWS Transform web experience from your member accounts.

**Note**  
To use the Landing Zone Accelerator (LZA) on AWS solution to build your landing zone together with AWS Transform for migration capabilities, your AWS Transform account and LZA installation must be in the same AWS Organization. Using separate Organizations IDs for LZA and AWS Transform deployments is not supported because this can cause inconsistencies in organizational management and resource deployments. To learn how to set up your LZA installation using Organizations see [Deploy a cloud foundation to support highly-regulated workloads and complex compliance requirements ](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html) in the *Landing Zone Accelerator on AWS Implementation Guide user guide*. 

## Getting started with AWS IAM Identity Center
<a name="transform-app-admin-starting-idc"></a>

Follow these steps to use IAM Identity Center for AWS Transform and to add users and groups.

By default, no users have access to AWS Transform when you first enable it. 

**Note**  
IAM Identity Center is not limited to the region in which it is set up. If you already set up IAM Identity Center in a region that is not supported by AWS Transform, you can use it for AWS Transform.

1. Set up IAM Identity Center following the instructions in [ To enable an instance of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html#to-enable-identity-center-instance).

   Configure IAM Identity Center to use an external enterprise identity provider, and replicate its user and group info into IAM Identity Center.

1. In the AWS console, select AWS Transform and choose **Get started**.

1. Choose **Enable service** for your organization to use AWS Transform.

1. Select an encryption key. The default selection is an AWS managed key. To use a custom key:

   1. Under **Encryption key**, choose **Customize encryption settings**.

   1. Select **Use an AWS KMS key**.

   1. Choose an existing key or create a new one.

   1. Choose **Submit** to apply your changes, and then choose **Enable AWS Transform**.

   Choose **View profile** to view the configuration. The Web application URL is used by your users to access the AWS Transform unified web experience.

1. Select **Users** in the navigation pane and select **Assign users or groups**.

1. Search for the name of the user or groups you want to authorize to use AWS Transform. The search references users and groups propagated from your identity provider.

1. Select a group or user, select **Done**, and then, **Assign**. These users are authorized to use the AWS Transform unified web interface.

## Using third-party identity providers
<a name="transform-third-party-identity"></a>

AWS Transform supports integration with third-party identity providers (IdPs) such as Azure Active Directory (Entra ID) and Okta Workforce Identity. This allows you to use your existing identity management system for user authentication.

### Prerequisites
<a name="transform-third-party-prerequisites"></a>

Before configuring third-party identity provider integration, ensure that users in your identity provider have name, email, and username attributes configured

### Stored Information
<a name="transform-stored-information"></a>

When you use AWS Transform with IdPs, AWS stores minimal user information that is encrypted and secured:

Stored User Information  
AWS Transform stores basic user profile information upon first login, including display name, email address, username (preferred\_username), and a unique user identifier. This information is encrypted using either a customer-owned KMS key or a service-owned key, depending on the customer's AWS Transform profile configuration. The data is stored in AWS Transform's authentication database and is only collected during the initial login session. This populates the search results when inviting other users to a workspace.

Data Lifecycle  
User information is stored only for users who have logged in to the AWS Transform web app at least once, and may become stale if users update their information in their identity provider without logging back into AWS Transform. All stored user information is deleted when the AWS Transform profile is deleted.

Client Secret Storage  
The client secret provided during setup is stored using AWS Secrets Manager via a Service Linked Secret (SLS) in your account.

### User Identifier Handling
<a name="transform-user-identifier-handling"></a>

Entra  
Uses the "oid" (object identifier) claim as the unique user identifier, which is immutable and uniquely identifies users across the Microsoft tenant. This value is visible to customers in the Entra console and appears in CloudTrail logs.

Okta Workforce Identity  
Uses different claims for user identification depending on token type - the "sub" claim in ID tokens and the "uid" claim in Access tokens. AWS Transform validates that both claims contain the same value during authentication. This value is visible to customers in the Okta console and appears in CloudTrail logs.

### Setting up Azure Active Directory (Entra ID)
<a name="transform-azure-setup"></a>

To configure Azure Active Directory integration with AWS Transform:

1. Navigate to the Azure portal and select **Azure Active Directory**.

1. In the left navigation pane, choose **Manage** > **App registrations**.

1. Choose **\+ New registration**.

1. Enter an application name, choose your supported account type, leave the redirect URI blank, and choose **Register**.

1. In the left navigation, choose **Manage** > **Manifest**.

1. Update `requestedAccessTokenVersion` from `null` to `2` and choose **Save**.

1. Choose **Manage** > **Expose an API** and choose **Add a scope**.

1. Create an Application ID URI using the default structure `api://<client-id>`.

1. Add the scope `transform:read_write`.

1. Choose **Add a certificate or secret** and create a new client secret. Save this value as it's needed for profile creation.

1. Find the Issuer URL by choosing **Endpoints** and selecting the OpenID Connect metadata document. The "issuer" field in the metadata is your Issuer URL.

1. Create a profile in the AWS Transform console using the Client ID, Client Secret, and Issuer URL.

1. After profile creation, add a redirect URI by choosing **Add a platform**, selecting **Web**, and entering `<web-application-url>/login/callback`.

### Setting up Okta Workforce Identity
<a name="transform-okta-setup"></a>

To configure Okta Workforce Identity integration with AWS Transform:

1. Navigate to your Okta Workforce Identity console.

1. Choose **Applications** > **Applications** and select **Create App Integration**.

1. Select **OIDC - OpenID Connect** and **Web Application**, then choose **Next**.

1. Name your application, leave the Grant Type as *Authorization Code*, leave redirect URIs blank, configure user assignments, and choose **Save**.

1. Navigate to the **Sign On** tab and set the Issuer to **Okta URL** instead of Dynamic.

1. Copy the Client ID and configure it as the Audience for your Authorization Server by going to **Security** > **API** and adding an Authorization Server.

1. In the Authorization Server, add the scope `transform:read_write` under the **Scopes** tab.

1. Add an Access Policy that allows the OIDC Application to use this Authorization Server and configure a rule for the policy.

1. On the Authorization Server Settings page, note the Issuer URL for profile creation in AWS Transform.

1. Create a profile in AWS Transform using the Issuer URL, Client ID, and Client Secret from the application settings.

1. After profile creation, add `<web-application-url>/login/callback` as a redirect URL in the application's General tab.
**Note**  
If you would like to be redirected back to the AWS Transform web application after logout, you’ll need to configure your web application URL as a trusted origin under **Security** > **API**.

## User onboarding
<a name="transform-user-onboarding"></a>

This section describes the experience for users who have been granted access to AWS Transform.

### Accepting the invitation
<a name="transform-user-invitation"></a>

When a user is added to AWS Transform, they receive an email invitation containing:
+ A greeting and information about the invitation
+ The AWS Transform web application URL
+ Their username
+ A link to accept the invitation and set up their password

To set up their account:

1. The user clicks the "Accept invitation" link in the email.

1. On the "New user sign up" page, they enter and confirm a password.

1. The password must meet security requirements, including:
   + At least 8 characters
   + At least one uppercase letter
   + At least one lowercase letter
   + At least one number
   + At least one special character

1. After creating a password, they see a confirmation that their account was successfully created.

### Signing in to AWS Transform
<a name="transform-user-signin"></a>

To sign in to AWS Transform:

1. Navigate to the AWS Transform web application URL provided in the invitation email.

1. Enter the username.

1. Choose **Next**.

1. Enter the password.

1. Choose **Sign in**.

### Welcome experience
<a name="transform-user-welcome"></a>

Upon first login, users see the AWS Transform welcome page with:
+ A personalized greeting
+ Available transformation capabilities
+ Option to create a workspace

The welcome page provides information about the transformation capabilities available in AWS Transform, including:
+ Modernize IBM z/OS migrations to AWS
+ Migrate VMware workloads to Amazon EC2
+ Modernize .NET applications to Linux-ready cross-platform .NET
+ Assess workloads for migration readiness

Users can start by creating a workspace or asking their team to add them to an existing workspace.