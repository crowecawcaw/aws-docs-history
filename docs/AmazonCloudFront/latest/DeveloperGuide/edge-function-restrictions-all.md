# Restrictions on all edge
 functions

The following restrictions apply to all edge functions, both CloudFront Functions and
 Lambda@Edge.

###### Topics

* [AWS account
 ownership](#function-restrictions-account-ownership "#function-restrictions-account-ownership")
* [Combining CloudFront Functions
 with Lambda@Edge](#function-restrictions-combining-functions "#function-restrictions-combining-functions")
* [HTTP status codes](#function-restrictions-status-codes "#function-restrictions-status-codes")
* [HTTP headers](#function-restrictions-headers "#function-restrictions-headers")
* [Query strings](#function-restrictions-query-strings "#function-restrictions-query-strings")
* [URI](#function-restrictions-uri "#function-restrictions-uri")
* [URI, query string, and headers
 encoding](#function-restrictions-encoding "#function-restrictions-encoding")
* [Microsoft Smooth
 Streaming](#function-restrictions-microsoft-smooth-streaming "#function-restrictions-microsoft-smooth-streaming")
* [Tagging](#function-restrictions-tagging "#function-restrictions-tagging")

## AWS account
 ownership


To associate an edge function with a CloudFront distribution, the function and
 distribution must be owned by the same AWS account.


## Combining CloudFront Functions
 with Lambda@Edge


For a given cache behavior, the following restrictions apply:



* Each event type (viewer request, origin request, origin response, and
 viewer response) can have only one edge function association.
* You can’t combine CloudFront Functions and Lambda@Edge in viewer events (viewer
 request and viewer response).

All other combinations of edge functions are allowed. The following table explains
 the allowed combinations.




|  |  |
| --- | --- |
|  | **CloudFront Functions** |
| **Viewer request** | **Viewer response** |
| **Lambda@Edge** | **Viewer request** | Not allowed | Not allowed |
| **Origin request** | Allowed | Allowed | | **Origin response** | Allowed | Allowed |
| **Viewer response** | Not allowed | Not allowed | ## HTTP status codes CloudFront doesn't invoke edge functions for viewer response events when the origin returns HTTP status code 400 or higher. Lambda@Edge functions for origin response events are invoked for *all* origin responses, including when the origin returns HTTP status code 400 or higher. For more information, see [Update HTTP responses in origin response triggers](lambda-generating-http-responses.md#lambda-updating-http-responses "lambda-generating-http-responses.md#lambda-updating-http-responses"). ## HTTP headers Certain HTTP headers are disallowed, which means they're not exposed to edge functions and functions can't add them. Other headers are read-only, which means functions can read them but can't add, modify, or delete them. ###### Topics <br>• [Disallowed headers](#function-restrictions-disallowed-headers "#function-restrictions-disallowed-headers") <br>• [Read-only headers](#function-restrictions-read-only-headers "#function-restrictions-read-only-headers") ### Disallowed headers The following HTTP headers are not exposed to edge functions, and functions can't add them. If your function adds one of these headers, it fails CloudFront validation and CloudFront returns HTTP status code 502 (Bad Gateway) to the viewer. <br>• `Connection` <br>• `Expect` <br>• `Keep-Alive` <br>• `Proxy-Authenticate` <br>• `Proxy-Authorization` <br>• `Proxy-Connection` <br>• `Trailer` <br>• `Upgrade` <br>• `X-Accel-Buffering` <br>• `X-Accel-Charset` <br>• `X-Accel-Limit-Rate` <br>• `X-Accel-Redirect` <br>• `X-Amz-Cf-*` <br>• `X-Amzn-Auth` <br>• `X-Amzn-Cf-Billing` <br>• `X-Amzn-Cf-Id` <br>• `X-Amzn-Cf-Xff` <br>• `X-Amzn-Errortype` <br>• `X-Amzn-Fle-Profile` <br>• `X-Amzn-Header-Count` <br>• `X-Amzn-Header-Order` <br>• `X-Amzn-Lambda-Integration-Tag` <br>• `X-Amzn-RequestId` <br>• `X-Cache` <br>• `X-Edge-*` <br>• `X-Forwarded-Proto` <br>• `X-Real-IP` ### Read-only headers The following headers are read-only. Your function can read them and use them as input to the function logic, but it can't change the values. If your function adds or edits a read-only header, the request fails CloudFront validation and CloudFront returns HTTP status code 502 (Bad Gateway) to the viewer. #### Read-only headers in viewer request events The following headers are read-only in viewer request events. <br>• `Content-Length` <br>• `Host` <br>• `Transfer-Encoding` <br>• `Via` #### Read-only headers in origin request events (Lambda@Edge only) The following headers are read-only in origin request events, which exist only in Lambda@Edge. <br>• `Accept-Encoding` <br>• `Content-Length` <br>• `If-Modified-Since` <br>• `If-None-Match` <br>• `If-Range` <br>• `If-Unmodified-Since` <br>• `Transfer-Encoding` <br>• `Via` #### Read-only headers in origin response events (Lambda@Edge only) The following headers are read-only in origin response events, which exist only in Lambda@Edge. <br>• `Transfer-Encoding` <br>• `Via` #### Read-only headers in viewer response events The following headers are read-only in viewer response events for both CloudFront Functions and Lambda@Edge. <br>• `Warning` <br>• `Via` The following headers are read-only in viewer response events for Lambda@Edge. <br>• `Content-Length` <br>• `Content-Encoding` <br>• `Transfer-Encoding` ## Query strings The following restrictions apply to functions that read, update, or create a query string in a request URI. <br>• (Lambda@Edge only) To access the query string in an origin request or origin response function, your cache policy or origin request policy must be set to **All** for **Query strings**. <br>• A function can create or update a query string for viewer request and origin request events (origin request events exist only in Lambda@Edge). <br>• A function can read a query string, but cannot create or update one, for origin response and viewer response events (origin response events exist only in Lambda@Edge). <br>• If a function creates or updates a query string, the following restrictions apply: + The query string can't include spaces, control characters, or the fragment identifier (`#`). + The total size of the URI, including the query string, must be less than 8,192 characters. + We recommend that you use percent encoding for the URI and query string. For more information, see [URI, query string, and headers encoding](#function-restrictions-encoding "#function-restrictions-encoding"). ## URI If a function changes the URI for a request, that doesn't change the cache behavior for the request or the origin that the request is forwarded to. The total size of the URI, including the query string, must be less than 8,192 characters. ## URI, query string, and headers encoding The values for the URI, query string, and headers that are passed to edge functions are UTF-8 encoded. Your function should use UTF-8 encoding for the URI, query string, and header values that it returns. Percent encoding is compatible with UTF-8 encoding. The following list explains how CloudFront handles encoding for the URI, query string, and headers: <br>• When values in the request are UTF-8 encoded, CloudFront forwards the values to your function without changing them. <br>• When values in the request are [ISO-8859-1 encoded](https://en.wikipedia.org/wiki/ISO/IEC_8859-1 "https://en.wikipedia.org/wiki/ISO/IEC_8859-1"), CloudFront converts the values to UTF-8 encoding before forwarding them to your function. <br>• When values in the request are encoded using some other character encoding, CloudFront assumes that they're ISO-8859-1 encoded and tries to convert from ISO-8859-1 to UTF-8. ###### Important The converted characters might be an inaccurate interpretation of the values in the original request. This might cause your function or your origin to produce an unintended result. The values for the URI, query string, and headers that CloudFront forwards to your origin depend on whether a function changes the values: <br>• If a function doesn't change the URI, query string, or header, CloudFront forwards the values that it received in the request to your origin. <br>• If a function changes the URI, query string, or header, CloudFront forwards the UTF-8 encoded values. ## Microsoft Smooth Streaming You can't use edge functions with a CloudFront distribution that you're using for streaming media files that you've transcoded into the Microsoft Smooth Streaming format. ## Tagging You can't add tags to edge functions. For more information about tagging in CloudFront, see [Tag a distribution](tagging.md "tagging.md").
