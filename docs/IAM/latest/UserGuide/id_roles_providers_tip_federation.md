

# TIP for IAM federation

Trusted identity propagation (TIP) for IAM federation attaches identity context to role sessions created through SAML or OpenID Connect (OIDC) federation. You configure TIP on an IAM identity provider by selecting a Subject source, an optional Subject type, and optional runtime claims.

For how TIP works across supported identity sources, see [Trusted identity propagation with IAM](id_roles_providers_tip.md). This page explains the IAM federation-specific configuration, propagation, authorization, and audit behavior.

**Topics**
+ [How TIP for IAM federation uses identity information](#id_roles_providers_tip_federation_identity_info)
+ [Regional availability](#id_roles_providers_tip_federation_regional_availability)
+ [Why use TIP for IAM federation](#id_roles_providers_tip_federation_why)
+ [How TIP for IAM federation works](#id_roles_providers_tip_federation_how)
+ [Understand TIP context from IAM federation](#id_roles_providers_tip_federation_context)
+ [Use TIP with group-based access](#id_roles_providers_tip_federation_groups)
+ [Authorization](#id_roles_providers_tip_federation_authorization)
+ [Auditing](#id_roles_providers_tip_federation_auditing)
+ [Related information](#id_roles_providers_tip_federation_related)
+ [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md)
+ [Configure TIP for an IAM identity provider](id_roles_providers_tip_federation_configure.md)
+ [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md)
+ [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md)

## How TIP for IAM federation uses identity information
<a name="id_roles_providers_tip_federation_identity_info"></a>

When you enable TIP for IAM federation, you select one SAML assertion field or OIDC token claim as the Subject. The Subject identifies the human user or workload. You can optionally configure a fixed or mapped Subject type and map up to 10 additional values as runtime claims. For complete definitions and context keys, see [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md).

**Note**  
You can use the identifier and attributes to manage access to AWS resources through IAM policies and data grants. AWS uses them to authorize requests, record activity in AWS CloudTrail and service logs, calculate fees, and enable you to allocate costs to users. The identifier and attributes travel with requests to the AWS accounts and Regions your federated users access. AWS may also process them in default Regions required to fulfill a request.  
These context keys do not constitute your content. AWS recommends that you do not include personally identifying, confidential, or sensitive information in the configured Subject or runtime claims. Consider selecting an opaque, immutable identifier as the Subject.

## Regional availability
<a name="id_roles_providers_tip_federation_regional_availability"></a>

TIP for IAM federation is available in supported Commercial AWS Regions, AWS China Regions, AWS GovCloud (US) Regions, and the AWS European Sovereign Cloud (Germany) Region.

## Why use TIP for IAM federation
<a name="id_roles_providers_tip_federation_why"></a>

TIP for IAM federation applies TIP to role sessions created through SAML or OIDC federation. You can carry selected identity-provider claims from the current federation session and optionally use AWS IAM Identity Center as the directory for supported group-based access without changing the IAM federation path.

## How TIP for IAM federation works
<a name="id_roles_providers_tip_federation_how"></a>

1. You configure TIP when you create an IAM SAML or OIDC identity provider or add TIP to an existing provider. You choose the Subject and any optional Subject type or runtime claims.

1. When a human user or workload federates, AWS STS validates the SAML assertion or OIDC token and attaches the configured identity context to the role session.

1. When a TIP session assumes another IAM role, AWS STS applies the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation). If the target role is within that boundary, the new role session carries TIP context. If the target role is outside the boundary, the role assumption can still succeed, but the new role session does not contain TIP context.

1. When a supported AWS service uses its own credentials to assume an [IAM service role](id_roles_create_for-service.md), AWS STS applies the [same TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) before reattaching TIP context to the service role session.

1. IAM policies and service-specific authorization models can use the context to authorize access to supported AWS services.

1. AWS CloudTrail can record the context for requests to AWS services that support TIP context logging.

**Important**  
Before you enable TIP on an IAM identity provider that is already in use, confirm that the identity provider sends every required Subject and mapped Subject type value. A missing required source or a present invalid mapped value causes AWS STS to reject the federation request with `InvalidIdentityToken`. An absent optional runtime claim is omitted from the session. For the complete rules, see [Meet source-value requirements](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_meet_source_value_requirements).

For a worked SAML example, see [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md). For setup instructions, see [Configure TIP for an IAM identity provider](id_roles_providers_tip_federation_configure.md). For current IAM policy and AWS CloudTrail support by AWS service, see [AWS services that support TIP](id_roles_providers_tip_services.md).

## Understand TIP context from IAM federation
<a name="id_roles_providers_tip_federation_context"></a>

TIP context from IAM federation includes core origin identity and can include identity-provider runtime claims or directory references for group-based access. For key definitions, value sources, presence rules, mapping behavior, and limits, see [Understand the context established through IAM federation](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_understand_the_context_established_through_iam_federation).

## Use TIP with group-based access
<a name="id_roles_providers_tip_federation_groups"></a>

TIP does not require IAM Identity Center. If a supported AWS service needs to make access decisions based on a human user's group membership, you can associate an IAM Identity Center instance with the IAM identity provider.

In the AWS IAM console, select **Allow granting permissions to groups** while configuring TIP. The external SAML or OIDC identity provider remains the authentication source. IAM Identity Center provides the directory that the supported AWS service uses to resolve the propagated Subject and group membership.

For instance selection, System for Cross-domain Identity Management (SCIM) provisioning, and verification, see [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md).

## Authorization
<a name="id_roles_providers_tip_federation_authorization"></a>

TIP adds identity context to the existing AWS authorization process. It does not grant permissions by itself. Policies can control:
+ Who can add, change, or remove TIP configuration.
+ Whether AWS STS can attach TIP context to a role session.
+ Whether a caller using credentials that carry TIP context can assume particular IAM roles or access particular AWS resources.

When a policy identifies a specific originator, evaluate Subject together with Issuer. Before using TIP context in a policy for an AWS service, confirm that the credentials evaluated by the policy carry TIP context.

For policy requirements, governance controls, and examples, see [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md). For current AWS service support, see [AWS services that support TIP](id_roles_providers_tip_services.md).

## Auditing
<a name="id_roles_providers_tip_federation_auditing"></a>

AWS CloudTrail can record TIP context for requests made with credentials that carry TIP context when the AWS service supports TIP context logging. Core origin identity appears in `userIdentity.onBehalfOf`. Runtime claims appear in `userIdentity.transactionContext.IdentityProvider`. The IAM role remains the AWS principal in the event.

For CloudTrail event fields, request paths, recipient accounts, safeguards, and TIP logging examples, see [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md).

## Related information
<a name="id_roles_providers_tip_federation_related"></a>
+ [Trusted identity propagation with IAM](id_roles_providers_tip.md)
+ [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md)
+ [Configure TIP for an IAM identity provider](id_roles_providers_tip_federation_configure.md)
  + [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md)
  + [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md)
  + [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md)
+ [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md)
+ [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md)
+ [AWS services that support TIP](id_roles_providers_tip_services.md)
+ [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md)