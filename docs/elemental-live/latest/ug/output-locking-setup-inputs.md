

# Step 2: Set up inputs in the events
<a name="output-locking-setup-inputs"></a>

After you have identified the sources and ensured that they [support output locking](output-locking-requirements.md#output-locking-output-requirements), you can set them up in the event as inputs.

**Note**  
This section refers to *pools*. For an explanation of pools, see [Output locking pools](opl-pools.md).

**To set up the inputs**

1. Create all of the inputs that you have identified. Create the same inputs in each event, and enter them in the same order in each event.

1. Complete all fields that apply to the input type.

   In the **Input – Video Selector** section of the event: Set the following fields as specified in the following table.

<a name="table-output-locking-event-setup-input-fields"></a>
<table>
<thead>
  <tr><th>Field name</th><th>Instruction</th><th>Notes</th></tr>
</thead>
<tbody>
  <tr><td><b>Input Name</b></td><td>In one event, enter a different name for each input. Use that name for the same input in the entire pool of locked events. </td><td>This field is optional. However, output locking works best if inputs have names.</td></tr>
  <tr><td><b>Timecode Source</b></td><td>For SDI inputs, choose <b>Embedded</b> or <b>LTC</b>, depending on the timecode in the input. <br />For other inputs, choose <b>Embedded</b>. </td><td>If an input doesn't have a timecode, <a href="output-locking-requirements.md#output-locking-input-requirements">you can't use it in the event</a>.</td></tr>
</tbody>
</table>
