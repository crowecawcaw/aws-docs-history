# Security Hub CSPM controls for Secrets Manager

These AWS Security Hub CSPM controls evaluate the AWS Secrets Manager service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [SecretsManager.1] Secrets Manager secrets should have automatic rotation enabled

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), PCI DSS v4.0.1/8.6.3, PCI DSS v4.0.1/8.3.9

**Category:** Protect > Secure development

**Severity:** Medium

**Resource type:**
`AWS::SecretsManager::Secret`

**AWS Config rule:**
[`secretsmanager-rotation-enabled-check`](../../../config/latest/developerguide/secretsmanager-rotation-enabled-check.md "../../../config/latest/developerguide/secretsmanager-rotation-enabled-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                         | Description                                                  | Type    | Allowed custom values | Security Hub CSPM default value |
| --------------------------------- | ------------------------------------------------------------ | ------- | --------------------- | ------------------------------- |
| `maximumAllowedRotationFrequency` | Maximum number of days allowed for secret rotation frequency | Integer | `1` to `365`          | No default value                |

This control checks whether a secret stored in AWS Secrets Manager is configured with automatic
rotation. The control fails if the secret isn't configured with automatic rotation. If you
provide a custom value for the `maximumAllowedRotationFrequency` parameter, the control passes
only if the secret is automatically rotated within the specified window of time.

Secrets Manager helps you improve the security posture of your organization. Secrets include database
credentials, passwords, and third-party API keys. You can use Secrets Manager to store secrets centrally,
encrypt secrets automatically, control access to secrets, and rotate secrets safely and
automatically.

Secrets Manager can rotate secrets. You can use rotation to replace long-term secrets with short-term
ones. Rotating your secrets limits how long an unauthorized user can use a compromised secret.
For this reason, you should rotate your secrets frequently. To learn more about rotation, see
[Rotating your AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_.

### Remediation

To turn on automatic rotation for Secrets Manager secrets, see
[Set up automatic rotation for AWS Secrets Manager secrets using the console](../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md "../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md") in the _AWS Secrets Manager User Guide_.
You must choose and configure an AWS Lambda function for rotation.

## [SecretsManager.2] Secrets Manager secrets configured with automatic rotation should rotate successfully

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), PCI DSS v4.0.1/8.6.3, PCI DSS v4.0.1/8.3.9

**Category:** Protect > Secure development

**Severity:** Medium

**Resource type:**
`AWS::SecretsManager::Secret`

**AWS Config rule:**
[`secretsmanager-scheduled-rotation-success-check`](../../../config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.md "../../../config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS Secrets Manager secret rotated successfully based on the rotation
schedule. The control fails if `RotationOccurringAsScheduled` is `false`.
The control only evaluates secrets that have rotation turned on.

Secrets Manager helps you improve the security posture of your organization. Secrets include database
credentials, passwords, and third-party API keys. You can use Secrets Manager to store secrets centrally,
encrypt secrets automatically, control access to secrets, and rotate secrets safely and
automatically.

Secrets Manager can rotate secrets. You can use rotation to replace long-term secrets with short-term
ones. Rotating your secrets limits how long an unauthorized user can use a compromised secret.
For this reason, you should rotate your secrets frequently.

In addition to configuring secrets to rotate automatically, you should ensure that those
secrets rotate successfully based on the rotation schedule.

To learn more about rotation, see [Rotating your AWS Secrets Manager
secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_.

### Remediation

If the automatic rotation fails, then Secrets Manager might have encountered errors with the
configuration. To rotate secrets in Secrets Manager, you use a Lambda function that defines how to interact with the
database or service that owns the secret.

For help diagnosing and fixing common errors related to secrets rotation, see [Troubleshooting AWS Secrets Manager rotation of secrets](../../../secretsmanager/latest/userguide/troubleshoot_rotation.md "../../../secretsmanager/latest/userguide/troubleshoot_rotation.md") in the _AWS Secrets Manager User Guide_.

## [SecretsManager.3] Remove unused Secrets Manager secrets

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15)

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::SecretsManager::Secret`

**AWS Config rule:**
[`secretsmanager-secret-unused`](../../../config/latest/developerguide/secretsmanager-secret-unused.md "../../../config/latest/developerguide/secretsmanager-secret-unused.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter       | Description                                            | Type    | Allowed custom values | Security Hub CSPM default value |
| --------------- | ------------------------------------------------------ | ------- | --------------------- | ------------------------------- |
| `unusedForDays` | Maximum number of days that a secret can remain unused | Integer | `1` to `365`          | `90`                            |

This control checks whether an AWS Secrets Manager secret has been accessed within the specified time
frame. The control fails if a secret is unused beyond the specified time frame. Unless you provide a custom parameter value for the access period, Security Hub CSPM uses a default value of 90 days.

Deleting unused secrets is as important as rotating secrets. Unused secrets can be abused
by their former users, who no longer need access to these secrets. Also, as more users get
access to a secret, someone might have mishandled and leaked it to an unauthorized entity, which
increases the risk of abuse. Deleting unused secrets helps revoke secret access from users who
no longer need it. It also helps to reduce the cost of using Secrets Manager. Therefore, it is
essential to routinely delete unused secrets.

### Remediation

To delete inactive Secrets Manager secrets, see [Delete an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/manage_delete-secret.md "../../../secretsmanager/latest/userguide/manage_delete-secret.md")
in the _AWS Secrets Manager User Guide_.

## [SecretsManager.4] Secrets Manager secrets should be rotated within a specified number of days

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3(15), PCI DSS v4.0.1/8.6.3, PCI DSS v4.0.1/8.3.9

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::SecretsManager::Secret`

**AWS Config rule:**
[`secretsmanager-secret-periodic-rotation`](../../../config/latest/developerguide/secretsmanager-secret-periodic-rotation.md "../../../config/latest/developerguide/secretsmanager-secret-periodic-rotation.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter              | Description                                               | Type    | Allowed custom values | Security Hub CSPM default value |
| ---------------------- | --------------------------------------------------------- | ------- | --------------------- | ------------------------------- |
| `maxDaysSinceRotation` | Maximum number of days that a secret can remain unchanged | Integer | `1` to `180`          | `90`                            |

This control checks whether an AWS Secrets Manager secret is rotated at least once within the specified time frame. The control
fails if a secret isn't rotated at least this frequently. Unless you provide a custom parameter value for the rotation
period, Security Hub CSPM uses a default value of 90 days.

Rotating secrets can help you to reduce the risk of an unauthorized use of your secrets in
your AWS account. Examples include database credentials, passwords, third-party API keys, and
even arbitrary text. If you do not change your secrets for a long period of time, the secrets
are more likely to be compromised.

As more users get access to a secret, it can become more likely that someone mishandled and
leaked it to an unauthorized entity. Secrets can be leaked through logs and cache data. They can
be shared for debugging purposes and not changed or revoked once the debugging completes. For
all these reasons, secrets should be rotated frequently.

You can configure automatic rotation for secrets in AWS Secrets Manager. With automatic
rotation, you can replace long-term secrets with short-term ones, significantly reducing the
risk of compromise. We recommend that you configure automatic rotation for your Secrets Manager secrets. For more information, see [Rotating your AWS Secrets Manager
secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_.

### Remediation

To turn on automatic rotation for Secrets Manager secrets, see
[Set up automatic rotation for AWS Secrets Manager secrets using the console](../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md "../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md") in the _AWS Secrets Manager User Guide_.
You must choose and configure an AWS Lambda function for rotation.

## [SecretsManager.5] Secrets Manager secrets should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SecretsManager::Secret`

**AWS Config rule:** `tagged-secretsmanager-secret` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an AWS Secrets Manager secret has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the secret doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the secret isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a Secrets Manager secret, see
[Tag AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/managing-secrets_tagging.md "../../../secretsmanager/latest/userguide/managing-secrets_tagging.md") in the _AWS Secrets Manager User Guide_.
