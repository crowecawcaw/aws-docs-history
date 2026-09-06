

# SetObjectAccessControlPolicy (SOAP API)
<a name="SOAPSetObjectAccessControlPolicy"></a>

**Note**  
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs. 

The `SetObjectAccessControlPolicy` operation sets the access control policy for an existing object. If successful, the previous access control policy for the object is entirely replaced with the specified access control policy.

**Example**  
This example gives the specified user (usually the owner) `FULL_CONTROL` access to the "Nelson" object from the "quotes" bucket.  
`Sample Request`  

```
 1. <SetObjectAccessControlPolicy xmlns="https://doc.s3.amazonaws.com/2006-03-01">
 2.   <Bucket>quotes</Bucket>
 3.   <Key>Nelson</Key>
 4.   <AccessControlList>
 5.     <Grant>
 6.       <Grantee xsi:type="CanonicalUser">
 7.         <ID>a9a7b886d6fd24a52fe8ca5bef65f89a64e0193f23000e241bf9b1c61be666e9</ID>
 8.         <DisplayName>chriscustomer</DisplayName>
 9.       </Grantee>
10.       <Permission>FULL_CONTROL</Permission>
11.     </Grant>
12.   </AccessControlList>
13.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
14.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
15.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
16. </SetObjectAccessControlPolicy>
```
`Sample Response`  

```
1. <SetObjectAccessControlPolicyResponse xmlns="https://s3.amazonaws.com/doc/2006-03-01">
2.   <SetObjectAccessControlPolicyResponse>
3.     <Code>200</Code>
4.     <Description>OK</Description>
5.   </SetObjectAccessControlPolicyResponse>
6. </SetObjectAccessControlPolicyResponse>
```

## Key
<a name="SOAPSetObjectAccessControlPolicyKey"></a>

## Access Control
<a name="SOAPSetObjectAccessControlPolicyAccessControl"></a>

You must have `WRITE_ACP` rights to the object in order to set the access control policy for a bucket.