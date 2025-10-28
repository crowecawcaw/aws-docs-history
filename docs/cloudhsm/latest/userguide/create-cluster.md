# Create a cluster in AWS CloudHSM

A cluster is a collection of individual hardware security modules (HSMs). AWS CloudHSM
synchronizes the HSMs in each cluster so that they function as a logical unit. AWS CloudHSM offers
two types of HSMs: _hsm1.medium_ and _hsm2m.medium_.
When you create a cluster, you choose which of the two will be in your cluster. For details
on the differences between each HSM type and cluster mode, see [AWS CloudHSM cluster modes](cluster-hsm-types.md "cluster-hsm-types.md").

When you create a cluster, AWS CloudHSM creates a security group for the cluster on your behalf.
This security group controls network access to the HSMs in the cluster. It allows inbound
connections only from Amazon Elastic Compute Cloud (Amazon EC2) instances that are in the security group. By
default, the security group doesn't contain any instances. Later, you [launch a client instance](launch-client-instance.md "launch-client-instance.md") and [configure the cluster's security group](configure-sg.md "configure-sg.md") to allow
communication and connections with the HSM.

###### Considerations

- The following are some considerations when creating a cluster in AWS CloudHSM:

      + When you create a cluster, AWS CloudHSM creates a [service-linked
       role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") named AWSServiceRoleForCloudHSM. If AWS CloudHSM cannot create the
       role or the role does not already exist, you may not be able to create a
       cluster. For more information, see [Resolving AWS CloudHSM cluster creation
       failures](troubleshooting-create-cluster.md "troubleshooting-create-cluster.md"). For more information
       about service–linked roles, see [Service-linked roles for AWS CloudHSM](service-linked-roles.md "service-linked-roles.md").
      + If you are using the [AWS CloudHSM dual-stack endpoint](../../../general/latest/gr/cloudhsm.md "../../../general/latest/gr/cloudhsm.md")
       (that is, cloudhsmv2.`<region>`.api.aws),
       ensure that your IAM policies are updated to handle IPv6. For more
       information, see the [Upgrade IAM policies to
       IPv6 section under Security](ip-access.md "ip-access.md").

  You can create a cluster from the [AWS CloudHSM
  console](https://console.aws.amazon.com/cloudhsm/ "https://console.aws.amazon.com/cloudhsm/"), the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"), or the
  AWS CloudHSM API.

For details on cluster arguments and APIs, see [**create-cluster**](../../../cli/latest/reference/cloudhsmv2/create-cluster.md "../../../cli/latest/reference/cloudhsmv2/create-cluster.md") in the AWS CLI Command Reference.

Console

###### To create a cluster (console)

1.  Open the AWS CloudHSM console at
    [https://console.aws.amazon.com/cloudhsm/home](https://console.aws.amazon.com/cloudhsm/home "https://console.aws.amazon.com/cloudhsm/home").
2.  On the navigation bar, use the region selector to choose one of the
    [AWS Regions where
    AWS CloudHSM is currently supported](../../../general/latest/gr/rande.md#cloudhsm_region "../../../general/latest/gr/rande.md#cloudhsm_region").
3.  Choose **Create cluster**.
4.  In the **Cluster configuration** section, do the
    following:
    1. For **VPC**, select the VPC that you created
       in [Create a virtual private cloud (VPC) for AWS CloudHSM](create-vpc.md "create-vpc.md").
    2. For **Availability Zone(s)**, next to each
       Availability Zone, choose the private subnet that you created.

    ###### Note

    Even if AWS CloudHSM is not supported in a given Availability
    Zone, performance should not be affected, as AWS CloudHSM
    automatically load balances across all HSMs in a cluster.
    See [AWS CloudHSM
    Regions and Endpoints](../../../general/latest/gr/rande.md#cloudhsm_region "../../../general/latest/gr/rande.md#cloudhsm_region") in the
    _AWS General Reference_ to see Availability
    Zone support for AWS CloudHSM. 3. For **HSM type**, select the HSM type that
    can be created in your cluster along with the desired mode of
    the cluster. To see what HSM types are supported in each region,
    see the [AWS CloudHSM
    pricing calculator](https://aws.amazon.com/cloudhsm/pricing/ "https://aws.amazon.com/cloudhsm/pricing/").

    ###### Important

    After the cluster is created, the cluster mode cannot be
    changed. For information on which type and mode is right for
    your use case, see [AWS CloudHSM cluster modes](cluster-hsm-types.md "cluster-hsm-types.md"). 4. For **Network Type**, choose the IP address
    protocols for accessing your HSMs. IPv4 limits communication
    between your application and HSMs to IPv4 only. This is the
    default option. Dual-stack enables both IPv4 and IPv6
    communication. To use dual-stack, add both IPv4 and IPv6 CIDRs
    to your VPC and subnet configurations. The Network Type is
    difficult to change after initial setup. To modify it, create a
    backup of your existing cluster and restore a new cluster with
    the desired Network Type. For more information, see [Creating AWS CloudHSM clusters from backups](create-cluster-from-backup.md "create-cluster-from-backup.md") 5. For **Cluster source**, specify whether you
    want to create a new cluster or restore one from an existing
    backup.

        * Backups of clusters in non-FIPS mode can only be used to restore clusters that are in non-FIPS mode.
        * Backups of clusters in FIPS mode can only be used to restore clusters that are in FIPS mode.

5.  Choose **Next**.
6.  Specify how long the service should retain backups.
    1. Accept the default retention period of 90 days or type a new
       value between 7 and 379 days. The service will automatically
       delete backups in this cluster older than the value you specify
       here. You can change this later. For more information, see [Configure backup retention](manage-backup-retention.md "manage-backup-retention.md").

7.  Choose **Next**.
8.  (Optional) Type a tag key and an optional tag value. To add more than
    one tag to the cluster, choose **Add tag**.
9.  Choose **Review**.
10. Review your cluster configuration, and then choose **Create
    cluster**.

If your attempts to create a cluster fail, it might be related to problems
with the AWS CloudHSM service-linked roles. For help on resolving the failure, see
[Resolving AWS CloudHSM cluster creation
failures](troubleshooting-create-cluster.md "troubleshooting-create-cluster.md").

AWS CLI

###### To create a cluster ([AWS CLI](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"))

- At a command prompt, run the **[create-cluster](../../../cli/latest/reference/cloudhsmv2/create-cluster.md "../../../cli/latest/reference/cloudhsmv2/create-cluster.md")** command. Specify the HSM
  instance type, the backup retention period, and the subnet IDs of the
  subnets where you plan to create HSMs. Use the subnet IDs of the private
  subnets that you created. Specify only one subnet per Availability Zone.

```
`$` `aws cloudhsmv2 create-cluster --hsm-type hsm2m.medium \
 --backup-retention-policy Type=DAYS,Value=`<number of days>` \
 --subnet-ids `<subnet ID>` \
 --mode `<FIPS>` \
 --network-type `<IPV4>``
`{
 "Cluster": {
 "BackupPolicy": "DEFAULT",
 "BackupRetentionPolicy": {
 "Type": "DAYS",
 "Value": 90
 },
 "VpcId": "vpc-50ae0636",
 "SubnetMapping": {
 "us-west-2b": "subnet-49a1bc00",
 "us-west-2c": "subnet-6f950334",
 "us-west-2a": "subnet-fd54af9b"
 },
 "SecurityGroup": "sg-6cb2c216",
 "HsmType": "hsm2m.medium",
 "NetworkType": "IPV4",
 "Certificates": {},
 "State": "CREATE_IN_PROGRESS",
 "Hsms": [],
 "ClusterId": "cluster-igklspoyj5v",
 "ClusterMode": "FIPS",
 "CreateTimestamp": 1502423370.069
 }
}`

```

###### Note

`ClusterMode` is a required parameter for all hsm types
except hsm1.medium.`--mode`:

```
`$` `aws cloudhsmv2 create-cluster --hsm-type hsm2m.medium \
 --backup-retention-policy Type=DAYS,Value=`<number of days>` \
 --subnet-ids `<subnet ID>` \
 --mode NON_FIPS`
```

If your attempts to create a cluster fail, it might be related to problems
with the AWS CloudHSM service-linked roles. For help on resolving the failure, see
[Resolving AWS CloudHSM cluster creation
failures](troubleshooting-create-cluster.md "troubleshooting-create-cluster.md").

AWS CloudHSM API

###### To create a cluster (AWS CloudHSM API)

- Send a [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") request. Specify the HSM
  instance type, the backup retention policy, and the subnet IDs of the
  subnets where you plan to create HSMs. Use the subnet IDs of the private
  subnets that you created. Specify only one subnet per Availability
  Zone.

If your attempts to create a cluster fail, it might be related to problems
with the AWS CloudHSM service-linked roles. For help on resolving the failure, see
[Resolving AWS CloudHSM cluster creation
failures](troubleshooting-create-cluster.md "troubleshooting-create-cluster.md").
