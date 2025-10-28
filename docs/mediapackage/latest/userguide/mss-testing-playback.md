# Testing MSS playback in AWS Elemental MediaPackage

After creating your MSS endpoint in AWS Elemental MediaPackage, you need to test playback to ensure your
content is properly delivered to viewers. This topic shows you how to test MSS playback
using compatible players and tools. For information about creating MSS endpoints, see [Create an MSS manifest](endpoints-create.md#endpoints-ism "endpoints-create.md#endpoints-ism"). For information about planning
your MSS implementation, see [Planning your MSS implementation](mss-overview.md#mss-features "mss-overview.md#mss-features").

## MSS compatible players

For testing MSS playback, we recommend using the following players:

- **Dash.js Reference Player** (recommended for
  unencrypted content): [https://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html](https://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html "https://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html")

Example URL format:
`https://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html?mpd=https://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest`

- **Castlabs Demo Player** (recommended for
  encrypted content): [https://demo.castlabs.com/](https://demo.castlabs.com/ "https://demo.castlabs.com/")

Use this player for PlayReady encrypted MSS content. The dash.js player might
not work reliably with encrypted MSS streams.

For detailed information about testing encrypted MSS content, see the [MSS DRM Castlabs documentation](https://w.amazon.com/bin/view/AWS/EMPv2/MSS-DRM-Castlabs-Docs-Feedback-Deck "https://w.amazon.com/bin/view/AWS/EMPv2/MSS-DRM-Castlabs-Docs-Feedback-Deck").

MSS is also supported by the following players and platforms:

- Microsoft Silverlight-based players
- Xbox 360 and Xbox One
- Windows Media Player with appropriate extensions
- Certain smart TV models (especially older Samsung and LG models)
- Some set-top boxes that specifically support MSS

When you select a player for testing MSS content, consider the following:

- **Dash.js Reference Player**: Good for general MSS testing and provides diagnostic information about manifest parsing and segment loading.
- **Castlabs Demo Player**: Best for encrypted content testing as it handles PlayReady DRM more reliably than other web-based players.
- **Xbox consoles**: Important for testing if your target audience includes gaming console users. Xbox 360 in particular relies heavily on MSS.
- **Legacy smart TVs**: If targeting older smart TV models, test on actual devices when possible, as their MSS implementations may have specific quirks or limitations.

## Testing procedure

Follow these steps to test your MSS endpoint:

1. Get your MSS endpoint URL from the MediaPackage console. The URL will end with
   .isml.
2. Open the Dash.js Reference Player or Castlabs Demo Player (for encrypted content).
3. Enter your MSS endpoint URL in the player.
4. Verify that playback starts and the content plays smoothly.
5. If your content is encrypted with PlayReady DRM, verify that the player can
   decrypt and play the content.

For a comprehensive test of your MSS implementation, consider these additional testing
steps:

- **Network condition testing**: Test playback
  under various network conditions (bandwidth throttling, packet loss, latency) to
  verify adaptive bitrate switching works correctly.
- **Device compatibility matrix**: Create a
  compatibility matrix of target devices and test on representative samples from
  each category.
- **Long-duration testing**: For live streams,
  conduct extended playback tests (4+ hours) to verify there are no issues with
  manifest updates or segment availability over time.
- **CDN edge case testing**: Test from different
  geographic locations to ensure your CDN configuration works properly across all
  regions.

###### Example Real-world testing scenario: Live sports broadcast

A media company preparing for a major sports tournament implemented the following
testing strategy for their MSS streams:

1. Pre-event testing with simulated content to verify endpoint
   configuration
2. Dress rehearsal with actual live content one week before the event
3. Testing on 5 different device types representing their audience
   demographics
4. Network simulation tests with bandwidth fluctuations to verify adaptive
   bitrate behavior
5. Monitoring setup to track manifest requests, segment delivery, and error
   rates during the event
   This comprehensive approach helped them identify and resolve several issues before
   the live event, including a CDN configuration problem that was causing intermittent
   404 errors for MSS segments.

For information about monitoring your MSS streams during testing and production, see
[Monitoring MSS streams](mss-troubleshooting.md#mss-monitoring-tips "mss-troubleshooting.md#mss-monitoring-tips"). For
information about testing encrypted MSS content, see [Verifying your encrypted MSS streams](mss-encryption.md#mss-encryption-testing "mss-encryption.md#mss-encryption-testing").

## CDN configuration for testing

For production environments, ensure your CDN is properly configured to handle MSS
content:

- Set appropriate cache control headers for both manifests (.isml) and
  segments
- Configure proper MIME types: application/vnd.ms-sstr+xml for manifests and
  video/mp4 for segments
- If using encryption, ensure your CDN is configured to handle PlayReady
  DRM

For detailed CDN configuration instructions specific to MSS, see [CDN configuration for MSS in AWS Elemental MediaPackage](mss-cdn-configuration.md "mss-cdn-configuration.md").

If you encounter issues during testing, see [Troubleshooting MSS endpoints in AWS Elemental MediaPackage](mss-troubleshooting.md "mss-troubleshooting.md") for common problems and solutions.
