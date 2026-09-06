

# SetBucketAccessControlPolicy (SOAP API)
<a name="SOAPSetBucketAccessControlPolicy"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `SetBucketAccessControlPolicy` operation sets the Access Control Policy for an existing bucket. If successful, the previous Access Control Policy for the bucket is entirely replaced with the specified Access Control Policy.

**Example**  
Give the specified user (usually the owner) `FULL_CONTROL` access to the "quotes" bucket.  
`Sample Request`  

```
 1. <SetBucketAccessControlPolicy xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2.   <Bucket>quotes</Bucket>
 3.   <AccessControlList>
 4.     <Grant>
 5.       <Grantee xsi:type="CanonicalUser">
 6.         <ID>a9a7b8863000e241bf9b1c61be666e9</ID>
 7.         <DisplayName>chriscustomer</DisplayName>
 8.       </Grantee>
 9.       <Permission>FULL_CONTROL</Permission>
10.     </Grant>
11.   </AccessControlList>
12.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
13.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
14.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
15. </SetBucketAccessControlPolicy >
```
`Sample Response`  

```
1. <GetBucketAccessControlPolicyResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <GetBucketAccessControlPolicyResponse>
3.     <Code>200</Code>
4.     <Description>OK</Description>
5.   </GetBucketAccessControlPolicyResponse>
6. </GetBucketAccessControlPolicyResponse>
```

## Access Control
<a name="SOAPSetBucketAccessControlPolicyAccessControl"></a>

You must have `WRITE_ACP` rights to the bucket in order to set the access control policy for a bucket.