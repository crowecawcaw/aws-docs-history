# Control origin requests with a policy

When a viewer request to CloudFront results in a _cache miss_
(the requested object is not cached at the edge location), CloudFront sends a request to the
origin to retrieve the object. This is called an _origin
request_. The origin request always includes the following information from the
viewer request:

- The URL path (the path only, without URL query strings or the domain name)
- The request body (if there is one)
- The HTTP headers that CloudFront automatically includes in every origin request,
  including `Host`, `User-Agent`, and
  `X-Amz-Cf-Id`
  Other information from the viewer request, such as URL query strings, HTTP headers, and
  cookies, is not included in the origin request by default. (Exception: With legacy cache settings,
  CloudFront forwards the headers to your origin by default.) However, you might want to receive
  some of this other information at the origin, for example to collect data for analytics or
  telemetry. You can use an _origin request policy_ to
  control the information that's included in an origin request.

Origin request policies are separate from [cache
policies](controlling-the-cache-key.md "controlling-the-cache-key.md"), which control the cache key. This way, you can receive
additional information at the origin and also maintain a good _cache
hit ratio_ (the proportion of viewer requests that result in a cache hit). You do
this by separately controlling which information is included in origin requests (using the
origin request policy) and which is included in the cache key (using the cache
policy).

Although the two kinds of policies are separate, they are related. All URL query strings,
HTTP headers, and cookies that you include in the cache key (using a cache policy) are
automatically included in origin requests. Use the origin request policy to specify the
information that you want to include in origin requests, but _not_ include in the cache key. Just like a cache policy, you attach an origin
request policy to one or more cache behaviors in a CloudFront distribution.

You can also use an origin request policy to add additional HTTP headers to an origin
request that were not included in the viewer request. These additional headers are added by
CloudFront before sending the origin request, with header values that are determined automatically
based on the viewer request. For more information, see [Add CloudFront request headers](adding-cloudfront-headers.md "adding-cloudfront-headers.md").

###### Topics

- [Understand origin request policies](origin-request-understand-origin-request-policy.md "origin-request-understand-origin-request-policy.md")
- [Create origin request policies](origin-request-create-origin-request-policy.md "origin-request-create-origin-request-policy.md")
- [Use managed origin request policies](using-managed-origin-request-policies.md "using-managed-origin-request-policies.md")
- [Add CloudFront request headers](adding-cloudfront-headers.md "adding-cloudfront-headers.md")
- [Understand how origin request policies and cache policies work together](understanding-how-origin-request-policies-and-cache-policies-work-together.md "understanding-how-origin-request-policies-and-cache-policies-work-together.md")
