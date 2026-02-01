Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Associating IAM

roles with clusters

After you have created an IAM role that authorizes Amazon Redshift to access other AWS
services for you, you must associate that role with an Amazon Redshift cluster. You must
do this before you can use the role to load or unload data.

## Permissions required to associate an IAM role with a cluster

To associate an IAM role with a cluster, a user must have
`iam:PassRole` permission for that IAM role. This permission
allows an administrator to restrict which IAM roles a user can associate with
Amazon Redshift clusters. As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

The following example shows an IAM policy that can be attached to a user that
allows the user to take these actions:

- Get the details for all Amazon Redshift clusters owned by that user's
  account.
- Associate any of three IAM roles with either of two Amazon Redshift
  clusters.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "redshift:DescribeClusters",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "redshift:ModifyClusterIamRoles",
 "redshift:CreateCluster"
 ],
 "Resource": [
 "arn:aws:redshift:us-east-1:123456789012:cluster:my-redshift-cluster",
 "arn:aws:redshift:us-east-1:123456789012:cluster:my-second-redshift-cluster"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::123456789012:role/MyRedshiftRole",
 "arn:aws:iam::123456789012:role/SecondRedshiftRole",
 "arn:aws:iam::123456789012:role/ThirdRedshiftRole"
 ]
 }
 ]
}`

```

After a user has the appropriate permissions, that user can associate an IAM
role with an Amazon Redshift cluster. The IAM role is then ready to use with the COPY
or UNLOAD command or other Amazon Redshift commands.

For more information on IAM policies, see [Overview of IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in
the _IAM User Guide_.

## Managing IAM role

association with a cluster

You can associate an IAM role with an Amazon Redshift cluster when you create the
cluster. Or you can modify an existing cluster and add or remove one or more IAM
role associations.

Be aware of the following:

- The maximum number of IAM roles that you can associate is subject to
  a quota.
- An IAM role can be associated with multiple Amazon Redshift clusters.
- An IAM role can be associated with an Amazon Redshift cluster only if both the
  IAM role and the cluster are owned by the same AWS account.

You can manage IAM role associations for a cluster with the console by
using the following procedure.

###### To manage IAM role associations

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then
   choose the cluster that you want to update.
3. For **Actions**, choose **Manage IAM
   roles** to display the current list IAM roles
   associated with the cluster.
4. On the **Manage IAM roles** page, choose the
   available IAM roles to add, and then choose **Add IAM
   role**.
5. Choose **Done** to save your changes.

You can manage IAM role associations for a cluster with the AWS CLI by using
the following approaches.

To associate an IAM role with a cluster when the cluster is created,
specify the Amazon Resource Name (ARN) of the IAM role for the
`--iam-role-arns` parameter of the
`create-cluster` command. The maximum number of IAM
roles that you can add when calling the `create-cluster`
command is subject to a quota.

Associating and disassociating IAM roles with Amazon Redshift clusters is an
asynchronous process. You can get the status of all IAM role cluster
associations by calling the `describe-clusters`
command.

The following example associates two IAM roles with the newly created
cluster named `my-redshift-cluster`.

```
aws redshift create-cluster \
    --cluster-identifier "my-redshift-cluster" \
    --node-type "ra3.4xlarge" \
    --number-of-nodes 16 \
    --iam-role-arns "arn:aws:iam::123456789012:role/RedshiftCopyUnload" \
                    "arn:aws:iam::123456789012:role/SecondRedshiftRole"
```

To associate an IAM role with an existing Amazon Redshift cluster, specify
the Amazon Resource Name (ARN) of the IAM role for the
`--add-iam-roles` parameter of the
`modify-cluster-iam-roles` command. The maximum number of
IAM roles that you can add when calling the
`modify-cluster-iam-roles` command is subject to a quota.

The following example associates an IAM role with an existing cluster
named `my-redshift-cluster`.

```
aws redshift modify-cluster-iam-roles \
    --cluster-identifier "my-redshift-cluster" \
    --add-iam-roles "arn:aws:iam::123456789012:role/RedshiftCopyUnload"
```

To disassociate an IAM role from a cluster, specify the ARN of the IAM
role for the `--remove-iam-roles` parameter of the
`modify-cluster-iam-roles` command.
`modify-cluster-iam-roles` The maximum number of IAM
roles that you can remove when calling the
`modify-cluster-iam-roles` command is subject to a
quota.

The following example removes the association for an IAM role for the
`123456789012` AWS account from a cluster named
`my-redshift-cluster`.

```
aws redshift modify-cluster-iam-roles \
    --cluster-identifier "my-redshift-cluster" \
    --remove-iam-roles "arn:aws:iam::123456789012:role/RedshiftCopyUnload"
```

### Listing IAM role associations for a cluster using the

AWS CLI

To list all of the IAM roles that are associated with an Amazon Redshift
cluster, and the status of the IAM role association, call the
`describe-clusters` command. The ARN for each IAM role
associated with the cluster is returned in the `IamRoles`
list as shown in the following example output.

Roles that have been associated with the cluster show a status of
`in-sync`. Roles that are in the process of being
associated with the cluster show a status of `adding`. Roles
that are being disassociated from the cluster show a status of
`removing`.

```

{
    "Clusters": [
        {
            "ClusterIdentifier": "my-redshift-cluster",
            "NodeType": "ra3.4xlarge",
            "NumberOfNodes": 16,
            "IamRoles": [
                {
                    "IamRoleArn": "arn:aws:iam::123456789012:role/MyRedshiftRole",
                    "IamRoleApplyStatus": "in-sync"
                },
                {
                    "IamRoleArn": "arn:aws:iam::123456789012:role/SecondRedshiftRole",
                    "IamRoleApplyStatus": "in-sync"
                }
            ],
            ...
        },
        {
            "ClusterIdentifier": "my-second-redshift-cluster",
            "NodeType": "ra3.4xlarge",
            "NumberOfNodes": 10,
            "IamRoles": [
                {
                    "IamRoleArn": "arn:aws:iam::123456789012:role/MyRedshiftRole",
                    "IamRoleApplyStatus": "in-sync"
                },
                {
                    "IamRoleArn": "arn:aws:iam::123456789012:role/SecondRedshiftRole",
                    "IamRoleApplyStatus": "in-sync"
                },
                {
                    "IamRoleArn": "arn:aws:iam::123456789012:role/ThirdRedshiftRole",
                    "IamRoleApplyStatus": "in-sync"
                }
            ],
            ...
        }
    ]
}

```

For more information on using the AWS CLI, see _[AWS CLI User
Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md")_.
