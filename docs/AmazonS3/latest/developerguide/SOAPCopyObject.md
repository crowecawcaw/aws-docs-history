# CopyObject (SOAP API)

###### Note

SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs.

## Description

The `CopyObject` operation creates a copy of an object when you specify the
key and bucket of a source object and the key and bucket of a target destination.

When copying an object, you can preserve all metadata (default) or specify new
metadata. However, the ACL is not preserved and is set to `private` for the
user making the request. To override the default ACL setting, specify a new ACL when
generating a copy request. For more information, see [Using ACLs](../userguide/S3_ACLs_UsingACLs.md "../userguide/S3_ACLs_UsingACLs.md").

All copy requests must be authenticated. Additionally, you must have
_read_ access to the source object and _write_
access to the destination bucket. For more information, see [Using Auth Access](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

To only copy an object under certain conditions, such as whether the Etag matches or
whether the object was modified before or after a specified date, use the request
parameters `CopySourceIfUnmodifiedSince`, `CopyIfUnmodifiedSince`,
`CopySourceIfMatch`, or `CopySourceIfNoneMatch`.

###### Note

You might need to configure the SOAP stack socket timeout for copying large
objects.

## Request Syntax

```

<CopyObject xmlns="http://*bucket\_name*.s3.amazonaws.com/2006-03-01">
  <SourceBucket>`source_bucket`</SourceBucket>
  <SourceObject>`source_object`</SourceObject>
  <DestinationBucket>`destination_bucket`</DestinationBucket>
  <DestinationObject>`destination_object`</DestinationObject>
  <MetadataDirective>{REPLACE | COPY}</MetadataDirective>
  <Metadata>
    <Name>`metadata_name`</Name>
    <Value>`metadata_value`</Value>
  </Metadata>
  ...
  <AccessControlList>
    <Grant>
      <Grantee xsi:type="`user_type`">
        <ID>`user_id`</ID>
        <DisplayName>`display_name`</DisplayName>
      </Grantee>
      <Permission>`permission`</Permission>
    </Grant>
    ...
  </AccessControlList>
  <CopySourceIfMatch>`etag`</CopySourceIfMatch>
  <CopySourceIfNoneMatch>`etag`</CopySourceIfNoneMatch>
  <CopySourceIfModifiedSince>`date_time`</CopySourceIfModifiedSince>
  <CopySourceIfUnmodifiedSince>`date_time`</CopySourceIfUnmodifiedSince>
  <AWSAccessKeyId>*AWSAccessKeyId*</AWSAccessKeyId>
  <Timestamp>*TimeStamp*</Timestamp>
  <Signature>*Signature*</Signature>
</CopyObject>

```

## Request Parameters

| Name                          | Description                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| `SourceBucket`                | The name of the source bucket.<br>Type: String<br>Default: None<br>Constraints: A valid source bucket.                                                                                                                          | Yes                                                                                                                                                                                                                            |
| `SourceKey`                   | The key name of the source object.<br>Type: String<br>Default: None<br>Constraints: The key for a valid source object to which you<br>have READ access.                                                                         | Yes                                                                                                                                                                                                                            |
| `DestinationBucket`           | The name of the destination bucket.<br>Type: String<br>Default: None<br>Constraints: You must have WRITE access to the destination<br>bucket.                                                                                   | Yes                                                                                                                                                                                                                            |
| `DestinationKey`              | The key of the destination object.<br>Type: String<br>Default: None<br>Constraints: You must have WRITE access to the destination<br>bucket.                                                                                    | Yes                                                                                                                                                                                                                            |
| `MetadataDirective`           | Specifies whether the metadata is copied from the source<br>object or replaced with metadata provided in the request.<br>Type: String<br>Default: COPY<br>Valid values: COPY                                                    | REPLACE<br>Constraints: Values other than `COPY` or<br>`REPLACE` will result in an immediate error. You<br>cannot copy an object to itself unless the MetadataDirective header<br>is specified and its value set to `REPLACE`. | No  |
| `Metadata`                    | Specifies metadata name-value pairs to set for the object.If<br>MetadataDirective is set to `COPY`, all metadata is<br>ignored.<br>Type: String<br>Default: None<br>Constraints: None.                                          | No                                                                                                                                                                                                                             |
| `AccessControlList`           | Grants access to users by e-mail addresses or canonical user<br>ID.<br>Type: String<br>Default: None<br>Constraints: None                                                                                                       | No                                                                                                                                                                                                                             |
| `CopySourceIfMatch`           | Copies the object if its entity tag (ETag) matches the<br>specified tag; otherwise return a PreconditionFailed.<br>Type: String<br>Default: None<br>Constraints: None. If the Etag does not match, the object is<br>not copied. | No                                                                                                                                                                                                                             |
| `CopySourceIfNoneMatch`       | Copies the object if its entity tag (ETag) is different than<br>the specified Etag; otherwise returns an error.<br>Type: String<br>Default: None<br>Constraints: None.                                                          | No                                                                                                                                                                                                                             |
| `CopySourceIfUnmodifiedSince` | Copies the object if it hasn't been modified since the<br>specified time; otherwise returns a PreconditionFailed.<br>Type: dateTime<br>Default: None                                                                            | No                                                                                                                                                                                                                             |
| `CopySourceIfModifiedSince`   | Copies the object if it has been modified since the specified<br>time; otherwise returns an error.<br>Type: dateTime<br>Default: None                                                                                           | No                                                                                                                                                                                                                             |

## Response Syntax

```
<CopyObjectResponse xmlns="http://*bucket\_name*.s3.amazonaws.com/2006-03-01">
  <CopyObjectResponse>
    <ETag>"`etag`"</ETag>
    <LastModified>`timestamp`</LastModified>
  </CopyObjectResponse>
</CopyObjectResponse>
```

## Response Elements

Following is a list of response elements.

###### Note

The SOAP API does not return extra whitespace. Extra whitespace is
only returned by the REST API.

| Name           | Description                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Etag`         | Returns the etag of the new object. The ETag only reflects changes to the contents of an object, not its metadata.<br>Type: String<br>Ancestor: CopyObjectResult |
| `LastModified` | Returns the date the object was last modified.<br>Type: String<br>Ancestor: CopyObjectResult                                                                     |

For information about general response elements, see [Using REST Error Response Headers](../userguide/HandlingErrors.md#UsingRESTErrorResponseHeaders "../userguide/HandlingErrors.md#UsingRESTErrorResponseHeaders").

## Special Errors

There are no special errors for this operation. For information about general Amazon S3
errors, see [List of error codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").

## Examples

This example copies the `flotsam` object from the `pacific`
bucket to the `jetsam` object of the `atlantic` bucket, preserving
its metadata.

### Sample Request

```
<CopyObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <SourceBucket>pacific</SourceBucket>
  <SourceObject>flotsam</SourceObject>
  <DestinationBucket>atlantic</DestinationBucket>
  <DestinationObject>jetsam</DestinationObject>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2008-02-18T13:54:10.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbq7RrtSFmw=</Signature>
</CopyObject>
```

### Sample Response

```
<CopyObjectResponse xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <CopyObjectResponse>
    <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
    <LastModified>2008-02-18T13:54:10.183Z</LastModified>
  </CopyObjectResponse>
</CopyObjectResponse>
```

This example copies the "tweedledee" object from the wonderland bucket to the
"tweedledum" object of the wonderland bucket, replacing its metadata.

### Sample Request

```
<CopyObject xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <SourceBucket>wonderland</SourceBucket>
  <SourceObject>tweedledee</SourceObject>
  <DestinationBucket>wonderland</DestinationBucket>
  <DestinationObject>tweedledum</DestinationObject>
  <MetadataDirective >REPLACE</MetadataDirective >
  <Metadata>
    <Name>Content-Type</Name>
    <Value>text/plain</Value>
  </Metadata>
  <Metadata>
    <Name>relationship</Name>
    <Value>twins</Value>
  </Metadata>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2008-02-18T13:54:10.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbq7RrtSFmw=</Signature>
</CopyObject>
```

### Sample Response

```
<CopyObjectResponse xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <CopyObjectResponse>
    <ETag>"828ef3fdfa96f00ad9f27c383fc9ac7f"</ETag>
    <LastModified>2008-02-18T13:54:10.183Z</LastModified>
  </CopyObjectResponse>
</CopyObjectResponse>
```

## Related Resources

- [PutObject (SOAP API)](SOAPPutObject.md "SOAPPutObject.md")
- [PutObjectInline (SOAP API)](SOAPPutObjectInline.md "SOAPPutObjectInline.md")
