# Request and response behavior

for custom origins

To understand how CloudFront processes requests and responses when you're using custom
origins, see the following sections:

###### Topics

- [How CloudFront processes and forwards
  requests to your custom origin](#RequestBehaviorCustomOrigin "#RequestBehaviorCustomOrigin")
- [How CloudFront processes responses from
  your custom origin](#ResponseBehaviorCustomOrigin "#ResponseBehaviorCustomOrigin")

## How CloudFront processes and forwards

requests to your custom origin

Learn about how CloudFront processes viewer requests and forwards the requests to your
custom origin.

###### Contents

- [Authentication](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomClientAuth "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomClientAuth")
- [Caching duration and minimum TTL](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomCaching "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomCaching")
- [Client IP addresses](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomIPAddresses "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomIPAddresses")
- [Client-side SSL
  authentication](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomClientSideSslAuth "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomClientSideSslAuth")
- [Compression](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomCompression "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomCompression")
- [Conditional requests](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomConditionalGETs "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomConditionalGETs")
- [Cookies](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomCookies "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomCookies")
- [Cross-origin resource sharing
  (CORS)](RequestAndResponseBehaviorCustomOrigin.md#request-custom-cors "RequestAndResponseBehaviorCustomOrigin.md#request-custom-cors")
- [Encryption](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomEncryption "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomEncryption")
- [GET requests that include a
  body](RequestAndResponseBehaviorCustomOrigin.md#RequestCustom-get-body "RequestAndResponseBehaviorCustomOrigin.md#RequestCustom-get-body")
- [HTTP methods](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomHTTPMethods "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomHTTPMethods")
- [HTTP request headers and CloudFront
  behavior (custom and Amazon S3 origins)](RequestAndResponseBehaviorCustomOrigin.md#request-custom-headers-behavior "RequestAndResponseBehaviorCustomOrigin.md#request-custom-headers-behavior")
- [HTTP version](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomHTTPVersion "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomHTTPVersion")
- [Maximum length of a
  request and maximum length of a URL](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomMaxRequestStringLength "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomMaxRequestStringLength")
- [OCSP stapling](RequestAndResponseBehaviorCustomOrigin.md#request-custom-ocsp-stapling "RequestAndResponseBehaviorCustomOrigin.md#request-custom-ocsp-stapling")
- [Persistent
  connections](RequestAndResponseBehaviorCustomOrigin.md#request-custom-persistent-connections "RequestAndResponseBehaviorCustomOrigin.md#request-custom-persistent-connections")
- [Protocols](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomProtocols "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomProtocols")
- [Query strings](RequestAndResponseBehaviorCustomOrigin.md#RequestCustomQueryStrings "RequestAndResponseBehaviorCustomOrigin.md#RequestCustomQueryStrings")
- [Origin connection timeout and
  attempts](RequestAndResponseBehaviorCustomOrigin.md#custom-origin-timeout-attempts "RequestAndResponseBehaviorCustomOrigin.md#custom-origin-timeout-attempts")
- [Origin response timeout](RequestAndResponseBehaviorCustomOrigin.md#request-custom-request-timeout "RequestAndResponseBehaviorCustomOrigin.md#request-custom-request-timeout")
- [Simultaneous requests for the
  same object (request collapsing)](RequestAndResponseBehaviorCustomOrigin.md#request-custom-traffic-spikes "RequestAndResponseBehaviorCustomOrigin.md#request-custom-traffic-spikes")
- [User-Agent
  header](RequestAndResponseBehaviorCustomOrigin.md#request-custom-user-agent-header "RequestAndResponseBehaviorCustomOrigin.md#request-custom-user-agent-header")

### Authentication

If you forward the `Authorization` header to your origin, you can
then configure your origin server to request client authentication for the
following types of requests:

- `DELETE`
- `GET`
- `HEAD`
- `PATCH`
- `PUT`
- `POST`

For `OPTIONS` requests, client authentication can
_only_ be configured if you use the following CloudFront
settings:

- CloudFront is configured to forward the `Authorization` header to
  your origin
- CloudFront is configured to _not_ cache the response to
  `OPTIONS` requests

For more information, see [Configure CloudFront to
forward the Authorization header](add-origin-custom-headers.md#add-origin-custom-headers-forward-authorization "add-origin-custom-headers.md#add-origin-custom-headers-forward-authorization").

You can use HTTP or HTTPS to forward requests to your origin server. For more
information, see [Use HTTPS with CloudFront](using-https.md "using-https.md").

### Caching duration and minimum TTL

To control how long your objects stay in a CloudFront cache before CloudFront forwards
another request to your origin, you can:

- Configure your origin to add a `Cache-Control` or an
  `Expires` header field to each object.
- Specify a value for Minimum TTL in CloudFront cache behaviors.
- Use the default value of 24 hours.

For more information, see [Manage how long content stays in the cache
(expiration)](Expiration.md "Expiration.md").

### Client IP addresses

If a viewer sends a request to CloudFront and does not include an
`X-Forwarded-For` request header, CloudFront gets the IP address of the
viewer from the TCP connection, adds an `X-Forwarded-For` header that
includes the IP address, and forwards the request to the origin. For example, if
CloudFront gets the IP address `192.0.2.2` from the TCP connection, it
forwards the following header to the origin:

`X-Forwarded-For: 192.0.2.2`

If a viewer sends a request to CloudFront and includes an
`X-Forwarded-For` request header, CloudFront gets the IP address of the
viewer from the TCP connection, appends it to the end of the
`X-Forwarded-For` header, and forwards the request to the origin.
For example, if the viewer request includes `X-Forwarded-For:
 192.0.2.4,192.0.2.3` and CloudFront gets the IP address
`192.0.2.2` from the TCP connection, it forwards the following
header to the origin:

`X-Forwarded-For: 192.0.2.4,192.0.2.3,192.0.2.2`

Some applications, such as load balancers (including Elastic Load Balancing),
web application firewalls, reverse proxies, intrusion prevention systems, and
API Gateway, append the IP address of the CloudFront edge server that forwarded the
request onto the end of the `X-Forwarded-For` header. For example, if
CloudFront includes `X-Forwarded-For: 192.0.2.2` in a request that it
forwards to ELB and if the IP address of the CloudFront edge server is 192.0.2.199,
the request that your EC2 instance receives contains the following
header:

`X-Forwarded-For: 192.0.2.2,192.0.2.199`

###### Note

The `X-Forwarded-For` header contains IPv4 addresses (such as
192.0.2.44) and IPv6 addresses (such as
2001:0db8:85a3::8a2e:0370:7334).

Also note that the `X-Forwarded-For` header may be modified by
every node on the path to the current server (CloudFront). For more information,
see section 8.1 in [RFC 7239](https://datatracker.ietf.org/doc/html/rfc7239 "https://datatracker.ietf.org/doc/html/rfc7239").
You can also modify the header using CloudFront edge compute functions.

### Client-side SSL

authentication

CloudFront does not support client authentication with client-side SSL certificates.
If an origin requests a client-side certificate, CloudFront drops the request.

### Compression

For more information, see [Serve compressed files](ServingCompressedFiles.md "ServingCompressedFiles.md").

### Conditional requests

When CloudFront receives a request for an object that has expired from an edge
cache, it forwards the request to the origin either to get the latest version of
the object or to get confirmation from the origin that the CloudFront edge cache
already has the latest version. Typically, when the origin last sent the object
to CloudFront, it included an `ETag` value, a `LastModified`
value, or both values in the response. In the new request that CloudFront forwards to
the origin, CloudFront adds one or both of the following:

- An `If-Match` or `If-None-Match` header that
  contains the `ETag` value for the expired version of the
  object.
- An `If-Modified-Since` header that contains the
  `LastModified` value for the expired version of the
  object.

The origin uses this information to determine whether the object has been
updated and, therefore, whether to return the entire object to CloudFront or to return
only an HTTP 304 status code (not modified).

###### Note

`If-Modified-Since` and `If-None-Match` conditional requests are not supported when CloudFront is configured to forward cookies (all or a subset).

For more information, see [Cache content based on cookies](Cookies.md "Cookies.md").

### Cookies

You can configure CloudFront to forward cookies to your origin. For more
information, see [Cache content based on cookies](Cookies.md "Cookies.md").

### Cross-origin resource sharing

(CORS)

If you want CloudFront to respect cross-origin resource sharing settings, configure
CloudFront to forward the `Origin` header to your origin. For more
information, see [Cache content based on request headers](header-caching.md "header-caching.md").

### Encryption

You can require viewers to use HTTPS to send requests to CloudFront and require CloudFront
to forward requests to your custom origin by using the protocol that is used by
the viewer. For more information, see the following distribution
settings:

- [Viewer protocol
  policy](DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy "DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy")
- [Protocol (custom origins
  only)](DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy "DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy")

CloudFront forwards HTTPS requests to the origin server using the SSLv3, TLSv1.0, TLSv1.1,
TLSv1.2, and TLSv1.3 protocols. For custom origins, you can choose the SSL
protocols that you want CloudFront to use when communicating with your origin:

- If you're using the CloudFront console, choose protocols by using the
  **Origin SSL Protocols** check boxes. For more
  information, see [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").
- If you're using the CloudFront API, specify protocols by using the
  `OriginSslProtocols` element. For more information, see
  [OriginSslProtocols](../../../cloudfront/latest/APIReference/API_OriginSslProtocols.md "../../../cloudfront/latest/APIReference/API_OriginSslProtocols.md") and [DistributionConfig](../../../cloudfront/latest/APIReference/API_DistributionConfig.md "../../../cloudfront/latest/APIReference/API_DistributionConfig.md") in the
  _Amazon CloudFront API Reference_.

If the origin is an Amazon S3 bucket, CloudFront will default to TLSv1.3.

###### Important

Other versions of SSL and TLS are not supported.

For more information about using HTTPS with CloudFront, see [Use HTTPS with CloudFront](using-https.md "using-https.md"). For lists of the
ciphers that CloudFront supports for HTTPS communication between viewers and CloudFront, and
between CloudFront and your origin, see [Supported
protocols and ciphers between viewers and CloudFront](secure-connections-supported-viewer-protocols-ciphers.md "secure-connections-supported-viewer-protocols-ciphers.md").

### GET requests that include a

body

If a viewer `GET` request includes a body, CloudFront returns an HTTP
status code 403 (Forbidden) to the viewer.

### HTTP methods

If you configure CloudFront to process all of the HTTP methods that it supports,
CloudFront accepts the following requests from viewers and forwards them to your
custom origin:

- `DELETE`
- `GET`
- `HEAD`
- `OPTIONS`
- `PATCH`
- `POST`
- `PUT`

CloudFront always caches responses to `GET` and `HEAD`
requests. You can also configure CloudFront to cache responses to `OPTIONS`
requests. CloudFront does not cache responses to requests that use the other
methods.

For information about configuring whether your custom origin processes these
methods, see the documentation for your origin.

###### Important

If you configure CloudFront to accept and forward to your origin all of the HTTP
methods that CloudFront supports, configure your origin server to handle all
methods. For example, if you configure CloudFront to accept and forward these
methods because you want to use `POST`, you must configure your
origin server to handle `DELETE` requests appropriately so
viewers can't delete resources that you don't want them to. For more
information, see the documentation for your HTTP server.

### HTTP request headers and CloudFront

behavior (custom and Amazon S3 origins)

The following table lists HTTP request headers that you can forward to both
custom and Amazon S3 origins (with the exceptions that are noted). For each header,
the table includes information about the following:

- CloudFront behavior if you don't configure CloudFront to forward the header to
  your origin, which causes CloudFront to cache your objects based on header
  values.
- Whether you can configure CloudFront to cache objects based on header values
  for that header.

You can configure CloudFront to cache objects based on values in the
`Date` and `User-Agent` headers, but we don't
recommend it. These headers have many possible values, and caching based
on their values would cause CloudFront to forward significantly more requests
to your origin.

For more information about caching based on header values, see [Cache content based on request headers](header-caching.md "header-caching.md").

| Header                         | Behavior if you don't configure CloudFront to cache based on header<br>values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Caching based on header values is supported |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Other-defined headers          | **Legacy cache settings**<br>– CloudFront forwards the headers to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Accept`                       | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Accept-Charset`               | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Accept-Encoding`              | If the value contains `gzip` or<br>`br`, CloudFront forwards a normalized<br>`Accept-Encoding` header to your<br>origin.<br>For more information, see [Compression support](cache-key-understand-cache-policy.md#cache-policy-compressed-objects "cache-key-understand-cache-policy.md#cache-policy-compressed-objects") and<br>[Serve compressed files](ServingCompressedFiles.md "ServingCompressedFiles.md").                                                                                                                                                                                                                                                      | Yes                                         |
| `Accept-Language`              | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Authorization`                | • `GET` and `HEAD` requests<br>– CloudFront removes the `Authorization`<br>header field before forwarding the request to your<br>origin.<br>• `OPTIONS` requests – CloudFront<br>removes the `Authorization` header field<br>before forwarding the request to your origin if you<br>configure CloudFront to cache responses to<br>`OPTIONS` requests.<br>CloudFront forwards the `Authorization`<br>header field to your origin if you do not configure<br>CloudFront to cache responses to OPTIONS requests.<br>• `DELETE`, `PATCH`,<br>`POST`, and `PUT` requests<br>– CloudFront does not remove the header field<br>before forwarding the request to your origin. | Yes                                         |
| `Cache-Control`                | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `CloudFront-Forwarded-Proto`   | CloudFront does not add the header before forwarding the request<br>to your origin.<br>For more information, see [Configure caching based on the<br>protocol of the request](header-caching.md#header-caching-web-protocol "header-caching.md#header-caching-web-protocol").                                                                                                                                                                                                                                                                                                                                                                                          | Yes                                         |
| `CloudFront-Is-Desktop-Viewer` | CloudFront does not add the header before forwarding the request<br>to your origin.<br>For more information, see [Configure caching based on the device<br>type](header-caching.md#header-caching-web-device "header-caching.md#header-caching-web-device").                                                                                                                                                                                                                                                                                                                                                                                                          | Yes                                         |
| `CloudFront-Is-Mobile-Viewer`  | CloudFront does not add the header before forwarding the request<br>to your origin.<br>For more information, see [Configure caching based on the device<br>type](header-caching.md#header-caching-web-device "header-caching.md#header-caching-web-device").                                                                                                                                                                                                                                                                                                                                                                                                          | Yes                                         |
| `CloudFront-Is-Tablet-Viewer`  | CloudFront does not add the header before forwarding the request<br>to your origin.<br>For more information, see [Configure caching based on the device<br>type](header-caching.md#header-caching-web-device "header-caching.md#header-caching-web-device").                                                                                                                                                                                                                                                                                                                                                                                                          | Yes                                         |
| `CloudFront-Viewer-Country`    | CloudFront does not add the header before forwarding the request<br>to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes                                         |
| `Connection`                   | CloudFront replaces this header with `Connection:<br>Keep-Alive` before forwarding the request to your<br>origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No                                          |
| `Content-Length`               | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Content-MD5`                  | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Content-Type`                 | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Cookie`                       | If you configure CloudFront to forward cookies, it will forward<br>the `Cookie` header field to your origin. If you<br>don't, CloudFront removes the `Cookie` header field.<br>For more information, see [Cache content based on cookies](Cookies.md "Cookies.md").                                                                                                                                                                                                                                                                                                                                                                                                   | No                                          |
| `Date`                         | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes, but not recommended                    |
| `Expect`                       | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `From`                         | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Host`                         | CloudFront sets the value to the domain name of the origin that<br>is associated with the requested object.<br>You can't cache based on the Host header for Amazon S3 or MediaStore<br>origins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes (custom)<br>No (S3 and MediaStore)      |
| `If-Match`                     | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `If-Modified-Since`            | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `If-None-Match`                | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `If-Range`                     | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `If-Unmodified-Since`          | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Max-Forwards`                 | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Origin`                       | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Pragma`                       | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Proxy-Authenticate`           | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Proxy-Authorization`          | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Proxy-Connection`             | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Range`                        | CloudFront forwards the header to your origin. For more<br>information, see [How CloudFront processes partial requests for an object (range<br>GETs)](RangeGETs.md "RangeGETs.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes, by default                             |
| `Referer`                      | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Request-Range`                | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `TE`                           | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Trailer`                      | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Transfer-Encoding`            | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `Upgrade`                      | CloudFront removes the header, unless you've established a<br>WebSocket connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No (except for WebSocket connections)       |
| `User-Agent`                   | CloudFront replaces the value of this header field with<br>`Amazon CloudFront`. If you want CloudFront to<br>cache your content based on the device the user is using,<br>see [Configure caching based on the device<br>type](header-caching.md#header-caching-web-device "header-caching.md#header-caching-web-device").                                                                                                                                                                                                                                                                                                                                             | Yes, but not recommended                    |
| `Via`                          | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `Warning`                      | CloudFront forwards the header to your origin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `X-Amz-Cf-Id`                  | CloudFront adds the header to the viewer request before<br>forwarding the request to your origin. The header value<br>contains an encrypted string that uniquely identifies the<br>request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                          |
| `X-Edge-*`                     | CloudFront removes all `X-Edge-*` headers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No                                          |
| `X-Forwarded-For`              | CloudFront forwards the header to your origin. For more<br>information, see [Client IP addresses](#RequestCustomIPAddresses "#RequestCustomIPAddresses").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes                                         |
| `X-Forwarded-Proto`            | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |
| `X-HTTP-Method-Override`       | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                                         |
| `X-Real-IP`                    | CloudFront removes the header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                          |

### HTTP version

CloudFront forwards requests to your custom origin using HTTP/1.1.

### Maximum length of a

request and maximum length of a URL

The maximum length of a request, including the path, the query string (if
any), and headers, is 20,480 bytes.

CloudFront constructs a URL from the request. The maximum length of this URL is 8192
bytes.

If a request or a URL exceeds these maximums, CloudFront returns HTTP status code
413, Request Entity Too Large, to the viewer, and then terminates the TCP
connection to the viewer.

### OCSP stapling

When a viewer submits an HTTPS request for an object, either CloudFront or the
viewer must confirm with the certificate authority (CA) that the SSL certificate
for the domain has not been revoked. OCSP stapling speeds up certificate
validation by allowing CloudFront to validate the certificate and to cache the
response from the CA, so the client doesn't need to validate the certificate
directly with the CA.

The performance improvement of OCSP stapling is more pronounced when CloudFront
receives numerous HTTPS requests for objects in the same domain. Each server in
a CloudFront edge location must submit a separate validation request. When CloudFront
receives a lot of HTTPS requests for the same domain, every server in the edge
location soon has a response from the CA that it can "staple" to a packet in the
SSL handshake; when the viewer is satisfied that the certificate is valid, CloudFront
can serve the requested object. If your distribution doesn't get much traffic in
a CloudFront edge location, new requests are more likely to be directed to a server
that hasn't validated the certificate with the CA yet. In that case, the viewer
separately performs the validation step and the CloudFront server serves the object.
That CloudFront server also submits a validation request to the CA, so the next time
it receives a request that includes the same domain name, it has a validation
response from the CA.

### Persistent

connections

When CloudFront gets a response from your origin, it tries to maintain the
connection for several seconds in case another request arrives during that
period. Maintaining a persistent connection saves the time required to
re-establish the TCP connection and perform another TLS handshake for subsequent
requests.

For more information, including how to configure the duration of persistent
connections, see [Keep-alive timeout (custom
and VPC origins only)](DownloadDistValuesOrigin.md#DownloadDistValuesOriginKeepaliveTimeout "DownloadDistValuesOrigin.md#DownloadDistValuesOriginKeepaliveTimeout") in the section
[All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

### Protocols

CloudFront forwards HTTP or HTTPS requests to the origin server based on the
following:

- The protocol of the request that the viewer sends to CloudFront, either HTTP
  or HTTPS.
- The value of the **Origin Protocol Policy** field in
  the CloudFront console or, if you're using the CloudFront API, the
  `OriginProtocolPolicy` element in the
  `DistributionConfig` complex type. In the CloudFront console,
  the options are **HTTP Only**, **HTTPS
  Only**, and **Match Viewer**.

If you specify **HTTP Only** or **HTTPS
Only**, CloudFront forwards requests to the origin server using the
specified protocol, regardless of the protocol in the viewer request.

If you specify **Match Viewer**, CloudFront forwards requests to
the origin server using the protocol in the viewer request. Note that CloudFront
caches the object only once even if viewers make requests using both HTTP and
HTTPS protocols.

###### Important

If CloudFront forwards a request to the origin using the HTTPS protocol, and if
the origin server returns an invalid certificate or a self-signed
certificate, CloudFront drops the TCP connection.

For information about how to update a distribution using the CloudFront console, see
[Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md"). For information about how to
update a distribution using the CloudFront API, go to [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") in
the _Amazon CloudFront API Reference_.

### Query strings

You can configure whether CloudFront forwards query string parameters to your
origin. For more information, see [Cache content based on query string
parameters](QueryStringParameters.md "QueryStringParameters.md").

### Origin connection timeout and

attempts

_Origin
connection timeout_ is the number of seconds that CloudFront waits when
trying to establish a connection to the origin.

_Origin connection attempts_ is the number of
times that CloudFront attempts to connect to the origin.

Together, these settings determine how long CloudFront tries to connect to the
origin before failing over to the secondary origin (in the case of an origin
group) or returning an error response to the viewer. By default, CloudFront waits as
long as 30 seconds (3 attempts of 10 seconds each) before attempting to connect
to the secondary origin or returning an error response. You can reduce this time
by specifying a shorter connection timeout, fewer attempts, or both.

For more information, see [Control origin timeouts and
attempts](high_availability_origin_failover.md#controlling-attempts-and-timeouts "high_availability_origin_failover.md#controlling-attempts-and-timeouts").

### Origin response timeout

The _origin response timeout_, also known as
the _origin read timeout_ or _origin request timeout_, applies to both of the
following:

- The amount of time, in seconds, that CloudFront waits for a response after
  forwarding a request to the origin.
- The amount of time, in seconds, that CloudFront waits after receiving a
  packet of a response from the origin and before receiving the next
  packet.

CloudFront behavior depends on the HTTP method of the viewer request:

- `GET` and `HEAD` requests – If the origin
  doesn’t respond or stops responding within the duration of the response
  timeout, CloudFront drops the connection. If the specified number of [origin connection
  attempts](DownloadDistValuesOrigin.md#origin-connection-attempts "DownloadDistValuesOrigin.md#origin-connection-attempts") is more than 1, CloudFront tries again to get a complete
  response. CloudFront tries up to 3 times, as determined by the value of the
  _origin connection attempts_
  setting. If the origin doesn’t respond during the final attempt, CloudFront
  doesn’t try again until it receives another request for content on the
  same origin.
- `DELETE`, `OPTIONS`, `PATCH`,
  `PUT`, and `POST` requests – If the
  origin doesn’t respond for the duration of the read timeout, CloudFront drops
  the connection and doesn’t try again to contact the origin. The client
  can resubmit the request if necessary.

For more information, including how to configure the origin response timeout,
see [Response timeout](DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout "DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout").

### Simultaneous requests for the

same object (request collapsing)

When a CloudFront edge location receives a request for
an object and the object isn't in the cache or the cached object is
expired, CloudFront immediately sends the request to the origin. However, if there are
simultaneous requests for the same object—that is, if additional requests for
the same object (with the same cache key) arrive at the edge location before
CloudFront receives the response to the first request—CloudFront pauses before forwarding
the additional requests to the origin. This brief pause helps to reduce the load
on the origin. CloudFront sends the response from the original request to all the
requests that it received while it was paused. This is called
_request collapsing_. In CloudFront logs, the first
request is identified as a `Miss` in the
`x-edge-result-type` field, and the collapsed requests are identified
as a `Hit`. For more information about CloudFront logs, see
[CloudFront and edge function logging](logging.md "logging.md").

CloudFront only collapses requests that share a [cache
key](understanding-the-cache-key.md "understanding-the-cache-key.md"). If the additional requests do not share the same cache
key because, for example, you configured CloudFront to cache based on request headers
or cookies or query strings, CloudFront forwards all the requests with a unique cache
key to your origin.

If you want to prevent all request collapsing, you can use the managed cache policy `CachingDisabled`, which also prevents caching.
For more information, see [Use managed cache policies](using-managed-cache-policies.md "using-managed-cache-policies.md").

If you want to prevent request collapsing for specific objects, you can
set the minimum TTL for the cache behavior to 0 _and_ configure the origin to send `Cache-Control:
 private`, `Cache-Control: no-store`, `Cache-Control:
 no-cache`, `Cache-Control: max-age=0`, or
`Cache-Control: s-maxage=0`. These configurations will increase
the load on your origin and introduce additional latency for the simultaneous
requests that are paused while CloudFront waits for the response to the first
request.

###### Important

Currently, CloudFront doesn't support request collapsing if you enable cookie forwarding in the [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md"), the [origin request
policy](controlling-origin-requests.md "controlling-origin-requests.md"), or the legacy cache settings.

### `User-Agent`

header

If you want CloudFront to cache different versions of your objects based on
the device that a user is using to view your content, we recommend that you
configure CloudFront to forward one or more of the following headers to your custom
origin:

- `CloudFront-Is-Desktop-Viewer`
- `CloudFront-Is-Mobile-Viewer`
- `CloudFront-Is-SmartTV-Viewer`
- `CloudFront-Is-Tablet-Viewer`

Based on the value of the `User-Agent` header, CloudFront sets the value
of these headers to `true` or `false` before forwarding
the request to your origin. If a device falls into more than one category, more
than one value might be `true`. For example, for some tablet devices,
CloudFront might set both `CloudFront-Is-Mobile-Viewer` and
`CloudFront-Is-Tablet-Viewer` to `true`. For more
information about configuring CloudFront to cache based on request headers, see [Cache content based on request headers](header-caching.md "header-caching.md").

You can configure CloudFront to cache objects based on values in the
`User-Agent` header, but we don't recommend it. The
`User-Agent` header has many possible values, and caching based
on those values would cause CloudFront to forward significantly more requests to your
origin.

If you do not configure CloudFront to cache objects based on values in the
`User-Agent` header, CloudFront adds a `User-Agent` header
with the following value before it forwards a request to your origin:

`User-Agent = Amazon CloudFront`

CloudFront adds this header regardless of whether the request from the viewer
includes a `User-Agent` header. If the request from the viewer
includes a `User-Agent` header, CloudFront removes it.

## How CloudFront processes responses from

your custom origin

Learn how CloudFront processes responses from your custom origin.

###### Contents

- [100 Continue
  responses](RequestAndResponseBehaviorCustomOrigin.md#Response100Continue "RequestAndResponseBehaviorCustomOrigin.md#Response100Continue")
- [Caching](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomCaching "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomCaching")
- [Canceled requests](RequestAndResponseBehaviorCustomOrigin.md#response-custom-canceled-requests "RequestAndResponseBehaviorCustomOrigin.md#response-custom-canceled-requests")
- [Content negotiation](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomContentNegotiation "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomContentNegotiation")
- [Cookies](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomCookies "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomCookies")
- [Dropped TCP
  connections](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomDroppedTCPConnections "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomDroppedTCPConnections")
- [HTTP response headers that CloudFront
  removes or replaces](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomRemovedHeaders "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomRemovedHeaders")
- [Maximum cacheable file size](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomMaxFileSize "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomMaxFileSize")
- [Origin unavailable](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomOriginUnavailable "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomOriginUnavailable")
- [Redirects](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomRedirects "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomRedirects")
- [Transfer-Encoding
  header](RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomTransferEncoding "RequestAndResponseBehaviorCustomOrigin.md#ResponseCustomTransferEncoding")

### `100 Continue`

responses

Your origin cannot send more than one 100-Continue response to CloudFront. After the
first 100-Continue response, CloudFront expects an HTTP 200 OK response. If your
origin sends another 100-Continue response after the first one, CloudFront will return
an error.

### Caching

- Ensure that the origin server sets valid and accurate values for the
  `Date` and `Last-Modified` header
  fields.
- CloudFront normally respects a `Cache-Control: no-cache` header
  in the response from the origin. For an exception, see [Simultaneous requests for the
  same object (request collapsing)](#request-custom-traffic-spikes "#request-custom-traffic-spikes").

### Canceled requests

If an object is not in the edge cache, and if a viewer terminates a session
(for example, closes a browser) after CloudFront gets the object from your origin but
before it can deliver the requested object, CloudFront does not cache the object in
the edge location.

### Content negotiation

If your origin returns `Vary:*` in the response, and if the value
of **Minimum TTL** for the corresponding cache behavior is
**0**, CloudFront caches the object but still forwards every
subsequent request for the object to the origin to confirm that the cache
contains the latest version of the object. CloudFront doesn't include any conditional
headers, such as `If-None-Match` or `If-Modified-Since`.
As a result, your origin returns the object to CloudFront in response to every
request.

If your origin returns `Vary:*` in the response, and if the value
of **Minimum TTL** for the corresponding cache behavior is any
other value, CloudFront processes the `Vary` header as described in [HTTP response headers that CloudFront
removes or replaces](#ResponseCustomRemovedHeaders "#ResponseCustomRemovedHeaders").

### Cookies

If you enable cookies for a cache behavior, and if the origin returns cookies
with an object, CloudFront caches both the object and the cookies. Note that this
reduces cacheability for an object. For more information, see [Cache content based on cookies](Cookies.md "Cookies.md").

### Dropped TCP

connections

If the TCP connection between CloudFront and your origin drops while your origin is
returning an object to CloudFront, CloudFront behavior depends on whether your origin
included a `Content-Length` header in the response:

- **Content-Length header** – CloudFront
  returns the object to the viewer as it gets the object from your origin.
  However, if the value of the `Content-Length` header doesn't
  match the size of the object, CloudFront doesn't cache the object.
- **Transfer-Encoding: Chunked** –
  CloudFront returns the object to the viewer as it gets the object from your
  origin. However, if the chunked response is not complete, CloudFront does not
  cache the object.
- **No Content-Length header** –
  CloudFront returns the object to the viewer and caches it, but the object may
  not be complete. Without a `Content-Length` header, CloudFront
  cannot determine whether the TCP connection was dropped accidentally or
  on purpose.

We recommend that you configure your HTTP server to add a
`Content-Length` header to prevent CloudFront from caching partial
objects.

### HTTP response headers that CloudFront

removes or replaces

CloudFront removes or updates the following header fields before forwarding the
response from your origin to the viewer:

- `Set-Cookie` – If you configure CloudFront to forward
  cookies, it will forward the `Set-Cookie` header field to
  clients. For more information, see [Cache content based on cookies](Cookies.md "Cookies.md").
- `Trailer`
- `Transfer-Encoding` – If your origin returns this
  header field, CloudFront sets the value to `chunked` before
  returning the response to the viewer.
- `Upgrade`
- `Vary` – Note the following:
  - If you configure CloudFront to forward any of the device-specific
    headers to your origin
    (`CloudFront-Is-Desktop-Viewer`,
    `CloudFront-Is-Mobile-Viewer`,
    `CloudFront-Is-SmartTV-Viewer`,
    `CloudFront-Is-Tablet-Viewer`) and you configure
    your origin to return `Vary:User-Agent` to CloudFront, CloudFront
    returns `Vary:User-Agent` to the viewer. For more
    information, see [Configure caching based on the device
    type](header-caching.md#header-caching-web-device "header-caching.md#header-caching-web-device").
  - If you configure your origin to include either
    `Accept-Encoding` or `Cookie` in the
    `Vary` header, CloudFront includes the values in the
    response to the viewer.
  - If you configure CloudFront to forward headers to your origin, and
    if you configure your origin to return the header names to CloudFront
    in the `Vary` header (for example,
    `Vary:Accept-Charset,Accept-Language`), CloudFront
    returns the `Vary` header with those values to the
    viewer.
  - For information about how CloudFront processes a value of
    `*` in the `Vary` header, see [Content negotiation](#ResponseCustomContentNegotiation "#ResponseCustomContentNegotiation").
  - If you configure your origin to include any other values in
    the `Vary` header, CloudFront removes the values before
    returning the response to the viewer.

- `Via` – CloudFront sets the value to the following in the
  response to the viewer:

`Via:` `http-version`
`alphanumeric-string``.cloudfront.net
 (CloudFront)`

For example, the value is something like the following:

`Via: 1.1 1026589cc7887e7a0dc7827b4example.cloudfront.net
 (CloudFront)`

### Maximum cacheable file size

The maximum size of a response body that CloudFront saves in its cache is
50 GB. This includes
chunked transfer responses that don't specify the `Content-Length`
header value.

You can use CloudFront to cache an object that is larger than this size by using range
requests to request the objects in parts that are each 50 GB or smaller. CloudFront
caches these parts because each of them is 50 GB or smaller. After the viewer
retrieves all the parts of the object, it can reconstruct the original, larger
object. For more information, see [Use range requests to
cache large objects](RangeGETs.md#cache-large-objects-with-range-requests "RangeGETs.md#cache-large-objects-with-range-requests").

### Origin unavailable

If your origin server is unavailable and CloudFront gets a request for an object
that is in the edge cache but that has expired (for example, because the period
of time specified in the `Cache-Control max-age` directive has
passed), CloudFront either serves the expired version of the object or serves a custom
error page. For more information about CloudFront behavior when you've configured
custom error pages, see [How CloudFront processes errors when
you have configured custom error pages](HTTPStatusCodes.md#HTTPStatusCodes-custom-error-pages "HTTPStatusCodes.md#HTTPStatusCodes-custom-error-pages").

In some cases, an object that is seldom requested is evicted and is no longer
available in the edge cache. CloudFront can't serve an object that has been
evicted.

### Redirects

If you change the location of an object on the origin server, you can
configure your web server to redirect requests to the new location. After you
configure the redirect, the first time a viewer submits a request for the
object, CloudFront sends the request to the origin, and the origin responds with a
redirect (for example, `302 Moved Temporarily`). CloudFront caches the
redirect and returns it to the viewer. CloudFront does not follow the redirect.

You can configure your web server to redirect requests to one of the following
locations:

- The new URL of the object on the origin server. When the viewer
  follows the redirect to the new URL, the viewer bypasses CloudFront and goes
  straight to the origin. As a result, we recommend that you don't
  redirect requests to the new URL of the object on the origin.
- The new CloudFront URL for the object. When the viewer submits the request
  that contains the new CloudFront URL, CloudFront gets the object from the new
  location on your origin, caches it at the edge location, and returns the
  object to the viewer. Subsequent requests for the object will be served
  by the edge location. This avoids the latency and load associated with
  viewers requesting the object from the origin. However, every new
  request for the object will incur charges for two requests to
  CloudFront.

### `Transfer-Encoding`

header

CloudFront supports only the `chunked` value of the
`Transfer-Encoding` header. If your origin returns
`Transfer-Encoding: chunked`, CloudFront returns the object to the
client as the object is received at the edge location, and caches the object in
chunked format for subsequent requests.

If the viewer makes a `Range GET` request and the origin returns
`Transfer-Encoding: chunked`, CloudFront returns the entire object to
the viewer instead of the requested range.

We recommend that you use chunked encoding if the content length of your
response cannot be predetermined. For more information, see [Dropped TCP
connections](#ResponseCustomDroppedTCPConnections "#ResponseCustomDroppedTCPConnections").
