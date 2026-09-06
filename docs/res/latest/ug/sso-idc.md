

# Setting up single sign-on (SSO) with IAM Identity Center
<a name="sso-idc"></a>

If you do not already have an identity center connected to the managed Active Directory, start with [Step 1: Set up an identity center](#set-up-identity-center). If you already have an identity center connected with the managed Active Directory, start with [Step 2: Connect to an identity center](#connect-identity-center).

**Note**  
If you are deploying to a GovCloud Region, set up SSO in the AWS GovCloud (US) partition account where you deployed Research and Engineering Studio.

## Step 1: Set up an identity center
<a name="set-up-identity-center"></a>

### Enabling IAM Identity Center
<a name="enabling-identity-center"></a>

1. Sign in to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam).

1. Open the **Identity Center**.

1. Choose **Enable**.

1. Choose **Enable with AWS Organizations**.

1. Choose **Continue**.

**Note**  
Make sure you are in the same Region where you have your managed Active Directory.

### Connecting IAM Identity Center to a managed Active Directory
<a name="connecting-identity-center-ad"></a>

After you enable IAM Identity Center, complete these recommended set up steps:

1. In the navigation pane, choose **Settings**.

1. Under **Identity source**, choose **Actions** and choose **Change identity source**.

1. Under **Existing directories**, select your directory.

1. Choose **Next**.

1. Review your changes and enter **ACCEPT** in the confirmation box.

1. Choose **Change identity source**.

### Syncing users and groups to identity center
<a name="syncing-identity-center"></a>

Once the changes made in [Connecting IAM Identity Center to a managed Active Directory](#connecting-identity-center-ad) are complete, a green confirmation banner appears.

1. In the confirmation banner, choose **Start guided setup**.

1. From **Configure attribute mappings**, choose **Next**.

1. Under the **User** section, enter the users you want to sync.

1. Choose **Add**.

1. Choose **Next**.

1. Review your changes, then choose **Save configuration**.

1. The sync process may take a few minutes. If you receive a warning message about users not syncing, choose **Resume sync**.

### Enabling users
<a name="enabling-users"></a>

1. From the menu, choose **Users**.

1. Select the user(s) for whom you want to enable access.

1. Choose **Enable user access**.

## Step 2: Connect to an identity center
<a name="connect-identity-center"></a>

### Setting up the application in IAM Identity Center
<a name="setup-application-identity-center"></a>

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. Choose **Applications**.

1. Choose **Add application**.

1. Under **Setup preference**, choose **I have an application I want to set up**.

1. Under **Application type**, choose **SAML 2.0**.

1. Choose **Next**.

1. Enter the display name and description you would like to use.

1. Under **IAM Identity Center metadata**, copy the link for the **IAM Identity Center SAML metadata** file. You will need this when configuring IAM Identity Center with the RES portal.

1. Under **Application properties**, enter your **Application start URL**. For example, `<your-portal-domain>/sso`.

1. Under **Application ACS URL**, enter the redirect URL from the RES portal. To find this: 

   1. Under **Environment management**, choose **General settings**.

   1. Select the **Identity provider** tab.

   1. Under **Single Sign-On**, you will find the **SAML Redirect URL**.

1. Under **Application SAML audience**, enter the Amazon Cognito URN.

   To create the urn:

   1. From the RES portal, open **General Settings**.

   1. Under the **Identity provider** tab, locate the **User Pool ID**. 

   1. Add the **User Pool ID** to this string: 

      ```
      urn:amazon:cognito:sp:{{<user_pool_id>}}
      ```

1. After you enter the Amazon Cognito URN, choose **Submit**.

### Configuring attribute mappings for the application
<a name="configure-attribute-mappings"></a>

1. From the **Identity Center**, open the details for your created application.

1. Choose **Actions**, then choose **Edit attribute mappings**. 

1. Under **Subject**, enter **${user:email}**.

1. Under **Format**, choose **emailAddress**.

1. Choose **Add new attribute mapping**. 

1. Under **User attribute in the application**, enter 'email'. 

1. Under **Maps to this string value or user attribute in IAM Identity Center**, enter **${user:email}**.

1. Under **Format**, enter 'unspecified'.

1. Choose **Save changes**.

### Adding users to the application in IAM Identity Center
<a name="add-users-to-application"></a>

1. From the Identity Center, open **Assigned users** for your created application and choose **Assign users**.

1. Select the users you want to assign application access.

1. Choose **Assign users**.

### Setting up IAM Identity Center within the RES environment
<a name="setup-sso-environment"></a>

1. From the Research and Engineering Studio environment, under **Environment management**, open **Identity Management**.

1. Under **Single Sign-On**, choose **Edit** (next to **Status**).

1. Complete the form with the following information:

   1. Choose **SAML**.

   1. Under **Provider name**, enter a user friendly name.

   1. Choose **Enter metadata document endpoint URL**.

   1. Enter the URL you copied during [Setting up the application in IAM Identity Center](#setup-application-identity-center).

   1. Under **Provider email attribute**, enter 'email'.

   1. Choose **Submit**.

1. Refresh the page and check that the **Status** displays as enabled. 