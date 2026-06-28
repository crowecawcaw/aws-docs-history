This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Setting Up HDR Jobs Using the REST API

This section provides information for setting up your AWS Elemental Server job and
profile XML for HDR.

To use the information in this section, you should understand:

- The conceptual information provided in the main body of this document.
- How to create and modify jobs using XML.

## XML Reference Tables for HDR

Managing Overwrite of Source Metadata| Element | Notes |
| --- | --- |
| job | Top-level element |
| | input | |
| | | video\_selector | Corresponds to the Video Selector section of the UI, under Input<br>> Advanced. One <video\_selector> element exists per job, which<br>applies to all outputs. |
| | | | force\_color | Corresponds to the Force Color checkbox in the UI. Set to<br>`true` to overwrite the source metadata with the<br>values in <color\_space> and, for HDR10, the children of<br><hdr10\_metadata>. Set to `false` to retain metadata<br>from the source. |
| | | | color\_space | Corresponds to the Color Space dropdown in the Video Selector<br>section of the UI.<br>Valid values are: follow, rec\_601, rec\_709, hdr10,<br>hlg\_2020 |
| | | | hdr10\_metadata | Contains children for specifying master display information for<br>HDR10. See the table below. |

Metadata Specific to HDR10| **Child of<br><hdr10\_metadata>** | **Valid Range** |
| --- | --- |
| red\_primary\_x | 0-50000 |
| red\_primary\_y | 0-50000 |
| green\_primary\_x | 0-50000 |
| green\_primary\_y | 0-50000 |
| blue\_primary\_x | 0-50000 |
| blue\_primary\_y | 0-50000 |
| white\_point\_x | 0-50000 |
| white\_point\_y | 0-50000 |
| min\_lumninance | 0-2147483647 |
| max\_luminance | 0-2147483647 |
| maxcll | 0<br>• 65535 |
| maxfall | 0<br>• 65535 |

For the following table, different outputs can have different values for
`<insert_color_metadata>` because this setting is contained in the
stream assembly.

Including or Excluding Metadata from Outputs| Element | Notes |
| --- | --- |
| job | Top-level element |
| | stream\_assembly | Use one <stream\_assembly> element for each set of encoding<br>instructions you need. |
| | | name | Use the value of this element to map a stream assembly to an<br>output. |
| | | video\_description | Contains settings for how the video is encoded. |
| | | | insert\_color\_metadata | Set to `true` to include color metadata in the output;<br>set to `false` to exclude it. |
| | output group | Use one output group element for each video package type<br>produced.<br>Different outputs within the group can have different sets of<br>encoding instructions (different stream assemblies) applied to<br>them. |
| | | output | Represents the actual set of elementary streams delivered to a<br>single destination address. |
| | | | stream\_assembly\_name | Set the value of this element to match that of a<br><stream\_assembly>/<name> element, which associates this<br>output with the stream assembly. |

For the following table, different outputs can have different settings for color
correction because this setting is contained in the stream assembly.

Color Correction| Element | Notes |
| --- | --- |
| job | Top-level element |
| | stream\_assembly | Use one <stream\_assembly> element for each set of encoding<br>instructions you need. |
| | | name | Use the value of this element to map a stream assembly to an<br>output. |
| | | | video\_preprocessors | |
| | | | | color\_corrector | Include this element if you want color correction on your<br>output. |
| | | | | | color\_space\_conversion | Use this element to specify the color space or format you want<br>your video stream converted to.<br>Supported conversions are between HDR10 and HLG, from either<br>rec. 601 or rec. 709 to either HDR10 or HLG, and between rec.<br>601 and rec. 709.<br>Valid values are: none, force\_601, force\_709, force\_hdr10,<br>force\_hlg\_2020 |
| | | | | | brightness | Provide brightness correction value here.<br>Valid range is: 1 through 100 |
| | | | | | contrast | Provide contrast correction value here.<br>Valid range is: 1 through 100 |
| | | | | | hue | Provide hue correction value here.<br>Valid range is: -180 through 180 |
| | | | | | saturation | Provide saturation correction value here.<br>Valid range is: 1 through 100 |
| | | | | | hdr10\_metadata | Contains children for specifying master display information for<br>HDR10. See the table below. |
| | output group | Use one output group element for each video package type<br>produced.<br>Different outputs within the group can have different sets of<br>encoding instructions (different stream assemblies) applied to<br>them. |
| | | output | Represents the actual set of elementary streams delivered to a<br>single destination address. |
| | | | stream\_assembly\_name | Set the value of this element to match that of a<br><stream\_assembly>/<name> element, which associates this<br>output with the stream assembly. |

The following table shows HDR10-specific metadata structures and ranges for which
values for the elements must be supplied by your color grader or another upstream
source along with information about your specific video asset.

Metadata Specific to HDR10| Child of <hdr10\_metadata> | Valid Range |
| --- | --- |
| red\_primary\_x | 0-50000 |
| red\_primary\_y | 0-50000 |
| green\_primary\_x | 0-50000 |
| green\_primary\_y | 0-50000 |
| blue\_primary\_x | 0-50000 |
| blue\_primary\_y | 0-50000 |
| white\_point\_x | 0-50000 |
| white\_point\_y | 0-50000 |
| min\_lumninance | 0-2147483647 |
| max\_luminance | 0-2147483647 |
| maxcll | 0<br>• 65535 |
| maxfall | 0<br>• 65535 |
