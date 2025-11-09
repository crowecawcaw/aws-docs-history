# Step 2: Set up inputs in the

events

After you have identified the sources and ensured that they [support output
locking](output-locking-requirements.md#output-locking-output-requirements "output-locking-requirements.md#output-locking-output-requirements"), you can set them up in the event as inputs.

###### Note

This section refers to _pools_. For
an explanation of pools, see [Output locking pools](opl-pools.md "opl-pools.md").

###### To set up the inputs

1. Create all of the inputs that you have identified. Create the same inputs in each
   event, and enter them in the same order in each event.
2. Complete all fields that apply to the input type.

In the **Input – Video Selector** section
of the event: Set the following fields as specified in the following
table.

| Field name          | Instruction                                                                                                                                    | Notes                                                                                                                                                                                                         |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input Name**      | In one event, enter a different name for each input. Use that name for the<br>same input in the entire pool of locked events.                  | This field is optional. However, output locking works best if inputs have<br>names.                                                                                                                           |
| **Timecode Source** | For SDI inputs, choose **Embedded\*<br>• or<br>**LTC**, depending on the timecode in the<br>input.<br>For other inputs, choose **Embedded\*\*. | If an input doesn't have a timecode, [you can't use<br>it in the event](output-locking-requirements.md#output-locking-input-requirements "output-locking-requirements.md#output-locking-input-requirements"). |
