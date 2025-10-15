# GetObjectAccessControlPolicy (SOAP API)

###### Note


 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on October 31, 2025. We recommend that you use either the REST API or the AWS SDKs.
 

The `GetObjectAccessControlPolicy` operation fetches the access control policy for an object.

###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").

###### Example

This example retrieves the access control policy for the "Nelson" object from the "quotes" bucket.

`Sample Request`


```
<GetObjectAccessControlPolicy xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Bucket>quotes</Bucket>
  <Key>Nelson</Key>
  <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
  <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
  <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
</GetObjectAccessControlPolicy>
```
`Sample Response`


```
<AccessControlPolicy>
  <Owner>
    <ID>a9a7b886d6fd24a541bf9b1c61be666e9</ID>
    <DisplayName>chriscustomer</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xsi:type="CanonicalUser">
        <ID>a9a7b841bf9b1c61be666e9</ID>
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
</AccessControlPolicy>
```
## Response Body


The response contains the access control policy for the bucket. For an explanation of this response, [SOAP Access Policy](../userguide/SOAPAccessPolicy.md "../userguide/SOAPAccessPolicy.md")
.


## Access Control


You must have `READ_ACP` rights to the object in order to retrieve the access control policy for an object.
