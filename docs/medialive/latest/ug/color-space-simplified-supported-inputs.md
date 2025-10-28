# Input requirements

MediaLive can work with the [supported color
space](color-space-simplified-standards.md "color-space-simplified-standards.md") in all [supported types of
input](inputs-supported-formats.md "inputs-supported-formats.md") with the following notes.

**Elemental Link input**

MediaLive can't read the color space metadata in a source from an AWS Elemental Link device. The
workaround when you set up the input is to specify the color space that applies, as
described in [Configuring the inputs](color-space-simplified-setup-input.md "color-space-simplified-setup-input.md").

**Source when converting to Dolby Vision 8.1**

- The video source must be HD or 4K resolution. In other words, the source must be
  1080p or higher.
- The video source can't be a file. This means that the source can't be a VOD asset in
  an MP4 file or in a transport stream file.
  These constraints are stipulated by Dolby Vision 8.1, and relate to the minimal video
  quality required to produce Dolby Vision 8.1 outputs that meet the Dolby Vision 8.1
  standard.
