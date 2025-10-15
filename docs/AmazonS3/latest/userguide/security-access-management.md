# Access management

Amazon S3 provides a variety of access management tools. The following is a list of these features and tools. You do not need all of these access
 management tools, but you must use one or more to grant access to your Amazon S3 buckets, objects, and other [S3 resources](access-management.md#access-management-resources "access-management.md#access-management-resources").
 Proper application of these tools can help make sure that your resources are accessible
 only to the intended users. 

The most commonly used access management tool is an *access
 policy*. An access policy can be a *resource-based policy*
 that is attached to an AWS resource, such as a bucket policy for a bucket. An access
 policy can also be an *identity-based policy* that is attached to an
 AWS Identity and Access Management (IAM) identity, such as an IAM user, group, or role. An access policy describes who has access to what things. Write an access
 policy to grant AWS accounts and IAM users, groups, and roles permission to perform
 operations on a resource. For example, you can grant `PUT Object` permission
 to another AWS account so that the other account can upload objects to your
 bucket.

The following are the access management tools available in Amazon S3. For a more comprehensive guide on Amazon S3 access control, see [Access control in Amazon S3](access-management.md "access-management.md").


###### Bucket policy


An Amazon S3 bucket policy is a JSON-formatted [AWS Identity and Access Management (IAM)
 resource-based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html") that is attached to a particular bucket. Use
 bucket policies to grant other AWS accounts or IAM identities permissions
 for the bucket and the objects in it. Many S3 access management use cases can be
 met by using a bucket policy. With bucket policies, you can personalize bucket
 access to help make sure that only the identities that you have approved can
 access resources and perform actions within them. For more information, see
 [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md"). 


###### Identity-based policy


An identity-based or IAM user policy is a type of [AWS Identity and Access Management (IAM) policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"). An identity-based policy is a
 JSON-formatted policy that is attached to IAM users, groups, or roles in your
 AWS account. You can use identity-based policies to grant an IAM identity
 access to your buckets or objects. You can create IAM users, groups, and roles
 in your account and attach access policies to them. You can then grant access to
 AWS resources, including Amazon S3 resources. For more information, see [Identity-based policies for
 Amazon S3](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). 


###### S3 Access Grants


Use S3 Access Grants to create access grants to your Amazon S3 data for both identities in
 corporate identity directories, such as Active Directory, and to
 AWS Identity and Access Management (IAM) identities. S3 Access Grants helps you manage data permissions at scale.
 Additionally, S3 Access Grants logs end-user identity and the application used to access
 the S3 data in AWS CloudTrail. This provides a detailed audit history down to the
 end-user identity for all access to the data in your S3 buckets. For more
 information, see [Managing access with S3 Access Grants](access-grants.md "access-grants.md").


###### Access Points


Amazon S3 Access Points simplifies managing data access at scale for applications
 that use shared datasets on S3. Access Points are named network endpoints that
 are attached to a bucket. You can use access points to perform S3 object
 operations at scale, such as uploading and retrieving objects. A bucket can have
 up to 10,000 access points attached, and for each access point, you can enforce distinct
 permissions and network controls to give you detailed control over access to
 your S3 objects. S3 Access Points can be associated with buckets in the same
 account or in another trusted account. Access Points policies are resource-based
 policies that are evaluated in conjunction with the underlying bucket policy.
 For more information, see [Managing access to shared datasets with access points](access-points.md "access-points.md").


###### Access control list (ACL)


An
 ACL is a list of grants identifying the grantee and the
 permission granted. ACLs grant basic read or write permissions to other
 AWS accounts. ACLs use an Amazon S3–specific XML schema. An ACL is a type of
 [AWS Identity and Access Management (IAM) policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"). An object ACL is used to manage access to
 an object, and a bucket ACL is used to manage access to a bucket. With bucket
 policies, there is a single policy for the entire bucket, but object ACLs are
 specified for each object. We recommend that you keep ACLs turned off, except in
 circumstances where you must individually control access for each
 object. For more information about using ACLs, see [Controlling ownership of objects and disabling ACLs
 for your bucket](about-object-ownership.md "about-object-ownership.md").


###### Warning

The majority of modern use cases in Amazon S3 do not require the use of ACLs.
 


###### Object Ownership


To manage access to your objects, you must be the owner of the object. You can
 use the Object Ownership bucket-level setting to control ownership of objects
 uploaded to your bucket. Also, use Object Ownership to turn on ACLs. By default,
 Object Ownership is set to the *Bucket owner enforced
 setting* and all ACLs are turned off. When ACLs are turned off,
 the bucket owner owns all of the objects in the bucket and exclusively manages
 access to data. To manage access, the bucket owner uses policies or another
 access management tool, excluding ACLs. For more information, see [Controlling ownership of objects and disabling ACLs
 for your bucket](about-object-ownership.md "about-object-ownership.md").


For a more comprehensive guide on Amazon S3 access control and additional best practices, see [Access control in Amazon S3](access-management.md "access-management.md").
