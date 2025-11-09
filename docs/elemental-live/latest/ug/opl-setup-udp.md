# Setting up a UDP/TS output group

This section shows how to set up a UDP/TS output group to implement Elemental Live
output locking.

1. Go to the **UDP/TS Output Group** section of
   the event. Set the fields as follows.
   - **Custom Group Name**: Enter the same name
     across all events in the pool.
   - Set other fields to suit your workflow.

2. Go to each output. In the **Transport Stream
   Settings** section, set the fields as specified in the
   following table.

| Field name               | Instruction                                                                                                                                                                                                                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Segmentation Markers** | Output lock requires that a UDP/TS output have<br>segmentation markers.<br>Always choose **EBP Cablelabs**.<br>Other options aren't valid for output locking. This option<br>adds Encoder Boundary Point information to the adaptation<br>field in conformance with OpenCable specification<br>OC-SP-EBP-I01-130118. |
| **Segmentation Time**    | Required.<br>This field ensures that all of the outputs in the pool<br>synchronize continually, not just when the events first<br>start.                                                                                                                                                                             |
| **Fragment Time**        | Required.                                                                                                                                                                                                                                                                                                            |

3. Set other fields in the outputs to suit your workflow.
