# Working with access points

EFS _access points_ are application-specific
entry points into an EFS file system that make it easier to manage application access to
shared datasets. Access points can enforce a user identity, including the user's POSIX
groups, for all file system requests that are made through the access point. Access points
can also enforce a different root directory for the file system so that clients can only
access data in the specified directory or its subdirectories.

You can use AWS Identity and Access Management (IAM) policies to enforce that specific applications use a specific
access point. By combining IAM policies with access points, you can easily provide secure
access to specific datasets for your applications.

You can create access points for an existing EFS file system using the
AWS Management Console, the AWS Command Line Interface (AWS CLI), and the Amazon EFS API. For step-by-step procedures to create
an access point, see [Creating access points](create-access-point.md "create-access-point.md").

## Access points work with mount targets

You must create at least one mount target in your VPC before using access points.
Mount targets provide the network connectivity to your EFS file system while
access points provide the access control and application-specific entry points.

Access points inherit the mount target's Availability Zone
placement.

- Security groups are applied at the mount target level, not the access point level.
- Access points are available in all Availability Zones where you have mount
  targets.
- The IAM condition key `elasticfilesystem:AccessedViaMountTarget` ensures
  file system access only occurs through mount targets, which applies to both
  direct mounts and access point mounts.

You use the EFS mount helper when mounting a file system using an access point. In the
mount command, include file system ID, the access point ID, and the `tls` mount
option, as shown in the following example.

```
`$` mount -t efs -o tls,iam,accesspoint=fsap-abcdef0123456789a fs-abc0123def456789a: /`localmountpoint`
```

For more information on mounting file systems using an access point, see
[Mounting with EFS access points](mounting-access-points.md "mounting-access-points.md").

###### Topics

- [Enforcing a user identity using an access point](enforce-identity-access-points.md "enforce-identity-access-points.md")
- [Enforcing a root directory with an access point](enforce-root-directory-access-point.md "enforce-root-directory-access-point.md")
- [Using access points in IAM policies](access-points-iam-policy.md "access-points-iam-policy.md")
