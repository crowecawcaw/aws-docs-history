

# Channel Types
<a name="channel-types"></a>

There are four channel types: `STANDARD`, `ADVANCED_SD`, `ADVANCED_HD`, and `BASIC`. When you create a channel, the default type is `STANDARD`.

There are two types of video processing, *transcoding* and *transmuxing*. This is determined by the channel type, whether the channel is configured for multitrack video input, and whether the broadcaster uses a multitrack-enabled client. (Multitrack video is configured with the `multitrackInputConfiguration` API property of the [Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html) data type.)
+ Video on `STANDARD` (without multitrack input) and `ADVANCED` channels is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Transcoding is the best option for broadcasters with limited first-mile internet connectivity and/or limited device capabilities (e.g., mobile phones instead of desktop PCs).
+ Video on `STANDARD` (with multitrack input enabled and the broadcaster using a multitrack-enabled client) and `BASIC` channels is transmuxed: Amazon IVS delivers the original input to viewers. Similar to transcoding, transmuxed multitrack input delivers viewers the best experience for their devices and network conditions.

All transcoded channels have *transcode* presets, which determine which renditions are produced. Think of these as ABR ladders. They allow you to trade off available download bandwidth and video quality, to optimize the viewing experience.
+ `STANDARD` channels have one, default transcode preset.
+ `ADVANCED` channels have two, selectable transcode presets:
  + *Constrained bandwidth delivery* uses a lower bitrate than `STANDARD` for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads).
  + *Higher bandwidth delivery* uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes). This is the default.

## STANDARD Channels
<a name="channel-types-standard"></a>

### Single-Track Video Input
<a name="channel-types-standard-without-multitrack"></a>

`STANDARD` channels are transcoded. The highest video resolution produced is full HD, 1080p. This is the default channel type.
+ **Transcode presets**: There is one, default transcode-preset ladder.
+ **Audio**: For renditions 360p and below, audio is transcoded. For other renditions: original audio is passed through.


| Input Resolution and Maximum Bitrate | Ladder Details | 
| --- | --- | 
| 1080p60 at 8.5 Mbps |  1.  Video: source passthrough, audio: source passthrough <br />2.  Video: 720p60 at 3.4 Mbps, audio: source passthrough <br />3.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />4.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />5.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 
| 1080p30 at 8.5 Mbps |  1.  Video: Source passthrough, audio: source passthrough <br />2.  Video: 720p30 at 2.4 Mbps, audio: source passthrough <br />3.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />4.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />5.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 
| Less than 1080p60 and greater than 720p60, at 8.5 Mbps |  1.  Video: source passthrough, audio: source passthrough <br />2.  Video: 720p60 at 3.4 Mbps, audio: source passthrough <br />3.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />4.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />5.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 
| Less than 1080p30 and greater than 720p30, at 8.5 Mbps |  1.  Video: source passthrough, audio: source passthrough <br />2.  Video: 720p30 at 2.4 Mbps, audio: source passthrough <br />3.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />4.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />5.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 
| 720p60 at 8.5 Mbps |  1.  Video: 720p60 at 3.4 Mbps, audio: source passthrough <br />2.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />3.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 
| 720p30 at 8.5 Mbps |  1.  Video: 720p30 at 2.4 Mbps, audio: source passthrough <br />2.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />3.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 
| Less than 720p30/60 and greater than or equal to 480p30/60, at 8.5 Mbps |  1.  Video: 480p30 at 1.4 Mbps, audio: source passthrough <br />2.  Video: 360p30 at 0.63 Mbps, audio: 64 kbps <br />3.  Video: 160p30 at 0.23 Mbps, audio: 48 kbps   | 

### Multitrack Video Input
<a name="channel-types-standard-with-multitrack"></a>

`STANDARD` channels are transmuxed when the input is multitrack video. The highest video resolution produced is limited by the `multitrackInputConfiguration.maximumResolution` property. The specific renditions are dynamic depending on the [broadcaster’s system and environmental requirements](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multitrack-video-setup.html#multitrack-video-setup-broadcaster-system).

For all video renditions, audio is source passthrough.

## ADVANCED-HD Channels
<a name="channel-types-advanced-hd"></a>

`ADVANCED_HD` channels are transcoded. The highest video resolution produced is HD, 720p.
+ **Transcode presets**: There are two, selectable transcode-preset ladders.
+ **Audio**: Audio is transcoded.


| Input Resolution and Maximum Bitrate | Ladder Details | 
| --- | --- | 
| 720p60 up to 1080p60, at 8.5 Mbps | Transcode preset: higher bandwidth delivery (default):1.  Video: 720p60 at 3 Mbps, audio: 128 kbps <br />2.  Video: 480p30 at 1.3 Mbps, audio: 128 kbps <br />3.  Video: 360p30 at 0.7 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.27 Mbps, audio: 48 kbps <br />5.  Audio-only at 64 kbps <br />Transcode preset: constrained bandwidth delivery:1.  Video: 720p60 at 2.2 Mbps, audio: 128 kbps <br />2.  Video: 480p30 at 0.8 Mbps, audio: 128 kbps <br />3.  Video: 360p30 at 0.4 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.22 Mbps, audio: 48 kbps <br />5.  Audio-only at 64 kbps  | 
| 720p30 up to 1080p30, at 8.5 Mbps | Transcode preset: higher bandwidth delivery (default):1.  Video: 720p30 at 2.3 Mbps, audio: 128 kbps <br />2.  Video: 480p30 at 1.3 Mbps, audio: 128 kbps <br />3.  Video: 360p30 at 0.7 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.27 Mbps, audio: 48 kbps <br />5.  Audio-only at 64 kbps <br />Transcode preset: constrained bandwidth delivery:1.  Video: 720p30 at 1.9 Mbps, audio: 128 kbps <br />2.  Video: 480p30 at 0.8 Mbps, audio: 128 kbps <br />3.  Video: 360p30 at 0.4 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.22 Mbps, audio: 48 kbps <br />5.  Audio-only at 64 kbps  | 
| Less than 720p30/60 and greater than 480p30/60, at 8.5 Mbps | Transcode preset: higher bandwidth delivery (default):1.  Video: Source transcoded at 2.3 Mbps, audio: 128 kbps <br />2.  Video: 480p30 at 1.3 Mbps, audio: 128 kbps <br />3.  Video: 360p30 at 0.7 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.27 Mbps, audio: 48 kbps <br />5.  Audio-only at 64 kbps <br />Transcode preset: constrained bandwidth delivery:1.  Video: Source transcoded at 1.9 Mbps, audio: 128 kbps <br />2.  Video: 480p30 at 0.8 Mbps, audio: 128 kbps <br />3.  Video: 360p30 at 0.4 Mbps, audio: 64 kbps <br />4.  Video: 160p30 at 0.22 Mbps, audio: 48 kbps <br />5.  Audio-only at 64 kbps  | 
| 480p30/60 at 8.5 Mbps | Transcode preset: higher bandwidth delivery (default):1.  Video: 480p30 at 1.3 Mbps, audio: 128 kbps <br />2.  Video: 360p30 at 0.7 Mbps, audio: 64 kbps <br />3.  Video: 160p30 at 0.27 Mbps, audio: 48 kbps <br />4.  Audio-only at 64 kbps <br />Transcode preset: constrained bandwidth delivery:1.  Video: 480p30 at 0.8 Mbps, audio: 128 kbps <br />2.  Video: 360p30 at 0.4 Mbps, audio: 64 kbps <br />3.  Video: 160p30 at 0.22 Mbps, audio: 48 kbps <br />4.  Audio-only at 64 kbps  | 

## ADVANCED-SD Channels
<a name="channel-types-advanced-sd"></a>

`ADVANCED_SD` channels are transcoded. Available renditions are capped at input quality, with no up-conversion.
+ **Transcode presets**: There are two, selectable transcode-preset ladders.
+ **Audio**: Audio is transcoded.


| Input Resolution and Maximum Bitrate | Ladder Details | 
| --- | --- | 
| 480p30/60 up to 1080p30/60, at 8.5 Mbps | Transcode preset: higher bandwidth delivery (default):1.  Video: 480p30 at 1.3 Mbps, audio: 128 kbps <br />2.  Video: 360p30 at 0.7 Mbps, audio: 64 kbps <br />3.  Video: 160p30 at 0.27 Mbps, audio: 48 kbps <br />4.  Audio-only at 64 kbps <br />Transcode preset: constrained bandwidth delivery:1.  Video: 480p30 at 0.8 Mbps, audio: 128 kbps <br />2.  Video: 360p30 at 0.4 Mbps, audio: 64 kbps <br />3.  Video: 160p30 at 0.22 Mbps, audio: 48 kbps <br />4.  Audio-only at 64 kbps  | 

## BASIC Channels
<a name="channel-types-basic"></a>

`BASIC` channels are transmuxed. A single rendition is produced.
+ **Transcode presets**: NA
+ **Audio**: Source audio is passed through.


| Input Resolution and Maximum Bitrate | Ladder Details | 
| --- | --- | 
| Greater than 480p30/60 and less than or equal to 1080p30/60, at 3.5 Mbps | Source encoding parameters (no ladder) | 
| 480p30/60 at 1.5 Mbps | Source encoding parameters (no ladder) | 