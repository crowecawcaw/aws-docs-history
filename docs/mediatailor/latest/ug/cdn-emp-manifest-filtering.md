# Set up manifest filtering with MediaTailor, MediaPackage,

and CDN

AWS Elemental MediaTailor uses manifest filtering with AWS Elemental MediaPackage to customize which audio and video streams are included in manifests delivered to different viewers through a content delivery network (CDN). This is particularly useful for implementing tiered service offerings, device-specific optimizations, or content access controls.

This topic focuses specifically on implementing manifest filtering features. Before
implementing manifest filtering, you must complete the basic content delivery network integration setup. If you
haven't set up your basic MediaPackage and content delivery network integration yet, start with [Integrate MediaTailor with MediaPackage and CDN](mediapackage-integration.md "mediapackage-integration.md") .

## Manifest filtering capabilities

Before implementing manifest filtering, understand what you can accomplish with this feature:

### Core filtering capabilities

Manifest filtering provides several key capabilities that help you control content
delivery:

- Restrict viewer access to premium content (such as 4K HEVC)
- Target specific device types with appropriate streams
- Filter content based on audio sample rates, languages, or video
  codecs
- Deliver different quality tiers to different subscribers

### Common use cases

These use cases demonstrate how manifest filtering can address specific business
requirements:

**Subscription tiers**

Offer basic subscribers lower resolution streams while providing
premium subscribers access to 4K content

Example: Basic tier limited to 720p, Premium tier gets up to 4K

**Device optimization**

Automatically serve appropriate streams based on device
capabilities

Example: Mobile devices get lower bitrates, smart TVs get higher
quality

**Bandwidth management**

Limit stream quality during peak usage periods to manage network
costs

Example: Reduce maximum bitrate during high-traffic events

**Regional content**

Serve different audio languages or content variants based on viewer
location

Example: Automatically filter for local language audio tracks

For more information about manifest filtering concepts, see [Manifest filtering](../../../mediapackage/latest/ug/manifest-filtering.md "../../../mediapackage/latest/ug/manifest-filtering.md") in the AWS Elemental MediaPackage user guide.

## Configure your CDN for manifest

filtering

CDN configuration for manifest filtering is essential because your CDN must forward
the `aws.manifestfilter` query parameter to MediaPackage for filtering to work.
Without proper query string forwarding, filter parameters will be stripped by the CDN,
and all viewers will receive unfiltered manifests regardless of their subscription tier
or device capabilities. This configuration ensures that your filtering logic reaches
MediaPackage and functions as intended.

To enable manifest filtering through your CDN, you need to configure query string
forwarding:

1. In your CloudFront distribution, create or edit the cache behavior for manifest
   requests.
2. For **Cache policy,** create a new policy or edit an existing
   one.
3. Under **Cache key settings**, choose "Include specified query
   strings."
4. Add `aws.manifestfilter` to the list of allowed query
   strings.
5. If you're also using other MediaPackage features, add their query parameters:
   - `start` and `end` - For time-shifted
     viewing
   - `time_delay` - For time delay functionality
   - `_HLS_msn` and `_HLS_part` - For LL-HLS

For more information about creating distributions, see [Create a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.md") in the Amazon CloudFront developer guide.

## Implement client-side

filtering

Client-side implementation is where you define how your video players and applications
request filtered content. This configuration determines what content each viewer
receives based on their subscription level, device capabilities, or other criteria.
Proper implementation ensures that viewers receive only the content they should have
access to, while maintaining optimal CDN cache efficiency.

To implement manifest filtering in your video players and applications:

### How filtering works

The filtering process works as follows:

1. Your video player or application requests a manifest URL that includes
   filter parameters
2. The CDN forwards the request (including query parameters) to MediaTailor
3. MediaTailor passes the filter parameters to MediaPackage when requesting the origin
   manifest
4. MediaPackage applies the filters and returns a customized manifest containing
   only the variants that match your criteria
5. MediaTailor processes the filtered manifest for ad insertion and returns it to
   the player

### URL format for filtering

Understanding the correct URL format is critical for successful filtering
implementation. Incorrect URL formatting will result in filtering parameters being
ignored or causing HTTP errors. The URL structure must include filter parameters as
query strings that your CDN forwards to MediaPackage. Follow these steps to implement
proper URL formatting:

To implement manifest filtering in your video players:

1. Modify your player's manifest request URLs to include the appropriate
   filter parameters.
2. Use the following URL format with query parameters:

```
https://`CloudFront-Domain`/v1/master/`MediaTailor-Config`/index.m3u8?aws.manifestfilter=video_codec:h264;audio_language:en-US
```

3. When your player requests this URL, MediaTailor will pass these parameters to
   MediaPackage, resulting in a filtered manifest.

## Common filtering scenarios

Use these examples to implement common filtering scenarios:

**Device-specific content delivery**

To filter based on device capabilities, add this parameter to your manifest request:

```
aws.manifestfilter=video_codec:h264;audio_sample_rate:0-44100
```

This example limits content to H.264 video and audio with sample rates up to 44.1 kHz, suitable for mobile devices.

**Premium content restriction**

To limit access to high-bitrate content, add this parameter to your manifest request:

```
aws.manifestfilter=video_bitrate:0-9000000
```

This example restricts video bitrates to 9 Mbps or lower, suitable for basic subscription tiers.

**Language selection**

To filter for specific audio languages, add this parameter to your manifest request:

```
aws.manifestfilter=audio_language:fr,en-US,de
```

This example includes only French, US English, and German audio tracks.

**Resolution targeting**

To filter for specific video resolutions, add this parameter to your manifest request:

```
aws.manifestfilter=video_height:240-360,720-1080
```

This example includes video streams with heights between 240-360 pixels and 720-1080 pixels, excluding mid-range resolutions.

**Codec-based filtering**

To filter for specific video codecs, add this parameter to your manifest request:

```
aws.manifestfilter=video_codec:h264,h265
```

This example includes only H.264 and H.265 video streams, excluding other codecs.

## Special considerations and limitations

To avoid common issues when implementing manifest filtering:

### Technical limitations

- For TS manifests, use audio rendition groups to avoid removing video streams that are multiplexed with filtered-out audio streams
- In TS and CMAF manifests, audio sample rate and video bitrate are not easily visible in the manifest for verification
- Request parameters appended to media playlists or segments will result in
  an HTTP 400 error

### Error conditions

- If filtering results in an empty manifest (no streams meet the filter criteria), MediaPackage will return an HTTP 400 error
- Conflicting filter configurations (endpoint filters + query parameters) result in HTTP 404 errors
- Invalid filter syntax or unsupported filter types result in HTTP 400 errors

### Performance considerations

- Each unique filter combination creates a separate cache entry, potentially reducing cache efficiency
- Complex filters with many criteria might impact manifest generation
  performance
- Consider using endpoint-level filters for static filtering scenarios to improve cache performance

## Test your filtering implementation

Testing your manifest filtering implementation is crucial to ensure that viewers
receive the correct content based on their access level and device capabilities. Failed
filtering can result in viewers receiving incorrect quality levels, unsupported formats,
or content they shouldn't have access to. Comprehensive testing helps identify and
resolve these issues before they affect your viewers.

To verify that your manifest filtering is working correctly:

1. Request manifests with different filter parameters and verify the
   results
2. Check that filtered manifests contain only the expected streams
3. Test edge cases (empty results, invalid filters) to ensure proper error
   handling
4. Verify that your CDN is properly forwarding filter parameters
5. Test with different devices and players to ensure compatibility

For troubleshooting filtering issues, see _Troubleshoot MediaPackage CDN integration
issues_.

If you encounter HTTP 400 errors, empty manifests, or filtering parameters that don't
work as expected, see [Troubleshoot MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-troubleshooting.md "cdn-emp-troubleshooting.md") for specific manifest filtering
troubleshooting guidance.
