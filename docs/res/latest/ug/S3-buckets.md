

# Amazon S3 buckets
<a name="S3-buckets"></a>

Research and Engineering Studio (RES) supports mounting [Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to Linux Virtual Desktop Infrastructure (VDI) instances. RES Administrators can onboard S3 buckets to RES, attach them to projects, edit their configuration, and remove buckets in the S3 buckets tab under **Environment Management**.

The S3 buckets dashboard provides a list of onboarded S3 buckets available to you. From the S3 buckets dashboard, you can:

1. Use **Add bucket** to onboard an S3 bucket to RES. 

1. Select an S3 bucket and use the **Actions** menu to: 
   + Edit a bucket
   + Remove a bucket

1. Use the search field to search by Bucket name and find onboarded S3 buckets.  
![The S3 buckets list lets you search by bucket name and find onboarded buckets](http://docs.aws.amazon.com/res/latest/ug/images/docs-list-bucket.png)

The following sections describe how to manage Amazon S3 buckets in your RES projects.

**Topics**
+ [Amazon S3 bucket prerequisites for isolated VPC deployments](S3-buckets-prereqs.md)
+ [Add an Amazon S3 bucket](S3-buckets-add.md)
+ [Edit an Amazon S3 bucket](S3-buckets-edit.md)
+ [Remove an Amazon S3 bucket](S3-buckets-remove.md)
+ [Data Isolation](S3-buckets-data-isolation.md)
+ [Cross account bucket access](S3-buckets-cross-account-access.md)
+ [Preventing data exfiltration in a private VPC](S3-buckets-preventing-exfiltration.md)
+ [Troubleshooting](S3-buckets-troubleshooting.md)
+ [Enabling CloudTrail](S3-buckets-enabling-cloudtrail.md)