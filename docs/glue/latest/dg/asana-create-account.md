

# Creating an Asana account
<a name="asana-create-account"></a>

1. Sign up for an [Asana Account](https://asana.com/create-account) and choose **Sign Up**.

1. After logging in, you will be redirected to the [Account Setup](https://app.asana.com/0/account_setup) page. Complete the following steps:
   + Review the account setup form.
   + Fill in all the relevant details to create your Asana account.
   + Double-check the information for accuracy.

1. Choose **Create Account** or **Submit** (the exact button text may vary) to finalize your account setup.

**Creating the App in Asana for `OAuth2.0`**

1. Log in to Asana account using your [Asana Customer Credentials](https://app.asana.com/-/login). 

1. Choose your user profile icon in the top-right corner and select **My Settings** from the dropdown menu.

1. Select the **Apps** tab and then select **Manage Developer Apps**.

1. Select **Create new app** and enter the relevant details. 

1. Choose **Create Apps**.

1. On the **My Apps** page: 

   1. Select **OAuth** and in the **App Credentials** section, make a note of your Client ID and Client Secret.

   1. In the **Redirect URLs** section, add the necessary redirect URL(s).
**Note**  
Enter the Redirect URI using this format: `https://{aws-region-code}.console.aws.amazon.com/gluestudio/oauth`. Example: For the US East (N. Virginia), use: `https://us-east-1.console.aws.amazon.com/gluestudio/oauth`

**Creating the App in Asana for `PAT` Token**

1. Log in to Asana account using your [Asana Customer Credentials](https://app.asana.com/-/login). 

1. Choose on your user profile icon in the top-right corner and select **My Profile Settings** from the dropdown menu.

1. Select the **Apps** tab and then select **Service accounts**.

1. Select **Create new app** and enter the relevant details. 

1. Choose **Add service account**.

1. The next page displays your token, copy your token and store it securely. 
**Important**  
This token will only be displayed once. Ensure you copy it and store it securely. 