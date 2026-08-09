# CloudFront for e-commerce and marketplace applications

An e-commerce or marketplace application serves three distinct content types through a
single CloudFront distribution: static assets (product images, CSS, JavaScript), dynamic pages
(product listings, search results), and API responses (cart, inventory, pricing). Each
content type requires different cache behavior, TTL, and origin configuration to balance
freshness against performance.

## Architecture overview

A marketplace CloudFront distribution uses multiple cache behaviors to route requests to the
correct origin based on URL path patterns. Static assets are served from Amazon Simple Storage Service (Amazon S3), while
dynamic content and API requests are forwarded to an Elastic Load Balancing (Application Load Balancer)
in front of your application servers. An Porting Assistant for .NET (Valkey) cluster provides an application-level
cache between the ALB and your database for frequently accessed product data.

Distribution architecture components| Component | Content served | Purpose |
| --- | --- | --- |
| CloudFront distribution | All content (single domain) | Global edge caching, TLS termination, request routing via cache behaviors |
| Amazon S3 origin (static assets) | Product images, CSS, JS, fonts | Durable object storage with origin access control (OAC). Immutable content<br>with long TTLs. |
| ALB origin (dynamic content) | Product pages, search, API endpoints | Routes to application servers. Short TTLs or no caching for personalized<br>content. |
| Porting Assistant for .NET cluster (Valkey) | Product catalog, inventory counts, session data | Application-level cache between ALB and database. Sub-millisecond reads<br>for frequently accessed data. |

## Cache behaviors for e-commerce

Cache behaviors determine how CloudFront handles requests based on URL path patterns.
For a marketplace, configure separate behaviors for each content type with appropriate
cache policies and TTLs.

Recommended cache behaviors| Path pattern | Origin | TTL | Cache policy | Rationale |
| --- | --- | --- | --- | --- |
| `/static/*` | Amazon S3 | 365 days | CachingOptimized | Versioned filenames (e.g., `app.a1b2c3.js`) allow maximum<br>TTL. Cache invalidation is never needed — deploy new versions with new filenames. |
| `/images/*` | Amazon S3 | 30 days | CachingOptimized | Product images change infrequently. Use cache-tag invalidation when a<br>seller updates an image. Lower TTL than static assets since image URLs may be reused. |
| `/api/products/*` | ALB | 60 seconds | Custom (include query strings) | Product listing and search APIs change frequently but tolerate brief<br>staleness. Include query string parameters in the cache key for pagination and<br>filters. |
| `/api/cart/*` | ALB | 0 (no cache) | CachingDisabled | Cart operations are user-specific and must always reach the origin.<br>Disable caching entirely. |
| `/api/inventory/*` | ALB | 5 seconds | Custom (include query strings) | Inventory counts change rapidly during sales events. Very short TTL<br>prevents overselling while reducing origin load. |
| `Default (*)` | ALB | 0 (no cache) | CachingDisabled | Default behavior forwards uncached requests to the application for<br>server-side rendering. Pages that include personalized content (recommendations,<br>user name) shouldn't be cached at the edge. |

###### Note

Order cache behaviors from most specific to least specific. CloudFront evaluates path
patterns in the order listed and uses the first match. Place `/api/cart/*`
before `/api/*` to ensure cart requests bypass caching.

For more information about cache behaviors, see
[Cache behavior settings](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md").

## TTL strategy for marketplace content

TTL configuration determines how long CloudFront serves cached content before checking the
origin for updates. E-commerce applications require different TTL strategies depending on
how content freshness affects the customer experience.

**Immutable assets (CSS, JS, fonts)**

Set the maximum TTL (365 days). Use content-hashed filenames so each deployment
creates new URLs. Never invalidate — old versions expire naturally as users load
the new filenames. Set `Cache-Control: public, max-age=31536000, immutable`
at the origin.

**Product images**

Set TTL to 30 days with cache-tag invalidation on update. When a seller uploads
a new image, invalidate by the product's cache tag rather than by path. This targets
only the affected objects without broad wildcard invalidation. Set
`Cache-Control: public, max-age=2592000` at the origin.

**Product catalog API**

Set TTL to 60 seconds. Product listings, descriptions, and pricing tolerate
brief staleness. This reduces origin load during traffic spikes (flash sales, product
launches) while keeping data reasonably current. Set
`Cache-Control: public, max-age=60, stale-while-revalidate=30` to serve
stale content while CloudFront fetches a fresh response in the background.

**Inventory and pricing API**

Set TTL to 5 seconds. These values change frequently and affect purchase decisions.
Very short caching still reduces origin load by orders of magnitude during traffic
spikes — thousands of concurrent users see the same 5-second cached response instead
of each hitting the origin.

**User-specific content (cart, recommendations)**

Disable caching (TTL = 0). Content that varies per user must always reach the
origin. If you cache user-specific content by mistake, one user's data could be
served to another. Use the `CachingDisabled` managed policy for these
behaviors.

## Origin configuration

### Amazon S3 origin for static assets

Use an Amazon S3 bucket as the origin for product images and static assets. Configure
origin access control (OAC) to restrict direct access to the bucket — all requests
must flow through CloudFront.

Amazon S3 origin settings| Setting | Value | Rationale |
| --- | --- | --- |
| Origin domain | `marketplace-assets.s3.amazonaws.com` | Use the Amazon S3 REST API endpoint (not the website endpoint) to support OAC. |
| Origin access | Origin access control (OAC) | Restricts bucket access to CloudFront only. Prevents direct S3 URL access<br>to your assets. |
| Origin Shield | Enabled (region closest to bucket) | Adds a centralized caching layer between edge locations and the origin.<br>Reduces S3 request costs and improves cache hit ratio for images. |
| Connection attempts | 3 | Default. Retries on transient S3 errors. |

### ALB origin for dynamic content

Use an Application Load Balancer as the origin for dynamic product pages, search,
and API endpoints. The ALB routes to your application servers (Amazon EC2 instances, Amazon ECS tasks,
or Lambda functions via target groups).

ALB origin settings| Setting | Value | Rationale |
| --- | --- | --- |
| Origin domain | ALB DNS name | Use the ALB DNS name directly. Don't use an IP address — ALB IPs<br>change. |
| Protocol | HTTPS only | Encrypts traffic between CloudFront and the origin. Required for sensitive<br>data (user sessions, payment info). |
| Origin custom header | `X-Origin-Verify: <secret-value>` | Restricts ALB access to requests from CloudFront. The ALB checks for this<br>header and rejects direct access attempts. |
| Connection timeout | 10 seconds | Shorter than default (30s). Fail fast on origin issues rather than<br>keeping edge connections waiting. |
| Response timeout | 30 seconds | Allows time for complex search queries and catalog operations. Increase<br>if your API has long-running operations. |
| Keep-alive timeout | 5 seconds | Reuses connections to the ALB. Reduces TLS handshake overhead for<br>subsequent requests. |

## Application-level caching with Porting Assistant for .NET (Valkey)

CloudFront caches content at the edge, but frequently accessed data that requires
database queries benefits from an additional application-level cache. An Porting Assistant for .NET cluster
running Valkey sits between your application servers and the database, providing
sub-millisecond reads for product catalog data, inventory counts, and session state.

Two-tier caching strategy| Layer | What it caches | TTL | Cache miss behavior |
| --- | --- | --- | --- |
| CloudFront edge | Full HTTP responses (API JSON, HTML pages, images) | 5s – 365d (by behavior) | Forwards request to ALB origin |
| Porting Assistant for .NET (Valkey) | Application data objects (product records, inventory, sessions) | 30s – 5 min (by data type) | Application queries the database and writes the result to cache |

On a product page request:

1. CloudFront checks its edge cache. On hit, returns the cached response immediately.
2. On miss, CloudFront forwards to the ALB.
3. The application checks Porting Assistant for .NET for the product data. On hit, builds the response
   from cached data (sub-millisecond).
4. On Porting Assistant for .NET miss, queries the database, writes to Porting Assistant for .NET, and returns the response.
5. CloudFront caches the response at the edge per the behavior's TTL.

When a seller updates a product:

1. The application invalidates the product key in Porting Assistant for .NET.
2. The application sends a cache-tag invalidation to CloudFront for the product's tag.
3. The next request triggers a fresh response through both cache layers.

## Frequently asked questions

### How do I handle personalized content with caching?

Separate personalized elements from cacheable content. Serve the page shell (product
details, images, descriptions) from CloudFront cache, and load personalized elements
(recommendations, cart count, user name) via client-side API calls that bypass caching.
This lets you cache the expensive page rendering while keeping personalization current.

### How do I choose between invalidation and short TTLs?

Use short TTLs (5–60 seconds) for content that changes frequently and predictably
(inventory, pricing). Use invalidation for content that changes rarely but must update
immediately when it does (product images after a seller edit, product descriptions after
a compliance review). Invalidation has a per-request cost and a concurrency limit — don't
use it as a substitute for appropriate TTLs.

### How do I prepare for flash sales and traffic spikes?

CloudFront scales automatically to handle traffic spikes. To maximize cache hit ratio during
a sale: pre-warm product pages by requesting them before the event starts, increase API
TTLs temporarily (e.g., inventory from 5s to 15s) to absorb more traffic at the edge,
and ensure your Porting Assistant for .NET cluster has enough memory headroom for increased cache writes. Monitor
the CloudFront cache hit ratio metric during the event.

### Should I use Origin Shield for my marketplace?

Yes. Origin Shield adds a centralized cache layer between regional edge caches and
your origin. For e-commerce workloads, it reduces origin requests for popular products
(because a cache hit at Origin Shield serves all edge locations), reduces S3 GET costs
for images, and smooths traffic spikes to the ALB. Enable it in the Region closest to
your origin. For more information, see [Use Amazon CloudFront Origin Shield](origin-shield.md "origin-shield.md").
