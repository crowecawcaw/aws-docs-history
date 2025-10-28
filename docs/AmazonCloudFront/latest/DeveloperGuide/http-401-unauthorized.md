# HTTP 401 status code (Unauthorized)

A 401 Unauthorized response status code indicates that the client request hasn't
been completed because it lacks valid authentication credentials for the requested
resource. This status code is sent with an HTTP `WWW-Authenticate`
response header that contains information about how the client can request the
resource again after prompting the user for authentication credentials. For more
information, see [401
Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401 "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401").

In CloudFront, if your origin expects an `Authorization` header to
authenticate the requests, CloudFront needs to forward the `Authorization`
header to the origin to avoid a 401 Unauthorized error. When CloudFront forwards a viewer
request to your origin, CloudFront removes some viewer headers by default, including the
`Authorization` header. To make sure that your origin always receives
the `Authorization` header in origin requests, you have the following
options:

- Add the `Authorization` header to the cache key by using a
  cache policy. All headers in the cache key are automatically included in
  origin requests. For more information, see [Control the cache key with a policy](controlling-the-cache-key.md "controlling-the-cache-key.md").
- Use an origin request policy that forwards all viewer headers to the
  origin. You can't forward the `Authorization` header individually
  in an origin request policy, but when you forward all viewer headers, CloudFront
  includes the `Authorization` header in viewer requests. CloudFront
  provides the managed `AllViewer` origin request policy for this
  use case. For more information, see [Use managed origin request
  policies](using-managed-origin-request-policies.md "using-managed-origin-request-policies.md").
  For more information, see [How
  can I configure CloudFront to forward the Authorization header to the
  origin?](https://repost.aws/knowledge-center/cloudfront-authorization-header "https://repost.aws/knowledge-center/cloudfront-authorization-header")
