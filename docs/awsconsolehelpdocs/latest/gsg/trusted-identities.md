

# Trusted identities
<a name="trusted-identities"></a><a name="account-identity"></a>

With AWS Management Console Private Access, you can restrict which AWS accounts and organizational identities can use the AWS Management Console from within your VPC. This prevents access from personal accounts and from accounts outside your organization.

The AWS Management Console and AWS Sign-In VPC endpoints each support a VPC endpoint policy that controls the identity of the signed-in account. Policies are evaluated at the time of sign-in and are periodically re-evaluated for existing sessions.
+ **AWS Management Console VPC endpoint policies** – Restrict which signed-in identities can access the AWS Management Console through this endpoint. Use `Action: *` and `Principal: *`, with `aws:PrincipalOrgId` or `aws:PrincipalAccount` condition keys.
+ **AWS Sign-In VPC endpoint policies (sign-in flow)** – Restrict who can sign in to the AWS Management Console through this endpoint, with separate evaluation before and after credentials are validated. **Pre-authentication** blocks sign-in attempts before credentials are entered, using `signin:Authenticate`. **Post-authentication** validates the session after credentials are accepted and during OAuth token exchange, using `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token`.
+ **AWS Sign-In VPC endpoint policies (signup flow)** – Control whether the AWS account signup flow is accessible from within your private network. Supports the `signin:CreateAccount` action with implicit deny.

The following examples show how to restrict access by account or organization. Apply equivalent restrictions to both your AWS Management Console and AWS Sign-In VPC endpoints, using the appropriate policy format for each endpoint.

**Topics**
+ [AWS Management Console VPC endpoint examples](#console-vpc-endpoint-examples)
+ [AWS Sign-In VPC endpoint examples](#signin-vpc-endpoint-examples)
+ [Access denied error page](#access-denied-error)
+ [Allowing sign-in in service control policies](#private-access-with-SCPs)

**Note**  
The following examples are reference policies for illustration only. For production environments, use the comprehensive data perimeter policy examples in the [aws-samples/data-perimeter-policy-examples](https://github.com/aws-samples/data-perimeter-policy-examples) repository, such as the [network perimeter SCP](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_control_policies/network_perimeter_sourcevpc_scp.json).

## AWS Management Console VPC endpoint examples
<a name="console-vpc-endpoint-examples"></a>

**Example: Allow only accounts in your organization**  
This AWS Management Console VPC endpoint policy allows access for AWS accounts in the specified AWS organization and blocks any other accounts.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "*",
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

------

**Example: Allow only specific accounts**  
This AWS Management Console VPC endpoint policy limits access to a list of specific AWS accounts and blocks any other accounts.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalAccount": [ "111122223333", "222233334444" ]
        }
      }
    }
  ]
}
```

------

## AWS Sign-In VPC endpoint examples
<a name="signin-vpc-endpoint-examples"></a>

The AWS Sign-In VPC endpoint requires policies with specific Sign-In actions and condition keys appropriate to each authentication phase:
+ **Pre-authentication phase** – Evaluated before the user's identity is established. Only resource-based condition keys are available, because principal information is not yet known.
  + Supported action: `signin:Authenticate`
  + Supported condition keys: `aws:ResourceOrgId` or `aws:ResourceAccount`
+ **Post-authentication phase** – Evaluated after authentication when the sign-in service issues session credentials. Full principal information is available.
  + Supported actions: `signin:AuthorizeOAuth2Access`, `signin:CreateOAuth2Token`
  + Supported condition keys: `aws:PrincipalOrgId` or `aws:PrincipalAccount`, `aws:ResourceOrgId`, `aws:ResourceAccount`

**Example: Allow sign-in only for accounts in your organization**  
This AWS Sign-In VPC endpoint policy uses action-specific statements to allow sign-in for AWS accounts in the specified AWS organization at both the pre-authentication and post-authentication phases.

------
#### [ JSON ]

****  

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

------

**Example: Allow sign-in only for specific accounts**  
This AWS Sign-In VPC endpoint policy uses action-specific statements to limit sign-in to a list of specific AWS accounts at both the pre-authentication and post-authentication phases.

------
#### [ JSON ]

****  

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

------

**Controlling account signup flows**  
The `signin:CreateAccount` action controls whether the AWS account signup flow is accessible from within your private network. This action uses an anonymous principal (no account exists during signup) and does not support condition keys.

When using the AWS Sign-In VPC endpoint policy format, the signup flow is blocked by implicit deny unless you explicitly allow it. If your organization requires account signup from within the private network, add the following statement to your AWS Sign-In VPC endpoint policy:

------
#### [ JSON ]

****  

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

------

## Access denied error page
<a name="access-denied-error"></a>

If you connect with an identity that does not belong to your account, you see the "Your account doesn't have permission to use AWS Management Console Private Access" error. The following screenshot shows the access denied error page.

![The error page with a message that indicates that you don't have permission to use AWS Management Console Private Access.](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/images/console-private-access-denied.png)


## Allowing sign-in in service control policies
<a name="private-access-with-SCPs"></a>

If your AWS organization is using a service control policy (SCP) that allows specific services, you must add `signin:*` to the allowed actions. This permission is needed because signing in to the AWS Management Console over a Private Access VPC endpoint performs an IAM authorization that the SCP blocks without the permission. As an example, the following service control policy allows the Amazon EC2 and CloudWatch services to be used in the organization, including when they are accessed using an AWS Management Console Private Access endpoint.

```
{
  "Effect": "Allow",
  "Action": [
    "signin:*",
    "ec2:*",
    "cloudwatch:*",
    ... Other services allowed
  },
  "Resource": "*"
}
```

For more information about SCPs, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.