# Set up connections to data sources with OAuth

The following section describes the steps you must take to set up OAuth connections to
data sources from SageMaker Canvas. [OAuth](https://oauth.net/2/ "https://oauth.net/2/") is a common authentication platform for granting access to
resources without sharing passwords. With OAuth, you can quickly connect to your data from
Canvas and import it for building models. Canvas currently supports OAuth for Snowflake and
Salesforce Data Cloud.

###### Note

You can only establish one OAuth connection for each data source.

## Set up OAuth for Salesforce Data Cloud

To set up OAuth for Salesforce Data Cloud, follow these general steps:

1. Sign in to Salesforce Data Cloud.
2. In Salesforce Data Cloud, create a new app connection and do the following:
   1. Enable OAuth settings.
   2. When prompted for a callback URL (or the URL of the resource accessing your data),
      specify the URL for your Canvas application. The Canvas application URL follows this format:
      `https://`<domain-id>`.studio.`<region>`.sagemaker.aws/canvas/default`
   3. Copy the consumer key and secret.
   4. Copy your authorization URL and token URL.

For more detailed instructions about performing the preceding tasks in Salesforce Data Cloud, see
[Import data from Salesforce Data Cloud](data-wrangler-import.md#data-wrangler-import-salesforce-data-cloud "data-wrangler-import.md#data-wrangler-import-salesforce-data-cloud")
in the Data Wrangler documentation for importing data from Salesforce Data Cloud.

After enabling access from Salesforce Data Cloud and getting your connection information, you
must create an [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") secret to store the information and add it to your
Amazon SageMaker AI domain or user profile. Note that you can add a secret to both a domain and
user profile, but Canvas looks for secrets in the user profile first.

To add a secret to your domain or user profile, do the following:

1. Go to the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Choose **domains** in the navigation pane.
3. From the list of **domains**, choose your domain.
   1. If adding your secret to your domain, do the following:
      1. Choose the domain.
      2. On the **domain settings** page, choose the **domain settings**
         tab.
      3. Choose **Edit**.

   2. If adding the secret to your user profile, do the
      following:
      1. Choose the user’s domain.
      2. On the **domain settings** page, choose the user
         profile.
      3. On the **User Details** page,
         choose **Edit**.

4. In the navigation pane, choose **Canvas settings**.
5. For **OAuth settings**, choose
   **Add OAuth configuration**.
6. For **Data source**, select **Salesforce Data Cloud**.
7. For **Secret Setup**, select
   **Create a new secret**.
   Alternatively, if you already created an AWS Secrets Manager secret
   with your credentials, enter the ARN for the secret. If creating a
   new secret, do the following:
   1. For **Identity Provider**, select
      **SALESFORCE**.
   2. For **Client ID**, **Client Secret**, **Authorization URL**, and **Token URL**, enter all of the information you
      gathered from Salesforce Data Cloud in the previous procedure.

8. Save your domain or user profile settings.

You should now be able to create a connection to your data in Salesforce Data Cloud from Canvas.

## Set up OAuth for Snowflake

To set up authentication for Snowflake, Canvas supports identity providers that you can use instead of having users directly enter their credentials into Canvas.

The following are links to the Snowflake documentation for the identity providers that Canvas supports:

- [Azure AD](https://docs.snowflake.com/en/user-guide/oauth-azure.html "https://docs.snowflake.com/en/user-guide/oauth-azure.html")
- [Okta](https://docs.snowflake.com/en/user-guide/oauth-okta.html "https://docs.snowflake.com/en/user-guide/oauth-okta.html")
- [Ping Federate](https://docs.snowflake.com/en/user-guide/oauth-pingfed.html "https://docs.snowflake.com/en/user-guide/oauth-pingfed.html")

The following process describes the general steps you must take. For more detailed instructions about performing these steps,
you can refer to the [Setting up Snowflake OAuth Access](data-wrangler-import.md#data-wrangler-snowflake-oauth-setup "data-wrangler-import.md#data-wrangler-snowflake-oauth-setup")
section in the Data Wrangler documentation for importing data from Snowflake.

To set up OAuth for Snowflake, do the following:

1. Register Canvas as an application with the identity provider. This requires specifying a redirect URL to Canvas, which should follow this format:
   `https://`<domain-id>`.studio.`<region>`.sagemaker.aws/canvas/default`
2. Within the identity provider, create a server or API that sends OAuth tokens to Canvas so that Canvas can access Snowflake.
   When setting up the server, use the authorization code and refresh token grant types, specify the access token lifetime, and
   set a refresh token policy. Additionally, within the External OAuth Security Integration for Snowflake, enable `external_oauth_any_role_mode`.
3. Get the following information from the identity provider: token URL, authorization URL,
   client ID, client secret. For Azure AD, also retrieve the OAuth scope credentials.
4. Store the information retrieved in the previous step in an AWS Secrets Manager secret.
   1. For Okta and Ping Federate, the secret should look like the following format:

   ```
   {"token_url":"https://identityprovider.com/oauth2/example-portion-of-URL-path/v2/token",
   "client_id":"example-client-id", "client_secret":"example-client-secret", "identity_provider":"OKTA"|"PING_FEDERATE",
   "authorization_url":"https://identityprovider.com/oauth2/example-portion-of-URL-path/v2/authorize"}
   ```

   2. For Azure AD, the secret should also include the OAuth scope credentials as the `datasource_oauth_scope` field.

After configuring the identity provider and the secret, you
must create an [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") secret to store the information and add it to your
Amazon SageMaker AI domain or user profile. Note that you can add a secret to both a domain and
user profile, but Canvas looks for secrets in the user profile first.

To add a secret to your domain or user profile, do the following:

1. Go to the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker").
2. Choose **domains** in the navigation pane.
3. From the list of **domains**, choose your domain.
   1. If adding your secret to your domain, do the following:
      1. Choose the domain.
      2. On the **domain settings** page, choose the **domain settings**
         tab.
      3. Choose **Edit**.

   2. If adding the secret to your user profile, do the
      following:
      1. Choose the user’s domain.
      2. On the **domain settings** page, choose the user
         profile.
      3. On the **User Details** page,
         choose **Edit**.

4. In the navigation pane, choose **Canvas settings**.
5. For **OAuth settings**, choose
   **Add OAuth configuration**.
6. For **Data source**, select **Snowflake**.
7. For **Secret Setup**, select
   **Create a new secret**.
   Alternatively, if you already created an AWS Secrets Manager secret
   with your credentials, enter the ARN for the secret. If creating a
   new secret, do the following:
   1. For **Identity Provider**, select
      **SNOWFLAKE**.
   2. For **Client ID**, **Client Secret**, **Authorization URL**, and **Token URL**, enter all of the information you
      gathered from the identity provider in the previous procedure.

8. Save your domain or user profile settings.

You should now be able to create a connection to your data in Snowflake from Canvas.
