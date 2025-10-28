# Advanced DASH manifest concepts

When working with DASH manifests in MediaTailor, understanding the following advanced concepts can help you configure and troubleshoot your streaming workflows more effectively:

Period start time calculation

In DASH manifests, Period start times are calculated based on the MPD's `availabilityStartTime` attribute and the Period's `start` attribute. For live streams, the start time is relative to the availability start time, while for VOD content, it's typically relative to the beginning of the presentation.

When MediaTailor inserts ad Periods, it carefully calculates the start times to ensure seamless transitions between content and ads. This calculation takes into account:

- The original Period's start time
- The duration of preceding ad Periods
- Any time offset specified in the ad decision server response

Preroll timing calculations

Preroll ads in DASH manifests require special handling because they appear before the main content begins. MediaTailor inserts preroll ads as separate Periods at the beginning of the manifest with appropriate start times and durations.

For preroll ads, MediaTailor:

- Creates a new Period for each preroll ad
- Sets the first preroll Period's start time to 0
- Adjusts the start time of the main content Period to account for the total duration of all preroll ads

Live-to-VOD transitions

DASH manifests can transition from live to VOD (Video on Demand) format when a live stream ends. This transition involves changing the MPD's `type` attribute from `dynamic` to `static` and adjusting other attributes like `timeShiftBufferDepth` and `minimumUpdatePeriod`.

When MediaTailor processes manifests during live-to-VOD transitions, it ensures that:

- Ad markers are preserved in the VOD manifest
- Period start times are adjusted to maintain proper timing
- The manifest remains compatible with VOD playback clients

DRM handling

Digital Rights Management (DRM) information in DASH manifests is typically included in the `ContentProtection` elements within AdaptationSets or Representations. MediaTailor preserves these elements during ad insertion to ensure that content protection remains intact.

When processing DRM-protected content, MediaTailor:

- Maintains all ContentProtection elements from the original manifest
- Ensures that ad content uses compatible DRM schemes if applicable
- Preserves any DRM-related attributes and elements throughout the manifest

SCC flags

Supplemental Content Control (SCC) flags in DASH manifests provide additional information about content characteristics and playback requirements. These flags are typically included as attributes or elements within the MPD structure.

Common SCC flags that MediaTailor processes include:

- Content rating information
- Accessibility features (closed captions, audio descriptions)
- Content advisory notices
- Playback restrictions

MediaTailor preserves these flags during manifest processing to ensure that all content metadata is maintained in the personalized manifest.

Understanding these advanced concepts helps you configure MediaTailor for optimal performance and troubleshoot any issues that may arise in your DASH streaming workflows.
