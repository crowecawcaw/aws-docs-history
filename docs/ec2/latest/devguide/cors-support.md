

# Cross-origin resource sharing support and Amazon EC2
<a name="cors-support"></a>

The Amazon EC2 API supports cross-origin resource sharing (CORS). CORS defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. For more information, go to the [Cross-Origin Resource Sharing W3C Recommendation](http://www.w3.org/TR/cors/). With CORS support for Amazon EC2, you can build rich client-side web applications that use the Amazon EC2 API. For example, suppose you are hosting a web site, `mywebsite.example.com`, and you want to use JavaScript on your web pages to make requests to the Amazon EC2 API. Normally, a browser blocks JavaScript from allowing these requests, but with CORS, you are able to make cross-origin Amazon EC2 API calls from `mywebsite.example.com`.

CORS is already enabled for the Amazon EC2 API, and is ready for you to use. You do not need to perform any additional configuration steps to start using this feature. There is no change to the way that you make calls to the Amazon EC2 API; they must still be signed with valid AWS credentials to ensure that AWS can authenticate the requester. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*.

The implementation of CORS in the Amazon EC2 API is standardized. Your application can send a simple request to the Amazon EC2 API, or, depending on the content of the request, a preflight request followed by an actual request. Amazon EC2 allows the request from any origin

For more information about CORS and examples of how it works, go to the following article on the Mozilla Developer Network: [HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS).

## Simple requests
<a name="cors-simple"></a>

The following are the criteria that define a simple or actual request:
+ Requests only use the `GET` or `POST` HTTP methods. If the `POST` method is used, then `Content-Type` can only be one of the following: `application/x-www-form-urlencoded`, `multipart/form-data`, or `text/plain`.
+ Requests do not set custom headers, such as `X-Other-Header`.

Amazon EC2 allows the request from any origin. Any `GET` or `POST` request that attempts to use browser credentials by setting the `Access-Control-Allow-Credentials` value to `true` (where `XMLHttpRequest.withCredentials = true`) will fail. 

The following information describes the request headers to Amazon EC2:

**Simple request header values**
+ `Origin`: Specifies the domain that would like access to the resource (in this case, the resource is Amazon EC2). This is inserted by the browser in a cross-origin request.

The following information describes the response headers that Amazon EC2 returns (or does not return) after a simple or actual request:

**Simple response header values**
+ `Access-Control-Allow-Origin`: Specifies the domain that can access the resource (in this case, the resource is Amazon EC2). This is always returned with a \* value. Therefore, Amazon EC2 allows any cross-domain origin, and never allows browser credentials, such as cookies. 
+ `Access-Control-Allow-Credentials`: Indicates whether browser credentials can be used to make the actual request. This is never returned. Therefore, the browser should interpret the value as `Access-Control-Allow-Credentials: false`.

## Preflight requests
<a name="cors-preflight"></a>

If the content of your request meets the criteria below, then your request is checked for whether the actual request should be sent. A preflight request first sends an HTTP request to the resource (in this case, Amazon EC2) using the `OPTIONS` method. 

The following are the criteria that define a preflight request:
+ Requests use HTTP methods other than `GET` or `POST`. However, if the `POST` method is used, then the `Content-Type` is not one of the following: `application/x-www-form-urlencoded`, `multipart/form-data`, or `text/plain`.
+ Requests set custom headers; for example, `X-Other-Header`.

The Amazon EC2 CORS implementation allows any headers, and allows any origin in the actual request. 

The following information describes the request headers for a preflight request to Amazon EC2:

**Preflight request header values**
+ `Origin`: Specifies the domain that would like access to the resource (in this case, the resource is Amazon EC2). This is inserted by the browser in a cross-origin request.
+ `Access-Control-Request-Method`: The HTTP method to be used in the actual request from the browser.
+ `Access-Control-Request-Headers`: The custom headers to be sent in the actual cross-origin request.

The following information is about the response headers that Amazon EC2 returns (or does not return) after a preflight request:

**Preflight response header values**
+ `Access-Control-Allow-Origin`: Specifies the domain that can access the resource (in this case, the resource is Amazon EC2). This is always returned with a \* value. Therefore, Amazon EC2 allows any cross-domain origin, and never allows browser credentials, such as cookies. 
+ `Access-Control-Allow-Credentials`: Indicates whether browser credentials can be used to make the actual request. This is never returned by Amazon EC2. Therefore, the browser should interpret the value as `Access-Control-Allow-Credentials: false`. 
+ `Access-Control-Expose-Headers`: Allows headers to be exposed to the browser. This is never returned by Amazon EC2. Therefore, no return headers from Amazon EC2 can be read by the requesting domain. 
+ `Access-Control-Max-Age`: Specifies how long preflight request results can be cached. The value is set to 1800 seconds (30 minutes).
+ `Access-Control-Allow-Methods`: Indicates which methods are allowed when making an actual request. The following methods are allowed: `GET`, `POST`, `OPTIONS`, `DELETE`, and `PUT`. This also depends on how you are calling the Amazon EC2 API; for example, by using the Query API, or by using REST.
+ `Access-Control-Allow-Headers`: Indicates which headers can be used in the actual request. Amazon EC2 accepts any headers in preflight requests. If the HTTP headers are not relevant in the actual request, they are ignored.