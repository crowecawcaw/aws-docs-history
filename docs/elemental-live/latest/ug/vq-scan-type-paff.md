# Adaptive

field frame controls

## Description

The
following are the settings and internal algorithms tied to the scan type:

-
- **Picture Adaptive Field Frame (PAFF)**:
  This setting is automatically enabled on GPU-enabled versions of
  Elemental Live and automatically disabled on CPU-only versions.
- **Macroblock Adaptive Field Frame
  (MBAFF)**: This setting is automatically enabled on CPU-only
  versions of Elemental Live and automatically disabled on GPU-enabled
  versions.
- **Force Field Pictures**: This field
  appears only if the codec is H.264 and only affects GPU-enabled versions
  of Elemental Live.
  - **Enabled**: All outputs are forced to
    use PAFF field picture encoding.
  - **Disabled**: Elemental Live switches
    between PAFF and MBAFF, depending on the content.

## Recommendations

- **Force Field Pictures** results in a
  significant reduction in quality so it should only be used if required for
  compatibility with specific decoders or playback devices.

## Location of fields

| Location of field on web interface                | Location of tag in XML                                                                                 |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Streams – Video > Advanced > Force Field Pictures | stream_assembly/video_description/`codec`/force_field_pictures<br>where `codec` is:<br>`h264_settings` |
