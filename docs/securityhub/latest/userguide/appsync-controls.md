# Security Hub CSPM controls for AWS AppSync

These Security Hub CSPM controls evaluate the AWS AppSync service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [AppSync.1] AWS AppSync API caches should be encrypted at rest

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::AppSync::GraphQLApi`

**AWS Config rule:**
[appsync-cache-ct-encryption-at-rest](../../../config/latest/developerguide/appsync-cache-ct-encryption-at-rest.md "../../../config/latest/developerguide/appsync-cache-ct-encryption-at-rest.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS AppSync API cache is encrypted at rest. The control fails if the API cache isn't
encrypted at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

###### Note

Due to AWS AppSync implementing a service-level change that makes encryption at rest mandatory for all API caches, this control will be retired and removed from all applicable standards on March 9, 2026.

### Remediation

You can't change the encryption settings after enabling caching for your AWS AppSync API. Instead, you must delete the cache and
and recreate it with encryption enabled. For more information, see [Cache encryption](../../../appsync/latest/devguide/enabling-caching.md#caching-encryption "../../../appsync/latest/devguide/enabling-caching.md#caching-encryption") in the _AWS AppSync Developer Guide_.

## [AppSync.2] AWS AppSync should have field-level logging enabled

**Related requirements:** PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::AppSync::GraphQLApi`

**AWS Config rule:**
[`appsync-logging-enabled`](../../../config/latest/developerguide/appsync-logging-enabled.md "../../../config/latest/developerguide/appsync-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter           | Description         | Type | Allowed custom values           | Security Hub CSPM default value |
| ------------------- | ------------------- | ---- | ------------------------------- | ------------------------------- |
| `fieldLoggingLevel` | Field logging level | Enum | `ERROR`, `ALL`, `INFO`, `DEBUG` | `No default value`              |

This control checks whether an AWS AppSync API has field-level logging turned on. The control fails
if the field resolver log level is set to **None**. Unless you provide custom
parameter values to indicate that a specific log type should be enabled, Security Hub CSPM produces a passed finding if the field resolver log level is either `ERROR` or
`ALL`.

You can use logging and metrics to identify, troubleshoot, and optimize your GraphQL queries.
Turning on logging for AWS AppSync GraphQL helps you get detailed information about API requests and responses, identify and
respond to issues, and comply with regulatory requirements.

### Remediation

To turn on logging for AWS AppSync, see [Setup and configuration](../../../appsync/latest/devguide/monitoring.md#setup-and-configuration "../../../appsync/latest/devguide/monitoring.md#setup-and-configuration") in the _AWS AppSync Developer Guide_.

## [AppSync.4] AWS AppSync GraphQL APIs should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppSync::GraphQLApi`

**AWS Config rule:** `tagged-appsync-graphqlapi` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an AWS AppSync GraphQL API has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the GraphQL API doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the GraphQL API isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an AWS AppSync GraphQL API, see [TagResource](../../../appsync/latest/APIReference/API_TagResource.md "../../../appsync/latest/APIReference/API_TagResource.md") in the _AWS AppSync API Reference_.

## [AppSync.5] AWS AppSync GraphQL APIs should not be authenticated with API keys

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-6

**Category:** Protect > Secure access management > Passwordless authentication

**Severity:** High

**Resource type:**
`AWS::AppSync::GraphQLApi`

**AWS Config rule:**
[`appsync-authorization-check`](../../../config/latest/developerguide/appsync-authorization-check.md "../../../config/latest/developerguide/appsync-authorization-check.md")

**Schedule type:** Change triggered

**Parameters:**

- `AllowedAuthorizationTypes`: `AWS_LAMBDA, AWS_IAM, OPENID_CONNECT, AMAZON_COGNITO_USER_POOLS` (not customizable)

This control checks whether your application uses an API key to interact with an AWS AppSync GraphQL API. The control
fails if an AWS AppSync GraphQL API is authenticated with an API key.

An API key is a hard-coded value in your application that is generated by the AWS AppSync service when you create an
unauthenticated GraphQL endpoint. If this API key is compromised, your endpoint is vulnerable to unintended access. Unless you are
supporting a publicly accessible application or website, we don't recommend using an API key for authentication.

### Remediation

To set an authorization option for your AWS AppSync GraphQL API, see [Authorization and authentication](../../../appsync/latest/devguide/security-authz.md "../../../appsync/latest/devguide/security-authz.md") in the _AWS AppSync Developer Guide_.

## [AppSync.6] AWS AppSync API caches should be encrypted in transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::AppSync::ApiCache`

**AWS Config rule:**
[appsync-cache-ct-encryption-in-transit](../../../config/latest/developerguide/appsync-cache-ct-encryption-in-transit.md "../../../config/latest/developerguide/appsync-cache-ct-encryption-in-transit.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS AppSync API cache is encrypted in transit. The control fails if the API cache isn't
encrypted in transit.

Data in transit refers to data that moves from one location to another, such as between nodes in your cluster or between your cluster and your application. Data may move across the internet or within a private network. Encrypting data in transit reduces the risk that an unauthorized user can eavesdrop on network traffic.

###### Note

Due to AWS AppSync implementing a service-level change that makes encryption in transit mandatory for all API caches, this control will be retired and removed from all applicable standards on March 9, 2026.

### Remediation

You can't change the encryption settings after enabling caching for your AWS AppSync API. Instead, you must delete the cache and
and recreate it with encryption enabled. For more information, see [Cache encryption](../../../appsync/latest/devguide/enabling-caching.md#caching-encryption "../../../appsync/latest/devguide/enabling-caching.md#caching-encryption") in the _AWS AppSync Developer Guide_.
