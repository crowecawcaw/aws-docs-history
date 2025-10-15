# Downloading objects from Requester Pays
 buckets

Because requesters are charged for downloading data from Requester Pays buckets,
 the requests must contain a special parameter, `x-amz-request-payer`,
 which confirms that the requester knows that they will be charged for the download.
 To access objects in Requester Pays buckets, requests must include one of the
 following.


* For DELETE, GET, HEAD, POST, and PUT requests, include `x-amz-request-payer :
 requester` in the header
* For signed URLs, include `x-amz-request-payer=requester` in the
 request
If the request succeeds and the requester is charged, the response includes the
 header `x-amz-request-charged:requester`. If
 `x-amz-request-payer` is not in the request, Amazon S3 returns a 403 error
 and charges the bucket owner for the request.

###### Note

Bucket owners do not need to add `x-amz-request-payer` to their
 requests.

Ensure that you have included `x-amz-request-payer` and its value
 in your signature calculation. For more information, see [Using an Authorization Header](../API/sigv4-auth-using-authorization-header.md "../API/sigv4-auth-using-authorization-header.md") in the *Amazon S3 API Reference*
 .


###### To download objects from a Requester Pays bucket


* Use a `GET` request to download an object from a Requester
 Pays bucket, as shown in the following request.



```
GET / `[destinationObject]` HTTP/1.1
Host: `[BucketName]`.s3.amazonaws.com
x-amz-request-payer : requester
Date: Wed, 01 Mar 2009 12:00:00 GMT
Authorization: AWS `[Signature]`
```
If the GET request succeeds and the requester is charged, the response includes
 `x-amz-request-charged:requester`.

Amazon S3 can return an `Access Denied` error for requests that try to get
 objects from a Requester Pays bucket. For more information, see [Error Responses](../API/ErrorResponses.md "../API/ErrorResponses.md") in the *Amazon Simple Storage Service API Reference*.

To download objects from a Requester Pays bucket using the AWS CLI, you specify
 `--request-payer requester` as part of your
 `get-object` request. For more information, see [get-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html") in the *AWS CLI Reference*.
