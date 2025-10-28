# Troubleshooting S3 object

post-scan tag failures in Malware Protection for S3

This section applies to you only if you [Enable tagging for scanned
objects](enable-malware-protection-s3-bucket.md#tag-scanned-objects-s3-malware-protection "enable-malware-protection-s3-bucket.md#tag-scanned-objects-s3-malware-protection") in your protected
bucket.

When GuardDuty attempts to add a tag to your scanned S3 object, the action of tagging
may result in a failure. The potential reasons why this may happen to your bucket
are `ACCESS_DENIED` and `MAX_TAG_LIMIT_EXCEEDED`. Use the
following topics to understand the potential reasons for these post-scan tag failure
reasons and troubleshoot them.

**ACCESS_DENIED**

The following list provides potential reasons that may cause this
issue:

- The IAM role used for this protected S3 bucket is missing
  the **AllowPostScanTag** permission. Verify
  that the associated IAM role uses this bucket policy. For more
  information, see [Create or
  update IAM role policy](malware-protection-s3-iam-policy-prerequisite.md "malware-protection-s3-iam-policy-prerequisite.md").
- The protected S3 bucket policy does't allow GuardDuty to add
  tags to this object.
- The scanned S3 object no longer exists.

**MAX_TAG_LIMIT_EXCEEDED**

By default, you can associate up to 10 tags with an S3 object. For
more information, see Considerations for GuardDuty to add a tag to your S3
object under [Enable tagging for scanned
objects](enable-malware-protection-s3-bucket.md#tag-scanned-objects-s3-malware-protection "enable-malware-protection-s3-bucket.md#tag-scanned-objects-s3-malware-protection").
