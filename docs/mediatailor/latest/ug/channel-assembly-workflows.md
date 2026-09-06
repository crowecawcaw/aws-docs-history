

# Channel Assembly workflow types
<a name="channel-assembly-workflows"></a>

AWS Elemental MediaTailor Channel Assembly supports three workflow types for creating linear streaming channels. Each workflow type uses a different combination of source content to meet specific use cases. This topic describes each workflow type, when to use it, and links to the detailed setup procedures.


| Workflow type | Description | Playback mode | Use case | 
| --- | --- | --- | --- | 
| VOD-to-live | Assembles pre-recorded VOD assets into a live linear stream | Loop or Linear | 24/7 channels from a content library | 
| Live-to-live | Passes through live source feeds as programs in a scheduled channel | Linear only | News, sports, regional programming | 
| VOD \+ Live-to-live (Mixed) | Combines VOD and live sources in a single channel schedule | Linear only | Channels with mostly VOD content that include scheduled live events | 

## VOD-to-live
<a name="channel-assembly-workflows-vod-to-live"></a>

A VOD-to-live channel creates a linear stream entirely from pre-encoded, pre-packaged VOD content. The stream looks like a live broadcast with a live sliding manifest window, but uses only VOD assets. You don't need SCTE-35 markers in your source content because you define ad breaks when you schedule programs.

### When to use
<a name="channel-assembly-workflows-vod-to-live-when"></a>
+ You have a library of VOD assets and want to create a 24/7 linear channel.
+ You want to monetize content with ad breaks but don't have SCTE-35 markers in your source content.
+ You want a simple, low-cost linear stream that doesn't require live encoding infrastructure.

### How it works
<a name="channel-assembly-workflows-vod-to-live-how"></a>

1. **Prepare your content** – Encode and package your VOD assets. Host them on an origin server (Amazon S3, AWS Elemental MediaPackage, or any HTTP origin).

1. **Create a source location** – Register your origin server with MediaTailor.

1. **Add VOD sources** – Register each piece of content and define its package configurations and source groups.

1. **Create a channel** – Choose a playback mode (Loop or Linear) and configure outputs.

1. **Schedule programs** – Add programs to your channel's schedule in the order you want them to play.

1. **Configure ad breaks** – Add ad breaks to each program. Connect to an SSAI configuration for personalized ads.

1. **Start your channel and configure a CDN** – Start the channel. Optionally, add a CDN in front of it for scale and cost savings.

### Choosing a playback mode
<a name="channel-assembly-workflows-vod-to-live-playback"></a>

VOD-to-live channels support two playback modes:
+ **Loop (Basic tier)** – Programs play back-to-back in an endless loop. When the last program finishes, playback returns to the first. This is the simplest option for a 24/7 channel. Loop mode does not support live sources or filler slate.
+ **Linear (Standard tier)** – Programs play once in sequence. Linear mode supports time-based scheduling and filler slate for gaps between programs.

### Content requirements
<a name="channel-assembly-workflows-vod-to-live-content"></a>

For smooth transitions, all VOD assets in the same channel must have:
+ The same number of renditions (video, audio, subtitle, and so on) across all sources in a source group
+ Consistent segment durations across all assets. We recommend 2 to 6 seconds.
+ Matching bitrates and resolutions for corresponding renditions

**Important**  
Channel Assembly does not support per-title encoding or automated ABR encoding. These methods produce assets with different rendition counts and durations, which causes playback failures at program transitions.

### Ad breaks and monetization
<a name="channel-assembly-workflows-vod-to-live-ads"></a>

You define ad breaks when you add programs to your schedule. Each ad break needs an offset in milliseconds from the start of the program. The offset must align with a segment boundary on all tracks in the VOD source.

Your VOD source manifest might contain ad markers. For HLS, these are `EXT-X-DATERANGE` or `EXT-X-CUE-OUT` tags with a duration. For DASH, use `EventStream`. When MediaTailor detects these markers, it shows their offsets as options when you set up the ad break. This provides the most precise ad placement.

To serve personalized ads, pair your channel with a MediaTailor SSAI playback configuration. Set the content source to your channel's playback URL.

### Tips
<a name="channel-assembly-workflows-vod-to-live-tips"></a>


| Topic | Detail | 
| --- | --- | 
| Ad break placement | Ad break offsets that don't align with a segment boundary are adjusted to the nearest boundary. Use shorter segments (2–4 seconds) for more precise ad placement. | 
| Signed URL origins | MediaTailor caches VOD source manifests when you first add the source. If you use signed URLs with short expiration times, the cached URLs might expire before playback. Call the `UpdateVodSource` API to force MediaTailor to re-fetch the manifest. | 
| Rendition mismatch | If a program fails to transition cleanly, check that all VOD sources in the channel have the same rendition counts and use the same ABR ladder. | 
| Scheduling ahead | Add programs to a running Linear channel at least 10 minutes before their air time. Channel Assembly begins processing programs within this window. | 

For instructions on creating your first channel, see [Getting started with MediaTailor channel assembly](channel-assembly-getting-started.md).

## Live-to-live
<a name="channel-assembly-workflows-live-to-live"></a>

A live-to-live channel passes through live source feeds as programs in a scheduled channel. The channel switches between different live sources based on your schedule. Use this workflow when all of your content is live and you want to assemble multiple live feeds into a single linear channel.

### When to use
<a name="channel-assembly-workflows-live-to-live-when"></a>
+ You have multiple live encoders/packagers and want to switch between them on a schedule.
+ You're building a regional channel that switches between national and regional live feeds at different times of day.
+ You have 24/7 live feeds (news, sports networks) and want to create a curated channel that draws from multiple sources.

### How it works
<a name="channel-assembly-workflows-live-to-live-how"></a>

1. **Set up your live encoding pipeline** – Encode and package your live content using AWS Elemental MediaLive, AWS Elemental MediaPackage, or any live packaging origin.

1. **Create a source location** – Register the origin server for your live content with MediaTailor.

1. **Add live sources** – Register each live feed and define its package configurations and source groups.

1. **Create a channel** – Choose the Linear playback mode (required for live sources) and configure outputs.

1. **Schedule programs** – Add live source programs to your channel's schedule. Specify the duration for each live program.

1. **Start your channel and configure a CDN** – Start the channel. Optionally, add a CDN in front of it for scale and cost savings.

### Playback mode
<a name="channel-assembly-workflows-live-to-live-playback"></a>

Live-to-live channels require the **Linear (Standard tier)** playback mode. Loop mode does not support live sources.

### Content requirements
<a name="channel-assembly-workflows-live-to-live-content"></a>

In addition to the general requirements listed in [Working with source locations](channel-assembly-source-locations.md):
+ **HLS live sources** – You must provide `#EXT-X-PROGRAM-DATE-TIME` tags for the first segment in the manifest window and on every discontinuity.
+ **HLS ad markers** – You must configure ad markers as `DATERANGE`.
+ **Source manifest window** – Use a manifest window duration that's at least 30 seconds longer than the manifest window on your Channel Assembly channel.
+ **Target duration** – Make the target duration match the duration of the existing sources in the channel.
+ **Child playlists** – Make the number of child playlists match that of the other sources in the channel.

### Live source configuration with MediaPackage
<a name="channel-assembly-workflows-live-to-live-emp"></a>

If you use AWS Elemental MediaPackage as your packaging origin, we recommend the following configuration:

**HLS settings:**


| Setting | Value | Necessity | Notes | 
| --- | --- | --- | --- | 
| Endpoint type | Apple HLS or CMAF | Required | Use Apple HLS for TS segments, CMAF for MP4 segments | 
| ProgramDateTimeIntervalSeconds | 1 | Required | Prevents playback issues at discontinuities. | 
| PlaylistWindowSeconds | 30 seconds longer than the CA manifest window | Required |  | 
| AdMarkers | DATERANGE | Required | Required when passing through ad markers. | 
| IncludeIframeOnlyStream | Disabled | Recommended |  | 

**DASH settings:**


| Setting | Value | Necessity | Notes | 
| --- | --- | --- | --- | 
| ManifestLayout | FULL | Recommended |  | 
| SegmentTemplateFormat | NUMBER\_WITH\_TIMELINE or TIME\_WITH\_TIMELINE | Recommended | NUMBER\_WITH\_DURATION is not supported. | 
| ManifestWindowSeconds | 30 seconds longer than the CA manifest window | Required |  | 
| PeriodTriggers | ADS | Required | Required when passing through ad markers. | 

### Ad breaks
<a name="channel-assembly-workflows-live-to-live-ads"></a>

For live sources, you don't define ad breaks in the Channel Assembly schedule. Instead, ad breaks in the live source manifests are passed through automatically:
+ **HLS** – Ad breaks using the `EXT-X-DATERANGE` tag are passed through.
+ **DASH** – Ad breaks using `EventStream` are passed through.

To monetize passed-through ad breaks, pair your channel with a MediaTailor SSAI playback configuration.

### Tips
<a name="channel-assembly-workflows-live-to-live-tips"></a>


| Topic | Detail | 
| --- | --- | 
| Program duration | You must specify a duration for each live source program. When the duration expires, Channel Assembly transitions to the next program in the schedule. | 
| Filler slate | If there are gaps between programs in the schedule, MediaTailor plays filler slate. If the duration of the slate is less than the duration of the gap, MediaTailor loops the slate. Configure filler slate when you create your channel. | 
| Regional channels | Use live sources to create regional channels. Run one encoder/packager for national content, then run regional encoders when those regions are live. Create a separate channel per region, each with its own schedule. | 
| Transition timing | MediaTailor starts playback of a program on a common segment boundary. For absolute transitions, expect up to one segment of variance between the scheduled time and the actual transition. | 
| Encoding costs | Minimize costs by running encoders only when content is live. Configure filler slate on your channel to cover gaps between live events. | 

## VOD \+ Live-to-live (Mixed)
<a name="channel-assembly-workflows-mixed"></a>

A mixed channel combines both VOD and live sources in a single schedule. This is the most flexible workflow type. Use it when your channel is primarily VOD content with scheduled live events interspersed, or when you want to bridge gaps between live events with pre-recorded content.

### When to use
<a name="channel-assembly-workflows-mixed-when"></a>
+ Your channel is mostly VOD content, but you have scheduled live events (nightly news, weekly sports, special broadcasts).
+ You want to switch between VOD filler content and live feeds throughout the day.
+ You're building a channel that uses pre-recorded content between live event windows.

### How it works
<a name="channel-assembly-workflows-mixed-how"></a>

1. **Set up your content pipeline** – Encode and package both your VOD assets and live content. Host them on origin servers.

1. **Create source locations** – Register your origin servers with MediaTailor. You can use separate source locations for VOD and live content, or a single source location if they share an origin.

1. **Add VOD sources and live sources** – Register your VOD assets and live feeds, each with their package configurations and source groups.

1. **Create a channel** – Choose the Linear playback mode (required when using live sources) and configure outputs.

1. **Schedule programs** – Add a mix of VOD and live source programs to your channel's schedule. Use absolute transitions for live programs that must start at specific times. Use relative transitions for VOD programs that fill gaps.

1. **Configure ad breaks** – Add ad breaks to VOD programs. For live programs, ad breaks are passed through from the source manifest.

1. **Start your channel and configure a CDN** – Start the channel. Optionally, add a CDN in front of it for scale and cost savings.

### Playback mode
<a name="channel-assembly-workflows-mixed-playback"></a>

Mixed channels require the **Linear (Standard tier)** playback mode. Loop mode does not support live sources.

### Content requirements
<a name="channel-assembly-workflows-mixed-content"></a>

Mixed channels must meet the content requirements for both VOD and live sources:
+ All sources (VOD and live) within a source group must have the same number of renditions.
+ VOD and live sources must have matching target segment durations.
+ Live sources must meet the requirements for live sources, including `EXT-X-PROGRAM-DATE-TIME` tags for HLS.

### Scheduling patterns
<a name="channel-assembly-workflows-mixed-scheduling"></a>

Mixed channels support two transition types for programs:
+ **Relative** – The program plays before or after another program in the schedule. Available for VOD source programs only.
+ **Absolute** – The program plays at a specific wall-clock time. Available for both VOD and live source programs in Linear mode.

**Common scheduling patterns:**


| Pattern | Description | Example | 
| --- | --- | --- | 
| VOD filler with scheduled live windows | VOD programs fill the schedule, with live programs inserted at specific times. | A movie channel that switches to a live sports event at 8:00 PM. | 
| Live primary with VOD interstitials | A live feed runs most of the time, with VOD programs during breaks or off-hours. | A news channel that plays pre-recorded segments between live broadcasts. | 
| Time-of-day switching | Different sources (live or VOD) play at different times of day. | National feed during prime time, regional live feed in the morning, VOD content overnight. | 

### Ad breaks
<a name="channel-assembly-workflows-mixed-ads"></a>

Ad break behavior depends on the source type of each program:
+ **VOD programs** – You define ad breaks in the schedule with an offset in milliseconds. Connect to an SSAI configuration for personalized ads.
+ **Live programs** – Ad breaks are passed through from the live source manifest automatically. HLS uses `EXT-X-DATERANGE` tags; DASH uses `EventStream`.

### Tips
<a name="channel-assembly-workflows-mixed-tips"></a>


| Topic | Detail | 
| --- | --- | 
| Transition from VOD to live | When transitioning from a VOD program to a live program at an absolute time, MediaTailor truncates the VOD program at the closest common segment boundary to the live program's start time. | 
| Transition from live to VOD | When a live program's duration expires, MediaTailor transitions to the next program in the schedule. If the next program is VOD, playback is seamless as long as content requirements are met. | 
| Filler slate | Configure filler slate on your channel. MediaTailor plays slate during any gaps between programs. If the live source becomes unavailable mid-program, Channel Assembly continues to serve the last known segments until the program duration expires. | 
| Mixed ad monetization | You can use a single SSAI configuration for the entire channel. MediaTailor handles both scheduled ad breaks (VOD programs) and passed-through ad breaks (live programs) in the same stream. | 
| Schedule flexibility | Add VOD programs at least 10 minutes ahead of air time. For live programs using absolute transitions, schedule them at least 15 minutes ahead on a running channel. | 

## Choosing the right workflow
<a name="channel-assembly-workflows-choosing"></a>

Use the following decision guide to choose the right workflow type for your use case:
+ If you have *only VOD content* and don't need time-based scheduling → Use **VOD-to-live** with Loop playback mode.
+ If you have *only VOD content* and need time-based scheduling → Use **VOD-to-live** with Linear playback mode.
+ If you have *only live content* → Use **Live-to-live**.
+ If you have *both VOD and live content* → Use **VOD \+ Live-to-live (Mixed)**.

### Feature comparison
<a name="channel-assembly-workflows-comparison"></a>


| Feature | VOD-to-live (Loop) | VOD-to-live (Linear) | Live-to-live | Mixed | 
| --- | --- | --- | --- | --- | 
| VOD sources | Yes | Yes | No | Yes | 
| Live sources | No | No | Yes | Yes | 
| Absolute transitions | No | Yes | Yes | Yes | 
| Relative transitions | Yes | Yes | No | Yes (VOD only) | 
| Scheduled ad breaks | Yes | Yes | No | Yes (VOD only) | 
| Pass-through ad breaks | No | No | Yes | Yes (Live only) | 
| Filler slate | No | Yes | Yes | Yes | 
| 24/7 looping | Yes | No | No | No | 
| Time-based scheduling | No | Yes | Yes | Yes | 
| Channel tier | Basic | Standard | Standard | Standard | 

## Next steps
<a name="channel-assembly-workflows-next-steps"></a>
+ [Getting started with MediaTailor channel assembly](channel-assembly-getting-started.md) – Step-by-step tutorial for creating your first channel
+ [Working with source locations](channel-assembly-source-locations.md) – Detailed procedures for managing source locations and content
+ [Working with channels](channel-assembly-channels.md) – Channel configuration options and playback modes
+ [Adding a program to a channel's schedule](channel-assembly-programs.md) – Scheduling programs with VOD and live sources
+ [Insert personalized ads and ad breaks in a channel stream](channel-assembly-integrating-mediatailor-ssai.md) – Monetization with SSAI
+ [Build MediaTailor linear channels with channel assembly and CDN](ca-cdn-wflw.md) – CDN integration for scale and cost savings
+ [Time-shifting a channel's playback](channel-assembly-time-shift.md) – Enable catch-up and start-over functionality