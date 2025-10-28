Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Modifying a cluster

When you modify a cluster, changes to the following options are applied
immediately:

- **VPC security groups**
- **Publicly accessible**
- **Admin user password**
- **HSM Connection**
- **HSM Client Certificate**
- **Maintenance detail**
- **Snapshot preferences**
  Changes to the following options take effect only after the cluster is
  restarted:

- **Cluster identifier**

Amazon Redshift restarts the cluster automatically when you change **Cluster
identifier**.

- **Enhanced VPC routing**

Amazon Redshift restarts the cluster automatically when you change **Enhanced VPC
routing**.

- **Cluster parameter group**
- **IP address type**

This feature is only available in the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions. For more information on AWS Regions, see
[Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").
If you decrease the automated snapshot retention period, existing automated snapshots
whose settings fall outside of the new retention period are deleted. For more
information, see [Amazon Redshift snapshots and backups](working-with-snapshots.md "working-with-snapshots.md").

For more information about cluster properties, see [Additional
configurations](create-cluster.md#cluster-create-console-configuration "create-cluster.md#cluster-create-console-configuration").

###### To modify a cluster

1.  Sign in to the AWS Management Console and open the Amazon Redshift console at
    [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2.  On the navigation menu, choose **Clusters**.
3.  Choose the cluster to modify.
4.  Choose **Edit**. The **Edit cluster** page
    appears.
5.  Update the cluster properties. Some of the properties you can modify are:

        * Cluster identifier
        * Snapshot retention
        * Cluster relocation

    To edit settings for **Network and security**,
    **Maintenance**, and **Database
    configurations**, the console provides links to the appropriate
    cluster details tab.

6.  Choose **Save changes**.
