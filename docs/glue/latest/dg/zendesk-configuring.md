

# Configuring Zendesk
<a name="zendesk-configuring"></a>

Before you can use AWS Glue to transfer data from Zendesk, you must meet these requirements:

## Minimum requirements
<a name="zendesk-configuring-min-requirements"></a>

The following are minimum requirements:
+ You have a Zendesk account. For more information, see [Creating a Zendesk account](#zendesk-configuring-creating-account).
+ Your Zendesk account is enabled for API access.
+ Your Zendesk account allows you to install connected apps.

If you meet these requirements, you’re ready to connect AWS Glue to your Zendesk account.

## Creating a Zendesk account
<a name="zendesk-configuring-creating-account"></a>

To create a Zendesk account:

1. Go to https://www.zendesk.com/in/register/

1. Enter the details such as your work email, first name, last name, phone number, job title, company name, number of employees in company, password and preferred Language. Then choose **Complete trial Signup**.

1. Once your account is created, complete the verification link you received to verify your email address.

1. Once the work email address is verified, you are redirected to your Zendesk account. Choose the **Buy Zendesk option** for your preferred plan. Note: for the Zendesk connector it is recommended to purchase the Suite Enterprise plan.

## Creating a client app and OAuth 2.0 credentials
<a name="zendesk-configuring-creating-client-app"></a>

To create a client app and OAuth 2.0 credentials:

1. Log into your Zendesk account where you want the OAuth 2.0 app to be created https://www.zendesk.com/in/login/

1. Click the gear icon. Choose the **Go to admin center** link to open the admin center page.

1. Choose **Apps and integrations** in the left sidebar, then select **APIs** > **Zendesk API**.

1. On the Zendesk API page, choose the **OAuth Clients** tab.

1. Choose **Add Oauth Client** on the right side.

1. Complete the following fields to create a client:

   1. Client Name - Enter a name for your app. This is the name that users will see when asked to grant access to your application, and when they check the list of third-party apps that have access to their Zendesk.

   1. Description - Optional. A short description of your app that users will see when asked to grant access to it.

   1. Company - Optional. The company name that users will see when asked to grant access to your application. The information can help them understand who they're granting access to.

   1. Logo - Optional. This is the logo that users will see when asked to grant access to your application. The image can be JPG, GIF, or PNG. For best results, upload a square image. It will be resized for the authorization page.

   1. Unique Identifier - The field is auto-populated with a reformatted version of the name you entered for your app. You can change it if you want.

   1. Redirect URLs - Enter the URL or URLs that Zendesk should use to send the user's decision to grant access to your application.

      For example: https://us-east-1.console.aws.amazon.com/gluestudio/oauth

1. Click **Save**.

1. After the page refreshes, a new pre-populated **Secret** field appears on the lower side. This is the "client\_secret" value specified in the OAuth2 spec. Copy the Secret value to your clipboard and save it somewhere safe. Note: The characters may extend past the width of the text box, so make sure to select everything before copying.

1. Click **Save**.