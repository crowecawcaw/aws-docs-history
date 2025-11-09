This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Getting Ready to Create HLS

Rendition Groups

## Step 1. Create a

Mapping

Identify the video, audio, audio rendition groups and captions you require. Review the
[Rules for Rendition Groups](hls-rendition-groups-rules.md "hls-rendition-groups-rules.md") to ensure you design an output that is valid. For
example:

- Video “high definition.”
- Video “low definition.”
- A rendition group named “AAC group” for AAC audio.
- A rendition group named “Dolby group” for Dolby Digital audio.
- Audio English AAC in “AAC group” rendition group.
- Audio English Dolby Digital in “Dolby group” rendition group.
- Audio French AAC in “AAC group” rendition group.
- Audio French Dolby Digital in “Dolby group” rendition group.
- Video “high definition” to be associated with both rendition groups.
- Video “low definition” to be associated with the “Dolby group” rendition group.
- Captions in English and French in WebVTT format, to be associated with both rendition
  groups.

![This illustration shows an example output group.](images/hls-rendition-groups-getting-ready-create-mapping.png)

## Step 2. Determine

Defaults and Auto-Selection Behavior

For each audio rendition group, decide which audio will be the default and how
auto-selection works for the non-defaults. Setting up this information is useful if:

- The user has specified an audio preference on the client player but that preference is
  not available, or
- If the user has not specified an audio preference.

(Obviously, if the user has specified a preference and that preference is available, the
client player will select that preference.)

Set the **Alternate Audio Track Selection** field. The
options for this field for each audio stream are:

- **Default Audio**: The client player _should_ select this stream. Only one stream in the rendition group
  should be set as the default; otherwise, the client player may behave unexpectedly.
- **Alternate Audio, Auto Select**: The client player
  _may_ select this stream. Any number of streams in the
  rendition group can be set this way. The client player typically selects a stream based on
  the chosen system language or some other rule.
- **Alternate Audio, not Auto Select**: The client player
  _should never_ select this stream. Any number of streams
  in the rendition group can be set this way.
  Set the **Alternate Audio Track Selection** as follows.

| Desired Result                                                                     | How to Set                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| There is a default. The player can auto-select any<br>of the other audios.         | • Set only one audio stream to “Default Audio.”<br>• Set every other audio stream to “Alternate Audio, Auto-Select.”                                                                                        |
| There is a default. The player cannot auto-select<br>any of the other audios.      | • Set only one audio stream to “Default Audio.”<br>• Set every other audio stream to “Alternate Audio, not Auto-Select.”                                                                                    |
| There is a default. There are specific audios that<br>the player can auto-select.  | • Set only one audio stream to “Default Audio.”<br>• Set some of the other audio streams to “Alternate Audio, Auto-Select.”<br>• Set some of the other audio streams to “Alternate Audio, not Auto-Select.” |
| There is no default. The player can auto-select any<br>audio it chooses.           | • Set every audio stream to “Alternate Audio, Auto-Select.”                                                                                                                                                 |
| There is no default. The player cannot auto-select<br>any audio.                   | • Set every audio stream to “Alternate Audio, not Auto-Select.”                                                                                                                                             |
| There is no default. There are specific audios that<br>the player can auto-select. | • Set some audio streams to “Alternate Audio, Auto-Select.”<br>• Set some audio streams to “Alternate Audio, not Auto-Select.”                                                                              |

Set the Audio Track Type field. The options for this field for each audio stream follow.

| Value                                     | Client Player Behavior                                                                                                                                                               | Representation in HLS Manifest               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| Alternate Audio, Auto Select, Default     | The client player should \*select<br>• this stream. Only<br>one stream in the rendition group should be set as the default; otherwise, the client<br>player may behave unexpectedly. | EXT-X-MEDIA with DEFAULT=YES, AUTOSELECT=YES |
| Alternate Audio, Auto Select, Not Default | The client player \*may<br>• select this stream. Any number of streams in the rendition group can be set this<br>way.                                                                | EXT-X-MEDIA with DEFAULT=NO, AUTOSELECT=YES  |
| Alternate Audio, not Auto Select          | The client player \*should<br>never<br>• select this stream. Any number of streams in the rendition group can be<br>set this way.                                                    | EXT-X-MEDIA with DEFAULT=NO, AUTOSELECT=NO   |
| Audio-Only Variant Stream                 | The client can play back this audio-only stream<br>instead of video in low-bandwidth scenarios.                                                                                      | EXT-X-STREAM-INF                             |

1. Set the **Alternate Audio Track Selection** as
   follows:

| Desired Result                                                                     | How to Set                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| There is a default. The player can auto-select<br>any of the other audios.         | • Set only one audio stream to “Alternate Audio, Auto-Select, Not Default,<br>Default.”<br>• Set every other audio stream to “Alternate Audio, Auto-Select, Not<br>Default.”                                                                                        |
| There is a default. The player cannot auto-select<br>any of the other audios.      | • Set only one audio stream to “Alternate Audio, Auto-Select, Not Default,<br>Default.”<br>• Set every other audio stream to “Alternate Audio, not Auto-Select.”                                                                                                    |
| There is a default. There are specific audios<br>that the player can auto-select.  | • Set only one audio stream to “Alternate Audio, Auto-Select, Not Default,<br>Default.”<br>• Set some of the other audio streams to “Alternate Audio, Auto-Select, Not<br>Default.”<br>• Set some of the other audio streams to “Alternate Audio, not Auto Select.” |
| There is no default. The player can auto-select<br>any audio it chooses.           | • Set every audio stream to “Alternate Audio, Auto-Select, Not Default.”                                                                                                                                                                                            |
| There is no default. The player cannot<br>auto-select any audio.                   | • Set every audio stream to “Alternate Audio, not Auto-Select.”                                                                                                                                                                                                     |
| There is no default. There are specific audios<br>that the player can auto-select. | • Set some audio streams to “Alternate Audio, Auto-Select, Not Default.”<br>• Set some audio streams to “Alternate Audio, not Auto-Select.”                                                                                                                         |

2. In addition, if you have an audio that is intended as the audio to play when the
   bandwidth is so low that the video cannot be delivered, then set that audio to “**Audio-Only Variant Stream**.”
