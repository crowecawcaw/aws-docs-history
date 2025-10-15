# GetObjectAcl

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

###### Note

This operation is not supported for directory buckets.

Returns the access control list (ACL) of an object. To use this operation, you must have
 `s3:GetObjectAcl` permissions or `READ_ACP` access to the object. For more
 information, see [Mapping of ACL
 permissions and access policy permissions](../userguide/acl-overview.md#acl-access-policy-permission-mapping "../userguide/acl-overview.md#acl-access-policy-permission-mapping") in the *Amazon S3 User Guide*


This functionality is not supported for Amazon S3 on Outposts.

By default, GET returns ACL information about the current version of an object. To return ACL
 information about a different version, use the versionId subresource.

###### Note

If your bucket uses the bucket owner enforced setting for S3 Object Ownership, requests to read
 ACLs are still supported and return the `bucket-owner-full-control` ACL with the owner
 being the account that created the bucket. For more information, see  [Controlling object ownership and
 disabling ACLs](../userguide/about-object-ownership.md "../userguide/about-object-ownership.md") in the *Amazon S3 User Guide*.

The following operations are related to `GetObjectAcl`:


* [GetObject](API_GetObject.md "API_GetObject.md")
* [GetObjectAttributes](API_GetObjectAttributes.md "API_GetObjectAttributes.md")
* [DeleteObject](API_DeleteObject.md "API_DeleteObject.md")
* [PutObject](API_PutObject.md "API_PutObject.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /{Key+}?acl&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetObjectAcl_RequestSyntax "#API_GetObjectAcl_RequestSyntax")**


The bucket name that contains the object for which to get the ACL information. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_GetObjectAcl_RequestSyntax "#API_GetObjectAcl_RequestSyntax")**


The key of the object for which to get the ACL information.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_GetObjectAcl_RequestSyntax "#API_GetObjectAcl_RequestSyntax")**


Version ID used to reference a specific version of the object.


###### Note

This functionality is not supported for directory buckets.




**[x-amz-expected-bucket-owner](#API_GetObjectAcl_RequestSyntax "#API_GetObjectAcl_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_GetObjectAcl_RequestSyntax "#API_GetObjectAcl_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
x-amz-request-charged: `RequestCharged`
<?xml version="1.0" encoding="UTF-8"?>
<[AccessControlPolicy](#AmazonS3-GetObjectAcl-response-GetObjectAclOutput "#AmazonS3-GetObjectAcl-response-GetObjectAclOutput")>
   <[Owner](#AmazonS3-GetObjectAcl-response-Owner "#AmazonS3-GetObjectAcl-response-Owner")>
      <[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>***string***</[DisplayName](API_Owner.md#AmazonS3-Type-Owner-DisplayName "API_Owner.md#AmazonS3-Type-Owner-DisplayName")>
      <[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>***string***</[ID](API_Owner.md#AmazonS3-Type-Owner-ID "API_Owner.md#AmazonS3-Type-Owner-ID")>
   </[Owner](#AmazonS3-GetObjectAcl-response-Owner "#AmazonS3-GetObjectAcl-response-Owner")>
   <[AccessControlList](#AmazonS3-GetObjectAcl-response-Grants "#AmazonS3-GetObjectAcl-response-Grants")>
      <Grant>
         <[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
            <[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>***string***</[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>
            <[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>***string***</[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>
            <[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>***string***</[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>
            <[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>***string***</[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>
            <[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>***string***</[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>
         </[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
         <[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>***string***</[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>
      </Grant>
   </[AccessControlList](#AmazonS3-GetObjectAcl-response-Grants "#AmazonS3-GetObjectAcl-response-Grants")>
</[AccessControlPolicy](#AmazonS3-GetObjectAcl-response-GetObjectAclOutput "#AmazonS3-GetObjectAcl-response-GetObjectAclOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_GetObjectAcl_ResponseSyntax "#API_GetObjectAcl_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





The following data is returned in XML format by the service.





**[AccessControlPolicy](#API_GetObjectAcl_ResponseSyntax "#API_GetObjectAcl_ResponseSyntax")**


Root level tag for the AccessControlPolicy parameters.


Required: Yes




**[Grants](#API_GetObjectAcl_ResponseSyntax "#API_GetObjectAcl_ResponseSyntax")**


A list of grants.


Type: Array of [Grant](API_Grant.md "API_Grant.md") data types




**[Owner](#API_GetObjectAcl_ResponseSyntax "#API_GetObjectAcl_ResponseSyntax")**


 Container for the bucket owner's display name and ID.


Type: [Owner](API_Owner.md "API_Owner.md") data type




## Errors





**NoSuchKey** 


The specified key does not exist.


HTTP Status Code: 404




## Examples


### Sample Request


The following request returns information, including the ACL, of the object
 `my-image.jpg`.



```

         GET /my-image.jpg?acl HTTP/1.1
         Host: bucket.s3.<Region>.amazonaws.com
         Date: Wed, 28 Oct 2009 22:32:00 GMT
         Authorization: authorization string
         
```

### Sample Response


This example illustrates one usage of GetObjectAcl.



```

            HTTP/1.1 200 OK
            x-amz-id-2: eftixk72aD6Ap51TnqcoF8eFidJG9Z/2mkiDFu8yU9AS1ed4OpIszj7UDNEHGran
            x-amz-request-id: 318BC8BC148832E5
            x-amz-version-id: 4HL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nrjfkd
            Date: Wed, 28 Oct 2009 22:32:00 GMT
            Last-Modified: Sun, 1 Jan 2006 12:00:00 GMT
            Content-Length: 124
            Content-Type: text/plain
            Connection: close
            Server: AmazonS3
 
            <AccessControlPolicy>
              <Owner>
                <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
                <DisplayName>mtd@amazon.com</DisplayName>
              </Owner>
              <AccessControlList>
                <Grant>
                 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                   <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
                   <DisplayName>mtd@amazon.com</DisplayName>
                   <Type>CanonicalUser</Type>
                  </Grantee>
                  <Permission>FULL_CONTROL</Permission>
               </Grant>
              </AccessControlList>
            </AccessControlPolicy>
         
```

### Sample Request: Getting the ACL of the specific version of an object


The following request returns information, including the ACL, of the specified version of the
 object, my-image.jpg.



```

            GET /my-image.jpg?versionId=3/L4kqtJlcpXroDVBH40Nr8X8gdRQBpUMLUo&acl HTTP/1.1
            Host: bucket.s3.<Region>.amazonaws.com
            Date: Wed, 28 Oct 2009 22:32:00 GMT
            Authorization: authorization string
         
```

### Sample Response: Showing the ACL of the specific version


This example illustrates one usage of GetObjectAcl.



```

            HTTP/1.1 200 OK
            x-amz-id-2: eftixk72aD6Ap51TnqcoF8eFidJG9Z/2mkiDFu8yU9AS1ed4OpIszj7UDNEHGran
            x-amz-request-id: 318BC8BC148832E5
            Date: Wed, 28 Oct 2009 22:32:00 GMT
            Last-Modified: Sun, 1 Jan 2006 12:00:00 GMT
            x-amz-version-id: 3/L4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo
            Content-Length: 124
            Content-Type: text/plain
            Connection: close
            Server: AmazonS3
 
            <AccessControlPolicy>
             <Owner>
               <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
               <DisplayName>mdtd@amazon.com</DisplayName>
             </Owner>
             <AccessControlList>
               <Grant>
                 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                   <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID>
                   <DisplayName>mdtd@amazon.com</DisplayName>
                   <Type>CanonicalUser</Type>
                 </Grantee>
                 <Permission>FULL_CONTROL</Permission>
               </Grant>
             </AccessControlList>
            </AccessControlPolicy>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectAcl")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAcl "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectAcl")
