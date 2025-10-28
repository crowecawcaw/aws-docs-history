# Enabling trick-play in AWS Elemental MediaPackage

Trick-play, sometimes called trick mode, provides a visual cue to viewers
as they rewind, fast-forward, or seek through content in a digital video player. This helps
the person using the video player to visualize where they are in the content
timeline.

MediaPackage
supports the following trick-play types:

**Supported trick-play types for live workflows**

| Streaming protocol     | I-frame only | Image-based |
| ---------------------- | ------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HLS with TS segments   | √            | √           |
| HLS with CMAF segments | √            | √           |
| DASH                   | √            | √           | The following sections describe how to enable trick play in MediaPackage. ###### Topics <br>• [Using I-frame playlists](using-i-frame-playlists.md "using-i-frame-playlists.md") <br>• [Using image media playlists](using-image-media-playlists.md "using-image-media-playlists.md") |
