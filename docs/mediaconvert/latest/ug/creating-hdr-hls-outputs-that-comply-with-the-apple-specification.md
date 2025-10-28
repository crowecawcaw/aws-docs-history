# Creating HDR HLS outputs that comply with the Apple specification

For information about which Apple devices play back HDR content, see [Find and watch movies with 4K,
HDR, Dolby Vision, or Dolby Atmos](https://support.apple.com/en-us/HT207949 "https://support.apple.com/en-us/HT207949") in the Apple support
documentation.

To create HDR outputs that comply with the Apple specification, you must make
specific choices for your encoding settings. Specify the following settings:

- **Output group** – Choose **CMAF**
- **Encoding settings**, **Video codec** – Choose **HEVC
  (H.265)**.
- **Encoding settings**, **Codec details**, **MP4 packaging type** –
  **HVC1**.
- **Encoding settings**, **Codec details**, **Profile** – Choose
  **Main10/High**.
- **Encoding settings**, **Codec details**, **Level** – Choose **5**.
