# Troubleshoot common issues for CDN and MediaTailor integrations

Address common content delivery network (CDN) integration challenges with AWS Elemental MediaTailor before they impact your viewers. This
section helps you identify and resolve typical issues that occur during CDN integration
with AWS Elemental MediaTailor.

For comprehensive troubleshooting guidance, see [Troubleshooting MediaTailor](troubleshooting.md "troubleshooting.md") and [Troubleshooting CloudFront distributions](../../../AmazonCloudFront/latest/DeveloperGuide/troubleshooting.md "../../../AmazonCloudFront/latest/DeveloperGuide/troubleshooting.md").

## Resolving MediaTailor manifest delivery problems

If viewers experience playback issues or see incorrect ads, check these common
manifest-related problems:

- **Incorrect caching settings**: If your CDN
  caches personalized manifests, viewers may see ads intended for other
  users.

Solution: Configure your CDN with a cache TTL of 0 for manifest requests
to MediaTailor.

- **Origin request failures**: If your CDN
  can't reach MediaTailor, then manifest requests will fail.

Solution: Check network connectivity between your CDN and MediaTailor. Verify
your CDN properly forwards the correct headers.

- **Session parameter issues**: Missing or
  incorrect session parameters can cause personalization failures.

Solution: Ensure that your player is correctly appending all required
session parameters to the manifest requests.

## Fixing MediaTailor segment delivery problems

If content or ad segments aren't loading properly, investigate these common
issues:

- **Segment path rewriting**: Incorrect CDN
  configuration may rewrite segment URLs improperly.

Solution: Verify your CDN correctly handles segment URLs. Ensure it
doesn't modify paths in a way that breaks references.

- **CORS configuration**: Missing or incorrect
  CORS headers can prevent browsers from loading segments.

Solution: Configure your CDN to pass the appropriate CORS headers for
segment requests.

- **Cache miss storms**: During high-traffic
  events, multiple cache misses can overwhelm origin servers.

Solution: Implement request collapsing and origin shield capabilities to
reduce origin load during traffic spikes.

## Addressing MediaTailor CDN performance

problems

If viewers experience buffering or slow loading, check these performance-related
issues:

- **Low cache hit ratio**: If your CDN
  frequently requests content from the origin, then performance will
  suffer.

Solution: Analyze the cache hit ratios by content type and adjust the TTL
settings to improve caching efficiency.

- **Geographic distribution**: Viewers distant
  from CDN edge locations may experience increased latency.

Solution: Review your CDN edge location distribution. Add capacity in
regions with high viewer concentrations.

- **Origin capacity limitations**: If your
  origin servers are overloaded, then response times will increase.

Solution: Implement origin request limiting. You can also increase origin
capacity or improve caching to reduce origin load.

For additional troubleshooting assistance, see [Troubleshooting MediaTailor](troubleshooting.md "troubleshooting.md") or contact AWS Support. For implementation
guidance on resolving common CDN issues, see [Debugging your content delivery network](https://aws.amazon.com/blogs/media/debugging-your-content-delivery-network/ "https://aws.amazon.com/blogs/media/debugging-your-content-delivery-network/") on the AWS Media Blog.
