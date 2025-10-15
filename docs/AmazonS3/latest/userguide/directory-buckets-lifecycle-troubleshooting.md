# Troubleshooting S3 Lifecycle issues for directory buckets

###### Topics

* [I set up my lifecycle configuration but objects in my directory bucket are not expiring](#troubleshoot-directory-bucket-lifecycle-1 "#troubleshoot-directory-bucket-lifecycle-1")
* [How do I monitor the actions taken by my
 lifecycle rules?](#troubleshoot-directory-bucket-lifecycle-2 "#troubleshoot-directory-bucket-lifecycle-2")

## I set up my lifecycle configuration but objects in my directory bucket are not expiring


S3 Lifecycle for directory buckets utilizes public APIs to delete objects in S3
 Express One Zone. To use object level public APIs, you must grant permission to
 `CreateSession` and allow S3 Lifecycle permission to delete your objects.
 If you have an active policy that denies deletes, this will prevent you from allowing S3
 Lifecycle to delete objects on your behalf.


It’s important to configure your bucket policies correctly to ensure that the objects that you want to delete are eligible for expiration. You can check your AWS CloudTrail logs for `AccessDenied` Trails for `CreateSession` API invocations in CloudTrail to verify if access has been denied. 
 Checking your CloudTrail logs can assist you in troubleshooting access issues and identifying the root cause of access denied errors. 
 You can then fix your incorrect access controls by updating the relevant policies. 


If you confirm that your bucket policies are set correctly and you are still experiencing issues, we recommend that you review the 
 lifecycle rules to ensure that they are applied to the right subset of objects. 


## How do I monitor the actions taken by my
 lifecycle rules?



 You can use AWS CloudTrail data event logs to monitor actions taken by S3 Lifecycle in directory buckets. 
 For more information, see [CloudTrail log file examples](s3-express-log-files.md "s3-express-log-files.md").
