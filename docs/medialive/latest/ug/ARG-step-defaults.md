# Determine Defaults and Selection

Rules

As the second part of planning the audio rendition group, you should identify the
following:

- The rendition (if any) that is the default.
- How auto-selection will work for the non-default renditions.
  This information might be useful to the client player that is playing this media
  asset.

- If a client player is configured with an audio preference (for example,
  Spanish) and that preference is not available, the player can use this
  information to select an audio.
- Or if the client player is not configured with any audio preference, the
  client player can use this information to select an audio.
  (If the preference that is configured in the client player is available, the
  player ignores this information and selects that preference.)

###### To determine defaults and auto-selection behavior

- For each audio rendition in the rendition group, choose the behavior from
  the following table. Each audio can have a different value.

Each row in the following table describes a different behavior.

| Value for a given audio rendition         | Client player behavior                                                                                                                                                                               | Representation in HLS Manifest                        |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Alternate Audio, Auto Select, Default     | The client player should select this audio rendition.<br>Only one audio renditions in the rendition group should be<br>set as the default, otherwise the client player might behave<br>unexpectedly. | `EXT-X-MEDIA` with `DEFAULT=YES`,<br>`AUTOSELECT=YES` |
| Alternate Audio, Auto Select, Not Default | The client player might select this audio rendition. Any<br>number of renditions in the rendition group can be set this<br>way.                                                                      | `EXT-X-MEDIA` with `DEFAULT=NO`,<br>`AUTOSELECT=YES`  |
| Alternate Audio, not Auto Select          | The client player should never select this audio<br>rendition. Any number of renditions in the rendition group<br>can be set this way.                                                               | `EXT-X-MEDIA` with `DEFAULT=NO`,<br>`AUTOSELECT=NO`   |
| Audio-Only Variant Stream                 | The client can play back this audio-only rendition<br>instead of video, in low-bandwidth scenarios.                                                                                                  | `EXT-X-STREAM-INF`                                    |

###### Example 1

In this example you want to set up the audio rendition group so that the
client player can auto-select any of the renditions. You also want a default
audio in the rendition group in case the client player is not set up with a
default.

- Set only one audio rendition to _Alternate
  Audio, Auto Select, Default_.
- Set every other audio rendition to _Alternate
  Audio, Auto Select, Not Default_.
- Optionally, if you have an audio rendition that plays when the
  bandwidth is so low that the video cannot be delivered, then set that
  audio rendition to _Audio-Only Variant
  Stream_.

###### Example 2

In this example you want to set up the audio rendition group so that the
client player can auto-select only specific renditions. You also want a default
audio in the rendition group in case the client player is not set up with a
default.

- Set only one audio rendition to _Alternate
  Audio, Auto Select, Default_.
- Set some of the other renditions to _Alternate
  Audio, Auto Select, Not Default_.
- Set some of the other renditions to _Alternate
  Audio, not Auto Select_.
- Optionally, if you have an audio rendition that plays when the
  bandwidth is so low that the video cannot be delivered, then set that
  audio rendition to _Audio-Only Variant
  Stream_.

###### Example 3

In this example you want to set up the audio rendition group so that the
client player can auto-select any audio rendition it chooses. You don't want a
default audio rendition in the rendition group, so the client player always
auto-selects audio.

- Set every audio rendition to _Alternate Audio,
  Auto Select, Not Default_.
- Optionally, if you have an audio rendition that plays when the
  bandwidth is so low that the video cannot be delivered, then set that
  audio rendition to _Audio-Only Variant
  Stream_.
