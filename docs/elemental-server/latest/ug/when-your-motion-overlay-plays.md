This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Setting Up When Your

Motion Graphic Plays

When you place a motion graphic overlay, you set up when it starts and how long it
runs by specifying the **Action Time** and **Loop
Input**. The following image shows how you would specify these settings
if you wanted your overlay to start two minutes into the video and to continuously
loop over the rest of the video. If you keep **Action Time** and
**Loop Input** in their default state, the overlay will begin
at the first frame of each output and remain on the video for the duration of the
motion graphic played once.

###### Note

In this example, the motion graphic is three minutes long, but the overlay is
set to continue to repeat the motion graphic until the end of the output.

![The overlay is represented in this image as a rectangle above a number line. The number line is marked with timecode sat one minute apart. The left edge of the rectangle is aligned with the second mark, at 00:00:02:00. The right edge of the rectangle is aligned with the fourth mark, at 00:00:04:00.](images/motion-overlay-start-duration.png)

###### Action Time

Provide the timecode for the first frame that you want to have the overlay
appear on. If you set up your overlay to fade in, the fade-in begins at the
start time.

###### Note

Make sure that you take your timecode source settings into account when you
provide your start time. For motion graphic overlays, the job-wide
**Timecode Config > Source** setting affects your overlay
start time. The input **Input > Timecode Source** setting
affects doesn't affect your overlay start time.

Unless you have a reason to set it otherwise, set both of these settings to
**Start at 0** and specify your timecode
counting from 00:00:00:00 at the first frame, as illustrated in the
example.

###### **Loop Input**

You can set your overlay to last the duration of the motion graphic played
through once or you can set it to loop motion graphic continuously from the
start time to the end of the output. The duration of a `.mov`
motion graphic is built into the `.mov` file, which has a set
number of frames and a defined frame rate. If your motion graphic is a set of
.png images, you determine the duration of the overlay by how many images you
provide and the framerate you specify. The duration in seconds is the number of
frames times the framerate in frames per second.
