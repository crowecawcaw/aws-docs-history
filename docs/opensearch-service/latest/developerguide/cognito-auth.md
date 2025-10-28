# Configuring Amazon Cognito authentication for OpenSearch

Dashboards

You can authenticate and protect your Amazon OpenSearch Service default installation of OpenSearch
Dashboards using [Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md"). Amazon Cognito
authentication is optional and available only for domains using OpenSearch or Elasticsearch
5.1 or later. If you don't configure Amazon Cognito authentication, you can still protect Dashboards
using an [IP-based access policy](ac.md#ac-types-ip "ac.md#ac-types-ip") and a [proxy server](dashboards.md#dashboards-proxy "dashboards.md#dashboards-proxy"), HTTP basic authentication, or [SAML](saml.md "saml.md").

Much of the authentication process occurs in Amazon Cognito, but this section offers guidelines and
requirements for configuring Amazon Cognito resources to work with OpenSearch Service domains. [Standard pricing](https://aws.amazon.com/cognito/pricing/ "https://aws.amazon.com/cognito/pricing/") applies to all Amazon Cognito
resources.

###### Tip

The first time you configure a domain to use Amazon Cognito authentication for
OpenSearch Dashboards, we recommend using the console. Amazon Cognito resources are extremely
customizable, and the console can help you identify and understand the features that
matter to you.

###### Topics

- [Prerequisites](#cognito-auth-prereq "#cognito-auth-prereq")
- [Configuring a domain to use Amazon Cognito
  authentication](#cognito-auth-config "#cognito-auth-config")
- [Allowing the authenticated role](#cognito-auth-config-ac "#cognito-auth-config-ac")
- [Configuring identity providers](#cognito-auth-identity-providers "#cognito-auth-identity-providers")
- [(Optional) Configuring granular access](#cognito-auth-granular "#cognito-auth-granular")
- [(Optional) Customizing the sign-in page](#cognito-auth-customize "#cognito-auth-customize")
- [(Optional) Configuring advanced security](#cognito-auth-advanced "#cognito-auth-advanced")
- [Testing](#cognito-auth-testing "#cognito-auth-testing")
- [Quotas](#cognito-auth-limits "#cognito-auth-limits")
- [Common configuration issues](#cognito-auth-troubleshooting "#cognito-auth-troubleshooting")
- [Disabling Amazon Cognito authentication for
  OpenSearch Dashboards](#cognito-auth-disable "#cognito-auth-disable")
- [Deleting domains that use Amazon Cognito authentication for
  OpenSearch Dashboards](#cognito-auth-delete "#cognito-auth-delete")

## Prerequisites

Before you can configure Amazon Cognito authentication for OpenSearch Dashboards, you must fulfill
several prerequisites. The OpenSearch Service console helps streamline the creation of these
resources, but understanding the purpose of each resource helps with configuration and
troubleshooting. Amazon Cognito authentication for Dashboards requires the following
resources:

- Amazon Cognito [user
  pool](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md")
- Amazon Cognito [identity
  pool](../../../cognito/latest/developerguide/identity-pools.md "../../../cognito/latest/developerguide/identity-pools.md")
- IAM role that has the `AmazonOpenSearchServiceCognitoAccess`
  policy attached (`CognitoAccessForAmazonOpenSearch`)

###### Note

The user pool and identity pool must be in the same AWS Region. You can use the
same user pool, identity pool, and IAM role to add Amazon Cognito authentication for
Dashboards to multiple OpenSearch Service domains. To learn more, see [Quotas](#cognito-auth-limits "#cognito-auth-limits").

### About the user pool

User pools have two main features: create and manage a directory of users, and let
users sign up and log in. For instructions to create a user pool, see [Getting
started with user pools](../../../cognito/latest/developerguide/getting-started-user-pools.md "../../../cognito/latest/developerguide/getting-started-user-pools.md") in the
_Amazon Cognito Developer Guide_.

When you create a user pool to use with OpenSearch Service, consider the following:

- Your Amazon Cognito user pool must have a [domain name](../../../cognito/latest/developerguide/cognito-user-pools-domain.md "../../../cognito/latest/developerguide/cognito-user-pools-domain.md"). OpenSearch Service uses this domain name to redirect users to a
  login page for accessing Dashboards. Other than a domain name, the user pool
  doesn't require any non-default configuration.
- You must specify the pool's required [standard attributes](../../../cognito/latest/developerguide/user-pool-settings-attributes.md#cognito-user-pools-standard-attributes "../../../cognito/latest/developerguide/user-pool-settings-attributes.md#cognito-user-pools-standard-attributes")—attributes like name, birth date,
  email address, and phone number. You can't change these attributes after you
  create the user pool, so choose the ones that matter to you at this
  time.
- While creating your user pool, choose whether users can create their own
  accounts, the minimum password strength for accounts, and whether to enable
  multi-factor authentication. If you plan to use an [external identity provider](../../../cognito/latest/developerguide/cognito-user-pools-identity-federation.md "../../../cognito/latest/developerguide/cognito-user-pools-identity-federation.md"), these settings are inconsequential.
  Technically, you can enable the user pool as an identity provider _and_ enable an external identity provider, but
  most people prefer one or the other.

User pool IDs take the form of
``region`_`ID``.
If you plan to use the AWS CLI or an AWS SDK to configure OpenSearch Service, make note of the
ID.

### About the identity pool

Identity pools let you assign temporary, limited-privilege roles to users after
they log in. For instructions about creating an identity pool, see [Identity pools console overview](../../../cognito/latest/developerguide/identity-pools.md "../../../cognito/latest/developerguide/identity-pools.md") in the
_Amazon Cognito Developer Guide_. When you create an identity pool to use
with OpenSearch Service, consider the following:

- If you use the Amazon Cognito console, you must select the **Enable access
  to unauthenticated identities** check box to create the
  identity pool. After you create the identity pool and configure the OpenSearch Service
  domain, Amazon Cognito disables this setting.
- You don't need to add [external identity providers](../../../cognito/latest/developerguide/external-identity-providers.md "../../../cognito/latest/developerguide/external-identity-providers.md") to the identity pool. When you
  configure OpenSearch Service to use Amazon Cognito authentication, it configures the identity pool
  to use the user pool that you just created.
- After you create the identity pool, you must choose unauthenticated and
  authenticated IAM roles. These roles specify the access policies that
  users have before and after they log in. If you use the Amazon Cognito console, it
  can create these roles for you. After you create the authenticated role,
  make note of the ARN, which takes the form of
  `arn:aws:iam::`123456789012`:role/Cognito_`identitypoolname`Auth_Role`.

Identity pool IDs take the form of
``region`:`ID`-`ID`-`ID`-`ID`-`ID``.
If you plan to use the AWS CLI or an AWS SDK to configure OpenSearch Service, make note of the
ID.

### About the CognitoAccessForAmazonOpenSearch

role

OpenSearch Service needs permissions to configure the Amazon Cognito user and identity pools and use them
for authentication. You can use `AmazonOpenSearchServiceCognitoAccess`,
which is an AWS managed policy, for this purpose.
`AmazonESCognitoAccess` is a legacy policy that was replaced by
`AmazonOpenSearchServiceCognitoAccess` when the service was renamed
to Amazon OpenSearch Service. Both policies provide the minimum Amazon Cognito permissions necessary to enable
Amazon Cognito authentication. For policy details, see [AmazonOpenSearchServiceCognitoAccess](../../../aws-managed-policy/latest/reference/AmazonOpenSearchServiceCognitoAccess.md "../../../aws-managed-policy/latest/reference/AmazonOpenSearchServiceCognitoAccess.md") in the _AWS Managed
Policy Reference Guide_.

If you use the console to create or configure your OpenSearch Service domain, it creates an
IAM role for you and attaches the
`AmazonOpenSearchServiceCognitoAccess` policy (or the
`AmazonESCognitoAccess` policy if it's an Elasticsearch domain) to
the role. The default name for this role is
`CognitoAccessForAmazonOpenSearch`.

The role permissions policies `AmazonOpenSearchServiceCognitoAccess`
and `AmazonESCognitoAccess` both allow OpenSearch Service to complete the following
actions on all identity and user pools:

- Action: `cognito-idp:DescribeUserPool`
- Action: `cognito-idp:CreateUserPoolClient`
- Action: `cognito-idp:DeleteUserPoolClient`
- Action: `cognito-idp:UpdateUserPoolClient`
- Action: `cognito-idp:DescribeUserPoolClient`
- Action: `cognito-idp:AdminInitiateAuth`
- Action: `cognito-idp:AdminUserGlobalSignOut`
- Action:
  `cognito-idp:ListUserPoolClients`
- Action: `cognito-identity:DescribeIdentityPool`
- Action: `cognito-identity:SetIdentityPoolRoles`
- Action: `cognito-identity:GetIdentityPoolRoles`

If you use the AWS CLI or one of the AWS SDKs, you must create your own role,
attach the policy, and specify the ARN for this role when you configure your OpenSearch Service
domain. The role must have the following trust relationship:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "opensearchservice.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For instructions, see [Create a role to
delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") and [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

## Configuring a domain to use Amazon Cognito

authentication

After you complete the prerequisites, you can configure an OpenSearch Service domain to use Amazon Cognito
for Dashboards.

###### Note

Amazon Cognito is not available in all AWS Regions. For a list of supported Regions;, see
[Service
endpoints](../../../general/latest/gr/cognito_identity.md#cognito_identity_region "../../../general/latest/gr/cognito_identity.md#cognito_identity_region") for Amazon Cognito. You don't need to use the same Region for Amazon Cognito
that you use for OpenSearch Service.

### Configuring Amazon Cognito authentication

(console)

Because it creates the `CognitoAccessForAmazonOpenSearch` role
for you, the console offers the simplest configuration experience. In addition to
the standard OpenSearch Service permissions, you need the following set of permissions to use the
console to create a domain that uses Amazon Cognito authentication for
OpenSearch Dashboards.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "cognito-identity:ListIdentityPools",
 "cognito-idp:ListUserPools",
 "iam:CreateRole",
 "iam:AttachRolePolicy"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/service-role/`CognitoAccessForAmazonOpenSearch`"
 }
 ]
}`

```

For instructions to add permissions to an identity (user, user group, or role),
see [Adding IAM identity permissions (console)](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

If `CognitoAccessForAmazonOpenSearch` already exists, you need fewer
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "cognito-identity:ListIdentityPools",
 "cognito-idp:ListUserPools"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/service-role/`CognitoAccessForAmazonOpenSearch`"
 }
 ]
}`

```

###### To configure Amazon Cognito authentication for Dashboards (console)

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home/](https://console.aws.amazon.com/aos/home/ "https://console.aws.amazon.com/aos/home/").
2. Under **Domains**, select the domain you want to
   configure.
3. Choose **Actions**, **Edit security
   configuration**.
4. Select **Enable Amazon Cognito authentication**.
5. For **Region**, select the AWS Region that contains
   your Amazon Cognito user pool and identity pool.
6. For **Cognito user pool**, select a user pool or create
   one. For more information, see [About the user pool](#cognito-auth-prereq-up "#cognito-auth-prereq-up").
7. For **Cognito identity pool**, select an identity pool or
   create one. For more information, see [About the identity pool](#cognito-auth-prereq-ip "#cognito-auth-prereq-ip").

###### Note

The **Create user pool** and **Create
identity pool** links direct you to the Amazon Cognito console and
require you to create these resources manually. The process is not
automatic. For more information, see [Prerequisites](#cognito-auth-prereq "#cognito-auth-prereq"). 8. For **IAM role name**, use the default value of
`CognitoAccessForAmazonOpenSearch` (recommended) or enter a
new name. For more information, see [About the CognitoAccessForAmazonOpenSearch
role](#cognito-auth-role "#cognito-auth-role"). 9. Choose **Save changes**.

After your domain finishes processing, see [Allowing the authenticated role](#cognito-auth-config-ac "#cognito-auth-config-ac") and [Configuring identity providers](#cognito-auth-identity-providers "#cognito-auth-identity-providers") for additional
configuration steps.

### Configuring Amazon Cognito authentication

(AWS CLI)

Use the `--cognito-options` parameter to configure your OpenSearch Service domain.
The following syntax is used by both the `create-domain` and
`update-domain-config` commands:

```
--cognito-options Enabled=true,UserPoolId="`user-pool-id`",IdentityPoolId="`identity-pool-id`",RoleArn="`arn:aws:iam::123456789012:role/CognitoAccessForAmazonOpenSearch`"
```

**Example**

The following example creates a domain in the `us-east-1`
Region that enables Amazon Cognito authentication for Dashboards using the
`CognitoAccessForAmazonOpenSearch` role and provides domain access to
`Cognito_Auth_Role`:

```
aws opensearch create-domain --domain-name `my-domain` --region `us-east-1` --access-policies '{ "Version": "2012-10-17",		 	 	  "Statement":[{"Effect":"Allow","Principal":{"AWS": ["arn:aws:iam::`123456789012`:role/`Cognito_Auth_Role`"]},"Action":"es:ESHttp*","Resource":"arn:aws:es:`us-east-1:123456789012`:domain/*" }]}' --engine-version "OpenSearch_1.0" --cluster-config InstanceType=m4.xlarge.search,InstanceCount=1 --ebs-options EBSEnabled=true,VolumeSize=10 --cognito-options Enabled=true,UserPoolId="`us-east-1_123456789`",IdentityPoolId="`us-east-1:12345678-1234-1234-1234-123456789012`",RoleArn="arn:aws:iam::`123456789012`:role/`CognitoAccessForAmazonOpenSearch`"
```

After your domain finishes processing, see [Allowing the authenticated role](#cognito-auth-config-ac "#cognito-auth-config-ac") and [Configuring identity providers](#cognito-auth-identity-providers "#cognito-auth-identity-providers") for additional
configuration steps.

### Configuring Amazon Cognito Authentication (AWS

SDKs)

The AWS SDKs (except the Android and iOS SDKs) support all the operations that
are defined in the [Amazon OpenSearch Service API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md"), including the `CognitoOptions` parameter for the
`CreateDomain` and `UpdateDomainConfig` operations. For
more information about installing and using the AWS SDKs, see [AWS Software Development Kits](https://aws.amazon.com/code "https://aws.amazon.com/code").

After your domain finishes processing, see [Allowing the authenticated role](#cognito-auth-config-ac "#cognito-auth-config-ac") and [Configuring identity providers](#cognito-auth-identity-providers "#cognito-auth-identity-providers") for additional
configuration steps.

## Allowing the authenticated role

By default, the authenticated IAM role that you configured by following the
guidelines in [About the identity pool](#cognito-auth-prereq-ip "#cognito-auth-prereq-ip") does not have the necessary
privileges to access OpenSearch Dashboards. You must provide the role with additional
permissions.

###### Note

If you configured [fine-grained access control](fgac.md "fgac.md") and use
an open or IP-based access policy, you can skip this step.

You can include these permissions in an [identity-based](ac.md#ac-types-identity "ac.md#ac-types-identity") policy, but unless you want authenticated users to have
access to all OpenSearch Service domains, a [resource-based](ac.md#ac-types-resource "ac.md#ac-types-resource")
policy attached to a single domain is the better approach.

For the `Principal`, specify the ARN of the Cognito authenticated role that
you configured with the guidelines in [About the identity pool](#cognito-auth-prereq-ip "#cognito-auth-prereq-ip").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS":[
 "arn:aws:iam::`111122223333`:role/Cognito_`identitypoolname`/Auth_Role"
 ]
 },
 "Action":[
 "es:ESHttp*"
 ],
 "Resource":"arn:aws:es:`us-east-1`:`111122223333`:domain/`domain-name`/*"
 }
 ]
}`

```

For instructions about adding a resource-based policy to an OpenSearch Service domain, see [Configuring access
policies](createupdatedomains.md#createdomain-configure-access-policies "createupdatedomains.md#createdomain-configure-access-policies").

## Configuring identity providers

When you configure a domain to use Amazon Cognito authentication for Dashboards, OpenSearch Service adds an
[app
client](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md") to the user pool and adds the user pool to the identity pool as an
authentication provider.

###### Warning

Don't rename or delete the app client.

Depending on how you configured your user pool, you might need to create user accounts
manually, or users might be able to create their own. If these settings are acceptable,
you don't need to take further action. Many people, however, prefer to use external
identity providers.

To enable a SAML 2.0 identity provider, you must provide a SAML metadata document. To
enable social identity providers like Login with Amazon, Facebook, and Google, you must
have an app ID and app secret from those providers. You can enable any combination of
identity providers.

The easiest way to configure your user pool is to use the Amazon Cognito console. For
instructions, see [User
pool sign-in with third party identity providers](../../../cognito/latest/developerguide/cognito-user-pools-identity-federation.md "../../../cognito/latest/developerguide/cognito-user-pools-identity-federation.md") and [Application-specific settings with app client](../../../cognito/latest/developerguide/cognito-user-pools-app-idp-settings.md "../../../cognito/latest/developerguide/cognito-user-pools-app-idp-settings.md") in the
_Amazon Cognito Developer Guide_.

## (Optional) Configuring granular access

You might have noticed that the default identity pool settings assign every user who
logs in the same IAM role
(`Cognito_`identitypool`Auth_Role`), which means
that every user can access the same AWS resources. If you want to use [fine-grained access control](fgac.md "fgac.md") with Amazon Cognito—for example, if
you want your organization's analysts to have read-only access to several indices, but
developers to have write access to all indices—you have two options:

- Create user groups and configure your identity provider to choose the IAM
  role based on the user's authentication token (recommended).
- Configure your identity provider to choose the IAM role based on one or more
  rules.

For a walkthrough that includes fine-grained access control, see [Tutorial: Configure a domain with an IAM master user and Amazon Cognito
authentication](fgac-iam.md "fgac-iam.md").

###### Important

Just like the default role, Amazon Cognito must be part of each additional role's trust
relationship. For details, see [Creating roles for role mapping](../../../cognito/latest/developerguide/role-based-access-control.md#creating-roles-for-role-mapping "../../../cognito/latest/developerguide/role-based-access-control.md#creating-roles-for-role-mapping") in the
_Amazon Cognito Developer Guide_.

### User groups and tokens

When you create a user group, you choose an IAM role for members of the group.
For information about creating groups, see [Adding
groups to a user pool](../../../cognito/latest/developerguide/cognito-user-pools-user-groups.md "../../../cognito/latest/developerguide/cognito-user-pools-user-groups.md") in the
_Amazon Cognito Developer Guide_.

After you create one or more user groups, you can configure your authentication
provider to assign users their groups' roles rather than the identity pool's default
role. Select **Choose role from token**, then choose either
**Use default Authenticated role** or **DENY**
to specify how the identity pool handles users who aren't part of a group.

### Rules

Rules are essentially a series of `if` statements that Amazon Cognito evaluates
sequentially. For example, if a user's email address contains
`@corporate`, Amazon Cognito assigns that user `Role_A`. If a
user's email address contains `@subsidiary`, it assigns that user
`Role_B`. Otherwise, it assigns the user the default authenticated
role.

To learn more, see [Using rule-based mapping to assign roles to users](../../../cognito/latest/developerguide/role-based-access-control.md#using-rules-to-assign-roles-to-users "../../../cognito/latest/developerguide/role-based-access-control.md#using-rules-to-assign-roles-to-users") in the
_Amazon Cognito Developer Guide_.

## (Optional) Customizing the sign-in page

You can use the Amazon Cognito console to upload a custom logo and make CSS changes to the
sign-in page. For instructions and a full list of CSS properties, see [Customizing
hosted UI (classic) branding](../../../cognito/latest/developerguide/hosted-ui-classic-branding.md "../../../cognito/latest/developerguide/hosted-ui-classic-branding.md") in the
_Amazon Cognito Developer Guide_.

## (Optional) Configuring advanced security

Amazon Cognito user pools support advanced security features like multi-factor authentication,
compromised credential checking, and adaptive authentication. To learn more, see [Using Amazon Cognito user pools security features](../../../cognito/latest/developerguide/managing-security.md "../../../cognito/latest/developerguide/managing-security.md") in the
_Amazon Cognito Developer Guide_.

## Testing

After you're satisfied with your configuration, verify that the user experience meets
your expectations.

###### To access OpenSearch Dashboards

1. Navigate to
   `https://`opensearch-domain`/_dashboards`
   in a web browser. To log in to a specific tenant directly, append
   `?security_tenant=`tenant-name`` to
   the URL.
2. Sign in using your preferred credentials.
3. After OpenSearch Dashboards loads, configure at least one index pattern. Dashboards
   uses these patterns to identity which indices that you want to analyze. Enter
   `*`, choose **Next step**, and then choose
   **Create index pattern**.
4. To search or explore your data, choose **Discover**.

If any step of this process fails, see [Common configuration issues](#cognito-auth-troubleshooting "#cognito-auth-troubleshooting")
for troubleshooting information.

## Quotas

Amazon Cognito has soft limits on many of its resources. If you want to enable Dashboards
authentication for a large number of OpenSearch Service domains, review [Quotas in Amazon Cognito](../../../cognito/latest/developerguide/limits.md "../../../cognito/latest/developerguide/limits.md") and [request limit
increases](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") as necessary.

Each OpenSearch Service domain adds an [app
client](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md") to the user pool, which adds an [authentication
provider](../../../cognito/latest/developerguide/external-identity-providers.md "../../../cognito/latest/developerguide/external-identity-providers.md") to the identity pool. If you enable OpenSearch Dashboards authentication
for more than 10 domains, you might encounter the "maximum Amazon Cognito user pool
providers per identity pool" limit. If you exceed a limit, any OpenSearch Service domains that you try
to configure to use Amazon Cognito authentication for Dashboards can get stuck in a configuration
state of **Processing**.

## Common configuration issues

The following tables list common configuration issues and solutions.

| Configuring OpenSearch Service                                                                                                                                    | Issue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | -------- |
| `OpenSearch Service can't create the role` (console)                                                                                                              | You don't have the correct IAM permissions. Add the permissions specified in [Configuring Amazon Cognito authentication (console)](#cognito-auth-config-console "#cognito-auth-config-console").                                                                                                                                                                                                                                                                                                                                           |
| `User is not authorized to perform: iam:PassRole on resource CognitoAccessForAmazonOpenSearch` (console)                                                          | You don't have `iam:PassRole` permissions for the [CognitoAccessForAmazonOpenSearch](#cognito-auth-role "#cognito-auth-role") role. Attach the following policy to your account: JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "iam:PassRole" ], "Resource": "arn:aws:iam::`123456789012:role/service-role/CognitoAccessForAmazonOpenSearch`" } ] }` `` Alternately, you can attach the `IAMFullAccess` policy.                                                                                       |
| `User is not authorized to perform: cognito-identity:ListIdentityPools on resource`                                                                               | You don't have read permissions for Amazon Cognito. Attach the `AmazonCognitoReadOnly` policy to your account.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `An error occurred (ValidationException) when calling the CreateDomain operation: OpenSearch Service must be allowed to use the passed role`                      | OpenSearch Service isn't specified in the trust relationship of the `CognitoAccessForAmazonOpenSearch` role. Check that your role uses the trust relationship that is specified in [About the CognitoAccessForAmazonOpenSearch role](#cognito-auth-role "#cognito-auth-role"). Alternately, use the console to configure Amazon Cognito authentication. The console creates a role for you.                                                                                                                                                |
| `An error occurred (ValidationException) when calling the CreateDomain operation: User is not authorized to perform: cognito-idp:`action`on resource:`user pool`` | The role specified in `--cognito-options` does not have permissions to access Amazon Cognito. Check that the role has the AWS managed `AmazonOpenSearchServiceCognitoAccess` policy attached. Alternately, use the console to configure Amazon Cognito authentication. The console creates a role for you.                                                                                                                                                                                                                                 |
| `An error occurred (ValidationException) when calling the CreateDomain operation: User pool does not exist`                                                       | OpenSearch Service can't find the user pool. Confirm that you created one and have the correct ID. To find the ID, you can use the Amazon Cognito console or the following AWS CLI command: `` aws cognito-idp list-user-pools --max-results 60 --region `region` ``                                                                                                                                                                                                                                                                       |
| `An error occurred (ValidationException) when calling the CreateDomain operation: IdentityPool not found`                                                         | OpenSearch Service can't find the identity pool. Confirm that you created one and have the correct ID. To find the ID, you can use the Amazon Cognito console or the following AWS CLI command: `` aws cognito-identity list-identity-pools --max-results 60 --region `region` ``                                                                                                                                                                                                                                                          |
| `An error occurred (ValidationException) when calling the CreateDomain operation: Domain needs to be specified for user pool`                                     | The user pool does not have a domain name. You can configure one using the Amazon Cognito console or the following AWS CLI command: `` aws cognito-idp create-user-pool-domain --domain `name` --user-pool-id `id` ``                                                                                                                                                                                                                                                                                                                      | Accessing OpenSearch Dashboards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Issue | Solution |
| ---                                                                                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| The login page doesn't show my preferred identity providers.                                                                                                      | Check that you enabled the identity provider for the OpenSearch Service app client as specified in [Configuring identity providers](#cognito-auth-identity-providers "#cognito-auth-identity-providers").                                                                                                                                                                                                                                                                                                                                  |
| The login page doesn't look as if it's associated with my organization.                                                                                           | See [(Optional) Customizing the sign-in page](#cognito-auth-customize "#cognito-auth-customize").                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| My login credentials don't work.                                                                                                                                  | Check that you have configured the identity provider as specified in [Configuring identity providers](#cognito-auth-identity-providers "#cognito-auth-identity-providers"). If you use the user pool as your identity provider, check that the account exists on the Amazon Cognito console.                                                                                                                                                                                                                                               |
| OpenSearch Dashboards either doesn't load at all or doesn't work properly.                                                                                        | The Amazon Cognito authenticated role needs `es:ESHttp*` permissions for the domain (`/*`) to access and use Dashboards. Check that you added an access policy as specified in [Allowing the authenticated role](#cognito-auth-config-ac "#cognito-auth-config-ac").                                                                                                                                                                                                                                                                       |
| When I sign out of OpenSearch Dashboards from one tab, the remaining tabs display a message stating that the refresh token has been revoked.                      | When you sign out of an OpenSearch Dashboards session while using Amazon Cognito authentication, OpenSearch Service runs an [AdminUserGlobalSignOut](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUserGlobalSignOut.md") operation, which signs you out of _all_ active OpenSearch Dashboards sessions.                                                                                                                       |
| `Invalid identity pool configuration. Check assigned IAM roles for this pool.`                                                                                    | Amazon Cognito doesn't have permissions to assume the IAM role on behalf of the authenticated user. Modify the trust relationship for the role to include: JSON `` `{ "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": { "Federated": "cognito-identity.amazonaws.com" }, "Action": "sts:AssumeRoleWithWebIdentity", "Condition": { "StringEquals": { "cognito-identity.amazonaws.com:aud": "`identity-pool-id`" }, "ForAnyValue:StringLike": { "cognito-identity.amazonaws.com:amr": "authenticated" } } } ] }` `` |
| `Token is not from a supported provider of this identity pool.`                                                                                                   | This uncommon error can occur when you remove the app client from the user pool. Try opening Dashboards in a new browser session.                                                                                                                                                                                                                                                                                                                                                                                                          | ## Disabling Amazon Cognito authentication for OpenSearch Dashboards Use the following procedure to disable Amazon Cognito authentication for Dashboards. ###### To disable Amazon Cognito authentication for Dashboards (console) 1. Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home/ "https://console.aws.amazon.com/aos/home/"). 2. Under **Domains**, choose the domain you want to configure. 3. Choose **Actions**, **Edit security configuration**. 4. Deselect **Enable Amazon Cognito authentication**. 5. Choose **Save changes**. ###### Important If you no longer need the Amazon Cognito user pool and identity pool, delete them. Otherwise, you continue to incur charges. ## Deleting domains that use Amazon Cognito authentication for OpenSearch Dashboards To prevent domains that use Amazon Cognito authentication for Dashboards from becoming stuck in a configuration state of **Processing**, delete OpenSearch Service domains _before_ deleting their associated Amazon Cognito user and identity pools. |
