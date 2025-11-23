# Caching optimization for CDN and MediaTailor

integrations

AWS Elemental MediaTailor caching requirements vary by workflow type and content format. Proper
caching configuration is critical for optimal performance, cost efficiency, and viewer
experience. The following sections provide detailed caching guidance for different MediaTailor
implementations.

## Server-side ad insertion (SSAI)

caching

For server-side ad insertion workflows, personalized manifests cannot be cached,
but content and ad segments should be cached aggressively:

| SSAI CDN caching settings | Content type | TTL                    | Path pattern                    | Cache key elements |
| ------------------------- | ------------ | ---------------------- | ------------------------------- | ------------------ |
| Multivariant playlists    | 0 seconds    | /v1/master/\*          | URL path + all query parameters |
| Media playlists           | 0 seconds    | /v1/manifest/\*        | URL path + all query parameters |
| DASH MPDs                 | 0 seconds    | /v1/dash/\*            | URL path + all query parameters |
| Content segments          | 24+ hours    | Content-specific paths | URL path only                   |
| Ad segments               | 24+ hours    | /v1/segment/\*         | URL path only                   |

- Set TTL of 0 seconds for personalized manifests to ensure viewers receive
  up-to-date ad content
- Configure longer TTL values for content and ad segments to maximize cache
  efficiency
- Set up cache behaviors that include personalization parameters in the
  cache key if you support targeted advertising
- Implement request collapsing at the CDN level to efficiently handle
  concurrent requests

### Recommended TTL configuration

settings

For optimal SSAI performance, configure your CDN cache policies with these
specific TTL settings:

| SSAI TTL configuration settings | Content type | TTL setting              | Recommended value |
| ------------------------------- | ------------ | ------------------------ | ----------------- |
| Ad segments                     | Min TTL      | 1 second                 |
| Ad segments                     | Max TTL      | 86400 seconds (24 hours) |
| Ad segments                     | Default TTL  | 86400 seconds (24 hours) |
| Content segments                | Min TTL      | 1 second                 |
| Content segments                | Max TTL      | 86400 seconds (24 hours) |
| Content segments                | Default TTL  | 86400 seconds (24 hours) |

These settings ensure:

- **Min TTL of 1 second**: Allows for rapid
  cache invalidation when needed while preventing excessive origin
  requests
- **Max TTL of 24 hours**: Balances cache
  efficiency with content freshness requirements
- **Default TTL of 24 hours**: Provides
  optimal caching for segments that don't have explicit cache-control
  headers

## Server-guided ad insertion (SGAI)

caching

Server-guided ad insertion (SGAI) enables efficient CDN caching through cacheable
media manifests that use predictable URL patterns. This section focuses on CDN-specific
configuration requirements for optimal SGAI performance.

### CDN caching configuration for

SGAI

Configure your CDN with these SGAI-specific caching behaviors:

| SGAI CDN caching settings                  | Content type                      | TTL                  | Path pattern                         | Cache key elements |
| ------------------------------------------ | --------------------------------- | -------------------- | ------------------------------------ | ------------------ |
| SGAI multivariant playlists (do not cache) | 0 seconds (do not cache)          | /v1/master/\*        | URL path + selected query parameters |
| SGAI media playlists                       | 1-4 seconds (half segment length) | /v1/i-media/\*       | URL path + selected query parameters |
| Asset list responses (do not cache)        | 0 seconds (do not cache)          | /v1/interstitials/\* | URL path + all query parameters      |
| Ad segments                                | 24+ hours                         | Ad-specific paths    | URL path only                        |

### Cache behavior configuration

Set up dedicated cache behaviors for SGAI content:

- **SGAI manifest behavior** - Create a
  cache behavior for `/v1/i-media/*` paths with 1-4 second
  TTL
- **Asset list behavior** - Create a cache
  behavior for `/v1/interstitials/*` paths with 0 second
  TTL
- **Query parameter handling** - Include
  only essential targeting parameters in cache keys to maximize cache
  efficiency
- **Origin request headers** - Forward
  necessary headers for ad targeting while maintaining cacheability

## Channel assembly

caching

For channel assembly workflows, manifests can be cached for short periods, while
segments should be cached aggressively:

| Channel assembly CDN caching settings | Content type | VOD TTL      | Live TTL               | Path pattern                    | Cache key elements |
| ------------------------------------- | ------------ | ------------ | ---------------------- | ------------------------------- | ------------------ |
| Multivariant playlists                | 5-30 minutes | 5-10 seconds | Channel-specific paths | URL path + all query parameters |
| Media playlists                       | 5-30 minutes | 2-5 seconds  | Channel-specific paths | URL path + all query parameters |
| DASH MPDs                             | 5-30 minutes | 5-10 seconds | Channel-specific paths | URL path + all query parameters |
| Content segments                      | 24+ hours    | 5-15 minutes | Content-specific paths | URL path only                   |
| Ad segments                           | 24+ hours    | 24+ hours    | Ad-specific paths      | URL path only                   |

- Set short TTL values for manifests to ensure viewers receive up-to-date
  programming
- Configure longer TTL values for content segments to maximize cache
  efficiency
- Set up cache behaviors that include time-shift parameters in the cache key
  if you support time-shifted viewing
- Include query parameters in the cache key to properly handle time-shifted
  viewing requests

For detailed TTL configuration settings and best practices, see [Caching optimization for CDN and MediaTailor
integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

## Combined SSAI and channel assembly

caching

When implementing both channel assembly and SSAI, ensure your caching strategy is
consistent for both services to avoid conflicts and optimize performance:

| Combined workflow caching settings comparison | Content type | Channel assembly | SSAI                               | Combined recommendation |
| --------------------------------------------- | ------------ | ---------------- | ---------------------------------- | ----------------------- |
| VOD manifests                                 | 5-30 minutes | 0 seconds        | (use a separate config)            |
| Live manifests                                | 2-10 seconds | 0 seconds        | (use a separate config)            |
| SGAI VOD manifests                            | 5-30 minutes | 5-30 minutes     | 5-30 minutes (cacheable manifests) |
| SGAI Live manifests                           | 2-4 seconds  | 2-4 seconds      | 2-4 seconds (cacheable manifests)  |
| Content segments                              | 24+ hours    | 24+ hours        | 24+ hours (consistent)             |
| Ad segments                                   | 24+ hours    | 24+ hours        | 24+ hours (consistent)             |

This configuration maximizes cache efficiency while ensuring viewers receive
up-to-date manifests for personalized ad insertion.
