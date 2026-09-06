

# PutObject (SOAP API)
<a name="SOAPPutObject"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `PutObject` operation adds an object to a bucket. The data for the object is attached as a DIME attachment.

To ensure an object is not corrupted over the network, you can calculate the MD5 of an object, PUT it to Amazon S3, and compare the returned Etag to the calculated MD5 value.

If an object already exists in a bucket, the new object will overwrite it because Amazon S3 stores the last write request. However, Amazon S3 is a distributed system. If Amazon S3 receives multiple write requests for the same object nearly simultaneously, all of the objects might be stored, even though only one wins in the end. Amazon S3 does not provide object locking; if you need this, make sure to build it into your application layer.

**Example**  
This example puts some data and metadata in the "Nelson" object of the "quotes" bucket, give a user (usually the owner) `FULL_CONTROL` access to the object, and make the object readable by anonymous parties. In this sample, the actual attachment is not shown.  
`Sample Request`  

```
 1. <PutObject xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2.   <Bucket>quotes</Bucket>
 3.   <Key>Nelson</Key>
 4.   <Metadata>
 5.     <Name>Content-Type</Name>
 6.     <Value>text/plain</Value>
 7.   </Metadata>
 8.   <Metadata>
 9.     <Name>family</Name>
10.     <Value>Muntz</Value>
11.   </Metadata>
12.   <ContentLength>5</ContentLength>
13.   <AccessControlList>
14.     <Grant>
15.       <Grantee xsi:type="CanonicalUser">
16.         <ID>a9a7b886d6241bf9b1c61be666e9</ID>
17.         <DisplayName>chriscustomer</DisplayName>
18.       </Grantee>
19.       <Permission>FULL_CONTROL</Permission>
20.     </Grant>
21.     <Grant>
22.       <Grantee xsi:type="Group">
23.         <URI>http://acs.amazonaws.com/groups/global/AllUsers<URI>
24.       </Grantee>
25.       <Permission>READ</Permission>
26.     </Grant>
27.   </AccessControlList>
28.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
29.   <Timestamp>2007-05-11T12:00:00.183Z</Timestamp>
30.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
31. </PutObject>
```
`Sample Response`  

```
1. <PutObjectResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <PutObjectResponse>
3.     <ETag>&quot;828ef3fdfa96f00ad9f27c383fc9ac7f&quot;</ETag>
4.     <LastModified>2006-03-01T12:00:00.183Z</LastModified>
5.   </PutObjectResponse>
6. </PutObjectResponse>
```

## Elements
<a name="SOAPPutObjectElements"></a>
+  `Bucket:` The bucket in which to add the object.
+ `Key:` The key to assign to the object.
+ `Metadata:` You can provide name-value metadata pairs in the metadata element. These will be stored with the object.
+ `ContentLength:` The length of the data in bytes.
+ `AccessControlList:` An Access Control List for the resource. This element is optional. If omitted, the requester is given `FULL_CONTROL` access to the object. If the object already exists, the preexisting Access Control Policy is replaced.

## Responses
<a name="SOAPPutObjectResponse"></a>
+ `ETag:` The entity tag is an MD5 hash of the object that you can use to do conditional fetches of the object using `GetObjectExtended`. The ETag only reflects changes to the contents of an object, not its metadata.
+ `LastModified:` The Amazon S3 timestamp for the saved object.

## Access Control
<a name="SOAPPutObjectAccessControl"></a>

To put objects into a bucket, you must have `WRITE` access to the bucket.

## Related Resources
<a name="SOAPPutObject_RelatedResources"></a>
+  [CopyObject (SOAP API)](SOAPCopyObject.md) 