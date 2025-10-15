# Amazon EventBridge mapping and
 troubleshooting

The following table describes how Amazon S3 event types are mapped to Amazon EventBridge event
 types.



|  S3 event type |  Amazon EventBridge detail type  |
| --- | --- |
| [ObjectCreated:Put](../API/API_PutObject.md "../API/API_PutObject.md")
[ObjectCreated:Post](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
[ObjectCreated:Copy](../API/API_CopyObject.md "../API/API_CopyObject.md")
[ObjectCreated:CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md") | Object Created |
| ObjectRemoved:Delete
ObjectRemoved:DeleteMarkerCreated
LifecycleExpiration:Delete
LifecycleExpiration:DeleteMarkerCreated | Object Deleted |
| [ObjectRestore:Post](../API/API_RestoreObject.md "../API/API_RestoreObject.md") | Object Restore Initiated |
| ObjectRestore:Completed | Object Restore Completed |
| ObjectRestore:Delete | Object Restore Expired |
| LifecycleTransition | Object Storage Class Changed |
| IntelligentTiering | Object Access Tier Changed |
| [ObjectTagging:Put](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md") | Object Tags Added |
| [ObjectTagging:Delete](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md") | Object Tags Deleted |
| [ObjectAcl:Put](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md") | Object ACL Updated |


## Amazon EventBridge troubleshooting


For information about how to troubleshoot EventBridge, see [Troubleshooting Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-troubleshooting.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-troubleshooting.html") in
 the *Amazon EventBridge User Guide*.
