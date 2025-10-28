# Scenario C – Correct the metadata with

fallback

During assessment of the MediaLive input, you might have determined the following:

- Different portions of the content are in different color spaces. All those color
  spaces are supported.

- The metadata for one color space is either inaccurate everywhere, or is sometimes
  accurate and sometimes inaccurate.
- The metadata for content for all the other color spaces is accurate.
  For example, the input has Rec. 601 content that has portions that are inaccurately
  marked. It also has portions that are missing, unknown, or unsupported. The input also has
  HDR10 content and HLG content that is accurately marked.

You have this option for handling the metadata in the output:

**Correct the metadata**

Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md "color-space-input-setup.md"), and set the key
fields as follows:

- **Color space** field – Set to the color space that has
  inconsistent metadata (Rec. 601 in the above example).
- **Color space usage** field – Set to
  **FALLBACK**
  During ingest, MediaLive will create metadata of the specific color space for all missing,
  unmarked, and unknown video content. It won't change any supported color space metadata.
  (It will _fall back_ to the existing metadata.)
  Therefore, it won't change the accurately marked Rec. 601 or the accurately marked HDR10
  or HLG content.

After ingest, all the content in the input will be consistently marked, even though
the content is in several color spaces.
