# Supported types of conversion

in MediaLive

You can configure a channel to use the standard MediaLive color corrector when converting
the color space. Or you can use a [3D LUTs color
corrector file](color-space-process-with-lut.md "color-space-process-with-lut.md") that you provide.

The following table shows which conversions MediaLive supports. Read across each row.

| From any of these color spaces in the source | To this color space in the output      | Supported?    |
| -------------------------------------------- | -------------------------------------- | ------------- |
| Rec. 709, HLG, HDR10                         | Rec. 601                               | Yes           |
| Rec. 601, HLG, HDR10                         | Rec. 709                               | Yes           |
| Rec. 601, Rec. 709, HLG                      | HDR10                                  | Yes           |
| Rec. 601, Rec. 709, HDR10                    | HLG                                    | Not supported |
| Rec. 601, Rec. 709, HLG, HDR10               | Dolby Vision 8.1                       | Yes           |
| Dolby Vision 8.1                             | Any color space supported by MediaLive | Not supported |
