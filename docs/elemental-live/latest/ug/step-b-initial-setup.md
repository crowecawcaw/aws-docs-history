

# Step B: Initial setup
<a name="step-b-initial-setup"></a>

Create or modify the event as follows: 

1. Determine the location or locations in the event where the static overlay should be inserted, then display the appropriate section:
   + Input section: In the desired input or inputs, click Advanced. More fields appear. In the Image Inserter section, click On. More fields appear; see the table in the next step. 
   + Global Processors section: In the Global Processors section, go to the Image Inserter field and click On. More fields appear; see the table in the next step. 
   + Output section: In the desired output or outputs, determine the stream this output is associated with. In the corresponding Stream section, click Advanced. More fields appear; see the table in the next step. 

   For all locations, the following fields appear. (Note that the following image is from the Global Processors section, but the fields are the same in all sections.)   
![images/screenshot_StaticImgInst.png](https://docs.aws.amazon.com/elemental-live/latest/ug/images/screenshot_StaticImgInst.png)

1.  Complete the fields as follows:

<a name="step-b-initial-setup-table"></a>
<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Image Location</td><td>The location and filename of the PNG or BMP image file.<br />For file requirement details, information about where to store this file, and how to specify its location, see <a href="step-a-prepare-the-overlay-asset.md">Step A: Prepare the overlay asset</a>.<br />For S3, use <code>sse=true</code> to enable S3 Server Side Encryption (SSE) and <code>rrs=true</code> to enable Reduced Redundancy Storage (RRS). Default values for RRS and SSE are <code>false</code>.</td></tr>
  <tr><td>Username Password</td><td>If access to your local or mounted directory requires a username and password, click the lock icon next to the Image Location field to show the Username and Password fields.<br />For S3, Enter the Access Key ID in the username field. Enter the Secret Access Key in the password field.</td></tr>
  <tr><td>Layer</td><td>A number from 0 to 7 for the Z order of the static overlay. “Z order” means that static overlays with higher values of layer will be inserted on top of static overlays with lower values of layer.<br />Default is 0.</td></tr>
  <tr><td>Left</td><td>Placement of the left edge of the motion overlay relative to the left edge of the video frame, in pixels. 0 is the left edge of the frame.<br />Take note of the width of the motion overlay and make sure that the position of the left edge of the motion overlay does not cause the right edge to be cropped.</td></tr>
  <tr><td>Top</td><td>Placement of the top edge of the motion overlay relative to the top edge of the video frame, in pixels.0 is the top edge of the frame. Default is 0.<br />Take note of the height of the motion overlay and make sure that the position of the top edge of the motion overlay does not cause the bottom edge to be cropped.</td></tr>
  <tr><td>Opacity</td><td>The opacity of the static overlay, as a number from 0 to 100. 0 is transparent. 100 is fully opaque. Default is 50.</td></tr>
  <tr><td>Width</td><td>The width of the static overlay when inserted in the video, in pixels. Leave blank to use the native width of the static overlay. The original static overlay will be scaled up or down, to the specified width.</td></tr>
  <tr><td>Height</td><td>The height of the static overlay when inserted in the video, in pixels. Leave blank to use the native height of the static overlay. The original static overlay will be scaled up or down, to the specified height. </td></tr>
  <tr><td>Start Time</td><td>The start time for the overlay. Specify the start time in one of the formats listed at <a href="#start-time-formats">Start time formats</a>.</td></tr>
  <tr><td>Duration</td><td>The amount of time, in milliseconds, for the overlay to remain on the video.<br />If this field is left blank, the static overlay will remain on the video as follows:<ul><li>  In the Input section: Until this input ends.  </li><li>  In the Global Processor section: Until the event ends. </li><li>  In the Output section: Until the event ends.  </li></ul><br />The total running time of the static overlay is Fade in + Duration + Fade out.</td></tr>
  <tr><td>Fade In</td><td>The duration, in milliseconds, for the static overlay fade-in. This time is inserted before the start time of the static overlay.</td></tr>
  <tr><td>Fade Out</td><td>This field is valid only if the Duration field is completed.<br />The duration, in milliseconds, for the static overlay fade-out. This time is added to the static overlay duration.</td></tr>
  <tr><td>Enable Rest Control</td><td>Check this field only if you plan to manage motion overlays via the REST API, after this initial setup via the web interface. Typically, you will want this tag to be true. </td></tr>
</tbody>
</table>


1. If desired, click Add Image and enter the information for another static overlay, up to a maximum of 8 static overlays. 
   + Assign a unique Layer number to each static overlay. The layers do not have to appear in any particular order on the screen, but each number must be used once only.
   + The static overlay Start Time and Duration can be set so that any static overlay overlaps the display time of any other static overlay. 
   +  The Left/Top fields can be set so that any static overlay physically overlaps any other static overlay, as much as you want; the static overlays are displayed according to their Layer value.

Note: If you are using input switching to provide input redundancy (with or without the hot-hot backup mode), then make sure you insert the static overlay in both input pairs. 

## Start time formats
<a name="start-time-formats"></a>

**Option 1**: Timecode format (HH:MM:SS:FF). The overlay start is determined by comparing the specified start to the appropriate timecode. 
+ If the overlay is specified in the Input section: The start time for the static overlay will be compared to the input timecode (the timecode for a given input). The source for the input timecode is specified separately for each input (Input > Timecode Source field). The input timecode is calculated as follows: 
  + If Timecode Source is Embedded: The timecode associated with each frame is extracted from the timecode carried with the input media. Note that each input will have its own timecode and the timecode may not align well from one input to another. 
  + If Timecode Source field is Start at 0: The timecode of the first frame of the input is 00:00:00:00 and the timecode counts up with each successive frame. The timecode starts over with each input. 
  + If Timecode Source field is System Clock or Local System Clock (AWS Elemental Live only): The timecode of each frame in the input is the system time at which the frame is decoded. 
+ If the overlay is specified in the Global Processor section: The overlay start is compared to the output timecode (which is shared by all outputs). The source for the output timecode is specified for the entire event, in the Timecode Config > Source field. The output timecode is calculated as follows: 
  + If Source is Embedded: The timecode is extracted from the timecode carried with the input media. That timecode becomes the output timecode for the first transcoded frame. Then the output timecode counts up with each successive frame in the entire output. 
  + If Source is Start at 0: The output timecode for the first frame is 00:00:00:00 and then the output timecode counts up with each successive frame in the entire output. 
  + If Source is System Clock or Local System Clock (AWS Elemental Live only): The output timecode for the first frame is the system time at which the frame is decoded. Then the output timecode counts up with each successive frame in the entire output. 
  + If Source is Specified Start: The output timecode for the first frame is the time you specified when you selected this option as the timecode source. Then the output timecode counts up with each successive frame in the entire output. 
  + If Source is External Reference Connector (AWS Elemental Live only): The timecode is extracted from external LTC source. That timecode becomes the output timecode for the first transcoded frame. Then the output timecode counts up with each successive frame in the entire output. 
+ If the static overlay is specified in the Output section: The start time for the static overlay is calculated in the same way as a static overlay in the Global Processor section. 

**Option 2**: ISO 8601 UTC time with no dashes or colons. For example, 20160102T030405.678Z. In this case, the start time for every overlay (regardless of whether it is defined in the input, the global processor or the output) will be the UTC time. 

**Option 3**: Only when adding or modifying an overlay in a running event (not when creating an event or modifying a non-running event), set this tag to an empty string to set the start time to “now”. With this option, the start time is never exact. 