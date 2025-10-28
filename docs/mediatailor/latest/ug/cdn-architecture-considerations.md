# Architecture considerations for

CDN and MediaTailor integrations

Position your content delivery network (CDN) correctly in your architecture to
ensure optimal performance and reliability with AWS Elemental MediaTailor. The recommended
architecture places the CDN between viewers and MediaTailor, not between MediaTailor and your
origin.

For detailed architecture diagrams and workflow explanations, see the following
topics.

- [Ad insertion with CDN](ssai-cdn-workflow.md "ssai-cdn-workflow.md") for ad insertion architecture diagrams and detailed workflow
- [Understand CDN
  architecture](channel-assembly-cdn-architecture.md "channel-assembly-cdn-architecture.md") for channel
  assembly architecture diagrams and workflow
  Position your CDN correctly in your architecture:

1. Place your CDN between players and MediaTailor (not between MediaTailor and your
   origin).

This architecture allows your CDN to cache ad segments and content
segments. At the same time, MediaTailor can generate personalized manifests for
each viewer. 2. Create separate cache behaviors for different request types:

    * Manifest requests (no caching)
    * Content segments (longer TTL)
    * Ad segments (longer TTL)

3. Configure proper error handling:
   - Set up negative caching (temporarily storing error responses) to
     avoid overwhelming your origin with repeated requests during service
     disruptions. Negative caching means the CDN will temporarily store
     error responses (like 404 or 500 errors) to prevent repeated
     requests for content that doesn't exist or is temporarily
     unavailable.
   - Configure appropriate error response codes and retry
     behavior

4. Implement intermediate caching (origin shield):

Origin shield is a feature that creates an additional caching layer
between CDN edge locations and your origin server. This reduces the number
of redundant requests that reach your origin server.

    * Configure an intermediate caching layer between edge locations and
     your origin
    * Reduce the number of redundant requests to your origin during
     cache misses
    * Improve cache hit ratios across your CDN infrastructure
