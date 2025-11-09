# Requirements for

outputs

**Supported output types**

You can include any color space in any video in any supported output
type. The main consideration in choosing to convert to a color space in an
output is whether the intended downstream player can handle the color
space.

**Output requirements for HDR10 or Dolby
Vision**

There are specific requirements for converting to HDR10 or Dolby Vision
outputs.

| Requirement                                                                                                                                                                                                                                                                                                                                                  | Applies to converting to HDR10 | Applies to converting to Dolby Vision |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ | ------------------------------------- |
| Codec must be HEVC.                                                                                                                                                                                                                                                                                                                                          | Yes                            | Yes                                   |
| Profile must include the term _Main10_.                                                                                                                                                                                                                                                                                                                      | Yes                            | Yes                                   |
| For HD outputs, the event must run on an L800 series<br>appliance.                                                                                                                                                                                                                                                                                           | No                             | Yes                                   |
| For 4K outputs, the event must run on an appliance in the L730<br>series, the L840 series, or the L880 series.                                                                                                                                                                                                                                               | No                             | Yes                                   |
| You must obtain a license from<br>the<br>[AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations"). Note that pass through of Dolby Vision doesn't<br>require a license. | No                             | Yes                                   |
