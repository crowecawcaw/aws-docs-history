# How video is associated with audio rendition groups

The different “sets” of media are created as follows:

- Create one “video-only” stream assembly containing only one video stream.
- Create two or more “audio-only” stream assemblies, each containing only one audio
  stream.
- Assign “audio group IDs” to the audio-only streams. To group several audio streams into
  one rendition group, assign the same audio group ID to the relevant audio streams. To group
  other audio streams into another rendition group, define a different audio group ID and assign
  it to the relevant audio streams.
- Associate each video-only stream with its corresponding audio rendition group by assigning
  the desired audio group ID to that stream.
  For example:

- To group stream 3, 4 and 5 to one audio rendition group, set the audio group ID for each
  of these streams to “audio 1” or some other name of your choosing.
- To group streams 6, 7 and 8 to another audio rendition group, set the ID for each of these
  streams to “audio 2” or some other name.
- To associate video 1 with the first rendition group, set the “audio rendition sets ID” of
  that video to “audio 1”.
- To associate video 2 with the other group, set the audio rendition sets ID to “audio
  2.”
