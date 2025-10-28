# Testing tools and

utilities reference for CDN and MediaTailor integrations

AWS Elemental MediaTailor content delivery network (CDN) integration testing requires various tools for comprehensive validation
and debugging. Reference guide for tools commonly used in content delivery network and MediaTailor integration
testing.

`curl` - HTTP request testing

Test manifest requests: `curl -v "https://your-cdn-domain.com/v1/master/hls/config/master.m3u8"`

Test with headers: `curl -H "User-Agent: TestAgent/1.0" "https://your-cdn-domain.com/..."`

Test with parameters: `curl "https://your-cdn-domain.com/...?aws.sessionId=test123"`

`ffprobe` - HLS manifest validation

Validate HLS syntax: `ffprobe -v quiet -print_format json -show_format "https://your-cdn-domain.com/master.m3u8"`

Check segment information: `ffprobe -v quiet -show_entries packet=pts_time "segment.ts"`

`mp4box` - DASH manifest validation

Validate DASH MPD: `mp4box -info "https://your-cdn-domain.com/manifest.mpd"`

Check segment timing: `mp4box -info segment.m4s`

Browser developer tools

Monitor network requests in the Network tab

Check for CORS errors in the Console tab

Inspect request/response headers

Analyze timing and performance metrics

**Additional resources:**

- [Troubleshooting CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/Troubleshooting.md "../../../AmazonCloudFront/latest/DeveloperGuide/Troubleshooting.md") - Comprehensive CDN troubleshooting
  guide
- [Increase
  CloudFront cache hit ratio](../../../AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.md "../../../AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.md") - Performance optimization
  guidance
- [Monitor AWS resources](../../../wellarchitected/latest/performance-efficiency-pillar/monitor-aws-resources.md "../../../wellarchitected/latest/performance-efficiency-pillar/monitor-aws-resources.md") - Performance monitoring best
  practices
