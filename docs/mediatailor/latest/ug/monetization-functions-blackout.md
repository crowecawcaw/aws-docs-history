

# Blackout with Functions

A blackout replaces program content with a slate (a placeholder image or video) for viewers who aren't allowed to watch it. You can start or end a blackout from a tag at `POST_ORIGIN_RESPONSE`, or start one when the session begins at `PRE_SESSION_INITIALIZATION`. You can use blackout with HLS streams.

## How blackout works
<a name="monetization-functions-blackout-how"></a>

A start command opens a blackout window and the viewer sees the slate. An end command closes the window, or it closes when the maximum duration elapses, and program content resumes. A start command from a tag at `POST_ORIGIN_RESPONSE` must specify both a slate URL and a maximum duration. A start at `PRE_SESSION_INITIALIZATION` can omit the maximum duration, which then defaults to 2 hours.

Blackout requires `EXT-X-PROGRAM-DATE-TIME` tags in your origin's playlists. Without them, blackout commands have no effect. Your renditions must also have aligned segments that share media sequence numbers.

A start command from a tag applies to a viewer's session if the tag appears in that session's playlist. A viewer who joins after the tag has left the playlist doesn't get the blackout, unless your origin keeps the tag in its playlist while the blackout lasts.

The slate replaces program content from the segment that carries the start command. If an ad break is in progress at that segment, the slate starts after the break. For more information about ad breaks during a blackout, see [Ad breaks during a blackout](#monetization-functions-blackout-ads). Program content resumes at the segment that carries the end command. Every rendition switches between program content and slate on the same segment.

The maximum duration counts from the start of the segment that carries the start command. If the maximum duration elapses before an end command, program content resumes at the next segment boundary. If the maximum duration ends a fraction of a second after a segment boundary, program content resumes at that boundary instead.

Some origins keep the start tag at the top of the playlist. The segment that carries the tag then changes as the playlist moves. A viewer who joins later then gets a later start for the maximum duration. To end a blackout at the same time for every viewer, send an end command.

A blackout that starts at `PRE_SESSION_INITIALIZATION` replaces every segment of the viewer's first playlist. Its maximum duration counts from the first segment of that playlist. That segment can be up to one playlist window older than the session. So the blackout can end up to one playlist window earlier than the session start plus the maximum duration. To cover a fixed time, send an end command, or add the length of your playlist window to `aws.blackoutMaxDurationSecs`.

When a blackout lasts longer than the slate, the slate loops. MediaTailor adds an `EXT-X-DISCONTINUITY` tag where the slate starts, at the start of each loop, and where program content resumes.

## Slate requirements
<a name="monetization-functions-blackout-slate"></a>

A start command from a tag at `POST_ORIGIN_RESPONSE` must specify the slate URL. A start at `PRE_SESSION_INITIALIZATION` must set `aws.blackoutSlateUrl`. Without it, viewers see program content.

Use an MP4 slate that has both audio and video. If the server that hosts your slate uses HTTPS, its certificate must be from a well-known certificate authority, not a self-signed certificate. These are the same requirements as for the ad break slate. For more information, see [Configuring the slate](slate-management.md#configuring-the-slate).

Encode the slate's audio as AAC-LC at 48 kHz. The length guidance in the next section assumes AAC-LC audio at 48 kHz.

### MediaTailor blackout slate length
<a name="monetization-functions-blackout-slate-length"></a>

MediaTailor loops the slate for as long as the blackout lasts, up to 12 hours. Each pass of the slate's audio ends on a whole audio frame. If the slate length isn't a whole multiple of *L* (described next), each pass carries slightly more audio than video, up to one audio frame (about 21 ms).

Over many loops, some players let audio drift away from video. When the slate length is a whole multiple of *L*, audio and video have exactly the same length on every pass, so no drift builds up.

*L* is the shortest length that is both a whole number of slate segments and a whole number of audio frames. It depends on these two durations:

**Slate segment duration**  
The duration of the slate's segments as MediaTailor serves them. By default, MediaTailor transcodes ads and slates into 2-second segments. With segment length matching, MediaTailor uses your origin's segment duration. For more information, see [Dynamic transcoding](dynamic-transcoding.md). To confirm the duration, run a test blackout and read the `EXTINF` values of the slate segments.

**Audio frame duration**  
The samples per audio frame divided by the sample rate. For AAC-LC at 48 kHz, this is 1,024 ÷ 48,000 seconds, about 21.333 ms.

To compute *L*, write both durations as fractions in lowest terms, *p*/*q* and *r*/*t*. Then *L* = lcm(*p*, *r*) / gcd(*q*, *t*), where lcm is the least common multiple and gcd is the greatest common divisor. Use exact fractions, because a rounded decimal such as 29.97 gives the wrong answer. The example at the end of this section shows the calculation step by step.

This guidance is for AAC-LC audio at 48 kHz. At 44.1 kHz, *L* is impractically long for 29.97 and 59.94 fps content (for example, 10,250.24 seconds with 2.002-second segments).

The following table lists *L* for common outputs. The 2.002-second and 6.006-second rows apply when MediaTailor matches your origin's segment length.


| Output frame rate | Slate segment duration | Segment duration as a fraction | *L* | Slate lengths near 10 minutes | 
| --- | --- | --- | --- | --- | 
| 29.97 or 59.94 fps | 2.002 seconds | 1001/500 | 64.064 seconds (32 segments, 3,003 audio frames) | 576.576 seconds (9 × L), 640.64 seconds (10 × L) | 
| 29.97 or 59.94 fps | 6.006 seconds | 3003/500 | 192.192 seconds (32 segments, 9,009 audio frames) | 576.576 seconds (3 × L), 768.768 seconds (4 × L) | 
| 25, 30, 50, or 60 fps | 2 seconds | 2/1 | 8 seconds (4 segments, 375 audio frames) | 600 seconds (75 × L) | 
| 25, 30, 50, or 60 fps | 6 seconds | 6/1 | 24 seconds (4 segments, 1,125 audio frames) | 600 seconds (25 × L) | 

The table columns contain the following values:

**Output frame rate**  
The frame rate of your content's renditions. 29.97 and 59.94 fps share a row because the same segment duration fits both: 60 frames at 29.97 fps and 120 frames at 59.94 fps both last 2.002 seconds. These broadcast rates are exactly 30000/1001 and 60000/1001 frames per second. The other rates are exact.

**Slate segment duration**  
The `EXTINF` value of each segment in the slate's media playlists.

**Segment duration as a fraction**  
The segment duration as an exact ratio of whole numbers, which the formula needs. For example, 2.002 seconds is 2002/1000, which reduces to 1001/500.

***L***  
The shortest slate length that is both a whole number of segments and a whole number of audio frames. Every aligned slate length is a whole multiple of *L*.

**Slate lengths near 10 minutes**  
Whole multiples of *L* close to the recommended length.

Use a slate of about 10 minutes. Lengths from 1 to 30 minutes are suitable, as long as they're a whole multiple of *L*. Shorter slates loop more often, and each loop adds a discontinuity, so test your players if you choose a short slate.

Avoid slates of 1 hour or longer. They take longer to prepare and to fill CDN caches, and viewers can rebuffer while the caches fill. Don't use a slate of 2 hours or longer. It might never finish preparing, and viewers then see program content during the blackout.

**To choose a slate length**

1. Find the slate segment duration. If you aren't sure, run a test blackout and read the `EXTINF` values of the slate segments.

1. Find *L* in the table, or compute it.

1. Choose a whole multiple of *L* near the length that you want. Encode the slate to exactly that length, with AAC-LC audio at 48 kHz.

1. Check that the slate length divided by the segment duration, and the slate length divided by the audio frame duration, are both whole numbers.

**Example Compute *L* for 29.97 fps content with 2.002-second segments**  
This example uses AAC-LC audio at 48 kHz.  

1. **Segment duration as a fraction.** A 2.002-second segment holds 60 frames at 29.97 fps. The exact rate is 30000/1001 frames per second, so the segment duration is 60 × 1001 / 30000 = 1001/500 seconds. At 59.94 fps (60000/1001), the segment holds 120 frames and has the same duration.

1. **Audio frame duration.** An AAC-LC frame has 1,024 samples. At 48,000 samples per second, the frame duration is 1024/48000 = 8/375 seconds, about 21.333 ms.

1. **Least common multiple.** lcm(1001, 8) = 8,008, because 1001 = 7 × 11 × 13 and 8 = 2 × 2 × 2 share no factor. gcd(500, 375) = 125, because 500 = 4 × 125 and 375 = 3 × 125. So *L* = 8,008/125 = 64.064 seconds.

1. **Check.** 64.064 ÷ 2.002 = 32 segments, and 64.064 ÷ (8/375) = 3,003 audio frames. Both are whole numbers, so audio and video end together.

1. **Slate length.** For about 10 minutes, use 10 × 64.064 = 640.64 seconds: 320 segments and 30,030 audio frames.
A slate whose length isn't a multiple of *L* drifts. For example, a 600.6-second slate is 300 segments, but it's 600.6 ÷ (8/375) = 28,153.125 audio frames. The audio ends on a whole frame, so each loop has 28,154 audio frames (600.6187 seconds), which is 18.67 ms more audio than video.  
At 25 fps with 2-second segments, the same steps give a segment duration of 2/1 seconds (50 frames), the same 8/375-second audio frame, and *L* = lcm(2, 8) / gcd(1, 375) = 8 seconds. A 600-second slate is 75 × 8 seconds (300 segments and 28,125 audio frames), so it's aligned.

### Prepare the slate before the event
<a name="monetization-functions-blackout-slate-prepare"></a>

Your slate must be prepared for your content's renditions before viewers can see it. This happens the first time a blackout uses the slate. If the slate isn't ready when MediaTailor applies the start command to a viewer's session, that viewer sees program content for the whole blackout. Ad breaks during that blackout are personalized as usual. For a blackout that starts during a live event, this can affect every viewer who is watching.

Sessions that get the start command after the slate is ready see the slate. Longer slates take longer to prepare.

Run a test blackout well before the event.

**To prepare the slate**

1. Start a test blackout with the exact slate URL that the event uses, on the same playback configuration and origin. For example, use a `PRE_SESSION_INITIALIZATION` function that sets `aws.blackoutOperation` to `BLACKOUT_ON_INIT` and `aws.blackoutSlateUrl` to the slate URL for a test session.

1. Play the test session. The first session that uses a new slate starts its preparation, and it can show program content instead of the slate.

1. Wait, and then play a new test session. Longer slates need a longer wait. When a new session shows the slate, the slate is ready.

1. If the event is many hours after your test, test again closer to the event.

If you change the slate URL, your content's renditions or segment duration, or your transcode profile, prepare the slate again.

## Ad breaks during a blackout
<a name="monetization-functions-blackout-ads"></a>
+ For a viewer who is watching when the blackout starts, an ad break that's in progress plays to its end. The slate starts after the break.
+ If the break's ads are shorter than the break, the slate starts when the ads end. If your playback configuration has an ad break slate, that slate fills the rest of the break first, and the blackout slate starts when the break ends.
+ An ad break that starts during a blackout isn't personalized. The slate plays over it, MediaTailor doesn't request ads for it, and MediaTailor sends no tracking events for it. Any part of the break that runs past the end of the blackout plays the origin content.
+ If you use pre-roll ads, a viewer who joins during a blackout sees the pre-roll first, and then the slate.
+ If the slate wasn't ready when MediaTailor applied the start command, the viewer sees program content, and ad breaks are personalized as usual. For more information, see [Prepare the slate before the event](#monetization-functions-blackout-slate-prepare).

## Subtitle and I-frame playlists
<a name="monetization-functions-blackout-renditions"></a>

The slate has no subtitles. During a blackout, WebVTT subtitle playlists serve blank WebVTT segments that line up with the slate.

If the multivariant playlist that MediaTailor serves includes your I-frame playlists, MediaTailor prepares an I-frame rendition of the slate, and I-frame playlists show the slate the same way that video does. If MediaTailor can't prepare a matching I-frame rendition, it can't use the slate, and viewers see program content.

## Start or end blackout from a tag
<a name="monetization-functions-blackout-tag"></a>

In an HLS tag processor, patch `blackoutConfiguration` with `$updateTag`. The following table describes the blackout functions.


| Function | Description | 
| --- | --- | 
| $startBlackout(slateUrl, maxDurationSeconds) | Starts a blackout. At POST\_ORIGIN\_RESPONSE, both arguments are required: slateUrl must be a non-empty URL, and maxDurationSeconds must be greater than 0 and no more than 43,200 (12 hours). MediaTailor rejects and logs a start command that omits either argument or whose duration is out of range. | 
| $endBlackout() | Ends the active blackout. | 

The following example starts a blackout from a tag. Replace the example slate URL with the URL of your own slate.

```JSON
"tag": "{% $updateTag(tag, { 'blackoutConfiguration': $startBlackout('https://example.com/slates/regional.mp4', 600) }) %}"
```

For more information about the function type, see [HLS tag processor](monetization-functions-types-hls-tag-processor.md).

## Start blackout at session start
<a name="monetization-functions-blackout-session"></a>

A `PRE_SESSION_INITIALIZATION` function writes the following `aws.*` outputs.


| Output | Required | Description | 
| --- | --- | --- | 
| aws.blackoutOperation | Yes | BLACKOUT\_ON\_INIT starts a blackout when the session starts. NONE does nothing. | 
| aws.blackoutSlateUrl | Yes, with BLACKOUT\_ON\_INIT | The URL of the slate for the blackout. | 
| aws.blackoutMaxDurationSecs | No | Maximum blackout duration in seconds. Defaults to 7,200 (2 hours) when omitted. A non-numeric, non-positive, or over-12-hour value invalidates the command, and no blackout starts. | 

For more information about these service variables, see [Service variables (aws.\*)](monetization-functions-hooks-pre-session.md#monetization-functions-hooks-pre-session-output-aws).

## Limits
<a name="monetization-functions-blackout-limits"></a>

The maximum blackout duration is 12 hours (43,200 seconds). At `POST_ORIGIN_RESPONSE`, `maxDurationSeconds` is required on a start command. At `PRE_SESSION_INITIALIZATION`, `aws.blackoutMaxDurationSecs` is optional and defaults to 7,200 seconds (2 hours). For slate length, see [MediaTailor blackout slate length](#monetization-functions-blackout-slate-length).

For more information about limits, see [Limits](monetization-functions-limits.md).

## Troubleshoot blackout commands
<a name="monetization-functions-blackout-troubleshooting"></a>

MediaTailor logs a rejected blackout command to the customer log stream and doesn't start or end the blackout. MediaTailor rejects a command when the slate URL is missing or empty, when `maxDurationSeconds` is missing, non-positive, or greater than 12 hours, or when the command is otherwise malformed. Manifest processing continues (fail-open).

For more information about viewers who see program content instead of the slate, see [Blackout: Viewers see program content instead of the slate](monetization-functions-troubleshooting.md#monetization-functions-ts-blackout-no-slate). For more information about audio that drifts away from video during a long blackout, see [Blackout: Audio drifts away from video during a long blackout](monetization-functions-troubleshooting.md#monetization-functions-ts-blackout-av-drift).

For more information about troubleshooting, see [Troubleshooting and monitoring](monetization-functions-troubleshooting.md).

For more information about the blackout example, see [Example 7: Regional blackout](monetization-functions-examples-blackout.md).