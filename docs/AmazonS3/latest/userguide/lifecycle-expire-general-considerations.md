# Expiring objects

You can add transition actions to an S3 Lifecycle configuration to tell Amazon S3 to delete
 objects at the end of their lifetime. When an object reaches the end of its lifetime
 based on its lifecycle configuration, Amazon S3 takes an `Expiration` action based
 on which [S3 Versioning](Versioning.md "Versioning.md") state the bucket is in:


* **Nonversioned bucket** – Amazon S3 queues the
 object for removal and removes it asynchronously, permanently removing the
 object.
* **Versioning-enabled bucket** – If the
 current object version is not a delete marker, Amazon S3 adds a delete marker with a
 unique version ID. This makes the current version noncurrent, and the delete
 marker the current version.
* **Versioning-suspended bucket** – Amazon S3
 creates a delete marker with null as the version ID. This delete marker replaces
 any object version with a null version ID in the version hierarchy, which
 effectively deletes the object.
For a versioned bucket (that is, versioning-enabled or versioning-suspended), there
 are several considerations that guide how Amazon S3 handles the `Expiration`
 action. For versioning-enabled or versioning-suspended buckets, the following
 applies:


* Object expiration applies only to an object's current version (it has no
 impact on noncurrent object versions).
* Amazon S3 doesn't take any action if there are one or more object versions and the
 delete marker is the current version.
* If the current object version is the only object version and it is also a
 delete marker (also referred as an *expired object delete
 marker*, where all object versions are deleted and you only have a
 delete marker remaining), Amazon S3 removes the expired object delete marker. You can
 also use the `Expiration` action to direct Amazon S3 to remove any expired
 object delete markers. For example, see [Removing expired object delete markers in a versioning-enabled bucket](lifecycle-configuration-examples.md#lifecycle-config-conceptual-ex7 "lifecycle-configuration-examples.md#lifecycle-config-conceptual-ex7").
* You can use the `NoncurrentVersionExpiration` action element to
 direct Amazon S3 to permanently delete noncurrent versions of objects. These deleted
 objects can't be recovered. You can base this expiration on a certain number of
 days since the objects became noncurrent. In addition to the number of days, you
 can also provide a maximum number of noncurrent versions to retain (between 1
 and 100). This value specifies how many newer noncurrent versions must exist
 before Amazon S3 can perform the associated action on a given version. To specify the
 maximum number of noncurrent versions, you must also provide a
 `Filter` element. If you don't specify a `Filter`
 element, Amazon S3 generates an `InvalidRequest` error when you provide a
 maximum number of noncurrent versions. For more information about using the
 `NoncurrentVersionExpiration` action element, see [Elements to describe lifecycle
 actions](intro-lifecycle-rules.md#intro-lifecycle-rules-actions "intro-lifecycle-rules.md#intro-lifecycle-rules-actions").
* Amazon S3 doesn't take any action on noncurrent versions of objects that have the
 S3 Object Lock configuration applied.
* For objects with a `Pending` replication status, Amazon S3 doesn't take
 any action on current or non-current versions of objects.
For more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

###### Important

When you have multiple rules in an S3 Lifecycle configuration, an object can become
 eligible for multiple S3 Lifecycle actions on the same day. In such cases, Amazon S3
 follows these general rules:


* Permanent deletion takes precedence over transition.
* Transition takes precedence over creation of [delete markers](DeleteMarker.md "DeleteMarker.md").
* When an object is eligible for both an S3 Glacier Flexible Retrieval and an
 S3 Standard-IA (or an S3 One Zone-IA) transition, Amazon S3 chooses the
 S3 Glacier Flexible Retrieval transition.
 For examples, see [Examples of overlapping filters and
 conflicting lifecycle actions](lifecycle-conflicts.md#lifecycle-config-conceptual-ex5 "lifecycle-conflicts.md#lifecycle-config-conceptual-ex5"). 


###### Existing and new objects


When you add a Lifecycle configuration to a bucket, the configuration rules apply
 to both existing objects and objects that you add later. For example, if you add a
 Lifecycle configuration rule today with an expiration action that causes objects
 with a specific prefix to expire 30 days after creation, Amazon S3 will queue for removal
 any existing objects that are more than 30 days old and that have the specified
 prefix.


###### Important

You can't use a bucket policy to prevent deletions or transitions by an
 S3 Lifecycle rule. For example, even if your bucket policy denies all actions for all
 principals, your S3 Lifecycle configuration still functions as normal.


## How to find when objects will expire


To find when the current version of an object is scheduled to expire, use the
 [HeadObject](../API/RESTObjectHEAD.md "../API/RESTObjectHEAD.md")
 or [GetObject](../API/RESTObjectGET.md "../API/RESTObjectGET.md") API
 operation. These API operations return response headers that provide the date and
 time at which the current version of the object is no longer cacheable. 


###### Note


* There may be a delay between the expiration date and the date at which
 Amazon S3 removes an object. You are not charged for expiration or the
 storage time associated with an object that has expired.
* Before updating, disabling, or deleting Lifecycle rules, use the
 `LIST` API operations (such as [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md"), [ListObjectVersions](../API/API_ListObjectVersions.md "../API/API_ListObjectVersions.md"), and [ListMultipartUploads](../API/API_ListMultipartUploads.md "../API/API_ListMultipartUploads.md")) or [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md") to
 verify that Amazon S3 has transitioned and expired eligible objects based on
 your use cases.

## Minimum storage duration
 charge


If you create an S3 Lifecycle expiration rule that causes objects that have been in
 S3 Standard-IA or S3 One Zone-IA storage for less than 30 days to expire, you are
 charged for 30 days. If you create a Lifecycle expiration rule that causes objects
 that have been in S3 Glacier Flexible Retrieval storage for less than 90 days to
 expire, you are charged for 90 days. If you create a Lifecycle expiration rule that
 causes objects that have been in S3 Glacier Deep Archive storage for less
 than 180 days to expire, you are charged for 180 days.


For more information, see [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
