# CreateBucket (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 

The `CreateBucket` operation creates a bucket. Not every string is an acceptable bucket name.
 For information on bucket naming restrictions, see [Working with Amazon S3 Buckets](../userguide/UsingBucket.md "../userguide/UsingBucket.md")
.

###### Note


To determine whether a bucket name exists, use `ListBucket` and set `MaxKeys` to 0.
A NoSuchBucket response indicates that the bucket is available, an AccessDenied response indicates that someone else owns the bucket, and a Success response indicates that you own the bucket or have permission to access it.


###### Example Create a bucket named "quotes"

`Sample Request`


```
<CreateBucket xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>quotes</Bucket>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</CreateBucket>
```
`Sample Response`


```
<CreateBucketResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <CreateBucketResponse>
    <Bucket>quotes</Bucket>
  </CreateBucketResponse>
</CreateBucketResponse>
```
## Elements



* `Bucket:` The name of the bucket you are trying to create.
* `AccessControlList:` The access control list for the new bucket.
 This element is optional. If not provided, the bucket is created with an access policy
 that give the requester FULL\_CONTROL access.

## Access Control


You must authenticate with a valid AWS Access Key ID. Anonymous requests are never allowed to create buckets.


## Related Resources



* [ListBucket (SOAP API)](SOAPListBucket.md "SOAPListBucket.md")
