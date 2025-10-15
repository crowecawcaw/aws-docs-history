# Access control list (ACL) overview

Amazon S3 access control lists (ACLs) enable you to manage access to buckets and objects. Each
 bucket and object has an ACL attached to it as a subresource. It defines which AWS accounts or groups are granted access and the type of access. When a request is received
 against a resource, Amazon S3 checks the corresponding ACL to verify that the requester has
 the necessary access permissions. 

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to both control ownership of the objects that are 
 uploaded to your bucket and to disable or enable ACLs. By default, Object Ownership is set to the Bucket owner enforced setting, 
 and all ACLs are disabled. When ACLs are disabled, the bucket owner owns all the objects in the bucket and manages access to them 
 exclusively by using access-management policies.

 A majority of modern use cases in Amazon S3 no longer require the use of ACLs. We recommend that you keep ACLs disabled, except 
 in circumstances where you need to control access for each object individually. With ACLs disabled, you can use policies 
 to control access to all objects in your bucket, regardless of who uploaded the objects to your bucket. 
 For more information, see [Controlling ownership of objects and disabling ACLs
 for your bucket](about-object-ownership.md "about-object-ownership.md").

###### Important

If your general purpose bucket uses the Bucket owner enforced setting for S3 Object Ownership, you must use policies to 
 grant access to your general purpose bucket and the objects in it. With the Bucket owner enforced setting enabled, requests to set 
 access control lists (ACLs) or update ACLs fail and return the `AccessControlListNotSupported` error code. 
 Requests to read ACLs are still supported.

When you create a bucket or an object, Amazon S3 creates a default ACL that grants the resource
 owner full control over the resource. This is shown in the following sample bucket ACL
 (the default object ACL has the same structure):


```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>*** Owner-Canonical-User-ID ***</ID>
    <DisplayName>owner-display-name</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xsi:type="Canonical User">
        <ID>*** Owner-Canonical-User-ID ***</ID>
        <DisplayName>display-name</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy> 
```
The sample ACL includes an `Owner` element that identifies the owner by the
 AWS account's canonical user ID. For instructions on finding your canonical user ID,
 see [Finding an AWS account canonical user
 ID](#finding-canonical-id "#finding-canonical-id"). The
 `Grant` element identifies the grantee (either an AWS account or a
 predefined group) and the permission granted. This default ACL has one
 `Grant` element for the owner. You grant permissions by adding
 `Grant` elements, with each grant identifying the grantee and the
 permission. 

###### Note

An ACL can have up to 100 grants.

###### Topics

* [Who is a grantee?](#specifying-grantee "#specifying-grantee")
* [What permissions can I grant?](#permissions "#permissions")
* [aclRequired values for common Amazon S3
 requests](#aclrequired-s3 "#aclrequired-s3")
* [Sample ACL](#sample-acl "#sample-acl")
* [Canned ACL](#canned-acl "#canned-acl")
## Who is a grantee?


###### Important

End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue support for creating new Email Grantee Access Control Lists (ACL). 
 Email Grantee ACLs created prior to this date will continue to work and remain accessible through the AWS Management Console, Command Line Interface (CLI), SDKs, 
 and REST API. However, you will no longer be able to create new Email Grantee ACLs.

Between July 15, 2025 and October 1, 2025, you will begin to see an increasing rate of `HTTP 405` errors for requests to Amazon S3 when attempting to create 
 new Email Grantee ACLs.

This change affects the following AWS Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), 
 Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).


A grantee can be an AWS account or one of the predefined Amazon S3 groups. You grant
 permission to an AWS account using the email address or the canonical user ID.
 However, if you provide an email address in your grant request, Amazon S3 finds the
 canonical user ID for that account and adds it to the ACL. The resulting ACLs always
 contain the canonical user ID for the AWS account, not the email address of the
 AWS account.


When you grant access rights, you specify each grantee as a
 ``type`="`value`"`
 pair, where ``type`` is one of the
 following:



* `id` – If the value specified is the canonical user ID of an AWS account
* `uri` – If you are granting permissions to a predefined group
* `emailAddress` – If the value specified is the email address of an
 AWS account

###### Important

Using email addresses to specify a grantee is only supported in the following AWS
 Regions:


* US East (N. Virginia)
* US West (N. California)
* US West (Oregon)
* Asia Pacific (Singapore)
* Asia Pacific (Sydney)
* Asia Pacific (Tokyo)
* Europe (Ireland)
* South America (São Paulo)
For a list of all the Amazon S3 supported regions and endpoints, 
 see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the
 *Amazon Web Services General Reference*.


###### Example: Email address

For example, the following `x-amz-grant-read` header grants
 the AWS accounts identified by email addresses permissions to read object
 data and its metadata:


```
x-amz-grant-read: emailAddress="xyz@example.com", emailAddress="abc@example.com"
```

###### Warning

When you grant other AWS accounts access to your resources, be aware that the AWS accounts can delegate their permissions to users under their
 accounts. This is known as *cross-account
 access*. For information about using cross-account access,
 see [Creating a Role to Delegate Permissions to an IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html")
 in the *IAM User Guide*. 


### Finding an AWS account canonical user
 ID


The canonical user ID is associated with your AWS account. This ID is a long
 string of characters, such as:


`79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be`


For information about how to find the canonical user ID for your account, see
 [Find the canonical user ID for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindCanonicalId "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindCanonicalId") in the *AWS Account Management Reference Guide*.


You can also look up the canonical user ID of an AWS account by reading the
 ACL of a bucket or an object to which the AWS account has access permissions.
 When an individual AWS account is granted permissions by a grant request, a
 grant entry is added to the ACL with the account's canonical user ID. 


###### Note

If you make your bucket public (not recommended), any unauthenticated user
 can upload objects to the bucket. These anonymous users don't have an
 AWS account. When an anonymous user uploads an object to your bucket, Amazon S3
 adds a special canonical user ID
 (`65a011a29cdf8ec533ec3d1ccaae921c`) as the object owner in
 the ACL. For more information, see [Amazon S3 bucket and object ownership](access-policy-language-overview.md#about-resource-owner "access-policy-language-overview.md#about-resource-owner").


### Amazon S3 predefined
 groups


Amazon S3 has a set of predefined groups. When granting account access to a group, you specify
 one of the Amazon S3 URIs instead of a canonical user ID. Amazon S3 provides the following
 predefined groups:



* **Authenticated Users
 group** – Represented by
 `http://acs.amazonaws.com/groups/global/AuthenticatedUsers`.


This group represents all AWS accounts. **Access permission to this
 group allows any AWS account to access the resource.** However, all
 requests must be signed (authenticated).


###### Warning

When you grant access to the **Authenticated Users
 group**, any AWS authenticated user in the world can
 access your resource.
* **All Users group** –
 Represented by
 `http://acs.amazonaws.com/groups/global/AllUsers`.


**Access permission to this group allows anyone in the world access
 to the resource.** The requests can be signed
 (authenticated) or unsigned (anonymous). Unsigned requests omit the
 Authentication header in the request.


###### Warning

We highly recommend that you never grant the **All Users
 group**
`WRITE`, `WRITE_ACP`, or
 `FULL_CONTROL` permissions. For example, although
 `WRITE` permissions deny non-owners the ability to
 overwrite or delete existing objects, `WRITE` permissions
 still allow anyone to store objects in your bucket, for which you
 are billed. For more details about these permissions, see the
 following section [What permissions can I grant?](#permissions "#permissions").
* **Log Delivery group**
 – Represented by
 `http://acs.amazonaws.com/groups/s3/LogDelivery`.


`WRITE` permission on a bucket enables this group to write server access logs
 (see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md")) to the
 bucket.

###### Note

When using ACLs, a grantee can be an AWS account or one of the predefined Amazon S3 groups.
 However, the grantee cannot be an IAM user. For more information about AWS
 users and permissions within IAM, see [Using
 AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/ "https://docs.aws.amazon.com/IAM/latest/UserGuide/").


## What permissions can I grant?


The following table lists the set of permissions that Amazon S3 supports in an ACL. The set of
 ACL permissions is the same for an object ACL and a bucket ACL. However, depending
 on the context (bucket ACL or object ACL), these ACL permissions grant permissions
 for specific buckets or object operations. The table lists the permissions and
 describes what they mean in the context of objects and buckets. 


For more information about ACL permissions in the Amazon S3 console, see [Configuring ACLs](managing-acls.md "managing-acls.md").




| Permission | When granted on a bucket | When granted on an object |
| --- | --- | --- |
| `READ` | Allows grantee to list the objects in the bucket | Allows grantee to read the object data and its metadata |
| `WRITE` | Allows grantee to create new objects in the bucket. For the bucket and object owners
 of existing objects, also allows deletions and overwrites of those
 objects | Not applicable |
| `READ_ACP` | Allows grantee to read the bucket ACL | Allows grantee to read the object ACL |
| `WRITE_ACP` | Allows grantee to write the ACL for the applicable bucket | Allows grantee to write the ACL for the applicable object |
| `FULL_CONTROL` | Allows grantee the `READ`, `WRITE`, `READ_ACP`, and
 `WRITE_ACP` permissions on the bucket | Allows grantee the `READ`, `READ_ACP`, and
 `WRITE_ACP` permissions on the object |


###### Warning

Use caution when granting access permissions to your S3 buckets and objects. For example,
 granting `WRITE` access to a bucket allows the grantee to create
 objects in the bucket. We highly recommend that you read through the entire
 [Access control list (ACL) overview](acl-overview.md "acl-overview.md") section before
 granting permissions.


### Mapping of ACL permissions and access policy
 permissions


As shown in the preceding table, an ACL allows only a finite set of permissions, compared
 to the number of permissions that you can set in an access policy (see [Policy actions
 for Amazon S3](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions")).
 Each of these permissions allows one or more Amazon S3 operations.


The following table shows how each ACL permission maps to the corresponding access policy
 permissions. As you can see, access policy allows more permissions than an ACL
 does. You use ACLs primarily to grant basic read/write permissions, similar to
 file system permissions. For more information about when to use an ACL, see
 [Identity and Access Management for Amazon S3](security-iam.md "security-iam.md").


For more information about ACL permissions in the Amazon S3 console, see [Configuring ACLs](managing-acls.md "managing-acls.md").




| ACL permission | Corresponding access policy permissions when the ACL
 permission is granted on a bucket  | Corresponding access policy permissions when the ACL
 permission is granted on an object |
| --- | --- | --- |
| `READ` | `s3:ListBucket`,
 `s3:ListBucketVersions`, and
 `s3:ListBucketMultipartUploads` | `s3:GetObject` and `s3:GetObjectVersion` |
| `WRITE` | 
`s3:PutObject`
Bucket owner can create, overwrite, and delete any object in the bucket, and object
 owner has `FULL_CONTROL` over their object.
In addition, when the grantee is the bucket owner, granting `WRITE` permission
 in a bucket ACL allows the `s3:DeleteObjectVersion` action to
 be performed on any version in that bucket.  | Not applicable |
| `READ_ACP` | `s3:GetBucketAcl` | `s3:GetObjectAcl` and
 `s3:GetObjectVersionAcl` |
| `WRITE_ACP` | `s3:PutBucketAcl` | `s3:PutObjectAcl` and
 `s3:PutObjectVersionAcl` |
| `FULL_CONTROL` | Equivalent to granting `READ`, `WRITE`, `READ_ACP`,
 and `WRITE_ACP` ACL permissions. Accordingly, this
 ACL permission maps to a combination of corresponding access
 policy permissions. | Equivalent to granting `READ`, `READ_ACP`, and
 `WRITE_ACP` ACL permissions. Accordingly, this
 ACL permission maps to a combination of corresponding access
 policy permissions. |


### Condition keys


When you grant access policy permissions, you can use condition keys to constrain the
 value for the ACL on an object using a bucket policy. The following context keys
 correspond to ACLs. You can use these context keys to mandate the use of a
 specific ACL in a request:



* `s3:x-amz-grant-read` ‐ Require read access.
* `s3:x-amz-grant-write` ‐ Require write access.
* `s3:x-amz-grant-read-acp` ‐ Require read access to the bucket ACL.
* `s3:x-amz-grant-write-acp` ‐ Require write access to the bucket ACL.
* `s3:x-amz-grant-full-control` ‐ Require full control.
* `s3:x-amz-acl` ‐ Require a [Canned ACL](#canned-acl "#canned-acl").

For example policies that involve ACL-specific headers, see [Granting s3:PutObject permission
 with a condition requiring the bucket owner to get full control](example-bucket-policies-condition-keys.md#grant-putobject-conditionally-1 "example-bucket-policies-condition-keys.md#grant-putobject-conditionally-1"). For a complete list of
 Amazon S3 specific condition keys, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html") in the *Service Authorization 
 Reference*.


For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").


## `aclRequired` values for common Amazon S3
 requests


To identify Amazon S3 requests that required ACLs for authorization, you can use the
 `aclRequired` value in Amazon S3 server access logs or AWS CloudTrail. The
 `aclRequired` value that appears in CloudTrail or Amazon S3 server access logs
 depends on which operations were called and certain information about the requester,
 object owner, and bucket owner. If no ACLs were required, or if you are setting the
 `bucket-owner-full-control` canned ACL, or if the requests are
 allowed by your bucket policy, the `aclRequired` value string is
 "`-`" in Amazon S3 server access logs and is absent in CloudTrail.


The following tables list the expected `aclRequired` values in CloudTrail or
 Amazon S3 server access logs for the various Amazon S3 API operations. You can use this
 information to understand which Amazon S3 operations depend on ACLs for authorization. In
 the following tables, A, B, and C represent the different accounts associated with
 the requester, object owner, and bucket owner. Entries with an asterisk (\*) indicate
 any of accounts A, B, or C. 


###### Note

`PutObject` operations in the following table, unless specified
 otherwise, indicate requests that do not set an ACL, unless the ACL is a
 `bucket-owner-full-control` ACL. A null value for
 `aclRequired` indicates that `aclRequired` is absent
 in AWS CloudTrail logs.



 The following table shows the `aclRequired` values for CloudTrail.
 




| Operation name | Requester | Object owner | Bucket owner  | Bucket policy grants access | `aclRequired` value | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| `GetObject` | A | A | A | Yes or No | null | Same-account access |
| `GetObject` | A | B | A | Yes or No | null | Same-account access with bucket owner enforced |
| `GetObject` | A | A | B | Yes | null | Cross-account access granted by bucket policy |
| `GetObject` | A | A | B | No | Yes | Cross-account access relies on ACL |
| `GetObject` | A | A | B | Yes | null | Cross-account access granted by bucket policy |
| `GetObject` | A | B | B | No | Yes | Cross-account access relies on ACL |
| `GetObject` | A | B | C | Yes | null | Cross-account access granted by bucket policy |
| `GetObject` | A | B | C | No | Yes | Cross-account access relies on ACL |
| `PutObject` | A | Not applicable | A | Yes or No | null | Same-account access |
| `PutObject` | A | Not applicable | B | Yes | null | Cross-account access granted by bucket policy |
| `PutObject` | A | Not applicable | B | No | Yes | Cross-account access relies on ACL |
| `PutObject` with an ACL (except for
 `bucket-owner-full-control`) | \* | Not applicable | \* | Yes or No | Yes | Request grants ACL |
| `ListObjects` | A | Not applicable | A | Yes or No | null | Same-account access |
| `ListObjects` | A | Not applicable | B | Yes | null | Cross-account access granted by bucket policy |
| `ListObjects` | A | Not applicable | B | No | Yes | Cross-account access relies on ACL |
| `DeleteObject` | A | Not applicable | A | Yes or No | null | Same-account access |
| `DeleteObject` | A | Not applicable | B | Yes | null | Cross-account access granted by bucket policy |
| `DeleteObject` | A | Not applicable | B | No | Yes | Cross-account access relies on ACL |
| `PutObjectAcl` | \* | \* | \* | Yes or No | Yes | Request grants ACL |
| `PutBucketAcl` | \* | Not applicable | \* | Yes or No | Yes | Request grants ACL |


 


###### Note

`REST.PUT.OBJECT` operations in the following table, unless
 specified otherwise, indicate requests that do not set an ACL, unless the ACL is
 a `bucket-owner-full-control` ACL. An `aclRequired` value
 string of "`-`" indicates a null value in Amazon S3 server access
 logs.



 The following table shows the `aclRequired` values for Amazon S3 server access logs.
 




| Operation name | Requester | Object owner | Bucket owner  | Bucket policy grants access | `aclRequired` value | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| `REST.GET.OBJECT` | A | A | A | Yes or No | - | Same-account access |
| `REST.GET.OBJECT` | A | B | A | Yes or No | - | Same-account access with bucket owner enforced |
| `REST.GET.OBJECT` | A | A | B | Yes | - | Cross-account access granted by bucket policy |
| `REST.GET.OBJECT` | A | A | B | No | Yes | Cross-account access relies on ACL |
| `REST.GET.OBJECT` | A | B | B | Yes | - | Cross-account access granted by bucket policy |
| `REST.GET.OBJECT` | A | B | B | No | Yes | Cross-account access relies on ACL |
| `REST.GET.OBJECT` | A | B | C | Yes | - | Cross-account access granted by bucket policy |
| `REST.GET.OBJECT` | A | B | C | No | Yes | Cross-account access relies on ACL |
| `REST.PUT.OBJECT` | A | Not applicable | A | Yes or No | - | Same-account access |
| `REST.PUT.OBJECT` | A | Not applicable | B | Yes | - | Cross-account access granted by bucket policy |
| `REST.PUT.OBJECT` | A | Not applicable | B | No | Yes | Cross-account access relies on ACL |
| `REST.PUT.OBJECT` with an ACL (except for
 `bucket-owner-full-control`) | \* | Not applicable | \* | Yes or No | Yes | Request grants ACL |
| `REST.GET.BUCKET` | A | Not applicable | A | Yes or No | - | Same-account access |
| `REST.GET.BUCKET` | A | Not applicable | B | Yes | - | Cross-account access granted by bucket policy |
| `REST.GET.BUCKET` | A | Not applicable | B | No | Yes | Cross-account access relies on ACL |
| `REST.DELETE.OBJECT` | A | Not applicable | A | Yes or No | - | Same-account access |
| `REST.DELETE.OBJECT` | A | Not applicable | B | Yes | - | Cross-account access granted by bucket policy |
| `REST.DELETE.OBJECT` | A | Not applicable | B | No | Yes | Cross-account access relies on ACL |
| `REST.PUT.ACL` | \* | \* | \* | Yes or No | Yes | Request grants ACL |


## Sample ACL


The following sample ACL on a bucket identifies the resource owner and a set of
 grants. The format is the XML representation of an ACL in the Amazon S3 REST API. The
 bucket owner has `FULL_CONTROL` of the resource. In addition, the ACL
 shows how permissions are granted on a resource to two AWS accounts, identified by
 canonical user ID, and two of the predefined Amazon S3 groups discussed in the preceding
 section.



```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>Owner-canonical-user-ID</ID>
    <DisplayName>display-name</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>Owner-canonical-user-ID</ID>
        <DisplayName>display-name</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
    
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>user1-canonical-user-ID</ID>
        <DisplayName>display-name</DisplayName>
      </Grantee>
      <Permission>WRITE</Permission>
    </Grant>

    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
        <ID>user2-canonical-user-ID</ID>
        <DisplayName>display-name</DisplayName>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>

    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
        <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI> 
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
        <URI>http://acs.amazonaws.com/groups/s3/LogDelivery</URI>
      </Grantee>
      <Permission>WRITE</Permission>
    </Grant>

  </AccessControlList>
</AccessControlPolicy>
```

## Canned ACL


Amazon S3 supports a set of predefined grants, known as *canned ACLs*. Each
 canned ACL has a predefined set of grantees and permissions. The following table
 lists the set of canned ACLs and the associated predefined grants. 




| Canned ACL | Applies to | Permissions added to ACL |
| --- | --- | --- |
| `private` | Bucket and object | Owner gets `FULL_CONTROL`. No one else has access
 rights (default). |
| `public-read` | Bucket and object | Owner gets `FULL_CONTROL`. The `AllUsers` group (see [Who is a grantee?](#specifying-grantee "#specifying-grantee")) gets `READ` access.  |
| `public-read-write` | Bucket and object | Owner gets `FULL_CONTROL`. The
 `AllUsers` group gets `READ` and
 `WRITE` access. Granting this on a bucket is
 generally not recommended. |
| `aws-exec-read` | Bucket and object | Owner gets `FULL_CONTROL`. Amazon EC2 gets `READ` 
 access to `GET` an Amazon Machine Image (AMI) bundle from Amazon S3. |
| `authenticated-read` | Bucket and object | Owner gets `FULL_CONTROL`. The
 `AuthenticatedUsers` group gets `READ`
 access. |
| `bucket-owner-read` | Object | Object owner gets `FULL_CONTROL`. Bucket owner
 gets `READ` access. If you specify this canned ACL
 when creating a bucket, Amazon S3 ignores it. |
| `bucket-owner-full-control` | Object  | Both the object owner and the bucket owner get
 `FULL_CONTROL` over the object. If you specify
 this canned ACL when creating a bucket, Amazon S3 ignores it. |
| `log-delivery-write` | Bucket  | The `LogDelivery` group gets `WRITE` and `READ_ACP`
 permissions on the bucket. For more information about logs, see
 ([Logging requests with server access logging](ServerLogs.md "ServerLogs.md")). |


###### Note

You can specify only one of these canned ACLs in your request.


You specify a canned ACL in your request by using the `x-amz-acl` request
 header. When Amazon S3 receives a request with a canned ACL in the request, it adds the
 predefined grants to the ACL of the resource.
