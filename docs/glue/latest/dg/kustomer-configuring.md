

# Configuring Kustomer
<a name="kustomer-configuring"></a>

Before you can use AWS Glue to transfer data from Kustomer to supported destinations, you must meet these requirements:

## Minimum requirements
<a name="kustomer-configuring-min-requirements"></a>

The following are minimum requirements:
+ You have an account with Kustomer that contains the data that you want to transfer. 
+ In the settings for your account, you've created a API key. For more information, see [Creating an API key](#kustomer-configuring-creating-an-api-key).
+ You provide the API key to AWS Glue while creating the connection.

If you meet these requirements, you’re ready to connect AWS Glue to your Kustomer account.

## Creating an API key
<a name="kustomer-configuring-creating-an-api-key"></a>

To create an API key that you will use to create a connection for the Kustomer connector in AWS Glue Studio:

1. Log in to the [Kustomer dashboard using your credentials.](https://amazon-appflow.kustomerapp.com/login)

1. Choose the **Settings** icon from the left menu.

1. Expand the **Security** drop down and select **API Keys**.

1. In the API Key creation page select **Add an API Key** from the top right corner.

1. Fill the mandatory inputs for the API key being created.
   + Name: any name for your API Key.
   + Roles: 'org' must be selected for the Kustomer APIs to function.
   + Expires (in days): the number of days you want the API key to be valid. You can keep it as **Never expires**, if it suits your use case.

1. Choose **Create**.

1. Store the API key (token) value for further usage to create a connection for the Kustomer connector in AWS Glue Studio.