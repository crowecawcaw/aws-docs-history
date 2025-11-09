This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – Scan Type

## Description

The scan type of content can affect the video quality. The following are the settings and
internal algorithms tied to the scan type:

- The encoding controls that deal with scan type are dealt with in [Image Processing – Scan Type – Key Controls](vq-scan-type-key.md "vq-scan-type-key.md").
- **Picture Adaptive Field Frame (PAFF)**: This control is
  automatically enabled on Graphics Processing Unit (GPU)-enabled versions of the software and
  automatically disabled on Central Processing Unit (CPU)-only versions.
- **Macroblock Adaptive Field Frame (MBAFF)**: This control
  is automatically enabled on CPU-only versions of the software and automatically disabled on
  GPU-enabled versions.
- **Force Field Pictures**: This field appears only if the
  codec is H.264 and only affects GPU-enabled versions of the software.
  - **Enabled**: All outputs are forced to use PAFF field
    picture encoding.
  - **Disabled**: The encoder switches between PAFF and
    MBAFF, depending on the content.

## Recommendations

- **Force Field Pictures** results in a significant reduction
  in quality so it should only be used if required for compatibility with specific decoders or
  playback devices.

## Location of Fields

| Location of Field on Web Interface                   | Location of Tag in XML                                                                                 |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Streams – Video > Advanced > Force Field<br>Pictures | stream_assembly/video_description/`codec`/force_field_pictures<br>where `codec` is:<br>`h264_settings` |
