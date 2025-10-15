# Deleting Amazon S3 objects

You can delete one or more objects directly from Amazon S3 using the Amazon S3 console, AWS SDKs,
 AWS Command Line Interface (AWS CLI), or REST API. For example, if you're collecting log files, it's a good
 idea to delete them when they're no longer needed. You can [set up an
 S3 Lifecycle rule](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md") to automatically delete objects such as log files.

To delete an object, you can use one of the following API operations:


* Delete a single object – Amazon S3 provides the
 `DELETE` (`DeleteObject`) API operation that you can use
 to delete one object in a single HTTP request.
* Delete multiple objects – Amazon S3 provides the
 Multi-Object Delete (`DeleteObjects`) API operation that you can use to
 delete up to 1,000 objects in a single HTTP request.
When deleting objects from a bucket that is not versioning-enabled, you provide only the
 object key name. However, when deleting objects from a versioning-enabled bucket, you can
 provide the version ID of the object to delete a specific version of the object.


## Best practices to consider before
 deleting an object


Before you delete an object, consider the following best practices:



* Enable [bucket
 versioning](manage-versioning-examples.md "manage-versioning-examples.md"). [S3 Versioning](Versioning.md "Versioning.md") adds
 protection against simple `DeleteObject` requests to prevent accidental deletions.
 For versioned buckets, if you delete the current version of an object or when a
 delete request doesn’t specify a specific version Id, Amazon S3 doesn’t
 permanently delete the object. Instead, S3 adds a delete marker, issuing
 a soft delete of the object. The delete marker then becomes the current (or
 newest) version of the object with a new version ID. For more information, see [Deleting object
 versions from a versioning-enabled bucket](DeletingObjectVersions.md "DeletingObjectVersions.md").
* If you want to delete a large number of objects, or for programmatically
 deleting objects based on object creation date, [set a S3 Lifecycle configuration on your bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md"). To monitor these
 deletions, we recommend that you [use an
 S3 Lifecycle event notification](lifecycle-configure-notification.md "lifecycle-configure-notification.md"). When you configure S3 Lifecycle
 notifications, the `s3:LifecycleExpiration:Delete` event type
 notifies you when an object in a bucket is deleted. It also notifies you when an
 object version is permanently deleted by an S3 Lifecycle configuration. The
 `s3:LifecycleExpiration:DeleteMarkerCreated` event type notifies
 you when S3 Lifecycle creates a delete marker. A delete marker is created when a
 current version of an object in a versioned bucket is deleted.
* Before making any updates to your S3 Lifecycle configuration, confirm that
 Lifecycle has completed the actions on all intended objects. For more
 information, see the **Updating, disabling, or deleting
 Lifecycle rules** section in [Setting an S3 Lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").


###### Note

The S3 Lifecycle rules must apply to the right subset of objects to prevent
 unintended deletions. You can filter objects by prefixes, object tags, or
 object sizes when creating the Lifecycle rules.
* Consider restricting users from removing or deleting objects from your bucket.
 To restrict users, you’ll need to explicitly deny users the permissions for the
 following actions in your [Amazon S3 bucket
 policies](bucket-policies.md "bucket-policies.md"):




	+ `s3:DeleteObject`, `s3:DeleteObjectVersion` (to
	 control who can delete objects using API requests)
	+ `s3:PutLifecycleConfiguration` (to control who can add
	 S3 Lifecycle expiration rules)
* Consider using [S3 Replication](replication.md "replication.md") to
 create multiple copies of your data and to replicate them to multiple locations
 at once. You can choose as many destination buckets as needed. Additionally, if
 an object is unintentionally deleted, you'll still have a copy of the data.

## Deleting objects from a
 versioning-enabled bucket


If your bucket is versioning-enabled, multiple versions of the same object can exist
 in the bucket. When working with versioning-enabled buckets, the `Delete` API
 operations enable the following options:



* Specify a non-versioned delete request –
 Specify only the object's key, and not the version ID. In this case, Amazon S3
 creates a delete marker over the current version of the object and returns its
 version ID in the response. This makes your object disappear from the bucket.
 For information about object versioning and the delete marker concept, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").
* Specify a versioned delete request –
 Specify both the key and version ID. In this case, the following outcomes are
 possible:




	+ If the version ID maps to a specific object version, Amazon S3 deletes the
	 specific version of the object.
	+ If the version ID maps to the delete marker of an object, Amazon S3 deletes
	 the delete marker. When the delete marker gets deleted, the object then
	 reappears in your bucket.

## Deleting objects from a
 versioning-suspended bucket


If your bucket is versioning-suspended, the `Delete` API operations behave
 the same way for versioning enabled buckets (except for when the current version has a null
 version ID). For more information, see [Deleting objects from
 versioning-suspended buckets](DeletingObjectsfromVersioningSuspendedBuckets.md "DeletingObjectsfromVersioningSuspendedBuckets.md"). 


## Deleting objects from an
 unversioned bucket


If your bucket is unversioned, you can specify the object's key in the
 `Delete` API operations and Amazon S3 will permanently delete the object. To
 prevent permanent deletion of an object, [enable bucket
 versioning](manage-versioning-examples.md "manage-versioning-examples.md").


## Deleting objects from an
 MFA-enabled bucket


When deleting objects from a multi-factor authentication (MFA)-enabled bucket, note
 the following:



* If you provide an MFA token that isn't valid, the request always fails.
* If you have an MFA-enabled bucket and you make a versioned delete request (you
 provide an object key and version ID), the request fails if you don't provide a
 valid MFA token. In addition, when using the multi-object `Delete`
 API operation on an MFA-enabled bucket, if any of the deletes are a versioned
 delete request (that is, you specify an object key and version ID), the entire
 request fails if you don't provide an MFA token.

However, in the following cases, the request succeeds:



* If you have an MFA-enabled bucket and you make a non-versioned delete request
 (you are not deleting a versioned object),
 and you don't
 provide an MFA token, the delete succeeds.
* If you have a Multi-Object Delete request that specifies only non-versioned
 objects to delete from an MFA-enabled bucket
 and you don't provide an MFA
 token, the deletions succeed.

For information about MFA delete, see [Configuring MFA delete](MultiFactorAuthenticationDelete.md "MultiFactorAuthenticationDelete.md").


###### Topics

* [Deleting a single object](delete-objects.md "delete-objects.md")
* [Deleting multiple objects](delete-multiple-objects.md "delete-multiple-objects.md")
