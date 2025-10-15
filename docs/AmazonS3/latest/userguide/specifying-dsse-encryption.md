# Specifying dual-layer server-side encryption with AWS KMS
 keys (DSSE-KMS)

You can apply encryption when you are either uploading a new object or copying an existing
 object. 

You can specify DSSE-KMS by using the Amazon S3 console, Amazon S3 REST API, and the AWS Command Line Interface
 (AWS CLI). For more information, see the following topics. 

###### Note

You can use multi-Region AWS KMS keys in Amazon S3. However, Amazon S3 currently treats multi-Region keys 
as though they were single-Region keys, and does not use the multi-Region features of the key. For more 
information, see 
[Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html "https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html") in the *AWS Key Management Service Developer Guide*.

###### Note

If you want to use a KMS key that is owned by a different
 account, you must have permission to use the key. For more information about cross-account permissions for KMS keys,
 see [Creating KMS keys that other accounts can use](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html#cross-account-console "https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html#cross-account-console") in the 
 *AWS Key Management Service Developer Guide*. 

This section describes how to set or change the type of encryption of an object to
 use dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS) by
 using the Amazon S3 console.

###### Note


* You can change an object's encryption if your object is less than 5 GB. If your object is greater than 5 GB, you must use the [AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload") or [AWS SDKs](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md") to change an object's encryption.
* For a list of additional permissions required to change an object's encryption, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For example policies that grant this permission, see [Identity-based policy examples for Amazon S3](example-policies-s3.md "example-policies-s3.md").
* If you change an object's encryption, a new object is created to replace the old one.
 If S3 Versioning is enabled, a new version of the object is created, and the existing
 object becomes an older version. The role that changes the property also becomes the owner
 of the new object (or object version).
###### To add or change encryption for an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Buckets**, and then choose
 the **General purpose buckets** tab. Navigate to the Amazon S3 bucket or
 folder that contains the objects you want to change.
3. Select the check box for the objects you want to
 change.
4. On the **Actions** menu, choose **Edit server-side encryption** from
 the list of options that appears.
5. Scroll to the **Server-side encryption** section.
6. Under **Encryption settings**, choose **Use bucket settings for default encryption** or **Override bucket settings for default encryption**.
7. If you chose **Override bucket settings for default encryption**,
 configure the following encryption settings.


	1. Under **Encryption type**, choose **Dual-layer server-side encryption with AWS Key Management Service keys (DSSE-KMS)**.
	2. Under **AWS KMS key**, do one of the following to choose your
	 KMS key:
	
	
	
	
		* To choose from a list of available KMS keys, choose **Choose from your
		 AWS KMS keys**, and then choose your **KMS key** from
		 the list of available keys.
		
		
		Both the AWS managed key (`aws/s3`) and your customer managed keys appear in this
		 list. For more information about customer managed keys, see [Customer keys and AWS
		 keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt") in the *AWS Key Management Service Developer Guide*.
		* To enter the KMS key ARN, choose **Enter AWS KMS key ARN**,
		 and then enter your KMS key ARN in the field that appears.
		* To create a new customer managed key in the AWS KMS console, choose **Create a
		 KMS key**.
		
		
		For more information about creating an AWS KMS key, see [Creating
		 keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html "https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html") in the *AWS Key Management Service Developer Guide*.
	###### Important
	
	You can use only KMS keys that are available in the same AWS Region
	 as the bucket. The Amazon S3 console lists only the first 100 KMS keys in
	 the same Region as the bucket. To use a KMS key that is not listed,
	 you must enter your KMS key ARN. If you want to use a KMS key that
	 is owned by a different account, you must first have permission to use
	 the key, and then you must enter the KMS key ARN.
	
	Amazon S3 supports only symmetric encryption KMS keys, and not asymmetric
	 KMS keys. For more information, see [Identifying
	 asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html "https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html") in the
	 *AWS Key Management Service Developer Guide*.
8. For **Bucket Key**, choose **Disable**.
 S3 Bucket Keys aren't supported for DSSE-KMS.
9. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for storage class, ACLs, object tags, metadata, server-side encryption, and additional checksums.
10. Choose **Save changes**.
###### Note

This action applies encryption to all specified objects. When you're encrypting folders,
 wait for the save operation to finish before adding new objects to the folder.

When you create an object—that is, when you upload a new object or copy an
 existing object—you can specify the use of dual-layer server-side encryption
 with AWS KMS keys (DSSE-KMS) to encrypt your data. To do this, add the
 `x-amz-server-side-encryption` header to the request. Set the value
 of the header to the encryption algorithm `aws:kms:dsse`. Amazon S3 confirms
 that your object is stored with DSSE-KMS encryption by returning the response header
 `x-amz-server-side-encryption`. 

If you specify the `x-amz-server-side-encryption` header with a value of
 `aws:kms:dsse`, you can also use the following request headers:


* `x-amz-server-side-encryption-aws-kms-key-id: `SSEKMSKeyId``
* `x-amz-server-side-encryption-context: `SSEKMSEncryptionContext``
###### Topics

* [Amazon S3 REST API operations that support
 DSSE-KMS](#dsse-request-headers-kms "#dsse-request-headers-kms")
* [Encryption context
 (x-amz-server-side-encryption-context)](#s3-dsse-encryption-context "#s3-dsse-encryption-context")
* [AWS KMS key ID
 (x-amz-server-side-encryption-aws-kms-key-id)](#s3-dsse-key-id-api "#s3-dsse-key-id-api")

### Amazon S3 REST API operations that support
 DSSE-KMS


The following REST API operations accept the
 `x-amz-server-side-encryption`,
 `x-amz-server-side-encryption-aws-kms-key-id`, and
 `x-amz-server-side-encryption-context` request headers.



* [PutObject](../API/API_PutObject.md "../API/API_PutObject.md") – When you upload data by
 using the `PUT` API operation, you can specify these request
 headers.
* [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") – When you copy an object,
 you have both a source object and a target object. When you pass
 DSSE-KMS headers with the `CopyObject` operation, they are applied
 only to the target object. When you're copying an existing object,
 regardless of whether the source object is encrypted or not, the
 destination object is not encrypted unless you explicitly request
 server-side encryption.
* [POST Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
 – When you use a `POST` operation to upload an object,
 instead of the request headers, you provide the same information in the
 form fields.
* [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md") – When you
 upload large objects by using a multipart upload, you can specify these
 headers in the `CreateMultipartUpload` request.

The response headers of the following REST API operations return the
 `x-amz-server-side-encryption` header when an object is stored
 with server-side encryption.



* [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
* [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
* [POST
 Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
* [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
* [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
* [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
* [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
* [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
* [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")

###### Important


* All `GET` and `PUT` requests for an object that's
 protected by AWS KMS fail if you don't make them by using Secure
 Sockets Layer (SSL), Transport Layer Security (TLS), or Signature
 Version 4.
* If your object uses DSSE-KMS, don't send encryption request headers for
 `GET` requests and `HEAD` requests, or
 you'll get an **`HTTP 400 (Bad Request)`**
 error.

### Encryption context
 (`x-amz-server-side-encryption-context`)


If you specify `x-amz-server-side-encryption:aws:kms:dsse`, the Amazon S3 API
 supports an encryption context with the `x-amz-server-side-encryption-context`
 header. An encryption context is a set of key-value pairs that contain additional
 contextual information about the data.


Amazon S3 automatically uses the object's Amazon Resource Name (ARN) as the
 encryption context pair; for example,
 `arn:aws:s3:::`object_ARN``.


You can optionally provide an additional encryption context pair by using the
 `x-amz-server-side-encryption-context` header. However, because the
 encryption context is not encrypted, make sure it does not include sensitive information.
 Amazon S3 stores this additional key pair alongside the default encryption context.


For information about the encryption context in Amazon S3, see [Encryption context](UsingKMSEncryption.md#encryption-context "UsingKMSEncryption.md#encryption-context"). For general
 information about the encryption context, see [AWS Key Management Service Concepts -
 Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context") in the *AWS Key Management Service Developer Guide*. 


### AWS KMS key ID
 (`x-amz-server-side-encryption-aws-kms-key-id`)


You can use the `x-amz-server-side-encryption-aws-kms-key-id` header to
 specify the ID of the customer managed key that's used to protect the data. If you specify
 the `x-amz-server-side-encryption:aws:kms:dsse` header but don't
 provide the `x-amz-server-side-encryption-aws-kms-key-id` header,
 Amazon S3 uses the AWS managed key (`aws/s3`) to protect the data. If
 you want to use a customer managed key, you must provide the
 `x-amz-server-side-encryption-aws-kms-key-id` header of the
 customer managed key.


###### Important

When you use an AWS KMS key for server-side encryption in Amazon S3, you must choose a symmetric encryption KMS key. 
Amazon S3 supports only symmetric encryption KMS keys. For more information about these keys, see 
[Symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks") in the *AWS Key Management Service Developer Guide*.


When you upload a new object or copy an existing object, you can specify the use
 of DSSE-KMS to encrypt your data. To do this, add the `--server-side-encryption
 aws:kms:dsse` parameter to the request. Use the `--ssekms-key-id
 `example-key-id`` parameter to add your
 [customer managed
 AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") that you created. If you specify
 `--server-side-encryption aws:kms:dsse`, but do not provide an AWS KMS
 key ID, then Amazon S3 will use the AWS managed key (`aws/s3`).


```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key `example-object-key` --server-side-encryption aws:kms:dsse --ssekms-key-id `example-key-id` --body `filepath`
```
You can encrypt an unencrypted object to use DSSE-KMS by copying the object back
 in place.


```
aws s3api copy-object --bucket `amzn-s3-demo-bucket` --key `example-object-key` --copy-source `amzn-s3-demo-bucket`/`example-object-key` --server-side-encryption aws:kms:dsse --ssekms-key-id `example-key-id`
```
