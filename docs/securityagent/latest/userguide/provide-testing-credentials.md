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
3. In the **Access domain** dropdown, select the domain where these credentials will be used.
4. (Optional) Expand **Agent login prompt** to provide specific login instructions if your application has a complex authentication flow.

###### Important

Use test accounts with representative access rather than personal or administrative accounts.

## Use advanced setting

1. Select **Advanced setting**.
2. In the **User access strategy** dropdown, choose one of the following:

### Select available IAM role for agent to assume

Use this option for applications using AWS Cognito, API Gateway with IAM authentication, or other AWS-native authentication systems. The IAM role must have a trust relationship allowing AWS Security Agent to assume it and permissions to access your application’s authentication system.

### Select static credential from connected AWS Secrets Manager

Use this option to retrieve credentials securely from AWS Secrets Manager with encryption, rotation, and access auditing.

Format your secret with `username` and `password` fields:

```
{
  "username": "test-user@example.com",
  "password": "secure-password-here"
}
```

The IAM role must have `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` permissions.

### Select available Lambda function to retrieve credentials dynamically

Use this option for complex authentication systems, dynamic credential generation, or integration with external identity providers.

Your Lambda function must return credentials in this format:

```
{
  "username": "generated-user@example.com",
  "password": "dynamic-password"
}
```

The IAM role must have `lambda:InvokeFunction` permissions and the function must complete within 30 seconds.

## Configure multiple credentials

To test different user roles or authentication systems:

1. Click **Add another credential**.
2. Configure the additional credential using either input method.
3. To remove a credential, click **Remove** in the credential section.
