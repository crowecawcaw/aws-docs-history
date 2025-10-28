# Scenario B – Metadata can be corrected with

force

During assessment of the MediaLive input, you might have determined the following:

- The content is in one color space, and that is a supported color space.
- The color space metadata is inaccurate. It could be any combination of inaccurate,
  missing, unknown, or unsupported (inaccurately marked as a color space that MediaLive
  doesn't support).
  Note that this is the scenario that always applies if the input is from an AWS Elemental Link
  device.

You have this option for handling the metadata in the output:

**Correct the metadata**

You can correct the metadata. Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md "color-space-input-setup.md"), and set the key fields as follows:

- **Color space** field – Set to the color space that has
  unacceptable metadata.
- **Color space usage** field – Set to
  **FORCE**
  During processing, MediaLive will create metadata of the specified color space for all
  missing, unmarked, and unknown metadata. It will also change all existing metadata to the
  specified color space. (It will _force_ the
  metadata.)

After ingest, all the content in the input will be consistently marked as one color
space.
