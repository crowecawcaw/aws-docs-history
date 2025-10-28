# Configuring Domo

Before you can use AWS Glue to transfer data from Domo to supported destinations, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have a Domo account enabled for API access.
- You have an app under your Domo developer account that provides the client credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [Creating a Domo developer app](#domo-configuring-creating-developer-app "#domo-configuring-creating-developer-app").

If you meet these requirements, you’re ready to connect AWS Glue to your Domo account.

## Creating a Domo developer app

To get the Client ID and Client Secret you create a developer account.

1. Go to the [Domo developer login page.](https://developer.domo.com/manage-clients "https://developer.domo.com/manage-clients")
2. Choose **Login**.
3. Provide the domain name and click **Continue**.
4. Hover on **My Account** and choose **New Client**.
5. Provide the Name and Description and select the scope ("data") and choose **Create**.
6. Retrieve the generated **Client Id** and **Client Secret** from the new client created.
