

# Appendix: OPTIONS object
<a name="RESTOPTIONSobject"></a>

## Description
<a name="RESTOPTIONSobject-description"></a>

A browser can send this preflight request to Amazon S3 to determine if it can send an actual request with the specific origin, HTTP method, and headers. 

Amazon S3 supports cross-origin resource sharing (CORS) by enabling you to add a `cors` subresource on a bucket. When a browser sends this preflight request, Amazon S3 responds by evaluating the rules that are defined in the `cors` configuration.

If `cors` is not enabled on the bucket, then Amazon S3 returns a `403 Forbidden` response.

 For more information about CORS, go to [Enabling Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html) in the *Amazon Simple Storage Service User Guide*.

## Requests
<a name="RESTOPTIONSobject-requests"></a>

### Syntax
<a name="RESTOPTIONSobject-requests-syntax"></a>

```
1. OPTIONS /{{ObjectName}} HTTP/1.1
2. Host: {{BucketName}}.s3.amazonaws.com 
3. Origin: {{Origin}}
4. Access-Control-Request-Method: {{HTTPMethod}}
5. Access-Control-Request-Headers: {{RequestHeader}}
```

### Request Parameters
<a name="RESTOPTIONSobject-requests-request-parameters"></a>

 This operation does not introduce any specific request parameters, but it may contain any request parameters that are required by the actual request. 

### Request Headers
<a name="RESTOPTIONSobject-requests-request-headers"></a>


|  Name  |  Description  |  Required  | 
| --- | --- | --- | 
| Origin | Identifies the origin of the cross-origin request to Amazon S3. For example, http://www.example.com.<br />Type: String <br />Default: None |  Yes  | 
| Access-Control-Request-Method | Identifies what HTTP method will be used in the actual request.<br />Type: String <br />Default: None |  Yes  | 
| Access-Control-Request-Headers | A comma-delimited list of HTTP headers that will be sent in the actual request. <br />For example, to put an object with server-side encryption, this preflight request will determine if it can include the `x-amz-server-side-encryption` header with the request.<br />Type: String <br />Default: None |  No  | 

### Request Elements
<a name="RESTOPTIONSobject-requests-request-elements"></a>

This implementation of the operation does not use request elements.

## Responses
<a name="RESTOPTIONSobject-responses"></a>

### Response Headers
<a name="RESTOPTIONSobject-responses-response-headers"></a>


| Header | Description | 
| --- | --- | 
| Access-Control-Allow-Origin | The origin you sent in your request. If the origin in your request is not allowed, Amazon S3 will not include this header in the response.<br />Type: String | 
| Access-Control-Max-Age | How long, in seconds, the results of the preflight request can be cached.<br />Type: String | 
| Access-Control-Allow-Methods  | The HTTP method that was sent in the original request. If the method in the request is not allowed, Amazon S3 will not include this header in the response.<br />Type: String | 
| Access-Control-Allow-Headers  | A comma-delimited list of HTTP headers that the browser can send in the actual request. If any of the requested headers is not allowed, Amazon S3 will not include that header in the response, nor will the response contain any of the headers with the `Access-Control` prefix.<br />Type: String | 
| Access-Control-Expose-Headers  | A comma-delimited list of HTTP headers. This header provides the JavaScript client with access to these headers in the response to the actual request.<br />Type: String | 

### Response Elements
<a name="RESTOPTIONSobject-responses-response-elements"></a>

This implementation of the operation does not return response elements.

## Examples
<a name="RESTOPTIONSobject-examples"></a>

### Example : Send a preflight OPTIONS request to a `cors` enabled bucket
<a name="RESTOPTIONSobject-examples-example-1-configure-cors---single-rule"></a>

 A browser can send this preflight request to Amazon S3 to determine if it can send the actual PUT request from http://www.example.com origin to the Amazon S3 bucket named `examplebucket`. 

#### Sample Request
<a name="RESTOPTIONSobject-examples-example-1-configure-cors---single-rule-sample-request"></a>

```
1. OPTIONS /exampleobject HTTP/1.1
2. Host: examplebucket.s3.amazonaws.com 
3. Origin: http://www.example.com
4. Access-Control-Request-Method: PUT
```

#### Sample Response
<a name="RESTOPTIONSobject-examples-example-1-configure-cors---single-rule-sample-response"></a>

```
 1. HTTP/1.1 200 OK
 2. x-amz-id-2: 6SvaESv3VULYPLik5LLl7lSPPtSnBvDdGmnklX1HfUl7uS2m1DF6td6KWKNjYMXZ
 3. x-amz-request-id: BDC4B83DF5096BBE
 4. Date: Wed, 21 Aug 2012 23:09:55 GMT
 5. Etag: "1f1a1af1f1111111111111c11aed1da1"
 6. Access-Control-Allow-Origin: http://www.example.com
 7. Access-Control-Allow-Methods: PUT
 8. Access-Control-Expose-Headers: x-amz-request-id
 9. Content-Length: 0
10. Server: AmazonS3
```

## Related Resources
<a name="RESTOPTIONSobject-related-resources"></a>
+  [GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html) 
+  [DeleteBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html) 
+  [PutBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html) 