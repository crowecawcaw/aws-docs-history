# Restore objects with Batch Operations

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
 The **Restore** operation initiates restore requests for the archived Amazon S3
 objects that are listed in your manifest. The following archived objects must be restored before
 they can be accessed in real time:


* Objects archived in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage
 classes
* Objects archived through the S3 Intelligent-Tiering storage class in the Archive Access
 or Deep Archive Access tiers
Using a **Restore** ([S3InitiateRestoreObjectOperation](../API/API_control_S3InitiateRestoreObjectOperation.md "../API/API_control_S3InitiateRestoreObjectOperation.md")) operation in your S3 Batch Operations
 job results in a `RestoreObject` request for every object that's specified in the
 manifest.

###### Important

The **Restore** job only *initiates* the request to
 restore objects. S3 Batch Operations reports the job as complete for each object after the request
 is initiated for that object. Amazon S3 doesn't update the job or otherwise notify you when the
 objects have been restored. However, you can use S3 Event Notifications to receive
 notifications when the objects are available in Amazon S3. For more information, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").


When you create a **Restore** job, the following arguments are
 available:



**ExpirationInDays**

This argument specifies how long the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
 object remains available in Amazon S3. **Restore** jobs that target
 S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive objects require that you set
 `ExpirationInDays` to `1` or greater.


###### Important

Don't set `ExpirationInDays` when creating **Restore**
 operation jobs that target S3 Intelligent-Tiering Archive Access and Deep Archive Access
 tier objects. Objects in S3 Intelligent-Tiering archive access tiers aren't subject to
 restore expiration, so specifying `ExpirationInDays` results in a
 `RestoreObject` request failure.



**GlacierJobTier**

Amazon S3 can restore objects by using one of three different retrieval tiers:
 `EXPEDITED`, `STANDARD`, and `BULK`. However, the
 S3 Batch Operations feature supports only the `STANDARD` and `BULK`
 retrieval tiers. For more information about the differences between the retrieval tiers,
 see [Understanding archive retrieval options](restoring-objects-retrieval-options.md "restoring-objects-retrieval-options.md"). 


For more information about the pricing for each tier, see the **Requests &
 data retrievals** section on the [Amazon S3
 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") page.




## Differences when restoring from S3 Glacier and S3 Intelligent-Tiering


Restoring archived files from the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage
 classes differs from restoring files from the S3 Intelligent-Tiering storage class in the
 Archive Access or Deep Archive Access tiers.



* When you restore from S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive, a temporary
 *copy* of the object is created. Amazon S3 deletes this copy after the value
 that you specified in the `ExpirationInDays` argument has elapsed. After this
 temporary copy is deleted, you must submit an additional restore request to access the
 object.
* When restoring archived S3 Intelligent-Tiering objects, do *not*
 specify the `ExpirationInDays` argument. When you restore an object from the
 S3 Intelligent-Tiering Archive Access or Deep Archive Access tiers, the object transitions
 back into the S3 Intelligent-Tiering Frequent Access tier. After a minimum of 90 consecutive days of no
 access, the object automatically transitions into the Archive Access tier. After a minimum
 of 180 consecutive days of no access, the object automatically moves into the
 Deep Archive Access tier.
* Batch Operations jobs can operate either on S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive
 storage class objects *or* on S3 Intelligent-Tiering
 Archive Access and Deep Archive Access storage tier objects. Batch Operations can't operate on
 both types of archived objects in the same job. To restore objects of both types, you
 *must* create separate Batch Operations jobs.

## Overlapping restores


If your [S3InitiateRestoreObjectOperation](../API/API_control_S3InitiateRestoreObjectOperation.md "../API/API_control_S3InitiateRestoreObjectOperation.md") job tries to restore an object
 that's already in the process of being restored, S3 Batch Operations proceeds as follows.


The restore operation succeeds for the object if either of the following conditions is
 true:



* Compared to the restoration request already in progress, this job's
 `ExpirationInDays` value is the same and its `GlacierJobTier`
 value is faster.
* The previous restoration request has already been completed, and the object is
 currently available. In this case, Batch Operations updates the expiration date of the restored
 object to match the `ExpirationInDays` value that's specified in the
 in-progress restoration request.

The restore operation fails for the object if any of the following conditions are
 true:



* The restoration request already in progress hasn't yet been completed, and the
 restoration duration for this job (specified by the `ExpirationInDays` value)
 is different from the restoration duration that's specified in the in-progress restoration
 request.
* The restoration tier for this job (specified by the `GlacierJobTier` value)
 is the same or slower than the restoration tier that's specified in the in-progress
 restoration request.

## Limitations


`S3InitiateRestoreObjectOperation` jobs have the following limitations:



* You must create the job in the same Region as the archived objects.
* S3 Batch Operations doesn't support the `EXPEDITED` retrieval tier.
* A single Batch Operations Restore job can support a manifest with up to 4 billion objects.

For more information about restoring objects, see [Restoring an archived object](restoring-objects.md "restoring-objects.md").
