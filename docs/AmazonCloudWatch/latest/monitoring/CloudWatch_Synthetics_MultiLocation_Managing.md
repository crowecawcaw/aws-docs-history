# Managing multilocation canaries

## Creating a multilocation canary

To create a multilocation canary, follow the steps in [Creating a canary](CloudWatch_Synthetics_Canaries_Create.md "CloudWatch_Synthetics_Canaries_Create.md") and select additional
Regions under **Locations**. The current Region is automatically
selected as the primary location.

When you create a multilocation canary, the following requirements apply:

- You can add up to 50 replica locations.
- The canary script .zip file must not exceed 50 MB.
- The canary name must not already exist in any of the selected replica
  Regions.
- Replica locations must be supported CloudWatch Synthetics commercial Regions. The primary
  Region cannot be selected as a replica location.
- Multilocation canaries cannot be associated with a group. If your canary belongs
  to a group, disassociate it from all groups before adding replica locations.
- If your canary requires VPC connectivity, you must configure VPC settings for
  each replica Region separately. VPC settings are not inherited from the
  primary.
- Tags are not replicated to replica Regions. To add tags to a replica, navigate
  to the replica Region and add tags directly.

After creation, replicas are provisioned asynchronously. You can monitor the
replication progress on the canary detail page in the
**Configuration** tab. When a replica reaches
`InSync` state, it is fully provisioned and running. You can also
view the replica canary directly in the replica Region. For more information, see
[Replication status](#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage "#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage").

If a replica fails to provision, the primary canary is still created
successfully. The failed replica displays an `Inconsistent` replication
status. You can retry by updating the canary.

## Adding or removing replica locations

To add or remove replica locations, edit the canary from the primary Region and
update the selections under **Locations**. You cannot edit a
multilocation canary from a replica Region. For more information about editing a canary,
see [Edit or delete a canary](synthetics_canaries_deletion.md "synthetics_canaries_deletion.md").

When you add or remove replica locations, the following requirements apply:

- You cannot modify a multilocation canary while replication is in progress. Wait
  for all replicas to reach `InSync` or `Inconsistent` state
  before making changes. For more information, see [Replication status](#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage "#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage").
- When you add replica locations, you must include the canary code in your
  request.
- When you update a canary that has inconsistent replicas, you must include the
  canary code, unless you are removing all inconsistent replicas in the same
  request.
- You cannot add and remove the same location in a single request.
- You cannot remove a replica location that does not exist.

## Starting and stopping a multilocation canary

When you start or stop a multilocation canary, the action applies to the primary
canary and all replica locations.

When you start or stop a multilocation canary, the following requirements
apply:

- You must start or stop the canary from the primary Region. Start and stop
  operations are not permitted from a replica Region.
- You cannot start or stop a multilocation canary while replication is in
  progress. Wait for all replicas to reach `InSync` or
  `Inconsistent` state before starting or stopping. For more information,
  see [Replication status](#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage "#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage").
- The canary must be in the `READY` or `STOPPED` state to
  start, or in the `RUNNING` state to stop.

## Deleting a multilocation canary

To delete a multilocation canary, you must first remove all replica locations. For
more information, see [Edit or delete a canary](synthetics_canaries_deletion.md "synthetics_canaries_deletion.md"). The following requirements
apply:

- You must delete the canary from the primary Region. Delete operations are not
  permitted from a replica Region.
- Wait for all replicas to be fully removed before you attempt to delete. You can
  monitor removal progress in the **Configuration** tab. For more
  information, see [Replication status](#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage "#CloudWatch_Synthetics_MultiLocation_ReplicationStatus_Manage").
- The canary must be in the `STOPPED`, `READY`, or
  `ERROR` state. If the canary is running, stop it first.

## Replication status

Replication status indicates the synchronization state of a replica with the primary
canary. You can view the replication status on the canary detail page in the
**Configuration** tab.

Replicas can have the following replication status values:

- **InProgress**—The replica is being created
  or updated. Changes from the primary are being propagated to the replica.
- **InSync**—The replica is fully
  synchronized with the primary canary configuration.
- **Inconsistent**—The replica is out of
  sync with the primary canary. This can occur if a propagation failed. You can retry by
  updating the canary again.

The overall _ReplicationState_ on the primary canary shows the
aggregate state across all replicas. If any replica is `InProgress`, the
overall state is `InProgress`. If any replica is `Inconsistent`,
the overall state is `Inconsistent`.
