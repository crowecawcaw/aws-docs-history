# Restricting network access to OpenSearch UI applications

By default, an OpenSearch UI application exposes a public endpoint that accepts requests
from any network location. Your users are still subject to authentication (IAM or
AWS IAM Identity Center) and authorization, but anyone on the public internet can
_reach_ the application and its APIs.

If you require that access to OpenSearch UI come only from an approved network, you can
enforce this with the AWS Identity and Access Management (IAM) policy tools you already use. For example, you can
require that access arrive only through an interface VPC endpoint (AWS PrivateLink) or only
from a range of corporate IP addresses. Because OpenSearch UI evaluates access with
standard IAM request condition keys, you use the same policy language and condition keys
(`aws:SourceVpce`, `aws:SourceVpc`, and `aws:SourceIp`) that
you already use elsewhere in AWS. You don't need to learn a service-specific policy
format.

You can restrict access at three levels, from the most targeted to the broadest:

- An **identity-based policy** restricts a specific
  principal (user or role).
- A **VPC endpoint policy** restricts which applications
  users can reach through a specific endpoint.
- A **resource control policy (RCP)** enforces access
  uniformly across every account in your organization, and can block off-network users
  _before_ they authenticate.
  This topic describes how OpenSearch UI evaluates network access and walks through the
  most common task, blocking the login page for users outside an approved network. For policy
  examples and AWS CLI commands for each of the three control types, see [Network access control configuration reference for OpenSearch UI applications](application-network-access-reference.md "application-network-access-reference.md"). For information about creating the
  private connection itself, see [Managing access to the OpenSearch UI from a VPC endpoint](application-access-ui-from-vpc-endpoint.md "application-access-ui-from-vpc-endpoint.md").

###### Topics

- [How OpenSearch UI evaluates network access](#application-network-access-how "#application-network-access-how")
- [Prerequisites](#application-network-access-prereqs "#application-network-access-prereqs")
- [Blocking login page access from outside an approved network](#application-network-access-block-login-page "#application-network-access-block-login-page")
- [Considerations](#application-network-access-considerations "#application-network-access-considerations")
- [Network access control configuration reference for OpenSearch UI applications](application-network-access-reference.md "application-network-access-reference.md")

## How OpenSearch UI evaluates network access

OpenSearch UI evaluates access in two stages, and each stage authorizes a distinct
IAM action against the application resource.

- **`opensearch:ViewLoginPage`**.
  Authorized _before_ a user signs in, when the browser first
  requests the application login page. The user has no AWS credentials yet, so
  this request is anonymous. Because OpenSearch UI evaluates this action before
  authentication, a resource control policy that denies it for off-network
  requests prevents off-network users from reaching the login page. This denial
  applies uniformly to both IAM and AWS IAM Identity Center users.
- **`opensearch:ApplicationAccessAll`**.
  Authorized _after_ a user signs in, for access to the
  application and its APIs. You can restrict this action with an identity-based
  policy, a VPC endpoint policy, or an RCP.

OpenSearch UI authorizes both actions against the application resource ARN:

```
arn:aws:opensearch:`region`:`account-id`:application/`application-id`
```

When a request arrives, OpenSearch UI populates the following IAM request condition
keys from the trusted network metadata of the connection, so you can reference them in
your policy conditions:

- `aws:SourceVpce`. The ID of the interface VPC endpoint the
  request arrived through, if any.
- `aws:SourceVpc`. The ID of the VPC the request arrived
  through, if any.
- `aws:SourceIp`. The public source IP address of the
  request, for requests that do not arrive through a VPC endpoint.

## Prerequisites

- To restrict a specific principal, you must have permission to manage IAM
  policies for the users or roles that access the application. To restrict an
  endpoint, you must have permission to manage the policy of the VPC endpoint used
  to reach it.
- To enforce access across your organization with a resource control policy, your
  account must be a member of an AWS organization with all features enabled, and
  you must have permission to manage resource control policies. For more
  information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS
  Organizations User Guide_.

###### Note

A resource control policy has no effect on resources in the
organization's management account. To restrict network access to an
OpenSearch UI application with an RCP, the application must be in a member
account.

- To restrict access to a VPC endpoint, first create an interface VPC endpoint
  for OpenSearch UI. For more information, see [Managing access to the OpenSearch UI from a VPC endpoint](application-access-ui-from-vpc-endpoint.md "application-access-ui-from-vpc-endpoint.md").
- To run the AWS Command Line Interface (AWS CLI) examples in this topic, install and configure the
  AWS CLI. For more information, see [Getting started with
  the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS Command Line Interface User
  Guide_.

## Blocking login page access from outside an approved network

The following procedure blocks the login page for users outside your approved network.
It applies to applications that use either IAM or AWS IAM Identity Center authentication, because
OpenSearch UI authorizes `opensearch:ViewLoginPage` before a
user signs in, when the request is still anonymous.

###### To block login page access from outside an approved network

1. Confirm that your application is in an AWS account that is a member of your
   organization, and that resource control policies are enabled for your
   organization. For more information, see [Enabling a policy type](../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md "../../../organizations/latest/userguide/orgs_manage_policies_enable-disable.md") in the _AWS Organizations User
   Guide_.
2. Determine the approved network path that your users connect through, and choose
   the matching condition key. Use `aws:SourceVpce` for an
   interface VPC endpoint, `aws:SourceVpc` for a VPC, or
   `aws:SourceIp` for a range of public IP addresses, such
   as your corporate network's egress range.
3. Save a resource control policy that denies
   `opensearch:ViewLoginPage` and
   `opensearch:ApplicationAccessAll` unless the request
   matches your approved network to a local file named
   `policy.json`. The following example approves a single interface VPC
   endpoint. For the other condition keys, see [Network access control configuration reference for OpenSearch UI applications](application-network-access-reference.md "application-network-access-reference.md"). Replace the
   `placeholder value` with your own VPC endpoint
   ID.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyOpenSearchUIAccessOutsideVpce",
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "opensearch:ViewLoginPage",
                "opensearch:ApplicationAccessAll"
            ],
            "Resource": "arn:aws:opensearch:*:*:application/*",
            "Condition": {
                "StringNotEqualsIfExists": {
                    "aws:SourceVpce": "`vpc-endpoint-id`"
                }
            }
        }
    ]
}
```

4. Create the resource control policy. Run the following command from your
   organization's management account or from a delegated administrator
   account.

```
aws organizations create-policy \
  --name `DenyOpenSearchUIOffNetwork` \
  --description "`Denies OpenSearch UI access from outside the approved network`" \
  --type RESOURCE_CONTROL_POLICY \
  --content file://policy.json
```

The response includes the policy ID, which begins with
`p-`. Note this value for the next step. 5. Attach the policy to the organization root, an organizational unit, or the
account that contains the application. To limit the scope of your first change,
attach it to a single account and expand the scope after you verify the
behavior.

```
aws organizations attach-policy \
  --policy-id `p-example12345` \
  --target-id `111122223333`
```

6. Wait up to a minute for the policy to take effect.
7. From outside the approved network, request the application login page at
   `https://`application-endpoint`/_login/`. You
   receive a `403 forbidden` response instead of the login page.

###### Note

Request the `/_login/` path to confirm that the policy denies
the login page. If you open the application URL without a path, your browser
might be redirected to sign in before it requests the login page. In that
case, `opensearch:ApplicationAccessAll` denies
access after you sign in. 8. From inside the approved network, request the same URL. The login page renders
and you can sign in normally.

###### Note

For applications that use AWS IAM Identity Center authentication, restrict the network path that
users sign in through. OpenSearch UI evaluates
`opensearch:ViewLoginPage` before authentication for every
application, so denying it blocks off-network users from signing in. To also restrict
requests from IAM Identity Center users who already hold a valid session, have those users reach the
application through a VPC endpoint.

## Considerations

Keep the following in mind when you configure network access controls:

- **Choosing a control**. Use an
  identity-based policy to restrict a specific principal, a VPC endpoint policy to
  control which applications users can reach through an endpoint, and a resource
  control policy to enforce access across an entire organization. You can combine
  them for defense in depth.
- **Pre-authentication versus authenticated access**.
  Only `opensearch:ViewLoginPage`, enforced with an RCP, blocks
  off-network users before they sign in and applies uniformly to both IAM and
  AWS IAM Identity Center users. Conditions applied only to
  `opensearch:ApplicationAccessAll` restrict where an authenticated
  principal can access the application from.
- **Policy evaluation**. An explicit
  `Deny` always overrides an `Allow`. A resource control
  policy sets the maximum available permissions for resources in your organization,
  and an explicit `Deny` in an RCP cannot be overridden by an
  identity-based policy. Test your policy against a non-production application
  before applying it broadly.
- **Monitoring**. Use AWS CloudTrail and IAM
  Access Analyzer to review the effect of your network conditions on access.
