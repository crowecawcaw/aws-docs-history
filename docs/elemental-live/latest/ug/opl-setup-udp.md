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

| Field name               | Instruction                                                                                                                                                                                                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Segmentation Markers** | Output lock requires that a UDP/TS output have segmentation markers. Always choose **EBP Cablelabs**. Other options aren't valid for output locking. This option adds Encoder Boundary Point information to the adaptation field in conformance with OpenCable specification OC-SP-EBP-I01-130118. |
| **Segmentation Time**    | Required. This field ensures that all of the outputs in the pool synchronize continually, not just when the events first start.                                                                                                                                                                    |
| **Fragment Time**        | Required.                                                                                                                                                                                                                                                                                          | 3. Set other fields in the outputs to suit your workflow. |
