

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Motion Image Inserter (Graphic Overlay) in AWS Elemental Server
<a name="motion-graphic-overlay"></a>

The following procedure walks you through how to set up motion graphic overlays. Motion graphic overlays are global, so they appear in all outputs. 

**To set up a motion graphic overlay**

1. Prepare your overlay asset. For more information, see [Requirements for Motion Overlay Files](requirements-for-the-motion-overlay-file.md). 
**Note**  
Motion graphic overlays are in the global processors. They appear on every output of the job and they scale with the video. Therefore, make your overlay size proportional to the size of your input video.

1. In the medium gray **Global Processors** section of the job, choose the **Motion Image Inserter** slider. The **Global Processors** section is just below the dark gray **Input** section.

1. Specify values for the motion image inserter settings. See the following table for information about each field. For information about **Action Time** and **Loop Input**, see [Setting Up When Your Motion Graphic Plays](when-your-motion-overlay-plays.md).



<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Insertion Mode</b></td><td>Choose SWF, MOV, or PNG.</td></tr>
  <tr><td><b>Input</b></td><td>The location and file name of the motion graphic.<br />For more information, see <a href="specifying-the-motion-overlay-location.md">Specifying the Motion Overlay File Location</a>.</td></tr>
  <tr><td><b>Username</b>, <b>Password</b></td><td>If access to your local or mounted directory requires a user name and password, choose the lock icon next to <b>Browse</b> to show the <b>Username</b> and <b>Password</b> fields.<br />If you're using Amazon S3, enter the Access Key ID for <b>Username</b>. Enter the Secret Access Key for <b>Password</b>.</td></tr>
  <tr><td><b>Left</b></td><td>Placement of the left edge of the motion overlay relative to the left edge of the video frame, in pixels. 0 is the left edge of the frame.</td></tr>
  <tr><td><b>Top</b></td><td>Placement of the top edge of the motion overlay relative to the top edge of the video frame, in pixels. 0 is the top edge of the frame.</td></tr>
  <tr><td><b>ActionTime</b></td><td>The start time for the overlay. Specify the start time in ISO 8601 UTC time format with no dashes or colons. For example, 20160102T030405.678Z. <br />For more information, see <a href="when-your-motion-overlay-plays.md">Setting Up When Your Motion Graphic Plays</a>.</td></tr>
  <tr><td><b>Loop Input</b></td><td>Check to loop the motion overlay indefinitely. The motion overlay runs until the event ends. <br />Deselect if you want to run the motion overlay only once.<br />For more information, see <a href="when-your-motion-overlay-plays.md">Setting Up When Your Motion Graphic Plays</a>.</td></tr>
  <tr><td><b>Full Frame</b></td><td>Expand the overlay to fit the video frame. In this case, make sure <b>Left</b> and <b>Top</b> are set to 0.<br />If you enable <b>Full Frame</b> and the motion overlay has a different aspect ratio than the underlying video, AWS Elemental Server scales the overlay until either:<br />• The motion overlay fits in the length. The overlay is then positioned with equal space on the left and right.<br />• The motion overlay fits in the width. The overlay is then positioned with equal space above and below. The <b>Stretch to output</b> field in the <b>Stream</b> section does not affect the motion overlay. When the video is stretched, the overlay is not stretched. </td></tr>
  <tr><td><b>Numerator</b>, <b>Denominator</b> (.png only)</td><td>If you're using a series of <code>.png</code> files for your overlay, specify the frame rate as a fraction. For example, to set the frame rate to 23.976 frames per second, set <b>Numerator</b> to 24000 and set <b>Denominator</b> to 1001.</td></tr>
  <tr><td><b>SWF Arguments</b> (<code>.swf </code>only)</td><td>If your overlay is a <code>.swf </code>file and if you included ActionScript code in the <code>.swf</code> asset that includes arguments, enter values for the arguments in simple JSON name/value format.</td></tr>
</tbody>
</table>
