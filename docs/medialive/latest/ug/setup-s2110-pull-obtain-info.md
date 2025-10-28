# Obtain information

Obtain the following information from
the video
engineer who created the SMPTE 2110 SDP files:

- The location (URL) and file name of all the SDP files for the video,
  audio, and ancillary streams for the SMPTE 2110 source.

There should be only one video SDP file. There can be 0 or more audio SDP
files, and 0 or more ancillary SDP files.

- The number of video lines (v=) in the single video SDP file. If there is
  more than one video line, find out which line you must use.

You need the number of lines because you will need to identify the line to
use by specifying its position in a zero-based media index. For example, if
you need to use the third video line, the index is 2.

- The number of audio lines (a=) in each audio SDP file.

You need the number of lines because you will need to create a zero-based
media index of the audio lines whenever there is more than one SDP file,
and/or whenever there is more than one audio line in an SDP file.

For example, there might be two audio SDP files, one with one lines and
one with two lines. For the first file, you will create an index with one
member (0), and for the second file you will create an index with members 0
and 1.

- A list of the audio selectors you must create and the IDs of the channel
  groups (audio tracks) to include in each selector. (You don't need this
  information for video or ancillary streams.)

MediaLive assigns a track number to each channel group, starting with the
first channel group in the first line in the first SDP file, and covering
all the audio lines in all the audio SDP files. The tracks are numbered from

1.
