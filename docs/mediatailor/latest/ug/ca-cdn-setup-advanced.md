# Implement MediaTailor ad insertion with channel

assembly

Channel assembly in AWS Elemental MediaTailor integrates seamlessly with server-side ad insertion
(SSAI) and content delivery networks (CDNs) to create monetized linear channels with
personalized advertising.

When you combine channel assembly with SSAI, you can build linear channels that
deliver personalized ads to viewers while maintaining broadcast-quality experiences.
This integration enables you to do the following:

- Monetize content - Generate revenue through targeted advertising in your
  linear channels
- Personalize experiences - Deliver different ads to viewers watching the same
  channel based on their profiles
- Maintain quality - Ensure seamless transitions between content and ads for
  broadcast-quality viewing
- Scale efficiently - Support millions of concurrent viewers through CDN
  delivery
  For detailed information about SSAI with CDNs, see [Ad insertion with CDN](ssai-cdn-workflow.md "ssai-cdn-workflow.md").

1. Configure your edge CDN to accept manifest requests from viewers and forward
   them to MediaTailor ad insertion.
2. Set up MediaTailor ad insertion to forward requests to your origin CDN.
3. Configure your origin CDN to forward requests to MediaTailor channel
   assembly.
4. Set up MediaTailor channel assembly to generate dynamic manifests based on the
   current schedule.
5. Configure your origin CDN to forward the assembled manifests to MediaTailor ad
   insertion.
6. Set up MediaTailor ad insertion to request ad decisions from your ad decision server
   at ad break points.
7. Configure MediaTailor ad insertion to personalize manifests with ad markers.
8. Set up your edge CDN to deliver personalized manifests to viewers.
9. Configure your CDN architecture to handle both content and ad segment requests
   efficiently.
   The following diagram illustrates this combined workflow:

![Diagram showing CDN integration with both channel assembly and ad insertion](/images/mediatailor/latest/ug/images/ca-ssai-comb-cdn.png)
For optimal performance when combining channel assembly and SSAI:

- Configure cache behaviors that distinguish between channel assembly and SSAI
  requests
- Set appropriate TTL values for manifests and segments as recommended in [Caching optimization for CDN and MediaTailor
  integrations](cdn-optimize-caching.md "cdn-optimize-caching.md")
- Ensure proper routing between channel assembly, ad insertion, and your CDN
  origins
- Monitor the performance metrics for both channel assembly and ad insertion
  components
  For detailed information about configuring SSAI with CDNs, see:

- [Understand ad insertion architecture for CDN and MediaTailor integrations](ssai-cdn-architecture-overview.md "ssai-cdn-architecture-overview.md") - Learn about SSAI
  architecture and concepts
- [Set up basic MediaTailor SSAI with a CDN for optimal ad
  delivery](configuring-ssai-cdn.md "configuring-ssai-cdn.md") -
  Step-by-step SSAI configuration instructions
- [Troubleshoot MediaTailor SSAI with CDNs for
  uninterrupted ad delivery](troubleshooting-ssai-cdn.md "troubleshooting-ssai-cdn.md") - Troubleshoot common SSAI
  integration issues
