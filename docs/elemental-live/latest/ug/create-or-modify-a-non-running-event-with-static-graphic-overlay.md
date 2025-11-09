# Create or modify a non-running event with static graphic

overlay

Create or modify an Elemental Live event and include one or more static graphic overlays.
This description assumes that you are familiar with the XML body for a live_event
aside from the data for the graphic overlay.

## HTTP

request and response

**HTTP URL**

```
POST http://<Live IP Address>/live_events
```

or:

```
PUT http://<Live IP Address>/live_events/<event ID>
```

**Body of request – one
input**

To insert the static overlay in one input element:

XML content consisting of one live_event element that contains:

- All the usual elements and tags.
- One input element that contains:
  - All the usual elements and tags.
  - One image_inserter element that contains:
    - One enable_rest tag.
    - One insertable_images element that contains:
      - 1 to 8 insertable_image elements that contain the tags
        listed in the following table.

For a representation of the XML structure, see [XML structure](xml-structure-static.md "xml-structure-static.md").

**Body of request – all outputs**

To insert the static overlay in all outputs:

XML content consisting of one live_event element that contains:

- All the usual elements and tags.
- One image_inserter element that contains:
  - One enable_rest tag.
  - One insertable_images element that contains:
    - 1 to 8 insertable_image elements that contain the tags listed
      in the table on the following page.

For a representation of the XML structure, see [XML structure](xml-structure-static.md "xml-structure-static.md").

**Body of request – outputs for one
stream assembly**

To insert the static overlay in the outputs associated with a given stream. XML
content consisting of one live_event element that contains:

- All the usual elements and tags.
- One stream_assembly element that contains:
  - All the usual elements and tags.
  - One image_inserter element that contains:
    - One enable_rest tag.
    - One insertable_images element that contains:
      - 1 to 8 insertable_image elements that contain the tags
        listed in the following table.

For a representation of the XML structure, see [XML structure](xml-structure-static.md "xml-structure-static.md").

**Child elements of
<insertable_image> and <image>**

| Element              | Type     | Required                                   | Description for creating                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | -------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| activate             | Boolean  | Required                                   | Required when adding or modifying an overlay in a running event<br>(not when creating an event or modifying a non-running event). This<br>tag has no effect when creating or modifying a non-running<br>event.<br>• Set to true when adding any overlay or<br>modifying an overlay (in specified the<br>layer) in an existing event.<br>• Set to false to delete the overlay<br>(specified in the layer tag) from the<br>underlying video. Note that the entire<br>overlay is also deleted from the event XML.<br>(If you do not specify a layer tag in the<br>body, the overlay won’t be deleted.)<br>\*_Note:_<br>• <activate> is distinct<br>from <active>, which is used with motion image inserter. |
| duration             | Integer  | Optional Default: until end of<br>event    | The time in milliseconds for the overlay to remain on the<br>video.<br>When creating an event, if this field is left blank, the overlay<br>will remain on the video as follows:<br>• In the Input section: Until this input<br>ends.<br>• In the Global Processor section: Until<br>the event ends.<br>• In the Output section: Until the event<br>ends.<br>The total running time of the overlay is fade_in + duration +<br>fade_out.                                                                                                                                                                                                                                                                   |
| fade_in              | Integer  | Optional                                   | The duration, in milliseconds, for<br>the overlay fade-in. This time is inserted before the start time of the<br>overlay.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| fade_out             | Integer  | Optional                                   | This field is valid only if the Duration field is completed.<br>The duration, in milliseconds, for the overlay fade-out. This time<br>is added to the overlay duration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| height               | Integer  | Optional Default: native height of overlay | The height of the overlay when inserted in the video, in<br>pixels.<br>When creating an event, leave blank to use the native height of the<br>overlay. The original overlay will be scaled up or down, to the<br>specified height.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| width                | Integer  | Optional Default: native width of overlay  | The width of the overlay when inserted in the video, in<br>pixels.<br>When creating an event, leave blank to use the native height of the<br>overlay. The original overlay will be scaled up or down, to the<br>specified width.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| image_inserter_input | Location | Required                                   | Overlay PNG or BMP file to insert.<br>For file requirement details, information about where to store this<br>file, and how to specify its location, see [Step A:<br>Prepare the overlay asset](step-a-prepare-the-overlay-asset.md "step-a-prepare-the-overlay-asset.md").                                                                                                                                                                                                                                                                                                                                                                                                                               |
| image_x              | Integer  | Required                                   | Placement of the left edge of the overlay relative to the<br>horizontal axis for the video frame, in pixels. 0 is the left edge of<br>the frame. When creating an event, cannot be omitted.<br>Take note of the width of the overlay and make sure that the<br>position of the left edge of the overlay does not cause the right edge<br>to be cropped.                                                                                                                                                                                                                                                                                                                                                  |
| image_y              | Integer  | Required                                   | Placement of the top edge of the overlay relative to the vertical<br>axis for the video frame, in pixels. 0 is the top edge of the frame.<br>When creating an event, cannot be omitted.<br>Take note of the height of the overlay and make sure that the<br>position of the top edge of the overlay does not cause the bottom edge<br>to be cropped.                                                                                                                                                                                                                                                                                                                                                     |
| layer                | Integer  | Required                                   | A number from 0 to 7 to specify the Z order of the inserted<br>overlay. “Z order” means that overlays with higher values of layer<br>will be inserted on top of overlays with lower values of layer.<br>Must always be specified.<br>In the XML for modifying a static overlay at runtime, if the XML<br>has more than one image container, then each layer tag must have a<br>different value. So each overlay must be in its own layer.                                                                                                                                                                                                                                                                |
| opacity              | Integer  | Optional Default: 50                       | The opacity of the overlay, as a<br>number from 0 to 100. 0 is transparent. 100 is fully opaque. When<br>creating an event, cannot be omitted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| start_time           | String   | Optional Default: beginning of the event   | The start time for the overlay.<br>Specify the start time in one of the formats discussed below this<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

**Start time
formats**

**Option 1**: Timecode format (HH:MM:SS:FF). The overlay start is determined by
comparing the specified start to the appropriate timecode.

- If the overlay is specified in the Input section: The start time for the
  static overlay will be compared to the input timecode (the timecode for a
  given input). The source for the input timecode is specified separately for
  each input (Input > Timecode Source field). The input timecode is calculated
  as follows:
  - If Timecode Source is Embedded: The timecode associated with each
    frame is extracted from the timecode carried with the input media.
    Note that each input will have its own timecode and the timecode may
    not align well from one input to another.
  - If Timecode Source field is Start at 0: The timecode of the first
    frame of the input is 00:00:00:00 and the timecode counts up with each
    successive frame. The timecode starts over with each input.
  - If Timecode Source field is System Clock or Local System Clock
    (AWS Elemental Live only): The timecode of each frame in the input is the
    system time at which the frame is decoded.

- If the overlay is specified in the Global Processor section: The overlay
  start is compared to the output timecode (which is shared by all outputs).
  The source for the output timecode is specified for the entire event, in the
  Timecode Config > Source field. The output timecode is calculated as
  follows:
  - If Source is Embedded: The timecode is extracted from the timecode
    carried with the input media. That timecode becomes the output
    timecode for the first transcoded frame. Then the output timecode
    counts up with each successive frame in the entire output.
  - If Source is Start at 0: The output timecode for the first frame is
    00:00:00:00 and then the output timecode counts up with each
    successive frame in the entire output.
  - If Source is System Clock or Local System Clock (AWS Elemental Live
    only): The output timecode for the first frame is the system time at
    which the frame is decoded. Then the output timecode counts up with
    each successive frame in the entire output.
  - If Source is Specified Start: The output timecode for the first
    frame is the time you specified when you selected this option as the
    timecode source. Then the output timecode counts up with each
    successive frame in the entire output.
  - If Source is External Reference Connector (AWS Elemental Live only):
    The timecode is extracted from external LTC source. That timecode
    becomes the output timecode for the first transcoded frame. Then the
    output timecode counts up with each successive frame in the entire
    output.

- If the static overlay is specified in the Output section: The start time
  for the static overlay is calculated in the same way as a static overlay in
  the Global Processor section.

**Option 2**: ISO 8601 UTC time with no dashes or colons. For example,
20160102T030405.678Z. In this case, the start time for every overlay (regardless
of whether it is defined in the input, the global processor or the output) will be
the UTC time.

**Option 3**: Only when adding or modifying an overlay in a running event (not when creating an event or modifying a non-running event), set this tag to an empty string to set the start time to “now”. With this option, the start time is never exact.

## Example

The following request creates an event with the name myLiveEvent and includes
one static overlay to insert the file logo.bmp. The overlay is inserted directly
inside the live_event, which means it will appear in all outputs.

```
POST http://198.51.100.22/live_events
```

```
<?xml version="1.0" encoding="UTF-8"?>
  <live_event>
    <name>myLiveEvent</name>
    ...
      <image_inserter>
        <enable_rest>true</enable_rest>
        <insertable_images>
          <insertable_image>
            <duration>30000</duration>
            <fade_in>10</fade_in>
            <fade_out>10</fade_out>
            <height>900</height>
            <left>300</left>
            <top>400</top>
            <layer>0</layer>
            <start_time>16:09:09:10</start_time>
            <width>800</width>
            <image_inserter_input>
              <uri>mnt/storage/logo.bmp</uri>
            </image_inserter_input>
          </insertable_image>
        </insertable_images>
      </image_inserter>
     ...
  </live_event>
```
