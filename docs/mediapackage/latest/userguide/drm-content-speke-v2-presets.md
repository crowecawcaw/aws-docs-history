# Encryption presets in AWS Elemental MediaPackage

SPEKE Version 2.0 supports the use of multiple, distinct encryption keys for audio and
video tracks. MediaPackage uses **presets** to configure the
encryption. The MediaPackage API defines these presets, and they appear in the MediaPackage
console in the **Video encryption preset** and **Audio encryption
preset** menus of the **Package Encryption endpoints
configuration** section. The presets map encryption keys to specific audio or video
tracks, based on the number of channels for audio tracks, and based on the video resolution
for video tracks. MediaPackage uses specific combinations of audio and video encryption
presets to support three different encryption scenarios:

- [Scenario 1:
  Unencrypted tracks and encrypted tracks](#drm-content-speke-v2-presets-unencrypted-and-encrypted-tracks "#drm-content-speke-v2-presets-unencrypted-and-encrypted-tracks")
- [Scenario
  2: Single encryption key for all audio and video tracks](#drm-content-speke-v2-presets-single-encryption-key-for-all-tracks "#drm-content-speke-v2-presets-single-encryption-key-for-all-tracks")
- [Scenario 3: Multiple encryption keys for audio and video tracks](#drm-content-speke-v2-presets-multiple-encryption-keys-for-audio-and-video-tracks "#drm-content-speke-v2-presets-multiple-encryption-keys-for-audio-and-video-tracks")

## Scenario 1:

Unencrypted tracks and encrypted tracks

You can choose _not_ to encrypt the audio or the video tracks by
selecting the **UNENCRYPTED** preset in the **Video encryption
preset** or the **Audio encryption preset** menus. You can’t
select **UNENCRYPTED** for both audio and video presets, because doing so
would mean that you don’t intend to encrypt any of the tracks at all. Also, you can’t
combine **UNENCRYPTED** and **SHARED** presets for audio
and video, because **SHARED** is a special preset. For more information,
see [Scenario
2: Single encryption key for all audio and video tracks](#drm-content-speke-v2-presets-single-encryption-key-for-all-tracks "#drm-content-speke-v2-presets-single-encryption-key-for-all-tracks").

The following list describes valid combinations of **UNENCRYPTED**
presets:

- **UNENCRYPTED** for audio tracks, and any video preset with a name
  that starts with `PRESET-VIDEO-`
- **UNENCRYPTED** for video tracks, and any audio preset with a name
  that starts with `PRESET-AUDIO-`

## Scenario

2: Single encryption key for all audio and video tracks

The SPEKE Version 2.0 **SHARED** preset uses a single encryption key
for all audio and video tracks, as in SPEKE Version 1.0. When you select the
**SHARED** preset, select it for both audio and video encryption.

## Scenario 3: Multiple encryption keys for audio and video tracks

When you use a preset with a name that starts with `PRESET-VIDEO-` or
`PRESET-AUDIO-`, MediaPackage encrypts the audio tracks and video tracks with
the number of encryption keys that the specific preset defines. The following tables show
how many keys MediaPackage requests from the key server and how those keys map to tracks.
If no track matches the criteria for a particular key, MediaPackage does not use that key
to encrypt any track.

MediaPackage encrypts I-frame only trickplay tracks with the key corresponding to their
resolution.

In the following table, the **Key name** value is the value
of the `ContentKeyUsageRule@IntendedTrackType` attribute that MediaPackage uses
in the CPIX document. This is sent to the SPEKE server for a specific content key.

| Video encryption presets | Preset name | Number of keys | Key name                                                                                                      | Minimum resolution                                                                                                                                                                                                                                      | Maximum resolution |
| ------------------------ | ----------- | -------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | -------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PRESET-VIDEO-1**       | 1           | VIDEO          | No minimum or maximum resolution. MediaPackage encrypts all tracks with the same key.                         |
| **PRESET-VIDEO-2**       | 2           | SD             | No minimum                                                                                                    | <= 1024x576                                                                                                                                                                                                                                             |
| HD                       | > 1024x576  | No maximum     |
| **PRESET-VIDEO-3**       | 3           | SD             | No minimum                                                                                                    | <= 1024x576                                                                                                                                                                                                                                             |
| HD                       | > 1024x576  | <= 1920x1080   |                                                                                                               | UHD                                                                                                                                                                                                                                                     | > 1920x1080        | No maximum     |
| **PRESET-VIDEO-4**       | 4           | SD             | No minimum                                                                                                    | <= 1024x576                                                                                                                                                                                                                                             |
| HD                       | > 1024x576  | <= 1920x1080   |                                                                                                               | UHD1                                                                                                                                                                                                                                                    | > 1920x1080        | <= 4096x2160   |
| UHD2                     | > 4096x2160 | No maximum     |
| **PRESET-VIDEO-5**       | 5           | SD             | No minimum                                                                                                    | <= 1024x576                                                                                                                                                                                                                                             |
| HD1                      | > 1024x576  | <= 1280x720    |                                                                                                               | HD2                                                                                                                                                                                                                                                     | > 1280x720         | <= 1920x1080   |
| UHD1                     | > 1920x1080 | <= 4096x2160   |                                                                                                               | UHD2                                                                                                                                                                                                                                                    | > 4096x2160        | No maximum     |
| **PRESET-VIDEO-6**       | 4           | SD             | No minimum                                                                                                    | <= 1024x576                                                                                                                                                                                                                                             |
| HD1                      | > 1024x576  | <= 1280x720    |                                                                                                               | HD2                                                                                                                                                                                                                                                     | > 1280x720         | <= 1920x1080   |
| UHD                      | > 1920x1080 | No maximum     |
| **PRESET-VIDEO-7**       | 3           | SD+HD1         | No minimum                                                                                                    | <= 1280x720                                                                                                                                                                                                                                             |
| HD2                      | > 1280x720  | <= 1920x1080   |                                                                                                               | UHD                                                                                                                                                                                                                                                     | > 1920x1080        | No maximum     |
| **PRESET-VIDEO-8**       | 4           | SD+HD1         | No minimum                                                                                                    | <= 1280x720                                                                                                                                                                                                                                             |
| HD2                      | > 1280x720  | <= 1920x1080   |                                                                                                               | UHD1                                                                                                                                                                                                                                                    | > 1920x1080        | <= 4096x2160   |
| UHD2                     | > 4096x2160 | No maximum     |                                                                                                               | **SHARED**                                                                                                                                                                                                                                              | 1                  | ALL            | No minimum or maximum resolution. MediaPackage encrypts all video and audio tracks with the same key. |
| **UNENCRYPTED**          | 0           | _N/A_          | MediaPackage does not encrypt any video track.                                                                | In the following table, the **Key name** value is the value of the `ContentKeyUsageRule@IntendedTrackType` attribute that MediaPackage uses in the CPIX document. This is sent to the SPEKE server for a specific content key. Audio encryption presets | Preset name        | Number of keys | Key name                                                                                              | Minimum number of channels                     | Maximum number of channels                                                                                                                                                                                                                                     |
| ---                      | ---         | ---            | ---                                                                                                           | ---                                                                                                                                                                                                                                                     |
| **PRESET-AUDIO-1**       | 1           | AUDIO          | No minimum or maximum number of channels. MediaPackage encrypts all audio and video tracks with the same key. |
| **PRESET-AUDIO-2**       | 2           | STEREO_AUDIO   | No minimum                                                                                                    | 2                                                                                                                                                                                                                                                       |
| MULTICHANNEL_AUDIO       | > 2         | No maximum     |
| **PRESET-AUDIO-3**       | 3           | STEREO_AUDIO   | No minimum                                                                                                    | 2                                                                                                                                                                                                                                                       |
| MULTICHANNEL_AUDIO_3_6   | > 2         | <= 6           |                                                                                                               | MULTICHANNEL_AUDIO_7                                                                                                                                                                                                                                    | > 6                | No maximum     |
| **SHARED**               | 1           | ALL            | No minimum or maximum number of channels. MediaPackage encrypts all audio and video tracks with the same key. |                                                                                                                                                                                                                                                         | **UNENCRYPTED**    | 0              | _N/A_                                                                                                 | MediaPackage does not encrypt any audio track. | Now you know how MediaPackage supports SPEKE Version 2.0 presets for unencrypted tracks and encrypted tracks. With these presets, you can use a single encryption key for all audio and video tracks, and multiple encryption keys for audio and video tracks. |
