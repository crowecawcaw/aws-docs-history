# ListAllMyBuckets (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 

The `ListAllMyBuckets` operation returns a list of all buckets owned by the sender of the request.

###### Example

`Sample Request`


```
<ListAllMyBuckets xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</ListAllMyBuckets>
```
`Sample Response`


```
<ListAllMyBucketsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <Owner>
    <ID>bcaf1ffd86f41161ca5fb16fd081034f</ID>
    <DisplayName>webfile</DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <Name>quotes;/Name>
      <CreationDate>2006-02-03T16:45:09.000Z</CreationDate>
    </Bucket>
    <Bucket>
      <Name>samples</Name>
      <CreationDate>2006-02-03T16:41:58.000Z</CreationDate>
    </Bucket>
 </Buckets>
</ListAllMyBucketsResult>
```
## Response Body



* `Owner:`

 This provides information that Amazon S3 uses to
 represent your identity for purposes of authentication and access control. ID is a unique
 and permanent identifier for the developer who made the request. DisplayName is a
 human-readable name representing the developer who made the request. It is not unique, and
 might change over time.We recommend that you match your DisplayName to your Forum
 name.
* `Name:`

The name of a bucket. Note that if one of your
 buckets was recently deleted, the name of the deleted bucket might still be present in this
 list for a period of time.
* `CreationDate:`

 The time that the bucket was
 created.

## Access Control


You must authenticate with a valid AWS Access Key ID. Anonymous requests are never allowed to list buckets, and you can only list buckets for which you are the owner.
