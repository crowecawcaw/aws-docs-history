# Configuring Requester Pays on a bucket

You can configure an Amazon S3 bucket to be a *Requester
 Pays* bucket so that the requester pays the cost of the request and data
 download instead of the bucket owner.

This section provides examples of how to configure Requester Pays on an Amazon S3 bucket
 using the console and the REST API.

###### To enable Requester Pays for an S3 general purpose bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the **General purpose buckets** list, choose the name of the
 bucket that you want to enable Requester Pays for.
4. Choose **Properties**.
5. Under **Requester pays**, choose
 **Edit**.
6. Choose **Enable**, and choose **Save
 changes**.


Amazon S3 enables Requester Pays for your bucket and displays your
 **Bucket overview**. Under **Requester
 pays**, you see **Enabled**.
Only the bucket owner can set the
 `RequestPaymentConfiguration.payer` configuration value of a
 bucket to `BucketOwner` (the default) or `Requester`.
 Setting the `requestPayment` resource is optional. By default,
 the bucket is not a Requester Pays bucket.

To revert a Requester Pays bucket to a regular bucket, you use the value
 `BucketOwner`. Typically, you would use
 `BucketOwner` when uploading data to the Amazon S3 bucket, and
 then you would set the value to `Requester` before publishing the
 objects in the bucket.


###### To set requestPayment


* Use a `PUT` request to set the `Payer` value
 to `Requester` on a specified bucket.



```
PUT ?requestPayment HTTP/1.1
Host: `[BucketName]`.s3.amazonaws.com
Content-Length: 173
Date: Wed, 01 Mar 2009 12:00:00 GMT
Authorization: AWS `[Signature]`

<RequestPaymentConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<Payer>Requester</Payer>
</RequestPaymentConfiguration>
```
If the request succeeds, Amazon S3 returns a response similar to the
 following.


```
HTTP/1.1 200 OK
x-amz-id-2: [id]
x-amz-request-id: [request_id]
Date: Wed, 01 Mar 2009 12:00:00 GMT
Content-Length: 0
Connection: close
Server: AmazonS3
x-amz-request-charged:requester
```
You can set Requester Pays only at the bucket level. You can't set
 Requester Pays for specific objects within the bucket.

You can configure a bucket to be `BucketOwner` or
 `Requester` at any time. However, there might be a few
 minutes before the new configuration value takes effect.

###### Note

Bucket owners who give out presigned URLs should consider carefully
 before configuring a bucket to be Requester Pays, especially if the URL
 has a long lifetime. The bucket owner is charged each time the requester
 uses a presigned URL that uses the bucket owner's credentials.
