

# Control TIP for IAM federation with IAM policies

This page explains the permissions and AWS Organizations guardrails that apply when you configure and use TIP with IAM SAML or OpenID Connect (OIDC) federation.

For IAM federation context-key definitions, see [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md). For CloudTrail event fields, request paths, recipient accounts, safeguards, and TIP logging examples, see [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md). For configuration procedures, see [Configure TIP for an IAM identity provider](id_roles_providers_tip_federation_configure.md).

## Understand how policies apply to TIP
<a name="id_roles_providers_tip_federation_policies_understand_how_policies_apply_to_tip"></a>

Policies can control TIP at three points. The following table shows what each control point governs and the policy mechanism that applies.


| Control point | What you control | Policy mechanism | 
| --- | --- | --- | 
| [Configure TIP](#id_roles_providers_tip_federation_policies_control_tip_configuration) | Who can add, change, or remove TIP configuration, which identity provider issuers they can configure, and which IAM Identity Center instance they can associate | Allow the applicable [IAM identity provider actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_iam.html#list_iam-actions-as-permissions). Use the six configuration condition keys described in [Govern TIP configuration with service control policies](#id_roles_providers_tip_federation_policies_govern_tip_configuration_with_service_control_policies). | 
| [Attach TIP context](#id_roles_providers_tip_federation_policies_control_tip_context_attachment_with_aws_sts) | Whether AWS STS can complete a request that attaches or copies TIP context | Within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), use `sts:SetContext` to control context attachment. An applicable explicit `Deny` for `sts:SetContext` causes the complete request to fail. Outside the boundary, AWS STS drops TIP context and the role assumption can still succeed. During initial SAML or OIDC federation, use `sts:RequestContextProviders` to identify the requested context-provider type. | 
| [Authorize access](#id_roles_providers_tip_federation_policies_use_tip_context_to_authorize_access) | Whether a caller using credentials that carry TIP context can assume particular IAM roles or access particular AWS resources | Evaluate `aws:OriginIdentity/*` and `aws:TransactionContext/IdentityProvider/*` in applicable trust, identity, and resource policies. Use resource control policies (RCPs) to establish issuer guardrails for supported AWS resources. | 

AWS authorizes each control point independently:
+ Permission to configure TIP does not authorize federation.
+ Permission to call the primary AWS STS operation does not authorize context attachment.
+ Authorization to attach TIP context does not grant access to another role or AWS resource.

## Control TIP configuration
<a name="id_roles_providers_tip_federation_policies_control_tip_configuration"></a>

An administrator configures TIP while creating or updating an IAM SAML or OpenID Connect (OIDC) identity provider. The following table shows the IAM actions used for each protocol.


| Protocol | Create a provider | Add, change, or remove TIP on a provider | 
| --- | --- | --- | 
| SAML | [`iam:CreateSAMLProvider`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateSAMLProvider.html) | [`iam:UpdateSAMLProvider`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSAMLProvider.html) | 
| OIDC | [`iam:CreateOpenIDConnectProvider`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html) | `iam:UpdateOpenIDConnectProvider` | 

Grant administrators only the actions and resources required to manage the intended IAM identity providers. For the complete configuration flow, see [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md) or [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md).

Both create and update actions support resource-level permissions for the applicable `saml-provider` or `oidc-provider` resource.

### Govern TIP configuration with service control policies
<a name="id_roles_providers_tip_federation_policies_govern_tip_configuration_with_service_control_policies"></a>

An organization can use service control policies (SCPs) to set the maximum permissions available to principals in member accounts. An SCP does not grant permission to configure TIP. The administrator still needs an identity-based Allow for the applicable IAM identity provider action.

Use these IAM condition keys for configuration-time governance:
+ `iam:EnableIdentityPropagation` indicates whether the request changes TIP configuration. Its value is `true` when the request includes `ContextProvider` and `false` when the request includes `RemoveContextProvider`. The key is absent when the request does not change the context provider.
+ `iam:EnableIdentityCenterAssociation` indicates whether the request changes the IAM Identity Center association. Its value is `true` when the request includes `IdentityCenterInstanceArn` and `false` when the request includes `RemoveIdentityCenterInstance`. The key is absent when the request does not change the association.
+ `iam:RequestIdentityProviderIssuers` contains issuer values supplied by the request. It is a multivalued key. For OIDC, the request value is the provider host and path without the `https://` prefix. For SAML, the values are the signing-key hashes derived from a metadata document supplied in the request. The key is absent when a supported request does not supply an issuer value. `UpdateOpenIDConnectProvider` does not support this key because the operation does not accept a provider URL.
+ `iam:ResourceIdentityProviderIssuers` contains issuer values for the IAM identity provider being created or updated. It is a multivalued key. On create, the values match the request issuer values. For the `UpdateSAMLProvider` API operation, IAM derives the values from the stored SAML metadata. For the `UpdateOpenIDConnectProvider` API operation, IAM derives the value from the stored provider URL (its host and path). The key is absent for provider delete and tagging operations and for OIDC provider operations that add or remove client IDs or update thumbprints.
+ `iam:RequestIdentityCenterInstanceArn` contains the IAM Identity Center instance ARN supplied in the request. The key is present when the request includes `IdentityCenterInstanceArn` and absent when the request removes an association or does not change one.
+ `iam:ResourceIdentityCenterInstanceArn` contains the IAM Identity Center instance ARN associated with the provider being acted on. On create, the value is the request ARN. On update, the value is the existing association, so a policy can evaluate the instance being removed.

The request and resource issuer keys are multivalued. Use a set operator whenever a policy evaluates either key. The following SCP enforces two guardrails: a create or update request cannot supply any unapproved issuer, and TIP cannot be enabled or modified on a provider that has any unapproved stored issuer.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnapprovedRequestedIssuers",
      "Effect": "Deny",
      "Action": [
        "iam:CreateSAMLProvider",
        "iam:UpdateSAMLProvider",
        "iam:CreateOpenIDConnectProvider"
      ],
      "Resource": "*",
      "Condition": {
        "Null": {
          "iam:RequestIdentityProviderIssuers": "false"
        },
        "ForAnyValue:StringNotEquals": {
          "iam:RequestIdentityProviderIssuers": [
            "idp.example.com",
            "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
          ]
        }
      }
    },
    {
      "Sid": "DenyTIPForUnapprovedResourceIssuers",
      "Effect": "Deny",
      "Action": [
        "iam:CreateSAMLProvider",
        "iam:UpdateSAMLProvider",
        "iam:CreateOpenIDConnectProvider",
        "iam:UpdateOpenIDConnectProvider"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "iam:EnableIdentityPropagation": "true"
        },
        "Null": {
          "iam:ResourceIdentityProviderIssuers": "false"
        },
        "ForAnyValue:StringNotEquals": {
          "iam:ResourceIdentityProviderIssuers": [
            "idp.example.com",
            "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
          ]
        }
      }
    },
    {
      "Sid": "DenyTIPWithoutResourceIssuers",
      "Effect": "Deny",
      "Action": [
        "iam:CreateSAMLProvider",
        "iam:UpdateSAMLProvider",
        "iam:CreateOpenIDConnectProvider",
        "iam:UpdateOpenIDConnectProvider"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "iam:EnableIdentityPropagation": "true"
        },
        "Null": {
          "iam:ResourceIdentityProviderIssuers": "true"
        }
      }
    }
  ]
}
```

The first statement denies a request when any issuer supplied by that request is outside the approved list. The request-key presence requirement means that the statement does not affect an update that supplies no new issuer value. The second statement applies when a request enables or modifies TIP and denies the request when any stored provider issuer is unapproved. The third statement fails closed when a request enables or modifies TIP but IAM cannot determine a stored provider issuer.

A SAML metadata-only update does not include `iam:EnableIdentityPropagation`, so the resource-issuer statements do not block replacing unapproved stored metadata with approved metadata. The request-issuer statement still validates every issuer supplied by the replacement metadata.

To control IAM Identity Center associations, use `iam:RequestIdentityCenterInstanceArn` for an instance supplied by the request and `iam:ResourceIdentityCenterInstanceArn` for the association that exists on the provider. Use `iam:EnableIdentityCenterAssociation` to distinguish attachment (`true`) from removal (`false`). For the association procedure, see [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md).

## Control TIP context attachment with AWS STS
<a name="id_roles_providers_tip_federation_policies_control_tip_context_attachment_with_aws_sts"></a>

`sts:SetContext` is a permission-only action that AWS STS evaluates when it attaches TIP context during initial federation, copies TIP context during direct role chaining, or reattaches context when a supported AWS service assumes an IAM service role. It is not a separate API operation. Within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), AWS STS supplies an implicit `Allow` for `sts:SetContext` to the applicable trust and identity policy layers. Customers generally do not add an explicit `Allow` for `sts:SetContext` to those layers. Other restrictive policy layers must allow the action separately, and an applicable explicit `Deny` causes the complete request to fail. Outside the boundary, AWS STS drops TIP context and does not evaluate `sts:SetContext` for the dropped context. The primary role assumption can still succeed if it is otherwise authorized. The following table describes the authorization requirements when TIP context is within the boundary.


| Request path | Primary AWS STS authorization | Policy layers receiving the AWS STS-supplied `sts:SetContext` Allow | Other restrictive layers for `sts:SetContext` | 
| --- | --- | --- | --- | 
| Initial `AssumeRoleWithSAML` or `AssumeRoleWithWebIdentity` federation | The target role trust policy must allow the applicable federation operation. | Role trust policy | VPC endpoint policy | 
| Direct role chaining with eligible IAM federation TIP context | The caller must be authorized to call `sts:AssumeRole`, and the target role trust policy must allow the caller. | Caller's identity policy and target role trust policy | Caller's permissions boundary and session policy, applicable SCP, and VPC endpoint policy | 
| Supported AWS service reattachment through an IAM service role | The IAM service role trust policy must allow the AWS service principal to call `sts:AssumeRole`. | Caller's identity policy and IAM service role trust policy | Applicable permissions boundary, session policy, SCP, and VPC endpoint policy | 

The target role's permissions boundary and a session policy passed with the `AssumeRole` request apply to the resulting role session. These policies do not block creation of that session solely because they omit `sts:SetContext`. However, an onward role assumption within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) fails if one of these policies does not allow `sts:SetContext` for the resulting session.

A conditional customer-authored `Allow` for `sts:SetContext` in a trust or identity policy does not restrict context attachment because the unconditional AWS STS-supplied Allow can still authorize the action. To restrict the request within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), apply the condition to the primary AWS STS operation or use an explicit `Deny` for `sts:SetContext`.

An AWS STS-supplied Allow does not satisfy another restrictive policy layer that applies to the request. Within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), an applicable explicit `Deny` for `sts:SetContext` causes the complete federation or role-assumption request to fail. AWS STS does not issue credentials without TIP context for a request whose context is eligible to propagate within the boundary.

### Update restrictive Allow policies
<a name="id_roles_providers_tip_federation_policies_update_restrictive_allow_policies"></a>

Review the restrictive policy layers identified in the preceding request-path table. If one of these layers uses an Allow list for AWS STS actions, it must include `sts:SetContext` and the applicable primary AWS STS operation.

During initial SAML or OIDC federation, SCPs, permissions boundaries, and session policies do not apply because the caller is not an IAM user or role. If a VPC endpoint policy uses a restrictive Allow list for AWS STS actions, it must allow `sts:SetContext` and the applicable federation operation. The following VPC endpoint policy permits TIP context attachment for initial SAML and OIDC federation:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "sts:AssumeRoleWithSAML",
        "sts:AssumeRoleWithWebIdentity",
        "sts:SetContext"
      ],
      "Resource": "*"
    }
  ]
}
```

Apply the same requirement to the restrictive policy layers identified in the table for direct role chaining and supported AWS service reattachment. For a supported AWS service workflow, follow the AWS service documentation for additional service-specific policy requirements.

RCPs use Deny statements rather than restrictive Allow lists. An applicable explicit `Deny` statement for `sts:SetContext` in an RCP can still cause the complete request to fail.

Review restrictive policies that constrain AWS STS actions before using TIP. For detailed endpoint guidance, see [Control access to AWS STS with VPC endpoint policies](reference_sts_vpc_endpoint_policies.md).

### Restrict context attachment by provider type
<a name="id_roles_providers_tip_federation_policies_identify_the_context_provider"></a>

Use the `sts:RequestContextProviders` condition key in an explicit `Deny` statement to block initial federation requests that attach a selected context-provider type. During initial SAML or OIDC federation, the key identifies the type of TIP context that the request asks AWS STS to attach. Its value is a list, even when only one provider contributes context. For IAM federation, use only these AWS-owned context-provider values:
+ OIDC: `arn:<partition>:iam::aws:contextProvider/OIDCProvider`
+ SAML: `arn:<partition>:iam::aws:contextProvider/SAMLProvider`

Replace `<partition>` with the AWS partition for the request, such as `aws`. Do not use the ARN of a customer-created IAM identity provider as the value of `sts:RequestContextProviders`.

The following policy denies requests that attach OIDC provider context.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyOIDCProviderContext",
      "Effect": "Deny",
      "Action": "sts:SetContext",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:ArnEquals": {
          "sts:RequestContextProviders": "arn:aws:iam::aws:contextProvider/OIDCProvider"
        }
      }
    }
  ]
}
```

This condition matches only during initial OIDC federation. It does not match later propagation because `sts:RequestContextProviders` is absent during direct role chaining and contains an empty list when a supported AWS service reattaches context extracted from the initiating session. To restrict downstream access based on the originating IAM identity provider, use `aws:OriginIdentity/FederatedProviderArn` or `aws:OriginIdentity/Issuer`.

## Use TIP context to authorize access
<a name="id_roles_providers_tip_federation_policies_use_tip_context_to_authorize_access"></a>

TIP context keys retain their documented `aws:` namespaces during policy evaluation. Use the keys as documented without adding an AWS STS request-context prefix. The following table shows the keys to use for common authorization decisions.


| Authorization decision | Context keys | 
| --- | --- | 
| Identify a specific originator and the identity provider that authenticated it | `aws:OriginIdentity/Subject` and `aws:OriginIdentity/Issuer` | 
| Identify the IAM identity provider through which the identity entered AWS | `aws:OriginIdentity/FederatedProviderArn` | 
| Identify the AWS account that owns the IAM identity provider | `aws:OriginIdentity/IdentityProviderAccount` | 
| Identify the AWS organization that contains the identity provider account | `aws:OriginIdentity/IdentityProviderOrgID` | 
| Restrict access to a human user or workload | `aws:OriginIdentity/SubjectType` | 
| Evaluate a configured runtime claim | `aws:TransactionContext/IdentityProvider/<TargetKey>` | 

Subject, Issuer, FederatedProviderArn, and IdentityProviderAccount are present in every IAM federation session with TIP context. IdentityProviderOrgID is present only when the identity provider account belongs to an AWS organization. SubjectType and runtime claims are optional. For value sources and presence rules, see [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md).

Before using TIP context keys in a policy for an AWS service, confirm that the credentials evaluated by the policy carry TIP context. See [AWS services that support TIP](id_roles_providers_tip_services.md).

### Identify an originator with Subject and Issuer
<a name="id_roles_providers_tip_federation_policies_identify_an_originator_with_subject_and_issuer"></a>

A Subject value is meaningful only within the identity provider that issued it. When a policy identifies a specific originator, evaluate `aws:OriginIdentity/Subject` together with `aws:OriginIdentity/Issuer`. This prevents the same Subject value from another identity provider from satisfying the policy.

The following identity-based policy allows a role session to read reports only when the session represents the specified user from the specified OIDC issuer.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadReportsForSpecificOriginator",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-reports/reports/*",
      "Condition": {
        "StringEquals": {
          "aws:OriginIdentity/Subject": "user@example.com",
          "aws:OriginIdentity/Issuer": "idp.example.com",
          "aws:OriginIdentity/SubjectType": "user"
        }
      }
    }
  ]
}
```

For OIDC federation, `aws:OriginIdentity/Issuer` is the OIDC token's `iss` claim without the `https://` prefix. AWS preserves the host, path, and any trailing slash. For example, an `iss` claim of `https://idp.example.com` produces an Issuer value of `idp.example.com`. For SAML federation, `aws:OriginIdentity/Issuer` is the lowercase hexadecimal SHA-384 hash of the DER-encoded public key that AWS used to verify the SAML assertion's signature. It identifies the signing key, not the assertion's `<Issuer>` entity ID.

#### Retrieve SAML Issuer values
<a name="id_roles_providers_tip_federation_policies_retrieve_saml_issuer_values"></a>

Create the IAM SAML identity provider before authoring a policy that restricts SAML Issuer values. After the provider exists, retrieve its Issuer values with the [`GetSAMLProvider` API operation](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSAMLProvider.html), the [AWS CLI `get-saml-provider` command](https://docs.aws.amazon.com/cli/latest/reference/iam/get-saml-provider.html), or an AWS SDK method such as the [AWS SDK for Python `get_saml_provider` method](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/get_saml_provider.html). Provide the IAM SAML identity provider ARN in the `SAMLProviderArn` request parameter.

The `SAMLKeyHashes` response element groups each SAML metadata issuer, identified by the `IssuerURL` member, with its signing-key hashes in the `KeyHashes` list. A provider can return multiple signing-key hashes. Each TIP session carries one `aws:OriginIdentity/Issuer` value for the signing key that AWS used to verify that session's assertion. Use the values in `KeyHashes`, not `IssuerURL`, as Issuer values in policies.

The following AWS CLI command returns only the signing-key hashes:

```bash
aws iam get-saml-provider \
    --saml-provider-arn arn:aws:iam::111122223333:saml-provider/ExampleProvider \
    --query 'SAMLKeyHashes[].KeyHashes[]' \
    --output json
```

A successful response contains one or more 96-character lowercase hexadecimal values:

```json
[
  "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
]
```

You can also retrieve these values in the IAM console. Open the SAML identity provider. On the **Metadata** tab, in **Metadata document**, choose **Summary**, and copy every value under **Signing key hashes**.

Include every current signing-key hash in policies that restrict Issuer. Before the identity provider rotates a signing key, add the new hash to the policy. Otherwise, the policy can deny sessions signed with the new key.

### Authorize access with runtime claims
<a name="id_roles_providers_tip_federation_policies_authorize_access_with_runtime_claims"></a>

A runtime claim can narrow access using a session-specific value selected by the customer. The following condition requires the configured `department` runtime claim to contain the string `Engineering`:

```json
{
  "Condition": {
    "StringEquals": {
      "aws:TransactionContext/IdentityProvider/department": "Engineering"
    }
  }
}
```

Only configured mappings create runtime-claim keys. If an optional source is absent from the SAML assertion or OIDC token, AWS STS creates the TIP session without that runtime claim. Do not assume that every identity provider claim is available in policy evaluation.

**Important**  
TIP context keys are absent from requests that do not carry TIP context, and optional keys can be absent from TIP sessions. In a Deny statement that uses a negated condition operator with a TIP key, include a `Null` condition when the Deny should apply only if the key is present. To deny requests that lack the key, use a separate Deny statement with a `Null` condition set to `true`.

### Use TIP conditions with encrypted resources
<a name="id_roles_providers_tip_federation_policies_use_tip_conditions_with_encrypted_resources"></a>

Some AWS services, such as Amazon S3 with S3 Bucket Keys and Amazon DynamoDB, cache data keys from AWS KMS to reduce the number of requests they send to AWS KMS. The service caches a data key for the IAM role, not for the TIP context of each request. After a request from one user or workload succeeds, the service can use the cached data key for a later request from another user or workload that uses the same role, without a new request to AWS KMS. In that case, AWS KMS does not evaluate either `Allow` or explicit `Deny` statements that use TIP conditions in the key policy for the later request.

To control access to encrypted data by user or workload, add TIP conditions to the policy of the resource that the request accesses, such as the Amazon S3 bucket policy. You can also use TIP conditions in an AWS KMS key policy, but the key policy might not be evaluated for every request when another AWS service uses the key on your behalf.

For more information, see [AWS global condition keys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-aws.html) in the *AWS Key Management Service Developer Guide*.

## Establish trust within and across accounts
<a name="id_roles_providers_tip_federation_policies_establish_trust_within_and_across_accounts"></a>

TIP conditions identify the originator and the identity provider that authenticated it. They do not replace the principal boundary established by a role trust policy or resource policy. Use `aws:OriginIdentity/IdentityProviderAccount` when a policy must trust an IAM identity provider owned by a specific AWS account. Use `aws:OriginIdentity/IdentityProviderOrgID` when a policy must trust IAM identity providers owned by accounts in a specific AWS organization. When AWS STS carries TIP context within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), these AWS-derived values continue to identify the original identity provider owner through role chains and AWS service workflows that use an IAM service role. The following sections explain how these controls apply within and across accounts.

### Same-account access
<a name="id_roles_providers_tip_federation_policies_same_account_access"></a>

Within one account, an administrator configures the IAM identity provider and controls the local roles, resources, and policies. That configuration establishes local trust in the provider. An RCP is not required for ordinary same-account TIP authorization.

Use Subject with Issuer when identifying a specific originator even in the same account. An account can contain multiple identity providers, and two providers can issue the same Subject value. You can also use `aws:OriginIdentity/FederatedProviderArn` when authorization must depend on the specific IAM identity provider resource.

An organization can apply an RCP to enforce a common approved-issuer standard for resources in member accounts. When the RCP applies and its conditions match an unapproved Issuer, it denies the same-account request.

### Cross-account role assumption
<a name="id_roles_providers_tip_federation_policies_cross_account_role_assumption"></a>

For cross-account role assumption, the target role's trust policy establishes principal trust and can evaluate TIP context carried by the caller. Trust in the calling principal does not automatically establish trust in every identity provider that the caller account can configure. AWS STS then applies the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) when it creates the new role session. If the target account is within the boundary, the new session carries TIP context. If the target account is outside the boundary, the role assumption can still succeed, but the new session does not contain TIP context.

The following trust-policy statement allows a role from account `111122223333` to assume the target role only when the TIP context identifies the specified originator and issuer:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/FederatedAccessRole"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:OriginIdentity/Subject": "user@example.com",
          "aws:OriginIdentity/Issuer": "idp.example.com"
        }
      }
    }
  ]
}
```

The `Principal` element establishes which role can enter the target account. Subject and Issuer conditions establish which originator can make the `AssumeRole` request. If the target role is within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), the resulting role session carries the context and subsequent policies can evaluate it. If the target role is outside the boundary, the resulting role session does not contain TIP context. The policies that govern subsequent AWS resource requests are evaluated separately.

### Direct cross-account resource access
<a name="id_roles_providers_tip_federation_policies_direct_cross_account_resource_access"></a>

For direct cross-account access, a resource policy should scope `Principal` to the intended external account or role. Subject narrows access to the originator, and Issuer identifies the identity provider that authenticated the Subject. The following resource-policy statement allows the specified role to read reports only when its TIP context identifies the specified originator and issuer:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadReportsForCrossAccountOriginator",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/FederatedAccessRole"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-reports/reports/*",
      "Condition": {
        "StringEquals": {
          "aws:OriginIdentity/Subject": "user@example.com",
          "aws:OriginIdentity/Issuer": "idp.example.com"
        }
      }
    }
  ]
}
```

Do not use `Principal: "*"` with only a Subject condition to identify a cross-account originator. Another account can configure a different identity provider that issues the same Subject value. Use a scoped `Principal` element and evaluate Subject with Issuer.

### Enforce approved issuers for Amazon S3 with an RCP
<a name="id_roles_providers_tip_federation_policies_enforce_approved_issuers_with_an_rcp"></a>

An RCP sets the maximum permissions available for supported AWS resources in an organization. It does not grant access. The caller still needs an applicable Allow in an identity-based or resource-based policy, and any explicit Deny continues to override that Allow.

A customer-managed RCP must identify at least one AWS service in its `Action` element. The following RCP denies Amazon S3 requests made with TIP context when Issuer is not in the approved list. The `Null` condition limits the Deny to requests in which `aws:OriginIdentity/Issuer` is present, so requests made without TIP context are unaffected.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyTIPFromUnapprovedIssuers",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:OriginIdentity/Issuer": [
            "idp.example.com"
          ]
        },
        "Null": {
          "aws:OriginIdentity/Issuer": "false"
        }
      }
    }
  ]
}
```

The resource-owning organization controls this guardrail. AWS evaluates the RCP for requests to Amazon S3 resources in member accounts, including same-account and cross-account requests. When the conditions match, the RCP denies the Amazon S3 request. RCPs do not affect resources in the organization management account.

Before adapting this pattern to another AWS service, confirm that the AWS service supports RCPs and that `aws:OriginIdentity/Issuer` is available when the service authorizes the intended actions and resources.

Within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), an applicable RCP can contain an explicit `Deny` for `sts:SetContext`. That statement overrides the AWS STS-supplied Allow, and the complete federation or `AssumeRole` request fails with `AccessDenied`. Outside the boundary, AWS STS drops TIP context and does not evaluate `sts:SetContext` for the dropped context, so the role assumption can still succeed if it is otherwise authorized.

Before attaching an RCP broadly, test its effect in a separate organization or organizational unit that represents your production environment. Add exceptions required by supported AWS services, then deploy the RCP progressively. For general behavior and deployment guidance, see [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html), [RCP evaluation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_evaluation.html), and [Resource control policy examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps_examples.html).

## Verify and troubleshoot policy behavior
<a name="id_roles_providers_tip_federation_policies_verify_and_troubleshoot_policy_behavior"></a>

Determine first whether a failure occurred while configuring TIP, attaching TIP context, or authorizing access with the resulting credentials. The following table shows where to inspect each outcome, the exact expected value, and what a missing or different value means.


| Outcome | Where to inspect | Exact expected value | Meaning of a missing or different value | 
| --- | --- | --- | --- | 
| TIP configuration | Open the IAM identity provider details in the IAM console after the create or update request. | **Propagation status** is **Configured**, and the displayed Subject and runtime mappings match the submitted configuration. | IAM did not save the intended TIP configuration. The request might have been denied by an identity policy, permissions boundary, session policy, SCP, or applicable VPC endpoint policy, or the submitted values differed from the intended configuration. Inspect the create or update error before retrying. | 
| Context attachment | In the AWS CloudTrail trail log for the AWS Region that processed the federation request, inspect the `AssumeRoleWithSAML` event for SAML or the `AssumeRoleWithWebIdentity` event for OIDC. | `userIdentity.onBehalfOf.subject`, `userIdentity.onBehalfOf.issuer`, and `userIdentity.onBehalfOf.federatedProviderArn` contain the expected Subject, Issuer, and IAM identity provider ARN. | A missing `onBehalfOf` object or required member means the event does not contain the expected TIP context. Inspect the federation response and provider configuration to determine whether the request failed or created a session without the expected context. A different value means the request used a different originator or identity provider. | 
| Runtime claim | Inspect `userIdentity.transactionContext.IdentityProvider.<TargetKey>` in the same AWS CloudTrail federation event. | The member name equals the configured `TargetKey`, including case, and its string value equals the value supplied by the identity provider. | If the core `onBehalfOf` values are present but the runtime member is missing, the mapping was not configured or the optional source was absent. A different value means the identity provider supplied a different runtime value or the customer inspected a different target key. | 
| Initial federation blocked by an AWS STS policy | Inspect the target role trust policy and any VPC endpoint policy used for the initial SAML or OIDC federation request. | The role trust policy allows the applicable federation operation. Any restrictive VPC endpoint policy allows both the federation operation and `sts:SetContext`, and no applicable policy explicitly denies either action. | If the trust policy does not allow the federation operation, or the VPC endpoint policy omits or denies a required action, the entire federation request fails. SCPs, permissions boundaries, and session policies do not apply to the initial federation request. AWS STS does not remove TIP context and issue non-TIP credentials. | 
| Direct role chain blocked by an AWS STS policy | First confirm that the target role is within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation). Then inspect the session policy attached to the caller's session, the caller's permissions boundary, applicable SCPs, and the VPC endpoint policy. If the current role assumption succeeds but an onward hop fails, inspect the current role's permissions boundary and any session policy passed with the request that created the current session. Also inspect all applicable policy types for an explicit `Deny` that applies to `sts:AssumeRole` or `sts:SetContext`. | Within the boundary, each applicable restrictive policy for the role-assumption request permits both `sts:AssumeRole` and `sts:SetContext`, and no applicable policy explicitly denies either action. For an onward hop, the current role's permissions boundary and session policy also permit both actions. | Within the boundary, omitting `sts:SetContext` from the caller's restrictive session policy, permissions boundary, an allow-list SCP, or the VPC endpoint policy can deny the complete `AssumeRole` request. The target role's permissions boundary and a session policy passed with the current request do not block creation of the current session solely because they omit `sts:SetContext`. However, that omission can deny an onward role assumption within the boundary. An explicit Deny in any applicable policy also denies the request. The target role's trust policy and the caller's identity policy do not require a customer-authored `Allow` for `sts:SetContext`. Outside the boundary, AWS STS drops TIP context and the role assumption can still succeed if `sts:AssumeRole` is otherwise authorized. | 
| Subject-based authorization | Inspect the applicable trust, identity, and resource policy conditions, then compare them with the AWS CloudTrail `onBehalfOf` values. | The policy's `aws:OriginIdentity/Subject` value exactly matches `userIdentity.onBehalfOf.subject`, and its `aws:OriginIdentity/Issuer` value exactly matches `userIdentity.onBehalfOf.issuer`. | A missing policy condition can create an incomplete trust boundary. A missing context value prevents a positive `StringEquals` condition from matching. A different value means the policy identifies a different originator or identity provider. | 
| Approved-issuer RCP for Amazon S3 | In the organization that contains the target account, inspect the RCPs attached from the organization root through each organizational unit to the target account that owns the Amazon S3 resource. For a successful request, compare the approved values with `userIdentity.onBehalfOf.issuer` in the Amazon S3 event recorded in the target account. For a denied cross-account request, inspect the `AccessDenied` event in the caller account to identify the unapproved Issuer. The target account also receives an event, but the target-account event does not contain TIP context. | For a successful request, `userIdentity.onBehalfOf.issuer` equals an approved value, so the conditions in the RCP `Deny` statement do not match. For a denied test, the caller-account event contains the unapproved Issuer that caused the RCP `Deny` statement to match. The target-account event does not contain `userIdentity.onBehalfOf` or `userIdentity.transactionContext`. | If an approved request is denied, confirm that every applicable RCP contains the expected Issuer. If an unapproved request succeeds, confirm that the RCP is attached to the member account or an ancestor and that the requested Amazon S3 resource is covered. If the resource is in the management account, investigate other policy types because RCPs do not apply there. | 
| Non-TIP request denied unexpectedly | Inspect each Deny statement that uses a negated operator with an `aws:OriginIdentity/*` or `aws:TransactionContext/IdentityProvider/*` key. | Each statement intended to evaluate only requests that carry TIP context also contains `"Null": {"aws:OriginIdentity/Issuer": "false"}` when the statement tests that key. | A missing Null guard can cause the Deny to apply when the request does not contain the TIP key. Add the guard if non-TIP requests must remain unaffected. | 

For a first-use verification journey, see [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md).