# Retrieving the requestPayment
 configuration using the REST API

You can determine the `Payer` value that is set on a bucket by
 requesting the resource `requestPayment`.


###### To return the requestPayment resource


* Use a GET request to obtain the `requestPayment`
 resource, as shown in the following request.



```
GET ?requestPayment HTTP/1.1
Host: `[BucketName]`.s3.amazonaws.com
Date: Wed, 01 Mar 2009 12:00:00 GMT
Authorization: AWS `[Signature]`
```
If the request succeeds, Amazon S3 returns a response similar to the
 following.


```
HTTP/1.1 200 OK
x-amz-id-2: [id]
x-amz-request-id: [request_id]
Date: Wed, 01 Mar 2009 12:00:00 GMT
Content-Type: [type]
Content-Length: [length]
Connection: close
Server: AmazonS3

<?xml version="1.0" encoding="UTF-8"?>
<RequestPaymentConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<Payer>Requester</Payer>
</RequestPaymentConfiguration>
```
This response shows that the `payer` value is set to
 `Requester`.
