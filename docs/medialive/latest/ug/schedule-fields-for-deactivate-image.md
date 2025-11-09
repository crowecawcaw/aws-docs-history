# Fields for deactivating a

global image overlay

This table shows the fields that apply for an action to deactivate an image
overlay.

| Field             | Description                                                                                                                                                                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**   | Static Image Deactivate.                                                                                                                                                                                                                                                                                                    |
| **Action name**   | A name for this deactivation action. For example, the name of<br>the image. Or a name that ties back to the activation action<br>plus the term "deactivate."                                                                                                                                                                |
| **Start type**    | **Fixed\*<br>• or<br>**Immediate\*\*.                                                                                                                                                                                                                                                                                       |
| **Date and time** | If the **Start type\*<br>• is<br>**Fixed\*\*, specify the date and time<br>(in UTC format) that the channel must deactivate the image<br>overlay. The time should be at least 60 seconds later than<br>the time that you submit the action.<br>Note that the time is the wall clock time, not the<br>timecode in the input. |
| **Layer**         | Enter the layer that contains the image overlay that you want<br>to deactivate. A value 0 to 7. Default is 0.                                                                                                                                                                                                               |
| **Fade out**      | Enter the time in milliseconds for the image to fade out.<br>Default is 0 (no fade-out).                                                                                                                                                                                                                                    |
