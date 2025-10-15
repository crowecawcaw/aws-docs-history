# Bucket policies for Amazon S3

A bucket policy is a resource-based policy that you can use to grant access permissions to
 your Amazon S3 bucket and the objects in it. Only the bucket owner can associate a policy with a
 bucket. The permissions attached to the bucket apply to all of the objects in the bucket
 that are owned by the bucket owner. These permissions don't apply to objects that are owned
 by other AWS accounts.

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to control ownership
 of objects uploaded to your bucket and to disable or enable access control lists (ACLs). By
 default, Object Ownership is set to the Bucket owner enforced setting and all ACLs are
 disabled. The bucket owner owns all the objects in the bucket and manages access to data
 exclusively using policies.

Bucket policies use JSON-based AWS Identity and Access Management (IAM) policy language. You can use bucket
 policies to add or deny permissions for the objects in a bucket. Bucket policies can allow
 or deny requests based on the elements in the policy. These elements include the requester,
 S3 actions, resources, and aspects or conditions of the request (such as the IP address
 that's used to make the request). 

For example, you can create a bucket policy that does the following: 


* Grants other accounts cross-account permissions to upload objects to your S3
 bucket
* Makes sure that you, the bucket owner, has full control of the uploaded
 objects
For more information, see [Examples of Amazon S3 bucket policies](example-bucket-policies.md "example-bucket-policies.md").

###### Important

You can't use a bucket policy to prevent deletions or transitions by an [S3 Lifecycle](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md") rule. For example, even if your
 bucket policy denies all actions for all principals, your S3 Lifecycle configuration
 still functions as normal.

The topics in this section provide examples and show you how to add a bucket policy in the
 S3 console. For information about identity-based policies, see [Identity-based policies for
 Amazon S3](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). For information about bucket
 policy language, see [Policies and permissions in Amazon S3](access-policy-language-overview.md "access-policy-language-overview.md").

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

###### Topics

* [Adding a bucket policy by using the Amazon S3 console](add-bucket-policy.md "add-bucket-policy.md")
* [Controlling access from VPC
 endpoints with bucket policies](example-bucket-policies-vpc-endpoint.md "example-bucket-policies-vpc-endpoint.md")
* [Examples of Amazon S3 bucket policies](example-bucket-policies.md "example-bucket-policies.md")
* [Bucket policy examples using condition keys](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md")
