

# Controls for cross-partition identity federation
<a name="id_roles_providers_outbound_cross_partition_controls"></a>

Cross-partition identity federation involves three access decisions: who can request a token in the source account, which JWTs can be used to assume a role in the destination account, and what the resulting role session can access. [IAM](access_policies.md) and [AWS Organizations policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) govern these decisions. This page explains where each policy applies and provides examples for controlling access at each stage.

**Where to apply access controls**
+ [Control token requests in the source partition](#id_roles_providers_outbound_cross_partition_source_controls)
+ [Control access in the destination partition](#id_roles_providers_outbound_cross_partition_destination_controls)
  + [Who can assume a role](#cross-partition-destination-token-exchange)
  + [What role sessions can do](#cross-partition-destination-session-use)

## Control token requests in the source partition
<a name="id_roles_providers_outbound_cross_partition_source_controls"></a>

In the source account, [IAM identity-based policies](access_policies.md#policies_id-based) grant permission to call `sts:GetWebIdentityToken` and can restrict token audiences, lifetimes, and signing algorithms. Token requests that include tags also require the `sts:TagGetWebIdentityToken` permission. [Permissions boundaries](access_policies.md#policies_bound), [session policies](access_policies.md#policies_session), and applicable [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) can further restrict permission to request tokens. Requests made through an AWS STS VPC endpoint must also be allowed by its [endpoint policy](reference_sts_vpc_endpoint_policies.md).

For condition keys and policy examples that control token requests, see [Controlling access with IAM policies](id_roles_providers_outbound_policies.md).

**Note**  
Request the token with only the audience configured for your destination. `AssumeRoleWithWebIdentity` rejects tokens from `GetWebIdentityToken` that have more than one audience. See [Setting up cross-partition identity federation](id_roles_providers_outbound_cross_partition_setup.md).

## Control access in the destination partition
<a name="id_roles_providers_outbound_cross_partition_destination_controls"></a>

In the destination account, the role's trust policy controls which JWTs can be used to assume the role through `sts:AssumeRoleWithWebIdentity`. Applicable [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) can restrict role assumption across destination member accounts.

After role assumption, [identity-based policies](access_policies.md#policies_id-based) and [resource-based policies](access_policies.md#policies_resource-based) grant the session access to AWS services and resources. [Permissions boundaries](access_policies.md#policies_bound), [session policies](access_policies.md#policies_session), and applicable [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) and [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) can further restrict what the role session can access. Requests made through a service's VPC endpoint must also be allowed by its [endpoint policy](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).

### Who can assume a role
<a name="cross-partition-destination-token-exchange"></a>

<a name="cross-partition-destination-trust"></a>The following examples use the destination role's trust policy to allow a source role to assume it, and an RCP to allowlist trusted issuers or source partitions. For supported token claim condition keys, see the AWS STS tab under [Available keys for AWS OIDC federation](reference_policies_iam-condition-keys.md#condition-keys-wif).

**Example: Allow a source role to assume the destination role**

The destination role's trust policy allows the specified source role to assume it when the token has the expected audience and was issued in `us-east-1`. The source partition is `aws` and the destination partition is `aws-cn`. Replace the issuer host in the provider ARN and condition keys with your source account's issuer host, and replace `your-audience` with the audience configured for your destination OIDC provider. Replace `us-east-1` with the source AWS Region you want to allow.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws-cn:iam::{{111122223333}}:oidc-provider/{{a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws}}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "{{a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws}}:sub": "arn:aws:iam::{{123456789012}}:role/{{SourceWorkloadRole}}",
          "{{a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws}}:aud": "{{your-audience}}",
          "{{a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws}}:source_region": "{{us-east-1}}"
        }
      }
    }
  ]
}
```

**Note**  
The `sub` condition matches every session of `SourceWorkloadRole`. To limit access to a specific Amazon EC2 instance or Lambda function, use `{{issuer-host}}:ec2_source_instance_arn` or `{{issuer-host}}:lambda_source_function_arn`, respectively, when those claims are present. Use `{{issuer-host}}:org_id` to require a specific source organization.

<a name="cross-partition-destination-approved-issuers"></a>**Example: Allowlist trusted issuers with a resource control policy (RCP)**

The [aws:FederatedProvider](reference_policies_condition-keys.md#condition-keys-federatedprovider) condition key identifies the OIDC provider in the destination account. The issuer host in that provider's ARN identifies the source account.

The following RCP enforces an allowlist of approved source issuers for cross-partition role assumption. The `StringLike` condition scopes the deny to OIDC provider ARNs that match the AWS STS issuer pattern. Replace the example issuer host with your approved source issuer host.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceIssuerAllowlist",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:FederatedProvider": "arn:*:iam::*:oidc-provider/*.tokens.sts.*"
        },
        "StringNotLike": {
          "aws:FederatedProvider": [
            "arn:*:iam::*:oidc-provider/{{a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws}}"
          ]
        }
      }
    }
  ]
}
```

<a name="cross-partition-destination-approved-partitions"></a>**Example: Allowlist trusted source partitions with a resource control policy (RCP)**

To include all issuers from an approved source partition, match the issuer host suffix instead of an account-specific issuer host.


| Source partition | Issuer host suffix | 
| --- | --- | 
| aws | tokens.sts.global.api.aws | 
| aws-us-gov | tokens.sts.us-gov.api.aws | 
| aws-cn | tokens.sts.global.api.amazonwebservices.com.cn | 
| aws-eusc | tokens.sts.global.api.amazonwebservices.eu | 

The following RCP enforces an allowlist of approved source partitions for cross-partition role assumption. This example includes the `aws` partition in the allowlist. The `StringLike` condition scopes the deny to OIDC provider ARNs that match the AWS STS issuer pattern. The wildcard before the issuer host suffix matches every account's issuer in the approved partition. Add an ARN pattern for each approved source partition.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceSourcePartitionAllowlist",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:FederatedProvider": "arn:*:iam::*:oidc-provider/*.tokens.sts.*"
        },
        "StringNotLike": {
          "aws:FederatedProvider": [
            "arn:*:iam::*:oidc-provider/*.tokens.sts.global.api.aws"
          ]
        }
      }
    }
  ]
}
```

### What role sessions can do
<a name="cross-partition-destination-session-use"></a>

The following examples use an SCP to block requests by source issuer and an RCP to block Amazon S3 access by source AWS Region. After a policy change propagates, these denies apply to matching requests from new and existing role sessions, including sessions whose temporary credentials haven't expired. For the condition keys used in these examples, see [aws:FederatedProvider](reference_policies_condition-keys.md#condition-keys-federatedprovider) and [aws:CrossPartitionSourceRegion](reference_policies_condition-keys.md#condition-keys-crosspartitionsourceregion).

<a name="cross-partition-destination-session-permissions"></a>**Example: Block requests by source issuer with an SCP**

This SCP denies requests from destination role sessions that federated through the specified source issuer. It applies to destination roles in member accounts covered by the SCP. The example uses destination accounts in the `aws-cn` partition. Replace the example issuer host with the source issuer host you want to block.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenySessionsFromSourceIssuer",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:FederatedProvider": "arn:aws-cn:iam::*:oidc-provider/{{a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws}}"
        }
      }
    }
  ]
}
```

<a name="cross-partition-destination-session-rcp"></a>**Example: Block Amazon S3 access by source Region with an RCP**

This RCP denies access to Amazon S3 resources in your AWS organization's member accounts covered by the policy when a request uses a cross-partition federated session whose source token was issued in `us-east-1`. Replace `us-east-1` with the source AWS Region you want to block. Both SCPs and RCPs support the `aws:FederatedProvider` and `aws:CrossPartitionSourceRegion` condition keys.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyS3AccessFromSourceRegion",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:CrossPartitionSourceRegion": "{{us-east-1}}"
        }
      }
    }
  ]
}
```