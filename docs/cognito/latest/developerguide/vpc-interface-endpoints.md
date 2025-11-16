# Access Amazon Cognito user pools using an interface endpoint

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and Amazon Cognito. You
can access Amazon Cognito as if it were in your VPC, without the use of an internet gateway, NAT
device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to access
Amazon Cognito.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for Amazon Cognito.

For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

###### Important

The following authentication types aren't currently supported through
AWS PrivateLink:

1. Machine to machine (M2M) authorization with the OAuth 2.0 client credentials
   flow
2. Sign-in with managed login and the classic hosted UI.

###### Topics

- [Authentication flows for
  AWS PrivateLink integration](#privatelink-authentication-flows "#privatelink-authentication-flows")
- [Operational modes for
  AWS PrivateLink](#privatelink-operational-modes "#privatelink-operational-modes")
- [Considerations for Amazon Cognito](#vpc-endpoint-considerations "#vpc-endpoint-considerations")
- [Controlling access with resource
  control policies](#vpc-endpoint-considerations-rcps "#vpc-endpoint-considerations-rcps")
- [Create an interface endpoint for Amazon Cognito](#vpc-endpoint-create "#vpc-endpoint-create")
- [Create an endpoint policy for your interface
  endpoint](#vpc-endpoint-policy "#vpc-endpoint-policy")
- [Create an identity-based policy for
  AWS PrivateLink operations](#identity-based-vpc-policy "#identity-based-vpc-policy")

## Authentication flows for

AWS PrivateLink integration

The following table describes the authentication flows available to clients in VPCs,
and the IAM policies that you can apply to govern them. The policies that you can
evaluate in requests to user pools are resource control policies (RCPs), VPC endpoint
policies, and identity-based policies.

| Resource  | Authentication flow                                                                                                                                                                                                                                          | Policies evaluated when client transits a VPC endpoint                                                                | Policies evaluated when client origin is public              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| User pool | [Managed login &<br>classic hosted UI sign-in](cognito-user-pools-managed-login.md "cognito-user-pools-managed-login.md")                                                                                                                                    | None (no access)[1](#privatelink-vpc-endpoint-note "#privatelink-vpc-endpoint-note")                                  | None[2](#privatelink-domain-note "#privatelink-domain-note") |
| User pool | [Machine-to-machine authorization](cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-about-m2m "cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-about-m2m")                  | None (no access)[1](#privatelink-vpc-endpoint-note "#privatelink-vpc-endpoint-note")                                  | None[2](#privatelink-domain-note "#privatelink-domain-note") |
| User pool | SDK and REST API unauthenticated requests                                                                                                                                                                                                                    | RCPs, VPC endpoint policies[3](#privatelink-no-domain-note "#privatelink-no-domain-note")                             | RCPs                                                         |
| User pool | SDK and REST API SigV4 [authenticated](authentication-flows-public-server-side.md#amazon-cognito-user-pools-server-side-authentication-flow "authentication-flows-public-server-side.md#amazon-cognito-user-pools-server-side-authentication-flow") requests | RCPs, VPC endpoint policies, identity-based<br>policies[3](#privatelink-no-domain-note "#privatelink-no-domain-note") | RCPs, identity-based policies                                |

1
VPC endpoints don't accept requests for user pool domains. If the client has a route to
the internet, NAT is applied, making the origin public.

2 The
existence of a user pool domain prevents completion of any user pool requests that
transit a VPC endpoint. Any client can take public transit paths _only_ to the user pool domain and API service endpoints, making the VPC
endpoint unusable for the user pool. User pools with domains assigned are incompatible
with AWS PrivateLink.

3
User pool must _not_ have a domain assigned.

## Operational modes for

AWS PrivateLink

The following example implementation models are supported with AWS PrivateLink and
Amazon Cognito.

| Resource  | Implementation                                   | Actions                                                                                                             |
| --------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| User pool | Fully private SDK or REST API application        | 1. Delete domain<br>2. Create VPC endpoint<br>3. Configure RCP to `Deny` all cognito-idp actions<br>except from VPC |
| User pool | Private and public                               | 1. Delete domain<br>2. Create VPC endpoint                                                                          |
| User pool | Private or public OAuth 2.0 authorization server | 1. Not available to VPC                                                                                             |

## Considerations for Amazon Cognito

Before you set up an interface endpoint for Amazon Cognito, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_. Amazon Cognito
supports making calls to all Amazon Cognito API actions through the interface endpoint. For more
information about these operations, see the [Amazon Cognito user pools API
Reference](../../../cognito-user-identity-pools/latest/APIReference/Welcome.md "../../../cognito-user-identity-pools/latest/APIReference/Welcome.md").

AWS PrivateLink for Amazon Cognito is only available in commercial AWS Regions.

###### Topics

- [User pools and
  AWS PrivateLink](#vpc-endpoint-considerations-user-pools "#vpc-endpoint-considerations-user-pools")

### User pools and

AWS PrivateLink

You can make requests to all user pools API operations through the interface
endpoint, but not to operations that your application requests from the user pool
OAuth 2.0 authorization server for example client credentials grants and managed
login.

The `cognito-idp` user pools API has [unauthenticated,
authenticated, and token-authorized API operations](authentication-flows-public-server-side.md "authentication-flows-public-server-side.md"). You can grant
permissions for authenticated operations in VPC endpoint and resource control
policies. You can _also_ grant permissions for
unauthenticated and token-authorized operations, unlike in identity-based policies.
VPC endpoint and resource control policy types are able to evaluate and deny or
allow requests for otherwise-public operations.

Requests to domain endpoints are also public, but you can't evaluate them in
policies. VPC private DNS doesn't route requests for user pool domains to your VPC
endpoint. You can only make requests for domain services through public-internet
paths. For more information, see [Effects of policies
on user pool operations](#vpc-endpoint-considerations-policy-effects "#vpc-endpoint-considerations-policy-effects").

###### Topics

- [Supported
  operations](#vpc-endpoint-considerations-supported-operations "#vpc-endpoint-considerations-supported-operations")
- [Effects of policies
  on user pool operations](#vpc-endpoint-considerations-policy-effects "#vpc-endpoint-considerations-policy-effects")

#### Supported

operations

Systems in a VPC can send requests to [user pool API actions](../../../service-authorization/latest/reference/list_amazoncognitouserpools.md "../../../service-authorization/latest/reference/list_amazoncognitouserpools.md") but _not_ to
user pool [domain
endpoints](cognito-userpools-server-contract-reference.md "cognito-userpools-server-contract-reference.md"). OpenID Connect (OIDC) and OAuth 2.0 workflows that use
domain endpoints, for example [machine-to-machine
(M2M)](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md"), [federated sign-in](cognito-user-pools-identity-federation.md "cognito-user-pools-identity-federation.md"), and [authorization code grants](authorization-endpoint.md "authorization-endpoint.md"), are inaccessible through VPC endpoints.
VPC endpoint policies have no effect on these HTTP workflows and can't process
them. Requests to domain endpoints from within a VPC always fail at the
interface endpoint, but continue to be available through public DNS and routing
when you set up VPC endpoints for your user pools.

To prevent the assignment of domains from systems in a VPC, Amazon Cognito blocks
`CreateUserPoolDomain` requests at the interface endpoint. This
prevents addition of domains to your user pools from systems that are in a VPC.
To prevent the addition of a domain from all systems, apply a [resource
control policy](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") (RCP) like the following example to your
AWS account. This policy blocks the `CreateUserPoolDomain` action
against the specified user pool.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Deny",
            "Action": [
                "cognito-idp:CreateUserPoolDomain"
            ],
            "Resource": "arn:`aws`:cognito-idp:`us-east-1`:123456789012:userpool/`us-east-1_EXAMPLE`"
        }
    ]
}
```

Your user pool might have a domain, and in all cases that domain is
unavailable through AWS PrivateLink. All SDK-based [user pool API requests](../../../service-authorization/latest/reference/list_amazoncognitouserpools.md "../../../service-authorization/latest/reference/list_amazoncognitouserpools.md") to `cognito-idp`
[service
endpoints](../../../general/latest/gr/cognito.md#cognito-idp-region "../../../general/latest/gr/cognito.md#cognito-idp-region") accept requests through AWS PrivateLink, with the exception
of `CreateUserPoolDomain`. User pool API service endpoints and domain
endpoints remain always accessible through public-internet paths. To address
access from public sources, implement [AWS WAF
web ACLs](user-pool-waf.md "user-pool-waf.md").

#### Effects of policies

on user pool operations

All user pool API operations, even those that are typically public and
unauthenticated, can be controlled in VPC endpoint policies and resource control
policies (RCPs). You can also apply restrictions to user pool access in
identity-based policies with VPC condition keys. Only requests that include
authentication information in [SigV4 format](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") can be
controlled in identity-based policies. Managed login and classic hosted UI
operations are a separate category, and aren't eligible for VPC transit or the
application of any type of policies to their actions.

###### Unauthenticated operations

Amazon Cognito operations for client-side applications aren't authenticated with
SigV4. Example operations are in the example policy at [Create an endpoint policy for your interface
endpoint](#vpc-endpoint-policy "#vpc-endpoint-policy").
Additional examples of unauthenticated operations are `GetUser`
and `AssociateSoftwareToken`. When you add these operations to
[identity-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md"), they have no effect. However, you can
permit or restrict access to these actions in VPC endpoint policies and
[RCPs](#vpc-endpoint-considerations-rcps "#vpc-endpoint-considerations-rcps").

Unauthenticated operations aren't associated with an IAM principal. Your VPC
endpoint policy or RCP must allow all principals for these actions.

###### Authenticated operations

API operations for user pool administration and server-side authentication
_are_ authenticated with SigV4. For
authenticated operations, you can restrict principals with [endpoint
policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") that you apply to the VPC endpoint, [resource control policies](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in your organization, and in [identity-based policies](#identity-based-vpc-policy "#identity-based-vpc-policy") that
you apply to principals. Identity-based and resource-control policies are
VPC-aware with [network-based condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-network-properties "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-network-properties") like `aws:SourceVpc`
and `aws:SourceVpce`.

For more information about server-side, client-side, and administrative
classes of API operations for user pools, see [Authorization models for API and SDK
authentication](authentication-flows-public-server-side.md "authentication-flows-public-server-side.md").

## Controlling access with resource

control policies

Amazon Cognito supports controlling access to your resources with [resource control
policies](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") (RCPs). With [network-based condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-network-properties "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-network-properties"), RCPs can define the networks and actions that
are permitted for AWS PrivateLink access to your user pools and identity pools. The
`Action` statements in RCPs can control access to both authenticated and
unauthenticated user pool API operations.

For example, the following example policy prevents access to all user pools from a
specific VPC.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyCognitoAccessOutsideVPC",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "cognito-idp:*",
      "Resource": "*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "aws:SourceVpc": "vpc-02d6770f46ef1653b"
        }
      }
    }
  ]
}
```

## Create an interface endpoint for Amazon Cognito

You can create an interface endpoint for Amazon Cognito using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

Create an interface endpoint for Amazon Cognito user pools using the following service name:

```
com.amazonaws.`region`.cognito-idp
```

If you enable private DNS for the interface endpoint, you can make API requests to
Amazon Cognito using its default Regional DNS name. For example,
`cognito-idp.us-east-1.amazonaws.com` for user pools.

## Create an endpoint policy for your interface

endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Amazon Cognito through the interface endpoint.
To control the access allowed to Amazon Cognito from your VPC, attach a custom endpoint policy to
the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.
- The conditions that must be satisfied before the request is allowed or
  denied.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for user pool actions

The following is an example of a custom endpoint policy for user pools. When you
attach this policy to your interface endpoint, it grants access to the listed user
pool actions for all principals on all resources.

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Principal": {
            "AWS": "`arn:aws:iam::123456789012:assumed-role/MyWebAppRole/MyWebAppSession`"
         },
         "Effect": "Allow",
         "Action": [
            "`cognito-idp`:`AdminInitiateAuth`",
            "`cognito-idp`:`AdminRespondToAuthChallenge`",
            "`cognito-idp`:`AdminSetUserPassword`"
         ],
         "Resource":"arn:`aws`:cognito-idp:`us-east-1`:123456789012:userpool/`us-east-1_EXAMPLE`"
      },
      {
         "Effect": "Allow",
         "Action": [
            "`cognito-idp`:`InitiateAuth`",
            "`cognito-idp`:`RespondToAuthChallenge`",
            "`cognito-idp`:`ForgotPassword`",
            "`cognito-idp`:`ConfirmForgotPassword`"
         ],
         "Resource":"arn:`aws`:cognito-idp:`us-east-1`:123456789012:userpool/`us-east-1_EXAMPLE`"
      }
   ]
}
```

## Create an identity-based policy for

AWS PrivateLink operations

[Identity-based
policies](../../../IAM/latest/UserGuide/access_policies.md#policies_id-based "../../../IAM/latest/UserGuide/access_policies.md#policies_id-based") are IAM resources that you can attach to AWS principals. You
can control access to Amazon Cognito through VPC endpoints with identity-based policies for
IAM-authenticated operations. Unlike endpoint policies, you can't configure
permissions for unauthenticated operations in identity-based policies. Authenticated, or
administrative, operations require [Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
authorization. For user pools, authenticated operations include server-side
authentication requests like [AdminInitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminInitiateAuth.md") and administrative requests like [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md").

An identity-based policy specifies the following information:

- The actions that can be performed.
- The resources on which the actions can be performed.
- The conditions that must be satisfied before the request is allowed or
  denied.

###### Example: identity-based policy for user pool server-side authentication

The following example policy grants access to the listed user pool actions in the
specified user pool, from the specified endpoint. Apply this policy to the assumed
IAM role for your web application.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cognito-idp:AdminInitiateAuth",
                "cognito-idp:AdminRespondToAuthChallenge",
                "cognito-idp:AdminSetUserPassword"
            ],
            "Resource": "arn:aws:cognito-idp:`us-east-1`:`123456789012`:userpool/`us-east-1_EXAMPLE`",
            "Condition": {
                "StringEquals": {
                    "aws:SourceVpce": "`vpce-1a2b3c4d`"
                }
            }
        }
    ]
}
```
