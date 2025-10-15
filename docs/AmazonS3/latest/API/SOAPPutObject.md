# PutObject (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 

The `PutObject` operation adds an object to a bucket. The data for the object is attached as a DIME attachment.

To ensure an object is not corrupted over the network, you can calculate the MD5 of an object, PUT it to Amazon S3, and compare the returned Etag to the calculated MD5 value.

If an object already exists in a bucket, the new object will overwrite it because Amazon S3 stores the last write request. However, Amazon S3 is a distributed system. If Amazon S3 receives multiple write requests for the same object nearly simultaneously, all of the objects might be stored, even though only one wins in the end. Amazon S3 does not provide object locking; if you need this, make sure to build it into your application layer.

###### Example

This example puts some data and metadata in the "Nelson" object of the "quotes" bucket, give a user (usually the owner) `FULL_CONTROL` access to the object, and make the object readable by anonymous parties. In this sample, the actual attachment is not shown.

`Sample Request`


```
<PutObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>quotes</Bucket>
  <Key>Nelson</Key>
  <Metadata>
    <Name>Content-Type</Name>
    <Value>text/plain</Value>
  </Metadata>
  <Metadata>
    <Name>family</Name>
    <Value>Muntz</Value>
  </Metadata>
  <ContentLength>5</ContentLength>
  <AccessControlList>
    <Grant>
      <Grantee xsi:type="CanonicalUser">
        <ID>a9a7b886d6241bf9b1c61be666e9</ID>
        <DisplayName>chriscustomer</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    <Grant>
      <Grantee xsi:type="Group">
        <URI>http://acs.amazonaws.com/groups/global/AllUsers<URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2007-05-11T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</PutObject>
```
`Sample Response`


```
<PutObjectResponse xmlns="http://s3.amazonaws.com/doc/2006-03-01">
  <PutObjectResponse>
    <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
    <LastModified>2006-03-01T12:00:00.183Z</LastModified>
  </PutObjectResponse>
</PutObjectResponse>
```
## Elements



* `Bucket:` The bucket in which to add the object.
* `Key:` The key to assign to the object.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").
* `Metadata:` You can provide name-value metadata pairs in the metadata element. 
 These will be stored with the object.
* `ContentLength:` The length of the data in bytes.
* `AccessControlList:` An Access Control List for the resource. This
 element is optional. If omitted, the requester is given `FULL_CONTROL` access to
 the object. If the object already exists, the preexisting Access Control Policy is
 replaced.

## Responses



* `ETag:` The entity tag is an MD5 hash of the object that you can use 
 to do conditional fetches of the object using `GetObjectExtended`. The ETag only reflects changes to
 the contents of an object, not its metadata.
* `LastModified:` The Amazon S3 timestamp for the saved object.

## Access Control


To put objects into a bucket, you must have `WRITE` access to the bucket.


## Related Resources



* [CopyObject (SOAP API)](SOAPCopyObject.md "SOAPCopyObject.md")
