# Creating a video encode from scratch

You can create a video encode by entering values in all the appropriate fields.
Follow this procedure for video in all types of outputs except for Frame capture
outputs.

1. On the **Create channel** page, find the output group
   that you [created](creating-a-channel-step4.md "creating-a-channel-step4.md").
2. Under that output group, find the output where you want to set up a
   video encode.
3. Choose the link for the video encode.
4. For **Codec settings**, choose the codec to use for
   this encode. More fields appear in several sections.
5. Complete each field as appropriate. For details about a field, choose
   the **Info** link next to the field.

###### Topics

- [Width and height
  (resolution)](#video-encode-resolution "#video-encode-resolution")
- [Rate control](#video-encode-ratecontrol-fields "#video-encode-ratecontrol-fields")
- [Framerate](#video-encode-framerate "#video-encode-framerate")
- [Codec details](#video-encode-codec-details "#video-encode-codec-details")
- [Timecode](#video-encode-timecode "#video-encode-timecode")
- [Color space](#video-encode-colorspace "#video-encode-colorspace")
- [Additional encoding
  settings](#video-encode-additional-settings "#video-encode-additional-settings")

## Width and height

(resolution)

For information about the **Width** and
**Height** fields (which define the video resolution),
choose the **Info** link for each field. The frame rate
affects the output charges for this channel. For more information about
charges, see [the MediaLive price
list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").

## Rate control

For information about the **Rate control** fields, see
[Setting the rate control mode](video-encode-ratecontrol.md "video-encode-ratecontrol.md"). There are fields in this
section that affect the output charges for this channel. For more
information about charges, see [the MediaLive price
list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").

## Framerate

For information about the **Framerate** fields, choose
the **Info** link for each field. The frame rate affects
the output charges for this channel. For more information about charges, see
[the MediaLive price
list](https://aws.amazon.com/medialive/pricing/ "https://aws.amazon.com/medialive/pricing/").

## Codec details

### Profile field

for H.264

The **Profile** field sets the profile, chroma
sampling, and bit depth.

| Value in \*_Profile_<br>• field | Profile  | Chroma Sampling | Bit Depth |
| ------------------------------- | -------- | --------------- | --------- |
| **Baseline**                    | Baseline | 4:2:0           | 8-bit     |
| **Main**                        | Main     | 4:2:0           | 8-bit     |
| **High**                        | High     | 4:2:0           | 8-bit     |
| **High 10bit**                  | High     | 4:2:0           | 10-bit    |
| **High 422**                    | High     | 4:2:2           | 8-bit     |
| **High 422 10bit**              | High     | 4:2:2           | 10-bit    |

### Profile field

for H.265

The **Profile** field sets the profile, chroma
sampling, and bit depth.

| Value in Profile field | Profile | Chroma Sampling | Bit Depth |
| ---------------------- | ------- | --------------- | --------- |
| **Main**               | Main    | 4:2:0           | 8-bit     |
| **Main_10BIT**         | Main    | 4:2:0           | 10-bit    |

### Bit depth and level

fields for AV1

The **Bit Depth** field sets the bit depth for the
AV1 output encode. Choose **DEPTH_8** for 8-bit output
or **DEPTH_10** for 10-bit output. If you don't
specify a value, the default is 8-bit.

The **Level** field sets the level. Other encoding
schemes (profile, chroma sampling, and tier) are hard-coded. For more
information, see [Encoding schemes for the
AV1 codec](video-characteristics-encoding-schemes.md#video-characteristics-encoding-schema-av1 "video-characteristics-encoding-schemes.md#video-characteristics-encoding-schema-av1").

## Timecode

For information about the **Timecode** fields, see [Working with timecodes and timestamps](timecode.md "timecode.md").

## Color space

For information about the **Color space** fields, see
[Handling complex color space conversions](color-space.md "color-space.md").

## Additional encoding

settings

For information about the **Additional encoding
setting**s fields, see [Setting up enhanced VQ mode](video-enhancedvq.md "video-enhancedvq.md")
