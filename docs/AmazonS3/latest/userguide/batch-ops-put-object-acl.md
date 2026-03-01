# Replace access control list (ACL)

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
The **Replace access control list (ACL)** operation replaces the access control
lists (ACLs) for every object that's listed in the manifest. By using ACLs, you can define who
can access an object and what actions they can perform.

###### Note

A majority of modern use cases in Amazon S3 no longer require the use of ACLs. We recommend that
you keep ACLs disabled, except in circumstances where you need to control access for
each object individually. With ACLs disabled, you can use policies to control access to all
objects in your bucket, regardless of who uploaded the objects to your bucket. For more
information, see [Controlling ownership of objects and disabling ACLs for your bucket](about-object-ownership.md "about-object-ownership.md").

S3 Batch Operations support custom ACLs that you define and the canned ACLs that Amazon S3 provides
with a predefined set of access permissions.

If the objects in your manifest are in a versioned bucket, you can apply the ACLs to
specific versions of every object. To do so, specify a version ID for every object in the
manifest. If you don't include a version ID for any object, S3 Batch Operations applies the ACL to
the latest version of the object.

For more information about ACLs in Amazon S3, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md").

###### S3 Block Public Access

If you want to limit public access to all objects in a bucket, we recommend using Amazon S3
Block Public Access instead of using S3 Batch Operations to apply ACLs. Block Public Access can
limit public access on a per-bucket or account-wide basis with a single, simple operation that
takes effect quickly. This behavior makes Amazon S3 Block Public Access a better choice when your
goal is to control public access to all objects in a bucket or account. Use S3 Batch Operations
only when you need to apply a customized ACL to every object in the manifest. For more
information about S3 Block Public Access, see [Blocking public access to your Amazon S3 storage](access-control-block-public-access.md "access-control-block-public-access.md").

###### S3 Object Ownership

If the objects in the manifest are in a bucket that uses the **Bucket owner
enforced** setting for Object Ownership, the **Replace access control list
(ACL)** operation can only specify object ACLs that grant full control to the
bucket owner. In this case, the **Replace access control list (ACL)**
operation can't grant object ACL permissions to other AWS accounts or groups. For more
information, see [Controlling ownership of objects and disabling ACLs for your bucket](about-object-ownership.md "about-object-ownership.md").

## Restrictions and limitations

When you're using Batch Operations to replace ACLs, the following restrictions and limitations
apply:

- The AWS Identity and Access Management (IAM) role that you specify to run the **Replace access
  control list (ACL)** job must have permissions to perform the underlying Amazon S3
  `PutObjectAcl` operation. For more information about the permissions
  required, see [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md") in the
  _Amazon Simple Storage Service API Reference_.
- S3 Batch Operations uses the Amazon S3 `PutObjectAcl` operation to apply the
  specified ACL to every object in the manifest. Therefore, all restrictions and limitations
  that apply to the underlying `PutObjectAcl` operation also apply to
  S3 Batch Operations **Replace access control list (ACL)** jobs.
- A single replace access control list job can support a manifest with up to 20 billion objects.
