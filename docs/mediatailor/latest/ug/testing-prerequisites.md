# Testing prerequisites and

setup for CDN and MediaTailor integrations

AWS Elemental MediaTailor content delivery network (CDN) integration testing requires proper preparation and resource allocation.
Before beginning systematic testing, ensure you have the necessary resources and tools
in place.

**Required resources:**

- Test CDN distribution configured to mirror production settings
- Test MediaTailor configuration with known content and ad sources
- Test content with predictable characteristics (duration, format, ad break markers)
- Test ad decision server or mock ADS responses
- Multiple test devices and player types
  **Testing tools:**

- `curl` for HTTP request testing
- `ffprobe` for HLS manifest validation
- `mp4box` for DASH manifest validation
- Browser developer tools for network analysis
- Video players for end-to-end testing
