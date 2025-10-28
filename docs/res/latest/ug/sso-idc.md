# Setting up single sign-on (SSO) with IAM Identity Center

If you do not already have an identity center connected to the managed Active Directory,
start with [Step 1: Set up an identity center](#set-up-identity-center "#set-up-identity-center").
If you already have an identity center connected with the managed Active Directory, start
with [Step 2: Connect to an identity center](#connect-identity-center "#connect-identity-center").

###### Note

If you are deploying to a GovCloud Region, set up SSO in the AWS GovCloud (US)
partition account where you deployed Research and Engineering Studio.

## Step 1: Set up an identity center

1. Sign in to the [AWS Identity and Access Management console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. Open the **Identity Center**.
3. Choose **Enable**.
4. Choose **Enable with AWS Organizations**.
5. Choose **Continue**.

###### Note

Make sure you are in the same Region where you have your managed
Active Directory.

After you enable IAM Identity Center, complete these recommended set up steps:

1. In the navigation pane, choose **Settings**.
2. Under **Identity source**, choose **Actions**
   and choose **Change identity source**.
3. Under **Existing directories**, select your directory.
4. Choose **Next**.
5. Review your changes and enter `ACCEPT` in the
   confirmation box.
6. Choose **Change identity source**.
   Once the changes made in [Connecting IAM Identity Center to a managed
   Active Directory](#connecting-identity-center-ad "#connecting-identity-center-ad") are complete, a green confirmation
   banner appears.

7. In the confirmation banner, choose **Start guided setup**.
8. From **Configure attribute mappings**, choose
   **Next**.
9. Under the **User** section, enter the users you
   want to sync.
10. Choose **Add**.
11. Choose **Next**.
12. Review your changes, then choose **Save configuration**.
13. The sync process may take a few minutes. If you receive a warning
    message about users not syncing, choose **Resume sync**.
14. From the menu, choose **Users**.
15. Select the user(s) for whom you want to enable access.
16. Choose **Enable user access**.

## Step 2: Connect to an identity center

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Choose **Applications**.
3. Choose **Add application**.
4. Under **Setup preference**, choose **I have
   an application I want to set up**.
5. Under **Application type**, choose **SAML
   2.0**.
6. Choose **Next**.
7. Enter the display name and description you would like to use.
8. Under **IAM Identity Center metadata**, copy
   the link for the **IAM Identity Center SAML metadata**
   file. You will need this when configuring IAM Identity Center with the RES
   portal.
9. Under **Application properties**, enter your
   **Application start URL**. For example,
   `<your-portal-domain>/sso`.
10. Under **Application ACS URL**, enter the redirect
    URL from the RES portal. To find this:
    1. Under **Environment management**, choose
       **General settings**.
    2. Select the **Identity provider** tab.
    3. Under **Single Sign-On**, you will find the
       **SAML Redirect URL**.

11. Under **Application SAML audience**, enter the Amazon Cognito
    URN.

To create the urn:

    1. From the RES portal, open **General
     Settings**.
    2. Under the **Identity provider** tab, locate
     the **User Pool ID**.
    3. Add the **User Pool ID** to this string:



    ```
    urn:amazon:cognito:sp:`<user_pool_id>`
    ```

12. After you enter the Amazon Cognito URN, choose **Submit**.
1. From the **Identity Center**, open the details for
   your created application.
1. Choose **Actions**, then choose **Edit
   attribute mappings**.
1. Under **Subject**, enter
   `${user:email}`.
1. Under **Format**, choose
   **emailAddress**.
1. Choose **Add new attribute mapping**.
1. Under **User attribute in the application**,
   enter 'email'.
1. Under **Maps to this string value or user attribute in
   IAM Identity Center**, enter
   `${user:email}`.
1. Under **Format**, enter 'unspecified'.
1. Choose **Save changes**.
1. From the Identity Center, open **Assigned users** for
   your created application and choose **Assign users**.
1. Select the users you want to assign application access.
1. Choose **Assign users**.
1. From the Research and Engineering Studio environment, under **Environment management**,
   open **General settings**.
1. Open the **Identity provider** tab.
1. Under **Single Sign-On**, choose **Edit**
   (next to **Status**).
1. Complete the form with the following information:
   1. Choose **SAML**.
   2. Under **Provider name**, enter a user friendly
      name.
   3. Choose **Enter metadata document endpoint URL**.
   4. Enter the URL you copied during
      [Setting up the application
      in IAM Identity Center](#setup-application-identity-center "#setup-application-identity-center").
   5. Under **Provider email attribute**, enter
      'email'.
   6. Choose **Submit**.

1. Refresh the page and check that the **Status**
   displays as enabled.
