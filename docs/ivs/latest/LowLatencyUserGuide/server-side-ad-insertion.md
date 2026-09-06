

# Server-Side Ad Insertion (SSAI)
<a name="server-side-ad-insertion"></a>

Amazon IVS server-side ad insertion (SSAI) enables you to monetize your streams with video ads. IVS SSAI integrates with AWS Elemental MediaTailor, giving you access to capabilities such as ad decisioning, audience targeting, and personalization. IVS supports two types of ad breaks:
+ **Mid-roll** — Manually triggered during a live stream using the `InsertAdBreak` API.
+ **Post-roll** — Automatically inserted at the end of a stream.

IVS stitches ads directly into the video stream. This provides a seamless viewing experience and avoids complex client-side logic.

For information about costs associated with SSAI, see [IVS Costs](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/costs.html).

## Getting Started with SSAI
<a name="ssai-getting-started-with-ssai"></a>

This tutorial helps you get started with Amazon IVS server-side ad insertion (SSAI). At the end of this tutorial, you will have an IVS channel configured for server-side ad insertion, and you will know how to insert ad breaks into your live stream. IVS SSAI integrates with AWS Elemental MediaTailor to handle ad decisioning.

### Step 1: Create an IVS Channel
<a name="ssai-getting-started-with-ssai-step-1"></a>

Create an IVS channel. You need the channel's playback URL to configure MediaTailor in the next step. After creating your channel, save the following values:
+ **Channel ARN** — You need this to update the channel later.
+ **Playback URL prefix** — Extract the URL prefix from the playback URL (everything before /api/). For example, if your playback URL is:
  + https://c17b3fb37fc9.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.ABcdef12ghIJ.m3u8

  the prefix is:
  + https://c17b3fb37fc9.us-west-2.playback.live-video.net/
+ **Container format** — Must be set to MPEG Transport Stream (TS).

### Step 2: Create a MediaTailor Playback Configuration
<a name="ssai-getting-started-with-ssai-step-2"></a>

Create an AWS Elemental MediaTailor playback configuration. This configuration connects your ad decision server to IVS and enables ad insertion for your streams.

The playback configuration uses the playback URL prefix, which is common across all IVS channels in your account and region. This means you can use a single MediaTailor playback configuration with multiple IVS channels.

See [Creating a MediaTailor Playback Configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-create.html) in the *AWS Elemental MediaTailor User Guide* for instructions. When creating the configuration, the following settings are required for IVS SSAI:


| Setting | Location | Value | 
| --- | --- | --- | 
| Ad decision server URL | Required Settings | URL of the ad decision server | 
| Content source | Required Settings | URL prefix of your IVS playback URL; e.g., https://c17b3fb37fc9.us-west-2.playback.live-video.net/ | 
| Insertion mode | Personalization Details | PLAYER\_SELECT | 

**Important**  
Specify the content source using only the prefix of your channel's playback URL (ending in `live-video.net/`), not the full URL. If the format is incorrect, creating an ad configuration in the next step fails with a validation error.

### Step 3: Create an IVS Ad Configuration
<a name="ssai-getting-started-with-ssai-step-3"></a>

An ad configuration links your IVS resources to your MediaTailor playback configuration. You can use a MediaTailor playback configuration created in any IVS home region with an ad configuration in any other IVS home region. IVS home regions include `us-west-2`, `us-east-1`, `eu-west-1`, `eu-central-1`, `ap-northeast-1`, `ap-northeast-2`, and `ap-south-1`.

You can reuse a single ad configuration across multiple channels. An ad configuration supports up to 3 MediaTailor playback configurations. The first configuration in the list is used by default. To select a different one per viewing session, specify the `aws:ads-playback-config-name` claim in a [playback authorization token](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html).

To create an ad configuration (AWS CLI):

```
aws ivs create-ad-configuration \
	      --name "my-ad-config" \
	      --media-tailor-playback-configurations playbackConfigurationArn="arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/my-mediatailor-config" \
              --post-roll-configuration enabled=true,durationSeconds=30
```

The `--post-roll-configuration` parameter is optional. If omitted, post-roll configuration defaults to disabled (`enabled`: false) with a duration of 15 seconds (`durationSeconds`: 15). If provided, both `enabled` and `durationSeconds` are required. If omitted, you can enable it later using the [UpdateAdConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateAdConfiguration.html) API.

For [UpdateAdConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateAdConfiguration.html): if `--post-roll-configuration` is not included in the request, the existing post-roll configuration is not modified. If included, both fields are required.

Save the arn value from the response. You need it in the next step.

### Step 4: Update the Channel with the Ad Configuration
<a name="ssai-getting-started-with-ssai-step-4"></a>

Update your IVS channel to associate it with the ad configuration you created. To update the channel (AWS CLI):

```
aws ivs update-channel --arn "arn:aws:ivs:us-west-2:123456789012:channel/ABcdef12ghIJ" --ad-configuration-arn "arn:aws:ivs:us-west-2:123456789012:ad-configuration/ABcdef12ghIJ"
```

### Step 5: Start Streaming
<a name="ssai-getting-started-with-ssai-step-5"></a>

Use the ingest endpoint and stream key from your channel to start streaming.

### Step 6: Insert Ad Break
<a name="ssai-getting-started-with-ssai-step-6"></a>

While your stream is live, call the InsertAdBreak operation to insert an ad break. Specify the channel ARN and the duration (in seconds) for the ad break. This step applies to **mid-roll** ad breaks only. Post-roll ad breaks are triggered automatically and do not require calling `InsertAdBreak`.

To insert an ad break (AWS CLI):

```
aws ivs insert-ad-break --channel-arn "arn:aws:ivs:us-west-2:123456789012:channel/ABcdef12ghIJ" --duration-seconds 30
```

Upon successful return of InsertAdBreak, you can receive an EventBridge event (IVS Ad Break State Change) that contains a timestamp indicating the expected time the ad break will be inserted into viewer playlists. This is the time when the broadcaster can reasonably expect ads to begin replacing content. If an ad cannot be filled (for example, if your ad decision server does not return an ad or ads need to be transcoded by MediaTailor), source content is shown instead.

**Important**  
You cannot insert additional ad breaks while an existing ad break is still in progress. Subsequent calls to InsertAdBreak will return a 409 `ConflictException` until the current ad break concludes.

#### EventBridge Integration
<a name="ssai-getting-started-with-ssai-step-6-eventbridge-integration"></a>

With SSAI, an IVS Ad Break State Change event (called Ad Break Inserted) is added, with the following fields:


| Field | Description | 
| --- | --- | 
| event\_name | The name of the event being emitted. | 
| channel\_name | The name of the channel that is triggered by the InsertAdBreak API request. | 
| stream\_id | The ID of the live stream to the channel triggered by the InsertAdBreak API request. | 
| ad\_break\_id | The unique ID associated with the ad break, which corresponds to the ad break ID in the response from the initial InsertAdBreak request. | 
| duration\_seconds | The value in seconds that was included on the InsertAdBreak request and specified by the customer. | 
| target\_start\_time | The estimated timestamp for the live stream of when the ad break is inserted into the playlist.  | 

### Player SDK Events
<a name="ssai-getting-started-with-ssai-player-sdk-events"></a>

Across platforms, the Player SDK surfaces events when an ad break is played, notifying when an ad starts, progresses, and stops. Here is a high-level summary of the available events and timing:


| Event | Payload | Trigger | 
| --- | --- | --- | 
| Ad break started | AdBreak | First segment of ad break | 
| Ad creative started | AdCreative | First segment of each creative | 
| Ad time update | AdTimeUpdate | Every second during ad playback | 
| Ad creative ended | AdCreative | Last segment of each creative | 
| Ad break ended | AdBreak | First content segment after break | 

For the specific event and payload names for each platform, see the Player SDK documentation:
+ Web: See the PlayerEventType enumeration at [https://aws.github.io/amazon-ivs-player-docs/latest/web/](https://aws.github.io/amazon-ivs-player-docs/latest/web/)
+ Android: See the Player.Listener class at [https://aws.github.io/amazon-ivs-player-docs/latest/android/](https://aws.github.io/amazon-ivs-player-docs/latest/android/)
+ IOS: See the IVSPlayerDelegate protocol at [https://aws.github.io/amazon-ivs-player-docs/latest/ios/](https://aws.github.io/amazon-ivs-player-docs/latest/ios/)

Below is an example of using ad events in the Web SDK to create a simple ad countdown UI component during an ad break:

```
// State 
let podLength = 0;  
let podIndex = 0; 
let remainingSeconds = 0; 
 
// Fired every second during the ad break 
player.addEventListener(PlayerEventType.AD_TIME_UPDATE, (payload) => { 
    podLength = payload.podLength; 
    podIndex = payload.podIndex; 
    remainingSeconds = Math.round(payload.creativeDuration - payload.creativeElapsed); 
    const text = `Ad ${podIndex} of ${podLength} · ${remainingSeconds}s remaining` 
    // Ad 1 of 2 · 20s remaining 
    console.log('Ad countdown text', text); 
    UpdateAdOverlay(text); 
}); 

// Fired when the ad break ends  
player.addEventListener(PlayerEventType.AD_BREAK_ENDED, (payload) => { 
    hideAdOverlay(); 
});
```

### Ad Markers in Recorded Content
<a name="ssai-getting-started-with-ssai-ad-markers"></a>

When a live stream is recorded using auto-record to Amazon S3, IVS generates and writes a VOD playlist to S3 that includes SCTE-35 ad markers at the positions where ads were triggered during the live stream. See [SSAI Playlist Reference](#ssai-playlist-reference) for details.

### Viewer Experience
<a name="ssai-getting-started-with-ssai-viewer-experience"></a>

By default, MediaTailor fills and serves ads to all viewers when you insert an ad break. If you are using playback authorization tokens for your streams, you can opt viewers out of receiving ads by adding the claim `"aws:ads-opt-out": true` to your playback authorization JWT token.

When viewers begin streaming partway through an ad break, IVS rounds up the ad break duration to the nearest quartile. For example, a viewer who joins with 35 seconds remaining in a 60-second ad break will experience a 45-second ad break.

When updating your MediaTailor playback configuration or adding new ads, viewers might not see ads the first time you request an ad break because MediaTailor must first transcode the ads. After a few minutes, subsequent calls to InsertAdBreak will result in viewers seeing ads. MediaTailor’s transcode logs record these transcodes.

### Viewer Tracking Parameters
<a name="ssai-getting-started-with-ssai-viewer-tracking-parameters"></a>

When configuring an Ad Decisioning Server (ADS) in your Elemental MediaTailor PlaybackConfiguration, you can pass parameters to the ADS using templates (see [MediaTailor passing parameters to ADS](https://docs.aws.amazon.com/mediatailor/latest/ug/passing-paramters-to-the-ads.html)). With IVS SSAI, you can pass parameters for each viewer using the playback authorization token for that user, by adding a claim with the following format:

```
"aws:ads-player-params": { 
   "key1": "value1", 
   "key2": "value2" 
}
```

These parameters are passed to Elemental MediaTailor to be filled as the `[player_params.key1]` and `[player_params.key2]` template variables. Keys that you put in this list are always namespaced as `player_params` template parameters.

The total payload size for all keys and values combined is limited to 1000 bytes.

### Reporting Mode
<a name="ssai-getting-started-with-ssai-reporting-mode"></a>

As a viewer watches an ad, the client or server can send beacons indicating playback progress for each ad creative. By default, MediaTailor handles beaconing on the server side. You can control the reporting mode by adding the following claim to the playback authorization token:

```
"aws:ads-reporting-mode": "CLIENT" | "SERVER"
```

The default value is `SERVER`. When set to `SERVER`, MediaTailor sends beacons on the server side. When set to `CLIENT`, server-side beaconing is disabled and tracking data is provided in the `metadata.trackingData` field of the IVS Player SDK adBreakStarted event. The IVS player SDK does not call beacon URLs.

### Known Issues
<a name="ssai-getting-started-with-ssai-known-issues"></a>
+ IVS ads do not work if the IVS channel `containerFormat` is set to `FRAGMENTED_MP4`. Calls to UpdateChannel and CreateChannel will return a validation error if the FMP4 container format is used with an ad configuration.
+ During ad playback, switching between adaptive bitrate mode and manual quality selection can cause the player to experience freezing and buffering issues.
+ For streams longer than 12 hours that have encountered starvation, it is possible for the program date time to drift, causing viewers to not be served ads. The workaround is for the broadcaster to restart the stream.

## SSAI Playlist Reference
<a name="ssai-playlist-reference"></a>

### Live Variant Playlist with SSAI
<a name="ssai-playlist-reference-live"></a>

When an ad is stitched into the stream, IVS inserts the tags documented below, before the ad segments.

**1. Stitched Ad Declaration**

```
#EXT-X-DATERANGE:ID="stitched-ad-1765566299-20000000000",CLASS="live-video-net-stitched-ad",START-DATE="2025-12-12T19:04:59.079Z",DURATION=20.000,X-NET-LIVE-VIDEO-AD-AD-BREAK-ID="test"
```


| Attribute | Description | 
| --- | --- | 
| ID | Format: `stitched-ad-{timestamp}-{duration}`<br />`{timestamp}`: Unix timestamp of the ad start<br />`{duration}:` Ad duration as an integer in nanoseconds<br />Type: Array of strings | 
| CLASS | Always live-video-net-stitched-ad for SSAI ads. | 
| START-DATE | ISO 8601 program date/time when the ad begins. | 
| DURATION | Ad length in seconds. | 
| X-NET-LIVE-VIDEO-AD-AD-BREAK-ID | The ad break ID returned by IVS when the InsertAdBreak operation was called. | 

**2. Stream Source Change**

```
#EXT-X-DATERANGE:ID="source-1765566299",CLASS="live-video-net-stream-source",START-DATE="2025-12-12T19:04:59.079Z",END-ON-NEXT=YES,X-NET-LIVE-VIDEO-STREAM-SOURCE="0f262e65-a709-4ef1-8741-e82d936c"
```


| Attribute | Description | 
| --- | --- | 
| CLASS | Always live-video-net-stream-source. | 
| START-DATE / END-ON-NEXT | Time metadata for this source range. | 
| X-NET-LIVE-VIDEO-STREAM-SOURCE | Hints to the player that the video source is changing. Value is live for primary content or a unique ID for ad content. | 

**3. Discontinuity Marker**

```
#EXT-X-DISCONTINUITY
```

Standard HLS tag signaling that encoding parameters may change between the live stream and the ad content.

#### Ad Segments
<a name="ssai-playlist-reference-live-ad-segments"></a>

```
#EXT-X-PROGRAM-DATE-TIME:2025-12-12T19:04:59.079Z 
#EXTINF:2.000,0f262e65-a709-4ef1-8741-e82d936c 
https://4ce388b1cf28.j.cloudfront.hls.live-video.net/v1/segment/CvsCse8Qbs5DU_aRmrVLd72_nK9lo9xS1KjD115LsIXcsD27JfLfkSuamLUivqOTrfHUeGf6Zmx_c9rhq0btTOu7E4F1DaU8knNoebLq6FlKp6q8ysaQdEA10gKCNP92oAQ_0DGLInY462O9HUxgtk5KHj23ZjPhVCxIh3DjWqwaevDci1_q7dYL55rgSKd11SfpsGSS9Yup4g5dfzyGhfz6Y2Skaj34JtoVyd8Nxlppc4jDlZl-6j7YM1i2qdUcM3VNWrZrxCisBXgOPtI3vFdeNcNjPzVdOGjMz5cXcQIp8YOCwnkdkomhn_3xxmB1Zngl3QPao6-oPsjH3qVcMOCuKfKZSmRJGFLvkrO1PefV5ya3eUvihXCMvDE-81EmGp5q9ErEgFpz06rMDbYFWb3z9H8X0t8KzvGDOaqKTYHZ0lgEV-fULeDQ76pDy_OVPwhO2vJMxBpfdQ_IeB1QUK2wJmXJ96Mvv0C2dcb0F7zE3lr_iBGemUjwmb7JmBoM3HdJbpV0TGp8C6vhIAEqCXVzLXdlc3QtMjD3DQ.ts?dna=CmanuVzG9F6kGS2X7ThbGZyZPHWgX2TiBlBMYsvGWLcWaLWyntTaWRp5D9qjZsrGKkzdwoLNY4pri6ZgpxnzqLqWvhcP6zoGu8vifP5NxPgiNKMmYdUmQrqTAf7jbauvE3c6B9ebptAaDEkrbrnG1qF8Cv3kbiABKgl1cy13ZXN0LTIw9w0
```


| Attribute | Description | 
| --- | --- | 
| EXT-X-PROGRAM-DATE-TIME | Timestamp of this segment. | 
| EXTINF | Format: `{duration},{tag}`<br />`{duration}`: Segment length in seconds.<br />`{tag}`: Source identifier. For live content, this is always `live`. For ad content, this is a UUID provided by MediaTailor that uniquely identifies the ad asset transcode | 
| Segment URL | IVS-hosted endpoint containing encrypted information about the segment and its location in IVS caches. | 

### VOD Variant Playlist with SSAI
<a name="ssai-playlist-reference-vod"></a>

When a live stream is recorded, IVS generates and writes a VOD playlist to S3 that includes SCTE-35 ad markers at the positions where ads were triggered during the live stream. To serve ads during VOD playback, you serve this IVS playlist through MediaTailor, which is responsible for stitching ad segments into the playlist. MediaTailor replaces the original VOD segments during the ad break with ad segments.

**1. Ad Break Start Marker (SCTE35-OUT)**

```
#EXT-X-DATERANGE:ID="12345678",START-DATE="2025-12-06T00:45:45.723Z",PLANNED-DURATION=20.0,SCTE35-OUT=0xFC302000000000000000FFF00F05F8E7AEFC7FFFFE001B7740000000000000340CFD88
```


| Attribute | Description | 
| --- | --- | 
| ID | Unique identifier for this ad break. Used to correlate the start and end markers. | 
| START-DATE | ISO 8601 program date/time when the ad break begins. | 
| PLANNED-DURATION | Expected duration of the ad break in seconds. | 
| SCTE35-OUT | SCTE-35 marker signaling the start of the ad break. | 

**2. Ad Segments (MediaTailor Stitched)**

```
#EXTINF:2.0, ../../../../segment/b2857627df9428679e888ee8daa979d0b7559801/gk-test-ivs-vod/bd0c7d90-a47c-4a91-b5ec-7d0f9897049b/0/3
```


| Attribute | Description | 
| --- | --- | 
| EXTINF | Duration of the ad segment in seconds. | 
| Segment URL | Relative path to MediaTailor-hosted ad segment. | 

**3. Ad Break End Marker (SCTE35-IN)**

```
#EXT-X-DATERANGE:ID="12345678",START-DATE="2025-12-06T00:45:45.723Z",END-DATE="2025-12-06T00:46:07.889Z",DURATION=20.0,SCTE35-IN=0xFC302000000000000000FFF00F05F8E7AEFC7F7FFE001B7740000000000000C23E5851
```


| Attribute | Description | 
| --- | --- | 
| ID | Same ID as the start marker. Links the two together. | 
| START-DATE | Original start time of the ad break (same as start marker). | 
| END-DATE | ISO 8601 timestamp when the ad break ended. | 
| DURATION | Actual duration of the ad break in seconds. | 
| SCTE35-IN | SCTE-35 marker signaling the end of the ad break. | 