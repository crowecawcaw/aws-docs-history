# Creating an Productboard account

1. Navigate to the [Productboard
   sign up page](https://app.productboard.com/ "https://app.productboard.com/"), enter your email ID and password, and then choose
   **Log me in**.
2. In the **Account Name** field, enter the name of your Productboard account,
   and then select the **I agree to the Privacy Policy check** box.
3. On the **Now create your workspace** page, in the **Workspace URL** field, enter the URL for your new workspace.
   Then choose **Continue** to proceed to the next page and provide the remaining details.

This creates your trial account. The trial account is free for 15 days. After the trial period expires, you can purchase a paid plan.
Make a note of your email address, password, and workspace URL. You will need this information to access your account in the future."

###### Registering an `OAuth2.0` application

1. Navigate to the [Productboard
   login page](https://login.productboard.com/?locale=en "https://login.productboard.com/?locale=en"), enter your email ID and password, and choose
   **Log in**.
2. Select the **User** icon in the upper-right corner, and then choose **Account and billing** from the dropdown menu.
3. Select **Extras** and choose **Registered apps** from the dropdown menu.
4. Locate and choose **Register An App**.
5. Enter the following details:
   - **App name** – Name of the app.
   - **Company / Organization** – Name of your Company or Organization.
   - **App website** – Website of the app.
   - **Redirect URI** – A Redirect URI pattern is a URI path (or
     comma-separated list of paths) to which Productboard can redirect (if
     requested) when the login flow is complete. For example,
     `https://ap-southeast-2\\.console\\.aws\\.amazon\\.com`

6. Choose **Create**.
7. The **Client ID** and **Client Secret** will
   now be visible. Copy and save them in a secure location. Then, choose
   **Done**.

###### Note

Your Client ID and Client Secret strings are credentials used to establish
a connection with this connector when using AppFlow or AWS Glue.

###### Retrieving CustomAuth Credentials

1. Navigate to the [Productboard
   login page](https://app.productboard.com/ "https://app.productboard.com/"), enter your email ID and password, and choose
   **Log me in**.

You will be redirected to the home page. 2. On the home page, navigate to **Workspace Settings** > **Integrations** >
**Public APIs** > **Access Token**.

###### Note

If the **Public APIs** section is not visible, your account might be on the
Essentials plan. Access to API tokens requires at least a Pro plan. Plan
features and names are subject to change. For more information about the
packages, see [Productboard pricing](https://www.productboard.com/pricing/ "https://www.productboard.com/pricing/"). 3. Choose **+** to generate a new token, and make sure to securely store it for future reference.

###### Creating `OAuth2.0` credentials

To utilize `OAuth2.0` authentication with the Productboard connector, you need to register your
application on the Productboard platform and generate a `Client ID` and `Client Secret`.

1. Navigate to the [Productboard login
   page](https://app.productboard.com/ "https://app.productboard.com/"), enter your email ID and password, and choose **Log me
   in**.
2. To register new OAuth2 application with your Productboard account, navigate to
   [Producboard](to register new OAuth2 application with your Productboard account.md "to register new OAuth2 application with your Productboard account.md") page.
3. Complete the required fields and select the necessary scopes for each entity
   you wish to access.

###### Note

You have chosen the following four scopes, which are required for the six
supported entities. 4. **Redirect URL** must have the following format:
`https://ap-southeast-2\\.console\\.aws\\.amazon\\.com`

###### Note

The Appflow redirect URLs are subject to change. Once available, please
update the redirect URLs for the AWS Glue platform. 5. The **Client ID** and **Client Secret** will
now be visible. Copy and save them in a secure location. 6. You can set up and verify `OAuth2` by following the steps in the
[How to Integrate with Productboard via OAuth2 developer](https://developer.productboard.com/docs/how-to-integrate-with-productboard-via-oauth2-developer-documentation "https://developer.productboard.com/docs/how-to-integrate-with-productboard-via-oauth2-developer-documentation")
documentation.
