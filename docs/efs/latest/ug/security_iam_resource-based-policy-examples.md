# Resource-based policy

examples for Amazon EFS

In this section, you can find example file system policies that grant or deny
permissions for various Amazon EFS actions. EFS file system policies have a 20,000
character limit. For information about the elements of a resource-based policy, see [Resource-based
policies within Amazon EFS](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies").

###### Important

If you grant permission to an individual IAM user or role in a file system policy,
don't delete or recreate that user or role while the policy is in effect on the
file system. If this happens, that user or role is effectively locked out from file
system and will not be able to access it. For more information, see [Specifying a Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#Principal_specifying "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#Principal_specifying") in the _IAM User Guide_.

For information about how to create a file system policy, see [Creating file system policies](create-file-system-policy.md "create-file-system-policy.md").

###### Topics

- [Example: Grant read and write access to a
  specific AWS role](#file-sys-policy-readonly "#file-sys-policy-readonly")
- [Example: Grant read-only access](#file-sys-policy-readonly "#file-sys-policy-readonly")
- [Example: Grant access to an
  EFS access point](#file-sys-policy-accessprofile-efs "#file-sys-policy-accessprofile-efs")

## Example: Grant read and write access to a

specific AWS role

In this example, the EFS file system policy has the following
characteristics:

- The effect is `Allow`.
- The principal is set to the Testing_Role in the AWS account.
- The action is set to `ClientMount` (read), and
  `ClientWrite`.
- The condition for granting permissions is set to
  `AccessedViaMountTarget`.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/Testing_Role"
            },
            "Action": [
                "elasticfilesystem:ClientWrite",
                "elasticfilesystem:ClientMount"
            ],
            "Resource": "arn:aws:elasticfilesystem:us-east-2:111122223333:file-system/fs-1234abcd",
            "Condition": {
                "Bool": {
                    "elasticfilesystem:AccessedViaMountTarget": "true"
                }
            }
        }
    ]
}
```

## Example: Grant read-only access

The following file system policy only grants `ClientMount`, or read-only,
permissions to the `EfsReadOnly` IAM role.

```
{
    "Id": "read-only-example-policy02",
    "Statement": [
        {
            "Sid": "efs-statement-example02",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/EfsReadOnly"
            },
            "Action": [
                "elasticfilesystem:ClientMount"
            ],
            "Resource": "arn:aws:elasticfilesystem:us-east-2:111122223333:file-system/fs-12345678"
        }
    ]
}
```

To learn how to set additional file system policies, including denying root access to
all IAM principals, except for a specific management workstation, see [Enable root squashing using IAM authorization for NFS clients](accessing-fs-nfs-permissions.md#enable-root-squashing "accessing-fs-nfs-permissions.md#enable-root-squashing").

## Example: Grant access to an

EFS access point

You use an EFS access policy to provide an NFS client with an
application-specific view into shared file-based datasets on an EFS file
system. You grant the access point permissions on the file system using a file system
policy.

This file policy example uses a condition element to grant a specific access point
that is identified by its ARN full access to the file system.

For more information about using EFS access points, see [Working with access points](efs-access-points.md "efs-access-points.md").

```
{
    "Id": "access-point-example03",
    "Statement": [
        {
            "Sid": "access-point-statement-example03",
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::555555555555:role/EfsAccessPointFullAccess"},
            "Action": "elasticfilesystem:Client*",
            "Resource": "arn:aws:elasticfilesystem:us-east-2:111122223333:file-system/fs-12345678",
            "Condition": {
                "StringEquals": {
                    "elasticfilesystem:AccessPointArn":"arn:aws:elasticfilesystem:us-east-2:555555555555:access-point/fsap-12345678" }
            }
        }
    ]
}
```
