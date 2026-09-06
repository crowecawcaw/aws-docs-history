

# CopyObject (SOAP API)
<a name="SOAPCopyObject"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

## Description
<a name="SOAPCopyObject_Description"></a>

The `CopyObject` operation creates a copy of an object when you specify the key and bucket of a source object and the key and bucket of a target destination. 

When copying an object, you can preserve all metadata (default) or specify new metadata. However, the ACL is not preserved and is set to `private` for the user making the request. To override the default ACL setting, specify a new ACL when generating a copy request. For more information, see [Using ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3_ACLs_UsingACLs.html).

All copy requests must be authenticated. Additionally, you must have *read* access to the source object and *write* access to the destination bucket. For more information, see [Using Auth Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html). 

To only copy an object under certain conditions, such as whether the Etag matches or whether the object was modified before or after a specified date, use the request parameters `CopySourceIfUnmodifiedSince`, `CopyIfUnmodifiedSince`, `CopySourceIfMatch`, or `CopySourceIfNoneMatch`. 

**Note**  
 You might need to configure the SOAP stack socket timeout for copying large objects. 

## Request Syntax
<a name="SOAPCopyObject_RequestSyntax"></a>

```
 1. <CopyObject xmlns="http://bucket_name.s3.amazonaws.com/2006-03-01">
 2.   <SourceBucket>source_bucket</SourceBucket>
 3.   <SourceObject>source_object</SourceObject>
 4.   <DestinationBucket>destination_bucket</DestinationBucket>
 5.   <DestinationObject>destination_object</DestinationObject>
 6.   <MetadataDirective>{REPLACE | COPY}</MetadataDirective>
 7.   <Metadata>
 8.     <Name>metadata_name</Name>
 9.     <Value>metadata_value</Value>
10.   </Metadata>
11.   ...
12.   <AccessControlList>
13.     <Grant>
14.       <Grantee xsi:type="user_type">
15.         <ID>user_id</ID>
16.         <DisplayName>display_name</DisplayName>
17.       </Grantee>
18.       <Permission>permission</Permission>
19.     </Grant>
20.     ...
21.   </AccessControlList>
22.   <CopySourceIfMatch>etag</CopySourceIfMatch>
23.   <CopySourceIfNoneMatch>etag</CopySourceIfNoneMatch>
24.   <CopySourceIfModifiedSince>date_time</CopySourceIfModifiedSince>
25.   <CopySourceIfUnmodifiedSince>date_time</CopySourceIfUnmodifiedSince>
26.   <AWSAccessKeyId>AWSAccessKeyId</AWSAccessKeyId>
27.   <Timestamp>TimeStamp</Timestamp>
28.   <Signature>Signature</Signature>
29. </CopyObject>
```

## Request Parameters
<a name="SOAPCopyObject_RequestParameters"></a>


|  Name  |  Description  |  Required  | 
| --- | --- | --- | 
|  SourceBucket  | The name of the source bucket.<br />Type: String<br />Default: None<br />Constraints: A valid source bucket. |  Yes  | 
|  SourceKey  | The key name of the source object.<br />Type: String<br />Default: None<br />Constraints: The key for a valid source object to which you have READ access. |  Yes  | 
|  DestinationBucket  | The name of the destination bucket.<br />Type: String<br />Default: None<br />Constraints: You must have WRITE access to the destination bucket. |  Yes  | 
|  DestinationKey  |  The key of the destination object.<br />Type: String<br />Default: None<br />Constraints: You must have WRITE access to the destination bucket. |  Yes  | 
|  MetadataDirective  |  Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.<br />Type: String<br />Default: COPY<br />Valid values: COPY \| REPLACE<br />Constraints: Values other than `COPY` or `REPLACE` will result in an immediate error. You cannot copy an object to itself unless the MetadataDirective header is specified and its value set to `REPLACE`. |  No  | 
|  Metadata  |  Specifies metadata name-value pairs to set for the object.If MetadataDirective is set to `COPY`, all metadata is ignored.<br />Type: String<br />Default: None<br />Constraints: None. |  No  | 
|  AccessControlList  | Grants access to users by e-mail addresses or canonical user ID.<br />Type: String<br />Default: None<br />Constraints: None |  No  | 
|  CopySourceIfMatch  | Copies the object if its entity tag (ETag) matches the specified tag; otherwise return a PreconditionFailed.<br />Type: String<br />Default: None<br />Constraints: None. If the Etag does not match, the object is not copied. |  No  | 
|  CopySourceIfNoneMatch  | Copies the object if its entity tag (ETag) is different than the specified Etag; otherwise returns an error.<br />Type: String<br />Default: None<br />Constraints: None.  |  No  | 
|  CopySourceIfUnmodifiedSince  |  Copies the object if it hasn't been modified since the specified time; otherwise returns a PreconditionFailed.<br />Type: dateTime<br />Default: None |  No  | 
|  CopySourceIfModifiedSince  | Copies the object if it has been modified since the specified time; otherwise returns an error.<br />Type: dateTime<br />Default: None |  No  | 

## Response Syntax
<a name="SOAPCopyObject_ResponseSyntax"></a>

```
1. <CopyObjectResponse xmlns="http://bucket_name.s3.amazonaws.com/2006-03-01">
2.   <CopyObjectResponse>
3.     <ETag>"etag"</ETag>
4.     <LastModified>timestamp</LastModified>
5.   </CopyObjectResponse>
6. </CopyObjectResponse>
```

## Response Elements
<a name="SOAPCopyObject_CommonResponseElements"></a>

Following is a list of response elements.

**Note**  
 The SOAP API does not return extra whitespace. Extra whitespace is only returned by the REST API. 


|  Name  |  Description  | 
| --- | --- | 
|  Etag  | Returns the etag of the new object. The ETag only reflects changes to the contents of an object, not its metadata.<br />Type: String<br />Ancestor: CopyObjectResult | 
|  LastModified  | Returns the date the object was last modified.<br />Type: String<br />Ancestor: CopyObjectResult | 

For information about general response elements, see [Using REST Error Response Headers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HandlingErrors.html#UsingRESTErrorResponseHeaders).

## Special Errors
<a name="SOAPCopyObject_SpecialErrors"></a>

There are no special errors for this operation. For information about general Amazon S3 errors, see [List of error codes](ErrorResponses.md#ErrorCodeList).

## Examples
<a name="SOAPCopyObject_Examples"></a>

This example copies the `flotsam` object from the `pacific` bucket to the `jetsam` object of the `atlantic` bucket, preserving its metadata.

### Sample Request
<a name="SOAPCopyObject_Examples_Request1"></a>

```
1. <CopyObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
2.   <SourceBucket>pacific</SourceBucket>
3.   <SourceObject>flotsam</SourceObject>
4.   <DestinationBucket>atlantic</DestinationBucket>
5.   <DestinationObject>jetsam</DestinationObject>
6.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
7.   <Timestamp>2008-02-18T13:54:10.183Z</Timestamp>
8.   <Signature>Iuyz3d3P0aTou39dzbq7RrtSFmw=</Signature>
9. </CopyObject>
```

### Sample Response
<a name="SOAPCopyObject_Examples_Response1"></a>

```
1. <CopyObjectResponse xmlns="http://doc.s3.amazonaws.com/2006-03-01">
2.   <CopyObjectResponse>
3.     <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
4.     <LastModified>2008-02-18T13:54:10.183Z</LastModified>
5.   </CopyObjectResponse>
6. </CopyObjectResponse>
```

This example copies the "tweedledee" object from the wonderland bucket to the "tweedledum" object of the wonderland bucket, replacing its metadata.

### Sample Request
<a name="SOAPCopyObject_Examples_Request2"></a>

```
 1. <CopyObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
 2.   <SourceBucket>wonderland</SourceBucket>
 3.   <SourceObject>tweedledee</SourceObject>
 4.   <DestinationBucket>wonderland</DestinationBucket>
 5.   <DestinationObject>tweedledum</DestinationObject>
 6.   <MetadataDirective >REPLACE</MetadataDirective >
 7.   <Metadata>
 8.     <Name>Content-Type</Name>
 9.     <Value>text/plain</Value>
10.   </Metadata>
11.   <Metadata>
12.     <Name>relationship</Name>
13.     <Value>twins</Value>
14.   </Metadata>
15.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
16.   <Timestamp>2008-02-18T13:54:10.183Z</Timestamp>
17.   <Signature>Iuyz3d3P0aTou39dzbq7RrtSFmw=</Signature>
18. </CopyObject>
```

### Sample Response
<a name="SOAPCopyObject_Examples_Response2"></a>

```
1. <CopyObjectResponse xmlns="http://doc.s3.amazonaws.com/2006-03-01">
2.   <CopyObjectResponse>
3.     <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
4.     <LastModified>2008-02-18T13:54:10.183Z</LastModified>
5.   </CopyObjectResponse>
6. </CopyObjectResponse>
```

## Related Resources
<a name="SOAPCopyObject_RelatedResources"></a>
+  [PutObject (SOAP API)](SOAPPutObject.md) 
+  [PutObjectInline (SOAP API)](SOAPPutObjectInline.md) 