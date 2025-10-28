# How CloudFront processes HTTP 4xx and 5xx status codes from

your origin

When CloudFront requests an object from your Amazon S3 bucket or custom origin server, your
origin sometimes returns an HTTP 4xx or 5xx status code, which indicates that an error
has occurred. CloudFront behavior depends on:

- Whether you have configured custom error pages
- Whether you have configured how long you want CloudFront to cache error responses
  from your origin (error caching minimum TTL)
- The status code
- For 5xx status codes, whether the requested object is currently in the CloudFront
  edge cache
- For some 4xx status codes, whether the origin returns a `Cache-Control
 max-age` or `Cache-Control s-maxage` header
  CloudFront always caches responses to `GET` and `HEAD` requests. You
  can also configure CloudFront to cache responses to `OPTIONS` requests. CloudFront does
  not cache responses to requests that use the other methods.

If the origin doesn't respond, the CloudFront request to the origin times out which is
considered an HTTP 5xx error from the origin, even though the origin didn't respond with
that error. In that scenario, CloudFront continues to serve cached content. For more
information, see [Origin unavailable](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomOriginUnavailable "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomOriginUnavailable").

If you have enabled logging, CloudFront writes the results to the logs regardless of the
HTTP status code.

For more information about features and options that relate to the error message
returned from CloudFront, see the following:

- For information about settings for custom error pages in the CloudFront console, see
  [Custom error pages and error
  caching](DownloadDistValuesErrorPages.md "DownloadDistValuesErrorPages.md").
- For information about the error caching minimum TTL in the CloudFront console, see
  [Error caching minimum
  TTL (seconds)](DownloadDistValuesErrorPages.md#DownloadDistValuesErrorCachingMinTTL "DownloadDistValuesErrorPages.md#DownloadDistValuesErrorCachingMinTTL").
- For a list of the HTTP status codes that CloudFront caches, see [HTTP 4xx and 5xx status codes that
  CloudFront caches](#HTTPStatusCodes-cached-errors "#HTTPStatusCodes-cached-errors").

###### Topics

- [How CloudFront processes errors when
  you have configured custom error pages](#HTTPStatusCodes-custom-error-pages "#HTTPStatusCodes-custom-error-pages")
- [How CloudFront processes errors if
  you haven't configured custom error pages](#HTTPStatusCodes-no-custom-error-pages "#HTTPStatusCodes-no-custom-error-pages")
- [HTTP 4xx and 5xx status codes that
  CloudFront caches](#HTTPStatusCodes-cached-errors "#HTTPStatusCodes-cached-errors")

## How CloudFront processes errors when

you have configured custom error pages

If you have configured custom error pages, CloudFront behavior depends on whether the
requested object is in the edge cache.

### The requested

object is not in the edge cache

CloudFront continues to try to get the requested object from your origin when all of
the following are true:

- A viewer requests an object.
- The object isn't in the edge cache.
- Your origin returns an HTTP 4xx or 5xx status code and one of the
  following is true:
  - Your origin returns an HTTP 5xx status code instead of
    returning a 304 status code (Not Modified) or an updated version
    of the object.
  - Your origin returns an HTTP 4xx status code that is not
    restricted by a cache control header and is included in the
    following list of status codes: [HTTP 4xx and 5xx status codes that
    CloudFront caches](#HTTPStatusCodes-cached-errors "#HTTPStatusCodes-cached-errors").
  - Your origin returns an HTTP 4xx status code with a
    `Cache-Control max-age` header or a
    `Cache-Control s-maxage` header, and the status
    code is included in the following list of status codes: Control
    [HTTP 4xx
    status codes that CloudFront caches based on Cache-Control
    headers](#HTTPStatusCodes-cached-errors-with-cache-control "#HTTPStatusCodes-cached-errors-with-cache-control").

###### CloudFront does the following:

1. In the CloudFront edge cache that received the viewer request, CloudFront checks
   your distribution configuration and gets the path of the custom error
   page that corresponds with the status code that your origin returned.
2. CloudFront finds the first cache behavior in your distribution that has a
   path pattern that matches the path of the custom error page.
3. The CloudFront edge location sends a request for the custom error page to
   the origin that is specified in the cache behavior.
4. The origin returns the custom error page to the edge location.
5. CloudFront returns the custom error page to the viewer that made the
   request, and also caches the custom error page for the maximum of the
   following:
   - The amount of time specified by the error caching minimum TTL
     (10 seconds by default)
   - The amount of time specified by a `Cache-Control
max-age` header or a `Cache-Control
s-maxage` header that is returned by the origin when
     the first request generated the error

6. After the caching time (determined in Step 5) has elapsed, CloudFront tries
   again to get the requested object by forwarding another request to your
   origin. CloudFront continues to retry at intervals specified by the error
   caching minimum TTL.

###### Note

If you also configured a cache behavior for the same custom error page, CloudFront uses the
cache behavior TTL instead. In this case, CloudFront will do the following for
steps 5 and 6:

- After CloudFront returns the custom error page to the viewer that made
  the request, CloudFront checks the cache behavior TTL (for example, you
  set the default TTL to 5 seconds). CloudFront then caches the custom error
  page up to that maximum.
- After 5 seconds elapse, CloudFront fetches the custom error page from
  the origin again. CloudFront will continue to retry at intervals specified
  by the cache behavior TTL.
  For more information, see the cache behavior [TTL settings](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL").

### The requested

object is in the edge cache

CloudFront continues to serve the object that is currently in the edge cache when
all of the following are true:

- A viewer requests an object.
- The object is in the edge cache but it has expired.
- Your origin returns an HTTP 5xx status code instead of returning a 304
  status code (Not Modified) or an updated version of the object.

###### CloudFront does the following:

1. If your origin returns a 5xx status code, CloudFront serves the object even
   though it has expired. For the duration of the error caching minimum
   TTL, CloudFront continues to respond to viewer requests by serving the object
   from the edge cache.

If your origin returns a 4xx status code, CloudFront returns the status
code, not the requested object, to the viewer. 2. After the error caching minimum TTL has elapsed, CloudFront tries again to
get the requested object by forwarding another request to your origin.
Note that if the object is not requested frequently, CloudFront might evict it
from the edge cache while your origin server is still returning 5xx
responses. For information about how long objects stay in CloudFront edge
caches, see [Manage how long content stays in the cache
(expiration)](Expiration.md "Expiration.md").

## How CloudFront processes errors if

you haven't configured custom error pages

If you haven't configured custom error pages, CloudFront behavior depends on whether the
requested object is in the edge cache.

###### Topics

- [The
  requested object is not in the edge cache](#HTTPStatusCodes-no-custom-error-pages-not-in-cache "#HTTPStatusCodes-no-custom-error-pages-not-in-cache")
- [The requested
  object is in the edge cache](#HTTPStatusCodes-no-custom-error-pages-in-cache "#HTTPStatusCodes-no-custom-error-pages-in-cache")

### The

requested object is not in the edge cache

CloudFront continues to try to get the requested object from your origin when all of
the following are true:

- A viewer requests an object.
- The object isn't in the edge cache.
- Your origin returns an HTTP 4xx or 5xx status code and one of the
  following is true:
  - Your origin returns an HTTP 5xx status code instead of
    returning a 304 status code (Not Modified) or an updated version
    of the object.
  - Your origin returns an HTTP 4xx status code that is not
    restricted by a cache control header and is included in the
    following list of status codes: [HTTP 4xx and 5xx status codes that
    CloudFront caches](#HTTPStatusCodes-cached-errors "#HTTPStatusCodes-cached-errors")
  - Your origin returns an HTTP 4xx status code with a
    `Cache-Control max-age` header or a
    `Cache-Control s-maxage` header and the status
    code is included in the following list of status codes: Control
    [HTTP 4xx
    status codes that CloudFront caches based on Cache-Control
    headers](#HTTPStatusCodes-cached-errors-with-cache-control "#HTTPStatusCodes-cached-errors-with-cache-control").

CloudFront does the following:

1. CloudFront returns the 4xx or 5xx status code to the viewer, and also caches
   status code in the edge cache that received the request for the maximum
   of the following:
   - The amount of time specified by the error caching minimum TTL
     (10 seconds by default)
   - The amount of time specified by a `Cache-Control
max-age` header or a `Cache-Control
s-maxage` header that is returned by the origin when
     the first request generated the error

2. For the duration of the caching time (determined in Step 1), CloudFront
   responds to subsequent viewer requests for the same object with the
   cached 4xx or 5xx status code.
3. After the caching time (determined in Step 1) has elapsed, CloudFront tries
   again to get the requested object by forwarding another request to your
   origin. CloudFront continues to retry at intervals specified by the error
   caching minimum TTL.

### The requested

object is in the edge cache

CloudFront continues to serve the object that is currently in the edge cache when
all of the following are true:

- A viewer requests an object.
- The object is in the edge cache but it has expired. This means the
  object is _stale_.
- Your origin returns an HTTP 5xx status code instead of returning a 304
  status code (Not Modified) or an updated version of the object.

CloudFront does the following:

1. If your origin returns a 5xx error code, CloudFront serves the object even
   though it has expired. For the duration of the error caching minimum TTL
   (10 seconds by default), CloudFront continues to respond to viewer requests by
   serving the object from the edge cache.

If your origin returns a 4xx status code, CloudFront returns the status
code, not the requested object, to the viewer. 2. After the error caching minimum TTL has elapsed, CloudFront tries again to
get the requested object by forwarding another request to your origin.
If the object isn't requested frequently, CloudFront might evict it from the
edge cache while your origin server is still returning 5xx responses.
For more information, see [Manage how long content stays in the cache
(expiration)](Expiration.md "Expiration.md").

###### Tip

- If you configure the `stale-if-error` or
  `Stale-While-Revalidate` directive, you can specify how
  long the stale objects are available in the edge cache. This allows you
  to continue serving content for your viewers even when your origin is
  unavailable. For information, see [Serve stale (expired) content](Expiration.md#stale-content "Expiration.md#stale-content").
- CloudFront will only serve an object that is stale up to the specified [maximum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL") value. After this duration, the object won't be available from the edge cache.

## HTTP 4xx and 5xx status codes that

CloudFront caches

CloudFront caches HTTP 4xx and 5xx status codes returned by your origin, depending on
the specific status code that is returned and whether your origin returns specific
headers in the response.

CloudFront caches the following HTTP 4xx and 5xx status codes returned by your origin.
If you configured a custom error page for an HTTP status code, CloudFront caches the
custom error page.

###### Note

If you're using the [CachingDisabled](using-managed-cache-policies.md#managed-cache-policy-caching-disabled "using-managed-cache-policies.md#managed-cache-policy-caching-disabled") managed cache policy, CloudFront
won't cache these status codes or custom error pages.

|      |                        |
| ---- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 404  | Not Found              |
| 414  | Request-URI Too Large  |
| 500  | Internal Server Error  |
| 501  | Not Implemented        |
| 502  | Bad Gateway            |
| 503  | Service Unavailable    |
| 504  | Gateway Time-out       | ### HTTP 4xx status codes that CloudFront caches based on `Cache-Control` headers CloudFront only caches the following HTTP 4xx status codes returned by your origin if your origin returns a `Cache-Control max-age` or `Cache-Control s-maxage` header. If you have configured a custom error page for one of these HTTP status codes – and your origin returns one of the cache control headers – CloudFront caches the custom error page. |
|      |                        |
| ---  | ---                    |
| 400  | Bad Request            |
| 403  | Forbidden              |
| 405  | Method Not Allowed     |
| 412¹ | Precondition Failed    |
| 415¹ | Unsupported Media Type | ¹CloudFront doesn't support creating custom error pages for these HTTP status codes.                                                                                                                                                                                                                                                                                                                                                          |
