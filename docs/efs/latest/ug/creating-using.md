# Creating and managing EFS resources

Amazon EFS provides elastic, shared file storage that is POSIX-compliant. The file system that
you create supports concurrent read and write access from multiple Amazon EC2 instances. The file
system is also accessible from all of the Availability Zones in the AWS Region where it is
created.

You can mount an Amazon EFS file system on EC2 instances in your virtual private cloud (VPC)
based on Amazon VPC by using the Network File System versions 4.0 and 4.1 protocol (NFSv4). For more
information, see [How Amazon EFS works](how-it-works.md "how-it-works.md").

As an example, suppose that you have one or more EC2 instances launched in your VPC. Now you
want to create and use a file system on these instances. Following are the typical steps that
you must perform to use Amazon EFS file systems in the VPC:

- Create an Amazon EFS file system – When creating a file
  system, we recommend using the **Name** tag. The **Name**
  tag value appears in the console and makes it easier to identify the file system. You can
  also add other optional tags to the file system.
- Create mount targets for the file system – To
  access the file system in your VPC and mount the file system to your Amazon EC2 instance, you
  must create mount targets in the VPC subnets.
- Create security groups – Both an Amazon EC2 instance and
  a mount target must have associated security groups. These security groups act as a virtual
  firewall that controls the traffic between them. You can use the security group that you
  associated with the mount target to control inbound traffic to your file system. To do this,
  add an inbound rule to the mount target security group that allows access from a specific
  EC2 instance. Then, you can mount the file system only on that EC2 instance.

###### Topics

- [Implementation summary](how-it-works-implementation.md "how-it-works-implementation.md")
- [Resource IDs](#resource-ids "#resource-ids")
- [Creation token and idempotency](#creation-token "#creation-token")
- [Creating EFS file systems](creating-using-create-fs.md "creating-using-create-fs.md")
- [Deleting EFS file systems](delete-efs-fs.md "delete-efs-fs.md")
- [Creating file system policies](create-file-system-policy.md "create-file-system-policy.md")
- [Creating access points](create-access-point.md "create-access-point.md")
- [Deleting access points](delete-access-point.md "delete-access-point.md")
- [Tagging EFS resources](manage-fs-tags.md "manage-fs-tags.md")
- [Tutorial: Creating writable
  per-user subdirectories](accessing-fs-nfs-permissions-per-user-subdirs.md "accessing-fs-nfs-permissions-per-user-subdirs.md")

## Resource IDs

Amazon EFS assigns unique resource identifiers (IDs) to all EFS resources when they
are created. All EFS resource IDs consist of a resource identifier and a
combination of digits 0–9 and lowercase letters a–f.

Before October 2021, the IDs assigned to newly created file system and mount target
resources used 8 characters after the hyphen (for example, `fs-12345678`). From May
2021 to October 2021, we changed the IDs of these resource types to use 17 characters after
the hyphen (for example, `fs-1234567890abcdef0`). Depending on when your account
was created, you might have file system and mount target resources with short IDs, though any
new resources of these types receive the longer IDs. The Resource ID
never changes.

## Creation token and idempotency

_Idempotency_ ensures that an API request completes only once. With
idempotent requests, if the original request completes successfully, subsequent requests
have no additional effect. This is useful to prevent duplicate jobs from being created when
you interact with the Amazon EFS API.

The Amazon EFS API supports idempotency with client request tokens. A _client
request token_ is a unique string that you specify when you make a create job
request.

A client request token can be any string that includes up to 64 ASCII characters. If you
reuse a client request token within one minute of a successful request, the API returns the
job details of the original request.

If you use the console, it generates the token for you. If you use the **Custom
Create** flow in the console, the creation token that is generated for you has
the following format:

```
"CreationToken": "console-d215fa78-1f83-4651-b026-facafd8a7da7"
```

If you use Quick Create to create a file system with the service recommended settings,
the creation token has the following format:

```
"CreationToken": "quickCreated-d7f56c5f-e433-41ca-8307-9d9c0f8a77a2"
```
