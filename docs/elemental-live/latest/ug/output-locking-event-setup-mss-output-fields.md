# Setting

up an
MS
Smooth output group

This section shows how to set up an MS Smooth output group to
implement Elemental Live output locking.

1. Go to the **MS Smooth Settings** section of the
   output group. Set the fields that are listed in the following table
   as specified in the table.

| Field name            | Instruction                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Custom Group Name** | Enter the same name in all events in the pool.                                                                                                                                                                                                                                                                                                                                |
| **Fragment Length**   | Enter the same number in all events in the<br>pool.                                                                                                                                                                                                                                                                                                                           |
| **Use Event ID**      | If the pooled events are configured to publish to a<br>single publishing point, you can deselect this field. If you<br>don't deselect this field, then when one encoder stops, the<br>publishing point may stop accepting requests from the other<br>events in the pool.If the pooled events publish to<br>different publishing points, you can leave this field<br>selected. |
| **Send EOS**          | If the pooled events are configured to publish to a<br>single publishing point, you can deselect this field. If you<br>don't deselect this field, then when one encoder stops, the<br>publishing point may stop accepting requests from the other<br>events in the pool.If the pooled events publish to<br>different publishing points, you can leave this field<br>selected. |
| **Send Delay**        | Complete as desired. For details, see the tooltip on<br>the Elemental Live web interface.                                                                                                                                                                                                                                                                                     |

2. Set other fields in the **MS Smooth Settings**
   section to suit your workflow.
3. Set the fields in the outputs to suit your workflow.
