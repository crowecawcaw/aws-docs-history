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
4. (Optional) In the **2FA - optional** field, provide a TOTP secret for applications that require two-factor authentication. You can either:

   - Enter the TOTP secret directly (for example, `JBSWY3DPEHPK3PXP`), or enter the full `otpauth://totp/` URI (for example, `otpauth://totp/Example:user@example.com?secret=JBSWY3DPEHPK3PXP&issuer=Example`).
   - Choose the upload icon to upload a QR code image from your authenticator app setup page. The QR code is scanned locally and the TOTP URI is extracted automatically.

   When a TOTP secret is provided, the agent automatically generates fresh one-time codes and enters them when a 2FA prompt is detected during login.

5. (Optional) Expand **Agent Space login prompt** to provide specific login instructions if your application has a complex authentication flow.

###### Important

Use test accounts with representative access rather than personal or administrative accounts.

## Use advanced setting

When you select an advanced credential strategy (Secrets Manager, Lambda, or IAM role), AWS Security Agent retrieves your credentials directly from the configured AWS resource using the service role. Use the **Agent Space login prompt** to provide the agent with instructions on how to apply those credentials to your application - for example, which login URL to navigate to and which form fields to fill in.

###### Note

Secrets Manager secrets and Lambda functions must be in the same AWS account as your AWS Security Agent setup. Cross-account credentials are not currently supported.

1. Select **Advanced setting**.
2. In the **User access strategy** dropdown, choose one of the following:

### Select available IAM role for agent to assume

Use this option for applications using AWS Cognito, API Gateway with IAM authentication, or other AWS-native authentication systems. The IAM role must have a trust relationship allowing AWS Security Agent to assume it and permissions to access your application’s authentication system.

### Select static credential from connected AWS Secrets Manager

Use this option to retrieve credentials securely from AWS Secrets Manager with encryption, rotation, and access auditing.

The IAM role must have `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret` permissions.

The agent retrieves the secret value directly from Secrets Manager. Use the **Agent Space login prompt** to tell the agent how to apply those credentials to your application’s login flow - for example, which URL to navigate to and which form fields to fill in. You may use any format to store your secret, as the agent will interpret the format using the instructions you provide in the login prompt.

For example, if the agent is to submit a username/password login form at https://example.com/login, you may format your secret as JSON with `username` and `password` fields. If the application requires TOTP-based 2FA, include a `totpSecret` field with either the TOTP secret directly or a full `otpauth://totp/` URI:

```
{
  "username": "test-user",
  "password": "secure-password-here",
  "totpSecret": "JBSWY3DPEHPK3PXP"
}
```

Then, configure the authentication instructions:
. Set **Access URL** to `https://example.com` (or any other URL selected from the list of target endpoints).
. Enter the following into **Agent Space login prompt**: "Navigate to https://example.com/login and enter the provided username and password into the form."

As another example, if you instead have an API key to be provided in an HTTP header, you may store it as plaintext:

```
"api-key-here"
```

Then, configure the authentication instructions:
. Enter the following into **Agent Space login prompt**: "Set the X-API-Key header to the provided API key for all requests."

###### Important

AWS Security Agent supports TOTP-based 2FA and email-based MFA. It does not support SMS, push notifications, hardware keys, or OAuth authentication. For applications that send a one-time code or verification link by email, see [Configure email MFA](#provide-testing-credentials-email-mfa "#provide-testing-credentials-email-mfa").

### Select available Lambda function to retrieve credentials dynamically

Use this option for complex authentication systems, dynamic credential generation, or integration with external identity providers.

The IAM role must have `lambda:InvokeFunction` permissions and the function must complete within 30 seconds.

When the penetration test runs, AWS Security Agent invokes your AWS Lambda function synchronously and passes an event that identifies the penetration test and the specific credential being resolved:

```
{
  "pentest_arn": "arn:aws:securityagent:us-west-2:111122223333:pentest/pt-abcd1234-5678-90ab-cdef-EXAMPLE11111",
  "actor_identifier": "Credential1"
}
```

- `pentest_arn` – The Amazon Resource Name (ARN) of the penetration test that the credential is being resolved for. Use it to scope, authorize, or audit the request within your function.
- `actor_identifier` – The **Credential name** you assigned to this credential in the console (for example, `Credential1`). Use it to return the correct credential when a single function serves multiple credentials.

The agent uses the function’s output directly as the credential. Use the **Agent Space login prompt** to tell the agent how to apply those credentials to your application, the same way you would with AWS Secrets Manager. Refer to [Select static credential from connected AWS Secrets Manager](#provide-testing-credentials-secrets-manager "#provide-testing-credentials-secrets-manager") for examples of how to format the output of your Lambda function and supported authentication types.

## Configure email MFA

Use email MFA when your application sends a one-time code or verification link by email as part of its authentication flow. If your application uses an authenticator app instead, provide a TOTP secret as described in [Input credentials directly](#provide-testing-credentials-input "#provide-testing-credentials-input").

When you enable email MFA, AWS Security Agent generates a unique forwarding address for each credential. You then create a rule in your email provider that forwards only your application’s MFA messages to that address. During login, AWS Security Agent reads the forwarded message and submits the code or link to complete authentication.

###### Note

Email MFA is available for both the input credentials and advanced setting credential methods, and in both the console and the AWS CLI or API.

### Enable email MFA in the console

1. In the credential section, select your credential input method and enter your credentials as described earlier in this topic.
2. Expand **2FA - optional**, then choose **Email MFA**.
3. Create the penetration test. AWS Security Agent then displays the **Email MFA forwarding address** for the credential. You cannot choose this address yourself.
4. Copy the forwarding address, then configure forwarding in your email provider. For more information, see [Set up email forwarding](#provide-testing-credentials-email-forwarding "#provide-testing-credentials-email-forwarding").

###### Note

If you dismiss this display before you copy the address, you can retrieve it later from the **Configurations** page of the penetration test, which shows the **Email MFA forwarding address** for each credential.

### Enable email MFA with the AWS CLI or API

Set `enableEmailMfa` to `true` for the actor in the `assets` parameter of your `create-pentest` or `update-pentest` request. For example:

```
aws securityagent create-pentest \
  --title "My penetration test" \
  --agent-space-id "your-agent-space-id" \
  --assets '{"actors": [{"identifier": "test-user", "enableEmailMfa": true}]}'
```

AWS Security Agent returns an `mfaForwardingAddress` for each actor in the `assets` field of the response.

### Set up email forwarding

Create a separate forwarding rule for each credential that uses email MFA. The general steps are the same for every provider:

1. Sign in to the email account that receives your application’s MFA messages.
2. Create a rule that matches only your application’s MFA messages. For example, match on the sender address or on a subject line that identifies the message.
3. Set the rule to forward matching messages to the MFA forwarding address that you copied.
4. Send a test MFA message from your application, then confirm that the rule forwards it.

###### Important

Your email provider must forward to an address without verifying it first. Some providers send a verification message to the destination address and require you to open a link in that message before forwarding begins. AWS Security Agent manages the MFA forwarding address, and you cannot read the messages sent to it, so you cannot complete verification.

The following providers support automatic forwarding to the MFA forwarding address:

- **Microsoft 365 and Outlook** - Create an inbox rule that forwards or redirects matching messages. For more information, see [Use rules to automatically forward messages](https://support.microsoft.com/en-us/office/use-rules-to-automatically-forward-messages-45aa9664-4911-4f96-9663-ece42816d746 "https://support.microsoft.com/en-us/office/use-rules-to-automatically-forward-messages-45aa9664-4911-4f96-9663-ece42816d746") in the Microsoft documentation.
- **iCloud Mail** - In Mail on iCloud.com, create a rule that forwards matching messages. Each rule forwards to one address. For more information, see [Automatically forward email in Mail on iCloud.com](https://support.apple.com/guide/icloud/automatically-forward-email-mm6b1a3960/icloud "https://support.apple.com/guide/icloud/automatically-forward-email-mm6b1a3960/icloud") in the iCloud User Guide.
- **Custom domains and self-hosted mail servers** - Add a server-side alias, sieve rule, or filter that forwards only the matching messages. For more information, consult your mail server’s documentation.

The following providers do not support automatic forwarding to the MFA forwarding address, because they verify the destination address before forwarding begins:

- **Gmail and Google Workspace** - Before a Gmail filter can forward to an address, you must add the address under **Settings > Forwarding and POP/IMAP**. Gmail sends a verification message to that address and requires you to open a link in it, which you cannot do. For more information, see [Automatically forward Gmail messages to another account](https://support.google.com/mail/answer/10957 "https://support.google.com/mail/answer/10957") in the Google documentation.
- **Yahoo Mail** - Forwarding requires a Yahoo Mail Plus subscription, and Yahoo verifies the destination address before forwarding begins. For more information, see [Enable automatic email forwarding in Yahoo Mail](https://help.yahoo.com/kb/SLN3525.html "https://help.yahoo.com/kb/SLN3525.html") in the Yahoo documentation.

Any other provider that forwards to an unverified external address also works. Consult your provider’s documentation for the equivalent steps.

###### Note

Even when your provider does not support automatic forwarding, you can forward MFA messages manually. You do not need to verify the destination address when you forward a single message. Because MFA codes expire quickly, forward each message to the MFA forwarding address as soon as it arrives during login.

###### Important

Forward only your application’s MFA messages. Do not forward your entire inbox. A narrow rule keeps unrelated email out of the penetration test and limits what your rule sends to AWS Security Agent.

### Data retention

AWS Security Agent stores the messages that it receives at the forwarding address only to complete the penetration test login. AWS Security Agent automatically deletes these messages 24 hours after receiving them.

## Configure multiple credentials

To test different user roles or authentication systems:

1. Choose **Add another credential**.
2. Configure the additional credential using either input method.
3. To remove a credential, choose **Remove** in the credential section.

## Login Optimization

Login Optimization allows AWS Security Agent to learn navigation patterns from previous penetration test runs and apply them to subsequent runs. These patterns include login flows and multi-step authentication workflows. This reduces the time the agent spends re-discovering how to authenticate, resulting in faster scans and more consistent testing coverage.

### How Login Optimization works

On the first penetration test run, the agent discovers how to navigate your application’s login flow using the credentials you provide. It records the successful navigation steps and generates a skill file that captures the learned login workflow.

On subsequent runs, the agent reads the saved skill file and applies the learned navigation pattern directly, skipping the discovery phase. This means:

- Faster time to authenticated testing — the agent applies proven navigation patterns immediately instead of exploring from scratch
- More consistent behavior — the agent follows the same proven path rather than exploring alternatives

###### Note

Login Optimization learns during the first login session within a run. Subsequent login sessions in the same run will benefit from what was learned in the first session. On future runs, all login sessions benefit from the saved skill.

### Enable or disable Login Optimization

Login Optimization is enabled by default. To disable or re-enable it:

1. In the penetration test configuration, navigate to the **Authentication credentials - optional** section.
2. Locate the **Login Optimization** toggle.
3. To enable Login Optimization, turn on the toggle. To disable, turn it off.

When disabled, the agent re-discovers the login flow from scratch on every run. Previously learned navigation skills are preserved and will be applied again if the feature is re-enabled.

###### Tip

If your application’s login flow changes significantly (for example a redesigned login page or a new authentication step), the agent automatically adapts by updating its learned skill on the next run. You do not need to manually reset the optimization.
