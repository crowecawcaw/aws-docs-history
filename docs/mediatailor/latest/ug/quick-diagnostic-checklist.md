# Diagnostic checklist for MediaTailor and CDN

integrations

AWS Elemental MediaTailor content delivery network (CDN) integration problems can manifest in various
ways. Use this checklist to quickly identify the type of issue you're
experiencing:

1. **Is the issue affecting all viewers or specific
   viewers?**
   - All viewers → Likely CDN or MediaTailor configuration issue
   - Specific viewers → Likely personalization or targeting issue

2. **Are manifests loading correctly?**
   - No → CDN routing or MediaTailor connectivity issue
   - Yes, but wrong content → Caching or personalization issue

3. **Are segments loading correctly?**
   - Content segments fail → Origin connectivity issue
   - Ad segments fail → Ad delivery or transcoding issue

4. **Are ads being inserted correctly?**


    * No ads appear → Check ADS connectivity and configuration
    * Wrong ads appear → Check ad targeting parameters and
     personalization
    * Ads fail to play → Check ad transcoding and segment
     availability

436. **Is playback smooth and uninterrupted?**


    * Buffering issues → Check CDN cache performance and origin response
     times
    * Playback errors → Check manifest syntax and segment
     availability
    * Ad transition issues → Check ad break timing and segment
     alignment

437. **Are there specific error codes or
     messages?**


    * HTTP 4xx errors → Check CDN routing and configuration
    * HTTP 5xx errors → Check origin server and MediaTailor service health
    * Player-specific errors → Check manifest format and player
     compatibility

**Next steps based on your diagnosis:**

CDN configuration issues

For detailed CDN routing and caching troubleshooting, see [Troubleshoot issues with MediaTailor and CDN
integration](cdn-troubleshooting.md "cdn-troubleshooting.md").

Manifest and playback issues

For manifest validation and playback troubleshooting, see [CDN integration testing procedures](cdn-testing-procedures.md "cdn-testing-procedures.md").

Ad insertion and targeting issues

For ad-specific troubleshooting including ADS connectivity and ad
delivery, see your workflow-specific troubleshooting documentation.

Performance and monitoring issues

For performance analysis and monitoring setup, see [Monitor MediaTailor CDN operations and performance](cdn-monitoring.md "cdn-monitoring.md").

Log analysis and error codes

For detailed log analysis and error code reference, see [CDN integration log analysis and error code
reference for MediaTailor](cdn-log-error-reference.md "cdn-log-error-reference.md").

Testing and validation

For comprehensive testing procedures, see [Testing and validation
for CDN and MediaTailor integrations](cdn-integration-testing.md "cdn-integration-testing.md").

If you need immediate assistance or cannot resolve the issue using the linked
resources, see [Get support and troubleshooting
help for CDN and MediaTailor integrations](cdn-get-help.md "cdn-get-help.md") for
escalation procedures.
