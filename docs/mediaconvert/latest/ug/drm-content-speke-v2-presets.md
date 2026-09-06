

# SPEKE v2.0 presets
<a name="drm-content-speke-v2-presets"></a>

SPEKE Version 2.0 supports the use of multiple, distinct encryption keys for audio and video tracks. MediaConvert uses **presets** to configure the encryption. The MediaConvert API defines these presets. The presets map encryption keys to specific audio or video tracks, based on the number of channels for audio tracks, and based on the video resolution for video tracks. MediaConvert uses specific combinations of audio and video encryption presets to support three different encryption scenarios:
+ [Scenario 1: Unencrypted tracks and encrypted tracks](#drm-content-speke-v2-presets-unencrypted-and-encrypted-tracks)
+ [Scenario 2: Single encryption key for all audio and video tracks](#drm-content-speke-v2-presets-single-encryption-key-for-all-tracks)
+ [Scenario 3: Multiple encryption keys for audio and video tracks](#drm-content-speke-v2-presets-multiple-encryption-keys-for-audio-and-video-tracks)

## Scenario 1: Unencrypted tracks and encrypted tracks
<a name="drm-content-speke-v2-presets-unencrypted-and-encrypted-tracks"></a>

You can choose *not* to encrypt the audio or the video tracks by selecting the **UNENCRYPTED** preset in the **Video encryption preset** or the **Audio encryption preset** menus. You can’t select **UNENCRYPTED** for both audio and video presets, because doing so would mean that you don’t intend to encrypt any of the tracks at all. Also, you can’t combine **UNENCRYPTED** and **SHARED** presets for audio and video, because **SHARED** is a special preset. For more information, see [Scenario 2: Single encryption key for all audio and video tracks](#drm-content-speke-v2-presets-single-encryption-key-for-all-tracks). 

The following list describes valid combinations of **UNENCRYPTED** presets:
+ **UNENCRYPTED** for audio tracks, and any video preset with a name that starts with `PRESET_VIDEO_`
+ **UNENCRYPTED** for video tracks, and any audio preset with a name that starts with `PRESET_AUDIO_`

## Scenario 2: Single encryption key for all audio and video tracks
<a name="drm-content-speke-v2-presets-single-encryption-key-for-all-tracks"></a>

The SPEKE Version 2.0 **SHARED** preset uses a single encryption key for all audio and video tracks, as in SPEKE Version 1.0. When you select the **SHARED** preset, select it for both audio and video encryption.

## Scenario 3: Multiple encryption keys for audio and video tracks
<a name="drm-content-speke-v2-presets-multiple-encryption-keys-for-audio-and-video-tracks"></a>

When you use a preset with a name that starts with `PRESET_VIDEO_` or `PRESET_AUDIO_`, MediaConvert encrypts the audio tracks and video tracks with the number of encryption keys that the specific preset defines. The following tables show how many keys MediaConvert requests from the key server and how those keys map to tracks. If no track matches the criteria for a particular key, MediaConvert does not use that key to encrypt any track.

MediaConvert encrypts I-frame only trickplay tracks with the key corresponding to their resolution. 

In the following table, the **Key name** value is the value of the `ContentKeyUsageRule@IntendedTrackType` attribute that MediaConvert uses in the CPIX document. This is sent to the SPEKE server for a specific content key.


**Video encryption presets**  

<table>
<thead>
  <tr><th>Preset name</th><th>Number of keys</th><th>Key name</th><th>Minimum resolution</th><th>Maximum resolution</th></tr>
</thead>
<tbody>
  <tr><td><b>PRESET_VIDEO_1</b></td><td>1</td><td>VIDEO</td><td colspan="2">No minimum or maximum resolution. MediaConvert encrypts all tracks with the same key.</td></tr>
  <tr><td rowspan="2"><b>PRESET_VIDEO_2</b></td><td rowspan="2">2</td><td>SD</td><td>No minimum</td><td>&lt;= 1024x576</td></tr>
  <tr><td>HD</td><td>&gt; 1024x576</td><td>No maximum</td></tr>
  <tr><td rowspan="3"><b>PRESET_VIDEO_3</b></td><td rowspan="3">3</td><td>SD</td><td>No minimum</td><td>&lt;= 1024x576</td></tr>
  <tr><td>HD</td><td>&gt; 1024x576</td><td>&lt;= 1920x1080</td></tr>
  <tr><td>UHD</td><td>&gt; 1920x1080</td><td>No maximum</td></tr>
  <tr><td rowspan="4"><b>PRESET_VIDEO_4</b></td><td rowspan="4">4</td><td>SD</td><td>No minimum</td><td>&lt;= 1024x576</td></tr>
  <tr><td>HD</td><td>&gt; 1024x576</td><td>&lt;= 1920x1080</td></tr>
  <tr><td>UHD1</td><td>&gt; 1920x1080</td><td>&lt;= 4096x2160</td></tr>
  <tr><td>UHD2</td><td>&gt; 4096x2160</td><td>No maximum</td></tr>
  <tr><td rowspan="5"><b>PRESET_VIDEO_5</b></td><td rowspan="5">5</td><td>SD</td><td>No minimum</td><td>&lt;= 1024x576</td></tr>
  <tr><td>HD1</td><td>&gt; 1024x576</td><td>&lt;= 1280x720</td></tr>
  <tr><td>HD2</td><td>&gt; 1280x720</td><td>&lt;= 1920x1080</td></tr>
  <tr><td>UHD1</td><td>&gt; 1920x1080</td><td>&lt;= 4096x2160</td></tr>
  <tr><td>UHD2</td><td>&gt; 4096x2160</td><td>No maximum</td></tr>
  <tr><td rowspan="4"><b>PRESET_VIDEO_6</b></td><td rowspan="4">4</td><td>SD</td><td>No minimum</td><td>&lt;= 1024x576</td></tr>
  <tr><td>HD1</td><td>&gt; 1024x576</td><td>&lt;= 1280x720</td></tr>
  <tr><td>HD2</td><td>&gt; 1280x720</td><td>&lt;= 1920x1080</td></tr>
  <tr><td>UHD</td><td>&gt; 1920x1080</td><td>No maximum</td></tr>
  <tr><td rowspan="3"><b>PRESET_VIDEO_7</b></td><td rowspan="3">3</td><td>SD+HD1</td><td>No minimum</td><td>&lt;= 1280x720</td></tr>
  <tr><td>HD2</td><td>&gt; 1280x720</td><td>&lt;= 1920x1080</td></tr>
  <tr><td>UHD</td><td>&gt; 1920x1080</td><td>No maximum</td></tr>
  <tr><td rowspan="4"><b>PRESET_VIDEO_8</b></td><td rowspan="4">4</td><td>SD+HD1</td><td>No minimum</td><td>&lt;= 1280x720</td></tr>
  <tr><td>HD2</td><td>&gt; 1280x720</td><td>&lt;= 1920x1080</td></tr>
  <tr><td>UHD1</td><td>&gt; 1920x1080</td><td>&lt;= 4096x2160</td></tr>
  <tr><td>UHD2</td><td>&gt; 4096x2160</td><td>No maximum</td></tr>
  <tr><td><b>SHARED</b></td><td>1</td><td>ALL</td><td colspan="2">No minimum or maximum resolution. MediaConvert encrypts all video and audio tracks with the same key.</td></tr>
  <tr><td><b>UNENCRYPTED</b></td><td>0</td><td><i>N/A</i></td><td colspan="2">MediaConvert does not encrypt any video track.</td></tr>
</tbody>
</table>


In the following table, the **Key name** value is the value of the `ContentKeyUsageRule@IntendedTrackType` attribute that MediaConvert uses in the CPIX document. This is sent to the SPEKE server for a specific content key.


**Audio encryption presets**  

<table>
<thead>
  <tr><th>Preset name</th><th>Number of keys</th><th>Key name</th><th>Minimum number of channels</th><th>Maximum number of channels</th></tr>
</thead>
<tbody>
  <tr><td><b>PRESET_AUDIO_1</b></td><td>1</td><td>AUDIO</td><td colspan="2">No minimum or maximum number of channels. MediaConvert encrypts all audio and video tracks with the same key.</td></tr>
  <tr><td rowspan="2"><b>PRESET_AUDIO_2</b></td><td rowspan="2">2</td><td>STEREO_AUDIO</td><td>No minimum</td><td>2</td></tr>
  <tr><td>MULTICHANNEL_AUDIO</td><td>&gt; 2</td><td>No maximum</td></tr>
  <tr><td rowspan="3"><b>PRESET_AUDIO_3</b></td><td rowspan="3">3</td><td>STEREO_AUDIO</td><td>No minimum</td><td>2</td></tr>
  <tr><td>MULTICHANNEL_AUDIO_3_6</td><td>&gt; 2</td><td>&lt;= 6</td></tr>
  <tr><td>MULTICHANNEL_AUDIO_7</td><td>&gt; 6</td><td>No maximum</td></tr>
  <tr><td><b>SHARED</b></td><td>1</td><td>ALL</td><td colspan="2">No minimum or maximum number of channels. MediaConvert encrypts all audio and video tracks with the same key.</td></tr>
  <tr><td><b>UNENCRYPTED</b></td><td>0</td><td><i>N/A</i></td><td colspan="2">MediaConvert does not encrypt any audio track.</td></tr>
</tbody>
</table>


Now you know how MediaConvert supports SPEKE Version 2.0 presets for unencrypted tracks and encrypted tracks. With these presets, you can use a single encryption key for all audio and video tracks, and multiple encryption keys for audio and video tracks. 