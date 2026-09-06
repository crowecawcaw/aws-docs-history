

# Complete the fields on the console
<a name="archive-specify-destination"></a>

1. Enter the different portions of the destination in the appropriate fields.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/archive-specify-destination.html)

1. Leave the **Credentials** section blank in both the **Archive group destinations** sections. MediaLive has permission to write to the S3 bucket via the trusted entity. Someone in your organization should have already set up these permissions. For more information, see [Access requirements for the trusted entity](trusted-entity-requirements.md).

1. Complete the **CDN settings** field only if MediaLive must set a canned ACL whenever it sends this output to the Amazon S3 bucket.

   Use of a canned ACL typically only applies if your organization is not the owner of the Amazon S3 bucket. You should have discussed the use of a canned ACL with the bucket owner when you discussed the [destination for the output](archive-op-origin-server-s3.md#setting-dss-archive-canned-acl).

1. Complete the **Rollover interval** field in the **Archive settings** section.

   For example, **300** divides the output into separate files, each with a 300 second (5 minutes) long duration. 

   Each time the rollover expires, MediaLive closes the current file on Amazon S3 and starts a new file using the `baseFilename`, the `nameModifier`, and a sequential counter. 

   The current file is visible on Amazon S3 only after it has closed.

For more information, see the [examples](archive-examples.md). 