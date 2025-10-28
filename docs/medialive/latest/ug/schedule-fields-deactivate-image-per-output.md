# Fields for

deactivating a per-outputs image overlay

This table shows the fields that apply for an action to deactivate the image.
The deactivate action operates on one per-output layer that you specify and on
the outputs that you specify. It doesn't operate on a specific image.

To understand how this statement is significant, consider this example. You
might specify layer 4 and outputs A and C. Layer 4 in output A contains the
image overlay X, output B contains image overlay X, and output C contains image
X. MediaLive removes X from output A, and removes Y from output C. Image X in output
B will remain active.

| Field             | Description                                                                                                                                                                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**   | Static Image Output Deactivate.                                                                                                                                                                                                                                                                    |
| **Action name**   | A name for this deactivation action. For example, the name of the image. Or a name that ties back to the activation action plus the term "deactivate."                                                                                                                                             |
| **Start type**    | **Fixed** or **Immediate**.                                                                                                                                                                                                                                                                        |
| **Date and time** | If the **Start type** is **Fixed**, specify the date and time (in UTC format) that the channel must deactivate the image overlay. The time should be at least 60 seconds later than the time that you submit the action. Note that the time is the wall clock time, not the timecode in the input. |
| **Outputs**       | Select the output or outputs where you want to deactivate a specific layer.                                                                                                                                                                                                                        |
| **Layer**         | Identify the layer that you want to deactivate. Enter a value 0 to 7. Default is 0.                                                                                                                                                                                                                |
| **Fade out**      | Enter the time in milliseconds for the image to fade out. Default is 0 (no fade-out).                                                                                                                                                                                                              |
