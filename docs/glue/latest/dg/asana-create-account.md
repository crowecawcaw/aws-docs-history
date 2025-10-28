# Creating an Asana account

1. Sign up for an [Asana
   Account](https://asana.com/create-account "https://asana.com/create-account") and choose **Sign Up**.
2. After logging in, you will be redirected to the [Account Setup](https://app.asana.com/0/account_setup "https://app.asana.com/0/account_setup") page.
   Complete the following steps:
   - Review the account setup form.
   - Fill in all the relevant details to create your Asana account.
   - Double-check the information for accuracy.

3. Choose **Create Account** or **Submit**
   (the exact button text may vary) to finalize your account setup.

###### Creating the App in Asana for `OAuth2.0`

1. Log in to Asana account using your [Asana Customer Credentials](https://app.asana.com/-/login "https://app.asana.com/-/login").
2. Choose your user profile icon in the top-right corner and select **My
   Settings** from the dropdown menu.
3. Select the **Apps** tab and then select **Manage
   Developer Apps**.
4. Select **Create new app** and enter the relevant details.
5. Choose **Create Apps**.
6. On the **My Apps** page:
   1. Select **OAuth** and in the **App
      Credentials** section, make a note of your Client ID and
      Client Secret.
   2. In the **Redirect URLs** section, add the necessary
      redirect URL(s).

   ###### Note

   Enter the Redirect URI using this format:
   `https://{aws-region-code}.console.aws.amazon.com/gluestudio/oauth`.
   Example: For the US East (N. Virginia), use:
   `https://us-east-1.console.aws.amazon.com/gluestudio/oauth`

###### Creating the App in Asana for `PAT` Token

1. Log in to Asana account using your [Asana Customer Credentials](https://app.asana.com/-/login "https://app.asana.com/-/login").
2. Choose on your user profile icon in the top-right corner and select **My
   Profile Settings** from the dropdown menu.
3. Select the **Apps** tab and then select **Service accounts**.
4. Select **Create new app** and enter the relevant details.
5. Choose **Add service account**.
6. The next page displays your token, copy your token and store it securely.

###### Important

This token will only be displayed once. Ensure you copy it and store it securely.
