

# AWS PrivateLink for Access Portal
<a name="iam-id-center-privatelink"></a>

AWS IAM Identity Center (successor to AWS Single Sign-On) supports AWS PrivateLink, enabling you to access IAM Identity Center sign-in from within your Amazon VPC without traversing the public internet. You can configure a VPC endpoint for IAM Identity Center to keep workforce sign-in traffic on the AWS network, and configure network controls to require that sign-in requests originate from that VPC endpoint.

Use VPC endpoints and network controls for IAM Identity Center when you need:
+ Private connectivity for workforce sign-in to your AWS access portal from within your Amazon VPC or connected on-premises networks.
+ Network-level access controls for IAM Identity Center sign-in using VPC endpoint policies.
+ IAM Identity Center sign-in in network-isolated environments without public internet access.

**Note**  
IAM Identity Center sign-in shares the same VPC endpoint used for AWS Console Private Access. You stand up a single VPC endpoint for AWS sign-in and write one endpoint policy covering both sign-in paths. The policy differentiates between them by action namespace: `sso:*` for IAM Identity Center sign-in, and `signin:*` for IAM sign-in (root, IAM user, and federated sign-in using OAuth). For the IAM-side VPC endpoint policy reference, see [AWS PrivateLink](oauth-privatelink.md).

## Configuring a VPC endpoint for IAM Identity Center sign-in
<a name="iam-id-center-privatelink-configuring"></a>

IAM Identity Center sign-in supports operating in networks without access to the public internet. When you configure a VPC endpoint for IAM Identity Center, sign-in traffic between your applications and IAM Identity Center is routed through AWS PrivateLink. Internet connectivity is not required for sign-in itself.

Replace `region` with your own Region information.
+ **Classic partition**: create VPC endpoints for both `com.amazonaws.{{region}}.signin` and `com.amazonaws.{{region}}.signin-v2`. Interactive IAM Identity Center sign-in requires both endpoints.
+ **GovCloud partition**: create a VPC endpoint for `com.amazonaws.{{region}}.signin-v2` only. This endpoint serves both IPv4 and dual-stack sign-in traffic.

If you already have these VPC endpoints configured for AWS Console Private Access, you do not need to create additional endpoints. You add IAM Identity Center-specific statements to your existing VPC endpoint policy instead. For details on VPC endpoint creation, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon Virtual Private Cloud User Guide*.

## Implementing access controls
<a name="iam-id-center-privatelink-access-controls"></a>

You can use VPC endpoint policies to control IAM Identity Center instances permitted for enterprise users to sign in through your private network.

### Trusted identities
<a name="iam-id-center-privatelink-trusted-identities"></a>

IAM Identity Center sign-in actions use the `sso:*` action namespace on the shared sign-in endpoint. IAM Identity Center does not introduce new condition keys for this purpose. Instead, you scope access using the standard AWS resource context keys (`aws:ResourceOrgID`, `aws:ResourceAccount`) together with the `Resource` element of your policy statement, or by referencing your IAM Identity Center instance ARN directly.

**Important**  
The sign-in endpoint is shared with AWS Console Private Access. Do not write a policy that restricts access to only one service unless you intend to block the other. If you use both IAM Identity Center and Console Private Access, include policy statements for both.

#### Example: Allow IAM Identity Center sign-in for a specific instance
<a name="iam-id-center-privatelink-example-instance"></a>

```
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

#### Example: Allow both IAM Identity Center sign-in and IAM sign-in
<a name="iam-id-center-privatelink-example-org"></a>

This VPC endpoint policy allows both IAM Identity Center sign-in and IAM sign-in (Console Private Access) for identities in the same AWS Organizations.

```
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
                    "aws:ResourceOrgID": "o-xxxxxxxxxxx"
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
                    "aws:PrincipalOrgId": "o-xxxxxxxxxxx"
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
                    "aws:ResourceOrgID": "o-xxxxxxxxxxx"
                }
            }
        }
    ]
}
```

For the full IAM Identity Center VPC endpoint policy reference, including OIDC, the AWS access portal, administrative, and identity store endpoints, see [AWS PrivateLink for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/vpc-interface-endpoints.html) in the *IAM Identity Center User Guide*.

## Network controls for AWS access portal
<a name="iam-id-center-privatelink-network-controls"></a>

Network controls in IAM Identity Center let you require that all AWS access portal sign-in requests originate from your VPC endpoint. You configure network controls directly on your IAM Identity Center instance. This is separate from AWS Sign-In resource-based policies and resource control policies (RCPs), which do not currently support the AWS access portal. To enforce network controls organization-wide, use a service control policy (SCP) that denies `sso-admin:UpdateInstance` unless `sso:VpceAccessRequired` is `true`. For an SCP example, see [AWS PrivateLink for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/vpc-interface-endpoints.html) in the *IAM Identity Center User Guide*.

Use the `sso-admin update-instance` API with a `network-configuration` object to require VPC endpoint access for your instance.

```
aws sso-admin update-instance \
    --instance-arn {{arn:aws:sso:::instance/ssoins-1234567890abcdef}} \
    --network-configuration '{
        "VpceAccessRequired": true
    }'
```

When `VpceAccessRequired` is `true`, IAM Identity Center denies sign-in and application authorization requests that originate from outside your VPC endpoint. Depending on your IAM Identity Center instance type, IAM Identity Center allows only requests from VPC endpoints within your AWS account or organization. Set it to `false` (the default) to skip network control evaluation entirely, which allows access from both your VPC endpoint and public networks.

The `network-configuration` object also accepts the following fields:
+ `RestrictSourceVpcs` limits access to specific VPCs.
+ `AllowSourceIps` allows exceptions for public IP ranges.
+ `ExcludeApplicationArns` exempts specific applications from the requirement.

`UpdateInstance` replaces the object in full. If you omit a field, IAM Identity Center clears it rather than leaving it unchanged.

**Note**  
Network controls on your IAM Identity Center instance (`sso-admin update-instance`) are independent of network controls on your identity store resource (`identitystore update-identity-store`), which governs identity store API operations and SCIM provisioning separately, including its own `ScimAllowSourceIps` field. Setting one does not configure the other.

Two considerations apply when you enable network controls:
+ IAM Identity Center does not support AWS Managed Microsoft AD or a self-managed AD directory as an identity source when you use VPC endpoints.
+ IdP-initiated SAML sign-in requires either a relay state configured to route through the AWS access portal, or network access to `awsapps.com`, because IdP-initiated requests originate outside your VPC endpoint.

For complete details on network controls, including the full field reference, SCP enforcement, error handling, and considerations, see [AWS PrivateLink for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/vpc-interface-endpoints.html) in the *IAM Identity Center User Guide*.

## Related topics
<a name="iam-id-center-privatelink-related"></a>
+ [Login with IAM Identity Center credentials](command-line-sign-in.md#command-line-sign-in-sso)
+ [AWS PrivateLink](oauth-privatelink.md)
+ [Controlling console access with resource-based policies and resource control policies](console-access-control.md)
+ [AWS PrivateLink for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/vpc-interface-endpoints.html) in the *IAM Identity Center User Guide*