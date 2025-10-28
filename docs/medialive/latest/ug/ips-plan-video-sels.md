# Plan the video selectors

You can extract only one video from each MediaLive input. If a given input contains more than
one video, then create a video selector to extract that specific video. If a given input
contains only one video, there is no need to create a video selector. AWS Elemental MediaLive automatically
finds and extracts that video. On the output side, MediaLive automatically uses that one video
asset.
