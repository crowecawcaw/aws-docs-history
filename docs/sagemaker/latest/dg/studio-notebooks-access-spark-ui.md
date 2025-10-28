# Access Spark UI from Studio or

Studio Classic

The following sections give instructions for accessing the Spark UI from SageMaker AI
Studio or Studio Classic notebooks. The Spark UI allows you to monitor and debug your
Spark Jobs submitted to run on Amazon EMR from Studio or Studio Classic notebooks. SSH
tunneling and presigned URLs are two ways for accessing the Spark UI.

## Set up SSH tunneling for Spark

UI access

To set up SSH tunneling to access the Spark UI, follow one of the two options in
this section.

Options for setting up SSH tunneling:

- [Option 1: Set
  up an SSH tunnel to the master node using local port
  forwarding](../../../emr/latest/ManagementGuide/emr-ssh-tunnel-local.md "../../../emr/latest/ManagementGuide/emr-ssh-tunnel-local.md")
- [Option 2, part 1:
  Set up an SSH tunnel to the master node using dynamic port
  forwarding](../../../emr/latest/ManagementGuide/emr-ssh-tunnel.md "../../../emr/latest/ManagementGuide/emr-ssh-tunnel.md")

[Option 2, part 2: Configure proxy settings to view websites hosted on
the master node](../../../emr/latest/ManagementGuide/emr-connect-master-node-proxy.md "../../../emr/latest/ManagementGuide/emr-connect-master-node-proxy.md")

For information about viewing web interfaces hosted on Amazon EMR clusters, see [View web interfaces hosted on Amazon EMR Clusters](../../../emr/latest/ManagementGuide/emr-web-interfaces.md "../../../emr/latest/ManagementGuide/emr-web-interfaces.md"). You can also visit your
Amazon EMR console to get access to the Spark UI.

###### Note

You can set up an SSH tunnel even if presigned URLs are not available to you.

## Presigned

URLs

To create one-click URLs that can access Spark UI on Amazon EMR from SageMaker Studio
or Studio Classic notebooks, you must enable the following IAM permissions. Choose the
option that applies to you:

- **For Amazon EMR clusters that are in the same account as
  the SageMaker Studio or Studio Classic notebook: Add the following
  permissions to the SageMaker Studio or Studio Classic IAM execution role.**
- **For Amazon EMR clusters that are in a different account
  (not SageMaker Studio or Studio Classic notebook): Add the following
  permissions to the cross-account role that you created for [List Amazon EMR clusters from Studio or
  Studio Classic](discover-emr-clusters.md "discover-emr-clusters.md").**

###### Note

You can access presigned URLs from the console in the following
regions:

- US East (N. Virginia) Region
- US West (N. California) Region
- Canada (Central) Region
- Europe (Frankfurt) Region
- Europe (Stockholm) Region
- Europe (Ireland) Region
- Europe (London) Region
- Europe (Paris) Region
- Asia Pacific (Tokyo) Region
- Asia Pacific (Seoul) Region
- Asia Pacific (Sydney) Region
- Asia Pacific (Mumbai) Region
- Asia Pacific (Singapore) Region
- South America (São Paulo)

The following policy gives access to presigned URLs for your execution role.

```
{
        "Sid": "AllowPresignedUrl",
        "Effect": "Allow",
        "Action": [
            "elasticmapreduce:DescribeCluster",
            "elasticmapreduce:ListInstanceGroups",
            "elasticmapreduce:CreatePersistentAppUI",
            "elasticmapreduce:DescribePersistentAppUI",
            "elasticmapreduce:GetPersistentAppUIPresignedURL",
            "elasticmapreduce:GetOnClusterAppUIPresignedURL"
        ],
        "Resource": [
            "arn:aws:elasticmapreduce:`region`:`account-id`:cluster/*"
        ]
}
```
