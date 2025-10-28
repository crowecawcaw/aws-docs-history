# Administer the VHDs for your users'

application settings

###### Contents

- [Amazon S3 bucket storage](#app-persistence-s3-buckets "#app-persistence-s3-buckets")
- [Reset a user's application
  settings](#app-persistence-s3-reset "#app-persistence-s3-reset")
- [Enable Amazon S3 object
  versioning and revert a user's application settings](#app-persistence-enable-versions-revert-settings "#app-persistence-enable-versions-revert-settings")
- [Increase the size of the
  application settings VHD](#app-persistence-increase-VHD-size "#app-persistence-increase-VHD-size")

## Amazon S3 bucket storage

When you enable application settings persistence, your users’ application
customizations and Windows settings are automatically saved to a Virtual Hard Disk
(VHD) file that is stored in an Amazon S3 bucket created in your AWS account. For every
AWS Region, WorkSpaces Pools creates a bucket in your account that is unique to your
account and the Region. All application settings configured by your users are stored
in the bucket for that Region.

You do not need to perform any configuration tasks to manage these S3 buckets;
they are fully managed by the WorkSpaces Pools service. The VHD file that is stored in
each bucket is encrypted in transit using Amazon S3's SSL endpoints and at rest using
[AWS Managed CMKs](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk"). The buckets are named in a specific format as
follows:

```
wspool-app-settings-`<region-code>`-`<account-id-without-hyphens>`-`<random-identifier>`
```

**`region-code`**

This is the AWS Region code in which the directory is created with
application settings persistence.

**`account-id-without-hyphens`**

Your AWS account ID. The random identifier ensures there is no
conflict with other buckets in that Region. The first part of the bucket
name, `wspool-app-settings`, does not change across accounts
or Regions.

For example, if you enable application settings persistence for directories in the
US West (Oregon) Region (us-west-2) on account number 123456789012, WorkSpaces Pools
creates an Amazon S3 bucket within your account in that Region with the name shown. Only
an administrator with sufficient permissions can delete this bucket.

```
wspool-app-settings-us-west-2-1234567890123-abcdefg
```

Disabling application settings persistence does not delete any VHDs stored in the
S3 bucket. To permanently delete settings VHDs, you or another administrator with
adequate permissions must do so by using the Amazon S3 console or API. WorkSpaces Pools adds a
bucket policy that prevents accidental deletion of the
bucket.

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

The Windows version-specific prefix. For example, v4 for Windows
Server 2012 R2.

**`settings-group`**

The settings group value. This value is applied to one or more
directories that share the same the same application settings.

**`access-mode`**

The identity method of the user: `custom` for the
WorkSpaces Pools API or CLI, `federated` for SAML, and
`userpool` for user pool users.

**`user-id-SHA-256-hash`**

The user-specific folder name. This name is created using a lowercase
SHA-256 hash hexadecimal string generated from the user ID.

The following example folder structure applies to a streaming session that is
accessed using the API or CLI with a user ID of `testuser@mydomain.com`,
an AWS account ID of `123456789012`, and the settings group
`test-stack` in the US West (Oregon) Region (us-west-2):

```
wspool-app-settings-us-west-2-1234567890123-abcdefg/Windows/v4/test-stack/custom/a0bcb1da11f480d9b5b3e90f91243143eac04cfccfbdc777e740fab628a1cd13
```

You can identify the folder for a user by generating the lowercase SHA-256 hash
value of the user ID using websites or open source coding libraries available
online.

## Reset a user's application

settings

To reset a user's application settings, you must find and delete the VHD and
associated metadata file from the S3 bucket in your AWS account. Make sure that
you do not do this during a user's active streaming session. After you delete the
user's VHD and the metadata file, the next time the user launches a session from a
streaming instance that has application settings persistence enabled, WorkSpaces Pools
creates a new settings VHD for that user.

###### To reset a user's application settings

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the S3 bucket that
   contains the application settings VHD that you want to reset.
3. Locate the folder that contains the VHD. For more information about how to
   navigate the S3 bucket folder structure, see _Amazon S3 Bucket
   Storage_ earlier in this topic.
4. In the **Name** list, select the check box next to the
   VHD and the REG, choose **More**, and then choose
   **Delete**.
5. In the **Delete objects** dialog box, verify that the VHD
   and the REG are listed, and then choose **Delete**.

The next time the user streams from a pool on which application settings
persistence is enabled with the applicable settings group, a new application
settings VHD is created. This VHD is saved to the S3 bucket at the end of the
session.

## Enable Amazon S3 object

versioning and revert a user's application settings

You can use Amazon S3 object versioning and lifecycle policies to manage your users’
application settings when your users change them. With Amazon S3 object versioning, you
can preserve, retrieve, and restore every version of the settings VHD. This enables
you to recover from both unintended user actions and application failures. When
versioning is enabled, after each streaming session, a new version of the
application settings VHD is synced to Amazon S3. The new version does not overwrite the
previous version, so if an issue with your users' settings occurs, you can revert to
a previous version of the VHD.

###### Note

Each version of the application settings VHD is saved to Amazon S3 as a separate
object and is charged accordingly.

Object versioning is not enabled by default in your S3 bucket, so you must
explicitly enable it.

###### To enable object versioning for your application settings VHD

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the S3 bucket that
   contains the application settings VHD on which to enable object
   versioning.
3. Choose **Properties**.
4. Choose **Versioning**, **Enable
   versioning**, and then choose **Save**.

To expire older versions of your application settings VHDs, you can use Amazon S3
lifecycle policies. For information, see [How Do I
Create a Lifecycle Policy for an S3 Bucket?](../../../AmazonS3/latest/user-guide/create-lifecycle.md "../../../AmazonS3/latest/user-guide/create-lifecycle.md") in the
_Amazon Simple Storage Service User Guide_.

###### To revert a user's application settings VHD

You can revert to a previous version of a user's application settings VHD by
deleting newer versions of the VHD from the applicable S3 bucket. Do not do this
when the user has an active streaming session.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the S3 bucket that
   contains the user's application settings VHD version to revert to.
3. Locate and select the folder that contains the VHD. For information about
   how to navigate the S3 bucket folder structure, see _Amazon S3
   Bucket Storage_ earlier in this topic.

When you select the folder, the settings VHD and associated metadata file
display. 4. To display a list of the VHD and metadata file versions, choose
**Show**. 5. Locate the version of the VHD to revert to. 6. In the **Name** list, select the check boxes next to the
newer versions of the VHD and associated metadata files, choose
**More**, and then choose
**Delete**. 7. Verify that the application settings VHD that you want to revert to and
the associated metadata file are the newest versions of these files.

The next time the user streams from a pool on which application settings
persistence is enabled with the applicable settings group, the reverted version of
the user's settings displays.

## Increase the size of the

application settings VHD

The default VHD maximum size is 5 GB for Pools. If a user requires additional
space for application settings, you can download the applicable application settings
VHD to a Windows computer to expand it. Then, replace the current VHD in the S3
bucket with the larger one. Do not do this when the user has an active streaming
session.

###### Note

To reduce the physical size of the virtual hard disk (VHD), clear the recycle
bin before ending a session. This also reduces upload and download times, and
improves the overall user experience.

###### To increase the size of the application settings VHD

###### Note

The full VHD must be downloaded before a user can stream applications.
Increasing the size of an application settings VHD can increase the time it
takes for users to start application streaming sessions.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the S3 bucket that
   contains the application settings VHD to expand.
3. Locate and select the folder that contains the VHD. For information about
   how to navigate the S3 bucket folder structure, see [Amazon S3 bucket storage](#app-persistence-s3-buckets "#app-persistence-s3-buckets") earlier in this
   topic.

When you select the folder, the settings VHD and associated metadata file
display. 4. Download the `Profile.vhdx` file to a directory on your Windows
computer. Do not close your browser after the download completes, because
you'll use the browser again later to upload the expanded VHD. 5. To use Diskpart to increase the size of the VHD to 7 GB, open the command
prompt as an administrator, and type the following commands.

```
diskpart
```

```
select vdisk file="C:\path\to\application\settings\profile.vhdx"
```

```
expand vdisk maximum=7000
```

6. Then, type the following Diskpart commands to find and attach the VHD, and
   display the list of volumes:

```
elect vdisk file="C:\path\to\application\settings\profile.vhdx"
```

```
attach vdisk
```

```
list volume
```

In the output, make note of the volume number with the label
"AwsEucUsers". In the next step, you select this volume so that you can
enlarge it. 7. Type the following command in which
`<volume-number>` is the
number in the list volume output.

```
select volume `<volume-number>`
```

8. Type the following command:

```
extend
```

9. Type the following commands to confirm that the size of the partition on
   the VHD increased as expected (7 GB in this example):

```
diskpart
```

```
select vdisk file="C:\path\to\application\settings\profile.vhdx"
```

```
list volume
```

10. Type the following command to detach the VHD so that it can be
    uploaded:

```
detach vdisk
```

11. Return to your browser with the Amazon S3 console, choose
    **Upload**, **Add files**, and then
    select the enlarged VHD.
12. Choose **Upload**.

After the VHD is uploaded, the next time the user streams from a pool on which
application settings persistence is enabled with the applicable settings group, the
larger application settings VHD is available.
