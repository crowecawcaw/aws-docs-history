# Troubleshooting S3 access point issues

This section describes symptoms, causes, and resolutions for when you encounter issues accessing your FSx data from S3 access points.

## S3 access point creation failed due to file system user identity lookup failure

When creating and attaching an S3 Access Point, a [`FileSystemIdentity`](../APIReference/API_OntapFileSystemIdentity.md#FSx-Type-OntapFileSystemIdentity-Type "../APIReference/API_OntapFileSystemIdentity.md#FSx-Type-OntapFileSystemIdentity-Type") must be provided. You are responsible for configuring
the provided UNIX or Windows user within ONTAP.

If a [`UnixUser`](../APIReference/API_OntapUnixFileSystemUser.md "../APIReference/API_OntapUnixFileSystemUser.md") is provided, ONTAP must be able to map the UnixUser name to UNIX UID/GIDs. ONTAP determines how to perform this
mapping using the [name service switch configuration](https://docs.netapp.com/us-en/ontap/nfs-admin/ontap-name-service-switch-config-concept.html "https://docs.netapp.com/us-en/ontap/nfs-admin/ontap-name-service-switch-config-concept.html").

```
`>` vserver services name-service ns-switch show
```

```
`Vserver Database Order
--------------- ------------ ---------
svm_1 hosts files,
 dns
svm_1 group files,
 ldap
svm_1 passwd files,
 ldap
svm_1 netgroup nis,
 files`
```

Please ensure your UnixUser has an entry in the `passwd` and `group` databases using a valid source (`files`,`ldap`, etc).
The `files` source can be configured using the `vserver services name-service unix-user` and `vserver services name-service unix-group` commands.
The `ldap` source can be configured using the `vserver services name-service ldap` command.

If a [`WindowsUser`](../APIReference/API_OntapWindowsFileSystemUser.md "../APIReference/API_OntapWindowsFileSystemUser.md") is provided, ONTAP must be able to find the WindowsUser name in the joined Active Directory domain.

To confirm if a provided UnixUser or WindowsUser is mapped correctly, using `fsxadmin` you can use the following command (replace `-unix-user-name` with `-win-name` for WindowsUsers):

```
`>` vserver services access-check authentication show-creds -node `FsxId0fd48ff588b9d3eee-01` -vserver `svm_name` -unix-user-name `root` -show-partial-unix-creds true
```

Example successful output:

```
 `UNIX UID: root

 GID: daemon
 Supplementary GIDs:
 daemon`
```

Example unsuccessful output:

```
`Error: Acquire UNIX credentials procedure failed
 [ 2 ms] Entry for user-name: unmapped-user not found in the
 current source: FILES. Entry for user-name: unmapped-user
 not found in any of the available sources
**[ 3] FAILURE: Unable to retrieve UID for UNIX user
** unmapped-user

Error: command failed: Failed to resolve user name to a UNIX ID. Reason: "SecD Error: object not found".`
```

An incorrect user mapping may result in `Access Denied` errors from S3. See example failure reasons below.

**`Entry for user-name not found in the current source: LDAP`**

If your `ns-switch` is configured to use an `ldap` source, please ensure ONTAP is configured to use your LDAP server properly. See [NetApp's Technical Report for configuring LDAP](https://www.netapp.com/pdf.html?item=/media/19423-tr-4835.pdf "https://www.netapp.com/pdf.html?item=/media/19423-tr-4835.pdf") for more information.

**`RESULT_ERROR_DNS_CANT_REACH_SERVER` or `RESULT_ERROR_SECD_IN_DISCOVERY`**

This error indicates an issue with the vserver's DNS configuration in ONTAP. Run the following to ensure your vserver's DNS is configured properly:

```
`>` dns check -vserver `svm_name`
```

## S3 access point creation failed because the volume is not mounted.

S3 access points can only be attached to FSx for ONTAP volumes that are mounted (have junction paths). This also applies to DP (Data Protection) volumes types. See [ONTAP volume mount documentation](https://docs.netapp.com/us-en/ontap/nfs-admin/mount-unmount-existing-volumes-nas-namespace-task.html "https://docs.netapp.com/us-en/ontap/nfs-admin/mount-unmount-existing-volumes-nas-namespace-task.html") for more information.

## The file system is unable to handle S3 requests

If the S3 request volume for a particular workload exceeds the file system’s capacity to handle the traffic, you may experience
S3 request errors (for example, `Internal Server Error`, `503 Slow Down`, and `Service Unavailable`).
You can proactively monitor and alarm on the performance of your file system using Amazon CloudWatch metrics (for example, `Network throughput
 utilization` and `CPU utilization`). If you observe degraded performance, you can resolve this issue by increasing the file system's
throughput capacity.

## Access Denied with default S3 access point permissions for automatically created service roles

Some S3-integrated AWS services will create a custom service role and customize the attached permissions to your
specific usecase. When specifying your S3 access point alias as the S3 resource, those attached permissions may include your access point
using a bucket ARN format (for example, `arn:aws:s3:::my-fsx-ap-foo7detztxouyjpwtu8krroppxytruse1a-ext-s3alias`)
rather than the access point ARN format (for example, `arn:aws:s3:us-east-1:1234567890:accesspoint/my-fsx-ap`).
To resolve this, modify the policy to use the ARN of the access point.
