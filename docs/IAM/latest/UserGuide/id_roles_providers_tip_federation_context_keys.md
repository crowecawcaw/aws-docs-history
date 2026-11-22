

# TIP context keys and runtime claims for IAM federation

Trusted identity propagation (TIP) for IAM federation attaches identity context to role sessions created through SAML or OpenID Connect (OIDC) federation. The context identifies the end user, which can be a human user or workload, and the authenticating external identity provider. It can also include selected claims for the current federation session. AWS represents each value with a context key, such as `aws:OriginIdentity/Subject`. This page defines these keys and their value sources. It also explains which values are required or optional, how AWS preserves the context through supported workflows, and where customers can use or inspect the context.

For the shared TIP model and other ways to establish TIP context, see [Trusted identity propagation with IAM](id_roles_providers_tip.md). For IAM federation configuration procedures, see [Configure TIP for an IAM identity provider](id_roles_providers_tip_federation_configure.md). For Region and partition availability, see [Regional availability for TIP for IAM federation](id_roles_providers_tip_federation.md#id_roles_providers_tip_federation_regional_availability).

## Understand the context established through IAM federation
<a name="id_roles_providers_tip_federation_context_keys_understand_the_context_established_through_iam_federation"></a>

TIP context can contain core origin identity, optional identity provider runtime claims, and directory references for group-based access. The following table identifies these three categories, the keys or namespaces used for each category, and what each category represents.


| Context category | Keys or namespace | What it represents | 
| --- | --- | --- | 
| Core origin identity | `aws:OriginIdentity/*` | The end user that originated the workflow, the authenticating identity provider, the AWS account that owns the IAM identity provider, the AWS organization that contains that account when applicable, and the optional Subject type | 
| Identity provider runtime claims | `aws:TransactionContext/IdentityProvider/*` | Additional session-specific values that the identity provider supplies from sources selected by the customer | 
| Directory context | `aws:IdentityCenterInstanceArn` and `aws:IdentityStoreArn` | References to the IAM Identity Center instance and identity store that supported AWS services use to resolve the Subject's group membership | 

Values enter TIP context in three ways:
+ **Identity-provider-supplied values:** The customer selects a SAML assertion field or OIDC token claim. The identity provider supplies its value during federation. AWS STS validates the SAML assertion or OIDC token before attaching the selected value. This applies to Subject, mapped Subject type, and runtime claims.
+ **Customer-configured values and associations:** The customer can configure a fixed Subject type or associate an IAM Identity Center instance with the IAM identity provider.
+ **AWS-derived values:** AWS derives Issuer and the identity provider account from the configured IAM identity provider used for federation. When that account belongs to an AWS organization, AWS derives the identity provider organization ID. AWS derives the identity store ARN from the associated IAM Identity Center instance.

Every IAM federation session with TIP context contains Subject, Issuer, the federated provider ARN, and the identity provider account. Subject type and runtime claims are optional. The identity provider organization ID is present only when the identity provider account belongs to an AWS organization. Directory context is included only when group-based access is configured.

## Identify the originator and identity provider
<a name="id_roles_providers_tip_federation_context_keys_identify_the_originator_and_identity_provider"></a>

Core origin identity identifies the end user that started the workflow, the external identity provider used for federation, and the AWS ownership boundary for the corresponding IAM identity provider. Subject identifies the end user. Issuer and FederatedProviderArn identify the external identity provider and IAM identity provider resource. IdentityProviderAccount identifies the AWS account that owns the IAM identity provider. IdentityProviderOrgID identifies that account's AWS organization when the account belongs to one.

**Important**  
`aws:OriginIdentity/IdentityProviderAccount` and `aws:OriginIdentity/IdentityProviderOrgID` are AWS-derived ownership keys. They identify the AWS account that owns the IAM identity provider and, when applicable, the AWS organization that contains that account. AWS STS uses these values to determine the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation). Customers do not configure these values, and callers cannot change them after AWS STS attaches them to the session.

The following table lists each core origin identity key, when it appears, what it identifies, and where its value comes from.


| Context key | Presence | What it identifies | Value source | 
| --- | --- | --- | --- | 
| `aws:OriginIdentity/Subject` | Every IAM federation session with TIP context | The end user that started the workflow | The identity provider supplies the value from the customer-selected SAML assertion field or OIDC token claim. AWS STS validates the assertion or token before attaching the selected value. | 
| `aws:OriginIdentity/Issuer` | Every IAM federation session with TIP context | The external identity provider that authenticated the Subject | AWS derives the value from the identity provider used for federation. For OIDC federation, `aws:OriginIdentity/Issuer` is the OIDC token's `iss` claim without the `https://` prefix. AWS preserves the host, path, and any trailing slash. For SAML federation, `aws:OriginIdentity/Issuer` is the lowercase hexadecimal SHA-384 hash of the DER-encoded public key that AWS used to verify the SAML assertion's signature. The resulting value identifies the signing key, not the SAML assertion Issuer element. | 
| `aws:OriginIdentity/FederatedProviderArn` | Every IAM federation session with TIP context | The IAM identity provider through which the identity entered AWS | AWS derives the ARN from the IAM identity provider used for federation. | 
| `aws:OriginIdentity/IdentityProviderAccount` | Every IAM federation session with TIP context | The AWS account that owns the IAM identity provider used for federation | AWS derives the account ID from the validated IAM identity provider ARN. When AWS STS carries TIP context within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), this value remains unchanged through role chains and AWS service workflows that use an IAM service role. | 
| `aws:OriginIdentity/IdentityProviderOrgID` | When the identity provider account belongs to an AWS organization | The AWS organization that contains the account that owns the IAM identity provider | AWS derives the organization ID from the identity provider account. The key is absent when that account does not belong to an AWS organization. When AWS STS carries TIP context within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), this value remains unchanged through role chains and AWS service workflows that use an IAM service role. | 
| `aws:OriginIdentity/SubjectType` | Optional | Whether the end user is a `user` or `workload` | The customer configures `user` or `workload` as a fixed value, or selects a SAML assertion field or OIDC token claim. For a mapped value, the identity provider supplies the value and AWS STS validates the assertion or token before attaching it. | 

The selected Subject source must be present. Choose a source that is stable and unique within the identity provider. The value must meet the [source-value requirements](#id_roles_providers_tip_federation_context_keys_meet_source_value_requirements). For source-selection guidance, see [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md) or [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md).

If you do not configure Subject type, AWS STS does not attach `aws:OriginIdentity/SubjectType`.

## Map identity provider runtime claims
<a name="id_roles_providers_tip_federation_context_keys_map_identity_provider_runtime_claims"></a>

Runtime-claim mappings attach optional, session-specific identity provider values to TIP context. Each mapping has a required source and an optional target-key suffix:
+ A required source field in a SAML assertion or claim in an OIDC token
+ An optional target-key suffix that determines the resulting TIP context key

Each runtime context key uses this format:

```
aws:TransactionContext/IdentityProvider/<TargetKey>
```

The customer selects the source and can optionally specify a target-key suffix. If `TargetKey` is omitted, IAM uses `SourceKey` as the target-key suffix. If `TargetKey` is provided, it can differ from `SourceKey`. The identity provider supplies the source value during federation. AWS STS verifies the assertion or token and attaches the value under the resulting runtime context key.

When you configure TIP through an IAM API, CLI, or SDK, `KeyDefinitionList` in the `ContextProvider` request parameter defines the runtime-claim mappings. The following table lists the runtime-specific members, what each member controls, and whether it is required.


| `ContextProvider` member | Purpose | Requirement | 
| --- | --- | --- | 
| `KeyDefinitionList` | Contains the runtime-claim mappings | Optional; up to 10 entries | 
| `KeyDefinitionList[].SourceKey` | Identifies the source field in a SAML assertion or claim in an OIDC token | Required for each mapping; 1 to 128 characters | 
| `KeyDefinitionList[].TargetKey` | Supplies the suffix appended to `aws:TransactionContext/IdentityProvider/` | Optional. If omitted, IAM uses `SourceKey`. If provided, it must contain 1 to 128 characters; an empty value is invalid. | 

For the reserved source-key values that select standard SAML assertion fields, see [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-create-programmatically).

IAM applies the same character requirements to every source and target key in `ContextProvider`: the required Subject source, the optional Subject type source, each runtime-claim source, and each optional runtime-claim target suffix. In API, AWS CLI, and AWS SDK requests, these values are represented by `SubjectSourceKey`, `SubjectTypeSourceKey`, `KeyDefinitionList[].SourceKey`, and `KeyDefinitionList[].TargetKey`.

Each supplied key must contain 1 to 128 characters. It can contain only ASCII letters and digits, single spaces, and the characters `_ . : / = + - @ #`. It cannot start or end with a space or contain two consecutive spaces.

IAM reserves the effective target-key suffixes `subject`, `subjecttype`, `identitystorearn`, `identitycenterinstancearn`, and `identitycentersessionid`, in any capitalization. The effective suffix is `TargetKey` when you provide it and `SourceKey` when you omit `TargetKey`.

Runtime claims are optional and do not replace the required Subject. Each `SourceKey` must be unique without regard to case. Each effective target-key suffix must also be unique without regard to case.

## Meet source-value requirements
<a name="id_roles_providers_tip_federation_context_keys_meet_source_value_requirements"></a>

The Subject, a mapped Subject type, and each mapped runtime claim must contain one value of no more than 128 characters. AWS STS accepts strings, numbers, and Boolean values and represents accepted numbers and Boolean values as strings. Values can contain letters, numbers, spaces, and the characters `_ . : / = + - @`.

For an OIDC token, AWS STS flattens an object claim nested one level into `<claim>/<member>` sources. For example, you can map `org/team` from `"org": {"team": "payments"}`. The object claim itself is not a mappable value and is treated as absent. AWS STS rejects a mapped object nested more than one level deep. It also rejects a flattened key that collides with another claim of the same name, even when neither claim is mapped.

AWS STS rejects the federation request with `InvalidIdentityToken` in these cases:
+ The required Subject source is absent.
+ A configured mapped Subject type source is absent.
+ A configured source is present but empty, contains only whitespace or space separators, contains multiple values, exceeds 128 characters, uses an unsupported type, or contains an unsupported character.
+ The Subject starts or ends with a space or contains a separator character other than a space.
+ A mapped Subject type has a value other than `user` or `workload`.
+ A claim mapped to a target key ending in `IssueTime`, with that capitalization, does not contain an integer.
+ A target key matches, without regard to case, the `Age` key derived from another target key ending in `IssueTime`. For example, `loginIssueTime` reserves the derived key `loginAge`.

An absent optional runtime claim is omitted from the session. A present optional runtime claim that violates a requirement causes the federation request to fail.

TIP context shares the capacity of the AWS STS session token with other session data; it does not have a separate fixed aggregate runtime-claim quota in the IAM service model. If the combined session content is too large, the federation request fails with `PackedPolicyTooLarge`.

Customer-selected runtime claims use `aws:TransactionContext/IdentityProvider/*`. They do not use the `aws:OriginIdentity/*` namespace reserved for core origin identity.

## Resolve group membership through directory context
<a name="id_roles_providers_tip_federation_context_keys_resolve_group_membership_through_directory_context"></a>

When you configure TIP for a SAML or OIDC provider, you can select **Allow granting permissions to groups** to associate the provider with an IAM Identity Center instance. For the selection and setup procedure, see [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md). TIP then includes directory context that supported AWS services use to resolve the Subject and evaluate group-based access.

The following table identifies the directory context keys, what each key represents, and where its value comes from.


| Context key | What it identifies | Value source | 
| --- | --- | --- | 
| `aws:IdentityCenterInstanceArn` | The IAM Identity Center instance associated with the IAM identity provider | The customer selects the IAM Identity Center instance. IAM stores the provider association. AWS STS attaches the instance ARN to the TIP session. | 
| `aws:IdentityStoreArn` | The identity store associated with that IAM Identity Center instance | IAM derives and stores the identity store ARN from the selected instance. AWS STS attaches it to the TIP session. | 

These values are not identity provider claim mappings. They connect the propagated Subject to the directory used by supported AWS services. The Subject value must match the corresponding user's **Username** in IAM Identity Center so that the AWS service can resolve group membership.

When group-based access is configured, `aws:IdentityCenterInstanceArn` and `aws:IdentityStoreArn` are available for evaluation in applicable IAM policy conditions. Use these keys to restrict access to the expected IAM Identity Center instance or identity store. A `StringEquals` condition that tests either key does not match when the request does not contain that key.

## See the resulting TIP context
<a name="id_roles_providers_tip_federation_context_keys_see_the_resulting_tip_context"></a>

The following examples distinguish the identity provider input, customer configuration, AWS-derived values, and resulting context. They do not include directory context because group-based access is not configured. For complete configuration requests, see [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md) or [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md).

### OIDC workload example
<a name="id_roles_providers_tip_federation_context_keys_oidc_workload_example"></a>

**Identity provider input.** An OIDC provider issues a token that AWS STS verifies. The token contains the following claims:

```json
{
  "sub": "workload-1234567890",
  "environment": "production"
}
```

**Customer configuration.** The customer selects `sub` as the Subject, configures the fixed Subject type `workload`, and maps `environment` to the target-key suffix `environment`.

**AWS-derived context.** AWS derives the Issuer, federated provider ARN, identity provider account, and identity provider organization ID from the configured OIDC provider and its owning account. The customer does not configure these values as runtime-claim mappings.

**Resulting TIP context.** AWS STS attaches:

```
aws:OriginIdentity/Subject = "workload-1234567890"
aws:OriginIdentity/Issuer = "idp.example.com"
aws:OriginIdentity/FederatedProviderArn = "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
aws:OriginIdentity/IdentityProviderAccount = "111122223333"
aws:OriginIdentity/IdentityProviderOrgID = "o-a1b2c3d4e5"
aws:OriginIdentity/SubjectType = "workload"
aws:TransactionContext/IdentityProvider/environment = "production"
```

### SAML user example
<a name="id_roles_providers_tip_federation_context_keys_saml_user_example"></a>

**Identity provider input.** A SAML provider sends `user@example.com` in `Subject/NameID` and includes a `department` assertion attribute with the single value `Finance`.

**Customer configuration.** The customer selects `Subject/NameID` as the Subject, configures the fixed Subject type `user`, and maps the `department` attribute to the target-key suffix `department`.

**AWS-derived context.** AWS derives the Issuer as the lowercase hexadecimal SHA-384 hash of the DER-encoded public key that it used to verify the assertion's signature. The value identifies the signing key, not the assertion's `<Issuer>` entity ID. AWS also derives the federated provider ARN and identity provider account from the configured SAML provider. The example account belongs to an AWS organization, so AWS derives the identity provider organization ID.

**Resulting TIP context.** AWS STS attaches:

```
aws:OriginIdentity/Subject = "user@example.com"
aws:OriginIdentity/Issuer = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
aws:OriginIdentity/FederatedProviderArn = "arn:aws:iam::111122223333:saml-provider/ExampleProvider"
aws:OriginIdentity/IdentityProviderAccount = "111122223333"
aws:OriginIdentity/IdentityProviderOrgID = "o-a1b2c3d4e5"
aws:OriginIdentity/SubjectType = "user"
aws:TransactionContext/IdentityProvider/department = "Finance"
```

## Preserve TIP context across the workflow
<a name="id_roles_providers_tip_federation_context_keys_preserve_tip_context_across_the_workflow"></a>

The following scenarios show when TIP context persists as a workflow uses additional IAM roles:
+ **A federated session directly assumes another role.** An end user federates into Role A with TIP context and then uses that session to assume Role B. AWS STS first applies the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation). If Role B is within the boundary, AWS STS carries TIP context into the new role session without requiring a customer-authored Allow for `sts:SetContext`. An applicable explicit Deny for `sts:AssumeRole` or `sts:SetContext` causes the complete request to fail. If Role B is outside the boundary, AWS STS does not carry TIP context into the new session. The role assumption can still succeed if `sts:AssumeRole` is otherwise authorized.
+ **An AWS service assumes an IAM service role.** An end user calls a supported AWS service with a TIP session. When the AWS service uses its own credentials to assume an [IAM service role](id_roles_create_for-service.md) for that workflow, AWS STS applies the [same TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation). Within the boundary, AWS STS reattaches the caller's TIP context to the service role credentials. Outside the boundary, the role assumption can still succeed, but the service role credentials do not contain TIP context.

TIP context has these properties:
+ **Attached after validation:** AWS STS attaches identity-provider values only after validating the SAML assertion or OIDC token.
+ **Immutable:** A downstream caller cannot change or remove an attached value.
+ **Persistent within the TIP propagation boundary:** Supported workflows preserve the context as they use additional IAM roles within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation).
+ **Namespace-separated:** Core identity and runtime claims use different namespaces, so a runtime claim cannot replace the Subject or Issuer.

## Use and inspect TIP context
<a name="id_roles_providers_tip_federation_context_keys_use_and_inspect_tip_context"></a>

TIP context does not grant permissions by itself. Customers can use the context in IAM policy conditions and inspect it in AWS CloudTrail records.

### Use TIP context in IAM policies
<a name="id_roles_providers_tip_federation_context_keys_use_tip_context_in_iam_policies"></a>

All AWS services can use TIP context when they evaluate an IAM policy for a request made with credentials that carry TIP context. If an AWS service uses an IAM service role, it must carry TIP context into the service role credentials before the context is available for policy evaluation.

For condition keys and policy examples, see [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md). To check which AWS services can use TIP context in IAM policies, see [AWS services that support TIP](id_roles_providers_tip_services.md).

### Inspect TIP context in AWS CloudTrail
<a name="id_roles_providers_tip_federation_context_keys_inspect_tip_context_in_aws_cloudtrail"></a>

AWS CloudTrail records TIP context in the federation event that creates the TIP session. For later requests, supported events can include the context carried by the role session.

The following table shows the CloudTrail location for each TIP context category.


| TIP context category | AWS CloudTrail location | 
| --- | --- | 
| Core origin identity | `userIdentity.onBehalfOf` | 
| Identity provider runtime claims | `userIdentity.transactionContext.IdentityProvider` | 
| Directory context | `userIdentity.onBehalfOf.identityCenterInstanceArn` and `userIdentity.onBehalfOf.identityStoreArn` | 

For event paths, recipient accounts, personal-information disclosure, CloudTrail surfaces, retention, redaction, policy safeguards, and logging examples, see [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md).