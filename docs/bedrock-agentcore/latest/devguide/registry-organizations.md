# Using AWS Agent Registry with AWS Organizations

AWS Agent Registry integrates with AWS Organizations so that you can automatically catalog supported resources across your organization’s member accounts in a single registry.

When you enable **auto-detection** for a registry, supported resources — AgentCore Runtimes and Gateways — in your organization’s member accounts are automatically cataloged as registry records, with no setup required in the member accounts. A registry configured for organization-wide auto-detection is called an **organization-scoped registry**; it stays in sync as resources are created, updated, or deleted, and as accounts join or leave the organization.

This page explains how auto-detection works with AWS Organizations, how to enable it, and how to manage the records it produces.

###### Note

Auto-detection populates a registry from resources it discovers. You can still create and manage records manually in the same registry. Records created by auto-detection are marked so you can tell them apart from records you add yourself.

## How auto-detection works with AWS Organizations

### Accounts

Two accounts take part in auto-detection:

- **Management account** – The management account of your AWS organization enables trusted access for auto-detection and registers the delegated administrator. These are AWS Organizations operations that only the management account can perform.
- **Registry administrator** – The account that owns the organization-scoped registry and its auto-detected records. We recommend using a **delegated administrator** account for this, following the AWS security best practice of least privilege. The management account can also own the registry, but we don’t recommend this.

###### Note

An organization can have only one active organization-scoped registry per Region. Create it in either the management account or the delegated administrator — if one already exists in the organization in that Region, creating another is rejected.

### What auto-detection discovers

When auto-detection is enabled for an organization-scoped registry, it discovers the following resource types from your member accounts:

- Amazon Bedrock AgentCore Runtimes (`AWS::BedrockAgentCore::Runtime`)
- Amazon Bedrock AgentCore Gateways (`AWS::BedrockAgentCore::Gateway`)

Auto-detection discovers both resources that already exist when you enable the feature and resources that are created afterward.

### How detected resources become records

For each discovered resource, AWS Agent Registry creates a registry record in the administrator’s registry. Each auto-detected record includes a **provenance** entry that links it back to the source resource — containing the source resource’s ARN (`sourceId`), type (`sourceType`), and the relation `DETECTED_FROM`. You can use provenance to trace any record back to the resource — and the member account — it originated from.

Auto-detection is fully managed. After it’s enabled, there’s nothing to install or configure in individual member accounts — no agents, no per-account permissions, and no member-account resources to set up.

### How resource fields map to record fields

The following tables show how auto-detection maps properties from the source resource to registry record fields.

#### AgentCore Runtime → Registry record

| Source (Runtime property)                                  | Record field                                                                                           | Notes                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account ID, Region, Resource ID                            | `name`                                                                                                 | Auto-generated as `aws-autodetected-*<accountId>*-*<region>*-*<resourceId>*`. Not the runtime’s display name (`AgentRuntimeName`).                                                                                                                                                                                                                                                           |
| `ProtocolConfiguration.ServerProtocol`                     | `recordType`                                                                                           | Always `AGENT`. Every runtime protocol (`MCP`, `HTTP`, `A2A`, `AGUI`) maps to `AGENT`, because auto-detection can’t distinguish a standalone MCP server from an agent that exposes an MCP interface. You can narrow a runtime-detected record from `AGENT` to `MCP` yourself — see [Enriching auto-detected records](#registry-organizations-enriching "#registry-organizations-enriching"). |
| `ProtocolConfiguration.ServerProtocol`                     | Descriptor type (within `descriptors`)                                                                 | `MCP` → `mcpServer`; `HTTP` → `http`; `A2A` → `a2aAgentCard`; `AGUI` → `agui`. Defaults to `http` if absent or unrecognized.                                                                                                                                                                                                                                                                 |
| `AgentRuntimeVersion`                                      | `recordVersion`                                                                                        | Set from the runtime version at first detection, then treated as a value you own — a later change to the runtime’s version doesn’t change it (see [Enriching auto-detected records](#registry-organizations-enriching "#registry-organizations-enriching")). Defaults to `"1"` if absent.                                                                                                    |
| Constructed from runtime ARN and Region                    | Endpoint URL (within `descriptors`)                                                                    | Format: `https://bedrock-agentcore.*<region>*.amazonaws.com/runtimes/*<url-encoded-arn>*/invocations?qualifier=DEFAULT`                                                                                                                                                                                                                                                                      |
| Runtime ARN                                                | `provenance[].sourceId`                                                                                | The full ARN of the source runtime.                                                                                                                                                                                                                                                                                                                                                          |
| `AWS::BedrockAgentCore::Runtime`                           | `provenance[].sourceType`                                                                              | Constant for all runtime records.                                                                                                                                                                                                                                                                                                                                                            |
| `ProtocolConfiguration.ServerProtocol`                     | `provenance[].sourceDetails.agentcoreRuntime.protocolConfiguration.serverProtocol`                     | Raw wire value (for example, `MCP`, `HTTP`, `A2A`).                                                                                                                                                                                                                                                                                                                                          |
| `AuthorizerConfiguration.CustomJWTAuthorizer.DiscoveryUrl` | `provenance[].sourceDetails.agentcoreRuntime.authorizerConfiguration.customJWTAuthorizer.discoveryUrl` | Present only for runtimes with JWT authorization. Other authorizer fields (`AllowedClients`, `AllowedAudience`, `AllowedScopes`) are not carried into the record.                                                                                                                                                                                                                            |
| `WorkloadIdentityDetails.WorkloadIdentityArn`              | `provenance[].sourceDetails.agentcoreRuntime.workloadIdentityDetails.workloadIdentityArn`              | Present when the runtime has a workload identity configured.                                                                                                                                                                                                                                                                                                                                 |

#### AgentCore Gateway → Registry record

| Source (Gateway property)                                  | Record field                                                                                           | Notes                                                                                                                                                             |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account ID, Region, Resource ID                            | `name`                                                                                                 | Auto-generated as `aws-autodetected-*<accountId>*-*<region>*-*<resourceId>*`. Not the gateway’s display name (`Name`).                                            |
| `ProtocolType`                                             | `recordType`                                                                                           | `MCP` → `GATEWAY`. A gateway-detected record is always `GATEWAY` and can’t be changed to another type. Other protocol types are not currently supported.          |
| `ProtocolType`                                             | Descriptor type (within `descriptors`)                                                                 | `MCP` → `mcpServer`. Other protocol types are not currently supported.                                                                                            |
| (hardcoded)                                                | `recordVersion`                                                                                        | Always `"1"`. Gateways have no version concept; updates are in-place.                                                                                             |
| `GatewayUrl`                                               | Endpoint URL (within `descriptors`)                                                                    | Taken verbatim from the gateway configuration (for example, `\https://*<gateway-id>*.gateway.bedrock-agentcore.*<region>*.amazonaws.com/mcp`).                    |
| Gateway ARN                                                | `provenance[].sourceId`                                                                                | The full ARN of the source gateway.                                                                                                                               |
| `AWS::BedrockAgentCore::Gateway`                           | `provenance[].sourceType`                                                                              | Constant for all gateway records.                                                                                                                                 |
| `ProtocolType`                                             | `provenance[].sourceDetails.agentcoreGateway.protocolType`                                             | Raw wire value (for example, `MCP`).                                                                                                                              |
| `AuthorizerType`                                           | `provenance[].sourceDetails.agentcoreGateway.authorizerType`                                           | For example, `AWS_IAM` or `CUSTOM_JWT`.                                                                                                                           |
| `AuthorizerConfiguration.CustomJWTAuthorizer.DiscoveryUrl` | `provenance[].sourceDetails.agentcoreGateway.authorizerConfiguration.customJWTAuthorizer.discoveryUrl` | Present only for gateways with JWT authorization. Other authorizer fields (`AllowedClients`, `AllowedAudience`, `AllowedScopes`) are not carried into the record. |
| `WorkloadIdentityDetails.WorkloadIdentityArn`              | `provenance[].sourceDetails.agentcoreGateway.workloadIdentityDetails.workloadIdentityArn`              | Present when the gateway has a workload identity configured.                                                                                                      |

### How the catalog stays in sync

After auto-detection is active, AWS Agent Registry keeps the registry aligned with the state of your organization:

| Event in a member account                                          | Effect on the registry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A supported resource already exists when you enable auto-detection | A record is created for it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| A supported resource is created                                    | A record is created for it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| A supported resource is updated                                    | When a source-derived attribute changes (such as the resource’s protocol, authorizer, or endpoint), the record’s source-derived fields — its descriptor and provenance — are refreshed, while the values you set yourself (such as `name`, `description`, and `recordVersion`) are preserved. If the protocol changes, the descriptor is reconciled to the new protocol and `recordType` resets to the source default (`AGENT` for a runtime). If you had already approved the record, the refresh is applied as a new `Draft` revision that must be approved, while your previously approved revision stays discoverable — see [Approval](#registry-organizations-approval "#registry-organizations-approval"). |
| A supported resource is deleted                                    | Its record is removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| An account joins the organization                                  | Its supported resources are detected and added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| An account leaves (or is removed from) the organization            | All records detected from that account are removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

###### Note

If you deprecate an auto-detected record (set its status to `DEPRECATED`), auto-detection stops syncing changes from the source resource to that record. Subsequent updates to the source resource — such as protocol, authorizer, or endpoint changes — are not applied to the deprecated record. Use deprecation when you want to freeze a specific auto-detected record while re-sync continues to happen for the other auto-detected records within the registry.

### The auto-detection setting versus its status

Auto-detection involves two related fields — one that you set, and one that the service reports:

- **`autoDetectionConfiguration.enabled`** is the setting you control. You set it when you create or update the registry to request that auto-detection be on (`true`) or off (`false`). AWS Agent Registry also turns it off for you in a couple of teardown cases: when trusted access for auto-detection is disabled, or when a delegated administrator that owns the registry is deregistered.
- **`autoDetection.status`** is the state the service reports — `ACTIVE` or `INACTIVE`. You don’t set it. AWS Agent Registry makes it `ACTIVE` only when `enabled` is `true` and the organization meets the auto-detection preconditions; otherwise it’s `INACTIVE`.

In short, `enabled` is what you request, and `autoDetection.status` is what’s actually in effect. Setting `enabled` to `true` is necessary but not sufficient for `autoDetection.status` to be `ACTIVE`.

## Prerequisites

Before you enable auto-detection, make sure you have the following:

- Your accounts are members of an organization in AWS Organizations, with all features enabled. For more information, see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the _AWS Organizations User Guide_.
- You can sign in to the **management account** to enable trusted access and register the delegated administrator.
- You can sign in to the account that will be the **registry administrator** — the delegated administrator is recommended — to create the organization-scoped registry.
- You have the permissions described in [Permissions](#registry-organizations-permissions "#registry-organizations-permissions") in each of those accounts.

## Permissions

### In the management account

To enable trusted access and register the delegated administrator, the caller in the management account needs these AWS Organizations permissions:

- `organizations:EnableAWSServiceAccess`
- `organizations:RegisterDelegatedAdministrator`
- `organizations:DeregisterDelegatedAdministrator` and `organizations:DisableAWSServiceAccess` to turn the feature off later

The management account also needs `iam:CreateServiceLinkedRole` to create the AWS Agent Registry service-linked role. This role must exist in the management account before an organization-scoped registry can be created — see Step 1 in "Enabling auto-detection across your organization".

### In the registry administrator account

To create and manage the organization-scoped registry and its records, the caller needs AWS Agent Registry permissions, including `agent-registry:CreateRegistry`, `agent-registry:UpdateRegistry`, `agent-registry:GetRegistry`, `agent-registry:ListRegistryRecords`, and `agent-registry:UpdateRegistryRecord`. For the full list and example policies, see [IAM Permissions](registry-iam-permissions.md "registry-iam-permissions.md").

## Enabling auto-detection across your organization

Enabling auto-detection is a three-step process: the management account enables trusted access and registers a delegated administrator, and then the administrator creates an organization-scoped registry with auto-detection turned on.

###### Note

The steps in this section must be performed in order. After you register the delegated administrator (step 2), it can take a short time for the organization state to propagate. Until it does, creating an organization-scoped registry (step 3) is rejected. See [Troubleshooting](#registry-organizations-troubleshooting "#registry-organizations-troubleshooting").

### Step 1: Enable trusted access and create the service-linked role (management account)

Sign in to the management account, enable trusted access for auto-detection, and make sure the management account has the AWS Agent Registry service-linked role.

###### Important

The AWS Agent Registry service-linked role (`AWSServiceRoleForAgentRegistry`) must exist in the **management account** before an organization-scoped registry can be created — including when the registry is created by the delegated administrator rather than the management account. Enabling trusted access from the AWS Agent Registry console creates this role for you. If you set up with the AWS CLI or API, create it explicitly with the second command below.

If the organization-scoped registry is encrypted with a customer managed key, the service-linked role must _also_ exist in the **registry administrator** account (typically the delegated administrator) before `CreateRegistry` is called. The KMS key policy in that account names the service-linked role as a principal, and IAM rejects any key policy that references a principal that does not yet exist. Enabling trusted access provisions the role in the registry administrator account through ASLRP, but propagation can be briefly delayed — until the role lands there, `CreateRegistry` fails against the KMS key policy. To avoid this race, have the registry administrator account create the role directly with `aws iam create-service-linked-role --aws-service-name agent-registry.amazonaws.com`.

Organization-scoped registries that do not use a customer managed key don’t need this extra step — `CreateRegistry` creates the service-linked role in the registry administrator account if it isn’t already there.

**Console**

1. Open the [AWS Agent Registry console — Settings](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/settings "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/settings").
2. In the **AWS Organizations integration details** section, choose **Edit**.
3. On the **AWS Organizations settings** page, under **Trusted access**, turn on the **Enabled** toggle. This authorizes AWS Agent Registry to discover resources across member accounts and creates the `AWSServiceRoleForAgentRegistry` service-linked role in this account.
4. Under **Delegated administrator account**, enter the 12-digit account ID of the member account you want to use as the registry administrator.
5. Choose **Save**.

**AWS CLI**

Enable trusted access for auto-detection:

```
aws organizations enable-aws-service-access \
  --service-principal agent-registry.amazonaws.com
```

Create the AWS Agent Registry service-linked role in the management account:

```
aws iam create-service-linked-role \
  --aws-service-name agent-registry.amazonaws.com
```

### Step 2: Register a delegated administrator (management account)

Still in the management account, register the account that will own the organization-scoped registry as the delegated administrator for auto-detection.

###### Note

The account you register must already be a member of your organization. If it isn’t, add it in AWS Organizations before running this step.

**Console**

The delegated administrator is registered as part of Step 1 above. When you configure trusted access and enter the delegated administrator account ID on the AWS Organizations settings page, both steps are completed together.

**AWS CLI**

Replace `<delegated-admin-account-id>` with the 12-digit account ID of the account you want to use as the registry administrator.

```
aws organizations register-delegated-administrator \
  --account-id <delegated-admin-account-id> \
  --service-principal agent-registry.amazonaws.com
```

### Step 3: Create an organization-scoped registry (registry administrator)

Sign in to the delegated administrator account and create a registry with an auto-detection configuration that sets `scope` to `ORGANIZATION` and `enabled` to `true`. `enabled` must be `true` for auto-detection to activate — if it’s `false`, the registry is created but its auto-detection status never becomes `ACTIVE` and no resources are detected.

**Console**

1. Open the [AWS Agent Registry console — Registry](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries").
2. Choose **Create registry**.
3. Complete the required fields (**Name**, and optionally **Description**, **Discovery Authorization**, **Record approval**, **KMS key**, and **Tags**).
4. Expand the **Auto-detection** section.
5. Turn on the **Enable auto-detection** toggle. The **Scope** is set to **Organization** and the service access permissions are displayed.
6. Choose **Create registry**.

###### Note

Auto-detection runs in the current Region. To discover resources in other Regions, create a separate registry with auto-detection enabled in each Region. Only one registry can have auto-detection enabled per Region.

**AWS CLI**

```
aws agent-registry-control create-registry \
  --name "my-organization-registry" \
  --description "Auto-detected resources across my organization" \
  --auto-detection-configuration '{"scope":"ORGANIZATION","enabled":true}' \
  --region us-east-1
```

When you run `get-registry` or `list-registries`, you see two separate status fields. The registry `status` field starts as `CREATING` and transitions to `READY` when provisioning completes. The `autoDetection.status` field is tracked separately: it is `INACTIVE` until auto-detection is running, then becomes `ACTIVE`. When the registry `status` is `READY` and `autoDetection.status` is `ACTIVE`, records begin to appear for supported resources across your member accounts.

###### Note

Setting `enabled` to `true` requests auto-detection but is not sufficient on its own. The `autoDetection.status` field becomes `ACTIVE` only when both preconditions are met: trusted access is enabled for auto-detection, and the registry is owned by the management account or a registered delegated administrator. These conditions also have to propagate, which can take a short time after you enable trusted access or register a delegated administrator.

### Verify that resources are being detected

List the registry’s records and look for records created by auto-detection:

```
aws agent-registry-control list-registry-records \
  --registry-id <registry-id-or-arn> \
  --region us-east-1
```

###### Note

On first setup, auto-detection discovers the resources that already exist in your member accounts, and this initial discovery can take up to 20 minutes. Records for preexisting resources might not appear immediately.

For how to tell auto-detected records apart from records you add yourself, see [Identifying auto-detected records](#registry-organizations-identifying "#registry-organizations-identifying").

## Working with auto-detected records

### Identifying auto-detected records

Auto-detected records are identified by two characteristics:

- Their record name is prefixed with `aws-autodetected-`.
- They include a provenance entry whose relation is `DETECTED_FROM`, whose `sourceId` is the ARN of the source resource, and whose `sourceType` identifies the resource type (for example, `AWS::BedrockAgentCore::Runtime` or `AWS::BedrockAgentCore::Gateway`).

Use the name prefix to quickly filter for auto-detected records, and the provenance to trace a record back to the resource — and the member account — it came from.

**Console**

You can identify auto-detected records in the console in the following ways:

- **Registry records table** – The records table on the registry details page includes three columns for auto-detected records: **Auto-detection** (Yes/No), **Source type** (for example, Bedrock AgentCore runtime), and **Source ID** (the source resource ARN).
- **Property filter** – Use the property filter in the records table to filter by **Auto-detection = Yes** or **Auto-detection = No**.
- **Record details page** – For auto-detected records, the record details page displays an expandable **Provenance** section showing the relation (Detected from), Source ARN, Source type, Server protocol, and Workload identity ARN.

### Enriching auto-detected records

You can edit an auto-detected record to add your own information — for example, a more descriptive description — using `update-registry-record`. Your edits are preserved; auto-detection updates the record’s source-derived fields without overwriting the values you set.

```
aws agent-registry-control update-registry-record \
  --registry-id <registry-id-or-arn> \
  --record-id <record-id> \
  --description '{"optionalValue":"MCP server exposing the order-management API as agent tools"}' \
  --region us-east-1
```

AWS Agent Registry separates the fields you own from the fields auto-detection owns on an auto-detected record:

| Field                                  | Editable by you | Behavior                                                                                                                                                                                                                                                |
| -------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`, `description`, `recordVersion` | Yes             | Accepted and preserved; auto-detection does not overwrite them when it refreshes the record from the source.                                                                                                                                            |
| Descriptor `data`                      | Yes             | You can enrich it.                                                                                                                                                                                                                                      |
| `recordType`                           | Limited         | You can narrow a runtime-detected record from `AGENT` to `MCP`. Any other change (for example to `SKILL`, `GATEWAY`, or `CUSTOM`) is rejected, and a gateway-detected record is always `GATEWAY`.                                                       |
| Descriptor protocol (kind)             | No              | Derived from the source resource; a change is rejected.                                                                                                                                                                                                 |
| Descriptor source URL                  | No              | Derived from the source resource; you can’t change or clear it. To attach a credential provider for synchronization, supply the descriptor source with the same URL — see [Synchronizing records](registry-sync-records.md "registry-sync-records.md"). |
| `provenance`                           | No              | Links the record to its source resource; a change is rejected.                                                                                                                                                                                          |

###### Note

If the source resource’s protocol later changes, auto-detection reconciles the record’s descriptor to match the new protocol and resets `recordType` to `AGENT`, overriding a narrowing you made. Your other edits — such as `name` and `description` — are preserved.

For example, a runtime detected with the `MCP` protocol is cataloged as `recordType`
`AGENT` with an `mcpServer` descriptor, and you narrow the record to `MCP`. If that runtime is later updated to use the `A2A` protocol, the next refresh replaces the `mcpServer` descriptor with an `a2aAgentCard` descriptor and resets `recordType` from `MCP` back to `AGENT`. The `name`, `description`, and `recordVersion` you set remain unchanged.

### Deleting auto-detected records

You cannot delete an auto-detected record while auto-detection is enabled (`autoDetectionConfiguration.enabled` is `true`). Auto-detection manages the lifecycle of these records — records are removed automatically when the source resource is deleted or the member account leaves the organization.

To manually delete an auto-detected record, you must first disable auto-detection on the registry by setting `enabled` to `false`. After auto-detection is disabled, you can delete auto-detected records the same way you delete any other record.

### Approval

Auto-detected records follow the same approval workflow as records you create manually: a record must be in `APPROVED` status to be discoverable through the registry’s discovery APIs and the Record directory. If the registry is configured for auto-approval, records become discoverable without manual review; otherwise a curator reviews and approves them. For more information, see [Curating the registry](registry-curating.md "registry-curating.md").

When auto-detection refreshes a record you had already approved — for example, because the source resource’s protocol changed — the refreshed content is written as a new `Draft` revision and is not discoverable until it is approved. The revision you previously approved stays discoverable in the meantime, so discovery is uninterrupted. Approve the refreshed revision to publish it — if the registry uses auto-approval, submitting it for approval approves it immediately; otherwise a curator reviews and approves it. A refresh that changes no source-derived field leaves the record unchanged.

## Turning off auto-detection

### Disable auto-detection on the registry

To stop discovering resources, update the registry to set auto-detection `enabled` to `false`. You must disable auto-detection before you can delete an organization-scoped registry.

To delete an organization-scoped registry, complete these steps in order:

1. Disable auto-detection on the registry.
2. Delete all registry records.
3. Delete the registry.

```
aws agent-registry-control update-registry \
  --registry-id <registry-id-or-arn> \
  --auto-detection-configuration '{"optionalValue":{"scope":"ORGANIZATION","enabled":false}}' \
  --region us-east-1
```

The update is asynchronous: the registry moves to `UPDATING` and returns to `READY` when the change takes effect.

### Deregister the delegated administrator or disable trusted access

To remove auto-detection at the organization level, the management account can deregister the delegated administrator and disable trusted access:

```
aws organizations deregister-delegated-administrator \
  --account-id <delegated-admin-account-id> \
  --service-principal agent-registry.amazonaws.com
```

```
aws organizations disable-aws-service-access \
  --service-principal agent-registry.amazonaws.com
```

Disabling trusted access, or deregistering a delegated administrator that owns the registry, also sets the registry’s `autoDetectionConfiguration.enabled` to `false` and its `autoDetection.status` to `INACTIVE`. The status reason shows "Trusted access was disabled for the organization."

###### Important

If you re-enable trusted access after disabling it, auto-detection does not resume automatically. You must manually update the registry’s auto-detection configuration to set `enabled` back to `true`.

## Troubleshooting

For troubleshooting auto-detection issues, see [Auto-detection errors](registry-troubleshooting.md#registry-troubleshooting-auto-detection "registry-troubleshooting.md#registry-troubleshooting-auto-detection") in the main troubleshooting page.
