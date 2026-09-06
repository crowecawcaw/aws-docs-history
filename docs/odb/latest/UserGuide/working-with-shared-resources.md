

# Working with shared Oracle Database@AWS resources in a trusted account
<a name="working-with-shared-resources"></a>

After a resource has been shared with your trusted account and you've initialized the Oracle Database@AWS service, you can view and use the shared resource. This topic explains how to work with shared resources in a trusted account.

**Topics**
+ [Limitations for shared resources in a trusted account](#limitations-shared-resources)
+ [Creating VM clusters on shared Exadata infrastructure](#creating-vm-clusters)
+ [Viewing shared resources in a trusted account](#viewing-shared-resources)
+ [Setting up ODB peering with shared ODB networks](#network-peering-shared)

## Limitations for shared resources in a trusted account
<a name="limitations-shared-resources"></a>

When working with shared Oracle Database@AWS resources, be aware of the following limitations:
+ Resource sharing is supported only within the same AWS organization.
+ Only the buyer account (the account that accepts the Oracle Database@AWS private offer) can create Exadata infrastructure and ODB network resources.
+ You can create resources only on shared infrastructure and only if you have the necessary permissions.
+ The specific actions (managed permissions) for each resource type are automatically selected during resource share creation and can't be modified.
+ You can't modify or delete resources owned by another account.
+ Resources that you create on shared infrastructure are owned by your account and count toward your OCI quotas. The same applies to parent resources.
+ If the owner account unshares a resource, you can no longer create new resources on this shared infrastructure. However, your existing resources continue to function.
+ Cross-Region resource sharing isn't supported. You can only share resources within the same AWS Region.
+ Trusted account resources are billed to the buyer of the Oracle Database@AWS subscription.
+ When using a resource that is shared, you must provide the Amazon Resource Name (ARN).

## Creating VM clusters on shared Exadata infrastructure
<a name="creating-vm-clusters"></a>

If your trusted account has access to a shared Exadata infrastructure and ODB network, you can create Exadata VM clusters, Autonomous VM clusters, or ODB peerings on this infrastructure.

**Note**  
When using a resource that is shared to you, instead of only specifying the resource ID, you must specify the Amazon Resource Name (ARN).

### Console
<a name="creating-vm-clusters.CON"></a>

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/).

1. In the navigation pane, choose **Exadata VM clusters** or **Autonomous VM clusters**.

1. Choose **Create VM cluster** or **Create Autonomous VM cluster**.

1. For **Exadata infrastructure**, select the shared Exadata infrastructure on which you want to create the VM cluster.

1. Complete the remaining fields as required for your VM cluster configuration.

1. Choose **Create VM cluster** or **Create Autonomous VM cluster**.

### AWS CLI
<a name="creating-vm-clusters.CLI"></a>

To create a VM cluster on shared Exadata infrastructure using the AWS CLI, use the `create-cloud-vm-cluster` command:

```
aws odb create-cloud-vm-cluster --region us-east-1 \
    --cloud-exadata-infrastructure-id {{arn:aws:odb:us-east-1:111111111111:cloud-exadata-infrastructure/exa_aaaaaaaaaa}} \
    --odb-network-id {{arn:aws:odb:us-east-1:111111111111:odb-network/odbnet_aaaaaaaaaa}} \
    --cpu-core-count {{4}} \
    --display-name "{{Shared-VMC-1}}" \
    --gi-version "{{19.0.0.0}}" \
    --hostname "{{vmchost}}" \
    --ssh-public-keys "{{ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...}}" \
```

To create an Autonomous VM cluster on shared Exadata infrastructure using the AWS CLI, use the `create-cloud-vm-cluster` command:

```
aws odb create-cloud-autonomous-vm-cluster --region us-east-1  \
    --cloud-exadata-infrastructure-id {{arn:aws:odb:us-east-1:111111111111:cloud-exadata-infrastructure/exa_aaaaaaaaaa}} \
    --odb-network-id {{arn:aws:odb:us-east-1:111111111111:odb-network/odbnet_aaaaaaaaaa}}\
    --display-name "{{Shared-AVMC-1}}" \
    --autonomous-data-storage-size-in-tbs {{8}} \
    --cpu-core-count-per-node {{16}}
```

The VM cluster is created on the specified shared Exadata infrastructure and is owned by your trusted account.

## Viewing shared resources in a trusted account
<a name="viewing-shared-resources"></a>

You can view resources that have been shared with your account using the AWS Management Console or the AWS CLI.

### Console
<a name="viewing-shared-resources.CON"></a>

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/).

1. In the navigation pane, choose the resource type you want to view: **Exadata infrastructure** or **ODB network**.

1. The console displays resources shared with you.

1. Select a shared resource to view its details.

### AWS CLI
<a name="viewing-shared-resources.CLI"></a>

To view shared resources using the AWS CLI, use the appropriate `list` command for the resource type. For example, to list Exadata infrastructure:

```
aws odb list-cloud-exadata-infrastructures
```

The response shows resources shared with you.

To get detailed information about a specific shared resource, use the appropriate `get` command with the resource ID:

```
aws odb get-cloud-exadata-infrastructure --cloud-exadata-infrastructure-id {{exa_infra_1}}
```

## Setting up ODB peering with shared ODB networks
<a name="network-peering-shared"></a>

To enable communication between your applications and databases on shared ODB networks, you can set up ODB peering between your VPC and the shared ODB network. For more information about ODB peering, see [Creating an ODB peering connection in Oracle Database@AWS](configuring.md#network-peering).

### Console
<a name="network-peering-shared.CON"></a>

1. Open the Oracle Database@AWS console at [https://console.aws.amazon.com/odb/](https://console.aws.amazon.com/odb/).

1. In the navigation pane, choose **ODB peering**.

1. Choose **Create ODB network peering**.

1. For **ODB network**, select the shared ODB network you want to peer with.

1. For **Peer network**, select your VPC.

1. Choose **Create ODB network peering**.

### AWS CLI
<a name="network-peering-shared.CLI"></a>

To create a network peering connection between your VPC and a shared ODB network using the AWS CLI, use the `create-odb-peering-connection` command.

```
aws odb create-odb-peering-connection \
    --odb-network-id {{odbnet_1234567890abcdef}} \
    --peer-network-id {{vpc-abcdef1234567890}}
```

After creating the peering connection, update your route tables to enable traffic between the peered networks.

```
aws ec2 create-route \
    --route-table-id {{rtb-1234567890abcdef}} \
    --destination-cidr-block {{10.0.0.0/16}} \
    --odb-network-arn {{arn:aws:odb:us-east-1:111111111111:odb-network/odbnet_1234567890abcdef}}
```