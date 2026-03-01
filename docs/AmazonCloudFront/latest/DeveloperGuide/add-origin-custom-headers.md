# Add custom headers to origin requests

You can configure CloudFront to add custom headers to the requests that it sends to your origin.
You can use custom headers to send and gather information from your origin that you don’t
get with typical viewer requests. You can even customize the headers for each origin. CloudFront
supports custom headers for custom origins and Amazon S3 origins.

###### Contents

- [Use cases](add-origin-custom-headers.md#add-origin-custom-headers-use-cases "add-origin-custom-headers.md#add-origin-custom-headers-use-cases")
- [Configure CloudFront to add custom headers to origin requests](add-origin-custom-headers.md#add-origin-custom-headers-configure "add-origin-custom-headers.md#add-origin-custom-headers-configure")
- [Custom headers that CloudFront can’t add to origin requests](add-origin-custom-headers.md#add-origin-custom-headers-denylist "add-origin-custom-headers.md#add-origin-custom-headers-denylist")
- [Configure CloudFront to forward the Authorization header](add-origin-custom-headers.md#add-origin-custom-headers-forward-authorization "add-origin-custom-headers.md#add-origin-custom-headers-forward-authorization")

## Use cases

You can use custom headers, such as the following examples:

**Identifying requests from CloudFront**

You can identify the requests that your origin receives from CloudFront. This
can be useful if you want to know if users are bypassing CloudFront, or if you’re
using more than one CDN and you want information about which requests are
coming from each CDN.

###### Note

If you’re using an Amazon S3 origin and you enable [Amazon S3
server access logging](../../../AmazonS3/latest/dev/ServerLogs.md "../../../AmazonS3/latest/dev/ServerLogs.md"), the logs don’t include header
information.

**Determining which requests come from a particular distribution**

If you configure more than one CloudFront distribution to use the same origin,
you can add different custom headers in each distribution. You can then use
the logs from your origin to determine which requests came from which CloudFront
distribution.

**Enabling cross-origin resource sharing (CORS)**

If some of your viewers don’t support cross-origin resource sharing
(CORS), you can configure CloudFront to always add the `Origin` header
to requests that it sends to your origin. Then you can configure your origin
to return the `Access-Control-Allow-Origin` header for every
request. You must also [configure
CloudFront to respect CORS settings](header-caching.md#header-caching-web-cors "header-caching.md#header-caching-web-cors").

**Controlling access to content**

You can use custom headers to control access to content. By configuring
your origin to respond to requests only when they include a custom header
that gets added by CloudFront, you prevent users from bypassing CloudFront and accessing
your content directly on the origin. For more information, see [Restrict access to files on custom origins](private-content-overview.md#forward-custom-headers-restrict-access "private-content-overview.md#forward-custom-headers-restrict-access").

## Configure CloudFront to add custom headers to origin requests

To configure a distribution to add custom headers to requests that it sends to your
origin, update the origin configuration using one of the following methods:

- **CloudFront console** – When you create or
  update a distribution, specify header names and values in the **Add
  custom headers** settings. For more information, see [Add custom header](DownloadDistValuesOrigin.md#DownloadDistValuesOriginCustomHeaders "DownloadDistValuesOrigin.md#DownloadDistValuesOriginCustomHeaders").
- **CloudFront API** – For each origin that you
  want to add custom headers to, specify the header names and values in the
  `CustomHeaders` field inside `Origin`. For more
  information, see [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md") or [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") in the
  _Amazon CloudFront API Reference_.

If the header names and values that you specify are not already present in the viewer
request, CloudFront adds them to the origin request. If a header is present, CloudFront overwrites
the header value before forwarding the request to the origin.

For the quotas that apply to origin custom headers, see [Quotas on headers](cloudfront-limits.md#limits-custom-headers "cloudfront-limits.md#limits-custom-headers").

## Custom headers that CloudFront can’t add to origin requests

You can’t configure CloudFront to add any of the following headers to requests that it sends
to your origin:

- `Cache-Control`
- `Connection`
- `Content-Length`
- `Cookie`
- `Host`
- `If-Match`
- `If-Modified-Since`
- `If-None-Match`
- `If-Range`
- `If-Unmodified-Since`
- `Max-Forwards`
- `Pragma`
- `Proxy-Authenticate`
- `Proxy-Authorization`
- `Proxy-Connection`
- `Range`
- `Request-Range`
- `TE`
- `Trailer`
- `Transfer-Encoding`
- `Upgrade`
- `Via`
- Headers that begin with `X-Amz-`
- Headers that begin with `X-Edge-`
- `X-Real-Ip`

## Configure CloudFront to forward the `Authorization` header

When CloudFront forwards a viewer request to your origin, CloudFront removes some viewer headers
by default, including the `Authorization` header. To make sure that your
origin always receives the `Authorization` header in origin requests, you
have the following options:

- Add the `Authorization` header to the cache key using a cache
  policy. All headers in the cache key are automatically included in origin
  requests. For more information, see [Control the cache key with a policy](controlling-the-cache-key.md "controlling-the-cache-key.md").
- Use an origin request policy that forwards all viewer headers to the origin.
  You cannot forward the `Authorization` header individually in an
  origin request policy, but when you forward all viewer headers CloudFront includes the
  `Authorization` header in viewer requests. CloudFront provides a
  managed origin request policy for this use case, called **Managed-AllViewer**. For more information, see [Use managed origin request policies](using-managed-origin-request-policies.md "using-managed-origin-request-policies.md").
