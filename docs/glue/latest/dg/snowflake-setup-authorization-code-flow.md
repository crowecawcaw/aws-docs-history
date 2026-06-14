# Set up the Authorization Code flow for Snowflake

To use OAuth authentication method, ensure the following setup is complete:

- **Configure Snowflake OAuth for a custom client** by following the official Snowflake documentation:
  [Configure Snowflake OAuth for custom clients.](https://docs.snowflake.com/en/user-guide/oauth-custom "https://docs.snowflake.com/en/user-guide/oauth-custom")
- **Set the correct redirect URI** when creating the Snowflake security integration. For example:
  If you are creating the connection in the DUB (eu-west-1) region, your redirect URI should be: `https://eu-west-1.console.aws.amazon.com/gluestudio/oauth`
- After creating the security integration, retain the following information for use when creating the Glue connection:

  - OAUTH_CLIENT_ID: This value should be provided as User Managed Client Application Client ID on the Glue connection creation page.
  - OAUTH_CLIENT_SECRET: This value should be stored in the AWS Secret used for the connection, under the key USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET.
