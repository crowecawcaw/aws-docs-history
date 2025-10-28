# Configure and create a cluster with the

PCUI

The PCUI is a web-based user interface that mirrors the AWS ParallelCluster
`pcluster` CLI, while providing a console-like experience. You install and access
the PCUI in your AWS account. When you run it, the PCUI accesses an instance of the
AWS ParallelCluster API hosted on Amazon API Gateway in your AWS account.

###### Note

The PCUI wizard may not have UI options for all the supported features in the
latest supported AWS ParallelCluster version. You can manually edit the configuration file as
needed or use the AWS ParallelCluster CLI.

This section guides you through how to configure and create a cluster using the PCUI.

###### Prerequisites:

- Access to a running instance of PCUI. For more information, see
  [Installing the PCUI](install-pcui-v3.md "install-pcui-v3.md").

###### Configure and create a cluster

1. In the PCUI **Clusters** view, choose **Create
   cluster**, **Step by step**.
2. In **Cluster**, **Name**, enter a name for your
   cluster.
3. Choose a **VPC** with a public subnet for your cluster, then choose
   **Next**.
4. In **Head node**, choose **Add SSM session**, then
   choose **Next**.
5. In **Queues**, **Compute resources**, choose **1** for **Static nodes**.
6. For **Instance type**, remove the selected default instance type,
   choose **t2.micro**, then choose **Next**.
7. In **Storage**, choose **Next**.
8. In **Cluster configuration**, review the cluster configuration YAML and
   choose **Dry run** to validate it.
9. Choose **Create** to create your cluster, based on the validated
   configuration.
10. After a few seconds, the PCUI automatically navigates you back to
    **Clusters**, where you can monitor the cluster create status and
    **Stack events**.
11. Choose **Details** to see cluster details, such as the version and
    status.
12. Choose **Instances** to see the list of Amazon EC2 instances and
    status.
13. Choose **Stack events** to view cluster stack events, and a AWS Management Console
    link to the CloudFormation stack that creates the cluster.
14. In **Details**, after cluster creation completes, choose **View
    YAML** to view or download the cluster configuration YAML file.
15. After cluster creation completes, choose **Shell** to access the
    cluster head node.

###### Note

When you choose **Shell**, AWS ParallelCluster opens an Amazon EC2 Systems Manager
session and adds an `ssm-user` to `/etc/sudoers`. For more
information, see [Turn on or turn off `ssm-user` account administrative permissions](../../../systems-manager/latest/userguide/session-manager-getting-started-ssm-user-permissions.md "../../../systems-manager/latest/userguide/session-manager-getting-started-ssm-user-permissions.md") in
the _Amazon EC2 Systems Manager User Guide_. 16. To clean up, in the **Clusters** view, select the cluster, and choose
**Actions**, **Delete cluster**.
