# IVS Player SDK

To use Amazon Interactive Video Service (IVS), you must use the Amazon IVS Player. The
Player is a cross-platform suite of SDKs for playback of Amazon IVS streams. It is designed
to leverage the Amazon IVS architecture and optimized for Amazon IVS playback.

The only player whose performance we can guarantee is the Amazon IVS player. To achieve
low latency, the Amazon IVS player is required.

Key features of the Amazon IVS player are:

- **Low-latency streaming** — Low latency is a critical
  component in building good interactive user experiences that enrich the audience
  experience. Latency creeps in incrementally throughout the transmission path between
  broadcaster and viewer, eroding responsiveness.

End-to-end latency is the delay from when a live stream is captured on camera to
when it appears on a viewer’s screen. Amazon IVS is designed to deliver low
end-to-end latency (under five seconds, depending on the broadcast location and
broadcaster settings). _To achieve this low latency, the
Amazon IVS player is required_.

- **Cross-platform consistency** — Viewers watch
  broadcasts on a variety of platforms. From mobile devices to web browsers, the
  Amazon IVS Player gives all viewers a similar experience. This consistency is
  possible because every platform uses the same library of player functions. The
  player library is an integral component of the Amazon IVS architecture. Using one
  video stack ensures that all video-playback behaviors — including low-latency mode,
  timed metadata, analytics, error tracking, reporting, and logging — are available in
  a consistent way on all supported platforms.
- **Adaptive bitrate streaming (ABR)** — The Amazon IVS
  Player uses ABR algorithms optimized for low-latency environments. The Player
  measures quality of service and bandwidth availability in real time and adapts video
  quality and buffer levels, to provide uninterrupted playback. When connection
  quality suffers, ABR switches to a lower bitrate; when connection quality improves,
  it switches to a higher bitrate.
- **Timed metadata** — The Amazon IVS Player supports
  _timed metadata_, which can be used to build
  interactive elements such as polls and quizzes. Metadata is a set of data that
  describes and gives information about other data. With "timed" metadata, a timecode
  accompanies the piece of data about the stream. During playback, the timecode serves
  as a cue point to trigger action based on the data, such as:
  - Sending player statistics for a sports stream
  - Sending product details for a live shopping stream
  - Sending questions for a live quiz stream

- **Robust error handling** — Handling transient errors
  well avoids interruptions in the viewing experience. The Amazon IVS Player’s robust
  error handling detects many potential streaming errors, automatically switching to
  an alternative rendition. Viewers continue watching the broadcast uninterrupted,
  without having to take any corrective action.
- **Ease of integration** — The Amazon IVS Player API
  bridges the gap between Amazon IVS customers’ applications and the Player library.
  The API has bindings for all supported platforms, making it easy to integrate the
  Player into applications while using familiar coding environments and techniques.
  With full control over UI elements, customers can customize the branding and
  presentation aspects of their applications.
  The Amazon IVS player does not support casting with Airplay, but developers can implement Airplay by transitioning sessions to AVPlayer. However, latency on AVPlayer is higher than in the Amazon IVS player SDK, so the switch will not be seamless. An example of how to accomplish this transition is provided [here](https://github.com/aws-samples/sample-for-airplay-on-ivs "https://github.com/aws-samples/sample-for-airplay-on-ivs").

Casting with Chromecast can
be implemented outside the player using the default Chromecast receiver apps. However,
latency in those apps is higher than in the Amazon IVS player SDK, so the switch will not be
seamless. Also see our documentation on the Amazon IVS Broadcast SDK: for [Low-Latency Streaming](broadcast.md "broadcast.md") and for [Real-Time Streaming](../RealTimeUserGuide/broadcast.md "../RealTimeUserGuide/broadcast.md").

## Browser & Platform

Requirements

For details on the latest released versions of various browsers, see:

- [Chrome Platform
  Status](https://chromestatus.com/roadmap "https://chromestatus.com/roadmap")
- [Firefox
  Releases](https://www.mozilla.org/en-US/firefox/releases/ "https://www.mozilla.org/en-US/firefox/releases/")
- [Microsoft Edge Release Schedule](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule")
- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes "https://developer.apple.com/documentation/safari-release-notes")

While Amazon IVS may work with some older browsers, we do not fix bugs related to
older browsers.

The IVS Player Web SDK (including the Video.js and Player JW integrations) is not
supported in browser-like environments. This includes Native WebViews and “10-foot
devices” (TVs, consoles, set-top boxes) which support web applications. Please contact
IVS Support if you're unsure of specific browser support outside of the tables listed
below.

### Desktop

Browsers

| Desktop Browser | Supported Platforms   | Supported Versions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chrome          | Windows, macOS        | Two major versions (current and most recent prior version)                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Firefox         | Windows, macOS        | Two major versions (current and most recent prior<br>version)                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Edge            | Windows 8.1 and later | 44.0 and later<br>(In auto-quality mode on [Microsoft Edge Legacy](https://support.microsoft.com/en-us/microsoft-edge/what-is-microsoft-edge-legacy-3e779e55-4c55-08e6-ecc8-2333768c0fb0 "https://support.microsoft.com/en-us/microsoft-edge/what-is-microsoft-edge-legacy-3e779e55-4c55-08e6-ecc8-2333768c0fb0"), only normal-latency playback<br>is supported, not low-latency playback. Auto-quality mode refers<br>to whether ABR is enabled. For example, on the Web player, see<br>`setAutoQualityMode`. |
| Safari          | macOS                 | Two major versions (current and most recent prior<br>version)(In auto-quality mode on Safari for macOS 14 and above, IVS Player 1.3.0 and above support<br>low-latency playback. For earlier versions of Safari and IVS<br>Player, only normal-latency playback is supported. See above for<br>"auto-quality mode.")                                                                                                                                                                                           |

### Mobile

Browsers

| Mobile Browser                       | Supported Versions                                                                                                                                                                                                                                                      |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chrome for iOS, Safari for iOS       | Two major versions (current and most recent prior<br>version)<br>(Low-latency playback is not supported. Normal latency<br>playback is supported. This constraint applies to all browsers<br>for iOS.) (Timed metadata is supported only in<br>Player 1.3.0 and later.) |
| Chrome for iPadOS, Safari for iPadOS | Two major versions (current and most recent prior<br>version)<br>(When "Request Mobile Website" is selected:<br>• Low-latency playback is not supported.<br>• Timed metadata is supported only in Player 1.3.0 and<br>later.)                                           |
| Chrome for Android                   | Two major versions (current and most recent prior<br>version)                                                                                                                                                                                                           |

### Native

Platforms

| Platform | Supported Versions | Supported Devices  |
| -------- | ------------------ | ------------------ |
| Android  | 6.0 and later      | Phones and tablets |
| iOS      | 14+                | All                |

IVS supports a minimum of 4 major iOS versions and 6 major Android versions. Our current
version support may extend beyond these minimums. Customers will be notified via SDK
release notes at least 3 months in advance of a major version no longer being
supported.

## Reducing Latency in Third-Party

Players

**For Basic and Standard channel types**: For the lowest
possible latency, you must use the Amazon IVS player. In third-party players (including
iOS Safari), you can reduce latency to about 10 seconds by using the following
configuration:

- Set your encoder’s (e.g. OBS) keyframe interval to 2 seconds or below.
- Add `?keyframeInterval=2` to the RTMP(S) URL. For example:
  `rtmps://a1b2c3d4e5f6.global-contribute.live-video.net:443/app/sk_us-west-2_abcd1234efgh5678ijkl?keyframeInterval=2`

**Note**: The keyframe interval specified as part of the
RTMP URL must be greater than or equal to the value configured in the encoder;
otherwise, you may have playback issues. You can set the value to any integer between 2
and 6 inclusive, but 2 enables the lowest latency.

**For Advanced channel types**: The above guidance does
not apply. Advanced channel types generate keyframe intervals automatically for encoding
efficiency, with at most 2 seconds between keyframes, regardless of the source encoding
keyframe interval setting.

### iOS Safari

In iOS Safari, you can reduce latency to approximately 6-8 seconds by using the
IVS player and configuring it to use a service worker. See [Set Up Service Worker](web-getting-started.md#web-service-worker "web-getting-started.md#web-service-worker") in the _Player SDK: Web
Guide_ for implementation details and a reference sample.

**Note**: Getting the lowest latency requires an IVS
stream with the keyframe interval set to 2 seconds.

## Audio-Only Playback

All IVS channel types support audio-only renditions. This can be particularly valuable
for mobile applications. For instance, in your mobile app, you can switch the player to
the audio-only rendition when the user backgrounds the application to conserve
bandwidth.

For ADVANCED-SD and ADVANCED-HD channels, the audio-only rendition is included
automatically in the multivariant playlist. For BASIC and STANDARD channels, you must
append the `?allow_audio_only=true` query parameter to the playback URL to
enable inclusion of the audio-only rendition.

Note: The IVS web player SDK supports audio-only playback only in versions 1.24.0 and
later.

## Support

If you encounter a playback error or other playback issue with your stream, determine
the unique playback session identifier via the player API.

| For this Amazon IVS player: | Use this:                              |
| --------------------------- | -------------------------------------- |
| Android                     | `sessionId` function                   |
| iOS                         | `sessionId` property of<br>`IVSPlayer` |
| Web                         | `getSessionId` function                |

Share this playback session identifier with AWS support. With it, they can get
information to help troubleshoot your issue.

**Note:** The Player is continually improved. See [Amazon IVS Release Notes](release-notes.md "release-notes.md") for available versions and
fixed issues. If appropriate, before contacting support, update your version of the
Player and see if that resolves your issue.

### Versioning

The Amazon IVS Player SDKs use [semantic
versioning](https://semver.org/ "https://semver.org/").

For this discussion, suppose:

- The latest release is 4.1.3.
- The latest release of the prior major version is 3.2.4.
- The latest release of version 1.x is 1.5.6.

Backward-compatible new features are added as minor releases of the latest
version. In this case, the next set of new features will be added as version
4.2.0.

Backward-compatible, minor bug fixes are added as patch releases of the latest
version. Here, the next set of minor bug fixes will be added as version
4.1.4.

Backward-compatible, major bug fixes are handled differently; these are added to
several versions:

- Patch release of the latest version. Here, this is version 4.1.4.
- Patch release of the prior minor version. Here, this is version
  3.2.5.
- Patch release of the latest version 1.x release. Here, this is version
  1.5.7.

Major bug fixes are defined by the Amazon IVS product team. Typical examples are
critical security updates and selected other fixes necessary for customers.

**Note:** In the examples above, released versions
increment without skipping any numbers (e.g., from 4.1.3 to 4.1.4). In reality, one
or more patch numbers may remain internal and not be released, so the released
version could increment from 4.1.3 to, say, 4.1.6.
