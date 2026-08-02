# Getting started with the PricingPlanManager API

You can use the AWS CLI or the PricingPlanManager API to create, modify, and cancel flat-rate pricing plan subscriptions programmatically. The PricingPlanManager service manages subscriptions across plan families. Currently, `CloudFront` (CloudFront flat-rate pricing) is the only supported plan family.

This page provides a sample of the available operations, common workflows, and error handling. For complete API reference documentation, see the [PricingPlanManager API Reference](../../../pricingplanmanager/latest/APIReference/Welcome.md "../../../pricingplanmanager/latest/APIReference/Welcome.md").

For information about managing CloudFront flat-rate pricing plans using the CloudFront console, see [CloudFront flat-rate pricing plans](../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md "../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md") in the _Amazon CloudFront Developer Guide_.

## Prerequisites

Before you use the PricingPlanManager API, verify the following:

- **IAM permissions** — Your IAM identity must have permissions for the `pricingplanmanager` actions you want to perform. For more details on specific actions and AWS managed policies, see [Managing Access to AWS Flat-Rate Plans](security-pricing-plan.md "security-pricing-plan.md").
- **AWS CLI** — Install and configure the AWS CLI version 2. For installation instructions, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- **AWS credentials** — Configure credentials with access to the target AWS account. For more information, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
- **Region** — The PricingPlanManager API endpoint is available in `us-east-1`. Set your default Region or specify `--region us-east-1` in your CLI commands.

## Key concepts

### Subscription lifecycle

A pricing plan subscription goes through the following statuses:

| Status             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ACTIVE`           | The subscription is active and the pricing plan is applied to the associated resources. AWS bills usage at the subscription’s plan rate.                                                                                                                                                                                                                                                                                                                 |
| `PENDING_APPROVAL` | You created a paid subscription with `MANUAL` approval mode, and it is waiting for approval via `ApprovePaidSubscription`. The plan is not active and does not apply to the associated resources — AWS charges usage as pay-as-you-go until you approve the subscription and it becomes `ACTIVE`. The subscription does not expire while it is pending approval. A pending-approval subscription counts against your subscription quota while it exists. |
| `SYNC_IN_PROGRESS` | AWS is applying the subscription change to the associated resources. This typically takes 2–5 minutes. You cannot modify the subscription while it is in this state — wait for the sync to complete before making further changes. Fields that depend on the applied change (for example, a scheduled change’s `effectiveDate`) do not appear until the sync completes.                                                                                  |
| `FAILED`           | The subscription operation failed. Review the `statusReason` field on the subscription for a human-readable explanation of why it failed. Cancel the failed subscription and retry the operation to create a new subscription.                                                                                                                                                                                                                           |

### Optimistic concurrency (ETag)

All mutating operations use optimistic concurrency control through ETags. When you retrieve a subscription (using `GetSubscription` or `ListSubscriptions`), the response includes an `eTag` value. You must pass this value in the `ifMatch` parameter (`--if-match` in the CLI) when you update or cancel the subscription. If the subscription has changed since you retrieved it, the operation fails with a `ConflictException`.

This mechanism prevents one change from overwriting another.

### Two-phase subscription creation

When you create a subscription for a paid plan, you choose an approval mode that controls whether billing starts immediately or requires a separate approval step:

- **MANUAL** — The system creates the subscription in `PENDING_APPROVAL` status. You must make a separate call to `ApprovePaidSubscription` to activate the subscription and start billing.
- **IMMEDIATE** — The subscription is created and activated in a single step. Billing starts immediately.

###### Approval mode recommendation

We recommend using `MANUAL` approval mode for all programmatic workflows. You cannot cancel or revert an active paid subscription during the current billing period (calendar month). The two-phase approach prevents automated processes from starting billing without human confirmation. Premium plans can cost up to $10,000/mo.

**IAM permission separation**

To enforce the two-phase pattern, grant your automated workflows (such as deployment pipelines, agents, or service roles) only the `pricingplanmanager:CreateSubscription` permission. Reserve the `pricingplanmanager:ApprovePaidSubscription` permission for roles that require human authorization (such as administrator roles used interactively).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "pricingplanmanager:CreateSubscription",
      "Resource": "*"
    }
  ]
}
```

###### IMMEDIATE approval mode permissions

If a caller passes `approvalMode: "IMMEDIATE"` for a paid plan, the caller must have **both** the `pricingplanmanager:CreateSubscription` and `pricingplanmanager:ApprovePaidSubscription` permissions. The request fails with `AccessDeniedException` if the caller lacks the approval permission.

Free plan subscriptions are always activated immediately. For Free plans, the approval mode must be `IMMEDIATE` or omitted; a request that specifies `MANUAL` is rejected, because Free plans don’t require approval.

### Scheduled changes

Some changes don’t take effect immediately:

- **Downgrades** — When you change to a lower plan tier, the downgrade is scheduled for the end of the current billing period (calendar month). Feature availability changes immediately to match the new (lower) tier, but your usage allowances and billing remain at your current tier until the effective date.

###### Important

Although the downgrade is not fully effective until the end of the billing period, features exclusive to your current tier become unavailable immediately after you request the downgrade. You continue to be billed at your current tier’s rate until the effective date.

- **Cancellations** — When you cancel a paid plan, the cancellation is scheduled for the end of the current billing period (calendar month). Free plan cancellations take effect immediately.

Pending scheduled changes are recorded in the subscription’s `scheduledChange` field. You can cancel a pending scheduled change using `CancelSubscriptionChange` to keep your current plan.

## Operations reference

### CreateSubscription

Creates a new pricing plan subscription for one or more resources. For CloudFront plans, the resources are CloudFront distribution ARNs and WAF web ACL ARNs.

**CLI syntax**

```
aws pricing-plan-manager create-subscription \
    --plan-family <value> \
    --plan-tier <value> \
    [--usage-level <value>] \
    --resource-arns <value> [<value>...] \
    [--approval-mode <value>] \
    [--client-token <value>]
```

**Parameters**

| Parameter         | Required | Description                                                                                                                                                                                                                                                  |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--plan-family`   | Yes      | The pricing plan family. Use `CloudFront`.                                                                                                                                                                                                                   |
| `--plan-tier`     | Yes      | The plan tier. Valid values: `FREE`, `PRO`, `BUSINESS`, `PREMIUM`.                                                                                                                                                                                           |
| `--usage-level`   | No       | The usage level within the plan tier. Valid values depend on the plan family and tier. For CloudFront plans, see [Premium usage levels](#cf-premium-usage-levels "#cf-premium-usage-levels").                                                                |
| `--resource-arns` | Yes      | The resource ARNs to associate with the subscription. The required and optional resources depend on the plan family. For CloudFront plans, see [Required and optional resources](#cf-required-and-optional-resources "#cf-required-and-optional-resources"). |
| `--approval-mode` | No       | Controls whether paid subscriptions require separate approval. Valid values: `IMMEDIATE`, `MANUAL`. Default: `MANUAL`.                                                                                                                                       |
| `--client-token`  | No       | A unique token for idempotency. If you retry a request with the same client token, you get the same response without creating a duplicate subscription.                                                                                                      |

**Example request (recommended two-phase pattern)**

```
aws pricing-plan-manager create-subscription \
    --plan-family CloudFront \
    --plan-tier PRO \
    --resource-arns \
        arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE \
        arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
    --approval-mode MANUAL
```

**Example response**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "PRO",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "PENDING_APPROVAL",
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T10:00:00Z"
  },
  "eTag": "v1aXample1234"
}
```

**Notes**

- **Recommended:** Use `MANUAL` approval mode for paid plans in automated workflows to prevent unintended billing commitments. See [Two-phase subscription creation](#two-phase-subscription-creation "#two-phase-subscription-creation").
- If you use `MANUAL` approval mode for a paid plan, the subscription status is `PENDING_APPROVAL` until you call `ApprovePaidSubscription`. No billing charges occur until approval.
- If you use `IMMEDIATE` approval mode for a paid plan, the calling IAM principal must have both `pricingplanmanager:CreateSubscription` and `pricingplanmanager:ApprovePaidSubscription` permissions.
- Free plan subscriptions are always activated immediately regardless of the approval mode specified.

### ApprovePaidSubscription

Approves a subscription that is in `PENDING_APPROVAL` status. This activates the paid subscription and begins billing.

**CLI syntax**

```
aws pricing-plan-manager approve-paid-subscription \
    --arn <value> \
    --if-match <value> \
    [--client-token <value>]
```

**Parameters**

| Parameter        | Required | Description                                                                                              |
| ---------------- | -------- | -------------------------------------------------------------------------------------------------------- |
| `--arn`          | Yes      | The ARN of the subscription to approve.                                                                  |
| `--if-match`     | Yes      | The ETag value from a previous `GetSubscription`, `CreateSubscription`, or `ListSubscriptions` response. |
| `--client-token` | No       | A unique token for idempotency.                                                                          |

**Example request**

```
aws pricing-plan-manager approve-paid-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v1aXample1234"
```

**Example response**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "PRO",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "SYNC_IN_PROGRESS",
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T10:01:00Z"
  },
  "eTag": "v2bXample5678"
}
```

**Notes**

- You can only approve subscriptions with status `PENDING_APPROVAL`.
- After approval, AWS starts billing immediately for the paid plan.

### GetSubscription

Retrieves the details of a single pricing plan subscription.

**CLI syntax**

```
aws pricing-plan-manager get-subscription \
    --arn <value>
```

**Parameters**

| Parameter | Required | Description                              |
| --------- | -------- | ---------------------------------------- |
| `--arn`   | Yes      | The ARN of the subscription to retrieve. |

**Example request**

```
aws pricing-plan-manager get-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

**Example response**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "BUSINESS",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "ACTIVE",
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T12:30:00Z"
  },
  "eTag": "v3cXample9012"
}
```

**Notes**

- Use the `eTag` value from the response in subsequent mutating operations (`--if-match`).

### ListSubscriptions

Lists all pricing plan subscriptions in your account.

**CLI syntax**

```
aws pricing-plan-manager list-subscriptions \
    [--next-token <value>]
```

**Parameters**

| Parameter      | Required | Description                                                                                                               |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| `--next-token` | No       | A pagination token returned by a previous `ListSubscriptions` call. Pass this value to retrieve the next page of results. |

**Example request**

```
aws pricing-plan-manager list-subscriptions
```

**Example response**

```
{
  "subscriptionSummaries": [
    {
      "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "planFamily": "CloudFront",
      "planTier": "BUSINESS",
      "resourceArns": [
        "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
        "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
      ],
      "status": "ACTIVE",
      "createdAt": "2026-07-21T10:00:00Z",
      "updatedAt": "2026-07-23T10:00:00Z",
      "eTag": "v3cXample9012"
    }
  ],
  "nextToken": null
}
```

### UpdateSubscription

Changes the plan tier or usage level of an existing subscription.

**CLI syntax**

```
aws pricing-plan-manager update-subscription \
    --arn <value> \
    --if-match <value> \
    [--plan-tier <value>] \
    [--usage-level <value>] \
    [--client-token <value>]
```

**Parameters**

| Parameter        | Required | Description                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--arn`          | Yes      | The ARN of the subscription to update.                                                                                                                                                                                                                                                                                                                                         |
| `--if-match`     | Yes      | The ETag value from a previous `GetSubscription`, `CreateSubscription`, or `ListSubscriptions` response.                                                                                                                                                                                                                                                                       |
| `--plan-tier`    | Yes      | The new plan tier. Valid values: `FREE`, `PRO`, `BUSINESS`, `PREMIUM`.                                                                                                                                                                                                                                                                                                         |
| `--usage-level`  | No       | The new usage level within the plan tier. Valid values depend on the plan family and tier. For CloudFront plans, see [Premium usage levels](#cf-premium-usage-levels "#cf-premium-usage-levels").<br>If you omit this parameter, the usage level is reset to the default level — it is not left unchanged. To preserve your current usage level, always specify it explicitly. |
| `--client-token` | No       | A unique token for idempotency.                                                                                                                                                                                                                                                                                                                                                |

You must specify at least one of `--plan-tier` or `--usage-level`.

**Example request (upgrade)**

```
aws pricing-plan-manager update-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v3cXample9012" \
    --plan-tier PREMIUM \
    --usage-level CF_PREMIUM_L4
```

**Example response (upgrade)**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "PREMIUM",
    "usageLevel": "CF_PREMIUM_L4",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "ACTIVE",
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T14:00:00Z"
  },
  "eTag": "v4dXample3456"
}
```

**Example request (downgrade)**

```
aws pricing-plan-manager update-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v4dXample3456" \
    --plan-tier PRO
```

**Example response (downgrade)**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "PREMIUM",
    "usageLevel": "CF_PREMIUM_L4",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "SYNC_IN_PROGRESS",
    "scheduledChange": {
      "changeType": "DOWNGRADE",
      "planTier": "PRO"
    },
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T15:00:00Z"
  },
  "eTag": "v5eXample7890"
}
```

**Notes**

- **Upgrades** take effect immediately. You are billed at the new rate starting from the time of the upgrade.
- **Downgrades** are scheduled for the end of the current billing period. Feature availability changes immediately to match the new (lower) tier, but your usage allowances and billing remain at your current tier until the effective date. The `scheduledChange` field in the response contains the downgrade details and effective date.

### CancelSubscription

Cancels a pricing plan subscription. For paid plans, the cancellation is scheduled for the end of the current billing period. For Free plans, the cancellation takes effect immediately.

**CLI syntax**

```
aws pricing-plan-manager cancel-subscription \
    --arn <value> \
    --if-match <value> \
    [--client-token <value>]
```

**Parameters**

| Parameter        | Required | Description                                                                                              |
| ---------------- | -------- | -------------------------------------------------------------------------------------------------------- |
| `--arn`          | Yes      | The ARN of the subscription to cancel.                                                                   |
| `--if-match`     | Yes      | The ETag value from a previous `GetSubscription`, `CreateSubscription`, or `ListSubscriptions` response. |
| `--client-token` | No       | A unique token for idempotency.                                                                          |

**Example request**

```
aws pricing-plan-manager cancel-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v4dXample3456"
```

**Example response**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "PREMIUM",
    "usageLevel": "CF_PREMIUM_L4",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "SYNC_IN_PROGRESS",
    "scheduledChange": {
      "changeType": "CANCELLATION"
    },
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T16:00:00Z"
  },
  "eTag": "v6fXample1234"
}
```

**Notes**

- For paid plans, the subscription remains active until the scheduled cancellation date. You continue to receive plan benefits until then.
- For Free plans, cancellation takes effect immediately and no `scheduledChange` is returned.
- You can also cancel a subscription that is in `PENDING_APPROVAL` status. Because the subscription was never activated, the cancellation takes effect immediately.
- To undo a pending cancellation on an active subscription, use `CancelSubscriptionChange`.

### CancelSubscriptionChange

Cancels a pending scheduled change (downgrade or cancellation) on a subscription. The subscription continues with its current plan.

**CLI syntax**

```
aws pricing-plan-manager cancel-subscription-change \
    --arn <value> \
    --if-match <value> \
    [--client-token <value>]
```

**Parameters**

| Parameter        | Required | Description                                                                       |
| ---------------- | -------- | --------------------------------------------------------------------------------- |
| `--arn`          | Yes      | The ARN of the subscription with the scheduled change to cancel.                  |
| `--if-match`     | Yes      | The ETag value from a previous `GetSubscription` or `ListSubscriptions` response. |
| `--client-token` | No       | A unique token for idempotency.                                                   |

**Example request**

```
aws pricing-plan-manager cancel-subscription-change \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v6fXample1234"
```

**Example response**

```
{
  "subscription": {
    "arn": "arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "planFamily": "CloudFront",
    "planTier": "PREMIUM",
    "usageLevel": "CF_PREMIUM_L4",
    "resourceArns": [
      "arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE",
      "arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    ],
    "status": "ACTIVE",
    "createdAt": "2026-07-23T10:00:00Z",
    "updatedAt": "2026-07-23T17:00:00Z"
  },
  "eTag": "v7gXample5678"
}
```

**Notes**

- After you cancel a scheduled change, the `scheduledChange` field is removed from the subscription.
- You can only cancel scheduled changes of type `CANCELLATION` or `DOWNGRADE`.

### AssociateResourcesToSubscription

Adds one or more resources to an existing subscription. For CloudFront plans, use this to add optional resources (such as a Route 53 hosted zone ARN or a CloudFront KeyValueStore ARN) after the subscription is created.

**CLI syntax**

```
aws pricing-plan-manager associate-resources-to-subscription \
    --arn <value> \
    --if-match <value> \
    --resource-arns <value> [<value>...] \
    [--client-token <value>]
```

**Parameters**

| Parameter         | Required | Description                                                                                                                                                                                                                                                  |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--arn`           | Yes      | The ARN of the subscription to associate resources with.                                                                                                                                                                                                     |
| `--if-match`      | Yes      | The ETag value from a previous `GetSubscription` or `ListSubscriptions` response.                                                                                                                                                                            |
| `--resource-arns` | Yes      | The resource ARNs to associate with the subscription. The required and optional resources depend on the plan family. For CloudFront plans, see [Required and optional resources](#cf-required-and-optional-resources "#cf-required-and-optional-resources"). |
| `--client-token`  | No       | A unique token for idempotency.                                                                                                                                                                                                                              |

**Example request**

```
aws pricing-plan-manager associate-resources-to-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v3cXample9012" \
    --resource-arns \
        arn:aws:route53:::hostedzone/Z0123456789ABCDEFGHIJ
```

**Notes**

- You can only associate resources that are compatible with the subscription’s plan family.
- Resource validation occurs at the time of association.

### DisassociateResourcesFromSubscription

Removes one or more optional resources from an existing subscription. You cannot remove required resources (for example, for CloudFront plans, the distribution and web ACL are required and cannot be disassociated).

**CLI syntax**

```
aws pricing-plan-manager disassociate-resources-from-subscription \
    --arn <value> \
    --if-match <value> \
    --resource-arns <value> [<value>...] \
    [--client-token <value>]
```

**Parameters**

| Parameter         | Required | Description                                                                       |
| ----------------- | -------- | --------------------------------------------------------------------------------- |
| `--arn`           | Yes      | The ARN of the subscription to disassociate resources from.                       |
| `--if-match`      | Yes      | The ETag value from a previous `GetSubscription` or `ListSubscriptions` response. |
| `--resource-arns` | Yes      | The resource ARNs to remove from the subscription.                                |
| `--client-token`  | No       | A unique token for idempotency.                                                   |

**Example request**

```
aws pricing-plan-manager disassociate-resources-from-subscription \
    --arn arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --if-match "v3cXample9012" \
    --resource-arns \
        arn:aws:route53:::hostedzone/Z0123456789ABCDEFGHIJ
```

**Notes**

- You can only remove optional resources. Attempting to remove a required resource fails with a `ValidationException`.
- After disassociation, the plan no longer covers costs for the removed resource.

## Common workflows

This section shows end-to-end workflows using the AWS CLI.

### Subscribe and approve a paid plan

This workflow creates a subscription with manual approval, then approves it.

```
# Step 1: Create the subscription
read SUBSCRIPTION_ARN ETAG < <(aws pricing-plan-manager create-subscription \
    --plan-family CloudFront \
    --plan-tier BUSINESS \
    --resource-arns \
        arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE \
        arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
    --approval-mode MANUAL \
    --query '[subscription.arn, eTag]' \
    --output text)

echo "Subscription created: $SUBSCRIPTION_ARN (status: PENDING_APPROVAL)"
echo "ETag: $ETAG"

# Step 2: Approve the subscription
aws pricing-plan-manager approve-paid-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --if-match "$ETAG"
```

### Upgrade a subscription

This workflow retrieves a subscription, then upgrades it to a higher tier.

```
# Step 1: Get the current subscription to retrieve the ETag
SUBSCRIPTION_ARN="arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"

# Get current subscription — pull ETag and current tier in one call
read ETAG CURRENT_TIER < <(aws pricing-plan-manager get-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --query '[eTag, subscription.planTier]' \
    --output text)

echo "Current tier: $CURRENT_TIER"

# Step 2: Upgrade to Premium
aws pricing-plan-manager update-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --if-match "$ETAG" \
    --plan-tier PREMIUM \
    --usage-level CF_PREMIUM_L3
```

### Downgrade a subscription

This workflow downgrades a subscription. The downgrade is scheduled for the end of the billing period.

```
# Step 1: Get the current subscription
SUBSCRIPTION_ARN="arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"

ETAG=$(aws pricing-plan-manager get-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --query 'eTag' \
    --output text)

# Step 2: Downgrade to Pro (takes effect at end of billing period)
aws pricing-plan-manager update-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --if-match "$ETAG" \
    --plan-tier PRO \
    --query 'subscription.scheduledChange'
```

### Cancel a subscription and undo the cancellation

This workflow cancels a paid subscription, then undoes the cancellation before it takes effect.

```
SUBSCRIPTION_ARN="arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"

# Step 1: Get the current subscription
ETAG=$(aws pricing-plan-manager get-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --query 'eTag' \
    --output text)

# Step 2: Cancel the subscription (scheduled for end of billing period)
# Only the ETag is reliably present now — effectiveDate is not populated until sync completes.
NEW_ETAG=$(aws pricing-plan-manager cancel-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --if-match "$ETAG" \
    --query 'eTag' \
    --output text)

# Step 2b: Poll until the resource is done syncing and the effective date appears
echo "Waiting for scheduled change to sync..."
while true; do
    read STATUS EFFECTIVE_DATE LATEST_ETAG < <(aws pricing-plan-manager get-subscription \
        --arn "$SUBSCRIPTION_ARN" \
        --query '[subscription.status, subscription.scheduledChange.effectiveDate, eTag]' \
        --output text)
    if [ "$EFFECTIVE_DATE" != "None" ] && [ -n "$EFFECTIVE_DATE" ]; then
        break
    fi
    echo "  status: $STATUS (effective date not yet available)"
    sleep 5
done

echo "Cancellation scheduled for: $EFFECTIVE_DATE"

# Step 3: Changed your mind? Cancel the scheduled cancellation
# Use the latest ETag from the poll — the ETag may have changed during sync.
aws pricing-plan-manager cancel-subscription-change \
    --arn "$SUBSCRIPTION_ARN" \
    --if-match "$LATEST_ETAG"

echo "Cancellation undone. Subscription continues as normal."
```

## Plan family specifics

The key concepts, operations, and workflows described earlier apply to all plan families. This section covers the requirements and behavior that are specific to each plan family. `CloudFront` is currently the only plan family.

### Working with the CloudFront plan family

The `CloudFront` plan family applies flat-rate pricing to a CloudFront distribution and its associated AWS WAF web ACL, Amazon Route 53 hosted zone, and Amazon CloudWatch Logs ingestion. This section covers the CloudFront-specific details you need when you manage `CloudFront` plan subscriptions programmatically.

For the full description of plan tiers, included features, usage allowances, and unsupported configurations, see [CloudFront flat-rate pricing plans](../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md "../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md") in the _Amazon CloudFront Developer Guide_.

#### Required and optional resources

When you create a `CloudFront` plan subscription, the `resourceArns` list must include:

- **A CloudFront distribution ARN** (required) — the distribution the plan applies to.
- **An AWS WAF web ACL ARN** (required) — a plan requires an associated web ACL. You must create the web ACL before you create the subscription; the API doesn’t create one for you. The web ACL must be in the `CLOUDFRONT` scope (Region `us-east-1`).

You can optionally include, at create time or later using `AssociateResourcesToSubscription`:

- **A Route 53 hosted zone ARN** — attaches your hosted zone so the plan covers its standard costs, subject to the DNS query allowances for your tier.
- **A CloudFront KeyValueStore ARN** — for use with CloudFront Functions.

#### Plan tiers

The `CloudFront` plan family supports the following tiers, which you specify in the `planTier` parameter:

- `FREE` — For hobbyists, learners, and developers getting started.
- `PRO` — Launch and grow small websites, blogs, and applications.
- `BUSINESS` — Protect and accelerate business applications.
- `PREMIUM` — Scale and protect business and mission-critical applications. Supports configurable usage levels. See [Premium usage levels](#cf-premium-usage-levels "#cf-premium-usage-levels").

Higher tiers include all features of the lower tiers plus additional capabilities. For the complete feature matrix and monthly usage allowances, see [Features by pricing plan tier](../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md#pricing-plan-features "../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md#pricing-plan-features") in the _Amazon CloudFront Developer Guide_.

#### Premium usage levels

The Premium plan offers configurable monthly usage allowances. When you subscribe to or manage a Premium plan, you can select a higher monthly usage allowance from the following levels:

| Usage level     | Monthly data transfer | Monthly requests | Flat-rate price per month |
| --------------- | --------------------- | ---------------- | ------------------------- |
| `DEFAULT`       | 50 TB                 | 500 M            | $1,000                    |
| `CF_PREMIUM_L2` | 75 TB                 | 750 M            | $1,450                    |
| `CF_PREMIUM_L3` | 125 TB                | 1.25 B           | $2,250                    |
| `CF_PREMIUM_L4` | 200 TB                | 2 B              | $3,500                    |
| `CF_PREMIUM_L5` | 350 TB                | 3.5 B            | $6,000                    |
| `CF_PREMIUM_L6` | 600 TB                | 6 B              | $10,000                   |

When you select a higher usage level, your monthly price increases and your monthly usage allowance increases accordingly. The features and services included in the Premium plan remain the same at every usage level. You are only changing your usage allowance and flat-rate price.

When you increase your usage level, changes take effect immediately and your price is prorated. When you decrease your usage level, the change takes effect at the beginning of the next billing cycle.

If your application’s baseline usage exceeds 6 B requests or 600 TB per month, [contact us](https://aws.amazon.com/contact-us/sales-support/ "https://aws.amazon.com/contact-us/sales-support/") for custom pricing.

#### Create the distribution and web ACL before you subscribe

A `CloudFront` plan subscription requires both a CloudFront distribution and an AWS WAF web ACL, and both must exist before you create the subscription. Create the web ACL first, so that you can reference its ARN in the distribution configuration. The typical flow is: create the web ACL → create the distribution (referencing the web ACL) → create the subscription (referencing both ARNs). For paid plans, the subscription must also be approved to start billing—either in the same step with `IMMEDIATE` approval mode, or in a separate step with `MANUAL`.

**Step 1: Create the web ACL**

The following example creates a web ACL in the `CLOUDFRONT` scope with the AWS Managed Rules rule groups that correspond to the default one-click protection applied in the CloudFront console. The `AWSManagedRulesCommonRuleSet` and `AWSManagedRulesAmazonIpReputationList` rule groups provide baseline protection suitable for most applications.

```
aws wafv2 create-web-acl \
    --name my-plan-web-acl \
    --scope CLOUDFRONT \
    --region us-east-1 \
    --default-action Allow={} \
    --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=my-plan-web-acl \
    --rules '[
        {
            "Name": "AWS-AWSManagedRulesCommonRuleSet",
            "Priority": 0,
            "Statement": {
                "ManagedRuleGroupStatement": {
                    "VendorName": "AWS",
                    "Name": "AWSManagedRulesCommonRuleSet"
                }
            },
            "OverrideAction": { "None": {} },
            "VisibilityConfig": {
                "SampledRequestsEnabled": true,
                "CloudWatchMetricsEnabled": true,
                "MetricName": "AWSManagedRulesCommonRuleSet"
            }
        },
        {
            "Name": "AWS-AWSManagedRulesAmazonIpReputationList",
            "Priority": 1,
            "Statement": {
                "ManagedRuleGroupStatement": {
                    "VendorName": "AWS",
                    "Name": "AWSManagedRulesAmazonIpReputationList"
                }
            },
            "OverrideAction": { "None": {} },
            "VisibilityConfig": {
                "SampledRequestsEnabled": true,
                "CloudWatchMetricsEnabled": true,
                "MetricName": "AWSManagedRulesAmazonIpReputationList"
            }
        },
        {
            "Name": "AWS-AWSManagedRulesKnownBadInputsRuleSet",
            "Priority": 2,
            "Statement": {
                "ManagedRuleGroupStatement": {
                    "VendorName": "AWS",
                    "Name": "AWSManagedRulesKnownBadInputsRuleSet"
                }
            },
            "OverrideAction": { "None": {} },
            "VisibilityConfig": {
                "SampledRequestsEnabled": true,
                "CloudWatchMetricsEnabled": true,
                "MetricName": "AWSManagedRulesKnownBadInputsRuleSet"
            }
        }
    ]'
```

The response includes the web ACL’s ARN under `Summary.ARN`. Note this ARN — you reference it in the distribution configuration in the next step, and again in the `resourceArns` list when you create the subscription.

**Step 2: Create the distribution**

Create a distribution that references the web ACL from Step 1. In the distribution configuration, set the `WebACLId` field to the web ACL ARN you noted previously. The following example creates a distribution from a configuration file.

```
aws cloudfront create-distribution \
    --distribution-config file://distribution-config.json
```

The response includes the distribution’s ARN under `Distribution.ARN` and its ID under `Distribution.Id`. Use the distribution ARN, together with the web ACL ARN from Step 1, in the `resourceArns` list when you create the subscription. For details about distribution configuration, see [Create a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md") in the _Amazon CloudFront Developer Guide_.

**Step 3: Create the subscription**

Create the subscription, passing both the distribution ARN and the web ACL ARN in `resourceArns`. When you run this interactively and are ready to start billing, use `IMMEDIATE` approval mode to create and activate the subscription in a single step.

```
aws pricing-plan-manager create-subscription \
    --plan-family CloudFront \
    --plan-tier BUSINESS \
    --resource-arns \
        arn:aws:cloudfront::111122223333:distribution/EDFDVBD6EXAMPLE \
        arn:aws:wafv2:us-east-1:111122223333:global/webacl/my-plan-web-acl/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
    --approval-mode IMMEDIATE
```

The subscription is created with status `ACTIVE`, and billing begins immediately. Using `IMMEDIATE` requires both the `pricingplanmanager:CreateSubscription` and `pricingplanmanager:ApprovePaidSubscription` permissions.

For automated workflows—​such as deployment pipelines, agents, or service roles—​use `MANUAL` approval mode instead, so that a human authorizes billing in a separate step. For that flow, including guidance on separating create and approve permissions, see [Subscribe and approve a paid plan](#subscribe-and-approve-a-paid-plan "#subscribe-and-approve-a-paid-plan") and [Two-phase subscription creation](#two-phase-subscription-creation "#two-phase-subscription-creation").

#### Recommended: Anti-DDoS managed rule group for Business and Premium

For `BUSINESS` and `PREMIUM` plans, we recommend adding the AWS WAF Anti-DDoS managed rule group (`AWSManagedRulesAntiDDoSRuleSet`) to your web ACL. This rule group identifies and blocks DDoS attacks by learning your application’s traffic patterns to distinguish attacks from legitimate surges. Advanced DDoS protection is included in the Business and Premium tiers. For more information, see [AWS WAF Anti-DDoS rule group](../../../waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.md "../../../waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.md") in the _AWS WAF Developer Guide_.

Add the following rule to the `--rules` array shown previously (adjust `Priority` so it doesn’t collide with your other rules):

```
{
    "Name": "AWS-AWSManagedRulesAntiDDoSRuleSet",
    "Priority": 3,
    "Statement": {
        "ManagedRuleGroupStatement": {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesAntiDDoSRuleSet"
        }
    },
    "OverrideAction": { "None": {} },
    "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWSManagedRulesAntiDDoSRuleSet"
    }
}
```

#### Unsupported configurations

You can’t subscribe a distribution to a `CloudFront` plan if it uses certain features (for example, real-time logs, multi-tenant distributions, or staging distributions for continuous deployment). If the distribution uses an unsupported feature, `CreateSubscription` fails with a `ValidationException`. Disable or remove the unsupported feature before you subscribe. For the complete list of unsupported features and their alternatives, see [Unsupported features](../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md#pricing-plan-unsupported-features "../../../AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.md#pricing-plan-unsupported-features") in the _Amazon CloudFront Developer Guide_.

## Error handling

The PricingPlanManager API returns the following error types. Handle these in your application to provide appropriate error recovery.

| Error                           | HTTP status | Description                                                                                                                                                                                                                                                   |
| ------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AccessDeniedException`         | 403         | You don’t have permission to perform this operation. Verify your IAM policy includes the required `pricingplanmanager` actions.                                                                                                                               |
| `ConflictException`             | 409         | The subscription was modified since you last retrieved it. The `ifMatch` ETag value is stale. Retrieve the subscription again to get the current ETag and retry the operation.                                                                                |
| `ResourceNotFoundException`     | 404         | The specified subscription ARN does not exist. Verify the ARN is correct and that the subscription has not been deleted.                                                                                                                                      |
| `ServiceQuotaExceededException` | 402         | You have reached the maximum number of subscriptions for your account.                                                                                                                                                                                        |
| `ThrottlingException`           | 429         | You exceeded the API request rate limit. Implement exponential backoff and retry.                                                                                                                                                                             |
| `ValidationException`           | 400         | The request failed validation. This can occur when required fields are missing, field values are out of range, the operation is not valid for the current subscription state, or an associated resources uses features not available in the target plan tier. |

### Handling concurrency conflicts

Because the PricingPlanManager API uses optimistic concurrency, your application should handle `ConflictException` gracefully. The recommended pattern is to retrieve the latest ETag and retry the operation:

```
SUBSCRIPTION_ARN="arn:aws:pricingplanmanager:us-east-1:111122223333:subscription/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"

# Get the latest ETag
ETAG=$(aws pricing-plan-manager get-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --query 'eTag' \
    --output text)

# Retry the update with the fresh ETag
aws pricing-plan-manager update-subscription \
    --arn "$SUBSCRIPTION_ARN" \
    --if-match "$ETAG" \
    --plan-tier PREMIUM
```

### Handling throttling

If you receive a `ThrottlingException` (HTTP 429), wait before retrying. Implement exponential backoff in your scripts by increasing the wait time between retries:

```
MAX_RETRIES=5
ATTEMPT=0

while [ $ATTEMPT -lt $MAX_RETRIES ]; do
    RESPONSE=$(aws pricing-plan-manager list-subscriptions --output json 2>&1) && break
    if echo "$RESPONSE" | grep -q "ThrottlingException"; then
        DELAY=$((2 ** ATTEMPT))
        echo "Throttled. Retrying in ${DELAY}s (attempt $((ATTEMPT+1))/${MAX_RETRIES})..."
        sleep $DELAY
        ATTEMPT=$((ATTEMPT + 1))
    else
        echo "Error: $RESPONSE"
        break
    fi
done
```
