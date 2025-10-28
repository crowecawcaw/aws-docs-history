# Amazon S3 Bucket Storage

When you enable application settings persistence, your users’ application
customizations and Windows settings are automatically saved to a Virtual Hard Disk
(VHD) file that is stored in an Amazon S3 bucket created in your AWS account. For every
AWS Region, AppStream 2.0 creates a bucket in your account that is unique to your account
and the Region. All application settings configured by your users are stored in the
bucket for that Region.

You do not need to perform any configuration tasks to manage these S3 buckets;
they are fully managed by the AppStream 2.0 service. The VHD file that is stored in each
bucket is encrypted in transit using Amazon S3's SSL endpoints and at rest using [AWS Managed CMKs](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk"). The buckets are named in a specific format as
follows:

```
appstream-app-settings-`region-code`-`account-id-without-hyphens`-`random-identifier`
```

**`region-code`**

This is the AWS Region code in which the stack is created with
application settings persistence.

**`account-id-without-hyphens`**

Your AWS account ID. The random identifier ensures there is no
conflict with other buckets in that Region. The first part of the bucket
name, `appstream-app-settings`, does not change across
accounts or Regions.

For example, if you enable application settings persistence for stacks in the US
West (Oregon) Region (us-west-2) on account number 123456789012, AppStream 2.0 creates an
Amazon S3 bucket within your account in that Region with the name shown. Only an
administrator with sufficient permissions can delete this bucket.

```
appstream-app-settings-us-west-2-1234567890123-abcdefg
```

Disabling application settings persistence does not delete any VHDs stored in the
S3 bucket. To permanently delete settings VHDs, you or another administrator with
adequate permissions must do so by using the Amazon S3 console or API. AppStream 2.0 adds a
bucket policy that prevents accidental deletion of the bucket. For more information,
see _IAM Policies and the Amazon S3 Bucket for Application Settings
Persistence_ in [Identity and Access Management for Amazon AppStream 2.0](controlling-access.md "controlling-access.md").

When application settings persistence is enabled, a unique folder is created for
each settings group to store the settings VHD. The hierarchy of the folder in the S3
bucket depends on how the user launches a streaming session, as described in the
following section.

The path for the folder where the settings VHD is stored in the S3 bucket in your
account uses the following structure:

```
`bucket-name`/Windows/`prefix`/`settings-group`/`access-mode`/`user-id-SHA-256-hash`
```

**`bucket-name`**

The name of the S3 bucket in which users' application settings are
stored. The name format is described earlier in this
section.

**`prefix`**

The Windows version-specific prefix. For example, v4 for Windows Server 2012 R2.

**`settings-group`**

The settings group value. This value is applied to one or more stacks
that share the same the same application settings.

**`access-mode`**

The identity method of the user: `custom` for the AppStream 2.0
API or CLI, `federated` for SAML, and `userpool`
for user pool users.

**`user-id-SHA-256-hash`**

The user-specific folder name. This name is created using a lowercase
SHA-256 hash hexadecimal string generated from the user ID.

The following example folder structure applies to a streaming session that is
accessed using the API or CLI with a user ID of `testuser@mydomain.com`,
an AWS account ID of `123456789012`, and the settings group
`test-stack` in the US West (Oregon) Region (us-west-2):

```
appstream-app-settings-us-west-2-1234567890123-abcdefg/Windows/v4/test-stack/custom/a0bcb1da11f480d9b5b3e90f91243143eac04cfccfbdc777e740fab628a1cd13
```

You can identify the folder for a user by generating the lowercase SHA-256 hash
value of the user ID using websites or open source coding libraries available
online.
