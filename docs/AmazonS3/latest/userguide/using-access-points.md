# Using Amazon S3 access points for general purpose buckets

The following examples demonstrate how to use access points for general purpose buckets with compatible operations in Amazon S3.

###### Note

S3 automatically generate access point aliases for all access points and these aliases can be used
 anywhere a bucket name is used to perform object-level operations. For more
 information, see [Access point aliases](access-points-naming.md#access-points-alias "access-points-naming.md#access-points-alias").

You can only use access points for general purpose buckets to perform operations on objects. You can't use access points
 to perform other Amazon S3 operations, such as modifying or deleting buckets. For a
 complete list of S3 operations that support access points, see [Access point compatibility](access-points-service-api-support.md "access-points-service-api-support.md").

###### Topics

* [List objects through an access point for a general purpose bucket](list-object-ap.md "list-object-ap.md")
* [Download an object through an access point for a general purpose bucket](get-object-ap.md "get-object-ap.md")
* [Configure access control lists (ACLs) through an access point for a general purpose bucket](put-acl-permissions-ap.md "put-acl-permissions-ap.md")
* [Upload an object through an access point for a general purpose bucket](put-object-ap.md "put-object-ap.md")
* [Add a tag-set through an access point for a general purpose bucket](add-tag-set-ap.md "add-tag-set-ap.md")
* [Delete an object through an access point for a general purpose bucket](delete-object-ap.md "delete-object-ap.md")
