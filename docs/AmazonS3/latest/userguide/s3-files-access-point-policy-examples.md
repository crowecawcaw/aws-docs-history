

# Control client access to an S3 Files file system
<a name="s3-files-access-point-policy-examples"></a>

This topic describes how to use file system policies, IAM identity policies, and network controls to control which clients can access your S3 Files file system and through which access points.

## S3 Files access points
<a name="s3-files-access-point-policy-overview"></a>

S3 Files access points are application-specific entry points to a file system that simplify managing data access at scale. You can use access points to enforce user identities and permissions for all file system requests made through the access point, and restrict clients to only access data within a specified root directory and its subdirectories.

Access points scope what a client can do on the file system. They do not scope which clients can use them. Any role in your account with `s3files:ClientMount` permission can mount through any access point on the file system unless a file system policy restricts it. To control which clients can use which access point, combine three layers: network controls (prevent the connection), a file system resource policy (explicit deny that survives identity policy changes), and an IAM identity policy (least privilege on the role).

S3 Files evaluates `s3files:ClientMount`, `s3files:ClientWrite`, and `s3files:ClientRootAccess` against the file system policy on every mount. The `s3files:AccessPointArn` condition key is also evaluated on every mount, so you can write a single deny statement that blocks access through any access point except the one you specify. If any required action is denied or not granted, the mount fails before any file operations occur. The following two sections cover the two common requirements: restricting a workload to a specific access point, and denying a workload access to the file system altogether.

## Restrict access to a specific access point
<a name="s3-files-access-point-policy-restrict"></a>

This pattern applies when a role (for example, an EC2 instance role or an ECS task role) must mount the file system through one access point only. The condition key is `s3files:AccessPointArn`. The policy requires both an `Allow` for the intended access point and an explicit `Deny` for every other access point. IAM allow grants are additive across identity and resource policies; without an explicit deny, a separate policy can grant access to a different access point.

**Example file system policy:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowComputeAOnlyViaSpecificAP",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::ACCOUNT:role/compute-a-role" },
      "Action": [
        "s3files:ClientMount",
        "s3files:ClientWrite"
      ],
      "Condition": {
        "StringEquals": {
          "s3files:AccessPointArn": "arn:aws:s3files:REGION:ACCOUNT:file-system/fs-ID/access-point/fsap-ID"
        }
      }
    },
    {
      "Sid": "DenyComputeAIfWrongAP",
      "Effect": "Deny",
      "Principal": { "AWS": "arn:aws:iam::ACCOUNT:role/compute-a-role" },
      "Action": "s3files:Client*",
      "Condition": {
        "StringNotEquals": {
          "s3files:AccessPointArn": "arn:aws:s3files:REGION:ACCOUNT:file-system/fs-ID/access-point/fsap-ID"
        }
      }
    }
  ]
}
```

The role `compute-a-role` is allowed to mount and write only when the request targets `fsap-ID`, and is explicitly denied on every other access point on this file system. An explicit deny in a resource policy cannot be overridden by identity policies, so this restriction holds even if a broader IAM policy is attached to the role later.

**Mount command:**

```
sudo mount -t s3files -o accesspoint=fsap-ID fs-ID:/ /mnt/s3files
```

## Deny a workload access through any access point
<a name="s3-files-access-point-policy-deny"></a>

This pattern applies when a role shares an account with an S3 Files file system but must not mount it through any access point or directly. To block all access point usage, apply three layers ordered from strongest to weakest isolation guarantee.

**1. Network controls.** Remove the security group rule that grants `compute-b-role`'s instances access to the mount target on TCP port 2049. Network controls are the most resilient layer because they prevent the mount attempt before any credential exchange occurs. Even if a misconfigured policy grants mount permissions, the NFS connection cannot reach the mount target.

**2. Explicit deny in the file system policy.** A deny statement in the file system policy rejects the mount even if the role is granted broader IAM permissions later. A file system resource policy provides a deny that persists even if someone with `iam:PutRolePolicy` modifies the role's identity policies. Only principals with `s3files:PutFileSystemPolicy` can change this layer.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyComputeBOnFileSystem",
      "Effect": "Deny",
      "Principal": { "AWS": "arn:aws:iam::ACCOUNT:role/compute-b-role" },
      "Action": "s3files:Client*",
      "Resource": "*"
    }
  ]
}
```

**3. IAM identity policy.** Do not grant `s3files:Client*` permissions to the role. This is the final layer and the easiest to misconfigure, since any administrator with `iam:PutRolePolicy` can grant mount permissions to a role.

### Without a file system policy, any role can mount through any access point
<a name="s3-files-access-point-policy-deny-no-resource-policy"></a>

A file system resource policy provides a deny that cannot be removed by someone who only has permission to modify identity policies. Without a file system policy, any role with `s3files:ClientMount` in its identity policy can mount through any access point on the file system. We recommend that you attach a file system policy to every file system with a deny baseline, then add allow statements per workload.

## Best practices for access point isolation
<a name="s3-files-access-point-policy-best-practices"></a>

The following table summarizes recommended approaches for common access point isolation goals.


| Goal | Recommended approach | 
| --- | --- | 
| Restrict a workload to a single access point | Allow the role on the specific access point ARN, plus an explicit deny on every other access point. See "Restrict access to a specific access point." | 
| Block a role in the same account from mounting the file system | Remove network access to port 2049, deny in file system policy, and do not grant in IAM. | 
| Multiple workloads on the same file system, each scoped to their own access point | Maintain one allow \+ deny pair per role in the file system policy, each scoped to a different access point ARN. | 
| Cross-account access through an access point | Use the file system policy to grant the cross-account role on the specific access point ARN. Do not rely on identity policies alone. | 