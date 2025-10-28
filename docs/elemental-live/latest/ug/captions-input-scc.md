# Information for SCC

This section provides information specific to SCC input captions. It describes the
fields that appear when you choose **SCC** in the
**Source** field in the **Caption Selector** section
of the event. For more context, see this procedure.

SCC source captions are supplied in a captions file that is external to the video
input. You must specify this file.

- **External Caption File**: Specify the location of the file.
- **Time Delta**: Complete this field to adjust the timestamp in
  the caption file. With the SCC files, the situation sometimes arises where the
  timestamp in the file for the first captions does not work with the video. The start
  time for the video/audio always 00:00:00. The start time of the captions may not be
  00:00:00 – it may be some completely different, arbitrary time, such as 20:00:15.
  Assume that, in the video, the first words are spoken at 00:06:15. But given that the
  start time for the captions file is 20:00:15, then the time for the first caption will
  be marked as 20:06:30. This time will usually never work with the video. The solution
  is to adjust the times in the captions file. In this example, subtract 20 hours and 15
  seconds (72015 seconds) from the captions file.

Enter a value in this field to push the captions earlier or later:

    + Enter a positive number to add to the times in the caption file. For example,
     enter `15` to add 15 seconds to all the times in the caption
     file.
    + Enter a negative number to subtract from the times in the caption file. For
     example, enter `-5` to remove 5 seconds from all the times in
     the caption file.

The format of the times in the captions does not have to match the value in the
**Timecode Config** field (in the Input) of the video.
The number you enter in this field will simply delay the captions or make the captions
play earlier, regardless of the formats.

When using SCC, the video must absolutely have a value in the **Timecode Config** field. Otherwise the captions will not be
inserted.

- **Force 608 to 708 Upconvert**: SCC source captions are EIA-608
  format and are contained in an external file. The options for converting the caption
  are the following:
  - Check: To convert the captions to CEA-708 format.
  - Unchecked: To leave the captions unconverted.
