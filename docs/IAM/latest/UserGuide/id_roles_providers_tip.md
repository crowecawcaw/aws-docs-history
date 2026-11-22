

# Trusted identity propagation with IAM

Multiple human users or workloads can use the same IAM role. The role determines what the session can do, but the role alone does not identify the human user or workload throughout an AWS workflow. This makes it difficult to authorize or audit activity based on the identity behind the shared role.

Trusted identity propagation (TIP) attaches identity context from a trusted source when AWS creates a role session. The context identifies the human user or workload that started the request. After AWS attaches the context, callers cannot change it during the lifetime of the role session.

Trusted sources include configured external identity providers for AWS IAM federation and X.509 certificates validated against configured trust anchors for IAM Roles Anywhere.

Use this page to understand TIP across these identity sources and choose the applicable access path. Each path has its own configuration, permissions, verification procedure, and availability. For IAM federation availability, see [Regional availability for TIP for IAM federation](id_roles_providers_tip_federation.md#id_roles_providers_tip_federation_regional_availability).

**Topics**
+ [Why use TIP](#id_roles_providers_tip_why)
+ [How TIP works](#id_roles_providers_tip_how)
+ [Understand where TIP context propagates](#id_roles_providers_tip_propagation)
+ [Choose how to establish TIP context](#id_roles_providers_tip_choose)
+ [Understand TIP context](#id_roles_providers_tip_context)
+ [Use TIP context](#id_roles_providers_tip_use)
+ [Related information](#id_roles_providers_tip_related)
+ [TIP for IAM federation](id_roles_providers_tip_federation.md)
+ [Trusted identity propagation with IAM Roles Anywhere](id_roles_providers_tip_rolesanywhere.md)
+ [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md)
+ [AWS services that support TIP](id_roles_providers_tip_services.md)

## Why use TIP
<a name="id_roles_providers_tip_why"></a>

TIP helps you:
+ Make access-control decisions based on the human user or workload that originated the workflow.
+ Carry selected identity attributes that [supported AWS services](id_roles_providers_tip_services.md) can use for authorization decisions.
+ Attribute CloudTrail events that contain TIP context to the human user or workload that originated the request.
+ Preserve TIP context through role assumptions within the same AWS organization, or within the same standalone account. This includes a TIP session assuming another role and a supported AWS service assuming an [IAM service role](id_roles_create_for-service.md).

**Important**  
TIP context does not grant permissions. IAM policies and supported AWS services determine how to use the context. The IAM principal remains subject to the applicable authorization policies.

## How TIP works
<a name="id_roles_providers_tip_how"></a>

1. You configure a supported identity source and any source-specific settings used to establish TIP context.

1. A human user or workload establishes a role session through IAM federation or IAM Roles Anywhere.

1. AWS validates the applicable source evidence and attaches the supported identity context when it creates the role session.

1. When a TIP session assumes another IAM role, AWS Security Token Service (AWS STS) applies the [TIP propagation boundary](#id_roles_providers_tip_propagation). If the role is within that boundary, AWS STS carries TIP context into the new role session. The caller cannot change the context.

1. When a supported AWS service uses its own credentials to assume an [IAM service role](id_roles_create_for-service.md), AWS STS applies the [same TIP propagation boundary](#id_roles_providers_tip_propagation) and reattaches TIP context when the service role is within it.

1. IAM policies and service-specific authorization models can use TIP context when the AWS service supports the applicable context.

1. AWS CloudTrail can record the context for requests to AWS services that support TIP context logging.

For example, a GitHub Actions workload can use OIDC federation to assume a shared IAM role. TIP can attach the repository, workflow, and run identity to the role session so supported authorization and CloudTrail records can identify the workload behind the role. For a complete IAM federation walkthrough, see [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md).

## Understand where TIP context propagates
<a name="id_roles_providers_tip_propagation"></a>

TIP sessions include context keys that identify an origin account. For IAM federation, this is the account that contains the IAM SAML or OIDC identity provider used to create the TIP session. If the origin account belongs to an AWS organization, the TIP session also includes that organization as the origin organization. If the origin account does not belong to an organization, the TIP session does not carry origin organization information.

**Important**  
For IAM federation, `aws:OriginIdentity/IdentityProviderAccount` identifies the origin account, and `aws:OriginIdentity/IdentityProviderOrgID` identifies the origin organization when that value is present. AWS STS uses these AWS-derived values to determine where TIP context can propagate.

The origin account and the account that owns the target role determine whether AWS STS carries TIP context. The following table shows the behavior.


| Origin account | Account that owns the target role | Result | 
| --- | --- | --- | 
| Belongs to an AWS organization | The origin account or another account in the same AWS organization | AWS STS carries TIP context into the new role session. | 
| Belongs to an AWS organization | A standalone account or an account in a different AWS organization | AWS STS drops TIP context at the time of the new role assumption. The role assumption can still succeed if the applicable IAM permissions and the target role's trust policy allow the request. | 
| Does not belong to an AWS organization | The origin account | AWS STS carries TIP context into the new role session. | 
| Does not belong to an AWS organization | Any other account | AWS STS drops TIP context at the time of the new role assumption. The role assumption can still succeed if the applicable IAM permissions and the target role's trust policy allow the request. | 

When a supported AWS service assumes an [IAM service role](id_roles_create_for-service.md) on your behalf, AWS STS uses the origin account and, when present, the origin organization in the TIP context to apply this boundary. AWS STS does not use the AWS service principal's account.

This boundary applies to role assumptions that create new session credentials. A direct request to an AWS resource in an account that belongs to another AWS organization uses the original session credentials and does not create another role session. For direct cross-organization resource access, IAM can evaluate [supported TIP condition keys](#id_roles_providers_tip_context) carried in the request when an applicable resource policy references those keys.

## Choose how to establish TIP context
<a name="id_roles_providers_tip_choose"></a>

The way that TIP context enters an AWS workflow depends on the identity source and integration. The following table lists the supported access paths and where to start.


| TIP path | Use this path when | Guidance | 
| --- | --- | --- | 
| IAM federation | A human user or workload creates a role session through a configured SAML or OpenID Connect (OIDC) identity provider. | [TIP for IAM federation](id_roles_providers_tip_federation.md) | 

## Understand TIP context
<a name="id_roles_providers_tip_context"></a>

TIP context uses a common set of core identity keys across the documented paths. `aws:OriginIdentity/Subject` identifies the human user or workload that started the request. `aws:OriginIdentity/SubjectType` indicates whether the Subject represents a `user` or `workload`. `aws:OriginIdentity/Issuer` identifies the source that issued the identity. `aws:OriginIdentity/IdentityProviderAccount` identifies the AWS account where the identity provider that established the origin identity is configured. When available, `aws:OriginIdentity/IdentityProviderOrgID` identifies the AWS organization that contains that account. These account and organization values determine the [TIP propagation boundary](#id_roles_providers_tip_propagation) for later role assumptions. For IAM federation and IAM Roles Anywhere, `aws:OriginIdentity/FederatedProviderArn` identifies the configured IAM identity provider or trust anchor used to establish the identity.

Additional context depends on the access path. IAM federation can include customer-selected SAML attributes or OIDC claims under `aws:TransactionContext/IdentityProvider/*`. Verify source-specific values, propagation behavior, and availability in the applicable setup guide.

For source-specific TIP context guidance, see:
+ **AWS IAM federation:** [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md)

## Use TIP context
<a name="id_roles_providers_tip_use"></a>

You can use TIP context for:
+ **Authorization:** Use supported TIP context keys in IAM policy conditions or service-specific authorization models while retaining the IAM principal boundary established by the applicable identity, trust, or resource policy.
+ **Audit:** Review TIP context in AWS CloudTrail to identify the human user or workload behind a request. For event fields, request paths, recipient accounts, and safeguards, see [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md).

**Optional outbound use.** If a workload calls an external service through IAM outbound identity federation, it can call the `GetWebIdentityToken` API operation to request a signed JSON Web Token that contains applicable TIP context. In the JWT, AWS STS represents applicable origin identity and transaction context as `origin_identity` and `transaction_context` claims under the `https://sts.amazonaws.com/` namespace. The JWT claim set is not a one-to-one copy of the customer-facing IAM context keys. TIP does not send context outside AWS automatically. For the outbound flow, see [Federating AWS identities to external services](id_roles_providers_outbound.md). For claim names and presence rules, see [TIP and Scope claims](id_roles_providers_outbound_token_claims.md#outbound-token-claims-tip-scope).

For current downstream support after credentials contain TIP context, see [AWS services that support TIP](id_roles_providers_tip_services.md).

## Related information
<a name="id_roles_providers_tip_related"></a>
+ [Trusted identity propagation in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html)
+ [TIP for IAM federation](id_roles_providers_tip_federation.md)
  + [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md)
  + [Configure TIP for an IAM identity provider](id_roles_providers_tip_federation_configure.md)
  + [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md)
  + [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md)
+ [Trusted identity propagation with IAM Roles Anywhere](id_roles_providers_tip_rolesanywhere.md)
+ [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md)
+ [AWS services that support TIP](id_roles_providers_tip_services.md)