

# Managing Amazon S3 access points
<a name="access-points-for-fsxn-manage"></a>

This section explains how to manage and use your Amazon S3 access points using the AWS Management Console, AWS Command Line Interface, or API.

## S3 access point attachment lifecycle
<a name="access-point-lifecycle-states"></a>

You can view the status of an S3 access point attachment by using the Amazon FSx console, AWS CLI, or API. The following table describes the possible lifecycle states for an S3 access point attachment.


| Lifecycle state | Description | 
| --- | --- | 
| AVAILABLE | The access point attachment is available for use. | 
| CREATING | Amazon FSx is creating the access point attachment. | 
| DELETING | Amazon FSx is deleting the access point attachment. | 
| UPDATING | The access point attachment is undergoing an update. | 
| MISCONFIGURED | The access point attachment has a configuration issue that prevents it from serving requests. Common causes include the file system identity associated with the access point not being resolvable on the file system, or the attached volume being offline or unmounted. Amazon FSx periodically checks for these conditions and automatically returns the access point to `AVAILABLE` when the issue is resolved. For more information, see [S3 access point is in MISCONFIGURED state](troubleshooting-access-points-for-fsxn.md#misconfigured-access-point). | 
| FAILED | The access point attachment is in a terminal failure state. This can occur if the access point creation failed (for example, due to an unresolvable file system identity or a disabled S3 protocol on the SVM), or if the underlying S3 access point was deleted directly through Amazon S3 rather than through Amazon FSx. Delete the access point attachment and create a new one. | 

**Topics**
+ [S3 access point attachment lifecycle](#access-point-lifecycle-states)
+ [Listing S3 access point attachments](access-points-list.md)
+ [Viewing access point details](access-points-details.md)
+ [Deleting an S3 access point attachment](delete-access-point.md)