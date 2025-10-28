# Implementation summary

In Amazon EFS, a file system is the primary resource. Each file system has properties such as
ID, creation token, creation time, file system size in bytes, number of mount targets created
for the file system, and the file system lifecycle policies.

Amazon EFS also supports other resources to configure the primary resource. These include mount
targets and access points:

- **Mount target** – To access your file system, you
  must create mount targets in your VPC. Each mount target has the following properties: the
  mount target ID, the subnet ID in which it is created, the file system ID for which it is
  created, an IP address at which the file system may be mounted, VPC security groups, and the mount target
  state. You can use the IP address or the DNS name in your `mount` command.

Each file system has a DNS name of the following form.

```
`file-system-id`.efs.`aws-region`.amazonaws.com
```

You can specify this DNS name in your `mount` command to mount the Amazon EFS
file system. Suppose you create an `efs-mount-point` subdirectory off of your
home directory on your EC2 instance or on-premises server. Then, you can use the mount
command to mount the file system. For example, on an Amazon Linux AMI, you can use the
following `mount` command.

```
$ sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `file-system-DNS-name`:/ ~/efs-mount-point
```

For more information, see [Managing mount targets](accessing-fs.md "accessing-fs.md").

- **Access Points** – An access point applies an operating system user, group,
  and file system path to any file system request made using the access point. The access point's operating system
  user and group override any identity information provided by the NFS client.
  The file system path is exposed to the client as the access point's root directory.
  This ensures that each application always uses the correct operating system identity and the correct directory
  when accessing shared file-based datasets. Applications using the access point can only access data in its own directory and below.
  For more information, see [Working with access points](efs-access-points.md "efs-access-points.md").
  Mount targets and tags are _subresources_ that are associated with a file system. You can only create them
  within the context of an existing file system.

Amazon EFS provides API operations for you to create and manage these resources. In addition to
the create and delete operations for each resource, Amazon EFS supports a describe operation that
enables you to retrieve resource information. You have the following options for creating and
managing these resources:

- Use the Amazon EFS console – For an example, see [Getting started](getting-started.md "getting-started.md").
- Use the Amazon EFS command line interface (CLI) – For an example, see [Tutorial: Create an EFS file system and mount it on an
  EC2 instance using the AWS CLI](wt1-getting-started.md "wt1-getting-started.md").
- You can also manage these resources programmatically as follows:
  - Use the AWS SDKs – The AWS SDKs simplify your programming tasks by wrapping
    the underlying Amazon EFS API. The SDK clients also authenticate your requests by using
    access keys that you provide. For more information, see [Sample Code and Libraries](https://aws.amazon.com/code "https://aws.amazon.com/code").
  - Call the Amazon EFS API directly from your application – If you cannot use the
    SDKs for some reason, you can make the Amazon EFS API calls directly from your application.
    However, you need to write the necessary code to authenticate your requests if you use
    this option. For more information about the Amazon EFS API, see [Amazon EFS API](api-reference.md "api-reference.md").
