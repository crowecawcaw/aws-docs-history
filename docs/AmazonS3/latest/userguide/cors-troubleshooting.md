# Troubleshooting CORS

The following topics can help you troubleshoot some common CORS issues related to
 S3.

###### Topics

* [403 Forbidden error - CORS is not enabled
 for this bucket](#cors-not-enabled "#cors-not-enabled")
* [403 Forbidden error - This CORS request is
 not allowed](#cors-not-enabled "#cors-not-enabled")
* [Headers not found in CORS response](#Headers-not-found "#Headers-not-found")
* [Considerations of CORS on S3 proxy
 integrations](#cors-in-proxy "#cors-in-proxy")

## 403 Forbidden error: CORS is not enabled for this
 bucket


The following `403 Forbidden` error occurs when a cross-origin request
 is sent to Amazon S3 but CORS is not configured on your S3 bucket. 
 


 Error: **`HTTP/1.1 403 Forbidden CORS Response: CORS is not enabled for this
 bucket.`** 


The CORS configuration is a document or policy with rules that identify the
 origins that you will allow to access your bucket, the operations (HTTP methods) that
 you will support for each origin, and other operation-specific information. See how to
 [configure CORS](enabling-cors-examples.md "enabling-cors-examples.md")
 on S3 by using the Amazon S3 console, AWS SDKs, and REST API. For more information on
 CORS and examples of a CORS configuration, see  [Elements of
 CORS](ManageCorsUsing.md#cors-example-1 "ManageCorsUsing.md#cors-example-1").


## 403 Forbidden error: This CORS request is
 not allowed


The following `403 Forbidden` error is received when a CORS rule in your
 CORS configuration doesn't match the data in your request.


Error:  **`HTTP/1.1 403 Forbidden
 CORS Response: This CORS request is not allowed.`**


As a result, this `403 Forbidden` error can occur for multiple
 reasons:



* Origin is not allowed.
* Methods are not allowed.
* Requested headers are not allowed.

For each request that Amazon S3 receives, you must have a CORS rule in your CORS configuration that matches the data in your request. 


### Origin is not allowed


 The `Origin` header in a CORS request to your bucket must match the origins in the
 `AllowedOrigins` element in your CORS configuration. A wildcard
 character (`"*"`) in the `AllowedOrigins` element would match
 all HTTP methods. For more information on how to update the
 `AllowedOrigins` element, see [Configuring
 cross-origin resource sharing (CORS)](enabling-cors-examples.md "enabling-cors-examples.md").


 For example, if only the `http://www.example1.com` domain is included
 in the `AllowedOrigins` element, then a CORS request sent from the
 `http://www.example2.com` domain would receive the `403
 Forbidden` error. 


The following example shows part of a CORS configuration that includes
 the `http://www.example1.com` domain in the `AllowedOrigins`
 element. 



```
"AllowedOrigins":[
   "http://www.example1.com"
]
```

For a CORS request sent from the `http://www.example2.com`
 domain to be successful, the `http://www.example2.com` domain should be
 included in the `AllowedOrigins` element of CORS configuration. 



```
"AllowedOrigins":[
   "http://www.example1.com"
   "http://www.example2.com"
]
```

### Methods are not allowed


 The HTTP methods that are specified in the
 `Access-Control-Request-Method` in a CORS request to your bucket must
 match the method or methods listed in the `AllowedMethods` element in
 your CORS configuration. A wildcard character (`"*"`) in
 `AllowedMethods` would match all HTTP methods. For more information
 on how to update the `AllowedOrigins` element, see [Configuring
 cross-origin resource sharing (CORS)](enabling-cors-examples.md "enabling-cors-examples.md"). 


In a CORS configuration, you can specify the following methods in
 the `AllowedMethods` element:



* `GET`
* `PUT`
* `POST`
* `DELETE`
* `HEAD`

The following example shows part of a CORS configuration that includes the
 `GET` method in the `AllowedMethods` element. Only
 requests including the `GET` method would succeed. 



```
"AllowedMethods":[
   "GET"
]
```

 If an HTTP method (for example, `PUT`) was used in a CORS request or
 included in a pre-flight CORS request to your bucket but the method isn't present in
 your CORS configuration, the request would result in a `403 Forbidden`
 error. To allow this CORS request or CORS pre-flight request, the `PUT`
 method must be added to your CORS configuration. 



```
"AllowedMethods":[
   "GET"
   "PUT"
]
```

###  Requested headers are not
 allowed


 The headers listed in the `Access-Control-Request-Headers` header in a
 pre-flight request must match the headers in the `AllowedHeaders` element
 in your CORS configuration. For a list of common headers that can be used in
 requests to Amazon S3, see [Common Request
 Headers](../API/RESTCommonRequestHeaders.md "../API/RESTCommonRequestHeaders.md"). For more information on how to update the
 `AllowedHeaders` element, see [Configuring
 cross-origin resource sharing (CORS)](enabling-cors-examples.md "enabling-cors-examples.md"). 


The following example shows part of a CORS configuration that includes the
 `Authorization` header in the `AllowedHeaders` element.
 Only requests for the `Authorization` header would succeed. 



```
"AllowedHeaders":  [
    "Authorization"
]
```

 If a header (for example `Content-MD5` was included in a CORS request
 but the header isn't present in your CORS configuration, the request would result in
 a `403 Forbidden` error. To allow this CORS request , the
 `Content-MD5` header must be added to your CORS configuration. If you
 want to pass both `Authorization` and `Content-MD5` headers in
 a CORS request to your bucket, confirm that both headers are included in the
 `AllowedHeaders` element in your CORS configuration. 



```
"AllowedHeaders":  [
    "Authorization"
    "Content-MD5"
]           
```

##  Headers not found in CORS response


 The `ExposeHeaders` element in your CORS configuration identifies which
 response headers that you would like to make accessible to scripts and applications
 running in browsers, in response to a CORS request.


If your objects stored in your S3 bucket have user-defined metadata (for example,
 `x-amz-meta-custom-header`) along with the response data, this custom
 header could contain additional metadata or information that you want to access from
 your client-side JavaScript code. However, by default, browsers block access to custom
 headers for security reasons. To allow your client-side JavaScript to access custom
 headers, you need to include the header in your CORS configuration.


 In the example below, the `x-amz-meta-custom-header1` header is included
 in the `ExposeHeaders` element. The `x-amz-meta-custom-header2`
 isn't included in the `ExposeHeaders` element and is missing from the CORS
 configuration. In the response, only the values included in the
 `ExposeHeaders` element would be returned. If the request included the
 `x-amz-meta-custom-header2` header in the
 `Access-Control-Expose-Headers` header, the response would still return a
 `200 OK`. However, only the permitted header, For example
 `x-amz-meta-custom-header` would be returned and show in the response. 



```
"ExposeHeaders":  [
    "x-amz-meta-custom-header1"
]           
```

 To ensure all headers appear in the response, add all permitted headers to the `ExposeHeaders` element in your CORS configuration as shown below. 



```
"ExposeHeaders":  [
    "x-amz-meta-custom-header1",
    "x-amz-meta-custom-header2"
]           
```

## Considerations of CORS on S3 proxy
 integrations


If you are experiencing errors and have already checked the CORS configuration on your
 S3 bucket, and the cross-origin request is sent to proxies such as AWS CloudFront, try
 the following:



* Configure the settings to allow the `OPTIONS` method for HTTP requests.
* Configure the proxy to forward the following headers: `Origin`,
 `Access-Control-Request-Headers`, and
 `Access-Control-Request-Method`.
* Configure the proxy settings to include the origin header in its cache key. This is important because caching proxies that don't include the origin header in their cache key may serve cached responses that don't include the appropriate CORS headers for different origins.

Some proxies provide pre-defined features for CORS requests. For example, in
 CloudFront, you can configure a policy that includes the headers 


 that enable cross-origin resource sharing (CORS) requests when the origin is an
 Amazon S3 bucket.


 This policy has the following settings: 



* Headers included in origin requests:


 `Origin`


 `Access-Control-Request-Headers`


 `Access-Control-Request-Method`
* Cookies included in origin requests: None
* Query strings included in origin requests: None

For more information, see [Control
 origin requests with a policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.htm "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.htm") and [Use managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html#managed-origin-request-policy-cors-s3 "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html#managed-origin-request-policy-cors-s3") in the *CloudFront Developer
 Guide*.
