# Configuring Kustomer

Before you can use AWS Glue to transfer data from Kustomer to supported destinations, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have an account with Kustomer that contains the data that you want to transfer.
- In the settings for your account, you've created a API key. For more information, see [Creating an API key](#kustomer-configuring-creating-an-api-key "#kustomer-configuring-creating-an-api-key").
- You provide the API key to AWS Glue while creating the connection.

If you meet these requirements, you’re ready to connect AWS Glue to your Kustomer account.

## Creating an API key

To create an API key that you will use to create a connection for the Kustomer connector in AWS Glue Studio:

1. Log in to the [Kustomer dashboard using your credentials.](https://amazon-appflow.kustomerapp.com/login "https://amazon-appflow.kustomerapp.com/login")
2. Choose the **Settings** icon from the left menu.
3. Expand the **Security** drop down and select **API Keys**.
4. In the API Key creation page select **Add an API Key** from the top right corner.
5. Fill the mandatory inputs for the API key being created.
   - Name: any name for your API Key.
   - Roles: 'org' must be selected for the Kustomer APIs to function.
   - Expires (in days): the number of days you want the API key to be valid. You can keep it as **Never expires**, if it suits your use case.

6. Choose **Create**.
7. Store the API key (token) value for further usage to create a connection for the Kustomer connector in AWS Glue Studio.
