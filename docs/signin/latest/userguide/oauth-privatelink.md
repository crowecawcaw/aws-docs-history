# AWS PrivateLink

AWS Sign-In OAuth APIs support AWS PrivateLink, enabling you to access OAuth
authorization endpoints from within your Amazon VPC without traversing the public internet.
You can configure VPC endpoints for AWS Sign-In to keep OAuth authorization traffic on
the AWS network.

Use VPC endpoints for AWS Sign-In OAuth when you need:

- Private connectivity for OAuth authorization flows from within your Amazon VPC
  or connected on-premises networks.
- Network-level access controls for OAuth authorization using VPC endpoint
  policies.
- OAuth authorization in network-isolated environments without public internet
  access.

## Configuring VPC endpoints for accessing Sign-In OAuth APIs

AWS Sign-In OAuth supports operating in networks without access to the public
internet. When you configure a VPC endpoint for AWS Sign-In, OAuth authorization
traffic between your applications and AWS Sign-In is routed through AWS
PrivateLink. Internet connectivity is not required for the OAuth authorization
flow itself.

The VPC endpoint required depends on your authorization model. Replace
`region` with your own Region information.

### Interactive mode

Interactive OAuth authorization (browser-based) requires the following VPC
endpoints:

- `com.amazonaws.`region`.signin`
- `com.amazonaws.`region`.signin-v2`

### Non-interactive mode

Non-interactive OAuth authorization (client credentials grant using SigV4)
requires the following VPC endpoint:

- `com.amazonaws.`region`.signin-v2`

## Implementing access controls

You can use VPC endpoint policies to control which identities and accounts are
permitted to use AWS Sign-In OAuth APIs through your private network. VPC endpoint
policies are evaluated across OAuth operations.

### Trusted identities

The AWS Sign-In VPC endpoint requires policies with specific Sign-In actions
and condition keys appropriate to each authentication phase:

- **Pre-authentication phase** –
  Evaluated before the user's identity is established. Only
  resource-based condition keys are available, because principal
  information is not yet known.

  - Supported actions:
    `signin:Authenticate`,
    `signin:CreateOAuth2PublicClient`
  - Supported condition keys:
    `aws:ResourceOrgId` or
    `aws:ResourceAccount`

###### Note

`signin:CreateOAuth2PublicClient` only supports the
`signin:OAuthRedirectUri` condition key. Other condition
keys are not supported with this action.

- **Post-authentication phase** –
  Evaluated after authentication when the sign-in service issues session
  credentials. Full principal information is available.

  - Supported actions:
    `signin:AuthorizeOAuth2Access`,
    `signin:CreateOAuth2Token`,
    `signin:IntrospectOAuth2Token`,
    `signin:RevokeOAuth2Token`
  - Supported condition keys:
    `aws:PrincipalOrgId` or
    `aws:PrincipalAccount`,
    `aws:ResourceOrgId`,
    `aws:ResourceAccount`

#### Example: Allow OAuth operations only for accounts in your organization

This AWS Sign-In VPC endpoint policy uses action-specific statements to
allow OAuth operations for AWS accounts in the specified AWS
organization at both the pre-authentication and post-authentication
phases.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "PreAuthOrgRestriction",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "signin:Authenticate",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceOrgID": "o-xxxxxxxxxxx"
        }
      }
    },
    {
      "Sid": "PostAuthOrgRestriction",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "signin:AuthorizeOAuth2Access",
        "signin:CreateOAuth2Token"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgId": "o-xxxxxxxxxxx"
        }
      }
    }
  ]
}
```

#### Example: Allow OAuth operations only for specific accounts

This AWS Sign-In VPC endpoint policy uses action-specific statements to
allow OAuth operations for a list of specific AWS accounts at both the
pre-authentication and post-authentication phases.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "PreAuthAccountRestriction",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "signin:Authenticate",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": [ "123456789012", "210987654321" ]
        }
      }
    },
    {
      "Sid": "PostAuthAccountRestriction",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "signin:AuthorizeOAuth2Access",
        "signin:CreateOAuth2Token"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalAccount": [ "123456789012", "210987654321" ]
        }
      }
    }
  ]
}
```

#### Example: Restrict Dynamic Client Registration to localhost redirect URIs

This AWS Sign-In VPC endpoint policy restricts Dynamic Client Registration
to localhost redirect URIs only.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowDCRLocalhostOnly",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "signin:CreateOAuth2PublicClient",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "signin:OAuthRedirectUri": "http://localhost:*"
        }
      }
    }
  ]
}
```

#### Example: Allow token introspection and revocation for specific accounts

This AWS Sign-In VPC endpoint policy allows token introspection and
revocation for specific AWS accounts.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowIntrospectAndRevoke",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "signin:IntrospectOAuth2Token",
        "signin:RevokeOAuth2Token"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalAccount": [ "123456789012", "210987654321" ]
        }
      }
    }
  ]
}
```

### Expected networks

For network-based access controls, see [Controlling console access with resource-based policies and resource control policies](console-access-control.md "console-access-control.md").

### Controlling account signup flows

The `signin:CreateAccount` action controls whether the AWS
account signup flow is accessible from within your private network. This action
uses an anonymous principal (no account exists during signup) and does not
support condition keys.

When using the AWS Sign-In VPC endpoint policy format, the signup flow is
blocked by implicit deny unless you explicitly allow it. If your organization
requires account signup from within the private network, add the following
statement to your AWS Sign-In VPC endpoint policy:

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccountSignup",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "signin:CreateAccount",
      "Resource": "*"
    }
  ]
}
```
