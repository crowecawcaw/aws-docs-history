# Enable Amazon S3 Bucket

Storage for Session Script Logs

When you enable Amazon S3 logging in your session script configuration, AppStream 2.0 captures
standard output from your session script. The output is periodically uploaded to an
S3 bucket within your Amazon Web Services account. For every AWS Region, AppStream 2.0 creates a
bucket in your account that is unique to your account and the Region.

You do not need to perform any configuration tasks to manage these S3 buckets.
They are fully managed by the AppStream 2.0 service. The log files that are stored in each
bucket are encrypted in transit using Amazon S3's SSL endpoints and at rest using
Amazon S3-managed encryption keys. The buckets are named in a specific format as
follows:

```
appstream-logs-`region-code`-`account-id-without-hyphens`-`random-identifier`
```

**`region-code`**

This is the AWS Region code in which the stack is created with Amazon S3
bucket storage enabled for session script logs.

**`account-id-without-hyphens`**

Your Amazon Web Services account identifier. The random ID ensures that there is
no conflict with other buckets in that Region. The first part of the
bucket name, `appstream-logs`, does not change across
accounts or Regions.

For example, if you specify session scripts in an image in the US West (Oregon)
Region (us-west-2) on account number 123456789012, AppStream 2.0 creates an Amazon S3 bucket
within your account in that Region with the name shown. Only an administrator with
sufficient permissions can delete this bucket.

```
appstream-logs-us-west-2-1234567890123-abcdefg
```

Disabling session scripts does not delete any log files stored in the S3 bucket.
To permanently delete log files, you or another administrator with adequate
permissions must do so by using the Amazon S3 console or API. AppStream 2.0 adds a bucket policy
that prevents accidental deletion of the bucket. For more information, see
_IAM Policies and the Amazon S3 Bucket for Application Settings
Persistence_ in [Identity and Access Management for Amazon AppStream 2.0](controlling-access.md "controlling-access.md").

When session scripts are enabled, a unique folder is created for each streaming
session that is started.

The path for the folder where the log files are stored in the S3 bucket in your
account uses the following structure:

```
`bucket-name`/`stack-name`/`fleet-name`/`access-mode`/`user-id-SHA-256-hash`/`session-id`/SessionScriptsLogs/`session-event`
```

**`bucket-name`**

The name of the S3 bucket in which the session scripts are stored. The
name format is described earlier in this section.

**`stack-name`**

The name of the stack the session came from.

**`fleet-name`**

The name of the fleet the session script is running on.

**`access-mode`**

The identity method of the user: `custom` for the AppStream 2.0
API or CLI, `federated` for SAML, and `userpool`
for users in the user pool.

**`user-id-SHA-256-hash`**

The user-specific folder name. This name is created using a lowercase
SHA-256 hash hexadecimal string generated from the user
identifier.

**`session-id`**

The identifier of the user's streaming session. Each user streaming
session generates a unique ID.

**`session-event`**

The event that generated the session script log. The event values are:
`SessionStart` and
`SessionTermination`.

The following example folder structure applies to a streaming session started from
the test-stack and test-fleet. The session uses the API of user ID
`testuser@mydomain.com`, from an AWS account ID of
`123456789012`, and the settings group `test-stack` in the
US West (Oregon) Region (us-west-2):

```
appstream-logs-us-west-2-1234567890123-abcdefg/test-stack/test-fleet/custom/a0bcb1da11f480d9b5b3e90f91243143eac04cfccfbdc777e740fab628a1cd13/05yd1391-4805-3da6-f498-76f5x6746016/SessionScriptsLogs/SessionStart/
```

This example folder structure contains one log file for a user context session
start script, and one log file for a system context session start script, if
applicable.
