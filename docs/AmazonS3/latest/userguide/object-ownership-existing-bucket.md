# Setting Object Ownership on an
 existing bucket

You can configure S3 Object Ownership on an existing S3 bucket. To apply
 Object Ownership when you create a bucket, see [Setting Object Ownership when you create
 a bucket](object-ownership-new-bucket.md "object-ownership-new-bucket.md").

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to disable [access control lists (ACLs)](acl-overview.md "acl-overview.md") and take ownership of every
 object in your bucket, simplifying access management for data stored in Amazon S3. By default, S3 Object Ownership 
 is set to the Bucket owner enforced setting, and ACLs are disabled for new buckets. 
 With ACLs disabled, the bucket owner owns every object in the bucket and manages access to data 
 exclusively by using access-management policies. We recommend that you keep ACLs disabled, except in unusual 
 circumstances where you must control access for each object individually. 

Object Ownership has three settings that you can use to control ownership of objects
 uploaded to your bucket and to disable or enable ACLs:


###### ACLs disabled


* **Bucket owner enforced (default)** – ACLs are
 disabled, and the bucket owner automatically owns and has full control over every
 object in the bucket. ACLs no longer affect permissions to data in the S3 bucket.
 The bucket uses policies to define access control.

###### ACLs enabled


* **Bucket owner preferred** – The bucket owner owns and
 has full control over new objects that other accounts write to the bucket with the
 `bucket-owner-full-control` canned ACL.
* **Object writer** – The AWS account that
 uploads an object owns the object, has full control over it, and can grant other users access to
 it through ACLs.
**Prerequisites**: Before you apply the Bucket owner enforced
 setting to disable ACLs, you must migrate bucket ACL permissions to bucket policies and
 reset your bucket ACLs to the default private ACL. We also recommend that you migrate
 object ACL permissions to bucket policies and edit bucket policies that require ACLs
 other than bucket owner full control ACLs. For more information, see [Prerequisites for
 disabling ACLs](object-ownership-migrating-acls-prerequisites.md "object-ownership-migrating-acls-prerequisites.md").

**Permissions**: To use this operation, you must have the
 `s3:PutBucketOwnershipControls` permission. For more information about
 Amazon S3 permissions, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html") in the *Service Authorization 
 Reference*. 

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** list, choose the name of the bucket that you want to
 apply an S3 Object Ownership setting to.
3. Choose the **Permissions** tab.
4. Under **Object Ownership**, choose **Edit**.
5. Under **Object Ownership**, to disable or enable ACLs and control
 ownership of objects uploaded in your bucket, choose one of the following
 settings:



###### ACLs disabled



	* **Bucket owner enforced** – ACLs are disabled, and the
	 bucket owner automatically owns and has full control over every object in the
	 bucket. ACLs no longer affect permissions to data in the S3 bucket. The bucket
	 uses policies to define access control.
	
	
	To require that all new buckets are created with ACLs disabled by using IAM or AWS Organizations policies, see 
	 [Disabling ACLs
	 for all new buckets (bucket owner enforced)](ensure-object-ownership.md#object-ownership-requiring-bucket-owner-enforced "ensure-object-ownership.md#object-ownership-requiring-bucket-owner-enforced").

###### ACLs enabled



	* **Bucket owner preferred** – The bucket owner owns and
	 has full control over new objects that other accounts write to the bucket with
	 the `bucket-owner-full-control` canned ACL. 
	
	
	If you apply the bucket owner preferred setting, to require all Amazon S3 uploads
	 to include the `bucket-owner-full-control` canned ACL, you can [add a bucket policy](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy")
	 that only allows object uploads that use this ACL.
	* **Object writer** – The AWS account that uploads an
	 object owns the object, has full control over it, and can grant other users
	 access to it through ACLs.
6. Choose **Save**.
To apply an Object Ownership setting for an existing bucket, use the
 `put-bucket-ownership-controls` command with the
 `--ownership-controls` parameter. Valid values for ownership are
 `BucketOwnerEnforced`, `BucketOwnerPreferred`, or
 `ObjectWriter`.

This example applies the Bucket owner enforced setting for an existing bucket by using the
 AWS CLI:


```
aws s3api put-bucket-ownership-controls --bucket `amzn-s3-demo-bucket` --ownership-controls="Rules=[{ObjectOwnership=BucketOwnerEnforced}]"
```
For information about `put-bucket-ownership-controls`, see [put-bucket-ownership-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html") in the *AWS Command Line Interface User Guide*. 

This example applies the `BucketOwnerEnforced` setting for Object Ownership on
 an existing bucket by using the AWS SDK for Java:


```
         // Build the ObjectOwnership for BucketOwnerEnforced
         OwnershipControlsRule rule = OwnershipControlsRule.builder()
                .objectOwnership(ObjectOwnership.BucketOwnerEnforced)
                .build();

         OwnershipControls ownershipControls = OwnershipControls.builder()
                   .rules(rule)
                   .build()

          // Build the PutBucketOwnershipControlsRequest
          PutBucketOwnershipControlsRequest putBucketOwnershipControlsRequest =
                PutBucketOwnershipControlsRequest.builder()
                        .bucket(BUCKET_NAME)
                        .ownershipControls(ownershipControls)
                        .build();
                        
          // Send the request to Amazon S3 
          s3client.putBucketOwnershipControls(putBucketOwnershipControlsRequest);
```
To use AWS CloudFormation to apply an Object Ownership setting for an existing bucket, see
 [AWS::S3::Bucket OwnershipControls](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.md") in the
 *AWS CloudFormation User Guide*.

To use the REST API to apply an Object Ownership setting to an existing S3
 bucket, use `PutBucketOwnershipControls`. For more information, see
 [PutBucketOwnershipControls](../API/API_PutBucketOwnershipControls.md "../API/API_PutBucketOwnershipControls.md") in the
 *Amazon Simple Storage Service API Reference*.

**Next steps**: After you apply the Bucket owner enforced or
 bucket owner preferred settings for Object Ownership, you can further take the following steps:


* [Bucket owner enforced](ensure-object-ownership.md#object-ownership-requiring-bucket-owner-enforced "ensure-object-ownership.md#object-ownership-requiring-bucket-owner-enforced") – 
 Require that all new buckets are created with ACLs disabled by using an IAM or Organizations policy.
* [Bucket owner preferred](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy") – Add an 
 S3 bucket policy to require the `bucket-owner-full-control` canned ACL for all object uploads 
 to your bucket.
