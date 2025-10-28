# Using the Amazon Cognito prefix domain for

managed login

The default experience for managed login is hosted on a domain that AWS owns. This
approach has a low barrier to entry—choose a prefix name and it's active—but
doesn't have the trust-inspiring features of a custom domain. There isn't a cost difference
between the Amazon Cognito domain option and the custom domain option. The only difference is the
domain in the web address that you direct your users to. For cases of third-party IdP
redirects and client-credentials flows, the hosted domain has little visible effect. A
custom domain is better for cases where your users sign in with managed login and would
interact with a authentication domain that doesn't match the application domain.

The hosted Amazon Cognito domain has a prefix of your choosing, but is hosted at the root domain
`amazoncognito.com`. The following is an example:

```
https://`cognitoexample`.auth.`ap-south-1`.amazoncognito.com
```

All prefix domains follow this format:
`prefix`.`auth`.`AWS Region
 code`.`amazoncognito`.`com`. [Custom domain](cognito-user-pools-add-custom-domain.md "cognito-user-pools-add-custom-domain.md") user pools can host
the managed login or hosted UI pages on any domain that you own.

###### Note

To augment the security of your Amazon Cognito applications, the parent domains of user pool
endpoints are registered in the [Public Suffix
List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). The PSL helps your users' web browsers establish a consistent
understanding of your user pool endpoints and the cookies they set.

User pool parent domains take the following formats.

```

auth.`Region`.amazoncognito.com
auth-fips.`Region`.amazoncognito.com

```

To add an app client and a user pool domain with the AWS Management Console, see [Creating an app
client](user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-console-create "user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-console-create").

###### Topics

- [Prerequisites](#cognito-user-pools-assign-domain-prefix-prereq "#cognito-user-pools-assign-domain-prefix-prereq")
- [Configure an Amazon Cognito
  domain prefix](#cognito-user-pools-assign-domain-prefix-step-1 "#cognito-user-pools-assign-domain-prefix-step-1")
- [Verify your sign-in
  page](#cognito-user-pools-assign-domain-prefix-verify "#cognito-user-pools-assign-domain-prefix-verify")

## Prerequisites

Before you begin, you need:

- A user pool with an app client. For more information, see [Getting started with user pools](getting-started-user-pools.md "getting-started-user-pools.md").

## Configure an Amazon Cognito

domain prefix

You can use either the AWS Management Console or the AWS CLI or API to configure a user pool
domain.

Amazon Cognito console

###### Configure a domain

1. Navigate to the **Domain** menu under
   **Branding**.
2. Next to **Domain**, choose
   **Actions** and select **Create Cognito
   domain**. If you have already configured a user pool
   prefix domain, choose **Delete Cognito domain**
   before creating your new custom domain.
3. Enter an available domain prefix to use with a **Amazon Cognito
   domain**. For information on setting up a
   **Custom domain**, see [Using your own domain for managed
   login](cognito-user-pools-add-custom-domain.md "cognito-user-pools-add-custom-domain.md").
4. Choose a **Branding version**. Your branding
   version applies to all user-interactive pages at that domain. Your
   user pool can host either managed login or hosted UI branding for
   all app clients.

###### Note

You can have a custom domain and a prefix domain, but Amazon Cognito
only serves the `/.well-known/openid-configuration`
endpoint for the _custom_
domain. 5. Choose **Create**.

CLI/API
Use the following commands to create a domain prefix and assign it to your
user pool.

###### To configure a user pool domain

- AWS CLI: `aws cognito-idp create-user-pool-domain`

**Example:**
`aws cognito-idp create-user-pool-domain --user-pool-id
 `<user_pool_id>`--domain
`<domain_name>`  --managed-login-version
 `2``

- User pools API operation: [CreateUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolDomain.md")

###### To get information about a domain

- AWS CLI: `aws cognito-idp
describe-user-pool-domain`

**Example:**
`aws cognito-idp describe-user-pool-domain --domain
 `<domain_name>``

- User pools API operation: [DescribeUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolDomain.md")

###### To delete a domain

- AWS CLI: `aws cognito-idp delete-user-pool-domain`

**Example:**
`aws cognito-idp delete-user-pool-domain --domain
 `<domain_name>``

- User pools API operation: [DeleteUserPoolDomain](../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.md "../../../cognito-user-identity-pools/latest/APIReference/API_DeleteUserPoolDomain.md")

## Verify your sign-in

page

- Verify that the sign-in page is available from your Amazon Cognito hosted
  domain.

```

`https://`<your_domain>`/login?response_type=code&client_id=`<your_app_client_id>`&redirect_uri=`<your_callback_url>``

```

Your domain is shown on the **Domain name** page of the Amazon Cognito
console. Your app client ID and callback URL are shown on the **App client
settings** page.
