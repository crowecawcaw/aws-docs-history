# Fix CDN inconsistent behavior across

devices and platforms for MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) integration should provide consistent ad
delivery across all devices and platforms. If ads behave differently across
devices:

1.  Ensure consistent header forwarding across all CDN behaviors.
    - Verify that User-Agent, X-Forwarded-For, and custom targeting headers
      are forwarded consistently
    - Check that header forwarding rules apply to all relevant cache
      behaviors

2.  Verify player compatibility with your CDN configuration.
    - Test with multiple player types (HLS.js, Video.js, native players) to
      identify player-specific issues
    - Check for player-specific header requirements or URL handling
      differences

3.  Test with multiple device types to identify device-specific issues.

        * Include mobile devices, tablets, smart TVs, and desktop browsers in
         your testing
        * Test different operating systems and browser versions
        * Verify that device-specific ad targeting works correctly

    If you've followed these troubleshooting steps and still need assistance, see [Get CDN integration support](cdn-get-help.md "cdn-get-help.md").
