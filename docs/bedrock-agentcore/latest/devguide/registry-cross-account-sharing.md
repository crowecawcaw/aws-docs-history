# Sharing a registry across accounts with AWS RAM

You can share an AWS Agent Registry registry with other AWS accounts using AWS Resource Access Manager (RAM). With RAM sharing, accounts outside your own can discover, publish to, or administer records in your registry—without owning the registry itself.

When you share a registry, RAM creates and manages a resource-based policy on your behalf. You choose a managed permission that controls which actions the consumer account can perform, and RAM handles the rest.

## How cross-account sharing works

Cross-account sharing follows a three-step process:

1. **Registry owner shares the registry**—The owner creates a RAM resource share, selects a managed permission, and adds one or more consumer account IDs as principals. RAM attaches a resource-based policy to the registry.
2. **Consumer accepts the invitation**—For accounts outside the owner’s AWS Organization, RAM sends an invitation that the consumer must accept. For accounts within the same organization (with [RAM sharing with Organizations enabled](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs")), acceptance is automatic—no invitation is required.
3. **Consumer accesses the shared registry**—The consumer calls AWS Agent Registry APIs using their own credentials against the owner’s registry ARN. The actions they can perform depend on the managed permission attached to the share.

Key characteristics:

- Only the registry owner can initiate sharing.
- RAM creates and manages the resource-based policy on your behalf—you select a managed permission to control which actions it grants.
- The managed permission you select determines what the consumer can do (discover, publish, or administer).
- Control-plane registry mutations (`UpdateRegistry`, `DeleteRegistry`) always remain with the owner—they cannot be delegated through RAM.

## Prerequisites

Before you share a registry, make sure you meet the following requirements:

**In the registry owner account:**

- The registry is in `READY` status.
- The caller has IAM permissions for AWS RAM operations (`ram:CreateResourceShare`, `ram:AssociateResourceShare`, `ram:DisassociateResourceShare`, `ram:DeleteResourceShare`, `ram:GetResourceShares`, `ram:GetResourceShareAssociations`) and `agent-registry:PutResourcePolicy`.

**In the consumer account:**

- The caller has IAM permissions for the AWS Agent Registry actions that correspond to the managed permission attached to the share.
- For external (cross-organization) shares, the caller also needs `ram:GetResourceShareInvitations` and `ram:AcceptResourceShareInvitation` (or `ram:RejectResourceShareInvitation`).

**For organization-internal sharing:**

- AWS RAM sharing with AWS Organizations must be enabled. For more information, see [Enable sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.
- When organization sharing is enabled, accounts within the organization do not need to accept invitations—the share takes effect automatically.

## RAM managed permissions for AWS Agent Registry

When you share a registry, you attach an AWS RAM managed permission that controls which actions the consumer account can perform. AWS Agent Registry provides four managed permissions: one default and three role-based. These let you grant the minimum access needed for each use case.

### AWSRAMDefaultPermissionAgentRegistryReadOnly

This is the default permission for the `agent-registry:Registry` resource type. When you create a resource share without specifying a permission, RAM attaches this permission automatically. It grants read-only access to registry metadata and records—both control-plane reads and data-plane discovery—but does not allow publishing records or invoking the registry’s Model Context Protocol (MCP) endpoint.

**Use case:** Share a registry for visibility and auditing. The consumer can browse and search the catalog, but cannot publish, modify, or invoke tools through the MCP endpoint.

**Permissions granted:**

- `agent-registry:GetRegistry`—View registry configuration and metadata.
- `agent-registry:GetRegistryRecord`—Read individual record details (control plane).
- `agent-registry:ListRegistryRecords`—List all records in the registry (control plane).
- `agent-registry:SearchDiscoverableRegistryRecords`—Search approved records using hybrid search.
- `agent-registry:GetDiscoverableRegistryRecord`—Get full details of an approved record (data plane).
- `agent-registry:ListDiscoverableRegistryRecords`—List approved records (data plane).

### AWSRAMPermissionAgentRegistryForConsumer

This permission grants data-plane discovery access plus the ability to invoke the registry’s MCP endpoint. Use this permission for the **consumer** persona—AI agents or human users who need to discover and use tools registered in the catalog.

**Use case:** Share a registry with an account whose agents need to discover tools and invoke them through the MCP endpoint. The consumer cannot create or manage records.

**Permissions granted:**

- `agent-registry:SearchDiscoverableRegistryRecords`—Search approved records.
- `agent-registry:GetDiscoverableRegistryRecord`—Get full details of an approved record.
- `agent-registry:ListDiscoverableRegistryRecords`—List approved records.
- `agent-registry:InvokeRegistryMcp`—Invoke the registry’s MCP endpoint.

### AWSRAMPermissionAgentRegistryForPublisher

This permission grants everything the Consumer permission grants, plus control-plane access to create, update, delete, and submit records for approval. Use this permission for the **publisher** persona—builders in a shared account who contribute resources to a centrally owned registry.

**Use case:** Share a registry with a team that needs to publish MCP servers, agents, or tools into your catalog. The publisher can manage their own records and discover others, but cannot approve or reject records.

**Permissions granted:**

- `agent-registry:GetRegistry`—View registry configuration.
- `agent-registry:CreateRegistryRecord`—Create new records.
- `agent-registry:UpdateRegistryRecord`—Update existing records.
- `agent-registry:DeleteRegistryRecord`—Delete records.
- `agent-registry:GetRegistryRecord`—Read individual record details.
- `agent-registry:ListRegistryRecords`—List all records.
- `agent-registry:SubmitRegistryRecordForApproval`—Submit records for curator review.
- `agent-registry:SearchDiscoverableRegistryRecords`—Search approved records.
- `agent-registry:GetDiscoverableRegistryRecord`—Get full details of an approved record.
- `agent-registry:ListDiscoverableRegistryRecords`—List approved records.
- `agent-registry:InvokeRegistryMcp`—Invoke the registry’s MCP endpoint.

### AWSRAMPermissionAgentRegistryForAdmin

This permission grants everything the Publisher permission grants, plus the ability to approve, reject, or deprecate records. Use this permission for the **admin** persona—a delegated administrator in another account who curates the shared registry on behalf of the owner.

**Use case:** Share a registry with an account that manages the full record lifecycle—publishing, reviewing, and approving records—without owning the registry infrastructure itself. The admin cannot update or delete the registry.

**Permissions granted:**

- `agent-registry:GetRegistry`—View registry configuration.
- `agent-registry:CreateRegistryRecord`—Create new records.
- `agent-registry:UpdateRegistryRecord`—Update existing records.
- `agent-registry:UpdateRegistryRecordStatus`—Approve, reject, or deprecate records.
- `agent-registry:DeleteRegistryRecord`—Delete records.
- `agent-registry:GetRegistryRecord`—Read individual record details.
- `agent-registry:ListRegistryRecords`—List all records.
- `agent-registry:SubmitRegistryRecordForApproval`—Submit records for curator review.
- `agent-registry:SearchDiscoverableRegistryRecords`—Search approved records.
- `agent-registry:GetDiscoverableRegistryRecord`—Get full details of an approved record.
- `agent-registry:ListDiscoverableRegistryRecords`—List approved records.
- `agent-registry:InvokeRegistryMcp`—Invoke the registry’s MCP endpoint.

### Choosing a managed permission

| If you want the consumer to…​                              | Choose this permission                         |
| ---------------------------------------------------------- | ---------------------------------------------- |
| Browse and search the catalog (read-only, no MCP invoke)   | `AWSRAMDefaultPermissionAgentRegistryReadOnly` |
| Discover tools and invoke the MCP endpoint                 | `AWSRAMPermissionAgentRegistryForConsumer`     |
| Publish and manage records + discover tools                | `AWSRAMPermissionAgentRegistryForPublisher`    |
| Full record lifecycle (publish + approve/reject/deprecate) | `AWSRAMPermissionAgentRegistryForAdmin`        |

###### Tip

We recommend the **Consumer** permission for typical sharing scenarios where the consumer account’s agents need to discover and invoke tools.

### Creating a customer-managed permission

For advanced use cases—such as restricting access to only records created by a specific account using condition keys—you can create a customer-managed RAM permission. Customer-managed permissions let you define custom `Condition` blocks that reference AWS Agent Registry condition keys.

For more information about creating customer-managed permissions, see [Shareable resources](../../../ram/latest/userguide/shareable.md "../../../ram/latest/userguide/shareable.md") in the _AWS RAM User Guide_.

For the condition keys available for AWS Agent Registry, see [Condition keys for fine-grained record access](#registry-cross-account-condition-keys "#registry-cross-account-condition-keys").

## Share a registry with another account

Only the registry owner can initiate sharing.

### Console

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries").
2. Choose the registry you want to share.
3. On the registry details page, scroll down to the **Registry sharing** section.
4. Choose **Share registry**.
5. In the **Share registry** panel, under **AWS Resource Access Manager (RAM) share**, choose one of the following:

   - **AWS Organization-only RAM share**—The accounts you specify must be in your AWS Organization. Sharing with AWS Organizations must be enabled from the [AWS RAM Settings page](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs").
   - **External RAM share**—The accounts can be in your AWS Organization or outside of it.

6. Under **AWS RAM share managed permission**, select a managed permission from the dropdown. This is required—you must select a permission before you can share.

For help choosing a permission, see [Choosing a managed permission](#registry-cross-account-choosing-permission "#registry-cross-account-choosing-permission"). 7. Under **Accounts**, enter the AWS account ID of each account you want to share with. Choose **Add another account** to add more. 8. Choose **Share**.

The **Registry sharing** table shows the association. For external shares, the **Association status** shows **Associating** until the consumer accepts the invitation.

### AWS CLI

Use the `create-resource-share` command to create a RAM resource share with the registry ARN and the consumer account ID:

```
aws ram create-resource-share \
  --name "my-registry-share" \
  --resource-arns "arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId" \
  --principals "444455556666" \
  --permission-arns "arn:aws:ram::aws:permission/AWSRAMPermissionAgentRegistryForConsumer" \
  --allow-external-principals
```

Replace the following:

- `my-registry-share`—A descriptive name for the resource share.
- The registry ARN—The ARN of the registry you want to share.
- `444455556666`—The AWS account ID of the consumer.
- The permission ARN—The ARN of the managed permission to attach. Omit `--permission-arns` to use the default `AWSRAMDefaultPermissionAgentRegistryReadOnly`.
- `--allow-external-principals`—Include this flag if the consumer account is outside your AWS Organization. Omit it for organization-internal sharing.

Verify the share is active:

```
aws ram get-resource-share-associations \
  --association-type RESOURCE \
  --resource-arns "arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId"
```

## Accept a sharing invitation

When a registry is shared with an account outside the owner’s AWS Organization, the consumer account receives an invitation. The consumer must accept the invitation before they can access the shared registry.

###### Note

If both accounts are in the same AWS Organization and AWS RAM sharing with Organizations is enabled, acceptance is automatic—no invitation is required and you can skip this step.

### Console

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries").
2. At the top of the **Registry** overview page, a blue banner shows pending share requests (up to 3 are displayed at a time):

_"New registry share request—Account 111122223333 wants to share registry MyRegistryId with you on Aug 11, 2026."_ 3. Choose **Accept**.

After you accept, the shared registry appears in the consumer’s registry list. You can also choose **View invitation details** to see the share in the AWS RAM console.

### AWS CLI

Find the pending invitation:

```
aws ram get-resource-share-invitations \
  --query 'resourceShareInvitations[?status==`PENDING`]'
```

Accept the invitation using the invitation ARN from the response:

```
aws ram accept-resource-share-invitation \
  --resource-share-invitation-arn "arn:aws:ram:us-east-1:111122223333:resource-share-invitation/12345678-abcd-efgh-ijkl-123456789012"
```

## Reject a sharing invitation

If you do not want to access a shared registry, you can reject the invitation. Rejecting an invitation means you will not have access to the shared registry.

### Console

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries").
2. At the top of the **Registry** overview page, locate the pending share request banner.
3. Choose **Reject**.

### AWS CLI

Find the pending invitation:

```
aws ram get-resource-share-invitations \
  --query 'resourceShareInvitations[?status==`PENDING`]'
```

Reject the invitation:

```
aws ram reject-resource-share-invitation \
  --resource-share-invitation-arn "arn:aws:ram:us-east-1:111122223333:resource-share-invitation/12345678-abcd-efgh-ijkl-123456789012"
```

###### Note

After you accept a sharing invitation, permissions might take a short time to propagate.

## Access a shared registry

After the share is active (either through accepting an invitation or automatic organization-level acceptance), the consumer calls AWS Agent Registry APIs using their own credentials against the owner’s registry ARN. The specific operations available depend on the managed permission attached to the share.

**Example: Discover records as a consumer**

```
# List approved records in the shared registry
aws agent-registry list-discoverable-registry-records \
  --registry-id "arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId"

# Search for tools
aws agent-registry search-discoverable-registry-records \
  --registry-ids "arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId" \
  --search-query "order management"

# Get full record details
aws agent-registry batch-get-discoverable-registry-record \
  --entries '[{"registryId":"arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId","recordIds":["arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId/record/MyRecordId"]}]'
```

**Example: Publish a record as a publisher**

```
aws agent-registry-control create-registry-record \
  --registry-id "arn:aws:agent-registry:us-east-1:111122223333:registry/MyRegistryId" \
  --name "my-mcp-server" \
  --display-name "Order Management MCP Server" \
  --record-type MCP \
  --descriptors '{"mcpServer": {"data": "{\"name\": \"order-mgmt\", \"description\": \"Order management tools\", \"version\": \"1.0.0\"}", "dataSchemaVersion": "2025-12-11"}}' \
  --record-version "1.0"
```

## Stop sharing with an account

To revoke a consumer’s access to your shared registry, remove the consumer account from the resource share.

### Console

1. Open the [AWS Agent Registry console](https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries "https://console.aws.amazon.com/agent-registry/home?region=us-east-1#/registries").
2. Choose the registry you are sharing.
3. On the registry details page, scroll down to the **Registry sharing** section.
4. Select the account you want to remove.
5. Choose **Stop sharing**.

The consumer immediately loses access to the registry. There might be a short propagation delay (up to 30 seconds) before access is fully revoked.

### AWS CLI

Use `disassociate-resource-share` to remove a consumer account from the share:

```
aws ram disassociate-resource-share \
  --resource-share-arn "arn:aws:ram:us-east-1:111122223333:resource-share/12345678-1234-1234-1234-123456789012" \
  --principals "444455556666"
```

Verify the principal is disassociated:

```
aws ram get-resource-share-associations \
  --association-type PRINCIPAL \
  --resource-share-arns "arn:aws:ram:us-east-1:111122223333:resource-share/12345678-1234-1234-1234-123456789012"
```

To delete the entire resource share (removing all consumer accounts at once):

```
aws ram delete-resource-share \
  --resource-share-arn "arn:aws:ram:us-east-1:111122223333:resource-share/12345678-1234-1234-1234-123456789012"
```

## Condition keys for fine-grained record access

AWS Agent Registry provides two service-specific condition keys. You can use these keys in customer-managed RAM permissions, IAM identity policies, and SCPs to control access at the individual record level. They are especially useful when sharing a registry across accounts, where you want a consumer account to act only on the records it owns or that originate from its own account, even though another account owns the registry itself.

Both keys are resolved at authorization time from the stored record and cannot be set from request input, so a consumer cannot spoof them to gain access to records that belong to other accounts.

### Registry record condition keys

The following condition keys apply to the record-level operations listed in the **API operations** column.

| Condition key                         | Type   | API operations                                                                                                                                                        | Description                                                                                                                                                                                                                                              |
| ------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent-registry:RecordCreatorAccount` | String | `GetRegistryRecord`, `UpdateRegistryRecord`, `DeleteRegistryRecord`, `SubmitRegistryRecordForApproval`, `UpdateRegistryRecordStatus`, `GetDiscoverableRegistryRecord` | Filters access by the AWS account ID of the principal that created the registry record. Resolved at authorization time from the stored record; cannot be set from request input.                                                                         |
| `agent-registry:RecordSourceAccount`  | String | `GetRegistryRecord`, `UpdateRegistryRecord`, `DeleteRegistryRecord`, `SubmitRegistryRecordForApproval`, `UpdateRegistryRecordStatus`, `GetDiscoverableRegistryRecord` | Filters access by the AWS account ID of the source resource associated with a registry record—for example, the account where an auto-detected resource resides. Resolved at authorization time from the stored record; cannot be set from request input. |

###### Note

These condition keys are evaluated only on operations that reference a specific record. They are _not_ evaluated on:

- `CreateRegistryRecord`—the record does not exist yet at creation time, so there is no stored creator or source account to compare against.
- `SearchDiscoverableRegistryRecords`, `ListRegistryRecords`, and `ListDiscoverableRegistryRecords`—these operations return summaries for all matching records regardless of condition-key restrictions. The keys apply to individual record-read and record-write operations, not to search or list enumeration.

If you need to keep records from other accounts entirely out of a consumer’s view, do not grant the search and list actions in the shared permission.

### Example: Restrict access to records the consumer created

The following customer-managed RAM permission allows a consumer to read, update, and delete only records where the creator account matches the consumer’s own account:

```
{
  "Effect": "Allow",
  "Action": [
    "agent-registry:GetDiscoverableRegistryRecord",
    "agent-registry:GetRegistryRecord",
    "agent-registry:UpdateRegistryRecord",
    "agent-registry:DeleteRegistryRecord"
  ],
  "Condition": {
    "StringEquals": {
      "agent-registry:RecordCreatorAccount": "${aws:PrincipalAccount}"
    }
  }
}
```

The `${aws:PrincipalAccount}` policy variable resolves dynamically at evaluation time—each consumer can only access records they themselves created, even within a shared registry.

### Example: Restrict access to records that originate from the consumer’s account

The following customer-managed RAM permission allows a consumer to read only records whose source resource resides in the consumer’s own account—useful when records are auto-detected from resources owned by the consumer:

```
{
  "Effect": "Allow",
  "Action": [
    "agent-registry:GetDiscoverableRegistryRecord",
    "agent-registry:GetRegistryRecord"
  ],
  "Condition": {
    "StringEquals": {
      "agent-registry:RecordSourceAccount": "${aws:PrincipalAccount}"
    }
  }
}
```

For instructions on creating a customer-managed RAM permission, see [Creating a customer-managed permission](../../../ram/latest/userguide/working-with-sharing-create-permission.md "../../../ram/latest/userguide/working-with-sharing-create-permission.md") in the _AWS RAM User Guide_.

## Troubleshooting

| Symptom                                                                                        | Likely cause                                                                                                                                                                     | Resolution                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Consumer gets `AccessDeniedException` after accepting the invitation                           | The share is not yet fully active, or the consumer’s IAM role is missing `agent-registry:*` permissions.                                                                         | Confirm the share status is `ACTIVE` using `aws ram get-resource-shares --resource-owner OTHER-ACCOUNTS`. Verify the consumer’s identity policy includes the actions granted by the managed permission.                                                              |
| Resource association status shows `FAILED` after creating the share                            | The registry ARN was not accepted by RAM.                                                                                                                                        | Confirm the ARN starts with `arn:aws:agent-registry:` and the registry is in `READY` status.                                                                                                                                                                         |
| Consumer cannot find a pending invitation                                                      | The accounts are in the same AWS Organization with RAM organization sharing enabled.                                                                                             | Acceptance is automatic for organization-internal shares. Verify the shared registry appears in `aws ram list-resources --resource-owner OTHER-ACCOUNTS --resource-type agent-registry:Registry`.                                                                    |
| Consumer can call `list-discoverable-registry-records` but `search` or `batch-get` returns 403 | A customer-managed RAM permission is attached that grants only `ListDiscoverableRegistryRecords` without `SearchDiscoverableRegistryRecords` or `GetDiscoverableRegistryRecord`. | Verify which permission is attached using `aws ram list-resource-share-permissions --resource-share-arn …​`. Switch to an AWS managed permission (all four include list, search, and get), or update the customer-managed permission to include the missing actions. |
| After stopping sharing, the consumer can still access the registry briefly                     | Resource-based policy propagation has a short delay.                                                                                                                             | Wait approximately 30 seconds and retry. Access revocation is eventually consistent.                                                                                                                                                                                 |
| `ram:CreateResourceShare` returns `AccessDeniedException`                                      | The owner’s IAM role is missing RAM permissions.                                                                                                                                 | Attach `ram:CreateResourceShare` and `agent-registry:PutResourcePolicy` to the owner’s IAM role.                                                                                                                                                                     |
