

# Enable automatic provisioning
<a name="how-to-with-scim"></a>

Use the following procedure to enable automatic provisioning of users and groups from your IdP to IAM Identity Center using the SCIM protocol.

**Note**  
Before you begin this procedure, we recommend that you first review provisioning considerations that are applicable to your IdP. For more information, see the [IAM Identity Center identity source tutorials](tutorials.md) for your IdP.

**To enable automatic provisioning in IAM Identity Center**

1. After you have completed the prerequisites, open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings** in the left navigation pane.

1. On the **Settings** page, locate the **Automatic provisioning** information box, and then choose **Enable**. This immediately enables automatic provisioning in IAM Identity Center and displays the necessary SCIM endpoint and access token information.

1. In the **Inbound automatic provisioning** dialog box, copy the SCIM endpoint and access token. You'll need to paste these in later when you configure provisioning in your IdP.

   1. **SCIM endpoint** - For example, https://scim.{{us-east-2}}.amazonaws.com/{{11111111111-2222-3333-4444-555555555555}}/scim/v2

   1. **Access token** - Choose **Show token** to copy the value.
**Warning**  
This is the only time where you can obtain the SCIM endpoint and access token. Ensure you copy these values before moving forward. You will enter these values to configure automatic provisioning in your IdP later in this tutorial. 

1. Choose **Close**.

After you complete this procedure, you must configure automatic provisioning in your IdP. For more information, see the [IAM Identity Center identity source tutorials](tutorials.md) for your IdP.