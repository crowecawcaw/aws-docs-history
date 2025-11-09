# Create the Setup Script for the VHD in Amazon WorkSpaces Applications

WorkSpaces Applications uses a setup script that you provide to mount the VHD before the
application launches. You can also use the setup script to complete other tasks
required to make your application work. For example, you can configure registry keys,
register DLLs, manage pre-requisites, or modify the user profile from the setup
script. WorkSpaces Applications provides script examples that you can use to mount your VHD.
You will need to modify these scripts for your VHD and application needs.

###### Note

Setup scripts aren't required for app blocks with WorkSpaces Applications packaging.
However, you can provide optional post-setup scripts to customize
application installation.

Use the following links to download the example scripts:

- [Amazon Linux 2 bash
  script](samples/Linux-mount-vhd-script2.md "samples/Linux-mount-vhd-script2.md")
- [Microsoft Windows
  Powershell script](samples/Windows-mount-vhd-script3.md "samples/Windows-mount-vhd-script3.md")

###### Note

WorkSpaces Applications and the Microsoft Windows operating system reserve drive
letters A through E. Don't mount VHDs or network shares to these drive
letters.
WorkSpaces Applications downloads the setup script and VHD to a directory on the fleet streaming
instance, then runs the setup script. The setup script runs on the operating system
with full administrator rights. The setup script runs in the `SYSTEM`
context on Microsoft Windows, and as the `root` user on Amazon Linux 2.

File system location for the VHD and setup script:

- Amazon Linux 2:

`/opt/appstream/AppBlocks/`appblock-name`/`

**`appblock-name`**

The name of the app block that the VHD and setup script
correspond to.

- Microsoft Windows:

`C:\AppStream\AppBlocks\`appblock-name`\`

**`appblock-name`**

The name of the app block that the VHD and setup script
correspond to.
WorkSpaces Applications maintains the file name as they are on the object. For example, if your app
block is named `MyApps`, with a VHD named
`apps.vhd` and setup script named
`mount-apps.ps1`, then the full path on a Windows streaming
instance is:

- VHD

`C:\AppStream\AppBlocks\`MyApps`\`apps.vhd``

- Setup script

`C:\AppStream\AppBlocks\`MyApps`\`mount-apps.ps1``
WorkSpaces Applications captures the standard error and standard output from your setup script when
it runs on a fleet streaming instance and uploads the output to an Amazon S3 bucket
within your account. You can use these logs to identify and resolve issues you may
have with your setup script. The buckets are named in a specific format as
follows:

```
appstream-logs-`region-code`-`account-id-without-hyphens`-`random-identifier`
```

**`region-code`**

This is the AWS Region code in which the elastic fleet is created
within.

**`account-id-without-hyphens`**

Your AWS account identifier. The random ID ensures that there is no
conflict with other buckets in that Region. The first part of the bucket
name, appstream-logs, does not change across accounts or Regions.

For example, if you create an elastic fleet in the US West (Oregon) Region
(us-west-2) on account number 123456789012, WorkSpaces Applications creates an Amazon S3 bucket within
your account in that Region with the name shown. Only an administrator with
sufficient permissions can delete this bucket.

```
appstream-logs-us-west-2-1234567890123-abcdefg
```

The path for the folder where the log files are stored in the S3 bucket in your
account uses the following structure:

```
`bucket-name`/`fleet-name`/`instance-id`/`appblock-name`/
```

**`bucket-name`**

The name of the Amazon S3 bucket in which the setup script logs are stored.
The name format is described earlier in this section.

**`Instance-id`**

The unique identifier for the streaming instance that the setup script
ran on

**`appblock-name`**

The name of the appblock that the setup script corresponds to.

The following example folder structure applies to a streaming session started from
`test-fleet`. The session is from an AWS account ID of 123456789012,
and appblock name is testappblock in the US West (Oregon) Region (us-west-2):

`appstream-logs-us-west-2-1234567890123-abcdefg/test-fleet/i-084427ab4a1cff7f5/testappblock/`

This example folder structure contains one log file for the standard output, and
one log file for the standard error.

###### Topics

- [App block setup script execution in Amazon WorkSpaces Applications](script-execution.md "script-execution.md")
