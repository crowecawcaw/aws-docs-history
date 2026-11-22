

# Configure TIP for an IAM identity provider

Use this page to prepare a trusted identity propagation (TIP) configuration and choose the detailed procedure for an IAM SAML or OpenID Connect (OIDC) identity provider. For an overview of how TIP works with IAM federation, see [TIP for IAM federation](id_roles_providers_tip_federation.md).

**Topics**
+ [Before you configure TIP](#id_roles_providers_tip_federation_configure_before)
+ [Choose a configuration procedure](#id_roles_providers_tip_federation_configure_choose)
+ [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md)
+ [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md)
+ [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md)

## Before you configure TIP
<a name="id_roles_providers_tip_federation_configure_before"></a>

Before choosing a protocol procedure, plan the identity context, confirm the federation prerequisites, decide whether you need group-based access, and verify your permissions.

### Plan the identity context
<a name="id_roles_providers_tip_federation_configure_plan"></a>

TIP requires a Subject that identifies the human user or workload. Subject type and runtime claims are optional.
+ **Subject:** Choose a value that is stable and unique within the external identity provider. For SAML federation, `Subject/NameID` is recommended, but you can select another assertion field that contains one value. For OIDC federation, choose an appropriate token claim that contains one value.
+ **Subject type (optional):** Choose the fixed value `user` or `workload`, or select a SAML assertion field or OIDC token claim that supplies either `user` or `workload`.
+ **Runtime claims (optional):** Choose additional identity-provider claims that contain one value and that you want to carry for the current federation session.

AWS represents the resulting Subject, optional Subject type, and runtime claims as TIP context keys attached to the role session.

**Note**  
These context keys do not constitute your content. AWS recommends that you do not include personally identifying, confidential, or sensitive information in the configured Subject or runtime claims. Consider selecting an opaque, immutable identifier as the Subject. Configure only the context required for authorization or audit. For information about how AWS uses and processes this identity information, see [How TIP for IAM federation uses identity information](id_roles_providers_tip_federation.md#id_roles_providers_tip_federation_identity_info). For CloudTrail event recipients and governance controls, see [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md).

For context-key definitions, value sources, presence rules, mapping behavior, and limits, see [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md).

### Confirm the identity provider prerequisites
<a name="id_roles_providers_tip_federation_configure_prerequisites"></a>

TIP uses the standard SAML or OIDC provider and role trust requirements. Confirm that you have the information required to create the provider or that the existing provider meets those requirements:
+ **SAML:** Review the [SAML identity provider requirements](id_roles_providers_create_saml.md). Configure the assertion to include the selected Subject source and any attributes selected as runtime claims.
+ **OIDC:** Review the [OIDC identity provider requirements](id_roles_providers_create_oidc.md). Configure the token to include the selected Subject claim and any claims selected as runtime claims.

**Important**  
Before enabling TIP, confirm that every configured source meets the [source-value requirements](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_meet_source_value_requirements). After you enable TIP on an IAM identity provider that is already in use, any federation request with a missing required source or a present invalid mapped value fails with `InvalidIdentityToken`. An absent optional runtime claim is omitted from the session. If the combined session content is too large, the request fails with `PackedPolicyTooLarge`. To roll back the configuration, follow [Remove TIP from a SAML provider](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-remove-tip-from-a-saml-provider) or [Remove TIP from an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md#id_roles_providers_tip_federation_configure_oidc-remove-tip-from-an-oidc-provider).

### Decide whether to allow group-based access
<a name="id_roles_providers_tip_federation_configure_groups"></a>

If a supported AWS service needs to make access decisions based on a human user's group membership, configure group-based access. This associates an IAM Identity Center instance with the IAM identity provider. The external SAML or OIDC identity provider remains the authentication source.

For instance selection, creation, System for Cross-domain Identity Management (SCIM) provisioning, permissions, and verification, see [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md).

### Confirm permissions
<a name="id_roles_providers_tip_federation_configure_permissions"></a>

The following table shows the IAM action required to create a provider with TIP or manage TIP on an existing provider.


| Protocol | Create a provider with TIP | Add, change, or remove TIP on a provider | 
| --- | --- | --- | 
| SAML | `iam:CreateSAMLProvider` | `iam:UpdateSAMLProvider` | 
| OIDC | `iam:CreateOpenIDConnectProvider` | `iam:UpdateOpenIDConnectProvider` | 

During initial federation, the target role trust policy must allow `sts:AssumeRoleWithSAML` or `sts:AssumeRoleWithWebIdentity`. AWS STS supplies an implicit `Allow` for `sts:SetContext` in the role trust policy evaluation, so customers do not add that permission to the trust policy. If the request uses an AWS STS VPC endpoint whose endpoint policy has a restrictive Allow list, the endpoint policy must allow `sts:SetContext` and the applicable federation operation. SCPs, permissions boundaries, and session policies do not apply to initial federation because the caller is not an IAM user or role. For the complete request-path model, see [Update restrictive Allow policies](id_roles_providers_tip_federation_policies.md#id_roles_providers_tip_federation_policies_update_restrictive_allow_policies).

Group-based access also requires the IAM Identity Center permissions for the selected setup path. See [Permissions for each configuration action](id_roles_providers_tip_federation_configure_group_access.md#id_roles_providers_tip_federation_configure_group_access-permissions-for-each-configuration-action).

Identity policies and AWS Organizations policies can further restrict who configures TIP, which issuers they configure, and which IAM Identity Center instance they associate. For policy requirements and examples, see [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md#id_roles_providers_tip_federation_policies_control_tip_configuration).

## Choose a configuration procedure
<a name="id_roles_providers_tip_federation_configure_choose"></a>

Use the procedure for your identity-provider protocol:
+ [Configure TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md)
+ [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md)

For a worked SAML example that connects provider configuration to IAM policy evaluation and AWS CloudTrail verification, see [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md).