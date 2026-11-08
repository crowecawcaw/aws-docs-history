

# Setting up Amazon Quick on desktop for enterprise deployments
<a name="desktop-enterprise-setup"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators  | 

Users in your organization sign in to Amazon Quick on desktop with the sign-in method your Quick account already uses on the web. By default, you don't register an OpenID Connect (OIDC) application in your identity provider, create a client ID, or add extension access. If a user can sign in to Quick on the web, that user can sign in to the desktop application.

To turn on desktop access, an administrator adds the desktop connector one time. For instructions, see [Turning on desktop access](#desktop-enterprise-turn-on). If you need to manage desktop sign-in separately in your identity provider, you can set up a dedicated identity provider configuration instead. For more information, see [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md).

Both sign-in options work for accounts that use IAM Identity Center, IAM federation, or Quick-managed users.

**Note**  
If your organization already set up enterprise sign-in for the desktop application with a desktop extension, that setup keeps working. To move to the desktop connector, see [Moving from the desktop extension to the desktop connector](#desktop-enterprise-migrate).

**Note**  
If you are using a Free or Plus account, this section does not apply to you. Continue to [Getting started with the Amazon Quick desktop application](getting-started-desktop.md).

## Prerequisites
<a name="desktop-enterprise-prerequisites"></a>

Before you begin, verify that you have the following:
+ An AWS account with an active Amazon Quick subscription. The account's home Region (identity Region) must be a supported AWS Region. For a list of supported Regions, see [Supported AWS Regions for Amazon Quick](regions.md#regions-qs).
+ Administrator access to your Amazon Quick account.
+ Version 1.1.4053 or later of the desktop application.
+ In restricted network environments, the ability to reach the required Amazon Quick and identity provider domains. For the list of domains to add to your allow list, see [Network access and required domains](desktop-security.md#desktop-network-access).

**Important**  
Amazon Quick on desktop is available only in AWS Regions that support agentic features. To check your Region, see the **Agentic Features** column in [Supported AWS Regions for Amazon Quick](regions.md#regions-qs).

## Turning on desktop access
<a name="desktop-enterprise-turn-on"></a>

**Important**  
Adding the desktop connector turns on desktop access for all users in your account right away. To roll out desktop in stages, first restrict the **Quick desktop** capability in a custom permissions profile for the users or roles that shouldn't have access yet, and then add the connector. To give more users access later, update the profile. For more information, see [Custom permissions](custom-permissions.md). You can also restrict the capability after you add the connector.

**To add the desktop connector**

1. Sign in to the Amazon Quick console as an administrator.

1. Choose your profile icon, and then choose **Manage account**.

1. In the navigation pane, choose **Inbound connectors**, and then choose the **Quick Desktop** tab.

1. Choose **Add desktop connector**.

1. For the identity setup, choose **Use Quick's existing configured sign-in method**, and then choose **Confirm**. If your users already sign in to Quick on the web through your identity provider, this option already uses it. If you need to manage desktop sign-in separately in your identity provider, see [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md) instead.

1. Quick creates the connector. Verify that the connector card shows the name **Quick Desktop**, the connector type **Quick desktop**, and the status **Enabled**.

To install the application, see [Getting started with the Amazon Quick desktop application](getting-started-desktop.md). To deploy the application to a managed fleet, see [Managed deployment configuration](desktop-enterprise-managed-deployment.md).

## How sign-in works
<a name="desktop-enterprise-sign-in"></a>
+ To sign in, users need an active Amazon Quick web session in their browser. If they don't have one, the browser prompts them to sign in to Quick first.
+ A sign-in lasts up to 30 days, regardless of activity. During that time, access lasts one hour and renews automatically in the background, so users stay signed in. After 30 days, users sign in again.
+ Users are signed out if access can't be renewed or their session ends.

If you use a dedicated identity provider configuration, your identity provider's session limits also apply. For more information, see [How sign-in works with a dedicated identity provider](desktop-enterprise-advanced-idp.md#desktop-enterprise-how-it-works).

The desktop application stores its tokens in the operating system credential vault, with either sign-in method. For more information, see [Sign-in and credentials](desktop-security.md#desktop-security-sign-in).

## Moving from the desktop extension to the desktop connector
<a name="desktop-enterprise-migrate"></a>

If your organization set up enterprise sign-in with a desktop extension, that setup keeps working. There's no planned end date for the desktop extension, so you can move to the desktop connector at any time.

**To move to the desktop connector**

1. Update the desktop application on every device to version 1.1.4053 or later. To check the version, choose **Amazon Quick** > **About Amazon Quick** in the menu bar.

1. Add the desktop connector. For instructions, see [Turning on desktop access](#desktop-enterprise-turn-on).

1. After all users have updated to version 1.1.4053 or later, delete the desktop extension on the **Extensions** page in the Amazon Quick console.

**Important**  
Don't delete the extension until all users have moved. Users who haven't moved yet lose access. Older versions of the application show this error: "Enterprise sign-in for Quick Desktop has not been configured for this account. Contact your IT team for further support."

**Warning**  
If you use the `DisableAutoUpdates` policy, devices don't update automatically. Deploy version 1.1.4053 or later to every device before you add the connector. For more information, see [Application updates](desktop-enterprise-managed-deployment.md#desktop-enterprise-updates).

**Topics**
+ [Prerequisites](#desktop-enterprise-prerequisites)
+ [Turning on desktop access](#desktop-enterprise-turn-on)
+ [How sign-in works](#desktop-enterprise-sign-in)
+ [Moving from the desktop extension to the desktop connector](#desktop-enterprise-migrate)
+ [Using a dedicated identity provider configuration (advanced)](desktop-enterprise-advanced-idp.md)
+ [Managed deployment configuration](desktop-enterprise-managed-deployment.md)
+ [Troubleshooting enterprise sign-in for Amazon Quick on desktop](desktop-enterprise-setup-troubleshooting.md)
+ [Deploying Amazon Quick on desktop to a managed fleet with MDM](desktop-enterprise-mdm.md)