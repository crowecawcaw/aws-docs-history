# Troubleshoot issues with MediaTailor and CDN

integration

This comprehensive troubleshooting guide covers common content delivery network (CDN)
integration issues across all AWS Elemental MediaTailor implementations including server-side ad insertion
(SSAI), channel assembly, and AWS Elemental MediaPackage integration. When your CDN and MediaTailor integration
experiences problems, use this systematic diagnostic approach to quickly identify root
causes and implement validated solutions.

This guide applies to all MediaTailor CDN integrations regardless of your specific workflow. For
issues specific to particular services or workflows, see the related troubleshooting
sections referenced at the end of this guide.

**Before you begin:** Have these items ready for efficient
troubleshooting:

- Sample playback URLs that demonstrate the issue
- CDN access logs from the time period when issues occurred
- MediaTailor configuration name and AWS Region
- Player type and version (for example, HLS.js 1.4.0, Video.js 8.0)
- Device and browser information where issues occur
  **Related topics:**

- For operational setup and troubleshooting preparation, see Troubleshoot CDN integration
- For log analysis and error code reference, see [CDN integration log analysis
  reference](cdn-log-error-reference.md "cdn-log-error-reference.md")
- For escalation and getting additional help, see [Get CDN integration support](cdn-get-help.md "cdn-get-help.md")

## Troubleshooting preparation

Set up tools and processes to simplify troubleshooting when CDN integration issues
arise. Proactive preparation makes troubleshooting faster and more effective when issues
occur.

### Enable comprehensive logging

Detailed logs are essential for diagnosing CDN integration issues. Configure
logging to capture the information you'll need during troubleshooting.

1. Enable detailed CDN access logs:
   - Configure logging for all cache behaviors that handle MediaTailor
     requests
   - Include query strings and custom headers in log entries
   - Set up log analysis tools to identify patterns and
     anomalies
   - Enable real-time logs for immediate issue detection during live
     events
   - Configure log retention policies to maintain historical
     troubleshooting data

2. Configure MediaTailor logging:
   - Enable access logs for your MediaTailor configurations
   - Set up CloudWatch log groups for centralized log management
   - Configure log filters to identify error patterns

3. Set up origin server logging:
   - Enable detailed access logs on your content origin servers
   - Include request headers and response codes in logs
   - Monitor origin server performance metrics

### Add diagnostic request headers

Custom headers help track requests through your CDN and identify routing
issues.

1. Configure CDN diagnostic headers:
   - Add a unique identifier to each request (for example,
     `X-Request-ID`)
   - Include CDN-specific information in request headers
   - Add edge location or POP (point of presence) information to track
     geographic routing
   - Include cache status headers (Hit, Miss, RefreshHit) for cache
     behavior analysis

2. Add response headers for debugging:
   - Include server identification headers
   - Add timing information for performance analysis
   - Include cache control headers for manifest requests

### Establish baseline performance

metrics

Document normal performance ranges to quickly identify anomalies during
troubleshooting:

1. **Record baseline metrics**:
   - Cache hit ratios for different content types
   - Response time percentiles (P50, P95, P99)
   - Error rates by status code
   - Request volume patterns by time of day

2. **Document performance expectations**:
   - Target cache hit ratios (95%+ for content, 90%+ for ads)
   - Acceptable response times (<100ms cached, <500ms
     origin)
   - Maximum acceptable error rates (<1% for 4xx, <0.1% for
     5xx)

3. **Create performance dashboards**: Set up
   monitoring dashboards that show current metrics compared to baseline
   values.

### Prepare troubleshooting

tools

Set up tools and access permissions needed for effective troubleshooting:

1. **Command-line tools**:
   - `curl` for testing HTTP requests and responses
   - `dig` or `nslookup` for DNS
     troubleshooting
   - HLS/DASH validation tools for manifest verification
   - Log analysis tools (grep, awk, or specialized log
     analyzers)

2. **Access permissions**:
   - CDN management console access for configuration review
   - MediaTailor console access for configuration verification
   - CloudWatch access for metrics and log analysis
   - Origin server access for backend troubleshooting

3. **Documentation**:
   - Network architecture diagrams
   - CDN and MediaTailor configuration documentation
   - Contact information for escalation procedures
   - Troubleshooting runbooks for common scenarios

## Workflow-specific troubleshooting

guides

This universal troubleshooting guide covers common issues across all MediaTailor CDN
integrations. For issues specific to particular workflows or services, consult these
specialized troubleshooting resources:

Server-side ad insertion (SSAI) troubleshooting

For SSAI-specific issues including ad insertion failures, ad transition
problems, and personalization issues, see workflow-specific SSAI
troubleshooting documentation.

**Common SSAI-specific issues**:

- Ad insertion failures and empty ad breaks
- Ad transition timing and synchronization problems
- Personalization and targeting issues
- Ad tracking and analytics discrepancies

Channel assembly troubleshooting

For channel assembly-specific issues including manifest generation
problems and time-shift functionality, see channel assembly workflow
documentation.

**Common channel assembly issues**:

- Manifest generation and compilation errors
- Time-shift window and DVR functionality problems
- Source content availability and failover issues
- Program schedule and metadata synchronization

MediaPackage integration troubleshooting

For MediaPackage specific issues including manifest filtering and EMP
endpoint problems, see [CDN integration
troubleshooting](cdn-emp-troubleshooting.md "cdn-emp-troubleshooting.md").

**Common MediaPackage integration issues**:

- Manifest filtering parameter errors
- MediaPackage endpoint connectivity issues
- EMP-specific cache behavior problems
- MediaPackage origin authentication issues

CloudFront specific troubleshooting

For CloudFront specific configuration and setup issues, see CloudFront
integration documentation.

**Common CloudFront issues**:

- Distribution configuration and cache behavior setup
- Origin access identity and security configuration
- CloudFront specific error codes and responses
- Geographic restrictions and edge location issues

**Additional resources**:

- For performance optimization guidance, see [CDN performance optimization](cdn-optimization.md "cdn-optimization.md")
- For monitoring and alerting setup, see [CDN monitoring](cdn-monitoring.md "cdn-monitoring.md")
- For general support and assistance, see [Get CDN integration support](cdn-get-help.md "cdn-get-help.md")
