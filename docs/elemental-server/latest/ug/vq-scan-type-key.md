This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Image Processing – Scan Type – Key Controls

## Description

You can convert the scan type of the input to a different scan type: progressive,
interlaced, hard telecine, or soft telecine. You can configure to leave the scan type as is or
to convert from one incoming type (or a mix of incoming scan types) to another single type.
Configuring for scan type conversion involves setting fields in specific ways. The three key
fields to convert the scan type of the input are **Configuration - Deinterlace
Mode**, **Configuration - Interlace Mode**, and
**Configuration - Telecine**. The following table describes how to set these
three key fields to convert a given input to a given output.

| Input         | Output        | Configuration<br>• Deinterlace Mode | Configuration<br>• Interlace Mode | Configuration<br>• Telecine |
| ------------- | ------------- | ----------------------------------- | --------------------------------- | --------------------------- |
| Progressive   | Progressive   | Off                                 | Progressive                       | None                        |
| Interlaced    | Progressive   | Deinterlace                         | Progressive                       | None                        |
| Interlaced    | Progressive   | Adaptive                            | Progressive                       | None                        |
| Hard telecine | Progressive   | Inverse telecine                    | Progressive                       | None                        |
| Hard telecine | Progressive   | Adaptive                            | Progressive                       | None                        |
| Soft telecine | Progressive   | Off                                 | Progressive                       | None                        |
| Mixed         | Progressive   | Adaptive                            | Progressive                       | None                        |
| Progressive   | Hard telecine | Off                                 | One of the other options          | Hard telecine               |
| Hard telecine | Hard telecine | Off                                 | One of the other options          | None                        |
| Soft telecine | Hard telecine | Off                                 | One of the other options          | Hard telecine               |
| Mixed         | Hard telecine | Off                                 | One of the other options          | Hard telecine               |
| Interlaced    | Interlaced    | Off                                 | One of the other options          | None                        |
| Mixed         | Interlaced    | Off                                 | One of the other options          | None                        |
| Progressive   | Soft telecine | Off                                 | One of the other options          | Soft telecine               |
| Hard telecine | Soft telecine | Inverse telecine                    | One of the other options          | Soft telecine               |
| Hard telecine | Soft telecine | Adaptive                            | One of the other options          | Soft telecine               |
| Soft telecine | Soft telecine | Off                                 | One of the other options          | Soft telecine               |
| Mixed         | Soft telecine | Adaptive                            | One of the other options          | Soft telecine               |

\* Deinterlace Mode is an image processing control. Interlace Mode and Telecine are
encoding controls.

**Note: Converting the Scan Type to Progressive**

If content is not being converted to a higher framerate, the deinterlacer outputs one
frame for every two fields in the source content (i.e., 1080i30 content is converted to
1080p30). If the framerate is being doubled (e.g. 29.97 fps to 59.94 fps, 29.97 to 60, or 25 to
50), the deinterlacer converts each field into a frame.

**Deinterlace Mode**

This field applies an initial conversion for certain from/to conversions (as shown in the
table above).

- **Deinterlace**: Applies a deinterlace algorithm to content. If
  the AWS Elemental system detects that the source content is already progressive, no
  deinterlacing is applied.
- **Inverse Telecine**: Converts hard telecine 29.97i to
  progressive 23.976p.
- **Adaptive**: Analyzes source content to determine whether
  to apply the deinterlace or inverse telecine algorithm on source content.

**Interlace Mode**

This field controls video field order and how the scan type is represented in the output
bitstream.

- **Progressive**: Encodes output as "progressive."
- **Top Field First** or **Bottom Field
  First**: Forces field polarity (top or bottom first) to the specified value,
  reordering fields if the source has a different order and encodes the result as interlaced.
- **Follow (Default Top)** and **Follow
  (Default Bottom)**: Produces interlaced output, with the output having the same
  field polarity as the source. Therefore:
  - If the source is "interlaced", the output is interlaced with the same polarity as the
    source (it follows the source). The output could therefore be a mix of “top field first”
    and “bottom field first.”
  - If the source is "progressive", the output is interlaced with “top field first” or
    “bottom field first” polarity (depending on which Follow option you chose).

Note: If the output codec is Microsoft VC-1, then the interlace mode is always set to
"progressive."

**Telecine**

This field appears for MPEG-4 AVC and MPEG-2 only if the Streams > Advanced > framerate
field is set to 29.970.

- **Hard**: Produce 29.97i output from 23.976 input.
- **Soft**: Produce 23.976; the player converts this output
  to 29.97i.

## Recommendations

- Converting to progressive output always improves output quality and should be enabled in
  any use case where progressive output is required or acceptable.
- Interlace coding is inherently less efficient than progressive coding so use interlace
  coding only for content that has already been interlaced.
- The choice of deinterlacing algorithm is very subjective. **Motion
  Adaptive Interpolation** is generally recommended as the sharper image quality
  tends to provide the best perceived quality across a broad set of users. Use the **Force Mode** option for deinterlacing only when the input is known to
  be interlaced content incorrectly flagged as "progressive."
- Use the **Force Mode** option for **Inverse Hard Telecine** when the input is known to consist entirely of Hard
  Telecine content.

## Location of Fields

| Location of Field on Web Interface                                       | Location of Tag in XML                                                                                                                                                                                    |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streams > Advanced > Telecine                                            | stream_assembly/video_description/`codec`/telecinewhere `codec` is one of the following:<br>• `h264_settings`<br>• `mpeg2_settings`<br>• `h265_settings`<br>• `prores_settings`                           |
| Streams > Advanced > Interlace Mode                                      | stream_assembly/video_description/`codec`/interlace_modewhere `codec` is one of the following:<br>• `vc1_settings`<br>• `h264_settings`<br>• `mpeg2_settings`<br>• `h265_settings`<br>• `prores_settings` |
| Streams > Advanced >Preprocessors > Deinterlacer > Deinterlace Mode      | stream_assembly/video_description/video_preprocessors/deinterlacer/deinterlace_mode                                                                                                                       |
| Streams > Advanced >Preprocessors > Deinterlacer > Deinterlace Algorithm | stream_assembly/video_description/video_preprocessors/deinterlacer/algorithm                                                                                                                              |
| Streams > Advanced >Preprocessors > Deinterlacer > Force Mode            | stream_assembly/video_description/video_preprocessors/deinterlacer/force                                                                                                                                  |
