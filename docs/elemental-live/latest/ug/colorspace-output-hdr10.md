# Converting color space: Procedure B

Follow this procedure to convert to one of these color spaces:

- HDR10
- Dolby Vision
  For information about the source color spaces that you can convert to one
  of these color spaces, see [Support for conversion and
  passthrough](color-space-conversions.md "color-space-conversions.md").

For information about the results of conversion, see [The results of different types of conversions](color-space-conversion-results.md "color-space-conversion-results.md").

###### To set up each output

###### Note

This section assumes that you are familiar with creating or editing
an event.

Follow this procedure in each output.

1. On the **Event** page, in the **Output
   groups** section, choose the output group, and choose the
   output that contains the video.
2. Open the **Advanced** section. More fields
   appear.
3. Scroll down to the **Preprocessors** section and
   turn on **Color Corrector**. More fields appear.
4. Complete fields in the **Video** section as
   described in the following table.

| Field                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Video Codec**                                                                                        | If you are converting to HDR10, choose **MPEG-4 AVC<br>(H.264)\*<br>• or **HEVC (H.265)**.<br>If you are<br>converting<br>to Dolby Vision, choose **HEVC (H.265)\*\*.                                                                                                                                                                                                  |
| **Advanced**, then **Insert Color<br>Metadata**                                                        | Leave this field checked.<br>You should never remove the color metadata if you are converting<br>the color space.                                                                                                                                                                                                                                                      |
| **Advanced**, then<br>**Profile**<br>This field is towards the end of the<br>\*_Advanced_<br>• section | Choose a profile that includes the term **Main10**.                                                                                                                                                                                                                                                                                                                    |
| **Preprocessors**, then **Video<br>Range**                                                             | Choose the correct option, according to the information you [obtained from the content provider](color-space-input-procedure.md "color-space-input-procedure.md"):<br>• If the video input is full range, choose **Passthrough**.<br>• If the video input is video range, choose **Full Swing**.                                                                       |
| **Preprocessors**, then **Color Space<br>Conversion**                                                  | Choose the correct conversion:<br>**Force HDR10**<br>**Dolby Vision Profile 5**<br>**Dolby Vision Profile 8.1**                                                                                                                                                                                                                                                        |
| **Preprocessors**, then **HDR Master<br>Display Information**                                          | These fields appear after you complete the **Color Space<br>Conversion**.<br>You can optionally complete the \*_HDR Master Display<br>Information_<br>• fields. For information about<br>master<br>display information, see [Tips for HDR<br>master display information](#hdr-tips-for-hdr-master-display-information "#hdr-tips-for-hdr-master-display-information"). |

## Tips for HDR

master display information

The HDR Master Display Information fields appear if you are converting to HDR10 or Dolby
Vision. Take the appropriate action:

- If you have previously converted similar content to HDR10 and a
  color grading specialist in your organization has given you metadata,
  then enter it here. The values to enter here depend on the downstream
  player, so there is no point to asking your content provider for
  values.

For details about a field on the web interface, choose the question
mark next to the field.

- If you don't have metadata to use, set all fields to null values.
  It's better to set the fields to null values, rather than to make up
  values or to use the default values.

### Red, green, blue, white point x and

y

Your color grader might provide numbers like this for X and Y
points:

- G (x=0.265, y=0.690)
- B (x=0.150, y=0.060)
- R (x=0.680, y=0.320)

You must convert these numbers to numbers like this:

- G (13250, 34500)
- B (7500, 3000)
- R (34000, 16000)

To convert between the two formats, divide each number by 0.00002 as
per the HEVC specification.

For example, 0.265 divided by 0.00002 is 13250.

### Max luminance and min

luminance

The maximum and minimum luminance are given in units of **0.0001 candelas per square meter**. Your color
grader might provide this value in candelas per square meter instead. If
so, then convert these numbers by multiplying by 10,000, then entering the
result in the web interface.

For example, a value of 1000.0000 cd/m2 for max luminance would be
converted to 10,000,000 and entered as that in the web interface.
