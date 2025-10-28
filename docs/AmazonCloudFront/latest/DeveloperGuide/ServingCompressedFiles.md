# Serve compressed files

When requested objects are compressed, downloads can be faster because the objects are
smaller—in some cases, less than a quarter the size of the original. Faster downloads
can result in faster rendering of webpages for your viewers, especially for JavaScript and
CSS files. In addition, the cost of CloudFront data transfer is based on the total amount of data
served. Serving compressed objects can be less expensive than serving them
uncompressed.

###### Topics

- [Configure CloudFront to compress
  objects](#compressed-content-cloudfront-configuring "#compressed-content-cloudfront-configuring")
- [How CloudFront compression
  works](#compressed-content-cloudfront-how-it-works "#compressed-content-cloudfront-how-it-works")
- [Conditions for compression](#compressed-content-cloudfront-notes "#compressed-content-cloudfront-notes")
- [File types that CloudFront
  compresses](#compressed-content-cloudfront-file-types "#compressed-content-cloudfront-file-types")
- [ETag header
  conversion](#compressed-content-cloudfront-etag-header "#compressed-content-cloudfront-etag-header")

## Configure CloudFront to compress

objects

To configure CloudFront to compress objects, update the cache behavior that you want to
serve the compressed objects.

###### To configure CloudFront to compress objects (console)

1. Sign in to the [CloudFront
   console](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose your distribution and then choose the **Behavior** to
   edit.
3. For the **Compress objects automatically** setting, choose
   **Yes**.
4. Use a [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md") to specify
   the caching settings, and enable both **Gzip** and
   **Brotli** compression formats.

###### Notes

- You must use [cache
  policies](controlling-the-cache-key.md "controlling-the-cache-key.md") to use Brotli compression. Brotli doesn't support legacy
  cache settings.
- To enable compression by using [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.md") or the [CloudFront](../../../cloudfront/latest/APIReference/Welcome.md "../../../cloudfront/latest/APIReference/Welcome.md") API, set
  the `Compress`, `EnableAcceptEncodingGzip`,
  `EnableAcceptEncodingBrotli` parameters to
  `true`.

To understand how CloudFront compresses objects, see the following section.

## How CloudFront compression

works

1. A viewer requests an object. The viewer includes the
   `Accept-Encoding` HTTP header in the request, and the header
   value includes `gzip`, `br`, or both. This indicates that
   the viewer supports compressed objects. When the viewer supports both Gzip and
   Brotli, CloudFront uses Brotli.

###### Note

Chrome and Firefox web browsers support Brotli compression only when the
request is sent using HTTPS. They don't support Brotli with HTTP
requests. 2. At the edge location, CloudFront checks the cache for a compressed copy of the
requested object. 3. Depending whether the compressed object is in the cache or not, CloudFront does one
of the following:

    * If the compressed object is already in the cache, CloudFront sends the
     object to the viewer and skips the remaining steps.
    * If the compressed object isn't in the cache, CloudFront forwards the request
     to the origin.###### Note

If an uncompressed copy of the object is already in the cache, CloudFront might
send it to the viewer without forwarding the request to the origin. For
example, this can happen when CloudFront [previously skipped compression](#compression-skipped "#compression-skipped"). When this happens, CloudFront caches
the uncompressed object and continues to serve it until the object expires,
is evicted, or is invalidated. 4. If the origin returns a compressed object, (as indicated by the
`Content-Encoding` header in the HTTP response), CloudFront sends the
compressed object to the viewer, adds it to the cache, and skips the remaining
steps. CloudFront doesn’t compress the object again. 5. If the origin returns an uncompressed object to CloudFront without the
`Content-Encoding` header in the HTTP response, CloudFront then
determines whether the object can be compressed. For more information, see [Conditions for compression](#compressed-content-cloudfront-notes "#compressed-content-cloudfront-notes"). 6. If the object can be compressed, CloudFront compresses it, sends it to the viewer,
and then adds it to the cache. 7. If there are subsequent viewer requests for the same object, CloudFront returns the
first cached version. For example, if a viewer requests a specific cached object
that uses Gzip compression, and the viewer _accepts_ the Gzip
format, subsequent requests to the same object will always return the Gzip
version, even if the viewer accepts both Brotli and Gzip.

Some custom origins can also compress objects. Your origin might be able to compress
objects that CloudFront doesn’t compress. For more information, see [File types that CloudFront
compresses](#compressed-content-cloudfront-file-types "#compressed-content-cloudfront-file-types").

## Conditions for compression

The following list provides more information about scenarios in which CloudFront doesn't compress
objects.

**Request uses HTTP 1.0**

If a request to CloudFront uses HTTP 1.0, CloudFront removes the
`Accept-Encoding` header and doesn't compress the object in
the response.

**`Accept-Encoding` request header**

If the `Accept-Encoding` header is missing from the viewer
request, or if it doesn’t contain `gzip` or `br` as a
value, CloudFront doesn't compress the object in the response. If the
`Accept-Encoding` header includes additional values such as
`deflate`, CloudFront removes them before forwarding the request to
the origin.

When CloudFront is [configured to compress objects](#compressed-content-cloudfront-configuring "#compressed-content-cloudfront-configuring"), it includes the
`Accept-Encoding` header in the cache key and in origin
requests automatically.

**Content is already cached when you configure CloudFront to compress objects**

CloudFront compresses objects when it gets them from the origin. When you
configure CloudFront to compress objects, CloudFront doesn’t compress objects that are
already cached in edge locations. In addition, when a cached object expires
in an edge location and CloudFront forwards another request for the object to your
origin, CloudFront doesn’t compress the object when your origin returns an HTTP
status code 304. This means that the edge location already has the latest
version of the object. If you want CloudFront to compress objects that are already
cached in edge locations, you need to invalidate those objects. For more
information, see [Invalidate files to remove content](Invalidation.md "Invalidation.md").

**Origin is already configured to compress objects**

If you configure CloudFront to compress objects and the origin also compresses
objects, the origin should include a `Content-Encoding` header.
This header indicates to CloudFront that the object is already compressed. When a
response from an origin includes the `Content-Encoding` header,
CloudFront doesn't compress the object, regardless of the header’s value. CloudFront
sends the response to the viewer and caches the object in the edge
location.

**File types that CloudFront compresses**

For a complete list, see [File types that CloudFront
compresses](#compressed-content-cloudfront-file-types "#compressed-content-cloudfront-file-types").

**Size of objects that CloudFront compresses**

CloudFront compresses objects that are between 1,000 bytes and 10,000,000 bytes
in size.

**`Content-Length` header**

The origin must include a `Content-Length` header in the
response, which CloudFront uses to determine whether the size of the object is in
the range that CloudFront compresses. If the `Content-Length` header is
missing, contains an invalid value, or contains a value outside the range of
sizes that CloudFront compresses, CloudFront doesn't compress the object. For more
information about how CloudFront processes large objects that can exceed the size
range, see [How CloudFront processes partial requests for an object (range
GETs)](RangeGETs.md "RangeGETs.md").

**HTTP status code of the response**

CloudFront compresses objects only when the HTTP status code of the response is
`200`, `403`, or `404`.

**Response has no body**

When the HTTP response from the origin has no body, there is nothing for
CloudFront to compress.

**`ETag` header**

CloudFront sometimes modifies the `ETag` header in the HTTP response
when it compresses objects. For more information, see [ETag header
conversion](#compressed-content-cloudfront-etag-header "#compressed-content-cloudfront-etag-header").

**CloudFront skips compression**

CloudFront compresses objects on a best-effort basis. In rare cases, CloudFront skips
compressing an object when CloudFront experiences high traffic load. CloudFront makes
this decision based on a variety of factors, including host capacity. If
CloudFront skips compression for an object, it caches the uncompressed object and
continues to serve it to viewers until the object expires, is evicted, or is
invalidated.

## File types that CloudFront

compresses

If you configure CloudFront to compress objects, CloudFront only compresses objects that have one
of the following values in the `Content-Type` response header:

- `application/dash+xml`
- `application/eot`
- `application/font`
- `application/font-sfnt`
- `application/javascript`
- `application/json`
- `application/opentype`
- `application/otf`
- `application/pdf`
- `application/pkcs7-mime`
- `application/protobuf`
- `application/rss+xml`
- `application/truetype`
- `application/ttf`
- `application/vnd.apple.mpegurl`
- `application/vnd.mapbox-vector-tile`
- `application/vnd.ms-fontobject`
- `application/wasm`
- `application/xhtml+xml`
- `application/xml`
- `application/x-font-opentype`
- `application/x-font-truetype`
- `application/x-font-ttf`
- `application/x-httpd-cgi`
- `application/x-javascript`
- `application/x-mpegurl`
- `application/x-opentype`
- `application/x-otf`
- `application/x-perl`
- `application/x-ttf`
- `font/eot`
- `font/opentype`
- `font/otf`
- `font/ttf`
- `image/svg+xml`
- `text/css`
- `text/csv`
- `text/html`
- `text/javascript`
- `text/js`
- `text/plain`
- `text/richtext`
- `text/tab-separated-values`
- `text/xml`
- `text/x-component`
- `text/x-java-source`
- `text/x-script`
- `vnd.apple.mpegurl`

[Show moreShow less](# "#")

## `ETag` header

conversion

When the uncompressed object from the origin includes a valid, strong
`ETag` HTTP header, and CloudFront compresses the object, CloudFront also converts
the strong `ETag` header value to a weak `ETag`, and returns the
weak `ETag` value to the viewer. Viewers can store the weak `ETag`
value and use it to send conditional requests with the `If-None-Match` HTTP
header. This allows viewers, CloudFront, and the origin to treat the compressed and
uncompressed versions of an object as semantically equivalent, which reduces unnecessary
data transfer.

A valid, strong `ETag` header value begins and ends with a double quote
character (`"`). To convert the strong `ETag` value to a weak one,
CloudFront adds the characters `W/` to the beginning of the strong
`ETag` value.

When the object from the origin includes a weak `ETag` header value (a
value that begins with the characters `W/`), CloudFront does not modify this value,
and returns it to the viewer as received from the origin.

When the object from the origin includes an invalid `ETag` header value
(the value does not begin with `"` or with `W/`), CloudFront removes the
`ETag` header and returns the object to the viewer without the
`ETag` response header.

For more information, see the following pages in the MDN web docs:

- [Directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag#Directives "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag#Directives") (`ETag` HTTP header)
- [Weak validation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests#Weak_validation "https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests#Weak_validation") (HTTP conditional requests)
- [If-None-Match HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match")
