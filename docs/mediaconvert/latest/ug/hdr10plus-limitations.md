# Requirements for creating HDR10+ outputs

For information about which devices play back HDR 10+ content and test content, see [https://hdr10plus.org.](https://hdr10plus.org/ "https://hdr10plus.org/")

You must use the following rules to create HDR 10+ outputs in AWS Elemental MediaConvert:

- Your input source video pixels must be HDR10, that is, **Color
  space** must be set to **Follow** or the Color
  corrector preprocessor must have **Color space conversion**
  set to **Force HDR 10**.
- Set **Video codec** to **HEVC
  (H.265)**.
- Set **Profile** to **Main10/Main** or **Main10/High**
- Set **Quality tuning level** to **Multi-pass HQ**.
- You cannot use the Dolby Vision preprocessor.
