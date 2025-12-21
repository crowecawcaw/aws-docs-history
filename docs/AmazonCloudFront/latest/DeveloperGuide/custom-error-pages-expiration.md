# Control how long CloudFront caches

errors

CloudFront caches error responses for a default duration of 10 seconds. CloudFront then submits
the next request for the object to your origin to see if the problem that caused the
error has been resolved and the requested object is available.

You can specify the error-caching duration—the **Error Caching Minimum
TTL**—for each 4xx and 5xx status code that CloudFront caches. (For more
information, see [HTTP 4xx and 5xx status codes that
CloudFront caches](HTTPStatusCodes.md#HTTPStatusCodes-cached-errors "HTTPStatusCodes.md#HTTPStatusCodes-cached-errors").) When you specify a duration, note
the following:

- If you specify a short error-caching duration, CloudFront forwards more requests to
  your origin than if you specify a longer duration. For 5xx errors, this might
  aggravate the problem that originally caused your origin to return an
  error.
- When your origin returns an error for an object, CloudFront responds to requests for
  the object either with the error response or with your custom error page until
  the error-caching duration elapses. If you specify a long error-caching
  duration, CloudFront might continue to respond to requests with an error response or
  your custom error page for a long time after the object becomes available
  again.

###### Note

You can create a custom error page for HTTP status code 416 (Requested
Range Not Satisfiable), and you can change the HTTP status code that CloudFront
returns to viewers when your origin returns a status code 416 to CloudFront. (For
more information, see [Change response codes returned by
CloudFront](custom-error-pages-response-code.md "custom-error-pages-response-code.md").) However, CloudFront doesn't
cache status code 416 responses, so even if you specify a value for
**Error Caching Minimum TTL** for status code 416, CloudFront
doesn't use it.

If you want to control how long CloudFront caches errors for individual objects, you can
configure your origin server to add the applicable header to the error response for that
object.

If the origin adds a `Cache-Control: max-age` or `Cache-Control:
 s-maxage` directive, or an `Expires` header, CloudFront caches error
responses for the greater of the value in the header or the **Error Caching
Minimum TTL**.

###### Note

The `Cache-Control: max-age` and `Cache-Control: s-maxage`
values cannot be greater than the **Maximum TTL** value set for the
cache behavior for which the error page is being fetched.

If the origin adds a `Cache-Control: no-store`, `Cache-Control:
 no-cache`, or `Cache-Control: private` directive for error codes
404, 410, 414, or 501, CloudFront does not cache the error response. For all other error
codes, CloudFront ignores the `no-store`, `no-cache`, and
`private` directives and caches the error response for the value of
**Error Caching Minimum TTL**.

If the origin adds other `Cache-Control` directives or adds no headers,
CloudFront caches error responses for the value of **Error Caching Minimum
TTL**.

If the expiration time for a 4xx or 5xx status code for an object is longer than you
want, and the object is available again, you can invalidate cached error code by using
the URL of the requested object. If your origin is returning an error response for
multiple objects, you need to invalidate each object separately. For more information
about invalidating objects, see [Invalidate files to remove content](Invalidation.md "Invalidation.md").

If you have caching enabled for an S3 bucket origin, and you configure an error caching minimum TTL of 0 seconds in your CloudFront distribution, you will still see an error caching minimum TTL of 1 second for S3 origin errors. CloudFront does this to protect your origin from DDoS attacks. This doesn't apply to other types of origins.
