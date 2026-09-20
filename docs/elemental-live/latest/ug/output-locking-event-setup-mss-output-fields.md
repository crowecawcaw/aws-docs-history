

# Setting up an MS Smooth output group
<a name="output-locking-event-setup-mss-output-fields"></a>

This section shows how to set up an MS Smooth output group to implement Elemental Live output locking. 

1. Go to the **MS Smooth Settings** section of the output group. Set the fields that are listed in the following table as specified in the table. 

<a name="table-output-locking-event-setup-mss-output-fields"></a>
<table>
<thead>
  <tr><th>Field name</th><th>Instruction</th></tr>
</thead>
<tbody>
  <tr><td><b>Custom Group Name</b></td><td>Enter the same name in all events in the pool.</td></tr>
  <tr><td><b>Fragment Length</b></td><td>Enter the same number in all events in the pool.</td></tr>
  <tr><td><b>Use Event ID</b></td><td>If the pooled events are configured to publish to a single publishing point, you can deselect this field. If you don't deselect this field, then when one encoder stops, the publishing point may stop accepting requests from the other events in the pool.If the pooled events publish to different publishing points, you can leave this field selected.</td></tr>
  <tr><td><b>Send EOS</b></td><td>If the pooled events are configured to publish to a single publishing point, you can deselect this field. If you don't deselect this field, then when one encoder stops, the publishing point may stop accepting requests from the other events in the pool.If the pooled events publish to different publishing points, you can leave this field selected.</td></tr>
  <tr><td><b>Send Delay</b></td><td>Complete as desired. For details, see the tooltip on the Elemental Live web interface.</td></tr>
</tbody>
</table>


1. Set other fields in the **MS Smooth Settings** section to suit your workflow. 

1. Set the fields in the outputs to suit your workflow. 