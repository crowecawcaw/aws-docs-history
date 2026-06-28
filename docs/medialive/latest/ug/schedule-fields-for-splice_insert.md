# Fields for a splice\_insert message

This table shows the fields that apply for an action to insert a splice\_insert
SCTE 35 message.

| Field                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**           | SCTE 35 Splice Insert.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Action name**           | A name for this splice\_insert action. For example,<br>splice\_insert actions could be numbered sequentially, restarting<br>every day or every month.                                                                                                                                                                                                                                                                                          |
| **Start type**            | *_Fixed_<br>• or *_Follow_<br>• or<br>**Immediate**.                                                                                                                                                                                                                                                                                                                                                                                           |
| **Date and time**         | If the *_Start type_<br>• is<br>**Fixed**, specify the UTC start time<br>for the splice\_insert action. The time should be at least 15<br>seconds in the future.<br>Note that the time is the wall clock time, not the<br>timecode in the input.                                                                                                                                                                                               |
| **Reference action name** | If the *_Start type_<br>• is<br>**Follow**, choose the input to follow.<br>The dropdown list shows all existing input switches that are<br>file inputs. Remember that a SCTE 35 action can follow input<br>A only if input A is a file input and the source end<br>behavior for input A is _continue_.<br>For information about these switching rules, see [Fixed, immediate, and follow switches](ips-switch-types.md "ips-switch-types.md"). |
| **Follow point**          | If the *_Start type_<br>• is<br>**Follow**, complete this field. The follow<br>point is always **End**, to indicate that the<br>switch will occur when the input in *_Reference action<br>name_<br>• has finished.                                                                                                                                                                                                                             |
| **Splice event id**       | The ID for the splice event. Enter an ID for the splice event<br>that is unique among all scheduled and active splice\_insert<br>messages in this channel. A message is active if the schedule<br>action is in process in the channel and has not completed.                                                                                                                                                                                   |
| **Duration**              | The duration for the splice event. Complete in one of these ways:<br>• Enter the duration, in 90-kHz ticks. For example,<br>1350000, which is equal to 15 seconds.<br>• Leave empty to create a message with no<br>duration.                                                                                                                                                                                                                   |

The splice\_insert inserted in the transport stream will have the
following:

```

      segmentation_event_cancel_indicator = 0
      out_of_network = 1
      duration_flag = 1
      duration = the specified time

```

Or

```

      segmentation_event_cancel_indicator = 0
      out_of_network = 1
      duration_flag = 0

```
