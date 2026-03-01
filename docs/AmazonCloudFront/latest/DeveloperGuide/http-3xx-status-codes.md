# How CloudFront processes HTTP 3xx status codes from your origin

When CloudFront requests an object from your Amazon S3 bucket or custom origin server, your
origin sometimes returns an HTTP 3xx status code. This typically indicates one of the
following:

- The object’s URL has changed (for example, status codes 301, 302, 307, or

308.

- The object hasn’t changed since the last time CloudFront requested it (status code

304.  CloudFront caches 3xx responses according to the settings in your CloudFront distribution and the
      headers in the response. CloudFront caches 307 and 308 responses only when you include the
      `Cache-Control` header in responses from the origin. For more
      information, see [Manage how long content stays in the cache (expiration)](Expiration.md "Expiration.md").

If your origin returns a redirect status code (for example, 301 or 307), CloudFront doesn’t
follow the redirect. CloudFront passes along the 301 or 307 response to the viewer, who can
follow the redirect by sending a new request.
