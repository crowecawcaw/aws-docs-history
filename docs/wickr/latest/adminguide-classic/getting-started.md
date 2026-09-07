

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Getting started with AWS Wickr
<a name="getting-started"></a>

In this guide, we show you how to get started with Wickr by creating a network, configuring your network, and creating users.

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Step 1: Create a network](#getting-started-step1)
+ [Step 2: Configure your network](#getting-started-step2)
+ [Step 3: Create and invite users](#getting-started-step3)
+ [Next steps](#getting-started-next-steps)
+ [Transfer Wickr Pro to AWS Wickr](transfer-wickr-pro-to-aws-wickr.md)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Before you start, be sure to complete the following prerequisites if you haven't already:
+ Sign up for Amazon Web Services (AWS). For more information, see [Setting up for AWS Wickr](setting-up.md).
+ Ensure that you have the permissions required to administer Wickr. For more information, see [AWS managed policy: AWSWickrFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWickrFullAccess).
+ Make sure you allow list the appropriate ports and domains for Wickr. For more information, see [Ports and domains to allow list for your Wickr network](allow-list-ports-domains.md).

## Step 1: Create a network
<a name="getting-started-step1"></a>

Complete the following procedure to create a Wickr network for your account.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).
**Note**  
If you haven't created a Wickr networking before, you will see the informational page for the Wickr service. After you create one or more Wickr networks, you will see the **Networks** page, which contains a list view of all the Wickr networks you have created.

1. Choose **Create a network**.  
![The AWS Management Console for Wickr.](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/wickr-create-a-network-button.png)

1. Enter a name for your network in the **Network name** text box. Choose a name that members of your organization will recognize, such as the name of your company or the name of your team.

1. Choose a plan. You can choose one of the following Wickr network plans:
   + **Standard —** For small and large business teams that need administrative controls and flexibility.
   + **Premium** or **Premium Free Trial —** For businesses that require the highest feature limits, granular administrative controls, and data retention.

   Administrators can choose the premium free trial option, which is available for up to 30 users and lasts three months. This offer is open to new, legacy-free trial, and standard plans. Administrators can upgrade or downgrade to Premium or Standard plans during the premium free trial period.

   For more information about available Wickr plans and pricing, see the [Wickr pricing page](https://aws.amazon.com/wickr/pricing/).

1. (Optional) Choose **Add new tag** to add a tag to your network. Tags consist of a key value pair. Tags can be used to search and filter resources or track your AWS costs. For more information, see[ Network tags](network-tags.md).

1. Choose **Create Network**.

   You are redirected to the **Networks** page of the AWS Management Console for Wickr, and the new network is listed on the page.

## Step 2: Configure your network
<a name="getting-started-step2"></a>

Complete the following procedure to access the Wickr Admin Console, where you can add users, add security groups, configure SSO, configure data retention, and additional network settings.

1. On the **Networks** page, choose the **Admin** link, to navigate to Wickr Admin Console for that network.  
![The Networks page.](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/wickr-networks-page.png)

   You're redirected to the Wickr Admin Console for the selected network.

1. In the navigation pane of the Wickr Admin Console, choose **Network Settings**.  
![The Wickr Network Dashboard page of the Wickr Admin Console.](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/wickr-network-settings.png)

   The following network setting options are available. For more information about configuring these settings, see [Manage your AWS Wickr network](managing-network.md).
   + **Security Group** — Manage security groups and their settings, such as password complexity policies, messaging preferences, calling features, security features and external federation. For more information, see [Security groups for AWS Wickr](security-groups.md).
   + **SSO Configuration** — Configure SSO and view the endpoint address for your Wickr network. Wickr supports SSO providers who use OpenID Connect (OIDC) only. Providers who use Security Assertion Markup Language (SAML) are not supported. For more information, see [Single sign-on configuration for AWS Wickr](sso-configuration.md).

## Step 3: Create and invite users
<a name="getting-started-step3"></a>

You can create users in your Wickr network using the following methods:
+ **Single sign-on** — If you configure SSO, you can invite users by sharing your Wickr company ID. End users register for Wickr using the provided company ID and their work email address. For more information, see [Single sign-on configuration for AWS Wickr](sso-configuration.md).
+ **Invitation** — You can manually create users in the AWS Management Console for Wickr and have an email invitation sent to them. End users can register for Wickr by choosing the link in the email.

**Note**  
You can also enable guest users for your Wickr network. The guest user feature is currently in preview. For more information, see [Guest users in AWS Wickr network](guest-users.md)

Complete the following procedures to create or invite users.

**Note**  
Administrators are also considered users and must invite themselves to SSO or non-SSO Wickr networks.

------
#### [ SSO ]

Write and send an email to the SSO users who should sign up for Wickr. Include the following information in your email:
+ Your Wickr company ID. You specify a company ID for your Wickr network when you configure SSO. For more information, see [Configure SSO in AWS Wickr](configure-sso.md).
+ The email address they should use to sign up.
+ The URL to download the Wickr client. You can download the Wickr client from the AWS Wickr downloads page at [https://aws.amazon.com/wickr/download/](https://aws.amazon.com/wickr/download/).
**Note**  
If you created your Wickr network in AWS GovCloud (US-West), instruct your users to download and install the WickrGov client. For all other AWS Regions, instruct your users to download and install the standard Wickr client. For more information about AWS WickrGov, see [AWS WickrGov](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-wickr.html) in the *AWS GovCloud (US) User Guide*.

As users register for your Wickr network, they are added to the Wickr team directory with a status of **active**.

------
#### [ Non-SSO ]

**To manually create Wickr users and send invitations:**

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, choose the **Admin** link, to navigate to Wickr Admin Console for that network.  
![](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/wickr-networks-page.png)

   You're redirected to the Wickr Admin Console for a specific network. On the Wickr Admin Console, you can add users, add security groups, configure SSO, configure data retention, and additional settings for the specific network you selected.

1. In the navigation pane of the Wickr Admin Console, choose **Users**, and then choose **Team Directory**.

   In the **Users** page, you can add individual users by choosing **Create new user**. You can also bulk add users by choosing the **Add users** icon in the top navigation pane. Choose the **Download CSV** icon to download a CSV template that you can edit and upload with your list of users.

1. Enter the user's first name, last name, country code, phone number, and email address. Email address is the only field that is required. Be sure to choose the appropriate security group for the user. 

1. Choose **Create**.  
![The New User page of the Wickr Admin Console.](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/wickr-new-user.png)

   Wickr sends an invitation email to the address you specify for the user. The email provides download links for the Wickr client applications, and a link to register for Wickr. For more information about what this end user experience looks like, see [Download the Wickr app and accept your invitation](https://docs.aws.amazon.com/wickr/latest/userguide/getting-started.html#accept-invitation-step1) in the *AWS Wickr User Guide*.

   

   As users register for Wickr using the link in the email, their status in the Wickr team directory will change from **Pending** to **Active**.  
![The New User page of the Wickr Admin Console.](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/wickr-team-directory.png)

------

## Next steps
<a name="getting-started-next-steps"></a>

You completed the getting started steps. To manage Wickr, see the following guides:
+ [Manage your AWS Wickr network](managing-network.md)
+ [Manage users in AWS Wickr](managing-users.md)