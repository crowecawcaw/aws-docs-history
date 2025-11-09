# Fields for a PNG asset

| Field on web interface  | Tag in the XML                           | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------- | ---------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Insertion Mode          | <insertion_mode>                         | String  | Choose png.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Input                   | <uri>                                    | String  | The path and file name of the PNG files.<br>Provide the path and file name of the first PNG<br>file in the series. All files in the series must<br>have the same number of digits in the numerical<br>part of the file name.<br>For example, if the files are stored on<br>/mnt/storage/motion_logos/ and the files are named<br>logo_hi_001 to logo_hi_357, enter<br>`/mnt/storage/motion_logos/logo_hi_001`.<br>When using Amazon S3, you can optionally append the<br>path as follows:<br>• Use `sse`=`true` to<br>turn on Amazon S3 Server Side Encryption<br>(SSE).<br>• Use `rrs=true` to enable<br>Reduced Redundancy Storage (RRS).<br>Default values for RRS and SSE are<br>`false`.                                                                                                           |
| Username Password       | <username><password>                     |         | If access to your local or mounted directory<br>requires a user name and password, click the lock<br>icon next to the **Input\*<br>• field<br>to show the **Username*<br>• and<br>\*\*Password*<br>• fields.<br>For Amazon S3, enter the access key ID in the<br>username field. Enter the secret access key in the<br>password field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Left                    | <image_x>                                | Integer | Placement of the left edge of the motion<br>overlay relative to the left edge of the video<br>frame, in pixels. 0 is the left edge of the<br>frame.<br>Take note of the width of the motion overlay<br>and make sure that the position of the left edge<br>of the motion overlay does not cause the right<br>edge to be cropped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Top                     | <image_y>                                | Integer | Placement of the top edge of the motion overlay<br>relative to the top edge of the video frame, in<br>pixels. 0 is the top edge of the frame. Default<br>0.<br>Take note of the height of the motion overlay<br>and make sure that the position of the top edge of<br>the motion overlay does not cause the bottom edge<br>to be cropped.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ActionTime              | <action_time>                            | String  | The start time for the motion overlay. Specify<br>the start time in one of the formats discussed in<br>detail below this table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Numerator Denominator   | framerate_numeratorframerate_denominator | Integer | On the web interface, enter the frame rate as a<br>numerator over a denominator. For example, 29.97 fps<br>is a numerator of 30000 and a denominator of 1001.<br>Enter numbers that give a frame rate ratio between 1<br>and 120. When using the REST API, enter the<br>numerator and denominator<br>separately.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Loop Input              | <loop_input>                             | Boolean | • Select to loop the motion overlay<br>indefinitely.<br>The motion overlay will run until the event<br>ends. To stop the motion overlay earlier, see<br>[Step C: Manage the motion overlay on a running event](png-step-manage-the-overlay-on-a-running-event.md "png-step-manage-the-overlay-on-a-running-event.md") .<br>• Clear the check box to run the motion overlay<br>only once.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Full Frame              | <full_frame>                             | Boolean | Expand the motion overlay to fit the video<br>frame. In this case, make sure<br>**Left\*<br>• and<br>**Top*<br>• are set to 0.<br>If this field is selected and the motion<br>overlay has a different aspect ratio to the<br>underlying video, the motion overlay will be<br>scaled until one of the following applies:<br>• The motion overlay fits in the length.<br>The motion overlay will then be positioned<br>with equal space on the left and<br>right.<br>• The motion overlay fits in the width. The<br>motion overlay will then be positioned with<br>equal space above and below.<br>Note that the \*\*Stretch to<br>output*<br>• field in the<br>\*_Stream_<br>• section does not<br>affect the motion overlay; even if the video is<br>stretched, the motion overlay is not<br>stretched. |
| Active                  | <active>                                 | Boolean | Always select this box when initially setting<br>up the motion overlay.<br>After the initial setup, the value of this tag<br>can be changed via the REST API to manage the<br>content and behavior of the motion overlay.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Enable REST Control** | <enable_rest>                            | Boolean | Select this field only if you plan to manage<br>motion overlays via the REST API, after this initial<br>setup via the web interface. Typically, you will want<br>this tag to be true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

**Action time formats**

**Option 1:** Timecode format
(HH:MM:SS:FF).

The value to enter for HH:MM:SS:FF depends on the method used
to calculate the _output
timecode_. This method is specified in the
**Timecode Configuration > Source** field.
Identify the source method set for your event, then set the
action time to match the timecode of the frame where you want the
action to occur.

- If **Source** is
  **Embedded**: The output timecode is
  extracted from the timecode that is carried with the input
  media. That timecode becomes the output timecode for the
  first transcoded frame. Then the output timecode counts up
  with each successive frame in the entire output. For
  example, 10:24:25:20, 10:24:25:21, and so on.
- If **Source** is **Start at
  0**: The output timecode for the first frame is
  00:00:00:00 and then the output timecode counts up with
  each successive frame in the entire output. For example,
  00:00:00;01: 00;00:00:02, and so on.
- If **Source** is **System Clock** or **Local System Clock**: The
  output timecode for the first frame is the system time at
  which the frame is decoded. Then the output timecode counts
  up with each successive frame in the entire output. For
  example, if the first frame is decoded at 09:45:51, then
  that timecode is 09:45:51:01. The timecode for the next
  frame is 09:45:51:02, and so on.
- If **Source** is **Specified
  Start**: The output timecode for the first
  frame is the time you specified when you selected this
  option as the timecode source. Then the output timecode
  counts up with each successive frame in the entire output.
  For example, if you set the time to 15:30;00, then the
  timecode for the first frame is 15;30:00:01, and so on.
- If **Source** is **External
  Reference Connector**: The timecode is
  extracted from external LTC source. That timecode becomes
  the output timecode for the first transcoded frame. Then
  the output timecode counts up with each successive frame in
  the entire output. For example, the timecode for the first
  frame is 20:03:19:01, then 20:03:19:01, and so on.
  **Option 2:** ISO 8601 UTC time
  with no dashes or colons. For example, 20160102T030405.678Z. In
  this case, the start time for every motion overlay will be the
  UTC time.

**Option 3:** You can only use
this option while adding or modifying a motion overlay in a
running event. Set the `action_time` tag to an empty
string to set the start time to “now”. With this option, the
start time is never exact. You cannot use this option when
creating an event or modifying a non-running event.
