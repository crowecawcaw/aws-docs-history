# Trick-play track via the Image

Media Playlist specification

In an HLS output group, you can support a trick-play track by
providing an asset that follows the Image Media Playlist
specification, version 0.4. The Elemental Live implementation follows
the time-based method of the specification. The specification is
located here:

[https://github.com/image-media-playlist/spec/blob/master/image_media_playlist_v0_4.pdf](https://github.com/image-media-playlist/spec/blob/master/image_media_playlist_v0_4.pdf "https://github.com/image-media-playlist/spec/blob/master/image_media_playlist_v0_4.pdf")

Roku is one example of a platform that implements this
specification.

## How the method

works

When you create the output group, you create standard outputs
in the usual way for the video, audio, and captions encodes.

You also create one or more outputs that each contains one
encode (stream). This encode is the asset that the downstream
player can use to implement the trick-play track. The encode
consists of a series of JPEG files, with one file for every
video segment. This means that the capture follows the
segmentation of the video encode, which means it provides the
best experience on the video player.

Elemental Live creates a main manifest and child manifests in
the usual way. The main manifest includes an
`EXT-X-IMAGE-STREAM-INF` tag for the frame
capture encode. The child manifest for the frame capture encode
contains `EXT-X-IMAGES-ONLY` tags. The contents and
format of these tags comply with the Image Media Playlist
specification.

## Setting up

You set up the trick-play track in the output group by
creating an additional output that contains a video encode that
consists of frame captures.

###### Note

The information in this section assumes that you are
familiar with the general steps for creating an
event.

###### To set up the frame capture encode in an HLS output

group

To create a frame capture encode in an HLS output group,
you create an output, and set up the video stream to use the
**Frame Capture to JPEG** video
codec.

1. In the **HLS Output Group**, in
   **HLS Outputs**, choose
   **Add Output** to add another
   output.
2. For that output, go to the Video
   section in the corresponding Stream
   section.
3. Choose **Video** and set up the video
   fields, including:
   - **Video Codec** –
     Choose **Frame Capture to
     JPEG**.
   - **Resolution** –
     Contact your downstream system to obtain the
     correct width and height. If you guess at the
     values, the experience on the downstream player
     might not be optimal.
   - **Trick Play** – Select
     this field. Many of the remaining fields
     disappear.

4. Choose **Audio 1** and choose
   **X** to remove the audio stream.
   The output must have only one encode (a video
   encode).

The output is part of the ABR stack and has the same
destination as the other encodes in the HLS output group.
