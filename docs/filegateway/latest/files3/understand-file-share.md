# Understanding file share status

You can view the health of a file share at a glance by looking at its status. If the
status indicates that the file share is functioning normally, no action is needed on
your part. If the status indicates that there's a problem, you can investigate to
determine whether action could be required.

You can view a file share's status on the Storage Gateway console in the
**Status** column. A file share that's functioning properly shows a
status of AVAILABLE. This should be the status most of the time.

The following table describes file share statuses, what they mean, and whether action
might be required.

| Status         | Meaning                                                                                                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVAILABLE      | The file share is configured properly and is available to use.<br>This is the standard status for a file share that's working<br>properly.                                                                                                                                                  |
| CREATING       | The file share is not yet fully created and is not ready for use.<br>The CREATING status is transitional. No action is required. If the<br>file share gets stuck in this status, it's probably because the<br>gateway VM lost connection to AWS.                                            |
| UPDATING       | The file share configuration is currently updating. The UPDATING<br>status is transitional. No action is required. If a file share gets<br>stuck in this status, it's probably because the gateway VM lost<br>connection to AWS.                                                            |
| DELETING       | The file share is being deleted. The file share is not deleted<br>until all data is uploaded to AWS. The DELETING status is<br>transitional, and no action is required.                                                                                                                     |
| FORCE_DELETING | The file share is being deleted forcibly. The file share is<br>deleted immediately and data is not uploaded to AWS. The<br>FORCE_DELETING status is transitional, and no action is<br>required.                                                                                             |
| UNAVAILABLE    | The file share is in an unhealthy state. Action is required. Some<br>possible causes include role policy errors or mapping to an Amazon S3<br>bucket that doesn't exist. When the issue that caused the<br>unhealthy state is resolved, the file share returns to a status of<br>AVAILABLE. |
