# Exporting findings to Amazon S3 - access error

When you export GuardDuty findings to an Amazon S3 bucket (publishing destination),
if GuardDuty is unable to access this publishing destination, then you may get an access error.

After you configure settings to export findings, if GuardDuty is unable to export findings, it
displays an error message on the **Settings** page in the GuardDuty console. This
can potentially happen when GuardDuty can no longer access the target resource. For example, if your
Amazon S3 bucket was deleted or the permission to access the bucket was modified. This can also
potentially happen when GuardDuty can no longer access the AWS KMS key that was used to encrypt the
data in your Amazon S3 bucket. When GuardDuty is unable to export, it sends a notification to the email
associated with the account to provide information about this issue.

**How to resolve the access error?**

To resolve the issue, make sure that the corresponding resources exist and GuardDuty has the
permissions to access the needed resources.

For more information, see [Exporting generated findings to
Amazon S3](guardduty_exportfindings.md "guardduty_exportfindings.md").

**What happens when you don't resolve this error?**

If you don't resolve the issue before the 90-day
finding retention period completes in GuardDuty, your findings will not get exported. GuardDuty will
disable finding export settings for this account in the specific Region.

To start exporting the findings again, update the configuration settings in
the specific Region.
