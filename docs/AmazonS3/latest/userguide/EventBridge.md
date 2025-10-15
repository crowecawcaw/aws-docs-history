# Using EventBridge

Amazon S3 can send events to Amazon EventBridge whenever certain events happen in your bucket. Unlike
 other destinations, you don't need to select which event types you want to deliver. After
 EventBridge is enabled, all events below are sent to EventBridge. You can use EventBridge rules to route events
 to additional targets. The following lists the events Amazon S3 sends to EventBridge.



|  Event type |  Description  |
| --- | --- |
| *Object Created* | An object was created.
The reason field in the event message structure indicates which S3 API was used
 to create the object: [PutObject](../API/API_PutObject.md "../API/API_PutObject.md"), [POST
 Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md"), [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), or [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md"). |
| *Object Deleted (DeleteObject)*
*Object Deleted (Lifecycle expiration)* | An object was deleted.
When an object is deleted using an S3 API call, the reason field is set to
 DeleteObject. When an object is deleted by an S3 Lifecycle expiration rule, the
 reason field is set to Lifecycle Expiration. For more information, see [Expiring objects](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md").
When an unversioned object is deleted, or a versioned object is permanently
 deleted, the deletion-type field is set to Permanently Deleted. When a delete
 marker is created for a versioned object, the `deletion-type` field is set to
 Delete Marker Created. For more information, see [Deleting object versions from a
 versioning-enabled bucket](DeletingObjectVersions.md "DeletingObjectVersions.md"). |
| *Object Restore Initiated* | An object restore was initiated from S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
 storage class or from S3 Intelligent-Tiering Archive Access or Deep Archive Access tier.
 For more information, see [Working with archived objects](archived-objects.md "archived-objects.md"). |
| *Object Restore Completed* | An object restore was completed. |
| *Object Restore Expired* | The temporary copy of an object restored from S3 Glacier Flexible Retrieval or
 S3 Glacier Deep Archive expired and was deleted. |
| *Object Storage Class Changed* | An object was transitioned to a different storage class. For more
 information, see [Transitioning objects
 using Amazon S3 Lifecycle](lifecycle-transition-general-considerations.md "lifecycle-transition-general-considerations.md"). |
| *Object Access Tier Changed* | An object was transitioned to the S3 Intelligent-Tiering Archive Access tier or
 Deep Archive Access tier. For more information, see [Managing storage costs with Amazon S3 Intelligent-Tiering](intelligent-tiering.md "intelligent-tiering.md"). |
| *Object ACL Updated* | An object's access control list (ACL) was set using `PutObjectAcl`.
 An event is not generated when a request results in no change to an object’s ACL. For more
 information, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md"). |
| *Object Tags Added* | A set of tags was added to an object using `PutObjectTagging`. For
 more information, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md"). |
| *Object Tags Deleted* | All tags were removed from an object using `DeleteObjectTagging`. For
 more information, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md"). |

###### Note

For more information about how Amazon S3 event types map to EventBridge event types, see [Amazon EventBridge mapping and
 troubleshooting](ev-mapping-troubleshooting.md "ev-mapping-troubleshooting.md").

You can use Amazon S3 Event Notifications with EventBridge to write rules that take actions when an event occurs
 in your bucket. For example, you can have it send you a notification. For more information, see [What is EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html") in the
 *Amazon EventBridge User Guide*.

For more information about the actions and data types you can interact with using the EventBridge API, see the [Amazon EventBridge API Reference](https://docs.aws.amazon.com/eventbridge/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/eventbridge/latest/APIReference/Welcome.html") in the *Amazon EventBridge API Reference*.

For information about pricing, see [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing "https://aws.amazon.com/eventbridge/pricing").

###### Topics

* [Amazon EventBridge permissions](ev-permissions.md "ev-permissions.md")
* [Enabling Amazon EventBridge](enable-event-notifications-eventbridge.md "enable-event-notifications-eventbridge.md")
* [EventBridge event message structure](ev-events.md "ev-events.md")
* [Amazon EventBridge mapping and
 troubleshooting](ev-mapping-troubleshooting.md "ev-mapping-troubleshooting.md")
