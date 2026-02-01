Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Relocating a cluster

By using _relocation_ in Amazon Redshift, you allow Amazon Redshift to
move a cluster to another Availability Zone (AZ) without any loss of data or changes to your
applications. With relocation, you can continue operations when there is an interruption of
service on your cluster with minimal impact.

When cluster relocation is turned on, Amazon Redshift might choose to relocate clusters in some
situations. In particular, this happens where issues in the current Availability Zone
prevent optimal cluster operation or to improve service availability. You can also invoke
the relocation function in cases where resource constraints in a given Availability Zone are
disrupting cluster operations. An example is the ability to resume or resize a cluster.
Amazon Redshift offers the relocation feature at no extra charge.

When an Amazon Redshift cluster is relocated to a new Availability Zone, the new cluster has the
same endpoint as the original cluster. Your applications can reconnect to the endpoint and
continue operations without modifications or loss of data. However, relocation might not
always be possible due to potential resource constraints in a given Availability
Zone.

Amazon Redshift cluster relocation is supported for the RA3 instance types only.
RA3 instance types use Redshift Managed Storage
(RMS) as a durable storage layer. The latest copy of a cluster's data is always available in
other Availability Zones in an AWS Region. In other words, you can relocate an Amazon Redshift
cluster to another Availability Zone without any loss of data.

When you turn on relocation for your cluster, Amazon Redshift migrates your cluster to be behind
a proxy. Doing this helps implement location-independent access to a cluster's compute

resources. The migration causes the cluster to be rebooted. When a cluster is relocated to
another Availability Zone, an outage occurs while the new cluster is brought back online in
the new Availability Zone. However, you don't have to make any changes to your
applications because the cluster endpoint remains unchanged even after the cluster is
relocated to the new Availability Zone.

Cluster relocation is enabled by default on newly created or restored
RA3 clusters whose subnet group includes multiple Availability Zones. Amazon Redshift assigns
5439 as the default port while creating a provisioned cluster. You can change to another port from the port
range of 5431-5455 or 8191-8215. (Don't change to a port outside the ranges. It results in an error.) To change the default
port for a provisioned cluster, use the Amazon Redshift console, AWS CLI, or Amazon Redshift API. To change the default port for a
serverless workgroup, use the AWS CLI or the Amazon Redshift Serverless API.

If you turn on relocation and you currently use the leader node IP address to access your
your cluster or Enhanced VPC Routing, make sure to change that access. Instead, use the IP address associated with the
cluster's virtual private cloud (VPC) endpoint. To find this cluster IP address, find
and use the VPC endpoint in the **Network and security** section of the
cluster details page. To get more details on the VPC endpoint, sign in to the Amazon VPC console.

You can also use the AWS Command Line Interface (AWS CLI) command `describe-vpc-endpoints` to get
the elastic network interface associated with the endpoint. You can use the
`describe-network-interfaces` command to get the associated IP address. For
more information on Amazon Redshift AWS CLI commands, see [Available commands](../../../cli/latest/reference/redshift/index.md "../../../cli/latest/reference/redshift/index.md") in the
_AWS CLI Command Reference._

## Limitations

When using Amazon Redshift relocation, be aware of the following limitations:

- Cluster relocation might not be possible in all scenarios due to potential
  resource limitations in a given Availability Zone. If this happens, Amazon Redshift
  doesn't change the original cluster.
- Relocation isn't supported on DC2 instance families of products.
- You can't perform a relocation across AWS Regions.
- Amazon Redshift relocation defaults to port number 5439. You can also change to
  another port in the ranges 5431-5455 or 8191-8215.

## Managing relocation using the console

You can manage the settings for cluster relocation using the Amazon Redshift
console.

### Turning off relocation when creating a new

cluster

Use the following procedure to turn off relocation when creating a new
cluster.

###### To turn off relocation for a new cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**.
3. Choose **Create cluster** to create a new cluster. For more information on
   how to create a cluster, see [Get started with Amazon Redshift provisioned data warehouses](../gsg/new-user.md "../gsg/new-user.md") in
   _Amazon Redshift Getting Started Guide_.
4. Under **Backup**, for **Cluster
   relocation**, choose **Disabled**. Relocation
   is turned on by default.
5. Choose **Create cluster**.

### Modifying relocation for an existing cluster

Use the following procedure to change the relocation setting for an existing cluster.

###### To modify the relocation setting for an existing cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**. The clusters for your account in
   the current AWS Region are listed. A subset of properties of each cluster is
   displayed in columns in the list.
3. Choose the name of the cluster that you want to modify from the list. The cluster details page
   appears.
4. Choose the **Maintenance** tab, then in the **Backup details** section
   choose **Edit**.
5. Under **Backup**, choose **Disabled**. Relocation is turned on
   by default.
6. Choose **Modify cluster**.

### Relocating a cluster

Use the following procedure to manually relocate a cluster to another
Availability Zone. This is especially useful when you want to test your network
setup in secondary Availability Zones or when you are running into resource
constraints in the current Availability Zone.

###### To relocate a cluster to another Availability Zone

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**. The clusters for your account in
   the current AWS Region are listed. A subset of properties of each cluster is
   displayed in columns in the list.
3. Choose the name of the cluster that you want to move from the list. The cluster details page
   appears.
4. For **Actions**, choose **Relocate**. The **Relocate
   cluster** page appears.
5. (Optional) Choose an **Availability Zone**.
   If you don't choose an Availability Zone, Amazon Redshift chooses one for you.

Amazon Redshift starts the relocation and displays the cluster as relocating. After the
relocation completes, the cluster status changes to available.

## Managing relocation using the Amazon Redshift CLI

You can manage the settings for cluster relocation using the AWS
Command Line Interface (CLI).

With the AWS CLI, the following example command creates an Amazon Redshift cluster named
`mycluster` that has relocation turned on.

```
aws redshift create-cluster --cluster-identifier mycluster --number-of-nodes 2 --master-username `enter a username` --master-user-password `enter a password` --node-type ra3.4xlarge --port 5439 --no-availability-zone-relocation
```

If your current cluster is using a different port, you must modify it to use from the port range
of 5431-5455 or 8191-8215 before modifying it to turn on relocation. The default is 5439. The following example command
modifies the port in case your cluster doesn't use one from the given range.

```
aws redshift modify-cluster --cluster-identifier mycluster --port 5439
```

The following example command includes the availability-zone-relocation parameter on
the Amazon Redshift cluster.

```
aws redshift modify-cluster --cluster-identifier mycluster --availability-zone-relocation
```

The following example command turns off the availability-zone-relocation parameter on the Amazon Redshift cluster.

```
aws redshift modify-cluster --cluster-identifier mycluster --no-availability-zone-relocation
```

The following example command invokes relocation on the Amazon Redshift cluster.

```
aws redshift modify-cluster --cluster-identifier mycluster --availability-zone us-east-1b
```
