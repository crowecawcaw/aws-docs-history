

# Logging TIP activity with AWS CloudTrail

AWS CloudTrail supports TIP context logging for [AWS services that support TIP](id_roles_providers_tip_services.md). The recorded context helps customers identify the human user or workload that initiated a request.

This page explains how CloudTrail records TIP identity context, where that context appears within a CloudTrail event, and whether the caller account or target account receives the resulting event. The page also explains how logging changes when TIP context first enters a role session, when that session assumes another role, when an AWS service assumes a role on a customer's behalf, and when requests cross account boundaries.

## Before you enable TIP
<a name="id_roles_providers_tip_cloudtrail-before-you-enable-tip"></a>

**Note**  
For requests to AWS services that support TIP context logging, AWS CloudTrail records the configured Subject and any runtime claims present in the TIP context. These values can contain personally identifying, confidential, or sensitive information. The context keys do not constitute your content. AWS recommends that you do not include personally identifying, confidential, or sensitive information in the configured Subject or runtime claims.

Review these logging implications before you enable TIP:
+ **Choose the appropriate context:** Configure one Subject source and the optional runtime mappings required by your use case.
+ **Review CloudTrail access:** Control who can view Event History, trail log files, and CloudTrail Lake event data stores.
+ **Review cross-account disclosure:** TIP context can appear in CloudTrail records owned by another AWS organization. When a TIP session assumes a role across the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation), the target account's successful `AssumeRole` event records the caller's TIP context even though AWS STS drops that context from the resulting role session. When TIP session credentials are used to directly access a cross-organization resource, a [supported AWS service](id_roles_providers_tip_services.md) event in the target account can also record the TIP context.
+ **Apply authorization controls:** AWS STS automatically enforces the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) for role assumptions. Use [applicable IAM policies and AWS Organizations guardrails](id_roles_providers_tip_federation_policies.md) to restrict role assumptions within that boundary and to apply controls for direct cross-account resource access.

## Find TIP identity context in a CloudTrail event
<a name="id_roles_providers_tip_cloudtrail-find-tip-identity-context-in-a-cloudtrail-event"></a>

CloudTrail records TIP identity context in sections within the `userIdentity` element of a CloudTrail event. For the IAM federation path, CloudTrail records customer-configured runtime claims only when those claims are attached to the TIP session. The following table shows the complete CloudTrail JSON path for each IAM federation context category.


| TIP context | Location within `userIdentity` in the CloudTrail event | What it identifies | 
| --- | --- | --- | 
| [Core origin identity](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_identify_the_originator_and_identity_provider) | `userIdentity.onBehalfOf` | The human user or workload represented by the TIP session and the external identity provider used for federation. | 
| [Identity provider runtime context](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_map_identity_provider_runtime_claims) | `userIdentity.transactionContext.IdentityProvider` | For IAM federation only, the applicable runtime claims that the customer configured and that were attached to the TIP session, such as department, team, or cost center. This section is absent when no applicable runtime claims are attached. | 

### Identify when AWS STS drops TIP context
<a name="id_roles_providers_tip_cloudtrail-identify-when-aws-sts-drops-tip-context"></a>

When a TIP session assumes another role in a different AWS organization, AWS STS drops TIP context from the new role session. The calling TIP session retains its TIP context. AWS STS also drops TIP context from the new role session when the role assumption crosses between an AWS organization and a standalone account, or between different standalone accounts. For more information, see [Understand where TIP context propagates](id_roles_providers_tip.md#id_roles_providers_tip_propagation).

When AWS STS drops TIP context, the target account's CloudTrail event for the successful `AssumeRole` request includes `additionalEventData.trustedIdentityPropagationSuppressed` with the Boolean value `true`. The target account is the account that owns the role being assumed. The field is absent when AWS STS does not drop TIP context.

Although AWS STS drops TIP context from the new role session, the target-account CloudTrail event records the TIP context that AWS STS evaluated for the `AssumeRole` request. The event includes `userIdentity.onBehalfOf` and any evaluated `userIdentity.transactionContext` values. Requests made with the new role session do not record the dropped TIP context. For an example, see [Cross-boundary role assumption](#id_roles_providers_tip_cloudtrail-cross-boundary-role-assumption).

## Understand logging by request path
<a name="id_roles_providers_tip_cloudtrail-understand-logging-by-request-path"></a>

The request path determines whether the caller account or target account receives the CloudTrail event and which sections of the event record TIP context. The following table shows what you configure, which event you inspect, and where TIP context appears in the event.


| Request path | What you configure | CloudTrail event to inspect | TIP context in the CloudTrail event | 
| --- | --- | --- | --- | 
| Initial IAM federation | Enable TIP for [IAM SAML federation](id_roles_providers_tip_federation_configure_saml.md) or [IAM OIDC federation](id_roles_providers_tip_federation_configure_oidc.md). Configure the [core origin identity](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_identify_the_originator_and_identity_provider) and any optional [identity provider runtime context](id_roles_providers_tip_federation_context_keys.md#id_roles_providers_tip_federation_context_keys_map_identity_provider_runtime_claims). | A successful `AssumeRoleWithSAML` or `AssumeRoleWithWebIdentity` event in the target account | The `userIdentity.onBehalfOf` section records the core origin identity. If configured runtime claims were present in the SAML assertion or OIDC token and attached to the TIP session, `userIdentity.transactionContext.IdentityProvider` records those claims. | 
| Caller invokes an AWS service API in the same account | Use credentials that carry TIP context to call an [AWS service that supports TIP context logging](id_roles_providers_tip_services.md). | The AWS service event in the caller account | The `userIdentity.onBehalfOf` section records the core origin identity carried by the credentials. For an IAM federation session, `userIdentity.transactionContext.IdentityProvider` records configured runtime claims only when those claims are attached to the TIP session. | 
| Later role assumption within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) | Allow the TIP session to call `sts:AssumeRole`. No new TIP source configuration is required. | The successful `AssumeRole` event and subsequent supported events in the target account | The new role session carries TIP context. The `AssumeRole` event and subsequent supported events record the core origin identity in `userIdentity.onBehalfOf`. For IAM federation, configured runtime claims appear in `userIdentity.transactionContext.IdentityProvider` when they are attached to the TIP session. `additionalEventData.trustedIdentityPropagationSuppressed` is absent. | 
| AWS service assumes an IAM service role | Use an AWS service workflow that carries TIP context into an [IAM service role](id_roles_create_for-service.md). Review policies that govern `sts:SetContext` and the primary AWS STS operation. | The target-account copy of the successful `AssumeRole` event and subsequent events made with the service role credentials | The `userIdentity.onBehalfOf` section in the target-account copy records the core origin identity attached to the service role credentials. For the IAM federation path, `userIdentity.transactionContext.IdentityProvider` records configured runtime claims only when those claims are reattached. | 
| Direct role assumption across the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) | Configure the target role's trust policy to allow `sts:AssumeRole`. No customer configuration can carry TIP context across this boundary at launch. | The successful `AssumeRole` event in the caller account and the target account. Also inspect subsequent supported events made with the resulting credentials in the target account. | The caller-account event records the TIP context from the caller's TIP session. The target-account event records the TIP context evaluated during the request and sets `additionalEventData.trustedIdentityPropagationSuppressed` to `true`. The resulting role session and subsequent events made with its credentials do not contain TIP context. | 
| Direct cross-account resource access | Configure the target resource policy and any TIP conditions. | The successful AWS service event in the target account | No new role session is created. The `userIdentity.onBehalfOf` section in the target-account copy records the core origin identity carried by the TIP session credentials. For the IAM federation path, `userIdentity.transactionContext.IdentityProvider` records configured runtime claims only when those claims are attached to the TIP session. | 

For context categories and field definitions that apply to IAM federation, see [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md). For current AWS service support, see [AWS services that support TIP](id_roles_providers_tip_services.md).

### Understand denied federation requests
<a name="id_roles_providers_tip_cloudtrail-understand-denied-federation-requests"></a>

When authorization denies an initial `AssumeRoleWithSAML` or `AssumeRoleWithWebIdentity` request, CloudTrail records an `AccessDenied` event in the account that owns the IAM identity provider and target role. The event includes `userIdentity.onBehalfOf` and any `userIdentity.transactionContext` values that AWS STS evaluated. This applies, for example, when the role trust policy does not allow the request or an applicable policy explicitly denies `sts:SetContext`.

When AWS STS rejects the assertion or token with `InvalidIdentityToken` because a required or mapped claim is invalid, CloudTrail does not record an event for the rejected federation request.

### Understand denied cross-account requests
<a name="id_roles_providers_tip_cloudtrail-understand-denied-cross-account-requests"></a>

A successful cross-boundary `AssumeRole` request with suppressed TIP context is not a denied request. The request completes without an `errorCode`, and the target-account CloudTrail event sets `additionalEventData.trustedIdentityPropagationSuppressed` to `true`. The resulting role session does not contain TIP context.

When authorization denies a cross-account `AssumeRole` request, CloudTrail records an `AccessDenied` event in the caller account but not in the target account that owns the role. The target account therefore receives neither a CloudTrail copy of the denied request nor TIP context from that request.

For a denied direct cross-account resource request, CloudTrail records the denied request in the caller account. The target account does not receive TIP context from the denied request.

## Control access to TIP context
<a name="id_roles_providers_tip_cloudtrail-control-access-to-tip-context"></a>

You can use different controls to limit which identity context is propagated, who can read recorded context, and which destinations can receive it. The following table shows the control for each customer use case and its effect.


| Customer use case | Control | Effect | 
| --- | --- | --- | 
| Avoid propagating unnecessary identity context | Configure only the Subject and optional runtime context required for authorization or audit. | Role sessions and CloudTrail events do not contain additional customer-selected context that was not configured. | 
| Limit who can read TIP context in CloudTrail | Use IAM permissions to control access to Event History, Amazon S3 access policies to control trail log files, and event data store resource policies to control CloudTrail Lake. For examples, see [Identity-based policy examples for AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_id-based-policy-examples.html), [Sharing CloudTrail log files between AWS accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-sharing-logs.html), and [AWS CloudTrail resource-based policy examples](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html). | Only authorized principals can read the recorded TIP context. | 
| Prevent TIP context from entering a new role session outside the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) | No customer configuration is required. AWS STS applies the boundary when it creates the new role session. | AWS STS drops TIP context. The role assumption can still succeed if `sts:AssumeRole` is otherwise authorized. The successful target-account CloudTrail event sets `additionalEventData.trustedIdentityPropagationSuppressed` to `true`. | 
| Block context attachment within the [TIP propagation boundary](id_roles_providers_tip.md#id_roles_providers_tip_propagation) | Use an applicable policy to deny `sts:AssumeRole` or explicitly deny `sts:SetContext`. | The complete role-assumption request fails. AWS STS does not create the new role session. | 
| Restrict direct cross-account access to a resource | Scope the resource-policy `Principal` and use applicable TIP context conditions, such as Subject and Issuer. | The resource accepts requests only from the intended principal and TIP identity context. No new role session is created. | 

For complete policy examples and evaluation behavior, see [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md).

## IAM-specific logging examples
<a name="id_roles_providers_tip_cloudtrail-validate-the-logging-examples"></a>

The following shortened examples show IAM-specific request paths and account-copy behavior. For canonical complete CloudTrail event examples, see [Understanding CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html).

Each example includes only the fields needed to explain its IAM-specific request path. A complete CloudTrail event contains additional fields.

### Initial IAM federation
<a name="id_roles_providers_tip_cloudtrail-initial-iam-federation"></a>

The following example represents the initial SAML federation event. The equivalent OIDC event uses `AssumeRoleWithWebIdentity` and the OIDC Issuer and provider ARN.

```json
{
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRoleWithSAML",
  "recipientAccountId": "111122223333",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
      "federatedProviderArn": "arn:aws:iam::111122223333:saml-provider/ExampleProvider"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

### Same-account AWS service request
<a name="id_roles_providers_tip_cloudtrail-same-account-aws-service-request"></a>

The following example represents an Amazon S3 request made with credentials that carry TIP context in the same account.

```json
{
  "eventSource": "s3.amazonaws.com",
  "eventName": "GetObject",
  "recipientAccountId": "111122223333",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

### Later role assumption
<a name="id_roles_providers_tip_cloudtrail-later-role-assumption"></a>

The following example represents a TIP session directly assuming another role in the same account.

```json
{
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRole",
  "recipientAccountId": "111122223333",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

### Same-organization cross-account role assumption
<a name="id_roles_providers_tip_cloudtrail-cross-account-role-assumption"></a>

The following caller-account copy represents a TIP session in account `111122223333` assuming a role in account `444455556666`. Both accounts belong to the same AWS organization, so AWS STS carries TIP context into the resulting role session.

```json
{
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRole",
  "recipientAccountId": "111122223333",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

The following target-account copy represents the same successful `AssumeRole` request.

```json
{
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRole",
  "recipientAccountId": "444455556666",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

`additionalEventData.trustedIdentityPropagationSuppressed` is absent because AWS STS carried TIP context into the resulting role session.

### Cross-boundary role assumption
<a name="id_roles_providers_tip_cloudtrail-cross-boundary-role-assumption"></a>

The following CloudTrail event is the target-account copy of a successful `AssumeRole` request. CloudTrail records this event in account `777788889999`, which owns the role being assumed. The caller uses a TIP session from account `111122223333`. The two accounts belong to different AWS organizations, so AWS STS drops TIP context when it creates the new role session.

```json
{
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRole",
  "recipientAccountId": "777788889999",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  },
  "additionalEventData": {
    "trustedIdentityPropagationSuppressed": true
  }
}
```

The event records the TIP context evaluated during the role assumption. The resulting role session does not contain TIP context, so subsequent requests made with its credentials do not record this origin identity or runtime context.

### Direct cross-account resource access
<a name="id_roles_providers_tip_cloudtrail-direct-cross-account-resource-access"></a>

The following example represents direct access from account `111122223333` to an Amazon S3 resource owned by account `444455556666`. The accounts belong to different AWS organizations. The caller uses the TIP session credentials to access the resource, so no new role session is created. The CloudTrail event in the target account can record the TIP context carried by those credentials.

```json
{
  "eventSource": "s3.amazonaws.com",
  "eventName": "GetObject",
  "recipientAccountId": "444455556666",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

### Denied cross-account role assumption
<a name="id_roles_providers_tip_cloudtrail-denied-cross-account-role-assumption"></a>

The following example represents the caller-account copy of a cross-account `AssumeRole` request that fails with `AccessDenied`. The denied request does not create a role session. This differs from a successful cross-boundary role assumption, where AWS STS completes the request and drops TIP context from the resulting role session. CloudTrail does not deliver a copy of the denied request to the target account.

```json
{
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRole",
  "recipientAccountId": "111122223333",
  "errorCode": "AccessDenied",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

### Denied direct cross-account resource access
<a name="id_roles_providers_tip_cloudtrail-denied-direct-cross-account-resource-access"></a>

The following example represents the caller-account event for a denied request from account `111122223333` to an Amazon S3 resource owned by account `444455556666`. The target account does not receive TIP context from the denied request.

```json
{
  "eventSource": "s3.amazonaws.com",
  "eventName": "GetObject",
  "recipientAccountId": "111122223333",
  "errorCode": "AccessDenied",
  "userIdentity": {
    "onBehalfOf": {
      "subject": "user@example.com",
      "subjectType": "user",
      "issuer": "idp.example.com",
      "federatedProviderArn": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
    },
    "transactionContext": {
      "IdentityProvider": {
        "department": "Engineering"
      }
    }
  }
}
```

## Related information
<a name="id_roles_providers_tip_cloudtrail-related-information"></a>
+ [Understand where TIP context propagates](id_roles_providers_tip.md#id_roles_providers_tip_propagation)
+ [TIP context keys and runtime claims for IAM federation](id_roles_providers_tip_federation_context_keys.md)
+ [Control TIP for IAM federation with IAM policies](id_roles_providers_tip_federation_policies.md)
+ [Getting started with TIP for IAM federation](id_roles_providers_tip_federation_getting_started.md)
+ [AWS services that support TIP](id_roles_providers_tip_services.md)
+ [AWS CloudTrail user identity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)