# How Amazon S3 works with IAM

Before you use IAM to manage access to Amazon S3, learn what IAM features are
 available to use with Amazon S3.



IAM features you can use with Amazon S3| IAM feature | Amazon S3 support |
| --- | --- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies") | 
 
 Yes |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies") | 
 
 Yes |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions") | 
 
 Yes |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources") | 
 
 Yes |
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys") | 
 
 Yes |
| [ACLs](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls") | 
 
 Yes |
| [ABAC (tags in
 policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags") | 
 
 Partial |
| [Temporary
 credentials](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds") | 
 
 Yes |
| [Forward access sessions (FAS)](#security_iam_service-with-iam-principal-permissions "#security_iam_service-with-iam-principal-permissions") | 
 
 Yes |
| [Service
 roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service") | 
 
 Yes |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked") | 
 
 Partial |

To get a high-level view of how Amazon S3 and other AWS services work with most IAM
 features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html") in the
 *IAM User Guide*.

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").


## Identity-based
 policies for Amazon S3


**Supports identity-based policies:**
 
 
 Yes


Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
 policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
 policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html") in the
 *IAM User Guide*.


With IAM identity-based policies, you can specify allowed or denied actions and
 resources as well as the conditions under which actions are allowed or denied. You
 can't specify the principal in an identity-based policy because it applies to the user
 or role to which it is attached. To learn about all of the elements that you can use in a
 JSON policy, see [IAM JSON
 policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html") in the
 *IAM User Guide*.


### 
 Identity-based policy examples for Amazon S3


To view examples of Amazon S3 identity-based policies, see [Identity-based policies for
 Amazon S3](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").


## Resource-based
 policies within Amazon S3


**Supports resource-based policies:**
 
 
 Yes


Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are 
 IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service 
 administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
 a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html") in a resource-based policy. Principals 
 can include accounts, users, roles, federated users, or AWS services.


To enable cross-account access, you can specify an entire account or IAM entities
 in another account as the principal in a
 resource-based policy. Adding a cross-account principal to a resource-based
 policy is only half of establishing the trust relationship. When the principal and the
 resource are in different AWS accounts, an IAM administrator in the trusted account 
 must also grant the principal entity (user or role) permission to access the resource. They grant 
 permission by attaching an identity-based policy to the entity. However, if a resource-based 
 policy grants access to a principal in the same account, no additional identity-based policy is 
 required. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html") in the
 *IAM User Guide*.


The Amazon S3 service supports *bucket policies*,
 *access points policies*, and *access
 grants*:



* Bucket policies are resource-based policies that are attached to an Amazon S3
 bucket. A bucket policy defines which principals can perform actions on the
 bucket.
* Access point policies are resource-based polices that are evaluated in conjunction
 with the underlying bucket policy.
* Access grants are a simplified model for defining access permissions to data in
 Amazon S3 by prefix, bucket, or object. For information about S3 Access Grants, see [Managing access with S3 Access Grants](access-grants.md "access-grants.md").

### Principals for bucket policies


The `Principal` element specifies the user, account, service, or other
 entity that is either allowed or denied access to a resource.
 The following are examples of specifying `Principal`. For more
 information, see [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html")
 in the *IAM User Guide*.


#### Grant permissions to an AWS account


To grant permissions to an AWS account, identify the account using the
 following format.



```
"AWS":"`account-ARN`"
```

The following are examples.



```
"Principal":{"AWS":"arn:aws:iam::`AccountIDWithoutHyphens`:root"}
```


```
"Principal":{"AWS":["arn:aws:iam::`AccountID1WithoutHyphens`:root","arn:aws:iam::`AccountID2WithoutHyphens`:root"]}
```

###### Note

The examples above grant permissions to the root user, which delegates permissions to the account level. However, IAM policies are still required on the specific roles and users in the account.


#### Grant permissions to an
 IAM user


To grant permission to an IAM user within your account, you must provide an
 `"AWS":"`user-ARN`"` name-value
 pair.



```
"Principal":{"AWS":"arn:aws:iam::`account-number-without-hyphens`:user/`username`"}
```

For detailed examples that provide step-by-step instructions, see [Example 1: Bucket owner
 granting its users bucket permissions](example-walkthroughs-managing-access-example1.md "example-walkthroughs-managing-access-example1.md") and [Example 3: Bucket owner
 granting permissions to objects it does not own](example-walkthroughs-managing-access-example3.md "example-walkthroughs-managing-access-example3.md").


###### Note

If an IAM identity is deleted after you update your bucket policy, the bucket policy
 will show a unique identifier in the principal element instead of an ARN.
 These unique IDs are never reused, so you can safely remove principals with
 unique identifiers from all of your policy statements. For more information
 about unique identifiers, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids") in the *IAM User Guide*.


#### Grant anonymous permissions


###### Warning

Use caution when granting anonymous access to your Amazon S3 bucket. When you grant
 anonymous access, anyone in the world can access your bucket. We highly recommend
 that you never grant any kind of anonymous write access to your S3 bucket.


To grant permission to everyone, also referred as anonymous access, you set
 the wildcard (`"*"`) as the `Principal` value. For
 example, if you configure your bucket as a website, you want all the objects in
 the bucket to be publicly accessible.



```
"Principal":"*"
```


```
"Principal":{"AWS":"*"}
```

Using `"Principal": "*"` with an `Allow` effect in a
 resource-based policy allows anyone, even if they’re not signed in to AWS, to
 access your resource. 


Using `"Principal" : { "AWS" : "*" }` with an `Allow`
 effect in a resource-based policy allows any root user, IAM user, assumed-role
 session, or federated user in any account in the same partition to access your
 resource.


For anonymous users, these two methods are equivalent. For more information, see [All principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous") in the *IAM User Guide*.


You cannot use a wildcard to match part of a principal name or ARN.


###### Important

In AWS access control policies, the Principals "\*" and {"AWS": "\*"} behave identically.


#### Restrict resource permissions


You can also use resource policy to restrict access to resources that would otherwise be available to IAM principals. Use a `Deny` statement to prevent access.


The following example blocks access if a secure transport protocol isn’t used:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "DenyBucketAccessIfSTPNotUsed",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 }
 ]
}`

```





Using `"Principal": "*"` so that this restriction applies to everyone is a best practice for this policy, instead of attempting to deny access only to specific accounts or principals using this method. 


#### Require access through CloudFront URLs


You can require that your users access your Amazon S3 content only by using CloudFront URLs instead of Amazon S3 URLs. To do this, create a CloudFront origin access control (OAC). Then, change the permissions on your S3 data. In your bucket policy, you can set CloudFront as the Principal as follows:



```
"Principal":{"Service":"cloudfront.amazonaws.com"}
```

Use a `Condition` element in the policy to allow CloudFront to access the bucket only when the request is on behalf of the CloudFront distribution that contains the S3 origin.



```

        "Condition": {
           "StringEquals": {
              "AWS:SourceArn": "arn:aws:cloudfront::`111122223333`:distribution/`CloudFront-distribution-ID`"
           }
        }
        
```

For more information about requiring S3 access through CloudFront URLs, see [Restricting access to an Amazon Simple Storage Service origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html") in the *Amazon CloudFront Developer Guide*. For more information about the security and privacy benefits of using Amazon CloudFront, see [Configuring secure access and restricting access to content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecurityAndPrivateContent.html "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecurityAndPrivateContent.html"). 


### Resource-based policy examples for Amazon S3



* To view policy examples for Amazon S3 buckets, see [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md").
* To view policy examples for access points, see [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").

## Policy actions
 for Amazon S3


**Supports policy actions:**
 
 
 Yes


Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform 
 **actions** on what **resources**, and under what **conditions**.


The `Action` element of a JSON policy describes the
 actions that you can use to allow or deny access in a policy. Policy
 actions usually have the same name as the associated AWS API operation. There are some exceptions, such as *permission-only 
 actions* that don't have a matching API operation. There are also some operations that require multiple actions in a policy. 
 These additional actions are called *dependent actions*.


Include actions in a policy to grant permissions to perform the associated operation.


The following shows different types of mapping relationship between S3 API operations and the
 required policy actions.



* One-to-one mapping with the same name. For example, to use the `PutBucketPolicy` API operation, the `s3:PutBucketPolicy` policy action is required.
* One-to-one mapping with different names. For example, to use the `ListObjectsV2` API operation, the `s3:ListBucket` policy action is required.
* One-to-many mapping. For example, to use the `HeadObject` API operation, the
 `s3:GetObject` is required. Also, when you use S3
 Object Lock and want to get an object's Legal Hold status or retention
 settings, the corresponding `s3:GetObjectLegalHold` or
 `s3:GetObjectRetention` policy actions are also required
 before you can use the `HeadObject` API operation.
* Many-to-one mapping. For example, to use the `ListObjectsV2` or `HeadBucket` API operations, the `s3:ListBucket` policy action is required.


To see a list of Amazon S3 actions for use in policies, see [Actions defined by Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-actions-as-permissions "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-actions-as-permissions") in the
 *Service Authorization Reference*. For a complete list of Amazon S3 API operations, see [Amazon S3 API Actions](../API/API_Operations.md "../API/API_Operations.md") in the *Amazon Simple Storage Service API Reference*.


For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").


Policy actions in Amazon S3 use the following prefix before the action:



```
s3
```

To specify multiple actions in a single statement, separate them with commas.



```
"Action": [
      "s3:`action1`",
      "s3:`action2`"
         ]
```



### Bucket operations


Bucket operations are S3 API operations that operate on the bucket resource type. For
 example, `CreateBucket`, `ListObjectsV2`, and
 `PutBucketPolicy`. S3 policy actions for bucket operations
 require the `Resource` element in bucket policies or IAM
 identity-based policies to be the S3 bucket type Amazon Resource Name (ARN) identifier in the following
 example format. 



```
"Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
```

The following bucket policy grants the user
 ``Akua`` with account
 ``12345678901`` the
 `s3:ListBucket` permission to perform the [ListObjectsV2](../API/API_PutObject.md "../API/API_PutObject.md")
 API operation and list objects in an S3 bucket.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Allow Akua to list objects in the bucket",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Akua"
 },
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 }
 ]
}`

```





###### Bucket operations in policies for access points for general purpose buckets


Permissions granted in an access point for general purpose buckets policy are effective only if the underlying
 bucket allows the same permissions. When you use S3 Access Points, you must
 delegate access control from the bucket to the access point or add the same permissions in
 the access point policies to the underlying bucket's policy. For more information, see
 [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md"). In access point policies, S3 policy actions for bucket operations require you to use
 the access point ARN for the `Resource` element in the following
 format. 



```
"Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point`"
```

The following access point policy grants the user
 ``Akua`` with account
 ``12345678901`` the
 `s3:ListBucket` permission to perform the [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md") API operation through the S3 access point named
 ``example-access-point``. This permission
 allows ``Akua`` to list the objects in the bucket
 that's associated with ``example-access-point``. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "AllowAkuaToListObjectsInBucketThroughAccessPoint",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`Akua`"
 },
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:`us-west-2`:`111122223333`:accesspoint/`example-access-point`"
 }
 ]
}`

```





###### Note

Not all bucket operations are supported by access points for general purpose buckets. For more information, see [Access points compatibility with S3
 operations](access-points-service-api-support.md#access-points-operations-support "access-points-service-api-support.md#access-points-operations-support").


###### Bucket operations in policies for access points for directory buckets


Permissions granted in an access points for directory buckets policy are effective only if the underlying
 bucket allows the same permissions. When you use S3 Access Points, you must
 delegate access control from the bucket to the access point or add the same permissions in
 the access point policies to the underlying bucket's policy. For more information, see
 [Configuring IAM policies for using access points for directory buckets](access-points-directory-buckets-policies.md "access-points-directory-buckets-policies.md"). In access point policies, S3 policy actions for bucket operations require you to use
 the access point ARN for the `Resource` element in the following
 format. 



```
"Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point--usw2-az1--xa-s3`"
```

The following access point policy grants the user
 ``Akua`` with account
 ``12345678901`` the
 `s3:ListBucket` permission to perform the [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md") API operation through the access point named
 ``example-access-point--usw2-az1--xa-s3``. This permission
 allows ``Akua`` to list the objects in the bucket
 that's associated with ``example-access-point--usw2-az1--xa-s3``. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "AllowAkuaToListObjectsInTheBucketThroughAccessPoint",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:user/Akua"
 },
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3express:us-east-1:111122223333:accesspoint/example-access-point-usw2-az1-xa-s3"
 }
 ]
}`

```





###### Note

Not all bucket operations are supported by access points for directory buckets. For more information, see [Object operations for access points for directory buckets](access-points-directory-buckets-service-api-support.md "access-points-directory-buckets-service-api-support.md").


### Object operations


Object operations are S3 API operations that act upon the object resource type. For
 example, `GetObject`, `PutObject`, and
 `DeleteObject`. S3 policy actions for object operations require
 the `Resource` element in policies to be the S3 object ARN in the
 following example formats. 



```
"Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
```


```
"Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`prefix`/*"
```

###### Note

The object ARN must contain a forward slash after the bucket name, as seen in the previous
 examples.


The following bucket policy grants the user
 ``Akua`` with account
 ``12345678901`` the
 `s3:PutObject` permission. This permission allows
 ``Akua`` to use the [PutObject](../API/API_PutObject.md "../API/API_PutObject.md") API operation to upload objects to the S3
 bucket named
 ``amzn-s3-demo-bucket``.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Allow `Akua` to upload objects",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`Akua`"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```





###### Object operations in access point policies


When you use S3 Access Points to control access to object operations, you can
 use access point policies. When you use access point policies, S3 policy actions for object
 operations require you to use the access point ARN for the `Resource`
 element in the following format:
 `arn:aws:s3:`region`:`account-id`:accesspoint/`access-point-name`/object/`resource``.
 For object operations that use access points, you must include the
 `/object/` value after the whole access point ARN in the
 `Resource` element. Here are some examples.



```
"Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point`/object/*"
```


```
"Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point`/object/`prefix`/*"
```

The following access point policy grants the user
 ``Akua`` with account
 ``12345678901`` the
 `s3:GetObject` permission. This permission allows
 ``Akua`` to perform the [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") API operation through the access point named
 ``example-access-point`` on all objects in
 the bucket that's associated with the access point. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Allow `Akua` to get objects through access point",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`Akua`"
 },
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:`us-east-1`:`111122223333`:accesspoint/`example-access-point`/object/*"
 }
 ]
}`

```





###### Note

Not all object operations are supported by access points. For more information, see [Access points compatibility with S3
 operations](access-points-service-api-support.md#access-points-operations-support "access-points-service-api-support.md#access-points-operations-support").


###### Object operations in policies for access points for directory buckets


When you use access points for directory buckets to control access to object operations, you can
 use access point policies. When you use access point policies, S3 policy actions for object
 operations require you to use the access point ARN for the `Resource`
 element in the following format:
 `arn:aws:s3:`region`:`account-id`:accesspoint/`access-point-name`/object/`resource``.
 For object operations that use access points, you must include the
 `/object/` value after the whole access point ARN in the
 `Resource` element. Here are some examples.



```
"Resource": "arn:aws:s3express:`us-west-2`:`123456789012`:accesspoint/`example-access-point--usw2-az1--xa-s3`/object/*"
```


```
"Resource": "arn:aws:s3express:`us-west-2`:`123456789012`:accesspoint/`example-access-point--usw2-az1--xa-s3`/object/`prefix`/*"
```

The following access point policy grants the user
 ``Akua`` with account
 ``12345678901`` the
 `s3:GetObject` permission. This permission allows
 ``Akua`` to perform the [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") API operation through the access point named
 ``example-access-point--usw2-az1--xa-s3`` on all objects in
 the bucket that's associated with the access point. 



```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Allow `Akua` to get objects through access point",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`12345678901`:user/`Akua`"
            },
            "Action": "s3express:CreateSession","s3:GetObject"
            "Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point--usw2-az1--xa-s3`/object/*"
        }
    ]
}
```

###### Note

Not all object operations are supported by access points for directory buckets. For more information, see [Object operations for access points for directory buckets](access-points-directory-buckets-service-api-support.md "access-points-directory-buckets-service-api-support.md").


### Access point for general purpose bucket operations


Access point operations are S3 API operations that operate on the
 `accesspoint` resource type. For example,
 `CreateAccessPoint`, `DeleteAccessPoint`, and
 `GetAccessPointPolicy`. S3 policy actions for access point operations can only
 be used in IAM identity-based policies, not in bucket policies or access point policies.
 Access points operations require the `Resource` element to be the access
 point ARN in the following example format. 



```
"Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point`"
```

The following IAM identity-based policy grants the
 `s3:GetAccessPointPolicy` permission to perform the [GetAccessPointPolicy](../API/API_control_GetAccessPointPolicy.md "../API/API_control_GetAccessPointPolicy.md") API operation on
 the S3 access point named
 ``example-access-point``.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "GrantPermissionToRetrieveTheAccessPointPolicyOfAccessPointExampleAccessPoint",
 "Effect": "Allow",
 "Action": [
 "s3:GetAccessPointPolicy"
 ],
 "Resource": "arn:aws:s3:*:`123456789012`:accesspoint/`example-access-point`"
 }
 ]
}`

```





When you use Access Points, to control access to bucket operations, see [Bucket operations in policies for access points for general purpose buckets](#bucket-operations-ap "#bucket-operations-ap"); to control access to object operations, see [Object operations in access point policies](#object-operations-ap "#object-operations-ap"). 
 For more information about how to configure access point policies, see [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").


### Access point for directory buckets operations


Access point for directory buckets operations are S3 API operations that operate on the
 `accesspoint` resource type. For example,
 `CreateAccessPoint`, `DeleteAccessPoint`, and
 `GetAccessPointPolicy`. S3 policy actions for access point operations can only
 be used in IAM identity-based policies, not in bucket policies or access point policies.
 Access points for directory buckets operations require the `Resource` element to be the access
 point ARN in the following example format. 



```
"Resource": "arn:aws:s3:`us-west-2`:`123456789012`:accesspoint/`example-access-point--usw2-az1--xa-s3`"
```

The following IAM identity-based policy grants the
 `s3express:GetAccessPointPolicy` permission to perform the [GetAccessPointPolicy](../API/API_control_GetAccessPointPolicy.md "../API/API_control_GetAccessPointPolicy.md") API operation on
 the access point named
 ``example-access-point--usw2-az1--xa-s3``.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "GrantPermissionToRetrieveTheAccessPointPolicyOfAccessPointExampleAccessPointUsw2Az1XaS3",
 "Effect": "Allow",
 "Action": [
 "s3express:CreateSession","s3express:GetAccessPointPolicy"
 ],
 "Resource": "arn:aws:s3:*:`111122223333`:accesspoint/`example-access-point`"
 }
 ]
}`

```





The following IAM identity-based policy grants the `s3express:CreateAccessPoint` permission to create an access points for directory buckets.



```

{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Grant CreateAccessPoint.",
            "Principal": "*",
            "Action": "s3express:CreateSession",
            "s3express:CreateAccessPoint""Effect": "Allow",
            "Resource": "*"
        }
    ]
}
            
```

The following IAM identity-based policy grants the `s3express:PutAccessPointScope` permission to create access point scope for access points for directory buckets.



```

{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Grant PutAccessPointScope",
            "Principal": "*",
            "Action": "s3express:CreateSession",
            "s3express:CreateAccessPoint",
            "S3Express:PutAccessPointScope""Effect": "Allow",
            "Resource": "*",
        }
    ]
}
            
```

When you use access points for directory buckets to control access to bucket operations, see [Bucket operations in policies for access points for directory buckets](#bucket-operations-ap-directory-buckets "#bucket-operations-ap-directory-buckets"); to control access to object operations, see [Object operations in policies for access points for directory buckets](#object-operations-ap-directory-buckets "#object-operations-ap-directory-buckets"). 
 For more information about how to configure access points for directory buckets policies, see [Configuring IAM policies for using access points for directory buckets](access-points-directory-buckets-policies.md "access-points-directory-buckets-policies.md").


### Object Lambda Access Point operations


With Amazon S3 Object Lambda, you can add your own code to Amazon S3 `GET`, `LIST`,
 and `HEAD` requests to modify and process data as it is returned to an
 application. You can make requests through an Object Lambda Access Point, which works the same as making requests through other access points. For more information, see [Transforming objects with S3 Object Lambda](transforming-objects.md "transforming-objects.md").


For more information about how to configure policies for Object Lambda Access Point operations, see [Configuring IAM policies for Object Lambda Access Points](olap-policies.md "olap-policies.md").


### Multi-Region Access Point operations


A Multi-Region Access Point provides a global endpoint that applications can use to fulfill requests from S3 buckets that are located in multiple AWS Region. You can use a Multi-Region Access Point to build multi-Region applications with the same architecture that's used in a single Region, and then run those applications anywhere in the world. For more information, see [Managing multi-Region traffic with Multi-Region Access Points](MultiRegionAccessPoints.md "MultiRegionAccessPoints.md").


For more information about how to configure policies for Multi-Region Access Point operations, see [Multi-Region Access Point policy examples](MultiRegionAccessPointPermissions.md#MultiRegionAccessPointPolicyExamples "MultiRegionAccessPointPermissions.md#MultiRegionAccessPointPolicyExamples").


### Batch job operations


(Batch Operations) job operations are S3 API operations that operate on the job resource type.
 For example, `DescribeJob` and `CreateJob`. S3 policy
 actions for job operations can only be used in IAM identity-based policies,
 not in bucket policies. Also, job operations require the `Resource`
 element in IAM identity-based policies to be the `job` ARN in the
 following example format. 



```
"Resource": "arn:aws:s3:*:`123456789012`:job/*"
```

The following IAM identity-based policy grants the `s3:DescribeJob`
 permission to perform the [DescribeJob](../API/API_DescribeJob.md "../API/API_DescribeJob.md") API operation
 on the S3 Batch Operations job named
 ``example-job``.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "AllowDescribingBatchOperationJob",
 "Effect": "Allow",
 "Action": [
 "s3:DescribeJob"
 ],
 "Resource": "arn:aws:s3:*:`111122223333`:job/`example-job`"
 }
 ]
}`

```





### S3 Storage Lens configuration operations


For more information about how to configure S3 Storage Lens configuration operations, see [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md "storage_lens_iam_permissions.md").


### Account operations


Account operations are S3 API operations that operate on the account level. For example, `GetPublicAccessBlock` (for account). Account isn't a resource type defined by Amazon S3.
 S3 policy actions for account operations can only be used in IAM identity-based policies, not in bucket policies. Also, account operations require the `Resource` element in IAM identity-based policies to be `"*"`. 


The following IAM identity-based policy grants the
 `s3:GetAccountPublicAccessBlock` permission to perform the
 account-level [GetPublicAccessBlock](../API/API_control_GetPublicAccessBlock.md "../API/API_control_GetPublicAccessBlock.md") API operation and retrieve the
 account-level Public Access Block settings.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[
 {
 "Sid":"AllowRetrievingTheAccountLevelPublicAccessBlockSettings",
 "Effect":"Allow",
 "Action":[
 "s3:GetAccountPublicAccessBlock" 
 ],
 "Resource":[
 "*"
 ]
 }
 ]
}`

```





### 
 Policy examples for Amazon S3



* To view examples of Amazon S3 identity-based policies, see [Identity-based policies for
 Amazon S3](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
* To view examples of Amazon S3 resource-based policies, see [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md") and [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").

## Policy
 resources for Amazon S3


**Supports policy resources:**
 
 
 Yes


Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform 
 **actions** on what **resources**, and under what **conditions**.


The `Resource` JSON policy element specifies the object or objects to which the action applies. Statements must include either a
 `Resource` or a `NotResource` element. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html"). You can do this for actions that support a 
 specific resource type, known as *resource-level permissions*.


For actions that don't support resource-level permissions, such as listing operations,
 use a wildcard (\*) to indicate that the statement applies to all resources.



```
"Resource": "*"
```

Some Amazon S3 API actions support multiple resources. For example,
 `s3:GetObject` accesses
 ``example-resource-1`` and
 ``example-resource-2``, so a principal must
 have permissions to access both resources. To specify multiple resources in a single
 statement, separate the ARNs with commas, as shown in the following example. 



```
"Resource": [
      "`example-resource-1`",
      "`example-resource-2`"
```

Resources in Amazon S3 are buckets, objects, access points, or jobs. In a policy, use the
 Amazon Resource Name (ARN) of the bucket, object, access point, or job to identify the
 resource.


To see a complete list of Amazon S3 resource types and their ARNs, see [Resources defined by Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies")
 in the *Service Authorization Reference*. To learn with which actions you can
 specify the ARN of each resource, see [Actions defined by Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-actions-as-permissions "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-actions-as-permissions").


For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").


### Wildcard characters in resource ARNs


You can use wildcard characters as part of the resource ARN. You can use the
 wildcard characters (`*` and `?`) within any ARN segment (the
 parts separated by colons). An asterisk (`*`) represents any combination
 of zero or more characters, and a question mark (`?`) represents any
 single character. You can use multiple `*` or `?` characters in
 each segment. However, a wildcard character can't span segments. 



* The following ARN uses the `*` wildcard character in the
 `relative-ID` part of the ARN to identify all objects in the
 ``amzn-s3-demo-bucket`` bucket.



```
arn:aws:s3:::`amzn-s3-demo-bucket`/*
```
* The following ARN uses `*` to indicate all S3 buckets and
 objects.



```
arn:aws:s3:::*
```
* The following ARN uses both of the wildcard characters, `*` and
 `?`, in the `relative-ID` part. This ARN identifies
 all objects in buckets such as
 ``amzn-s3-demo-example1bucket``,
 ``amzn-s3-demo-example2bucket``,
 ``amzn-s3-demo-example3bucket``, and
 so on.



```
arn:aws:s3:::`amzn-s3-demo-example`?`bucket`/*
```

### Policy variables for resource ARNs


You can use policy variables in Amazon S3 ARNs. At policy-evaluation time, these
 predefined variables are replaced by their corresponding values. Suppose that you
 organize your bucket as a collection of folders, with one folder for each of your
 users. The folder name is the same as the username. To grant users permission to
 their folders, you can specify a policy variable in the resource ARN:



```
arn:aws:s3:::`bucket_name`/`developers`/${aws:username}/
```

At runtime, when the policy is evaluated, the variable
 `${aws:username}` in the resource ARN is substituted with the username
 of the person who is making the request. 




### 
 Policy examples for Amazon S3



* To view examples of Amazon S3 identity-based policies, see [Identity-based policies for
 Amazon S3](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
* To view examples of Amazon S3 resource-based policies, see [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md") and [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").

## Policy
 condition keys for Amazon S3


**Supports service-specific policy condition keys:**
 
 
 Yes


Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform 
 **actions** on what **resources**, and under what **conditions**.


The `Condition` element (or `Condition`
*block*) lets you specify conditions in which a
 statement is in effect. The `Condition` element is optional. You can create
 conditional expressions that use [condition
 operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html"), such as equals or less than, to match the condition in the
 policy with values in the request. 


If you specify multiple `Condition` elements in a statement, or
 multiple keys in a single `Condition` element, AWS evaluates them using
 a logical `AND` operation. If you specify multiple values for a single
 condition key, AWS evaluates the condition using a logical `OR`
 operation. All of the conditions must be met before the statement's permissions are
 granted.


 You can also use placeholder variables when you specify conditions. For example,
 you can grant an IAM user permission to access a resource only if it is tagged with
 their IAM user name. For more information, see [IAM policy elements:
 variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html") in the *IAM User Guide*. 


AWS supports global condition keys and service-specific condition keys. To see all AWS global
 condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html") in the
 *IAM User Guide*.


Each Amazon S3 condition key maps to the same name request header allowed by the API
 on which the condition can be set. Amazon S3‐specific condition keys dictate the
 behavior of the same name request headers. For example, the condition key
 `s3:VersionId` used to grant conditional permission for the `s3:GetObjectVersion` permission defines behavior of the
 `versionId` query parameter that you set in a GET Object request.


To see a list of Amazon S3 condition keys, see [Condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-policy-keys "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-policy-keys") in the
 *Service Authorization Reference*. To learn with which actions and resources you
 can use a condition key, see [Actions defined by Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-actions-as-permissions "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-actions-as-permissions").


### Example: Restricting object uploads to
 objects with a specific storage class


Suppose that Account A, represented by account ID
 ``123456789012``, owns a bucket. The
 Account A administrator wants to restrict
 ``Dave``, a user in Account A, so that
 ``Dave`` can upload objects to the bucket
 only if the object is stored in the `STANDARD_IA` storage class. To
 restrict object uploads to a specific storage class, the Account A administrator can
 use the `s3:x-amz-storage-class` condition key, as shown in the following
 example bucket policy. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "statement1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/`Dave`"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-storage-class": [
 "STANDARD_IA"
 ]
 }
 }
 }
 ]
 }`

```





In the example, the `Condition` block specifies the
 `StringEquals` condition that is applied to the specified key-value pair,
 `"s3:x-amz-acl":["public-read"]`. There is a set of predefined keys that
 you can use in expressing a condition. The example uses the `s3:x-amz-acl`
 condition key. This condition requires the user to include the `x-amz-acl`
 header with value `public-read` in every `PutObject`
 request.


### 
 Policy examples for Amazon S3



* To view examples of Amazon S3 identity-based policies, see [Identity-based policies for
 Amazon S3](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
* To view examples of Amazon S3 resource-based policies, see [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md") and [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").

## ACLs in Amazon S3


**Supports ACLs:** 
 
 
 Yes


In Amazon S3, access control lists (ACLs) control which AWS accounts have permissions to access a resource. 
 ACLs are similar to resource-based policies, although they do not use the JSON policy document format.


###### Important

A majority of modern use cases in Amazon S3 no longer require the use of ACLs. 


For information about using ACLs to control access in Amazon S3, see [Managing access with ACLs](acls.md "acls.md").


## ABAC with Amazon S3


**Supports ABAC (tags in policies):**
 
 
 Partial


Attribute-based access control (ABAC) is an authorization strategy that defines permissions
 based on attributes. In AWS, these attributes are called *tags*. You can attach tags to IAM entities (users
 or roles) and to many AWS resources. Tagging entities and resources is the first step of ABAC. Then you 
 design ABAC policies to allow operations when the principal's tag matches the tag on the resource that they 
 are trying to access.


ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.


To control access based on tags, you provide tag information in the [condition
 element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html") of a policy using the
 `aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
 `aws:TagKeys` condition keys.


If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. 
 If a service supports all three condition keys for only some resource types, then the value is **Partial**.


For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html") in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see 
 [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html") in the *IAM User Guide*.


For information about resources that support ABAC in Amazon S3, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").


To view example identity-based policies for limiting access to S3 Batch Operations jobs based on
 tags, see [Controlling permissions for Batch Operations using job
 tags](batch-ops-job-tags-examples.md "batch-ops-job-tags-examples.md").


### ABAC and object tags


In ABAC policies, objects use `s3:` tags instead of `aws:`
 tags. To control access to objects based on object tags, you provide tag information
 in the [Condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html") of a policy using the following
 tags:



* `s3:ExistingObjectTag/`tag-key``
* `s3:RequestObjectTagKeys`
* `s3:RequestObjectTag/`tag-key``

For information about using object tags to control access, including example permission
 policies, see [Tagging and access control policies](tagging-and-policies.md "tagging-and-policies.md").


## Using temporary
 credentials with Amazon S3


**Supports temporary credentials:**
 
 
 Yes


Some AWS services don't work when you sign in using temporary credentials. For additional 
 information, including which AWS services work with temporary credentials, see [AWS services
 that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html") in the *IAM User Guide*.


You are using temporary credentials if you sign in to the AWS Management Console using any method
 except a user name and password. For example, when you access AWS using your
 company's single sign-on (SSO) link, that process automatically creates temporary credentials.
 You also automatically create temporary credentials when you sign in to the console as a user and
 then switch roles. For more information about switching roles, see [Switch from a user to an IAM role
 (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html") in the *IAM User Guide*.


You can manually create temporary credentials using the AWS CLI or AWS API. You can
 then use those temporary credentials to access AWS. AWS recommends that you
 dynamically generate temporary credentials instead of using long-term access keys. For
 more information, see [Temporary
 security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html").


## Forward access
 sessions for Amazon S3


**Supports forward access sessions (FAS):** 
 
 
 Yes




 When you use an IAM user or role to perform actions in AWS, you are considered a principal. When you use some services, you might perform an action that then initiates
 another action in a different service. FAS uses the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services.
 FAS requests are only made when a service receives a request that requires interactions with other AWS services or resources to complete. In this case, you must have permissions to
 perform both actions. For policy details
 when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html").
 



* FAS is used by Amazon S3 to make calls to AWS KMS to decrypt an object when SSE-KMS was used to encrypt it. For more information, see [Using server-side encryption with AWS KMS keys
 (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").
* S3 Access Grants also uses FAS. After you create an access grant to your S3 data for a particular identity, the grantee requests a temporary credential from S3 Access Grants. S3 Access Grants obtains a temporary credential for the requester from AWS STS and vends the credential to the requester. For more information, see [Request access to Amazon S3 data through
 S3 Access Grants](access-grants-credentials.md "access-grants-credentials.md").

## Service roles for
 Amazon S3


**Supports service roles:** 
 
 
 Yes




 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html") that a service assumes to perform 
 actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For 
 more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html") in the *IAM User Guide*.
 


###### Warning

Changing the permissions for a service role might break Amazon S3 functionality.
 Edit service roles only when Amazon S3 provides guidance to do so.


## Service-linked
 roles for Amazon S3


**Supports service-linked roles:**
 
 
 Partial




 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. 
 Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, 
 but not edit the permissions for service-linked roles. 
 


Amazon S3 supports service-linked roles for Amazon S3 Storage Lens. 
 For details about creating or managing Amazon S3 service-linked roles, see [Using service-linked roles for
 Amazon S3 Storage Lens](using-service-linked-roles.md "using-service-linked-roles.md").


**Amazon S3 Service as a Principal**




| Service name in the policy | S3 feature | More information |
| --- | --- | --- |
| `s3.amazonaws.com` | S3 Replication | [Setting up live replication overview](replication-how-setup.md "replication-how-setup.md") |
| `s3.amazonaws.com` | S3 event notifications | [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md") |
| `s3.amazonaws.com` | S3 Inventory | [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md") |
| `access-grants.s3.amazonaws.com` | S3 Access Grants | [Register a location](access-grants-location-register.md "access-grants-location-register.md") |
| `batchoperations.s3.amazonaws.com` | S3 Batch Operations | [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md") |
| `logging.s3.amazonaws.com` | S3 Server Access Logging | [Enabling Amazon S3 server access logging](enable-server-access-logging.md "enable-server-access-logging.md") |
| `storage-lens.s3.amazonaws.com` | S3 Storage Lens | [Viewing Amazon S3 Storage Lens metrics using a data
 export](storage_lens_view_metrics_export.md "storage_lens_view_metrics_export.md") |
