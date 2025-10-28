# Configuring Zendesk

Before you can use AWS Glue to transfer data from Zendesk, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have a Zendesk account. For more information, see [Creating a Zendesk account](#zendesk-configuring-creating-account "#zendesk-configuring-creating-account").
- Your Zendesk account is enabled for API access.
- Your Zendesk account allows you to install connected apps.

If you meet these requirements, you’re ready to connect AWS Glue to your Zendesk account.

## Creating a Zendesk account

To create a Zendesk account:

1. Go to https://www.zendesk.com/in/register/
2. Enter the details such as your work email, first name, last name, phone number, job title, company name, number of employees in company, password and preferred Language. Then choose **Complete trial Signup**.
3. Once your account is created, complete the verification link you received to verify your email address.
4. Once the work email address is verified, you are redirected to your Zendesk account. Choose the **Buy Zendesk option** for your preferred plan. Note: for the Zendesk connector it is recommended to purchase the Suite Enterprise plan.

## Creating a client app and OAuth 2.0 credentials

To create a client app and OAuth 2.0 credentials:

1. Log into your Zendesk account where you want the OAuth 2.0 app to be created https://www.zendesk.com/in/login/
2. Click the gear icon. Choose the **Go to admin center** link to open the admin center page.
3. Choose **Apps and integrations** in the left sidebar, then select **APIs** > **Zendesk API**.
4. On the Zendesk API page, choose the **OAuth Clients** tab.
5. Choose **Add Oauth Client** on the right side.
6. Complete the following fields to create a client:
   1. Client Name - Enter a name for your app. This is the name that users will see when asked to grant access to your application, and when they check the list of third-party apps that have access to their Zendesk.
   2. Description - Optional. A short description of your app that users will see when asked to grant access to it.
   3. Company - Optional. The company name that users will see when asked to grant access to your application. The information can help them understand who they're granting access to.
   4. Logo - Optional. This is the logo that users will see when asked to grant access to your application. The image can be JPG, GIF, or PNG. For best results, upload a square image. It will be resized for the authorization page.
   5. Unique Identifier - The field is auto-populated with a reformatted version of the name you entered for your app. You can change it if you want.
   6. Redirect URLs - Enter the URL or URLs that Zendesk should use to send the user's decision to grant access to your application.

   For example: https://us-east-1.console.aws.amazon.com/gluestudio/oauth

7. Click **Save**.
8. After the page refreshes, a new pre-populated **Secret** field appears on the lower side. This is the "client_secret" value specified in the OAuth2 spec. Copy the Secret value to your clipboard and save it somewhere safe. Note: The characters may extend past the width of the text box, so make sure to select everything before copying.
9. Click **Save**.
