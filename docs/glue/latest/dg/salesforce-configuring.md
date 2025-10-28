# Configuring Salesforce

Before you can use AWS Glue to transfer data to or from Salesforce, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have a Salesforce account.
- Your Salesforce account is enabled for API access. API access is enabled by default for the Enterprise, Unlimited, Developer, and Performance editions.

If you meet these requirements, you’re ready to connect AWS Glue to your Salesforce account. AWS Glue handles the remaining requirements with the AWS managed connected app.

## The AWS managed connected app for Salesforce

The AWS managed connected app helps you create a Salesforce connection in fewer steps. In Salesforce, a connected app is a framework that authorizes external applications, like AWS Glue, to access your Salesforce data using OAuth 2.0. To use the AWS managed connected app, create a Salesforce connection by using the AWS Glue consule. When you configure the connection, set the **OAuth grant type** to **Authorization code** and leave the box checked for **Use AWS managed client application**.

When saving the connection, you will be redirected to Salesforce to login and approve AWS Glue access to your Salesforce account.

## Apply System Admin profile

In Salesforce, follow the steps to apply the System Admin profile:

1. In Salesforce, navigate to **Settings > Connected Apps > Connected Apps OAuth Usage**.
2. In the list of connected apps, find AWS Glue and choose **Install**. If needed, choose **Unblock**.
3. Navigate to **Settings > Manage Connected Apps then choose AWS Glue**. Under OAuth Policies, choose **Admin
   approved users are pre-authorized** and select the **System Admin** profile. This action restricts
   access to AWS Glue only to users with the System Admin profile.
