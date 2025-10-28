# Control the cache key with a policy

With a CloudFront _cache policy_, you can specify the HTTP
headers, cookies, and query strings that CloudFront includes in the _cache
key_ for objects that are cached at CloudFront edge locations. The cache key is the
unique identifier for every object in the cache, and it determines whether a viewer's HTTP
request results in a _cache hit_.

A cache hit occurs when a viewer request generates the same cache key as a prior request,
and the object for that cache key is in the edge location's cache and valid. When there's a
cache hit, the object is served to the viewer from a CloudFront edge location, which has the
following benefits:

- Reduced load on your origin server
- Reduced latency for the viewer
  Including fewer values in the cache key increases the likelihood of a cache hit. This can
  get you better performance from your website or application because there's a higher
  _cache hit ratio_ (a higher proportion of viewer
  requests that result in a cache hit). For more information, see [Understand the cache key](understanding-the-cache-key.md "understanding-the-cache-key.md").

To control the cache key, you use a CloudFront _cache policy_.
You attach a cache policy to one or more cache behaviors in a CloudFront distribution.

You can also use the cache policy to specify time to live (TTL) settings for objects in
the CloudFront cache, and enable CloudFront to request and cache compressed objects.

###### Note

Cache settings don't affect gRPC requests because gRPC traffic can't be cached. For
more information, see [Using gRPC with CloudFront distributions](distribution-using-grpc.md "distribution-using-grpc.md").

###### Topics

- [Understand cache policies](cache-key-understand-cache-policy.md "cache-key-understand-cache-policy.md")
- [Create cache policies](cache-key-create-cache-policy.md "cache-key-create-cache-policy.md")
- [Use managed cache policies](using-managed-cache-policies.md "using-managed-cache-policies.md")
- [Understand the cache key](understanding-the-cache-key.md "understanding-the-cache-key.md")
