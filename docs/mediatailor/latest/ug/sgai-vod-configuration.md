# MediaTailor server-guided ad insertion configuration for VOD content

AWS Elemental MediaTailor server-guided ad insertion for VOD content provides significant performance
benefits through highly cacheable manifests and reduced server processing. Configuring SGAI
for VOD content leverages the static nature of video-on-demand assets to maximize caching
efficiency and minimize origin requests, making it ideal for large content libraries with
repeated viewing patterns.

## Requirements for VOD SGAI

Before you enable SGAI for VOD content, ensure that you have the following:

- Your VOD content includes properly formatted ad markers (SCTE-35 or timed metadata)
- Content is stored in a reliable origin with consistent availability
- Your CDN is configured to cache SGAI manifests with appropriate TTL values
- Players support server-guided ad insertion workflows
- Your ad decision server can handle VOD-specific metadata and targeting

### Player requirements

Players must be configured to handle SGAI VOD manifests and ad insertion:

- Support for server-guided ad insertion workflows
- Ability to process ad insertion guidance from VOD manifests
- Support for client-side ad insertion during VOD playback
- Proper handling of seek operations across ad breaks
- Support for content duration and position tracking

## VOD playback configuration

To enable SGAI for VOD content, create a playback configuration that has the
following settings:

###### Example SGAI VOD playback configuration

```

{
  "Name": "VODSGAIConfig",
  "VideoContentSourceUrl": "https://your-vod-origin.com/content/",
  "AdDecisionServerUrl": "https://your-ads.com/ads",
  "PersonalizationThresholdSeconds": 5,
  "InsertionMode": "PLAYER_SELECT"
}

```

The following are key considerations for VOD SGAI configuration:

`VideoContentSourceUrl`

Should point to your VOD content library with consistent URL patterns.
Ensure the origin can handle the expected request volume and provides
reliable content delivery.

`ConfigurationAliases`

Include VOD-specific parameters like content duration, genre, or
series information that can be used for ad targeting without affecting
manifest cacheability.

`ManifestProcessingRules`

Enable ad marker passthrough to preserve original content timing
information, which is especially important for VOD content with
pre-defined ad break positions.

## SGAI VOD manifest requests

SGAI VOD manifests use the same URL pattern traditional VOD ad insertion.

```

https://your-config.mediatailor.region.amazonaws.com/v1/master/config-name/content-path/manifest.m3u8?aws.insertionMode=GUIDED

```

## VOD-specific ad targeting

VOD content enables unique ad targeting opportunities:

### Content metadata targeting

Leverage VOD content metadata for improved ad targeting:

- **Genre and category:** Target ads based
  on content type (drama, comedy, documentary)
- **Content rating:** Ensure age-appropriate
  ad content (G, PG, R ratings)
- **Series and season:** Target ads for
  series continuity or related content
- **Release date:** Target based on content
  age (new releases vs. catalog content)
- **Content duration:** Adjust ad load based
  on total content length

### Viewing context targeting

VOD viewing patterns enable contextual ad targeting:

- **Time of day:** Target ads based on when
  content is being watched
- **Binge watching:** Adjust ad frequency
  for users watching multiple episodes
- **Completion rate:** Target based on
  user's historical content completion patterns
- **Device type:** Optimize ad formats
  for viewing device (TV, mobile, tablet)

## Testing SGAI VOD configuration

Verify your SGAI VOD setup with these validation steps:

1. **Test manifest generation**

Request SGAI VOD manifest URLs for different content types and verify
they return cacheable content with proper ad insertion guidance. 2. **Verify CDN caching**

Check that your CDN is caching SGAI manifests according to the
configured TTL values and achieving high cache hit rates. 3. **Test ad insertion**

Confirm that players can successfully insert ads using the guidance
provided in SGAI manifests for various VOD content. 4. **Test seek operations**

Verify that seeking within VOD content works correctly across ad
breaks and maintains proper playback position. 5. **Monitor performance**

Use CloudWatch metrics to verify reduced origin load, improved cache
hit rates, and successful ad insertion rates.

### Key testing scenarios

Test these specific VOD scenarios:

- **Popular content:** Verify high cache
  hit rates for frequently accessed VOD assets
- **Long-form content:** Test ad insertion
  in movies or long episodes with multiple ad breaks
- **Series content:** Verify consistent
  ad targeting across episodes in a series
- **Different genres:** Test ad targeting
  based on content metadata and genre

## VOD SGAI optimization best practices

Optimize your SGAI VOD implementation for maximum performance:

### Cache optimization

- **Maximize TTL values:** Use longer cache
  durations for VOD manifests since content doesn't change
- **Minimize cache keys:** Reduce cache
  key variations to improve hit rates
- **Pre-warm popular content:** Cache
  manifests for trending or featured VOD content
- **Monitor cache performance:** Track
  cache hit rates and optimize based on usage patterns

### Content delivery optimization

- **Consistent URL patterns:** Use
  predictable URL structures for better caching
- **Metadata standardization:** Ensure
  consistent content metadata for reliable ad targeting
- **Ad break positioning:** Optimize ad
  break placement for natural content transitions
- **Quality variants:** Ensure SGAI works
  across all bitrate variants of your VOD content
