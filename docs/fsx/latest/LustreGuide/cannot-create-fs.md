# Creating an FSx for Lustre file system fails

There are a number of potential causes when a file system creation request fails,
as described in the following topics.

## Cannot create an EFA-enabled file system because of

misconfigured security group

Creating an FSx for Lustre EFA-enabled file system fails with the following error message:

```
`Insufficient security group permissions to create an EFA-enabled file system.
Update security group to allow all internal inbound and outbound traffic.`
```

**Action to take**

Make sure that the VPC security group you are using for the creation operation
is configured as described in [EFA-enabled security groups](limit-access-security-groups.md#efa-security-groups "limit-access-security-groups.md#efa-security-groups"). An EFA requires a security group that allows
all inbound and outbound traffic to and from the security group itself and the
security group of the clients if clients reside in a different security group.

## Cannot create a file system because of

misconfigured security group

Creating an FSx for Lustre file system fails with the following error message:

```
`The file system cannot be created because the default security group in the subnet provided
or the provided security groups do not permit Lustre LNET network traffic on port 988`
```

**Action to take**

Make sure that the VPC security group you are using for the creation operation
is configured as described in [File system access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md"). You must set up the security
group to allow inbound traffic on ports 988 and 1018-1023 from the security
group itself or the full subnet CIDR, which is required to allow the file system
hosts to communicate with each other.

## Cannot create a file system because of

insufficient capacity errors

You may receive an insufficient capacity error when attempting to create a new file system,
update storage capacity, or modify throughput capacity.

**Cause**

This error occurs when FSx for Lustre does not currently have enough available hardware capacity
in the requested Availability Zone to fulfill your request.

**Solution**

To resolve the issue, try the following:

- Wait a few minutes and retry your request, as capacity availability
  changes frequently.
- Try your request in a different Availability Zone.
- Attempt the operation with a smaller storage size or lower
  throughput level

## Cannot create a file system that is linked to an S3 bucket

If creating a new file system that is linked to an S3 bucket fails with an error message similar to the following.

```
User: arn:aws:iam::`012345678901`:user/`username` is not authorized to perform: iam:PutRolePolicy on resource: `resource ARN`

```

This error can happen if you try to create a file system linked to an Amazon S3 bucket
without the necessary IAM permissions. The required IAM
permissions support the Amazon FSx for Lustre service-linked role that is used to access the specified
Amazon S3 bucket on your behalf.

**Action to take**

Ensure that your IAM entity (user, group, or role) has the appropriate permissions
to create file systems. Doing this includes adding the permissions policy that supports
the Amazon FSx for Lustre service-linked role. For more information, see [Adding permissions to use data repositories in
Amazon S3](setting-up.md#fsx-adding-permissions-s3 "setting-up.md#fsx-adding-permissions-s3").

For more information about service-linked roles, see [Using service-linked roles for
Amazon FSx](using-service-linked-roles.md "using-service-linked-roles.md").
