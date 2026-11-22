

# Getting started with TIP for IAM federation

In this tutorial, you configure TIP on an IAM SAML identity provider and test it with the human user `user@example.com`. When the user federates to assume `TIPExampleRole`, AWS STS attaches the user's Subject and `department` value, `Engineering`, to the role session. An identity-based policy permits the session to read a specific Amazon S3 object only when the attached TIP context matches the policy conditions. You verify that the request succeeds and that the `AssumeRoleWithSAML` event in AWS CloudTrail contains the same context.

For an overview of the IAM federation path and how it preserves identity context through supported workflows, see [TIP for IAM federation](id_roles_providers_tip_federation.md).

This tutorial uses SAML federation. TIP also supports OpenID Connect (OIDC) federation. For the corresponding OIDC provider configuration and verification procedures, see [Configure TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md).

**Important**  
Use a separate test SAML provider and test role for this tutorial. Do not first enable TIP on a provider used for production access. If a required Subject or mapped Subject type value is missing or invalid, AWS STS rejects the federation request. If you must test an existing provider, follow [Add TIP to an existing SAML provider](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-add-tip-to-an-existing-saml-provider), confirm its assertions meet the source-value requirements, and be prepared to [remove TIP](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-remove-tip-from-a-saml-provider) if federation fails.

## How this tutorial works
<a name="id_roles_providers_tip_federation_getting_started-how-this-tutorial-works"></a>

This tutorial configures and tests TIP in six steps:

1. [**Prepare the SAML identity values.**](#id_roles_providers_tip_federation_getting_started-prepare-the-saml-identity-values) Configure the external identity provider to send `user@example.com` in `Subject/NameID` and `Engineering` in the `department` attribute. These are the values that TIP carries into the AWS role session.

1. [**Configure TIP on the IAM SAML provider.**](#id_roles_providers_tip_federation_getting_started-configure-tip-on-the-iam-saml-provider) Configure `Subject/NameID` as the Subject source, set the Subject type to `user`, and map the `department` attribute to the runtime-claim target key `department`. IAM stores this configuration on `ExampleProvider`.

1. [**Configure the IAM role and access policy.**](#id_roles_providers_tip_federation_getting_started-configure-the-iam-role-and-access-policy) Configure `TIPExampleRole` to trust `ExampleProvider`. Attach a policy that permits `s3:GetObject` only when the Subject, Issuer, Subject type, and department in the role session match the example values. If federation uses an AWS STS VPC endpoint, check that its endpoint policy does not block `sts:SetContext`.

1. [**Create the TIP session.**](#id_roles_providers_tip_federation_getting_started-create-the-tip-enabled-role-session) Sign in as `user@example.com` through the external SAML identity provider. AWS STS validates the SAML assertion, creates a session for `TIPExampleRole`, and attaches the configured TIP context.

1. [**Test authorization.**](#id_roles_providers_tip_federation_getting_started-test-authorization) Use the role session to retrieve `s3://example-reports/reports/example.txt`. IAM evaluates the TIP context in the session against the identity-based policy attached to the role.

1. [**Verify the propagated context.**](#id_roles_providers_tip_federation_getting_started-verify-the-propagated-context) Open the `AssumeRoleWithSAML` event in the AWS CloudTrail trail log. Confirm that the recorded Subject, Issuer, provider ARN, Subject type, and department match the tutorial values.

If a step does not produce the expected result, see [Troubleshoot TIP configuration](#id_roles_providers_tip_federation_getting_started-troubleshoot-tip-configuration).

## Prepare the SAML identity values
<a name="id_roles_providers_tip_federation_getting_started-prepare-the-saml-identity-values"></a>

The following table shows each identity value, where it comes from, and the synthetic value used in the tutorial.


| Identity value | Source | Example value | 
| --- | --- | --- | 
| Subject | Subject/NameID in the SAML assertion | user@example.com | 
| Subject type | Fixed value in the TIP configuration | user | 
| Runtime claim | SAML assertion attribute department, mapped to target key department | Engineering | 
| Issuer | AWS derives the value from the signing key used to validate the SAML assertion | 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef | 

Use a test human user whose SAML assertion values you can inspect. Configure the external SAML identity provider to send `user@example.com` in `Subject/NameID` and one `department` attribute with the value `Engineering`.

Replace the identity values and SAML Issuer with values from your environment. Use the supported method in [Identify an originator with Subject and Issuer](id_roles_providers_tip_federation_policies.md#id_roles_providers_tip_federation_policies_identify_an_originator_with_subject_and_issuer) to obtain the exact SAML Issuer value for your provider. Do not calculate the value independently.

For identity-context planning and value definitions, see [Before you configure TIP](id_roles_providers_tip_federation_configure.md#id_roles_providers_tip_federation_configure_before) and [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md).

## Configure TIP on the IAM SAML provider
<a name="id_roles_providers_tip_federation_getting_started-configure-tip-on-the-iam-saml-provider"></a>

This example uses an IAM SAML provider named `ExampleProvider`. Use the detailed SAML procedure to create the provider with TIP or add TIP to an existing provider:
+ [Configure TIP when creating a SAML provider](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-configure-tip-when-creating-a-saml-provider)
+ [Add TIP to an existing SAML provider](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-add-tip-to-an-existing-saml-provider)

The linked procedures provide AWS IAM console, AWS CLI, and AWS SDK for Python (Boto3) paths. Use these settings for the tutorial:
+ Select `Subject/NameID` as the Subject source.
+ Configure the fixed Subject type `user`.
+ Map the SAML attribute `department` to the target key `department`.
+ Do not configure group-based access.

After saving, open `ExampleProvider` in the AWS IAM console and choose the **Identity propagation** tab. **Propagation status** must be **Configured**. The saved Subject must be `Subject/NameID`, Subject type must be the fixed value `user`, and the runtime mapping must show `department` as both the source and target. A missing or different value means that IAM did not save the example configuration or that you opened a different provider. Correct the configuration by using the SAML procedure, and then verify it again.

For AWS CLI or SDK verification, follow [Verify the TIP configuration](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-verify-the-tip-configuration). The returned configuration must contain the same Subject, Subject type, and runtime mapping. A missing or different value means that the saved configuration does not match the tutorial; correct the request and verify it again.

## Configure the IAM role and access policy
<a name="id_roles_providers_tip_federation_getting_started-configure-the-iam-role-and-access-policy"></a>

Create or identify an IAM role named `TIPExampleRole`. Its trust policy must allow SAML federation through `ExampleProvider`. TIP does not replace the standard role trust policy required for SAML federation. For the role procedure, see [Create a role for SAML 2.0 federation (console)](id_roles_create_for-idp_saml.md).

Create the test object `s3://example-reports/reports/example.txt`, replacing the bucket and object names with a resource from your environment. Confirm that Amazon S3 can use TIP context in IAM policies in [AWS services that support TIP](id_roles_providers_tip_services.md).

Attach an identity-based policy to `TIPExampleRole` that permits the test action only for the example identity context. The following policy uses the same identity values and Amazon S3 resource defined in the tutorial.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadExampleReportWithTIP",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-reports/reports/example.txt",
      "Condition": {
        "StringEquals": {
          "aws:OriginIdentity/Subject": "user@example.com",
          "aws:OriginIdentity/Issuer": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
          "aws:OriginIdentity/SubjectType": "user",
          "aws:TransactionContext/IdentityProvider/department": "Engineering"
        }
      }
    }
  ]
}
```

Before testing, inspect the permissions for `TIPExampleRole`. The policy must allow `s3:GetObject` on the exact test object, and each condition value must match the example. A missing or different value prevents this Allow from matching the request. Also confirm that no applicable policy explicitly denies the action.

Eligible TIP context from an IAM SAML provider receives an implicit `Allow` for `sts:SetContext` in the role trust policy evaluation. If the federation request uses an AWS STS VPC endpoint whose endpoint policy has a restrictive Allow list, the endpoint policy must include `sts:SetContext` and `sts:AssumeRoleWithSAML`. SCPs, permissions boundaries, and session policies do not apply to initial federation because the caller is not an IAM user or role. For the complete policy model, see [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md). For restrictive policy details, see [Update restrictive Allow policies](id_roles_providers_tip_federation_policies.md#id_roles_providers_tip_federation_policies_update_restrictive_allow_policies). For later role assumptions, see the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation).

## Create the TIP session
<a name="id_roles_providers_tip_federation_getting_started-create-the-tip-enabled-role-session"></a>

Use your existing SAML federation flow to sign in as `user@example.com` and assume `TIPExampleRole` through `ExampleProvider`. The SAML assertion must contain `user@example.com` in `Subject/NameID` and one `department` attribute with the value `Engineering`.

Federation must succeed and create a session for `TIPExampleRole`. If federation fails, inspect the federation response and SAML assertion. A missing Subject, multiple values for a mapped field, or a role trust policy that does not allow `ExampleProvider` prevents AWS STS from creating the expected session.

## Test authorization
<a name="id_roles_providers_tip_federation_getting_started-test-authorization"></a>

Use the `TIPExampleRole` session to retrieve `s3://example-reports/reports/example.txt`.

The request must return the object. An `AccessDenied` response means that the policy did not allow the action or an applicable policy explicitly denied it. Before changing the policy, compare the role, action, resource, Subject, Issuer, Subject type, and department values with the tutorial values.

To test that the TIP conditions restrict access, repeat the request with a session whose Subject or department differs while keeping other test permissions unchanged. The request must return `AccessDenied` when no other policy grants access to the object. If it succeeds, another policy grants access or the intended TIP conditions do not apply to the request.

## Verify the propagated context
<a name="id_roles_providers_tip_federation_getting_started-verify-the-propagated-context"></a>

You need an [AWS CloudTrail trail that records management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html) in the AWS Region that processes the federation request and permission to inspect its delivered logs. This procedure verifies only the initial SAML federation event. For other request paths, event recipients, disclosure, retention, and safeguards, see [Logging TIP activity with AWS CloudTrail](id_roles_providers_tip_cloudtrail.md).

In the delivered trail log, open the successful `AssumeRoleWithSAML` event for the example session. Inspect these fields:
+ `userIdentity.onBehalfOf.subject` must be `user@example.com`.
+ `userIdentity.onBehalfOf.issuer` must be the SAML Issuer used in the policy.
+ `userIdentity.onBehalfOf.federatedProviderArn` must equal the IAM SAML provider ARN used for federation. In this example, the value is `arn:aws:iam::111122223333:saml-provider/ExampleProvider`.
+ `userIdentity.onBehalfOf.subjectType` must be `user`.
+ `userIdentity.transactionContext.IdentityProvider.department` must be `Engineering`.

The following shortened example is based on a successful `AssumeRoleWithSAML` event delivered to an AWS CloudTrail trail. Identifiers, timestamps, and runtime-claim values are synthetic.

```json
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "SAMLUser",
    "onBehalfOf": {
      "federatedProviderArn": "arn:aws:iam::111122223333:saml-provider/ExampleProvider",
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  },
  "eventTime": "2026-11-10T18:05:30Z",
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRoleWithSAML",
  "awsRegion": "us-east-1",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management"
}
```

For SAML federation, `issuer` is the hash of the public key in the provider's metadata XML that AWS used to validate the assertion.

If `userIdentity.onBehalfOf` or a required member is absent, the event does not contain the expected TIP context. Confirm that **Propagation status** is **Configured**, that the event identifies `ExampleProvider`, and that the SAML assertion contains the tutorial Subject. A different value means that the session used a different identity, provider, or saved mapping. If `department` is missing while `onBehalfOf` is present, confirm that the saved runtime mapping uses `department` as both the source and target and that the assertion contains the attribute with one value.

## Troubleshoot TIP configuration
<a name="id_roles_providers_tip_federation_getting_started-troubleshoot-tip-configuration"></a>

If a TIP step fails, use the detailed guidance for that part of the workflow:
+ If IAM does not save the expected Subject, Subject type, or runtime mapping, follow the verification procedure for your provider:
  + [Verify TIP for a SAML provider](id_roles_providers_tip_federation_configure_saml.md#id_roles_providers_tip_federation_configure_saml-verify-the-tip-configuration)
  + [Verify TIP for an OIDC provider](id_roles_providers_tip_federation_configure_oidc.md#id_roles_providers_tip_federation_configure_oidc-verify-the-tip-configuration)
+ If federation does not create the role session, use the existing federation troubleshooting guidance for your SAML or OIDC provider. For this tutorial, see [Troubleshoot SAML federation with IAM](troubleshoot_saml.md).
+ If an AWS service request returns `AccessDenied`, see [Verify and troubleshoot policy behavior](id_roles_providers_tip_federation_policies.md#id_roles_providers_tip_federation_policies_verify_and_troubleshoot_policy_behavior).
+ If the federation event does not contain the expected TIP context, compare the event with the saved provider configuration and the SAML assertion or OIDC token. For the SAML example, repeat [Verify the propagated context](#id_roles_providers_tip_federation_getting_started-verify-the-propagated-context).
+ For group-resolution failures, see [Configure group-based access for TIP](id_roles_providers_tip_federation_configure_group_access.md).

After correcting the configuration, repeat the failed step and confirm that it produces the expected result.