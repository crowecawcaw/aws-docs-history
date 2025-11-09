# Step 3: Set up the global

controls

This section shows how to set up global controls to enable output locking and epoch
locking in an Elemental Live event. You must set up the controls that apply to the entire
event—the timecode and the communications mechanism.

###### Note

This section refers to _pools_ and
_redundant pairs_. For an explanation
of pools, see [Output locking pools](opl-pools.md "opl-pools.md"). For an explanation of pairs,
see [Output locking pairs](opl-redundant-pairs.md "opl-redundant-pairs.md").

###### Topics

- [Set up the
  timecode](#output-locking-event-global-tcode "#output-locking-event-global-tcode")
- [Enable output
  locking](#output-locking-event-global-comms "#output-locking-event-global-comms")

## Set up the

timecode

In the **Timecode Configuration** section that
appears after the **Inputs** section of the event: Set
the fields as specified in the following table. This setup configures
the timecode for use in all outputs.

| Field name                   | Instruction                                                                           | Notes                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source**                   | Choose any value, but choose the same value in all events<br>in the pool.             | This timecode is the timecode for the outputs. It is<br>inserted in all the outputs in the pool of locked<br>events.<br>The downstream system can use this timecode to determine<br>that a frame from one event corresponds to the frame from<br>another event.  |
| **Sync Threshold**           | Deselect this field.                                                                  |                                                                                                                                                                                                                                                                  |
| **Require Initial Timecode** | Select the check box to ensure that the first source does<br>in fact have a timecode. | If you select this check box, the event will fail to start<br>if the first input has no embedded timecode. The event<br>will also fail to start if you stop and restart the event, and<br>the input that is active when you restart has no embedded<br>timecode. |

## Enable output

locking

You must enable output locking.

Make sure that you perform the same setup in all the events in the
pool.

###### To set up to use multicast for standard output locking

To implement standard output locking, the events you are locking
together must be able to communicate with each other over multicast or
unicast. You can use multicast if you are locking together two events,
or if you are locking together several events.

1. In the **Global Processors** section of the
   event set the **Output Locking** field to
   **On**.
2. Set the fields as shown in the following table.

| Field name                                                               | Instruction                                                                                                                                                                                                                                                                                       | Notes                                                        |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Epoch locking**                                                        | Deselect this field.                                                                                                                                                                                                                                                                              |                                                              |
| **Multicast**                                                            | Select this field.                                                                                                                                                                                                                                                                                |                                                              |
| **Address**<br>**Port\*<br>• (optional)<br>**Interface\*<br>• (optional) | These fields appear only if you have selected<br>**Multicast**.Enter the multicast address of any<br>server. Enter the identical address, port, and interface across all events that<br>you want to lock together. For more information, see the tooltips on the<br>Elemental Live web interface. | The events communicate with each other through this address. |

###### To set up to use unicast for standard output locking

To implement standard output locking, the events that you're locking together must be
able to communicate with each other over multicast or unicast. Unicast is a point-to-point
protocol, so you can use unicast only if you're locking together two events.

- In the **Global Processors** section of the event
  set the **Output Locking** field to
  **On**.

Set the fields as shown in the following table.

| Field name                                                                | Instruction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Notes                                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **Epoch locking**                                                         | Deselect this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                         |
| **Multicast**                                                             | Deselect this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                         |
| **Address**<br>**Port\*<br>• (optional)<br>**Interface\*<br>• (optional)  | These fields appear only if you have deselected<br>**Multicast**.Enter the address where<br>the other event is listening. See the tooltips on the<br>Elemental Live web interface for more information.<br>If you have more than one locked event on the<br>same appliance, make sure that you assign a unique port to<br>each event. Two different events can't listen on the same<br>port. For an example of two locked events on an appliance,<br>see **Appliance 3**in the<br>diagram in [Example of a workflow](opl-example.md "opl-example.md"). | This event in the event pair uses this address to send a<br>message to the other event. |
| **Receive Port\*<br>• (required)<br>**Receive Interface\*<br>• (optional) | These fields appear only if you have deselected<br>**Multicast**.Enter the address where<br>this event is listening. See the tooltips on the<br>Elemental Live web interface for more information. If<br>you have more than one locked event on the same appliance,<br>make sure that you assign a unique port to each event. Two<br>different events can't listen on the same port.                                                                                                                                                                   | The other event uses this address to send messages to<br>this event.                    |

###### To set up for epoch locking

1. In the **Global Processors** section, set the
   **Output Locking** field to
   **On**.
2. Select **Epoch Locking**. The values of other
   fields are ignored.
