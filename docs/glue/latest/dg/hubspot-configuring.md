# Configuring HubSpot

Before you can use AWS Glue to transfer data from HubSpot, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have a HubSpot account. For more information, see [Creating a HubSpot account](#hubspot-configuring-creating-hubspot-account "#hubspot-configuring-creating-hubspot-account").
- Your HubSpot account is enabled for API access.
- You should have an app under your HubSpot developer account that provides the client credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [Creating a HubSpot developer app](#hubspot-configuring-creating-hubspot-developer-app "#hubspot-configuring-creating-hubspot-developer-app").

If you meet these requirements, you’re ready to connect AWS Glue to your HubSpot account. For typical connections, you don't have do anything else in HubSpot.

## Creating a HubSpot account

To create a HubSpot account:

1. Go to the [HubSpot CRM SignUp URL](https://app.hubspot.com/login "https://app.hubspot.com/login").
2. Enter your email address and choose **Verify email** (alternatively, you can choose to sign up with a Google, Microsoft or Apple account).
3. Check your inbox for the verification code from HubSpot.
4. Enter the 6-digit verification code and click **Next**.
5. Enter a password and click **Next**.
6. Enter your first name and last name and click **Next**, or sign up using the **Sign up with Google** link.
7. Enter your industry and click **Next**.
8. Enter your job role and click **Next**.
9. Enter your company name and click **Next**.
10. Select the size of your company (number of employees working in your company) and click **Next**.
11. Enter your company website and click **Next**.
12. Select where your data should be hosted (United States or Europe) and click **Create Account**.
13. Select the purpose of your account creation and click **Next**.
14. Choose **Connect Google Account** or choose to add contacts yourself to link your contacts with your HubSpot account.
15. Log in to your Google account if you chose the **Connect Google Account** option to link your contacts and start using your HubSpot account.

## Creating a HubSpot developer app

App developer accounts are intended for creating and managing apps, integrations, and developer test accounts. They're also where you can create and manage App Marketplace listings. However, app developer accounts and their associated test accounts aren’t connected to a standard HubSpot account. They can't sync data or assets to or from another HubSpot account. To get the Client ID and Client Secret you create a developers account.

1. Go to https://developers.hubspot.com/
2. Choose **Create developer account** and scroll down.
3. You will be asked whether you want to create an App developers account, Private App account, or CMS Developer Sandbox account. Choose **Create App developers account**.
4. Since you already created an Account with HubSpot, you can choose **Continue with this user**.
5. Click **Start signup**.
6. Enter your Job Role and click **Next**.
7. Name your developer account and click **Next**, then **Skip**.
8. Choose **Create App**.
9. Once your App is created, choose **Auth**.
10. Under Auth, note the Client ID and Client Secret.
11. Add your region specific **Redirect URL** as https:`//<aws-region>`.console.aws.amazon.com/gluestudio/oauth. For example, add https://us-east-1.console.aws.amazon.com/gluestudio/oauth for the us-east-1 region.
12. Scroll down and find scopes. There are two kinds of scopes you must select under headings "CRM" and "Standard".
13. Add the following scopes:

```
content
automation
oauth
crm.objects.owners.read
forms
tickets
crm.objects.contacts.write
e-commerce
crm.schemas.custom.read
crm.objects.custom.read
sales-email-read
crm.objects.custom.write
crm.objects.companies.write
crm.lists.write
crm.objects.companies.read
crm.lists.read
crm.objects.deals.read
crm.objects.deals.write
crm.objects.contacts.read

```

14. Click **Save** and your dev account is now ready to use.
15. Scroll above to find the **Client ID**.
16. On the same page, click **Show** to get the **Client secret**.

## Creating a HubSpot developer test account

Within app developer accounts, you can create developer test accounts to test apps and integrations without affecting any real HubSpot data. Developer test accounts do not mirror production accounts, but rather have access to a 90-day trial of
the Enterprise versions of Marketing, Sales, Service, CMS, and Operations Hub, providing the ability to test most HubSpot tools and APIs.

1. Click **Home**.
2. Click **Create test account**.
3. Click **Create App Test Account**.
4. A new window appears. Enter the app test account name and click **Create**.

Your app test account is now created.

###### Note

The developer account is related to development activities such as API integration, and the app test account is used to see the data which is created or pulled by the developer account.
