# Provide authentication credentials for penetration testing

Provide credentials to enable AWS Security Agent to test authenticated areas of your web applications. Without credentials, the agent can only test publicly accessible pages and APIs.

## Configure authentication credentials

1. In the penetration test creation workflow, locate the **Authentication credentials - Optional** section.
2. In the **Credential #1** section, choose your credential input method:
   - **Input credentials** - Enter credentials directly. Best for development and testing environments.
   - **Advanced setting** - Use AWS-native credential management. Recommended for production environments and sensitive credentials.

### Advanced options

If you select **Advanced setting**, you can choose from three credential strategies:

- **IAM role assumption** - For applications using AWS Cognito or IAM authentication
- **AWS Secrets Manager** - For secure credential storage with encryption and rotation
- **Lambda function** - For dynamic credential generation or complex authentication flows

## Input credentials directly

1. Select **Input credentials**.
2. Enter the **User name** and **Password**.
3. In the **Access URL** dropdown, select the URL where these credentials will be used. This must be selected from the list of target endpoints.
4. (Optional) Expand **Agent Space login prompt** to provide specific login instructions if your application has a complex authentication flow.

###### Important

Use test accounts with representative access rather than personal or administrative accounts.

## Use advanced setting

1. Select **Advanced setting**.
2. In the **User access strategy** dropdown, choose one of the following:

### Select available IAM role for agent to assume

Use this option for applications using AWS Cognito, API Gateway with IAM authentication, or other AWS-native authentication systems. The IAM role must have a trust relationship allowing AWS Security Agent to assume it and permissions to access your application’s authentication system.

### Select static credential from connected AWS Secrets Manager

Use this option to retrieve credentials securely from AWS Secrets Manager with encryption, rotation, and access auditing.

The IAM role must have `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` permissions.

Use the **Agent Space login prompt** to provide detailed instructions on how to interpret and use the credentials stored in the secret. You may use any format to store your secret, as the agent will dynamically interpret the format using these instructions.

For example, if the agent is to submit a username/password login form at https://example.com/login, you may format your secret as JSON with `username` and `password` fields:

```
{
  "username": "test-user",
  "password": "secure-password-here"
}
```

Then, configure the authentication instructions:
. Enable **Allow agent to perform browser login using this credential**.
. Set **Access URL** to `https://example.com` (or any other URL selected from the list of target endpoints).
. Enter the following into **Agent Space login prompt**: "Navigate to https://example.com/login and enter the provided username and password into the form."

As another example, if you instead have an API key to be provided in an HTTP header, you may store it as plaintext:

```
"api-key-here"
```

Then, configure the authentication instructions:
. Disable **Allow agent to perform browser login using this credential**.
. Enter the following into **Agent Space login prompt**: "Set the X-API-Key header to the provided API key for all requests."

###### Important

We currently do not support 2FA or OAuth-based authentication.

### Select available Lambda function to retrieve credentials dynamically

Use this option for complex authentication systems, dynamic credential generation, or integration with external identity providers.

The IAM role must have `lambda:InvokeFunction` permissions and the function must complete within 30 seconds.

Like with Secrets Manager, the agent will dynamically interpret your Lambda function’s output using any login instructions provided in the **Agent Space login prompt**. Refer to [Select static credential from connected AWS Secrets Manager](#provide-testing-credentials-secrets-manager "#provide-testing-credentials-secrets-manager") for examples of how to format the output of your Lambda function and supported authentication types.

## Configure multiple credentials

To test different user roles or authentication systems:

1. Click **Add another credential**.
2. Configure the additional credential using either input method.
3. To remove a credential, click **Remove** in the credential section.
