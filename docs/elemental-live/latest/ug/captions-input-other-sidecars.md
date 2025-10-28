# Information for SMI, SMPTE-TT, SRT, STL,

TTML

This section provides information specific to SMI, SMPTE-TT, SRT, STL, and TTML input
captions. describes the fields that appear when you choose **SCC** in the
**Source** field in the **Caption Selector** section
of the **Create New Live Event** screen. For more context, see [Step 1: Identify the
source captions that you want](identify-captions-in-the-input.md "identify-captions-in-the-input.md").

With these formats, the source captions are supplied in a captions file that is
external to the video input. You must specify this file.

- **External Caption File**: Specify the location of this file.
- **Time Delta**: Complete this field to adjust the timestamp in
  the caption file. With the SCC files, the situation sometimes arises where the
  timestamp in the file for the first captions does not work with the video. With these
  types of captions, the start time for both the video/audio always 00:00:00. Assume
  that, in the video, the first words are spoken at 00:06:15. But in the captions file,
  this time is marked as 00:06:18, and every other caption is also off by 3 seconds. The
  solution is to adjust the times in the captions file. In this example, subtract 3
  seconds from the captions file.

Enter a value in this field to push the captions earlier or later.

    + Enter a positive number to add to the times in the caption file. For example,
     enter `2` to add 2 seconds to all the times in the caption
     file.
    + Enter a negative number to subtract from the times in the caption file. For
     example, enter `-3` to remove 3 seconds from all the times in
     the caption file.
