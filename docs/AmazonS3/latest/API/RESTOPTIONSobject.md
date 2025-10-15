# Appendix: OPTIONS object

## Description


A browser can send this preflight request to Amazon S3 to determine if it can send an actual
 request with the specific origin, HTTP method, and headers. 


Amazon S3 supports cross-origin resource sharing (CORS) by enabling you to add a
 `cors` subresource on a bucket. When a browser sends this preflight
 request, Amazon S3 responds by evaluating the rules that are defined in the
 `cors` configuration.


If `cors` is not enabled on the bucket, then Amazon S3 returns a `403
 Forbidden` response.


 For more information about CORS, go to [Enabling
 Cross-Origin Resource Sharing](../userguide/cors.md "../userguide/cors.md") in the *Amazon Simple Storage Service User Guide*.


## Requests


### Syntax



```
OPTIONS /`ObjectName` HTTP/1.1
Host: `BucketName`.s3.amazonaws.com 
Origin: `Origin`
Access-Control-Request-Method: `HTTPMethod`
Access-Control-Request-Headers: `RequestHeader`
```

### Request
 Parameters


 This operation does not introduce any specific request parameters, but it may contain any
 request parameters that are required by the actual request. 


### Request
 Headers




|  Name  |  Description  |  Required  |
| --- | --- | --- |
| `Origin` | Identifies the origin of the cross-origin request to Amazon S3. For example,
 http://www.example.com.
Type: String 
Default: None |  Yes  |
| `Access-Control-Request-Method` | Identifies what HTTP method will be used in the actual request.
Type: String 
Default: None |  Yes  |
| `Access-Control-Request-Headers` | A comma-delimited list of HTTP headers that will be sent in the actual request. 
For example, to put an object with server-side encryption, this preflight request will
 determine if it can include the
 `x-amz-server-side-encryption` header with the
 request.
Type: String 
Default: None |  No  |


### Request
 Elements


This implementation of the operation does not use request elements.


## Responses


### Response
 Headers




| Header | Description |
| --- | --- |
| `Access-Control-Allow-Origin` | The origin you sent in your request. If the origin in your request is not allowed,
 Amazon S3 will not include this header in the response.
Type: String |
| `Access-Control-Max-Age` | How long, in seconds, the results of the preflight request can be cached.
Type: String |
| `Access-Control-Allow-Methods`  | The HTTP method that was sent in the original request. If the method in the request is
 not allowed, Amazon S3 will not include this header in the
 response.
Type: String |
| `Access-Control-Allow-Headers`  | A comma-delimited list of HTTP headers that the browser can send in the actual
 request. If any of the requested headers is not allowed, Amazon
 S3 will not include that header in the response, nor will the
 response contain any of the headers with the
 `Access-Control` prefix.
Type: String |
| `Access-Control-Expose-Headers`  | A comma-delimited list of HTTP headers. This header provides the JavaScript client
 with access to these headers in the response to the actual
 request.
Type: String |


### Response
 Elements


This implementation of the operation does not return response elements.


## Examples


### Example :
 Send a preflight OPTIONS request to a `cors` enabled bucket


 A browser can send this preflight request to Amazon S3 to determine if it can send the
 actual PUT request from http://www.example.com origin to the Amazon S3 bucket named
 `examplebucket`. 


#### Sample Request



```
OPTIONS /exampleobject HTTP/1.1
Host: examplebucket.s3.amazonaws.com 
Origin: http://www.example.com
Access-Control-Request-Method: PUT
```

#### Sample Response



```
HTTP/1.1 200 OK
x-amz-id-2: 6SvaESv3VULYPLik5LLl7lSPPtSnBvDdGmnklX1HfUl7uS2m1DF6td6KWKNjYMXZ
x-amz-request-id: BDC4B83DF5096BBE
Date: Wed, 21 Aug 2012 23:09:55 GMT
Etag: "1f1a1af1f1111111111111c11aed1da1"
Access-Control-Allow-Origin: http://www.example.com
Access-Control-Allow-Methods: PUT
Access-Control-Expose-Headers: x-amz-request-id
Content-Length: 0
Server: AmazonS3
```

## Related
 Resources



* [GetBucketCors](API_GetBucketCors.md "API_GetBucketCors.md")
* [DeleteBucketCors](API_DeleteBucketCors.md "API_DeleteBucketCors.md")
* [PutBucketCors](API_PutBucketCors.md "API_PutBucketCors.md")
