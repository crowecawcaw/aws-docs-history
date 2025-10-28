# Custom error pages and error

caching

You can have CloudFront return an object to the viewer (for example, an HTML file)
when your Amazon S3 or custom origin returns an HTTP 4xx or 5xx status code to CloudFront.
You can also specify how long an error response from your origin or a custom
error page is cached in CloudFront edge caches. For more information, see [Create a custom error page for specific
HTTP status codes](creating-custom-error-pages.md "creating-custom-error-pages.md").

###### Note

The following values aren't included in the Create Distribution wizard, so
you can configure custom error pages only when you update a
distribution.

###### Topics

- [HTTP error code](#DownloadDistValuesErrorCode "#DownloadDistValuesErrorCode")
- [Response page
  path](#DownloadDistValuesResponsePagePath "#DownloadDistValuesResponsePagePath")
- [HTTP response code](#DownloadDistValuesResponseCode "#DownloadDistValuesResponseCode")
- [Error caching minimum
  TTL (seconds)](#DownloadDistValuesErrorCachingMinTTL "#DownloadDistValuesErrorCachingMinTTL")

## HTTP error code

The HTTP status code for which you want CloudFront to return a custom error
page. You can configure CloudFront to return custom error pages for none, some, or
all of the HTTP status codes that CloudFront caches.

## Response page

path

The path to the custom error page (for example,
`/4xx-errors/403-forbidden.html`) that you want CloudFront
to return to a viewer when your origin returns the HTTP status code that you
specified for **Error Code** (for example, 403). If you
want to store your objects and your custom error pages in different
locations, your distribution must include a cache behavior for which the
following is true:

- The value of **Path Pattern** matches the path to
  your custom error messages. For example, suppose you saved custom
  error pages for 4xx errors in an Amazon S3 bucket in a directory named
  `/4xx-errors`. Your distribution must include
  a cache behavior for which the path pattern routes requests for your
  custom error pages to that location, for example,
  **/4xx-errors/\***.
- The value of **Origin** specifies the value of
  **Origin ID** for the origin that contains your
  custom error pages.

## HTTP response code

The HTTP status code that you want CloudFront to return to the viewer along with
the custom error page.

## Error caching minimum

TTL (seconds)

The minimum amount of time that you want CloudFront to cache error responses
from your origin server.
