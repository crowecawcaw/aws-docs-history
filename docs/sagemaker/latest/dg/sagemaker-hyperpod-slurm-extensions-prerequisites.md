

# Prerequisites and IAM permissions for cluster extensions
+ **Slurm orchestration with continuous provisioning** – Your cluster uses Slurm orchestration with `NodeProvisioningMode` set to `Continuous`. A lifecycle script isn't required. For more information, see [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md). Requests for other clusters fail with a `ValidationException`.
+ **A supported AMI** – Every instance group in the cluster uses a SageMaker HyperPod default AMI released on or after November 2, 2026. Cluster extensions don't support custom AMIs. If an instance group uses an older AMI, run `update-cluster-software` to move it to the latest default AMI, and then create the extension. For more information, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software). Requests for clusters that don't meet this requirement fail with a `ValidationException`.
+ **IAM permissions to manage extensions** – Your IAM principal has the permissions described in the following section.
+ **IAM permissions for the cluster nodes** – Each instance group's execution role has the permissions that the extension needs. Health reporting needs only the Amazon CloudWatch Logs permissions in the `AmazonSageMakerClusterInstanceRolePolicy` AWS managed policy. Each extension's page lists any others.

The cluster doesn't need to be `InService` when you create an extension. If the cluster is still being created, HyperPod applies the extension to each node as the node comes up.

## IAM permissions to manage extensions
<a name="sagemaker-hyperpod-slurm-extensions-prerequisites-iam-permissions-to-manage-extensions"></a>

Your policy must allow `CreateClusterExtension`, `DescribeClusterExtension`, `UpdateClusterExtension`, and `DeleteClusterExtension` on both the cluster ARN and the extension ARN. `ListClusterExtensions` needs only the cluster ARN, and `ListClusterExtensionVersions` needs `*`. For every action, resource type, and condition key, see [Actions, resources, and condition keys for Amazon SageMaker AI](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html) in the *Service Authorization Reference*.

Each extension has its own ARN, so you can scope a policy to one extension on a cluster. For example, you can allow `sagemaker-observability` but not `sagemaker-user-management`.

The following example policy allows a principal to manage both extensions on one cluster.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListClusterExtensions",
      "Effect": "Allow",
      "Action": "sagemaker:ListClusterExtensions",
      "Resource": "arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh"
    },
    {
      "Sid": "ListClusterExtensionVersions",
      "Effect": "Allow",
      "Action": "sagemaker:ListClusterExtensionVersions",
      "Resource": "*"
    },
    {
      "Sid": "ManageClusterExtensions",
      "Effect": "Allow",
      "Action": [
        "sagemaker:CreateClusterExtension",
        "sagemaker:DescribeClusterExtension",
        "sagemaker:UpdateClusterExtension",
        "sagemaker:DeleteClusterExtension"
      ],
      "Resource": [
        "arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh",
        "arn:aws:sagemaker:us-west-2:111122223333:extension/sagemaker-abcd1234efgh/sagemaker-observability/*",
        "arn:aws:sagemaker:us-west-2:111122223333:extension/sagemaker-abcd1234efgh/sagemaker-user-management/*"
      ]
    }
  ]
}
```

Replace *us-west-2*, *111122223333*, and *abcd1234efgh* with your AWS Region, account ID, and cluster ID. Keep `*` at the end of each extension ARN, because the extension ID changes when you delete and create an extension again.

To give read-only access, for example to a security auditor, allow only `DescribeClusterExtension` and `ListClusterExtensions` on the same resources, and `ListClusterExtensionVersions` on `*`.

Most principals also need `sagemaker:DescribeCluster` to get the cluster ARN, and CloudWatch read permissions to view extension health. The `AmazonSageMakerFullAccess` AWS managed policy includes all `sagemaker` actions. Attach it only to cluster administrators, never to a cluster's execution role.

## Who should have extension permissions
<a name="sagemaker-hyperpod-slurm-extensions-prerequisites-who-should-have-extension-permissions"></a>

A cluster extension installs and runs software as root on your cluster's nodes. A principal that can call `CreateClusterExtension`, `UpdateClusterExtension`, or `DeleteClusterExtension` on a cluster can change that software, so treat these permissions as cluster administrator permissions. The following list describes who should have them.
+ **Cluster administrators only** – Grant them only to the IAM users or roles that administer the cluster.
+ **Never the execution role** – Don't grant them to the cluster's execution role. SageMaker HyperPod makes the execution role's credentials available on the nodes, so every user who can log in to the cluster can use them. For guidance and an example deny policy, see [AWS Identity and Access Management for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md) in *IAM for SageMaker HyperPod*.
+ **Read-only actions more widely** – `DescribeClusterExtension`, `ListClusterExtensions`, and `ListClusterExtensionVersions` are read-only, and you can grant them more widely.