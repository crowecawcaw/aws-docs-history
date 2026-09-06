

# Step B: Initial setup
<a name="step-b-initial-setup"></a>

Create or modify the event as follows: 

1. Determine the location or locations in the event where the static overlay should be inserted, then display the appropriate section:
   + Input section: In the desired input or inputs, click Advanced. More fields appear. In the Image Inserter section, click On. More fields appear; see the table in the next step. 
   + Global Processors section: In the Global Processors section, go to the Image Inserter field and click On. More fields appear; see the table in the next step. 
   + Output section: In the desired output or outputs, determine the stream this output is associated with. In the corresponding Stream section, click Advanced. More fields appear; see the table in the next step. 

   For all locations, the following fields appear. (Note that the following image is from the Global Processors section, but the fields are the same in all sections.)   
![images/screenshot_StaticImgInst.png](http://docs.aws.amazon.com/elemental-live/latest/ug/images/screenshot_StaticImgInst.png)

1.  Complete the fields as follows:    
<a name="step-b-initial-setup-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/step-b-initial-setup.html)

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