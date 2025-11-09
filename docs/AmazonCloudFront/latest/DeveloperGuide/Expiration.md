# Manage how long content stays in the cache

(expiration)

You can control how long your files stay in a CloudFront cache before CloudFront forwards another
request to your origin. Reducing the duration allows you to serve dynamic content.
Increasing the duration means that your users get better performance because your files
are more likely to be served directly from the edge cache. A longer duration also
reduces the load on your origin.

Typically, CloudFront serves a file from an edge location until the cache duration that you
specified passes—that is, until the file expires. After it expires, the next time
the edge location gets a request for the file, CloudFront forwards the request to the origin
to verify that the cache contains the latest version of the file. The response from the
origin depends on whether the file has changed:

- If the CloudFront cache already has the latest version, the origin returns a status
  code `304 Not Modified`.
- If the CloudFront cache does not have the latest version, the origin returns a
  status code `200 OK` and the latest version of the file.
  If a file in an edge location isn't frequently requested, CloudFront might evict the
  file—remove the file before its expiration date—to make room for files that
  have been requested more recently.

We recommend managing your cache duration by updating your distribution's cache policy. If you opt out of using a cache policy, the default TTL (Time to Live) is 24 hours, but you can update the following settings to override the default:

- To change the cache duration for all files that match the same path pattern,
  you can change the CloudFront settings for **Minimum TTL**,
  **Maximum TTL**, and **Default TTL** for a
  cache behavior. For information about the individual settings, see [Minimum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL"), [Maximum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL"), and [Default TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesDefaultTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesDefaultTTL").
- To change the cache duration for an individual file, you can configure your
  origin to add a `Cache-Control` header with the `max-age`
  or `s-maxage` directive, or an `Expires` header to the
  file. For more information, see [Use headers to control cache
  duration for individual objects](#expiration-individual-objects "#expiration-individual-objects").
  For more information about how **Minimum TTL**, **Default
  TTL**, and **Maximum TTL** interact with the
  `max-age` and `s-maxage` directives and the
  `Expires` header field, see [Specify the amount of time that CloudFront caches
  objects](#ExpirationDownloadDist "#ExpirationDownloadDist").

You can also control how long errors (for example, `404 Not Found`) stay in
a CloudFront cache before CloudFront tries again to get the requested object by forwarding another
request to your origin. For more information, see [How CloudFront processes HTTP 4xx and 5xx status codes from
your origin](HTTPStatusCodes.md "HTTPStatusCodes.md").

###### Topics

- [Use headers to control cache
  duration for individual objects](#expiration-individual-objects "#expiration-individual-objects")
- [Serve stale (expired) content](#stale-content "#stale-content")
- [Specify the amount of time that CloudFront caches
  objects](#ExpirationDownloadDist "#ExpirationDownloadDist")
- [Add headers to your objects by using the Amazon S3
  console](#ExpirationAddingHeadersInS3 "#ExpirationAddingHeadersInS3")

## Use headers to control cache

duration for individual objects

You can use the `Cache-Control` and `Expires` headers to
control how long objects stay in the cache. Settings for **Minimum
TTL**, **Default TTL**, and **Maximum TTL** also affect cache duration, but here's an overview of how headers can
affect cache duration:

- The `Cache-Control max-age` directive lets you specify how long
  (in seconds) that you want an object to remain in the cache before CloudFront gets
  the object again from the origin server. The minimum expiration time CloudFront
  supports is 0 seconds. The maximum value is 100 years. Specify the value in
  the following format:

`Cache-Control:
 max-age=``seconds`

For example, the following directive tells CloudFront to keep the associated
object in the cache for 3600 seconds (one hour):

`Cache-Control: max-age=3600`

If you want objects to stay in CloudFront edge caches for a different duration
than they stay in browser caches, you can use the `Cache-Control
 max-age` and `Cache-Control s-maxage` directives
together. For more information, see [Specify the amount of time that CloudFront caches
objects](#ExpirationDownloadDist "#ExpirationDownloadDist").

- The `Expires` header field lets you specify an expiration date
  and time using the format specified in [RFC 2616, Hypertext Transfer Protocol -- HTTP/1.1 Section 3.3.1, Full
  Date](https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3.1 "https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3.1"), for example:

`Sat, 27 Jun 2015 23:59:59 GMT`

We recommend that you use the `Cache-Control max-age` directive instead
of the `Expires` header field to control object caching. If you specify
values both for `Cache-Control max-age` and for `Expires`,
CloudFront uses only the value of `Cache-Control max-age`.

For more information, see [Specify the amount of time that CloudFront caches
objects](#ExpirationDownloadDist "#ExpirationDownloadDist").

You cannot use the HTTP `Cache-Control` or `Pragma` header
fields in a `GET` request from a viewer to force CloudFront to go back to the
origin server for the object. CloudFront ignores those header fields in viewer
requests.

For more information about the `Cache-Control` and `Expires`
header fields, see the following sections in _RFC 2616, Hypertext Transfer
Protocol -- HTTP/1.1_:

- [Section 14.9 Cache Control](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 "https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9")
- [Section 14.21 Expires](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.21 "https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.21")

## Serve stale (expired) content

CloudFront supports the `Stale-While-Revalidate` and
`Stale-If-Error` cache control directives. You can use these
directives to specify how long stale content is available for viewers.

###### Topics

- [Stale-While-Revalidate](#stale-while-revalidate "#stale-while-revalidate")
- [Stale-If-Error](#stale-if-error-only "#stale-if-error-only")
- [Use both directives](#use-both-stale-directives "#use-both-stale-directives")

### `Stale-While-Revalidate`

This directive allows CloudFront to serve stale content from the cache while CloudFront
asynchronously fetches a fresh version from the origin. This improves latency as
viewers receive responses immediately from edge locations without having to wait
for the background fetch. Fresh content is loaded in the background for future
requests.

###### Example: `Stale-While-Revalidate`

CloudFront does the following when you set the `Cache-Control` header
to use these directives.

```
Cache-Control: max-age=3600, stale-while-revalidate=600
```

1. CloudFront will cache a response for one hour
   (`max-age=3600`).
2. If a request is made after this duration, CloudFront serves the stale
   content, while concurrently sending a request to the origin to
   revalidate and refresh the cached content.
3. While the content is being revalidated, CloudFront serves the stale
   content up to 10 minutes
   (`stale-while-revalidate=600`).

###### Note

CloudFront will serve the stale content up to the value of the
`stale-while-revalidate` directive or the value of the CloudFront
[maximum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL"), whichever
is less. After the maximum TTL duration, the stale object won't be
available from the edge cache, regardless of the
`stale-while-revalidate` value.

### `Stale-If-Error`

This directive allows CloudFront to serve stale content from the cache if the origin
is unreachable or returns an error code that is between 500 and 600. This
ensures that viewers can access content even during an origin outage.

###### Example: `Stale-If-Error`

CloudFront does the following when you set the `Cache-Control` header
to use these directives.

```
Cache-Control: max-age=3600, stale-if-error=86400
```

1. CloudFront caches the response for one hour
   (`max-age=3600`).
2. If the origin is down or returns an error after this duration,
   CloudFront continues to serve the stale content for up to 24 hours
   (`stale-if-error=86400`)
3. If you configured custom error responses, CloudFront will attempt to
   serve the stale content if an error is encountered within the
   specified `stale-if-error` duration. If the stale content
   is unavailable, CloudFront will then serve the custom error responses that
   you configured for the corresponding error status code. For more
   information, see [Generate custom error responses](GeneratingCustomErrorResponses.md "GeneratingCustomErrorResponses.md").

###### Notes

- CloudFront will serve the stale content up to the value of the
  `stale-if-error` directive or the value of the CloudFront
  [maximum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMaxTTL"),
  whichever is less. After the maximum TTL duration, the stale object
  won't be available from the edge cache, regardless of the
  `stale-if-error` value.
- If you don't configure `stale-if-error` or custom error
  responses, CloudFront will return the stale object or forward the error
  response back to viewer, depending on whether the requested object
  is in the edge cache or not. For more information, see [How CloudFront processes errors if
  you haven't configured custom error pages](HTTPStatusCodes.md#HTTPStatusCodes-no-custom-error-pages "HTTPStatusCodes.md#HTTPStatusCodes-no-custom-error-pages").

### Use both directives

Both `stale-while-revalidate` and `stale-if-error` are
independent cache control directives that you can use together to reduce latency
and to add a buffer for your origin to respond or recover.

###### Example: Using both directives

CloudFront does the following when you set the `Cache-Control` header
to use the following directives.

```
Cache-Control: max-age=3600, stale-while-revalidate=600, stale-if-error=86400
```

1. CloudFront caches the response for one hour (`max-age=3600`).
2. If a request is made after this duration, CloudFront serves the stale
   content for up to 10 minutes
   (`stale-while-revalidate=600`) while the content is
   being revalidated.
3. If the origin server returns an error while CloudFront attempts to
   revalidate the content, CloudFront will continue to serve the stale
   content for up to 24 hours
   (`stale-if-error=86400`).

Caching is a balance between performance and freshness. Using directives like
`stale-while-revalidate` and `stale-if-error` can
enhance performance and user experience, but make sure the configurations align
with how fresh you want your content to be. Stale content directives are best
suited for use cases where content needs to be refreshed but having the latest
version is non-essential. Additionally, if your content doesn’t change or rarely
changes, `stale-while-revalidate` could add unnecessary network
requests. Instead, consider setting a long cache duration.

## Specify the amount of time that CloudFront caches

objects

To control the amount of time that CloudFront keeps an object in the cache before
sending another request to the origin, you can:

- Set the minimum, maximum, and default TTL values in a CloudFront distribution's
  cache behavior. You can set these values in a [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md") attached to the
  cache behavior (recommended), or in the legacy cache settings.
- Include the `Cache-Control` or `Expires` header in
  responses from the origin. These headers also help determine how long a
  browser keeps an object in the browser cache before sending another request
  to CloudFront.

The following table explains how the `Cache-Control` and
`Expires` headers sent from the origin work together with the TTL
settings in a cache behavior to affect caching.

| Origin headers                                                                                            | Minimum TTL = 0                                                                                                                                                                                                                                                                                | Minimum TTL > 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **The origin adds a `Cache-Control:<br>max-age` directive to the object**                                 | **CloudFront caching**<br>CloudFront caches the object for the lesser of the value of the<br>`Cache-Control: max-age` directive or the value<br>of the CloudFront maximum TTL.<br>**Browser caching**<br>Browsers cache the object for the value of the<br>`Cache-Control: max-age` directive. | **CloudFront caching**<br>CloudFront caching depends on the values of the CloudFront minimum TTL and<br>maximum TTL and the `Cache-Control max-age`<br>directive:<br>• If minimum TTL < `max-age` < maximum<br>TTL, then CloudFront caches the object for the value of the<br>`Cache-Control: max-age`<br>directive.<br>• If `max-age` < minimum TTL, then CloudFront<br>caches the object for the value of the CloudFront minimum<br>TTL.<br>• If `max-age` > maximum TTL, then CloudFront<br>caches the object for the value of the CloudFront maximum<br>TTL.<br>**Browser caching**<br>Browsers cache the object for the value of the<br>`Cache-Control: max-age` directive.       |
| **The origin does not add a<br>`Cache-Control: max-age` directive to the<br>object**                      | **CloudFront caching**<br>CloudFront caches the object for the value of the CloudFront default<br>TTL.<br>**Browser caching**<br>Depends on the browser.                                                                                                                                       | **CloudFront caching**<br>CloudFront caches the object for the greater of the value of the<br>CloudFront minimum TTL or default TTL.<br>**Browser caching**<br>Depends on the browser.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **The origin adds `Cache-Control:<br>max-age` and `Cache-Control: s-maxage`<br>directives to the object** | **CloudFront caching**<br>CloudFront caches the object for the lesser of the value of the<br>`Cache-Control: s-maxage` directive or the value<br>of the CloudFront maximum TTL.<br>**Browser caching**<br>Browsers cache the object for the value of the<br>`Cache-Control max-age` directive. | **CloudFront caching**<br>CloudFront caching depends on the values of the CloudFront minimum TTL and<br>maximum TTL and the `Cache-Control: s-maxage`<br>directive:<br>• If minimum TTL < `s-maxage` < maximum<br>TTL, then CloudFront caches the object for the value of the<br>`Cache-Control: s-maxage`<br>directive.<br>• If `s-maxage` < minimum TTL, then CloudFront<br>caches the object for the value of the CloudFront minimum<br>TTL.<br>• If `s-maxage` > maximum TTL, then CloudFront<br>caches the object for the value of the CloudFront maximum<br>TTL.<br>**Browser caching**<br>Browsers cache the object for the value of the<br>`Cache-Control: max-age` directive. |
| **The origin adds an `Expires`<br>header to the object**                                                  | **CloudFront caching**<br>CloudFront caches the object until the date in the<br>`Expires` header or for the value of the CloudFront<br>maximum TTL, whichever is sooner.<br>**Browser caching**<br>Browsers cache the object until the date in the<br>`Expires` header.                        | **CloudFront caching**<br>CloudFront caching depends on the values of the CloudFront minimum TTL and<br>maximum TTL and the `Expires` header:<br>• If minimum TTL < `Expires` < maximum<br>TTL, then CloudFront caches the object until the date and time<br>in the `Expires` header.<br>• If `Expires` < minimum TTL, then CloudFront<br>caches the object for the value of the CloudFront minimum<br>TTL.<br>• If `Expires` > maximum TTL, then CloudFront<br>caches the object for the value of the CloudFront maximum<br>TTL.<br>**Browser caching**<br>Browsers cache the object until the date and time in the<br>`Expires` header.                                              |
| **Origin adds `Cache-Control:<br>no-cache`, `no-store`, and/or<br>`private` directives to the<br>object** | CloudFront and browsers respect the headers.                                                                                                                                                                                                                                                   | **CloudFront caching**<br>CloudFront caches the object for the value of the CloudFront minimum TTL.<br>[See the warning below this<br>table](#stale-if-error "#stale-if-error").<br>**Browser caching**<br>Browsers respect the headers.                                                                                                                                                                                                                                                                                                                                                                                                                                               |

###### Warning

- If your minimum TTL is greater than 0, CloudFront uses the cache policy’s
  minimum TTL, even if the `Cache-Control: no-cache`,
  `no-store`, and/or `private` directives are
  present in the origin headers.

      + If the origin is reachable, CloudFront gets the object from the
       origin and returns it to the viewer.
      + If the origin is unreachable and the minimum *or* maximum TTL value is greater
       than 0, CloudFront will serve the object that it got from the origin
       previously.

  To avoid this behavior, include the `Cache-Control:
 stale-if-error=0` directive with the object returned from the
  origin. This causes CloudFront to return an error in response to future
  requests if the origin is unreachable, rather than returning the object
  that it got from the origin previously.

- CloudFront doesn't cache the HTTP 501 status code (Not Implemented) from an
  S3 origin when the origin headers include the `Cache-Control:
no-cache`, `no-store`, and/or `private`
  directives. This is the default behavior for an S3 origin, even if your
  [minimum TTL](DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL "DownloadDistValuesCacheBehavior.md#DownloadDistValuesMinTTL") setting
  is greater than 0.

For information about how to change settings for distributions using the CloudFront
console, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md"). For information about how to change
settings for distributions using the CloudFront API, see [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md").

## Add headers to your objects by using the Amazon S3

console

You can add the `Cache-Control` or `Expires` header field to your
Amazon S3 objects. To do so, you modify the metadata fields for the object.

###### To add a `Cache-Control` or `Expires` header field to Amazon S3

objects

1. Follow the procedure in the **Replacing system-defined metadata**
   section on the [Editing object
   metadata in the Amazon S3 console](../../../AmazonS3/latest/userguide/add-object-metadata.md "../../../AmazonS3/latest/userguide/add-object-metadata.md") topic in the
   _Amazon S3 User Guide_.
2. For **Key**, choose the name of the header that you are
   adding (**Cache-Control** or
   **Expires**).
3. For **Value**, enter a header value. For example, for a
   `Cache-Control` header, you could enter
   `max-age=86400`. For `Expires`, you could enter an
   expiration date and time such as `Wed, 30 Jun 2021 09:28:00
GMT`.
4. Follow the rest of the procedure to save your metadata changes.
