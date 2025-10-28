# Using a CDN to optimize MediaTailor ad personalization and

content delivery

AWS Elemental MediaTailor works effectively as a standalone service, but integrating it with a content
delivery network (CDN), such as Amazon CloudFront or other third-party CDNs, can significantly
enhance your streaming workflows. A CDN integration is particularly valuable when you need
to serve content to a large, geographically distributed audience or when you want to ensure
consistent ad delivery across different AWS Regions.

Without a CDN, your viewers connect directly to MediaTailor for personalized manifests and ad
segments, which can lead to increased latency, especially for viewers located far from the
AWS Region where your MediaTailor configuration is deployed. Additionally, during high-traffic
events, direct connections to MediaTailor might experience increased load, potentially affecting
performance.

For more information about MediaTailor concepts and workflows, see [What is AWS Elemental MediaTailor?](what-is.md "what-is.md").

When integrating a CDN with MediaTailor, it's important to configure proper CORS (Cross-Origin
Resource Sharing) handling to prevent issues that which can cause playback failures in
web-based players. Proper CORS configuration is essential for both ad segments and content
segments. While ad segments are more susceptible to CORS issues, applying consistent CORS
handling across all segment types ensures the most reliable playback experience. For
detailed guidance on configuring CDN routing behaviors with proper CORS handling, see [Production-ready CloudFront configuration for
MediaTailor](cf-comprehensive-configuration.md "cf-comprehensive-configuration.md").

CDN integration also enables advanced parameter passing and dynamic routing capabilities.
For information about passing query parameters through CDNs for authorization and routing,
see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").
For dynamic ad server and origin routing using configuration aliases, see [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").

Placing a CDN between your viewers and MediaTailor provides the following benefits:

- Reduce latency by serving content from edge locations closer to viewers
- Improve scalability by distributing load across the CDN's global
  infrastructure
- Enhance reliability through redundant delivery paths
- Optimize costs by reducing origin traffic
- Implement advanced features like Media Quality-Aware Routing (MQAR) for improved
  streaming quality

###### Topics

- [CDN selection](cdn-selection-guidance.md "cdn-selection-guidance.md")
- [Plan CDN integration](planning-cdn-integration.md "planning-cdn-integration.md")
- [Set up CDN integration](cdn-configuration.md "cdn-configuration.md")
- [Ad insertion with CDN](ssai-cdn-workflow.md "ssai-cdn-workflow.md")
- [Channel assembly with CDN](ca-cdn-wflw.md "ca-cdn-wflw.md")
- [MediaPackage CDN integration](mediapackage-integration.md "mediapackage-integration.md")
- [CloudFront
  integration](cloudfront-specific-recommendations.md "cloudfront-specific-recommendations.md")
- [Third-party CDN setup](cdn-provider-specific.md "cdn-provider-specific.md")
- [CDN performance optimization](cdn-optimization.md "cdn-optimization.md")
- [CDN monitoring](cdn-monitoring.md "cdn-monitoring.md")
- [CDN integration testing](cdn-integration-testing.md "cdn-integration-testing.md")
- [Troubleshoot CDN integration](cdn-troubleshooting.md "cdn-troubleshooting.md")
- [CDN integration log analysis
  reference](cdn-log-error-reference.md "cdn-log-error-reference.md")
- [AWS CloudFormation automation](automating-cdn-integration.md "automating-cdn-integration.md")
- [Production CloudFront
  configuration](cf-comprehensive-configuration.md "cf-comprehensive-configuration.md")
- [Get CDN integration support](cdn-get-help.md "cdn-get-help.md")
