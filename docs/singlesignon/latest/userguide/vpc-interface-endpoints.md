

# AWS PrivateLink for IAM Identity Center

You can establish a private connection between your VPC and AWS IAM Identity Center by creating an *interface VPC endpoint*. Interface endpoints are powered by AWS PrivateLink. For more information, see [AWS PrivateLink](https://aws.amazon.com/privatelink) on the AWS website. You can use this technology to privately access IAM Identity Center APIs without an internet gateway, NAT device, VPN connection, or connection. Resources in your VPC do not need public IP addresses to communicate with IAM Identity Center APIs. Traffic between your VPC and IAM Identity Center does not leave the AWS network.

IAM Identity Center supports the following interface VPC endpoints for administrative operations and workforce identity access to the AWS access portal, connected SaaS applications, and AWS accounts.


| Purpose | Service name | Description | 
| --- | --- | --- | 
| SSO Admin | com.amazonaws.{{region}}.sso | Supports administrative operations such as managing IAM Identity Center instances, applications, permission sets, and assignments. | 
| Identity Store | com.amazonaws.{{region}}.identitystore | Supports user and group management and identity lookup operations in the identity store. | 
| Sign-in | com.amazonaws.{{region}}.signin | Classic partition only: Workforce sign-in to IAM Identity Center (interactive, browser-based). This is the same endpoint used for AWS Console Private Access. | 
| Sign-in (dual-stack) | com.amazonaws.{{region}}.signin-v2 |  Classic partition: Workforce sign-in to IAM Identity Center (dual-stack). Required alongside the signin endpoint for interactive sign-in flows. GovCloud partition: Workforce sign-in to IAM Identity Center (IPv4 and dual-stack endpoints).  | 
| OIDC | com.amazonaws.{{region}}.sso-oauth | Supports OAuth 2.0 based authentication and token creation for IAM Identity Center integrated applications and tools (such as the AWS CLI). | 
| AWS access portal website | com.amazonaws.{{region}}.sso.portal.app | Supports loading static assets for the AWS access portal website. | 
| AWS access portal backend | com.amazonaws.{{region}}.sso.portal | Supports enumerating AWS accounts and generating IAM credentials for programmatic account access. Also supports backend APIs for the AWS access portal. | 

Each interface VPC endpoint is represented by one or more [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *Amazon Virtual Private Cloud User Guide*.

**Note**  
IAM Identity Center network controls cover workforce sign-in, application authorization, the AWS access portal, and administrative APIs. Network controls for SCIM provisioning from your identity provider are managed separately through IP address restrictions configured on your identity store resource, not on your IAM Identity Center instance. SCIM provisioning does not use a VPC endpoint. For more information, see [Network controls for SCIM provisioning](#vpc-network-controls-scim).

## VPC endpoints for IAM Identity Center
<a name="vpc-interface-endpoints-setup"></a>

### Service names for IAM Identity Center interface VPC endpoints
<a name="vpc-interface-endpoints-create"></a>

To create interface VPC endpoints for IAM Identity Center, use the Amazon VPC console, the AWS CLI, or the AWS SDK with the service names listed in the preceding table. For step-by-step instructions, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon Virtual Private Cloud User Guide*.

Create a VPC endpoint for the SSO Admin service name for administrative operations. Create a VPC endpoint for the Identity Store service name for administrative operations and for applications that look up user or group identity information. Create VPC endpoints for the Sign-in, OIDC, Portal website, and Portal backend service names to establish private connectivity for IAM Identity Center workforce access.

### VPC endpoint policies for IAM Identity Center
<a name="vpc-interface-endpoints-policies"></a>

You can attach endpoint policies to your interface VPC endpoints to restrict access to known IAM Identity Center instances from your private network as well as which identities can access known instances where applicable. An endpoint policy specifies the principals, actions, resources, and conditions for access. 

If you do not attach a policy to your endpoint, the default policy allows full access to the service through the endpoint. For more information, see [Control access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon Virtual Private Cloud User Guide*. 

#### Condition keys for VPC endpoint policies
<a name="vpc-endpoint-policy-context-keys"></a>

IAM Identity Center does not introduce new condition keys for its own endpoints (`sso`, `identitystore`, `sso-oauth`). Instead, you restrict access using the standard AWS resource and principal context keys together with the `Resource` element of your policy statement, which you can scope to a specific IAM Identity Center instance or application.


| Condition keys | Description | 
| --- | --- | 
| aws:ResourceAccount | The AWS account ID that owns the resource named in the policy's Resource element. | 
| aws:ResourceOrgID | The AWS Organizations ID that owns the resource named in the policy's Resource element (for example, the IAM Identity Center instance). | 

To scope a policy to a specific IAM Identity Center instance without a condition key, reference the instance ARN directly in the `Resource` element:

```JSON
"Resource": "arn:aws:sso:::instance/ssoins-{{1234567890abcdef}}"
```

For OIDC operations, reference the application and OAuth client resources:

```JSON
"Resource": [
    "arn:aws:sso::{{111122223333}}:application/ssoins-{{1234567890abcdef}}/*",
    "arn:aws:sso::{{111122223333}}:oauthClient/ssoins-{{1234567890abcdef}}/*"
]
```

For IAM SigV4 requests, the standard IAM condition keys (`aws:PrincipalOrgId`, `aws:PrincipalAccount`) are also available for restricting access by principal.

**Note**  
The AWS access portal and AWS managed applications that integrate with IAM Identity Center use a separate set of context keys with the `aws:IdentityCenter` prefix (for example, `aws:IdentityCenterInstanceArn`) in their own VPC endpoint policies. These keys are distinct from the resource context keys described in this section, which apply only to IAM Identity Center endpoints. For more information, see [VPC endpoint policies on the AWS access portal and AWS managed applications](#vpc-endpoint-policy-1p-apps).

#### SSO Admin endpoint (`sso`)
<a name="vpc-endpoint-policy-sso-admin"></a>

The SSO Admin endpoint (`com.amazonaws.{{region}}.sso`) handles administrative operations for IAM Identity Center, such as managing instances, permission sets, and account assignments. This endpoint supports IAM SigV4 requests only.

The following example restricts administrative access to a specific IAM Identity Center instance.

**Example Restrict SSO Admin access to a specific IAM Identity Center instance**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAdminForInstance",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sso:*",
            "Resource": "arn:aws:sso:::instance/ssoins-{{1234567890abcdef}}"
        }
    ]
}
```

To restrict administrative access to any instance in your organization instead of a single instance, use the `aws:ResourceOrgID` condition key.

**Example Restrict SSO Admin access to instances in the same organization**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAdminSameOrg",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sso:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-{{xxxxxxxxxxx}}"
                }
            }
        }
    ]
}
```

#### Identity Store endpoint (`identitystore`)
<a name="vpc-endpoint-policy-identity-store"></a>

The Identity Store endpoint (`com.amazonaws.{{region}}.identitystore`) handles user and group management operations in the identity store, and identity lookups performed by applications that need to resolve user or group information. This endpoint supports IAM SigV4 requests only.

The following example restricts Identity Store access to a specific identity store. Because the service authorizes the store resource and the user, group, and membership resources separately, the policy must allow each resource the caller needs.

**Example Restrict Identity Store access to a specific identity store**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowIdentityStoreForStore",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "identitystore:*",
            "Resource": [
                "arn:aws:identitystore::{{111122223333}}:identitystore/d-{{1234567890}}",
                "arn:aws:identitystore:::user/*",
                "arn:aws:identitystore:::group/*",
                "arn:aws:identitystore:::membership/*"
            ]
        }
    ]
}
```

To restrict access to any identity store in your organization instead of a single store, use the `aws:ResourceOrgID` condition key.

**Example Restrict Identity Store access to identity stores in the same organization**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowIdentityStoreSameOrg",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "identitystore:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-{{xxxxxxxxxxx}}"
                }
            }
        }
    ]
}
```

The Identity Store also has its own network configuration, separate from the VPC endpoint policy for the Identity Store endpoint described earlier in this section and separate from your IAM Identity Center instance's network controls. Use the `identitystore update-identity-store` API to require VPC endpoint access for the identity store's own API operations, restrict access to specific VPCs, or allow IP address exceptions for SCIM provisioning traffic. For details, see [Network controls for SCIM provisioning](#vpc-network-controls-scim).

#### Sign-in endpoint (`signin`)
<a name="vpc-endpoint-policy-signin"></a>

**Classic partition**: The sign-in endpoint (`com.amazonaws.{{region}}.signin`) is shared between IAM Identity Center and AWS Console Private Access. Interactive sign-in also requires the dual-stack endpoint (`com.amazonaws.{{region}}.signin-v2`).

**GovCloud partition**: The sign-in endpoint (`com.amazonaws.{{region}}.signin-v2`) is shared between IAM Identity Center and AWS Console Private Access. Both IAM and IAM Identity Center sign-in actions are evaluated under the same VPC endpoint policy on these endpoints. IAM Identity Center sign-in actions authenticate workforce identities during sign-in to IAM Identity Center.

When you already use this endpoint for Console Private Access, you add IAM Identity Center-specific statements to your existing VPC endpoint policy. IAM Identity Center sign-in actions use the `sso:*` namespace.

**Important**  
The sign-in endpoint is shared with AWS Console Private Access. Do not write a policy that restricts access to only one service unless you intend to block the other. If you use both IAM Identity Center and Console Private Access, include policy statements for both.

The following example allows IAM Identity Center sign-in for the same IAM Identity Center instance as the VPC endpoint, scoped by the instance ARN in the `Resource` element.

**Example Allow IAM Identity Center sign-in for a specific IAM Identity Center instance**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowIdCSignIn",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sso:*",
            "Resource": "arn:aws:sso:::instance/ssoins-{{1234567890abcdef}}"
        }
    ]
}
```

To restrict IAM Identity Center sign-in to any instance in your organization instead of a single instance, use the `aws:ResourceOrgID` condition key.

**Example Allow IAM Identity Center sign-in for instances in the same organization**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IdCSignInOrgRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sso:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-{{xxxxxxxxxxx}}"
                }
            }
        }
    ]
}
```

The following example allows both IAM Identity Center sign-in and IAM sign-in (Console Private Access) for identities in the same AWS Organizations. IAM sign-in is split into a pre-authentication statement (`signin:Authenticate`), scoped by `aws:ResourceOrgID`, and a post-authentication statement (`signin:AuthorizeOAuth2Access`, `signin:CreateOAuth2Token`), scoped by `aws:PrincipalOrgId`.

**Example Allow IAM Identity Center sign-in and IAM sign-in**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PreAuthIAMSignInOrgRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "signin:Authenticate",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-{{xxxxxxxxxxx}}"
                }
            }
        },
        {
            "Sid": "PostAuthIAMSignInOrgRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "signin:AuthorizeOAuth2Access",
                "signin:CreateOAuth2Token"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgId": "o-{{xxxxxxxxxxx}}"
                }
            }
        },
        {
            "Sid": "IdCSignInOrgRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sso:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-{{xxxxxxxxxxx}}"
                }
            }
        }
    ]
}
```

For more information about configuring VPC endpoint policies for the sign-in endpoint, including the pre-authentication and post-authentication phases, see [AWS PrivateLink](https://docs.aws.amazon.com/signin/latest/userguide/oauth-privatelink.html) in the *AWS Sign-In User Guide*.

#### OIDC endpoint (`sso-oauth`)
<a name="vpc-endpoint-policy-oidc"></a>

The OIDC endpoint (`com.amazonaws.{{region}}.sso-oauth`) handles token creation and introspection for both IAM SigV4 and IAM Identity Center bearer token operations. Configure a VPC endpoint policy to restrict which identities can perform these operations through your endpoint.

OIDC resources are represented by the `application` resource type, for confidential clients such as customer managed applications, and the `oauthClient` resource type, for public clients such as the AWS CLI. The following example policy allows access only for OIDC resources that belong to your AWS Organizations.

**Example Allow access to OIDC resources in the same organization**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IdCOIDCOrgRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": [
                "arn:aws:sso::{{111122223333}}:application/ssoins-{{1234567890abcdef}}/*",
                "arn:aws:sso::{{111122223333}}:oauthClient/ssoins-{{1234567890abcdef}}/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-{{xxxxxxxxxxx}}"
                }
            }
        }
    ]
}
```

The following example scopes access to a single IAM Identity Center instance by referencing its OIDC resources directly in the `Resource` element, without a condition key.

**Example Allow access to OIDC resources for a specific IAM Identity Center instance**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IdCOIDCInstanceRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": [
                "arn:aws:sso::{{111122223333}}:application/ssoins-{{1234567890abcdef}}/*",
                "arn:aws:sso::{{111122223333}}:oauthClient/ssoins-{{1234567890abcdef}}/*"
            ]
        }
    ]
}
```

**Note**  
The `CreateToken` operation (device code flow) uses bearer token authorization and does not carry IAM credentials. Principal-based conditions such as `aws:PrincipalOrgId` do not restrict these requests. Use the resource context keys (`aws:ResourceOrgID`, `aws:ResourceAccount`) or a scoped `Resource` element to restrict bearer token operations.

**Note**  
The preceding organization example uses `aws:ResourceOrgID`, which works for organization instances of IAM Identity Center. For account instances that are not part of an organization, use `aws:ResourceAccount` with the AWS account ID that owns the instance.

**Example Allow access to OIDC resources for an account-level instance**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IdCOIDCAccountRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": [
                "arn:aws:sso::{{111122223333}}:application/ssoins-{{1234567890abcdef}}/*",
                "arn:aws:sso::{{111122223333}}:oauthClient/ssoins-{{1234567890abcdef}}/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

#### AWS access portal endpoints
<a name="vpc-endpoint-policy-portal"></a>

The AWS access portal requires two VPC endpoints:
+ **Portal website** (`com.amazonaws.{{region}}.sso.portal.app`) – Serves static assets for the AWS access portal website. This endpoint does not support a VPC endpoint policy because it serves static content only.
+ **Portal backend** (`com.amazonaws.{{region}}.sso.portal`) – Handles API requests for the AWS access portal. This endpoint supports bearer token operations only. The AWS access portal uses the same `aws:IdentityCenter`-prefixed context keys as AWS managed applications to restrict access. For the full list of keys, see [VPC endpoint policies on the AWS access portal and AWS managed applications](#vpc-endpoint-policy-1p-apps).

The following example restricts portal backend access to identities from a specific IAM Identity Center instance.

**Example Restrict portal backend access to a specific IAM Identity Center instance**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPortalForInstance",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:IdentityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-{{1234567890abcdef}}"
                }
            }
        }
    ]
}
```

#### VPC endpoint policies on the AWS access portal and AWS managed applications
<a name="vpc-endpoint-policy-1p-apps"></a>

The AWS access portal and AWS managed applications that integrate with IAM Identity Center (such as Amazon Q, AWS IoT SiteWise, and Amazon Redshift Query Editor V2) share a common set of authorization context keys for VPC endpoint policies. When these applications and the AWS access portal validate IAM Identity Center tokens, they receive context keys that you can use in VPC endpoint policies on their respective endpoints.

These context keys use the `aws:IdentityCenter` prefix. IAM Identity Center's own endpoints (`sso`, `identitystore`, `sso-oauth`) do not use these keys — those endpoints use standard AWS resource context keys instead. For more information, see [Condition keys for VPC endpoint policies](#vpc-endpoint-policy-context-keys).


| Context key | Type | Description | 
| --- | --- | --- | 
| aws:IdentityCenterInstanceArn | String | The ARN of the IAM Identity Center instance connected to the bearer token. | 
| aws:IdentityStoreArn | String | The ARN of the identity store associated with the IAM Identity Center instance. | 
| aws:IdentityCenterSessionId | String | The session identifier for the current IAM Identity Center session. | 

These keys are returned to AWS managed applications when they validate IAM Identity Center tokens. Applications populate these keys into their authorization context for VPC endpoint policy evaluation.

**Example Allow access on a managed application endpoint for identities from a specific IAM Identity Center instance**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "IdCInstanceRestriction",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "service:DataAPI",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:IdentityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-{{1234567890abcdef}}"
                }
            }
        }
    ]
}
```

**Note**  
For information about using these context keys on a specific AWS managed application, see that application's VPC endpoint documentation.

## Network controls for IAM Identity Center
<a name="vpc-network-controls"></a>

Network controls let you require that all sign-in and application authorization requests for your IAM Identity Center instance originate from your VPC endpoints. You can enforce that requirement organization-wide with a service control policy.

### Requiring VPC endpoint access for IAM Identity Center
<a name="vpc-network-controls-require"></a>

You can configure your IAM Identity Center instance to require that all sign-in and application authorization requests originate from your VPC endpoints. When you enable this setting, IAM Identity Center denies requests to your IAM Identity Center instance from outside your VPC endpoints. Depending on your IAM Identity Center instance type, IAM Identity Center allows only requests from VPC endpoints within your AWS account (account instance) or your AWS Organizations (organization instance).

Use the `sso-admin update-instance` API to set the network access requirement. You configure network controls by passing a `network-configuration` object. You can't set network controls at instance creation time, only through `UpdateInstance` on an existing instance.

```bash
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{"VpceAccessRequired": true}'
```

When `VpceAccessRequired` is set to `true`:
+ All sign-in and authorization requests must originate from a VPC endpoint in your AWS account or AWS Organizations, depending on your IAM Identity Center instance type.
+ IAM Identity Center enforces network controls during token creation, verification, and revocation.
+ Network controls automatically bypass AWS managed applications that receive requests from other AWS services (service-to-service calls). Network controls evaluate only requests that originate from a customer's network.
+ You can optionally restrict access to specific VPCs, allow exceptions for public IP ranges, or exclude specific applications from the requirement.

The `network-configuration` object also accepts the following fields:
+ `RestrictSourceVpcs` – A list of VPC Amazon Resource Names (ARNs). When set, requests must originate from one of the listed VPCs. If `VpceAccessRequired` is also `true`, requests must additionally come through a VPC endpoint. If you don't specify this field, requests from any VPC endpoint in your AWS account or AWS Organizations are allowed.
+ `AllowSourceIps` – A list of IPv4 or IPv6 CIDR ranges that bypass the VPC endpoint and VPC restrictions. A request from an IP address in this list is permitted even if it doesn't come through a VPC endpoint or one of the VPCs in `RestrictSourceVpcs`.
+ `ExcludeApplicationArns` – A list of application ARNs whose OAuth token operations skip network control evaluation. User sign-in is still evaluated. For details and examples, see [Excluding OAuth applications from network controls](#vpc-network-controls-exclusions).

```bash
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{
        "VpceAccessRequired": true,
        "RestrictSourceVpcs": ["{{arn:aws:ec2:us-east-1:111122223333:vpc/vpc-0a1b2c3d4e5f67890}}"],
        "AllowSourceIps": ["{{203.0.113.0/24}}"],
        "ExcludeApplicationArns": ["{{arn:aws:sso::111122223333:application/ssoins-1234567890abcdef/apl-1234567890abcdef}}"]
    }'
```

You can set `VpceAccessRequired` to `false` to allow access from both VPC endpoints and public networks. When set to `false` (the default), network control evaluation is completely skipped — requests are not checked against the network control policy regardless of their origin.

To remove all network restrictions, set `VpceAccessRequired` to `false` and omit `RestrictSourceVpcs`, `AllowSourceIps`, and `ExcludeApplicationArns`. Because `UpdateInstance` performs a full replacement, omitting these fields clears them.

```bash
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{"VpceAccessRequired": false}'
```

**Important**  
`UpdateInstance` replaces the `network-configuration` object in full. `UpdateInstance` clears any field you omit from the object, or that you include as an empty list, instead of leaving it unchanged. To change a single field, include the complete `network-configuration` object with all the values you want to keep, not just the field you're changing.

A single `UpdateInstance` request can specify only one of `EncryptionConfiguration`, `PermissionSetsEnabled`, or `network-configuration`. A request that specifies more than one of these returns a `ValidationException`. To perform more than one of these updates, call `UpdateInstance` separately for each; the calls can be made in parallel.

### Excluding OAuth applications from network controls
<a name="vpc-network-controls-exclusions"></a>

Use `ExcludeApplicationArns` when IAM Identity Center integrated AWS services and applications must create, verify, refresh, or revoke OAuth credentials from outside your VPC endpoints. Exclusion applies only to the OAuth requests that the application makes with its OAuth client:

Skipped for excluded applications  
Requests to create, verify, refresh, or revoke OAuth credentials.

Still enforced  
User sign-in to IAM Identity Center and requests to the AWS access portal. When a user signs in to use an excluded application, the sign-in request must still originate from your VPC endpoints, from one of your `RestrictSourceVpcs`, or from an IP address in `AllowSourceIps`.

**Note**  
`ExcludeApplicationArns` doesn't apply to SAML applications. A SAML application doesn't call IAM Identity Center directly. The user's browser gets the SAML assertion from the AWS access portal and sends it to the application, so IAM Identity Center evaluates these requests as user sign-in and AWS access portal requests, which are always subject to network controls.

Which ARN you add to `ExcludeApplicationArns` depends on the type of client:


| Client type | ARN to exclude | Notes | 
| --- | --- | --- | 
| AWS managed application | The application's resource ARN in its own AWS service, for example arn:aws:qbusiness:{{aa-example-1}}:{{111122223333}}:application/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}} | Do not use the IAM Identity Center application ARN for an AWS managed application. It does not match. | 
| Customer managed application (custom OAuth application) | The IAM Identity Center application ARN, for example arn:aws:sso::{{111122223333}}:application/ssoins-{{1234567890abcdef}}/apl-{{1234567890abcdef}} | Applies to the application's confidential OAuth client, including CreateTokenWithIAM calls for trusted identity propagation. | 
| Public client (for example, the AWS CLI or an AWS SDK) | The OAuth client ARN in the AWS account that owns your IAM Identity Center instance, for example arn:aws:sso::{{111122223333}}:oauthClient/ssoins-{{1234567890abcdef}}/\* | A public client gets a new client ID each time it registers, so use \* as the client ID. This excludes all public clients for the instance. | 

**Example Exclude AWS managed OAuth applications**  
The following AWS CLI command excludes one Amazon Q application by its resource ARN, and all Amazon Q applications in another account by using wildcards in the Region and resource segments.  

```bash
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{
        "VpceAccessRequired": true,
        "ExcludeApplicationArns": [
            "{{arn:aws:qbusiness:aa-example-1:111122223333:application/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}",
            "{{arn:aws:qbusiness:*:444455556666:*}}"
        ]
    }'
```

**Example Exclude a customer managed OAuth application**  
The following AWS CLI command requires VPC endpoint access for your IAM Identity Center instance and excludes a customer managed application. The application can create tokens from its own network. Users who sign in to the application must still sign in through allowed VPC endpoints.  

```bash
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{
        "VpceAccessRequired": true,
        "ExcludeApplicationArns": [
            "{{arn:aws:sso::111122223333:application/ssoins-1234567890abcdef/apl-1234567890abcdef}}"
        ]
    }'
```

**Example Exclude public OAuth clients**  
The following AWS CLI command excludes all public clients for your IAM Identity Center instance, such as the AWS CLI and AWS SDKs. They can create and refresh tokens from outside your VPC endpoints. Users must still sign in through your VPC endpoints to authorize a device or an authorization code request.  

```bash
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{
        "VpceAccessRequired": true,
        "ExcludeApplicationArns": [
            "{{arn:aws:sso::111122223333:oauthClient/ssoins-1234567890abcdef/*}}"
        ]
    }'
```
To allow public clients only from a known network instead, add that network's public IP address range to `AllowSourceIps`. This allows all IAM Identity Center requests from that range, including user sign-in.

### Network control access denied errors
<a name="vpc-network-controls-errors"></a>

When network controls deny a request, IAM Identity Center returns an `AccessDeniedException` with the reason `NETWORK_CONTROLS_ACCESS_DENIED`. Common causes include:
+ The request did not originate from a VPC endpoint in your AWS account or AWS Organizations.
+ The VPC endpoint is not in the same AWS account (account instance) or AWS Organizations (organization instance) as the IAM Identity Center instance.
+ If you enable network controls before an AWS managed application that you use has integrated network context forwarding for this IAM Identity Center instance, requests through that application are denied.

IAM Identity Center also rejects an `UpdateInstance` request with a `ValidationException` in the following cases:
+ The new network configuration would block the request that is making the change. To prevent lockout, call `UpdateInstance` through one of your VPC endpoints or from an IP address that you include in `AllowSourceIps`.

  ```
  Provided network configuration did not pass lockout prevention check. Adjust
  your request so it does not block the access you need to make future changes.
  ```
+ You call `UpdateInstance` in a Region other than the primary Region of your IAM Identity Center instance. Configure network controls in the primary Region. IAM Identity Center replicates the configuration to your other Regions.

  ```
  This operation is supported only in the primary Region of the IAM Identity
  Center instance.
  ```

### Network configuration size limit
<a name="vpc-network-controls-size-limit"></a>

IAM Identity Center limits the combined size of your network configuration. If your `RestrictSourceVpcs`, `AllowSourceIps`, or `ExcludeApplicationArns` values are too numerous or too long, `UpdateInstance` fails with a `ValidationException`:

```
The provided network configuration cannot be applied because the resulting
configuration exceeds the supported size. Reduce the number of entries in
ExcludeApplicationArns, RestrictSourceVpcs and AllowSourceIps, or use shorter
application ARNs.
```

To resolve this error, reduce the number of entries or their length in the parameters listed in the error message, then retry the request.

### Enforcing network controls with service control policies
<a name="vpc-network-controls-scp"></a>

To prevent member accounts from disabling VPC endpoint access requirements, use a service control policy (SCP) with the `sso:VpceAccessRequired` condition key. This key is available on `sso:UpdateInstance` and reflects the network configuration that results from the request.

The following example SCP denies changes to the instance unless VPC endpoint access is set to `true`.

**Example Require VPC endpoint access for all IAM Identity Center instances**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceVpceAccess",
            "Effect": "Deny",
            "Action": "sso:UpdateInstance",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "sso:VpceAccessRequired": "false"
                }
            }
        }
    ]
}
```

### Network controls for SCIM provisioning
<a name="vpc-network-controls-scim"></a>

SCIM provisioning from your identity provider (such as Microsoft Entra ID, Okta, or PingOne) uses IP address restrictions rather than VPC endpoints. Because SCIM requests originate from your identity provider's infrastructure, which is outside of your VPC, you configure network controls for SCIM separately from sign-in network controls.

SCIM provisioning traffic goes to your identity store resource, not to your IAM Identity Center instance. The identity store's network configuration accepts `VpceAccessRequired`, `ApiRestrictSourceVpcs`, `ApiAllowSourceIps`, and `ScimAllowSourceIps`. `ApiAllowSourceIps` and `ScimAllowSourceIps` each accept IPv4 or IPv6 CIDR ranges. A single `VpceAccessRequired` flag covers both identity store API calls and SCIM provisioning, so there is no way to restrict SCIM by IP address without also requiring VPC endpoint access (or an `ApiAllowSourceIps` exception) for identity store API calls.

**Note**  
`ApiRestrictSourceVpcs` takes a list of VPC Amazon Resource Names (ARNs) (for example, `arn:aws:ec2:{{us-east-1}}:{{111122223333}}:vpc/vpc-{{0a1b2c3d4e5f67890}}`), the same shape as the IAM Identity Center instance's `RestrictSourceVpcs` field.

`ScimAllowSourceIps` is an exception to the identity store's network perimeter, the same way `ApiAllowSourceIps` is. When `VpceAccessRequired` is `true`, SCIM provisioning is already restricted; the IP ranges you add to `ScimAllowSourceIps` are what let your identity provider back in. If `ScimAllowSourceIps` is empty while `VpceAccessRequired` is `true`, all SCIM provisioning is blocked, because SCIM traffic from your identity provider cannot come through a VPC endpoint. Add your identity provider's published SCIM IP ranges to `ScimAllowSourceIps` at the same time you enable the identity store perimeter, or use `0.0.0.0/0` to leave SCIM open, or provisioning stops.

**Important**  
`UpdateIdentityStore` replaces the `NetworkConfiguration` object in full. Any field you omit is cleared, not left unchanged. An empty list is not accepted as a value — to clear a list field, omit it rather than setting it to `[]`.

```bash
aws identitystore update-identity-store \
    --identity-store-id {{d-1234567890}} \
    --network-configuration '{
        "VpceAccessRequired": true,
        "ApiRestrictSourceVpcs": ["{{arn:aws:ec2:us-east-1:111122223333:vpc/vpc-0a1b2c3d4e5f67890}}"],
        "ApiAllowSourceIps": ["{{203.0.113.0/24}}"],
        "ScimAllowSourceIps": ["{{0.0.0.0/0}}"]
    }'
```

**Important**  
`UpdateIdentityStore` has the same lockout prevention as `UpdateInstance`. If the new network configuration would block the request that is making the change, IAM Identity Center rejects it with a `ValidationException`. To avoid lockout, call `UpdateIdentityStore` through the identity store's VPC endpoint, or include the caller's IP address in `ApiAllowSourceIps`.

To remove all network restrictions from the identity store, set `VpceAccessRequired` to `false` and omit `ApiRestrictSourceVpcs`, `ApiAllowSourceIps`, and `ScimAllowSourceIps`. Because the update performs a full replacement, omitting these fields clears them.

```bash
aws identitystore update-identity-store \
    --identity-store-id {{d-1234567890}} \
    --network-configuration '{"VpceAccessRequired": false}'
```

**Note**  
Consult your identity provider's documentation for their published SCIM IP address ranges. For example, Microsoft Entra ID publishes IP ranges for the AzureActiveDirectory service tag.

To prevent member accounts from disabling VPC endpoint access for the identity store, use a service control policy (SCP) with the `identitystore:VpceAccessRequired` condition key. This key is available on `identitystore:UpdateIdentityStore` and reflects the network configuration that results from the request.

**Example Require VPC endpoint access for all identity stores**  

```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnforceIdentityStoreVpceAccess",
            "Effect": "Deny",
            "Action": "identitystore:UpdateIdentityStore",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "identitystore:VpceAccessRequired": "false"
                }
            }
        }
    ]
}
```

## Considerations for IAM Identity Center interface endpoints
<a name="vpc-interface-endpoints-considerations"></a>

Before you set up interface VPC endpoints for IAM Identity Center, review the following considerations:
+ With IAM Identity Center VPC endpoints, you can cover administrative operations, workforce sign-in, application authorization, and the AWS access portal, as described in [VPC endpoints for IAM Identity Center](#vpc-interface-endpoints-setup). Other IAM Identity Center traffic, such as SCIM provisioning from your identity provider, requires public endpoint access or IP-based restrictions.
+ VPC endpoints for IAM Identity Center do not support [cross-account access](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html#interface-endpoint-cross-account).
+ Most IAM Identity Center VPC endpoints support both IPv4 and dual-stack (IPv4 and IPv6) traffic. In the classic partition, the `signin` endpoint supports IPv4 only, so interactive sign-in also requires the dual-stack `signin-v2` endpoint.
+ IAM Identity Center does not support AWS Managed Microsoft AD or a self-managed directory in Active Directory (AD) as an identity source when you use VPC endpoints for IAM Identity Center. If your identity source is Active Directory, use an external identity provider or the IAM Identity Center identity store instead.
+ The sign-in endpoints (`com.amazonaws.{{region}}.signin` and `com.amazonaws.{{region}}.signin-v2`) are shared with AWS Console Private Access. If you already have these endpoints configured for Console Private Access, you add IAM Identity Center-specific policy statements to the same endpoints rather than creating additional ones.
+ If you use an external identity provider and rely on identity provider-initiated (IdP-initiated) sign-in, requests originate outside your VPC endpoint. To support IdP-initiated sign-in with network controls enabled, update your identity provider's SAML configuration to send the request through the AWS access portal relay state, or allow network access to `awsapps.com`.
+ Bearer token operations (such as `CreateToken` in the device code flow) do not carry IAM credentials. Principal-based conditions such as `aws:PrincipalOrgId` do not restrict these requests. Use resource context keys (`aws:ResourceOrgID`, `aws:ResourceAccount`) or a scoped `Resource` element instead.
+ Public clients, such as the AWS CLI and AWS SDKs, are subject to network controls unless you exclude them with `ExcludeApplicationArns`.
+ The AWS access portal website endpoint (`com.amazonaws.{{region}}.sso.portal.app`) serves static assets only. It does not support VPC endpoint policies and is not subject to network control enforcement. The AWS access portal backend endpoint (`com.amazonaws.{{region}}.sso.portal`) supports VPC endpoint policies and is subject to network controls for bearer token operations.
+ When a user changes networks (for example, disconnects from VPN), the AWS access portal synchronously re-evaluates network controls on the next request. Because this evaluation happens synchronously, the first request after a network change might take slightly longer to complete.
+ If you enable network controls before an AWS managed application has integrated network context forwarding, requests through that application are denied. Verify that your managed applications support network controls before you set `VpceAccessRequired` to `true`.