# IAM Identity Center support for Amazon OpenSearch Serverless

## IAM Identity Center support for Amazon OpenSearch Serverless

You can use IAM Identity Center principals (users and groups) to access Amazon OpenSearch Serverless data through
Amazon OpenSearch Applications. In order to enable IAM Identity Center support for Amazon OpenSearch Serverless, you will
need to enable use of IAM Identity Center. To learn more on how to do this, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")

After the IAM Identity Center instance is created, the customer account administrator needs to
create an IAM Identity Center application for the Amazon OpenSearch Serverless service. This can be done by calling the
[CreateSecurityConfig:](../ServerlessAPIReference/API_CreateSecurityConfig.md "../ServerlessAPIReference/API_CreateSecurityConfig.md"). The customer account administrator can specify what
attributes will be used for authorizing the request. The default attributes used are
`UserId` and `GroupId.`

The IAM Identity Center integration for Amazon OpenSearch Serverless uses the following AWS IAM Identity Center (IAM)
permsions:

- `aoss:CreateSecurityConfig` – Create an IAM Identity Center provider
- `aoss:ListSecurityConfig` – List all IAM Identity Center providers in the current
  account.
- `aoss:GetSecurityConfig` – View IAM Identity Center provider information.
- `aoss:UpdateSecurityConfig` – Modify a given IAM Identity Center
  configuration
- `aoss:DeleteSecurityConfig` – Delete an IAM Identity Centerprovider.

The following idenity-based access policy can be used to manage all IAM Identity Center
configurations:

JSON

```
`{
"Version": "2012-10-17",
 "Statement": [
 {
"Action": [
 "aoss:CreateSecurityConfig",
 "aoss:DeleteSecurityConfig",
 "aoss:GetSecurityConfig",
 "aoss:UpdateSecurityConfig",
 "aoss:ListSecurityConfigs"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

###### Note

The `Resource` element must be a wildcard.

## Creating an IAM Identity Center provider

(console)

You can create an IAM Identity Center provider to enable authentication with OpenSearch
Application. To enable IAM Identity Center authentication for OpenSearch Dashboards, perform the following
steps:

1. Sign in to the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home. "https://console.aws.amazon.com/aos/home.").
2. On the left navigation panel, expand
   **Serverless** and choose
   **Authentication**.
3. Choose **IAM Identity Center
   authentication**.
4. Select **Edit**
5. Check the box next to Authenticate with IAM Identity Center.
6. Select the **user and group** attribute key
   from the dropdown menu. User attributes will be used to authorize users based on
   `UserName`, `UserId`, and `Email`. Group
   attributes will be used to authenticate users based on `GroupName`
   and `GroupId`.
7. Select the
   **IAM Identity Center** instance.
8. Select **Save**

## Creating IAM Identity Center provider

(AWS CLI)

To create an IAM Identity Center provider using the AWS Command Line Interface (AWS CLI) use the following
command:

```
aws opensearchserverless create-security-config \
--region us-east-2 \
--name "iamidentitycenter-config" \
--description "description" \
--type "iamidentitycenter" \
--iam-identity-center-options '{
    "instanceArn": "arn:aws:sso:::instance/ssoins-99199c99e99ee999",
    "userAttribute": "UserName",
    "groupAttribute": "GroupId"
}'
```

After an IAM Identity Center is enabled, customers can only modify **user and group** attributes.

```
aws opensearchserverless update-security-config \
--region us-east-1 \
--id <id_from_list_security_configs> \
--config-version <config_version_from_get_security_config> \
--iam-identity-center-options-updates '{
    "userAttribute": "UserId",
    "groupAttribute": "GroupId"
}'
```

In order to view the IAM Identity Center provider using the AWS Command Line Interface, use the following
command:

```
aws opensearchserverless list-security-configs --type iamidentitycenter
```

## Deleting an IAM Identity Center provider

IAM Identity Center offers two instances of providers, one for your organization account and
one for your member account. If you need to change your IAM Identity Center instance, you need to
delete your security configuration through the `DeleteSecurityConfig` API and
create a new security configuration using the new IAM Identity Center instance. The following command
can be used to delete an IAM Identity Center provider:

```
aws opensearchserverless delete-security-config \
--region us-east-1 \
--id <id_from_list_security_configs>
```

## Granting IAM Identity Center access to

collection data

After your IAM Identity Center provider is enabled, you can update the collection data access
policy to include IAM Identity Center principals. IAM Identity Center principals need to be updated in the
following format:

```
[
   {
"Rules":[
       ...
      ],
      "Principal":[
         "iamidentitycenter/<iamidentitycenter-instance-id>/user/<UserName>",
         "iamidentitycenter/<iamidentitycenter-instance-id>/group/<GroupId>"
      ]
   }
]
```

###### Note

Amazon OpenSearch Serverless supports only one IAM Identity Center instance for all customer collections and
can support up to 100 groups for a single user. If you try to use more than the
number of allowed instances, you will experience inconsistency with your data
access policy authorization processing and receive a `403`error message.

You can grant access to collections, indexes, or both. If you want different users
to have different permssions, you will need to create multiple rules. For a list of
available permissions, see [Identity and Access Management in Amazon OpenSearch Service](ac.md "ac.md"). For information about how
to format an access policy, see [Granting SAML identities access to collection data](serverless-saml.md#serverless-saml-policies "serverless-saml.md#serverless-saml-policies") .

IAM Identity Center offers two instances of providers, one for your organization account and one for
your member accout. If you need to change your IAM Identity Center instance, you need to delete your
security configuration through the `DeleteSecurityConfig` API and create a
new security configuration using the new IAM Identity Center instance. The following command can be
used to delete an IAM Identity Center provider:

```
aws opensearchserverless delete-security-config \
--region us-east-1 \
--id <id_from_list_security_configs>
```
