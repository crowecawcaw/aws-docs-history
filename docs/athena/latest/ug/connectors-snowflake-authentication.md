# Authenticate with Snowflake

You can configure the Amazon Athena Snowflake connector to use either the key-pair
authentication or OAuth authentication method to connect to your Snowflake data warehouse.
Both methods provide secure access to Snowflake and eliminate the need to store passwords in
connection strings.

- **Key-pair authentication** – This method
  uses RSA public or private key pairs to authenticate with Snowflake. The private key
  digitally signs authentication requests while the corresponding public key is
  registered in Snowflake for verification. This method eliminates password
  storage.
- **OAuth authentication** – This method
  uses authorization token and refresh token to authenticate with Snowflake. It
  supports automatic token refresh, making it suitable for long-running
  applications.
  For more information, see the [Key-pair
  authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth "https://docs.snowflake.com/en/user-guide/key-pair-auth") and [OAuth authentication](https://docs.snowflake.com/en/user-guide/oauth-custom "https://docs.snowflake.com/en/user-guide/oauth-custom")
  in the Snowflake user guide.

## Prerequisites

Before you begin, complete the following prerequisites:

- Snowflake account access with administrative privileges.
- Snowflake user account dedicated for the Athena connector.
- OpenSSL or equivalent key generation tools for key-pair authentication.
- AWS Secrets Manager access to create and manage secrets.
- Web browser to complete the OAuth flow for the OAuth authentication.

## Configure key-pair authentication

This process involves generating an RSA key-pair, configuring your Snowflake account
with the public key, and securely storing the private key in AWS Secrets Manager. The following
steps will guide you through creating the cryptographic keys, setting up the necessary
Snowflake permissions, and configuring AWS credentials for seamless authentication.

1. **Generate RSA key-pair**

Generate a private and public key pair using OpenSSL.

    * To generate an unencrypted version, use the following command in your local command line
     application.



    ```
    openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
    ```
    * To generate an encrypted version, use the following command, which omits
     `-nocrypt`.



    ```
    openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8
    ```
    * To generate a public key from a private key.



    ```
    openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
    # Set appropriate permissions (Unix/Linux)
    chmod 600 rsa_key.p8
    chmod 644 rsa_key.pub
    ```

###### Note

Do not share your private key. The private key should only be accessible to the application that needs to authenticate with Snowflake. 2. **Extract public key content without delimiters for
Snowflake**

```
# Extract public key content (remove BEGIN/END lines and newlines)
cat rsa_key.pub | grep -v "BEGIN\|END" | tr -d '\n'
```

Save this output as you will need it later in the next step. 3. **Configure Snowflake user**

Follow these steps to configure a Snowflake user.

    1. Create a dedicated user for the Athena connector if it doesn't already
     exists.



    ```
    -- Create user for Athena connector
    CREATE USER `athena_connector_user`;

    -- Grant necessary privileges
    GRANT USAGE ON WAREHOUSE `your_warehouse` TO ROLE `athena_connector_role`;
    GRANT USAGE ON DATABASE `your_database` TO ROLE `athena_connector_role`;
    GRANT SELECT ON ALL TABLES IN DATABASE `your_database` TO ROLE `athena_connector_role`;
    ```
    2. Grant authentication privileges. To assign a public key to a user, you must have one of the
     following roles or privileges.




    	* The `MODIFY PROGRAMMATIC AUTHENTICATION METHODS` or `OWNERSHIP` privilege on the user.
    	* The `SECURITYADMIN` role or higher.
    Grant the necessary privileges to assign public keys with the
     following command.



    ```
    GRANT MODIFY PROGRAMMATIC AUTHENTICATION METHODS ON USER `athena_connector_user` TO ROLE `your_admin_role`;
    ```
    3. Assign the public key to the Snowflake user with the following
     command.



    ```
    ALTER USER `athena_connector_user` SET RSA_PUBLIC_KEY='`RSAkey`';
    ```

    Verify that the public key is successfully assigned to the user with
     the following command.



    ```
    DESC USER `athena_connector_user`;
    ```

4.  **Store private key in AWS Secrets Manager**
    1. Convert your private key to the format required by the connector.

    ```
    # Read private key content
    cat rsa_key.p8
    ```

    2. Create a secret in AWS Secrets Manager with the following structure.

    ```
    {
      "sfUser": "`your_snowflake_user`",
      "pem_private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----",
      "pem_private_key_passphrase": "`passphrase_in_case_of_encrypted_private_key(optional)`"
    }
    ```

    ###### Note

        * Header and footer are optional.
        * The private key must be separated by `\n`.

## Configure OAuth authentication

This authentication method enables secure, token-based access to Snowflake with
automatic credential refresh capabilities. The configuration process involves creating a
security integration in Snowflake, retrieving OAuth client credentials, completing the
authorization flow to obtain an access code, and storing the OAuth credentials in
AWS Secrets Manager for the connector to use.

1. **Create a security integration in Snowflake**

Execute the following SQL command in Snowflake to create a Snowflake OAuth
security integration.

```
CREATE SECURITY INTEGRATION `my_snowflake_oauth_integration_a`
  TYPE = OAUTH
  ENABLED = TRUE
  OAUTH_CLIENT = CUSTOM
  OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
  OAUTH_REDIRECT_URI = 'https://localhost:8080/oauth/callback'
  OAUTH_ISSUE_REFRESH_TOKENS = TRUE
  OAUTH_REFRESH_TOKEN_VALIDITY = 7776000;
```

**Configuration parameters**

    * `TYPE = OAUTH` – Specifies OAuth authentication
     type.
    * `ENABLED = TRUE` – Enables the security
     integration.
    * `OAUTH_CLIENT = CUSTOM` – Uses custom OAuth client
     configuration.
    * `OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'` – Sets client
     type for secure applications.
    * `OAUTH_REDIRECT_URI` – The callback URL for OAuth
     flow. It can be localhost for testing.
    * `OAUTH_ISSUE_REFRESH_TOKENS = TRUE` – Enables
     refresh token generation.
    * `OAUTH_REFRESH_TOKEN_VALIDITY = 7776000` – Sets
     refresh token validity (90 days in seconds).

2. **Retrieve OAuth client secrets**
   1. Run the following SQL command to get the client credentials.

   ```
   DESC SECURITY INTEGRATION '`MY_SNOWFLAKE_OAUTH_INTEGRATION_A`';
   ```

   2. Retrieve the OAuth client secrets.

   ```
   SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('`MY_SNOWFLAKE_OAUTH_INTEGRATION_A`');
   ```

   **Example response**

   ````
   {
     "OAUTH_CLIENT_SECRET_2": "`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`",
     "OAUTH_CLIENT_SECRET": "`je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY`,
     "OAUTH_CLIENT_ID": "`AIDACKCEVSQ6C2EXAMPLE`"
   }
   ```###### Note
   ````

Keep these credentials secure and do not share them. These will be used to configure the OAuth client. 3. **Authorize user and retrieve authorization code**

    1. Open the following URL in a browser.



    ```
    https://`<your_account>`.snowflakecomputing.com/oauth/authorize?client_id=`<OAUTH_CLIENT_ID>`&response_type=code&redirect_uri=https://localhost:8080/oauth/callback
    ```
    2. Complete the authorization flow.




    	1. Sign in using your Snowflake credentials.
    	2. Grant the requested permissions. You will be redirected to the callback URI
    	 with an authorization code.
    3. Extract the authorization code by copying the code parameter from the redirect URL.



    ```
    https://localhost:8080/oauth/callback?code=`<authorizationcode>`
    ```

    ###### Note

    The authorization code is valid for a limited time and can only be used once.

4. **Store OAuth credentials in AWS Secrets Manager**

Create a secret in AWS Secrets Manager with the following structure.

```
{
  "redirect_uri": "https://localhost:8080/oauth/callback",
  "client_secret": "`je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY`",
  "token_url": "https://<`your_account`>.snowflakecomputing.com/oauth/token-request",
  "client_id": "`AIDACKCEVSQ6C2EXAMPLE`,
  "username": "`your_snowflake_username`",
  "auth_code": "`authorizationcode`"
}
```

**Required fields**

    * `redirect_uri` – OAuth redirect URI that you
     obtained from Step 1.
    * `client_secret` – OAuth client secret that you
     obtained from Step 2.
    * `token_url` – Snowflake The OAuth token
     endpoint.
    * `client_id` – The OAuth client ID from Step
     2.
    * `username` – The Snowflake username for the
     connector.
    * `auth_code` – The authorization code that you
     obtained from Step 3.

After you create a secret, you get a secret ARN that you can use in your Glue connection
when you [create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md").
