# Step 5:

Set up the video encodes

This section shows how to set up video encode parameters in an event
that implements Elemental Live output locking.

###### Note

This section refers to _pools_. For
an explanation of pools, see [Output locking pools](opl-pools.md "opl-pools.md").

After you have created the output groups and outputs, follow these guidelines to create the
video encodes.

Set up the output encodes (video streams) in the usual way:

1. In each output group, create as many outputs as you [planned for that output
   group](opl-step-get-ready-outputs.md "opl-step-get-ready-outputs.md"). When you add an output, Elemental Live creates a new
   stream in the **Streams** section.
2. Set the following fields in the **Video** tab
   as specified.

| Field name    | Instruction                                                             | Notes                                                                                                                                                                                                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Codec**     | H.264 or H.265                                                          | You can use a combination of H.264 and H.265 in the pool of outputs.                                                                                                                                                                                                                                                                  |
| **Framerate** | Enter a value. We strongly recommend not to choose<br>**Follow source** | For information about the rules for frame rate, see [Output encode<br>requirements](output-locking-requirements.md#output-locking-output-requirements "output-locking-requirements.md#output-locking-output-requirements"). If you ignore these rules, the<br>encodes in the pool of outputs won't be frame accurate with each other. |

3. You can set other fields in the **Video** section, the fields in
   the **Audio** section, and the fields in the
   **Captions** tab to suit your workflow.
