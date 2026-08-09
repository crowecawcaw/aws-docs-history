# How S3 Files works with IAM

This page describes how AWS Identity and Access Management (IAM) works with S3 Files and
how you can use IAM policies to control access to your file systems.

S3 Files uses IAM for two distinct types of access control:

- **API access** — Controls who can create,
  manage, and delete S3 Files resources such as file systems, mount targets, and access
  points. You control this access using identity-based policies attached to IAM users,
  groups, or roles.
- **Client access** — Controls what clients (your
  mounted compute resources) can do with the file system once they connect, such as
  reading, writing, or accessing files as the root user. You control this access using
  a combination of resource-based policies, identity-based policies, access points,
  and POSIX permissions.
  Using IAM, you can permit clients to perform specific actions on a file system, including
  read-only, write, and root access. An "allow" permission on an action in either an IAM
  identity policy or a file system resource policy allows access for that action. The
  permission does not need to be granted in both an identity and a resource policy.

Your S3 bucket policies on your linked S3 bucket also govern access from your compute
resource and your file system to your S3 bucket. You must also make sure that the bucket
policies of your source bucket don't deny access from your compute resource or file system.
For more details, see [Bucket policies for Amazon
S3](bucket-policies.md "bucket-policies.md").

## Identity-based policies

Identity-based policies are JSON policies that you attach to IAM users, groups, or
roles. You can provide these permissions by writing custom policies or by attaching an
AWS managed policy. For more information about available managed policies for both API
access and client access, see [AWS managed policies for Amazon S3 Files](s3-files-security-iam-awsmanpol.md "s3-files-security-iam-awsmanpol.md").

S3 Files also optimizes read performance by allowing clients to read file data
directly from the source S3 bucket. When you mount an S3 file system on your compute
resource, you must add an inline policy to the IAM role of your compute resource which
grants permissions to read objects from the specified S3 bucket. The mount helper uses
these permissions to read the S3 data. For more details on this policy, see [IAM role for attaching your file system to AWS compute resources](s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role "s3-files-prereq-policies.md#s3-files-prereq-iam-compute-role").

## Resource-based policies

A file system policy is an IAM resource-based policy that you attach directly to a
file system to control client access. You can use file system policies to grant or deny
permissions for clients to perform operations such as mounting, writing, and root
access.

A file system either has an empty (default) file system policy or exactly one explicit
policy. S3 file system policies have a 20,000 character limit. For information on
creating and managing file system policies, see [Creating file system policies](s3-files-file-system-policies-creating.md "s3-files-file-system-policies-creating.md").

## S3 Files actions for clients

You can specify the following actions in a file system policy to control client
access:

| Action                     | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| `s3files:ClientMount`      | Provides read-only access to a file system.                 |
| `s3files:ClientWrite`      | Provides write permissions on a file system.                |
| `s3files:ClientRootAccess` | Provides use of the root user when accessing a file system. |

## S3 Files condition keys for clients

You can use the following condition keys in the `Condition` element of a
file system policy to further refine access control:

| Condition key            | Description                                                            | Operator |
| ------------------------ | ---------------------------------------------------------------------- | -------- |
| `s3files:AccessPointArn` | ARN of the S3 Files access point to which the client is<br>connecting. | String   |

## File system policy examples

### Example: Grant read-only access

The following file system policy grants only `ClientMount` (read-only)
permissions to the `ReadOnly` IAM role. Replace
`111122223333` with your AWS account ID.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:role/ReadOnly"
            },
            "Action": [
                "s3files:ClientMount"
            ]
        }
    ]
}
```

### Example: Grant access to an S3 Files access point

The following file system policy uses a condition element to grant a specific
access point full access to the file system when mounting through the access point
specified. Replace the access point ARN and account ID with your values. For more
information, see [Creating access points for an S3 file system](s3-files-access-points-creating.md "s3-files-access-points-creating.md").

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`555555555555`:role/S3FilesAccessPointFullAccess"
            },
            "Action": [
                "s3files:Client*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3files:AccessPointArn": "arn:`partition`:s3files:`region`:`account-id`:file-system/`fs-1234567890`/access-point/`fsap-0987654321`"
                }
            }
        }
    ]
}
```

## POSIX permissions

After IAM authorization succeeds, S3 Files enforces standard POSIX (Unix-style)
permissions at the file and directory level. POSIX permissions control access based on the
user ID (UID), group ID (GID), and permission bits (read, write, execute) associated with
each file and directory. Access points can enforce a specific POSIX user identity for all
requests, simplifying access management for shared datasets. For more information, see
[Creating access points for an S3 file system](s3-files-access-points-creating.md "s3-files-access-points-creating.md").

## Security groups

Security groups act as a network-level firewall that controls traffic between your
compute resources and the file system's mount targets. For details on configuring
security groups to get started on S3 Files, see [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups "s3-files-prereq-policies.md#s3-files-prereq-security-groups").
