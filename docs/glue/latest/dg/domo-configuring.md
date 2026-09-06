

# Configuring Domo
<a name="domo-configuring"></a>

Before you can use AWS Glue to transfer data from Domo to supported destinations, you must meet these requirements:

## Minimum requirements
<a name="domo-configuring-min-requirements"></a>

The following are minimum requirements:
+ You have a Domo account enabled for API access.
+ You have an app under your Domo developer account that provides the client credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [Creating a Domo developer app](#domo-configuring-creating-developer-app).

If you meet these requirements, you’re ready to connect AWS Glue to your Domo account.

## Creating a Domo developer app
<a name="domo-configuring-creating-developer-app"></a>

To get the Client ID and Client Secret you create a developer account.

1. Go to the [Domo developer login page.](https://developer.domo.com/manage-clients)

1. Choose **Login**.

1. Provide the domain name and click **Continue**.

1. Hover on **My Account** and choose **New Client**.

1. Provide the Name and Description and select the scope ("data") and choose **Create**.

1. Retrieve the generated **Client Id** and **Client Secret** from the new client created.