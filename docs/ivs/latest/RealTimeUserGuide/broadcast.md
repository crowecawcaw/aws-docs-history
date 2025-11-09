# IVS Broadcast SDK | Real-Time Streaming

The Amazon Interactive Video Services (IVS) Real-Time Streaming broadcast SDK is for
developers who are building applications with Amazon IVS. This SDK is designed to leverage
the Amazon IVS architecture and will see continual improvement and new features, alongside
Amazon IVS. As a native broadcast SDK, it is designed to minimize the performance impact on
your application and on the devices with which your users access your application.

Note that the broadcast SDK is used for both sending and receiving video; i.e., you use
the same SDK for hosts and viewers. No separate player SDK needed.

Your application can leverage the key features of the Amazon IVS broadcast SDK:

- **High quality streaming** — The broadcast SDK
  supports high quality streaming. Capture video from your camera and encode it at up
  to 720p.
- **Automatic Bitrate Adjustments** — Smartphone users
  are mobile, so their network conditions can change throughout the course of a
  broadcast. The Amazon IVS broadcast SDK automatically adjusts the video bitrate to
  accommodate changing network conditions.
- **Portrait and Landscape Support** — No matter how
  your users hold their devices, the image appears right-side up and properly scaled.
  The broadcast SDK supports both portrait and landscape canvas sizes. It
  automatically manages the aspect ratio when the users rotate their device away from
  the configured orientation.
- **Secure Streaming** — Your user’s broadcasts are
  encrypted using TLS, so they can keep their streams secure.
- **External Audio Devices** — The Amazon IVS broadcast
  SDK supports audio jack, USB, and Bluetooth SCO external microphones.

## Platform Requirements

### Native Platforms

| Platform | Supported Versions                                                                                                           |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Android  | 9.0+ -<br>• note customers can build with versions 6.0+ but<br>will not be able to use real-time streaming<br>functionality. |
| iOS      | 14+                                                                                                                          |

IVS supports a minimum of 4 major iOS versions and 6 major Android versions. Our
current version support may extend beyond these minimums. Customers will be notified
via SDK release notes at least 3 months in advance of a major version no longer
being supported.

### Desktop Browsers

| Browser | Supported Platforms | Supported Versions                                                                    |
| ------- | ------------------- | ------------------------------------------------------------------------------------- |
| Chrome  | Windows, macOS      | Two major versions (current and most recent prior<br>version)                         |
| Firefox | Windows, macOS      | Two major versions (current and most recent prior<br>version)                         |
| Edge    | Windows 8.1+        | Two major versions (current and most recent prior<br>version)<br>Excludes Edge Legacy |
| Safari  | macOS               | Two major versions (current and most recent prior<br>version)                         |

### Mobile Browsers (iOS and Android)

| Browser | Supported Platforms | Supported Versions                                            |
| ------- | ------------------- | ------------------------------------------------------------- |
| Chrome  | iOS, Android        | Two major versions (current and most recent prior<br>version) |
| Firefox | Android             | Two major versions (current and most recent prior<br>version) |
| Safari  | iOS                 | Two major versions (current and most recent prior<br>version) |

#### Known Limitations

- On all mobile web browsers, we recommend publishing/subscribing with no more than three simultaneous publishers, due to performance constraints which cause video artifacts and black screens. If you require more publishers, configure
  [audio-only publish and subscribe](web-publish-subscribe.md#web-publish-subscribe-concepts-strategy-updates "web-publish-subscribe.md#web-publish-subscribe-concepts-strategy-updates").
- We do not recommend compositing a stage and broadcasting it to a
  channel on Android Mobile Web, due to performance considerations and
  potential crashes. If broadcast functionality is required, integrate the
  [IVS real-time streaming Android broadcast SDK](broadcast-android.md "broadcast-android.md").

## Webviews

The Web broadcast SDK does not provide support for webviews or weblike environments
(TVs, consoles, etc). For mobile implementations, see the Real-Time Streaming
Broadcast SDK Guide for [Android](broadcast-android.md "broadcast-android.md") and for [iOS](broadcast-ios.md "broadcast-ios.md").

## Required Device Access

The broadcast SDK requires access to the device's cameras and microphones, both those
built into the device and those connected through Bluetooth, USB, or audio jack.

## Support

The broadcast SDK is continually improved. See [Amazon
IVS Release Notes](release-notes.md "release-notes.md") for available versions and fixed issues. If appropriate,
before contacting support, update your version of the broadcast SDK and see if that
resolves your issue.

### Versioning

The Amazon IVS broadcast SDKs use [semantic
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
