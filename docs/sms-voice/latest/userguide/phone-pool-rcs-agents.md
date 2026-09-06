

# Managing AWS RCS Agents in pools
<a name="phone-pool-rcs-agents"></a>

You can add an AWS RCS Agent as an origination identity in a phone pool alongside your SMS phone numbers. When a pool contains both an AWS RCS Agent and SMS phone numbers, AWS End User Messaging attempts RCS delivery first and automatically falls back to SMS if RCS delivery is not possible. For details on how fallback works, see [RCS to SMS fallback using phone pools](rcs-sms-fallback.md).

**Note**  
When you add an AWS RCS Agent to a pool, use `ZZ` as the ISO country code. The `ZZ` code indicates that the RCS agent is not country-specific at the pool level. Country-specific routing is handled through the agent's country launch registrations. A pool can contain phone numbers from multiple countries alongside the RCS agent.  
The ISO country code is provided at pool creation time but is not persisted on the pool. If you call `DescribePools`, the ISO country code does not appear in the response.

## Creating a pool with an AWS RCS Agent
<a name="phone-pool-rcs-create"></a>

You can create a new pool that includes your AWS RCS Agent using the AWS End User Messaging console or the `CreatePool` API.

------
#### [ Console ]

**To create a pool with an AWS RCS Agent using the console**

1. Open the AWS End User Messaging console.

1. In the navigation pane, choose **Phone pools**.

1. Choose **Create pool**.

1. For **Origination identity**, select your AWS RCS Agent. The pool inherits its configuration from the origination identity you select.

1. Configure the pool settings as needed, then choose **Create pool**.

1. After the pool is created, add your SMS phone numbers to the pool to enable SMS fallback. All origination identities in the pool must have matching configuration. For details, see [Pool configuration requirements for RCS](#phone-pool-rcs-config).

------
#### [ AWS CLI ]

Use the `CreatePool` API to create a pool with your AWS RCS Agent as the initial origination identity. Specify the AWS RCS Agent ARN as the origination identity when creating the pool.

The following example creates a pool using the AWS CLI:

```
aws pinpoint-sms-voice-v2 create-pool \
    --origination-identity arn:aws:sms-voice:{{region}}:{{account-id}}:rcs-agent/{{rcs-agent-id}} \
    --iso-country-code ZZ \
    --message-type TRANSACTIONAL
```

After the pool is created, use the `AssociateOriginationIdentity` API to add SMS phone numbers to the pool for fallback.

------

## Adding AWS RCS Agents to existing pools
<a name="phone-pool-rcs-add"></a>

If you already have a pool with SMS phone numbers, you can add your AWS RCS Agent to the pool to enable RCS messaging with SMS fallback. You can also add additional SMS phone numbers to a pool that already contains an AWS RCS Agent.

**Important**  
Before adding an origination identity to an existing pool, verify that the pool's configuration matches the identity you are adding. All origination identities in a pool must have identical metadata. If there is a mismatch, the operation fails with a `ConflictException`. For details on which fields must match and how to resolve mismatches, see [Pool configuration requirements for RCS](#phone-pool-rcs-config).

------
#### [ Console ]

Before adding an AWS RCS Agent to a pool using the console, inspect the pool's details page to review its current configuration. Confirm that the pool's message type, ISO country code, and other settings are compatible with the AWS RCS Agent you want to add.

**To add an AWS RCS Agent to an existing pool using the console**

1. Open the AWS End User Messaging console.

1. In the navigation pane, choose **Phone pools**.

1. Choose the pool that you want to add the AWS RCS Agent to.

1. Review the pool's configuration on the details page. Confirm that the message type and other settings match the AWS RCS Agent you want to add.

1. In the **Origination identities** section, choose **Add origination identity**.

1. Select your AWS RCS Agent from the list and choose **Add**.

------
#### [ AWS CLI ]

Before adding an AWS RCS Agent to a pool using the CLI or API, use the `DescribePools` API to retrieve the pool's current configuration. Verify that the pool's settings match the AWS RCS Agent you want to add.

The following example retrieves pool details:

```
aws pinpoint-sms-voice-v2 describe-pools \
    --pool-ids {{pool-id}}
```

After confirming the configuration matches, use the `AssociateOriginationIdentity` API to add the AWS RCS Agent to the pool:

```
aws pinpoint-sms-voice-v2 associate-origination-identity \
    --pool-id {{pool-id}} \
    --origination-identity arn:aws:sms-voice:{{region}}:{{account-id}}:rcs-agent/{{rcs-agent-id}} \
    --iso-country-code ZZ
```

------

## Pool configuration requirements for RCS
<a name="phone-pool-rcs-config"></a>

All origination identities in a pool must have identical metadata. When you add an origination identity to a pool, AWS End User Messaging compares the identity's configuration with the pool's existing configuration. If there is a mismatch, the operation fails with a `ConflictException` that includes details about the specific fields that differ.

Pool configuration fields fall into two categories: immutable fields that are set when the pool is created and cannot be changed, and mutable fields that you can update after creation.


**Immutable versus mutable pool configuration fields**  

| Field | Mutability | Notes | 
| --- | --- | --- | 
| Message type | Immutable | Set at pool creation. All identities must match. | 
| ISO country code | Immutable | Set at pool creation. For AWS RCS Agents, the value is ZZ. Pools can contain phone numbers from multiple countries. | 
| Deletion protection | Mutable | Can be toggled after creation. Must be consistent across identities. | 
| Opt-out list | Mutable | Can be changed after creation. Must be consistent across identities. | 

The following configuration fields must match across all origination identities in a pool:
+ **Message type** — All identities must be configured for the same message type (for example, TRANSACTIONAL or PROMOTIONAL).
+ **ISO country code** — Set at pool creation. For AWS RCS Agents, use `ZZ` as the ISO country code. Pools can contain phone numbers from multiple countries.
+ **Deletion protection** — The deletion protection setting must be consistent across identities.
+ **Opt-out list** — All identities must be associated with the same opt-out list, or none of them should have an opt-out list.

### Understanding ConflictException errors
<a name="phone-pool-rcs-config-conflict"></a>

When you attempt to add an origination identity to a pool and the configuration does not match, the `AssociateOriginationIdentity` or `CreatePool` API returns a `ConflictException`. The exception message includes details about which fields differ between the identity and the pool.

For example, if you try to add a phone number configured for PROMOTIONAL messages to a pool configured for TRANSACTIONAL messages, the error message indicates that the message type does not match.

To resolve a `ConflictException`:

1. Review the error message to identify which fields differ.

1. Update the origination identity or the pool configuration so that the fields match.

1. Retry the `AssociateOriginationIdentity` or `CreatePool` operation.

**Note**  
If you cannot resolve the configuration mismatch, consider creating a separate pool for the origination identity. Each pool can have its own configuration, and you can use different pools for different use cases.

## Removing AWS RCS Agents from pools
<a name="phone-pool-rcs-remove"></a>

You can remove an AWS RCS Agent from a pool using the AWS End User Messaging console or the `DisassociateOriginationIdentity` API. Removing an AWS RCS Agent from a pool disables RCS delivery for messages sent through that pool. Messages sent to the pool after the agent is removed are delivered via SMS only (using the remaining phone numbers in the pool).

------
#### [ Console ]

**To remove an AWS RCS Agent from a pool using the console**

1. Open the AWS End User Messaging console.

1. In the navigation pane, choose **Phone pools**.

1. Choose the pool that contains the AWS RCS Agent you want to remove.

1. In the **Origination identities** section, select the AWS RCS Agent.

1. Choose **Remove**, then confirm the removal.

------
#### [ AWS CLI ]

Use the `DisassociateOriginationIdentity` API to remove an AWS RCS Agent from a pool:

```
aws pinpoint-sms-voice-v2 disassociate-origination-identity \
    --pool-id {{pool-id}} \
    --origination-identity arn:aws:sms-voice:{{region}}:{{account-id}}:rcs-agent/{{rcs-agent-id}} \
    --iso-country-code ZZ
```

After removing the AWS RCS Agent, messages sent through the pool are delivered via SMS only. To re-enable RCS delivery, add the AWS RCS Agent back to the pool using the `AssociateOriginationIdentity` API.

------