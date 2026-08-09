# Notifications (Amazon EventBridge)

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

## Supported events

AWS Agent Registry emits Amazon EventBridge events for registry-record approval-workflow transitions and for registry provisioning and lifecycle transitions. Events are delivered to the **default** EventBridge bus in the resource’s own account.

###### Example

AWS Agent Registry namespace

**Event source:**
`aws.agent-registry`

**Registry-record events.** Emitted when a registry record transitions between approval-workflow states. `Resources` is the full record ARN; `detail` contains `registryRecordId` and `registryId`.

| Detail type                                         | Trigger                                                                                       |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `Registry Record State changed to Draft`            | Record version enters `DRAFT`                                                                 |
| `Registry Record State changed to Pending Approval` | `SubmitRegistryRecordForApproval` called _(unchanged from the `bedrock-agentcore` namespace)_ |
| `Registry Record State changed to Approved`         | Record transitions to `APPROVED`                                                              |
| `Registry Record State changed to Rejected`         | Record transitions to `REJECTED`                                                              |
| `Registry Record State changed to Deprecated`       | Record transitions to `DEPRECATED`                                                            |

**Registry events.** Emitted on registry provisioning and lifecycle transitions. `Resources` is the full registry ARN; `detail` contains `registryId` and `registryName` (present when the registry has a name).

| Detail type              | Trigger                                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Registry Creating`      | Registry enters `CREATING`                                                                                                           |
| `Registry Ready`         | Registry becomes `READY`<br>_(replaces the `bedrock-agentcore` namespace value `Registry State transitions from Creating to Ready`)_ |
| `Registry Create Failed` | Registry enters `CREATE_FAILED`                                                                                                      |
| `Registry Updating`      | Registry enters `UPDATING`                                                                                                           |
| `Registry Update Failed` | Registry enters `UPDATE_FAILED`                                                                                                      |
| `Registry Deleting`      | Registry enters `DELETING`                                                                                                           |
| `Registry Delete Failed` | Registry enters `DELETE_FAILED`                                                                                                      |

Amazon Bedrock AgentCore namespace (to be deprecated)

**Event source:**
`aws.bedrock-agentcore`

| Event                                       | Detail type                                         | Trigger                                  |
| ------------------------------------------- | --------------------------------------------------- | ---------------------------------------- |
| Record submitted for approval               | `Registry Record State changed to Pending Approval` | `SubmitRegistryRecordForApproval` called |
| Registry moves from Creating to Ready state | `Registry State transitions from Creating to Ready` | After a registry completes provisioning  |

To receive additional event types across the full registry-record and registry lifecycle, migrate to the `agent-registry` namespace. For migration details, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

See [Notifications for pending approvals](registry-notifications-approvals.md "registry-notifications-approvals.md") for the full event schema and rule setup instructions.
