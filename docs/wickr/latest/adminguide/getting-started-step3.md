

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Step 3: Create and invite users
<a name="getting-started-step3"></a>

You can create users in your Wickr network using the following methods:
+ **Single sign-on** — If you configure SSO, you can invite users by sharing your Wickr company ID. End users register for Wickr using the provided company ID and their work email address. For more information, see [Single sign-on configuration for AWS Wickr](sso-configuration.md).
+ **Invitation** — You can manually create users in the AWS Management Console for Wickr and have an email invitation sent to them. End users can register for Wickr by choosing the link in the email.

**Note**  
You can also enable guest users for your Wickr network. For more information, see [Guest users in AWS Wickr network](guest-users.md)

Complete the following procedures to create or invite users.

**Note**  
Administrators are also considered users and must invite themselves to SSO or non-SSO Wickr networks.

**To create Wickr users and send invitations with SSO:**

Write and send an email to the SSO users who should sign up for Wickr. Include the following information in your email:
+ Your Wickr company ID. You specify a company ID for your Wickr network when you configure SSO. For more information, see [Configure SSO in AWS Wickr](configure-sso.md).
+ The email address they should use to sign up.
+ The URL to download the Wickr client. You can download the Wickr client from the AWS Wickr downloads page at [https://aws.amazon.com/wickr/download/](https://aws.amazon.com/wickr/download/).
**Note**  
If you created your Wickr network in AWS GovCloud (US-West), instruct your users to download and install the WickrGov client. For all other AWS Regions, instruct your users to download and install the standard Wickr client. For more information about AWS WickrGov, see [AWS WickrGov](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-wickr.html) in the *AWS GovCloud (US) User Guide*.

As users register for your Wickr network, they are added to the Wickr team directory with a status of **active**.

**To manually create Wickr users and send invitations:**

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

   You're redirected to the Wickr network. In the Wickr network, you can add users, add security groups, configure SSO, configure data retention, and adjust additional settings.

1. In the navigation pane, choose **User management**.

1. On the **User management** page, under the **Team directory** tab, choose **Invite user**.

   You can also bulk invite users by choosing the drop-down arrow next to **Invite user**. On the **Bulk invite users** page, select **Download template** to download a CSV template that you can edit and upload with your list of users.

1. Enter the user's first name, last name, country code, phone number, and email address. Email address is the only field that is required. Be sure to choose the appropriate security group for the user. 

1. Choose **Invite**.

   Wickr sends an invitation email to the address you specify for the user. The email provides download links for the Wickr client applications, and a link to register for Wickr. For more information about what this end user experience looks like, see [Download the Wickr app and accept your invitation](https://docs.aws.amazon.com/wickr/latest/userguide/getting-started.html#accept-invitation-step1) in the *AWS Wickr User Guide*.

   

   As users register for Wickr using the link in the email, their status in the Wickr team directory will change from **Pending** to **Active**.

## Next steps
<a name="getting-started-next-steps"></a>

You completed the getting started steps. To manage Wickr, see the following:
+ [Manage your AWS Wickr network](managing-network.md)
+ [Manage users in AWS Wickr](managing-users.md)