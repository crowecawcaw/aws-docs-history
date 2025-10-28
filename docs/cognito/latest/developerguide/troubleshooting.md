# Troubleshoot Amazon Cognito

This chapter provides solutions to common problems you might encounter while working with Amazon Cognito. Amazon Cognito implementations can face various challenges across authentication flows, user pool configurations, and identity federation setups. Whether you're developing a new application or maintaining an existing one, this troubleshooting guide helps you identify and resolve common issues quickly.

## Custom domain configuration errors

When configuring custom domain names in Amazon Cognito, you might receive error messages. Common
errors include validation issues, certificate problems, or domain conflicts.

### `Custom domain is not a valid

subdomain`

This error indicates an issue with DNS resolution for the parent domain. Amazon Cognito does not
support top-level domains and requires the parent domain to have a DNS A record for
validation.

**Problem**

This error indicates an issue with DNS resolution for the parent domain. Amazon Cognito
does not support top-level domains and requires the parent domain to have a DNS A
record for validation.

**Solution**

- **Create an A Record for the Parent Domain:** You
  must create an A record in your DNS configuration for the parent domain of your
  custom domain.
  - **Example:** If your custom domain is
    `auth.xyz.yourdomain.com`, the parent domain is
    `xyz.yourdomain.com`. If you want to configure
    `xyz.yourdomain.com` as a custom domain, the parent is
    `yourdomain.com`.
  - The parent domain must resolve to a valid IP address. If it doesn't point
    to a real IP address, you can use a dummy IP address, such as
    `8.8.8.8`.

- **Verify DNS Propagation (Optional but
  Recommended):** To ensure your DNS provider has propagated the change,
  you can run a `dig` command.
  - If using `auth.xyz.yourdomain.com` as the custom domain:
    `dig A xyz.yourdomain.com +short`
  - If using `xyz.yourdomain.com` as the custom domain: `dig A
yourdomain.com +short`
  - The command should return the IP address you configured. If it doesn't,
    wait until the change has fully propagated.

- **Remove the parent domain A Record:** After
  successfully creating the custom domain in Amazon Cognito, you can remove the A record you
  created for the parent domain if it was a dummy one.

For more information, see [Using
your own domain for the hosted UI](cognito-user-pools-add-custom-domain.md "cognito-user-pools-add-custom-domain.md").

### `Domain already associated

with another user pool`

Custom domain names must be unique across all AWS accounts and Regions.

**Problem**

Custom domain names must be unique across all AWS accounts and Regions.

**Solution**

- To use the domain name for a new user pool, you must delete the custom domain
  from the user pool it's currently associated with.
- **Wait after deletion:** It takes time for the
  custom domain to fully delete from the first user pool. Creating a new custom
  domain with the same name immediately after deletion might still result in this
  error. Wait a few minutes before trying again.

### `One or more of the CNAMEs that

you provided are already associated with a different resource`

When you create a custom domain, Amazon Cognito creates an AWS-managed Amazon CloudFront distribution. A
domain name can only be used with one Amazon CloudFront distribution. This error occurs if the domain
name is already in use as an alternate domain for another Amazon CloudFront distribution.

**Problem**

When you create a custom domain, Amazon Cognito creates an AWS-managed Amazon CloudFront
distribution. A domain name can only be used with one Amazon CloudFront distribution. This
error occurs if the domain name is already in use as an alternate domain for another
Amazon CloudFront distribution.

**Solution**

- **Option 1:** Use a different domain name for
  your Amazon Cognito custom domain.
- **Option 2:** If you use the domain name for
  Amazon Cognito, do not use it with another Amazon CloudFront distribution.

### `The specified SSL certificate

doesn't exist`

Amazon Cognito uses Amazon CloudFront, which requires the AWS Certificate Manager (ACM) certificate to be in the
`us-east-1` (N. Virginia) AWS Region, regardless of the user pool's
Region.

**Problem**

Amazon Cognito uses Amazon CloudFront, which requires the AWS Certificate Manager (ACM) certificate to be in the
`us-east-1` (N. Virginia) AWS Region, regardless of the user pool's
Region.

**Solution**

- **Ensure Certificate Region:** Confirm the ACM
  certificate is in the `us-east-1` Region.
- **Check Certificate Validity:** Make sure the
  selected certificate is not expired.
- **Imported Certificates:** If you imported the
  certificate into ACM, ensure:
  - It was issued by a public certificate authority.
  - It includes the correct certificate chain.

- **AWS KMS Policy Check:** An explicit
  `deny` statement in an AWS Key Management Service (AWS KMS) policy for the IAM user or
  role creating the domain can cause this error. Specifically, check for explicit
  denials on `kms:DescribeKey`, `kms:CreateGrant`, or
  `kms:*` actions.

## `Invalid refresh token`

error

**Problem**

You receive an `Invalid refresh token` error when trying to use a refresh
token to get new access and ID tokens from your Amazon Cognito user pool using the
`AdminInitiateAuth` or `InitiateAuth` API operation.

**Solution**

Implement the following troubleshooting steps based on your user pool configuration
and API usage:

- **Ensure consistent app client ID:** When calling
  the `AdminInitiateAuth` or `InitiateAuth` API for token
  refresh, you must use the exact same app client ID that was used during the initial
  authentication that generated the refresh token.
- **Confirm the device:** If you have [device tracking](amazon-cognito-user-pools-device-tracking.md "amazon-cognito-user-pools-device-tracking.md") enabled
  on your user pool, but the user's device hasn't been confirmed, you must call the
  [ConfirmDevice](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.md") API first. After the user confirms their device, you can
  exchange the refresh token.
- **Include device key in refresh request:** If
  device tracking is enabled, include the unique device key as an
  `AuthParameter` when using the `REFRESH_TOKEN_AUTH`
  flow:

```
{
  "AuthFlow": "REFRESH_TOKEN_AUTH",
  "AuthParameters": {
    "REFRESH_TOKEN": "example_refresh_token",
    "SECRET_HASH": "example_secret_hash", // Required if your app client uses a client secret
    "DEVICE_KEY": "example_device_key"
  }
}
```

- **Use `USER_SRP_AUTH` for device
  tracking:** If you are using device tracking, the initial authentication
  flow must be `USER_SRP_AUTH`.

For more information, see [Working with user devices in your
user pool](amazon-cognito-user-pools-device-tracking.md "amazon-cognito-user-pools-device-tracking.md").

## Invalid SAML response errors in

federation

Users receive various `Invalid SAML response` and similar errors when
attempting to federate into Amazon Cognito using SAML 2.0. These errors can occur due to attribute
mapping issues, certificate problems, or configuration mismatches.

### `Invalid user attributes:

Required attribute`

**Problem**

A user is missing a value for an attribute that is required in your user pool, or
the IdP is attempting to remove or update an immutable attribute.

**Solution**

- Check the [required
  attributes](user-pool-settings-attributes.md#how-to-edit-standard-attributes "user-pool-settings-attributes.md#how-to-edit-standard-attributes") defined in your user pool configuration.
- Using network capture tools in your browser, retrieve the SAML response. You
  might need to perform URL and base64 decoding. Verify the attribute is present in
  the SAML assertion.
- Sign in to your identity provider and review the attributes that it is sending
  to Amazon Cognito. Verify that the IdP is configured to send the required attribute using
  the correct name.
- For immutable attributes, run the following AWS CLI command to identify them:
  `aws cognito-idp describe-user-pool --user-pool-id USER-POOL-ID --query
'UserPool.SchemaAttributes[?Mutable==`false`].Name'`.
- In the SAML attribute mappings of your IdP, delete any mapping that targets an
  immutable Amazon Cognito attribute. Alternately, update the destination attribute to a
  different, mutable attribute.

### `Invalid SAML response received:

SAML Response signature is invalid`

**Problem**

Your IdP has updated its SAML signing certificate, causing a mismatch between the
certificate in the SAML response and the metadata file stored in Amazon Cognito.

**Solution**

1. Download the latest metadata file from your IdP.
2. In the Amazon Cognito console, navigate to the **Social and external
   providers** for your user pool, edit your SAML provider, and replace
   the existing metadata file with the newly downloaded file.

### `Audience restriction`

or `Application with identifier not found`

**Problem**

An incorrect Entity ID is configured in your IdP, or the assertion uses another
user pool's Uniform Resource Name (URN).

**Solution**

1. Get your Amazon Cognito user pool ID from the **Overview** section in
   the console.
2. In the management console for your IdP, update the entity ID in the SAML
   application for your user pool. Configure the entity ID to match the format
   `urn:amazon:cognito:sp:`USER_POOL_ID``.
Replace `USER_POOL_ID` with the user pool ID from the previous
   step.

### `An error was encountered with the

requested page`

**Problem**

The Assertion Consumer Service (ACS) URL registered with your IdP is incorrectly
configured, or the IdP is not sending the SAML response using the required POST
binding.

**Solution**

- In the management console for your IdP, update the application with the
  correct ACS URL format, ensuring it uses the `HTTP POST`
  binding.
- **Default domain format:**
  `https://cognito-idp.`Region`.amazonaws.com/`your
  user pool ID`/saml2/idpresponse`
- **Custom domain format:**
  `https://`auth.example.com`/saml2/idpresponse`

### `Invalid relayState from identity

provider`

**Problem**

The `RelayState` parameter is missing or invalid, or the URL is
mismatched between the IdP and Amazon Cognito.

**Solution**

- **For [service provider
  initiated (SP-initiated)](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-saml-idp-authentication "cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-saml-idp-authentication") flows:** Always start the
  authentication at your user pool `/oauth2/authorize` endpoint. SAML
  assertion that don't return `RelayState` parameters from the user's
  initial visit to Amazon Cognito are not valid SP-initiated requests.
- **For [identity
  provider initiated (IdP-initiated)](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation "cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-SAML-session-initiation-idp-initiation") flows:** The IdP must
  include the `RelayState` parameter with the SAML assertion to the
  `/saml2/idpresponse` endpoint, using the required format:
  `redirect_uri=REDIRECT_URI&state=STATE`.

For more information, see [Using SAML identity providers with a user
pool](cognito-user-pools-saml-idp.md "cognito-user-pools-saml-idp.md").

## Managed login users can't select an MFA

factor

**Problem**

Users can't choose their preferred MFA method when signing in through managed login,
or they aren't being prompted for the MFA method you expect.

**Solution**

Amazon Cognito follows specific logic to determine which MFA factors are available to users
based on user pool settings, user attributes, and account recovery configuration. For
example, users can't use email MFA if email is configured as their primary account
recovery method.

To override the default MFA factor selection, you can implement either of these
approaches:

- For public applications: Use [SetUserMFAPreference](../../../cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetUserMFAPreference.md") with a valid access token to let users set their own
  MFA preferences
- For administrator-managed applications: Use [AdminSetUserMFAPreference](../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserMFAPreference.md") with AWS credentials to configure user MFA
  preferences

Both operations allow you to enable or disable SMS, email, and TOTP MFA methods for
individual users, and set one method as preferred.

For more information, see [Adding MFA to a user pool](user-pool-settings-mfa.md "user-pool-settings-mfa.md").

### Passwordless and passkey users can't use

MFA

**Problem**

Users who sign in with passwordless authentication methods or passkeys cannot add
or use multi-factor authentication.

**Solution**

This is an intended limitation. You can configure your user pool so that users
have MFA or sign in with passwordless factors, but not both. MFA is only available for
password-based authentication flows.

For more information, see [Authentication with
user pools](getting-started-identity-pools-application.md#user-pool-authentication "getting-started-identity-pools-application.md#user-pool-authentication").

## Not able to receive password reset code

through email/SMS

**Problem**

Users cannot receive verification codes during the forgot password workflow through
their email or SMS.

**Solution**

There are various reasons why verification codes may not be received. Follow this
checklist to troubleshoot the issue:

- Check the user's email spam and junk folders.
- Confirm that the user exists in the user pool.
- Verify that the user's status isn't `FORCE_CHANGE_PASSWORD`. If this
  is the case, the user was created by an administrator and Amazon Cognito will prompt them to
  set a password when they sign in with their temporary password.
- Check that the user has a verified email or phone number attribute.
- Check your account spend limit for SMS messaging
- Check your Amazon Simple Email Service (Amazon SES) message-sending quota.
- Check if both SMS and Amazon SES (if your user pool is configured to **Send
  email with Amazon SES**) have been moved out of sandbox. If they were not
  moved out from sandbox, email addresses or phone numbers which have not been
  verified by Amazon SES or AWS End User Messaging SMS will not be able to receive password reset
  codes.
- If the user has an active MFA factor, check that they aren't trying to generate
  a message to the same factor. For example, users with email MFA active can't sent
  password reset codes by email.

For more information, see [Email settings for Amazon Cognito user pools](user-pool-email.md "user-pool-email.md") and [SMS message settings for Amazon Cognito user pools](user-pool-sms-settings.md "user-pool-sms-settings.md").

## `SECRET_HASH` errors

**Problem**

Authentication API requests to app clients with client secrets return errors like
`An error occurred (NotAuthorizedException) when calling the ForgotPassword
 operation: Client 1example23456789 is configured with secret but SECRET_HASH was not
 received.`

**Solution**

Your application must calculate the `SECRET_HASH` for the current user,
app client, and client secret. The calculation method is:

```
Base64 ( HMAC_SHA256 ( "client secret", "Username" + "Client Id" ) )
```

To get the client secret, you can:

1. Open the Amazon Cognito console and navigate to your app client from the **App
   clients** menu. In the **App client information**
   section, locate **Client secret**. Select **Show client
   secret** and your app client secret appears.
2. Generate a [DescribeUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md") request. The client secret is
   included in the response.

For more information, see [Computing secret hash
values](signing-up-users-in-your-app.md#cognito-user-pools-computing-secret-hash "signing-up-users-in-your-app.md#cognito-user-pools-computing-secret-hash").

## The Amazon Cognito console chooses a default

configuration for a new user pool

**Problem**

When you set up a new user pool in the console, Amazon Cognito chooses several default
settings for you. Some settings can't be changed after the user pool is created. How can
you make informed choices and understand what Amazon Cognito selected automatically?

**Solution**

The new user pool setup in the Amazon Cognito console is designed for rapid testing and
prototyping. The console presents you with only the most critical configuration choices

- those that cannot be changed after user pool creation. All other settings that Amazon Cognito
  configures automatically can be modified later.

We recommend the following approach:

1. Use the console to create test user pools while you refine your
   implementation.
2. After you've determined your production configuration, apply those settings to
   your test user pools.
3. Use [DescribeUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.md") and [DescribeUserPoolClient](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.md") API operations to generate JSON templates of your
   tested configuration.
4. Use these templates with deployment tools like the AWS SDKs, CDK, REST API, or
   AWS CloudFormation to create your production resources.

For more information, see [Getting started with user pools](getting-started-user-pools.md "getting-started-user-pools.md").

## Additional troubleshooting resources

For additional troubleshooting guidance and community-contributed solutions, you can also explore the following external resources:

- [AWS re:Post Amazon Cognito community](https://repost.aws/tags/TA4IvCeRIxS_-n3_9K6hBrfw/amazon-cognito "https://repost.aws/tags/TA4IvCeRIxS_-n3_9K6hBrfw/amazon-cognito") - Browse community questions and solutions
- [AWS Knowledge Center Amazon Cognito articles](https://aws.amazon.com/premiumsupport/knowledge-center/cognito/ "https://aws.amazon.com/premiumsupport/knowledge-center/cognito/") - Curated troubleshooting articles
