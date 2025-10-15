# Troubleshooting Amazon S3 Lifecycle issues

The following information can help you troubleshoot common issues with Amazon S3 Lifecycle
 rules.

###### Topics

* [I ran a list operation on my bucket and saw
 objects that I thought were expired or transitioned by a lifecycle rule.](#troubleshoot-lifecycle-1 "#troubleshoot-lifecycle-1")
* [How do I monitor the actions taken by my
 lifecycle rules?](#troubleshoot-lifecycle-2 "#troubleshoot-lifecycle-2")
* [My S3 object count still increases, even
 after setting up lifecycle rules on a versioning-enabled bucket.](#troubleshoot-lifecycle-3 "#troubleshoot-lifecycle-3")
* [How do I empty my S3 bucket by using
 lifecycle rules?](#troubleshoot-lifecycle-4 "#troubleshoot-lifecycle-4")
* [My Amazon S3 bill increased after transitioning
 objects to a lower-cost storage class.](#troubleshoot-lifecycle-5 "#troubleshoot-lifecycle-5")
* [I’ve updated my bucket policy, but my S3
 objects are still being deleted by expired lifecycle rules.](#troubleshoot-lifecycle-6 "#troubleshoot-lifecycle-6")
* [Can I recover S3 objects that are expired by
 S3 Lifecycle rules?](#troubleshoot-lifecycle-7 "#troubleshoot-lifecycle-7")
* [Why are my expiration and transition lifecycle actions
 not occurring?](#troubleshoot-lifecycle-failures "#troubleshoot-lifecycle-failures")
* [How can I exclude a prefix from my lifecycle
 rule?](#troubleshoot-lifecycle-8 "#troubleshoot-lifecycle-8")
* [How can I include multiple prefixes in my
 lifecycle rule?](#troubleshoot-lifecycle-9 "#troubleshoot-lifecycle-9")

## I ran a list operation on my bucket and saw
 objects that I thought were expired or transitioned by a lifecycle rule.


S3 Lifecycle [object transitions](lifecycle-transition-general-considerations.md "lifecycle-transition-general-considerations.md") and [object
 expirations](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md") are asynchronous operations. Therefore, there might be a delay
 between the time that the objects are eligible for expiration or transition and the time
 that they are actually transitioned or expired. Changes in billing are applied as soon
 as the lifecycle rule is satisfied, even if the action isn't complete. The exception to
 this behavior is if you have a lifecycle rule set to transition to the
 S3 Intelligent-Tiering storage class. In that case, billing changes don't occur until the
 object has transitioned to S3 Intelligent-Tiering. For more information about changes in
 billing, see [Setting lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").


###### Note

Amazon S3 doesn’t transition objects that are smaller than 128 KB from the S3 Standard
 or S3 Standard-IA storage class to the S3 Intelligent-Tiering, S3 Standard-IA, or
 S3 One Zone-IA storage class.


## How do I monitor the actions taken by my
 lifecycle rules?


To monitor actions taken by lifecycle rules, you can use the following features: 



* **S3 Event Notifications** – You can set
 up [S3
 Event Notifications](lifecycle-configure-notification.md "lifecycle-configure-notification.md") so that you're notified of any S3 Lifecycle
 expiration or transition events.
* **S3 server access logs** – You can enable
 server access logs for your S3 buckets to capture S3 Lifecycle actions, such as
 object transitions to another storage class or object expirations. For more
 information, see [Lifecycle and logging](lifecycle-and-other-bucket-config.md#lifecycle-general-considerations-logging "lifecycle-and-other-bucket-config.md#lifecycle-general-considerations-logging").

To view the changes in your storage caused by lifecycle actions on a daily basis, we
 recommend using [S3 Storage Lens dashboards](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_dashboards "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_dashboards") instead of using Amazon CloudWatch metrics. In your Storage Lens
 dashboard, you can view the following metrics, which monitor the object count or
 size:



* **Current version bytes**
* **Current version object count**
* **Noncurrent version bytes**
* **Noncurrent version object count**
* **Delete marker object count**
* **Delete marker storage bytes**
* **Incomplete multipart upload bytes**
* **Incomplete multipart upload object count**

## My S3 object count still increases, even
 after setting up lifecycle rules on a versioning-enabled bucket.


In a [versioning-enabled
 bucket](Versioning.md#versioning-states "Versioning.md#versioning-states"), when an object is expired, the object isn't completely deleted from
 the bucket. Instead, a [delete marker](DeleteMarker.md "DeleteMarker.md") is created
 as the newest version of the object. Delete markers are still counted as objects.
 Therefore, if a lifecycle rule is created to expire only the current versions, then the
 object count in the S3 bucket actually increases instead of going down.


For example, let's say an S3 bucket is versioning-enabled with 100 objects, and a
 lifecycle rule is set to expire current versions of the object after 7 days. After the
 seventh day, the object count increases to 200 because 100 delete markers are created in
 addition to the 100 original objects, which are now the noncurrent versions. For more
 information about S3 Lifecycle configuration rule actions for versioning-enabled buckets,
 see [Setting lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").


To permanently remove objects, add an additional lifecycle configuration to delete the
 previous versions of the objects, expired delete markers, and incomplete multipart
 uploads. For instructions on how to create new lifecycle rules, see [Setting lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").


###### Note


* Amazon S3 rounds the transition or expiration date of an object to midnight UTC
 the next day. 


When evaluating objects for lifecycle actions, Amazon S3 uses the object
 creation time in UTC. For example, consider a nonversioned bucket with a
 lifecycle rule that's configured to expire objects after one day. Suppose
 that an object was created on January 1 at 17:05 Pacific Daylight Time
 (PDT), which corresponds to January 2 at 00:05 UTC. The object becomes one
 day old at 00:05 UTC on January 3, which makes it eligible for expiration
 when S3 Lifecycle evaluates objects at 00:00 UTC on January 4.


Because Amazon S3 lifecycle actions occur asynchronously, there might be
 some delay between the date specified in the lifecycle rule and the actual
 physical transition of the object. For more information, see [Transition or expiration
 delay](how-to-set-lifecycle-configuration-intro.md#lifecycle-action-delay "how-to-set-lifecycle-configuration-intro.md#lifecycle-action-delay").


For more information, see [Lifecycle rules: Based on an object's age](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-number-of-days "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-number-of-days").
* For S3 objects that are protected by Object Lock, current versions are
 not permanently deleted. Instead, a delete marker is added to the objects,
 making them noncurrent. Noncurrent versions are then preserved and are not
 permanently expired.

## How do I empty my S3 bucket by using
 lifecycle rules?


S3 Lifecycle rules are an effective tool to [empty an S3 bucket](empty-bucket.md "empty-bucket.md") with
 millions of objects. To delete a large number of objects from your S3 bucket, make sure
 to use these two pairs of lifecycle rules:



* **Expire current versions of objects** and
 **Permanently delete previous versions of objects**
* **Delete expired delete markers** and **Delete
 incomplete multipart uploads**

For steps on how to create a lifecycle configuration rule, see [Setting lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").


###### Note

For S3 objects that are protected by Object Lock, current versions are not
 permanently deleted. Instead, a delete marker is added to the objects, making them
 noncurrent. Noncurrent versions are then preserved and are not permanently
 expired.


## My Amazon S3 bill increased after transitioning
 objects to a lower-cost storage class.


There are several reasons that your bill might increase after transitioning objects to
 a lower-cost storage class: 



* S3 Glacier overhead charges for small objects


For each object that is transitioned to S3 Glacier Flexible Retrieval or
 S3 Glacier Deep Archive, a total overhead of 40 KB is associated with this storage
 update. As part of the 40 KB overhead, 8 KB is used to store metadata and the
 name of the object. This 8 KB is charged according to S3 Standard rates. The
 remaining 32 KB is used for indexing and related metadata. This 32 KB is charged
 according to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive pricing.


Therefore, if you're storing many smaller sized objects, we don't recommend
 using lifecycle transitions. Instead, to reduce any overhead charges, consider
 aggregating many smaller objects into a smaller number of large objects before
 storing them in Amazon S3. For more information about cost considerations, see [Transitioning to the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage
 classes (object archival)](lifecycle-transition-general-considerations.md#before-deciding-to-archive-objects "lifecycle-transition-general-considerations.md#before-deciding-to-archive-objects").
* Minimum storage charges


Some S3 storage classes have minimum storage-duration requirements. Objects
 that are deleted, overwritten, or transitioned from those classes before the
 minimum duration is satisfied are charged a prorated early transition or
 deletion fee. These minimum storage-duration requirements are as follows: 




	+ S3 Standard-IA and S3 One Zone-IA – 30 days
	+ S3 Glacier Flexible Retrieval and S3 Glacier Instant Retrieval –
	 90 days
	+ S3 Glacier Deep Archive – 180 days
For more information about these requirements, see the
 *Constraints* section of [Transitioning objects using S3 Lifecycle](lifecycle-transition-general-considerations.md "lifecycle-transition-general-considerations.md"). For general S3 pricing
 information, see [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") and the [AWS Pricing Calculator](https://calculator.aws/#/addService/S3 "https://calculator.aws/#/addService/S3").
* Lifecycle transition costs


Each time an object is transitioned to a different storage class by a
 lifecycle rule, Amazon S3 counts that transition as one transition request. The costs
 for these transition requests are in addition to the costs of these storage
 classes. If you plan to transition a large number of objects, consider the
 request costs when transitioning to a lower tier. For more information, see
 [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## I’ve updated my bucket policy, but my S3
 objects are still being deleted by expired lifecycle rules.


`Deny` statements in a bucket policy don't prevent the expiration of the
 objects defined in a lifecycle rule. Lifecycle actions (such as transitions or
 expirations) don't use the S3 `DeleteObject` operation. Instead, S3 Lifecycle
 actions are performed by using internal S3 endpoints. (For more information, see [Lifecycle and logging](lifecycle-and-other-bucket-config.md#lifecycle-general-considerations-logging "lifecycle-and-other-bucket-config.md#lifecycle-general-considerations-logging").) 


To prevent your lifecycle rule from taking any action, you must edit, delete, or
 [disable the rule](lifecycle-configuration-examples.md#lifecycle-config-conceptual-ex2 "lifecycle-configuration-examples.md#lifecycle-config-conceptual-ex2").


## Can I recover S3 objects that are expired by
 S3 Lifecycle rules?


The only way to recover objects that are expired by S3 Lifecycle is through versioning,
 which must be in place before the objects become eligible for expiration. You cannot
 undo the expiration operations that are performed by lifecycle rules. If objects are
 permanently deleted by the S3 Lifecycle rules that are in place, you cannot recover these
 objects. To enable versioning on a bucket, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").


If you have applied versioning to the bucket and the noncurrent versions of the
 objects are still intact, you can [restore previous
 versions of the expired objects](RestoringPreviousVersions.md "RestoringPreviousVersions.md"). For more information about the behavior of
 S3 Lifecycle rule actions and versioning states, see the *Lifecycle actions and
 bucket versioning state* table in [Elements to describe lifecycle actions](intro-lifecycle-rules.md#non-current-days-calculations "intro-lifecycle-rules.md#non-current-days-calculations").


###### Note

If the S3 bucket is protected by [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html "https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html") or [S3 Replication](replication.md "replication.md"), you might also be able to use these features to
 recover your expired objects.


## Why are my expiration and transition lifecycle actions
 not occurring?


For a versioning-enabled or versioning-suspended bucket, the following considerations guide how Amazon S3
 handles the Expiration action:



* Object expiration applies only to an object's current version (it has no impact on noncurrent
 object versions).
* Amazon S3 doesn't take any action if there are one or more object versions and the delete marker is
 the current version.
* Amazon S3 doesn't take any action on noncurrent versions of objects that have S3 Object Lock
 applied.
* For objects with a `PENDING` replication status, Amazon S3 doesn't take any action current
 or noncurrent versions of objects.

Lifecycle storage class transitions have the following constraints:



* By default, objects smaller than 128 KB won't transition to any storage class.
* Objects must be stored for at least 30 days before transitioning to S3 Standard-IA or
 S3 One Zone-IA.
* For versioning enabled or versioning suspended buckets, objects with a `PENDING`
 replication status can't be transitioned.

## How can I exclude a prefix from my lifecycle
 rule?


S3 Lifecycle doesn't support excluding prefixes in your rules. Instead, use tags to tag
 all of the objects that you want to include in the rule. For more information about
 using tags in your lifecycle rules, see [Archiving all objects within one day after creation](lifecycle-configuration-examples.md#lifecycle-config-ex1 "lifecycle-configuration-examples.md#lifecycle-config-ex1").


## How can I include multiple prefixes in my
 lifecycle rule?


S3 Lifecycle doesn't support including multiple prefixes in your rules. Instead, use
 tags to tag all of the objects that you want to include in the rule. For more
 information about using tags in your lifecycle rules, see [Archiving all objects within one day after creation](lifecycle-configuration-examples.md#lifecycle-config-ex1 "lifecycle-configuration-examples.md#lifecycle-config-ex1").


However, if you have one or more prefixes that start with the same characters, you can
 include all of those prefixes in your rule by specifying a partial prefix with no
 trailing slash (`/`) in the filter. For example, suppose that you have these
 prefixes:



```
sales1999/
sales2000/
sales2001/
```

To include all three prefixes in your rule, specify
 `<Prefix>sales</Prefix>` in your lifecycle rule.
