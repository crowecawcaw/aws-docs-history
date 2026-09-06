

# PutObjectInline (SOAP API)
<a name="SOAPPutObjectInline"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `PutObjectInline` operation adds an object to a bucket. The data for the object is provided in the body of the SOAP message. 

If an object already exists in a bucket, the new object will overwrite it because Amazon S3 stores the last write request. However, Amazon S3 is a distributed system. If Amazon S3 receives multiple write requests for the same object nearly simultaneously, all of the objects might be stored, even though only one wins in the end. Amazon S3 does not provide object locking; if you need this, make sure to build it into your application layer.

To ensure an object is not corrupted over the network, you can calculate the MD5 of an object, PUT it to Amazon S3, and compare the returned Etag to the calculated MD5 value.

PutObjectInline is not suitable for use with large objects. The system limits this operation to working with objects 1MB or smaller. PutObjectInline will fail with the `InlineDataTooLargeError` status code if the Data parameter encodes an object larger than 1MB. To upload large objects, consider using the non-inline PutObject API, or the REST API instead. 

**Example**  
This example writes some text and metadata into the "Nelson" object in the "quotes" bucket, give a user (usually the owner) `FULL_CONTROL` access to the object, and make the object readable by anonymous parties.  
`Sample Request`  

```
 1. <PutObjectInline xmlns="https://doc.s3.amazonaws.com/2006-03-01">
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
12.   <Data>aGEtaGE=</Data>
13.   <ContentLength>5</ContentLength>
14.   <AccessControlList>
15.     <Grant>
16.       <Grantee xsi:type="CanonicalUser">
17.         <ID>a9a7b886d6fde241bf9b1c61be666e9</ID>
18.         <DisplayName>chriscustomer</DisplayName>
19.       </Grantee>
20.       <Permission>FULL_CONTROL</Permission>
21.     </Grant>
22.     <Grant>
23.       <Grantee xsi:type="Group">
24.         <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
25.       </Grantee>
26.       <Permission>READ</Permission>
27.     </Grant>
28.   </AccessControlList>
29.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
30.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
31.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
32. </PutObjectInline>
```
`Sample Response`  

```
1. <PutObjectInlineResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <PutObjectInlineResponse>
3.     <ETag>&quot828ef3fdfa96f00ad9f27c383fc9ac7f&quot</ETag>
4.     <LastModified>2006-01-01T12:00:00.000Z</lastModified>
5.   </PutObjectInlineResponse>
6. </PutObjectInlineResponse>
```

## Elements
<a name="SOAPPutObjectInlineElements"></a>
+ `Bucket:` The bucket in which to add the object.

  
+ `Key:` The key to assign to the object.

  
+ `Metadata:` You can provide name-value metadata pairs in the metadata element. These will be stored with the object.

  
+ `Data:` The base 64 encoded form of the data.

  
+ `ContentLength:` The length of the data in bytes.

  
+ `AccessControlList:` An Access Control List for the resource. This element is optional. If omitted, the requester is given `FULL_CONTROL` access to the object. If the object already exists, the preexisting access control policy is replaced.

  

## Responses
<a name="SOAPPutObjectInlineResponse"></a>
+  `ETag:` The entity tag is an MD5 hash of the object that you can use to do conditional fetches of the object using `GetObjectExtended`. The ETag only reflects changes to the contents of an object, not its metadata. 
+ `LastModified:` The Amazon S3 timestamp for the saved object.

## Access Control
<a name="SOAPPutObjectInlineAccessControl"></a>

You must have `WRITE` access to the bucket in order to put objects into the bucket. 

## Related Resources
<a name="SOAPPutObjectInline_RelatedResources"></a>
+  [PutObject (SOAP API)](SOAPPutObject.md) 
+  [CopyObject (SOAP API)](SOAPCopyObject.md) 