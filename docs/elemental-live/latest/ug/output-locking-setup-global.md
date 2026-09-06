

# Step 3: Set up the global controls
<a name="output-locking-setup-global"></a>

This section shows how to set up global controls to enable output locking and epoch locking in an Elemental Live event. You must set up the controls that apply to the entire event—the timecode and the communications mechanism.

**Note**  
This section refers to *pools* and *redundant pairs*. For an explanation of pools, see [Output locking pools](opl-pools.md). For an explanation of pairs, see [Output locking pairs](opl-redundant-pairs.md).

**Topics**
+ [Set up the timecode](#output-locking-event-global-tcode)
+ [Enable output locking](#output-locking-event-global-comms)

## Set up the timecode
<a name="output-locking-event-global-tcode"></a>

In the **Timecode Configuration** section that appears after the **Inputs** section of the event: Set the fields as specified in the following table. This setup configures the timecode for use in all outputs.


| Field name | Instruction | Notes | 
| --- | --- | --- | 
| Source | Choose any value, but choose the same value in all events in the pool. | This timecode is the timecode for the outputs. It is inserted in all the outputs in the pool of locked events.<br />The downstream system can use this timecode to determine that a frame from one event corresponds to the frame from another event. | 
| Sync Threshold | Deselect this field. |  | 
| Require Initial Timecode | Select the check box to ensure that the first source does in fact have a timecode. | If you select this check box, the event will fail to start if the first input has no embedded timecode. The event will also fail to start if you stop and restart the event, and the input that is active when you restart has no embedded timecode. | 

## Enable output locking
<a name="output-locking-event-global-comms"></a>

You must enable output locking. 

Make sure that you perform the same setup in all the events in the pool.

**To set up to use multicast for standard output locking**

To implement standard output locking, the events you are locking together must be able to communicate with each other over multicast or unicast. You can use multicast if you are locking together two events, or if you are locking together several events.

1. In the **Global Processors** section of the event set the **Output Locking** field to **On**.

1. Set the fields as shown in the following table.    
<a name="table-output-locking-event-setup-global-processors-fields-for-multicast"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-setup-global.html)

**To set up to use unicast for standard output locking**

To implement standard output locking, the events that you're locking together must be able to communicate with each other over multicast or unicast. Unicast is a point-to-point protocol, so you can use unicast only if you're locking together two events.
+ In the **Global Processors** section of the event set the **Output Locking** field to **On**.

  Set the fields as shown in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-setup-global.html)

**To set up for epoch locking**

1. In the **Global Processors** section, set the **Output Locking** field to **On**.

1. Select **Epoch Locking**. The values of other fields are ignored.