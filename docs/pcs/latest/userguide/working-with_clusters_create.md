# Creating a cluster in AWS PCS

This topic provides an overview of available options and describes what to consider when you
create a cluster in AWS Parallel Computing Service (AWS PCS). If this is your first time creating an AWS PCS cluster, we recommend
you follow [Get started with AWS Parallel Computing Service](getting-started.md "getting-started.md"). The tutorial can help
you create a working HPC system without expanding into all the available options and
system architectures that are possible.

###### Note

After creating a cluster, you can modify many configuration settings without rebuilding your infrastructure. For more information, see [Updating a cluster in AWS PCS](working-with_clusters_update.md "working-with_clusters_update.md").

###### Note

You can configure custom Slurm settings to implement advanced scheduling policies and resource management. For more information, see [Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md "slurm-custom-settings.md").

## Prerequisites

- An existing VPC and subnet that meet [AWS PCS Networking](working-with_networking.md "working-with_networking.md") requirements. Before you deploy a cluster for
  production use, we recommend that you have a thorough understanding of the VPC and subnet
  requirements. To create a VPC and subnet, see [Creating a VPC for your AWS PCS
  cluster](working-with_networking_create-vpc.md "working-with_networking_create-vpc.md").
- An [IAM principal](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") with
  permissions to create and manage AWS PCS resources. For more information, see [Identity and Access Management for AWS Parallel Computing Service](security-iam.md "security-iam.md").

## Create an AWS PCS cluster

You can use the AWS Management Console or AWS CLI to create a cluster.

AWS Management Console

###### To create a cluster

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/home#/clusters](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters") and choose **Create
   cluster**.
2. In the **Cluster setup** section, enter the following fields:
   - Cluster name – A name for your cluster. The name can
     contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an
     alphabetic character and can't be longer than 40 characters. The name must be unique
     within the AWS Region and AWS account that you're creating the cluster in.
   - Scheduler – Choose a scheduler and version.
     For more information, see [Slurm versions in AWS PCS](slurm-versions.md "slurm-versions.md").
   - Controller size – Choose a size for your controller.
     This determines how many concurrent jobs and compute nodes can be managed by the
     AWS PCS cluster. You can only set the controller size when the cluster is created. For
     more information on sizing, see [Cluster size in AWS PCS](working-with_clusters_size.md "working-with_clusters_size.md").

3. In the **Networking** section, select values for the following
   fields:
   - Network type – Choose the IP address type for your
     cluster. Your cluster can use either IPv4 or IPv6, but not both. The VPC and subnets must
     use the same network address type. The IP address block you use for each subnet
     must have at least 1 available address. AWS reserves some of the addresses in each
     subnet. For more information, see [Subnet CIDR blocks](../../../vpc/latest/userguide/subnet-sizing.md "../../../vpc/latest/userguide/subnet-sizing.md")
     in the _Amazon VPC User Guide_.
   - VPC – Choose an existing VPC that meets AWS PCS
     requirements. For more information, see [AWS PCS VPC and subnet requirements
     and considerations](working-with_networking_vpc-requirements.md "working-with_networking_vpc-requirements.md"). After you create the cluster,
     you can't change its VPC. If no VPCs are listed, you must create one first.
   - Subnet – All available subnets in the selected VPC
     are listed. Choose a subnet that meets the
     AWS PCS subnet requirements. For more information, see [AWS PCS VPC and subnet requirements
     and considerations](working-with_networking_vpc-requirements.md "working-with_networking_vpc-requirements.md"). We recommend you select
     a private subnet to avoid exposing your scheduler endpoints to the public internet.
   - Security groups – Specify the security group(s) that
     you want AWS PCS to associate with the network interfaces it creates for your cluster.
     You must select at least one security group that allows communication between your cluster
     and its compute nodes. You can select **Quick create a security group** to have AWS PCS create one with the necessary configuration in your selected VPC, or select an existing security group. For more information, see [Security group requirements
     and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements "working-with_networking_sg.md#working-with_networking_sg-requirements").

4. (Optional) In the **Slurm accounting configuration** section, you can
   enable Slurm accounting and set accounting parameters. For more information, see
   [Slurm accounting in AWS PCS](slurm-accounting.md "slurm-accounting.md").
5. (Optional) In the **Slurm configuration** section, you can add parameter name and value pairs to configure additional Slurm settings. For a complete list of supported parameters, see [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md "slurm-custom-settings-cluster.md").
6. (Optional) Under **Tags**, add any tags to your AWS PCS cluster.
7. Choose **Create cluster**. The **Status**
   field shows `Creating` while the AWS PCS creates the cluster.
   This process can take several minutes.

###### Important

There can only be 1 cluster in a `Creating` state per AWS Region
per AWS account.
AWS PCS returns an error if there is already a cluster in a `Creating`
state when you try to create a cluster.

AWS CLI

###### To create a cluster

1. Create your cluster with the command that follows. Before running the command, make
   the following replacements:
   - Replace `region` with the ID of the AWS Region that you want to
     create your cluster in, such as `us-east-1`.
   - Replace `my-cluster` with a name for your cluster. The name
     can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with
     an alphabetic character and can't be longer than 40 characters. The name must be unique
     within the AWS Region and AWS account where you're creating the cluster.
   - Replace `25.05` with any supported version of Slurm.

   ###### Note

   AWS PCS currently supports Slurm 25.05, 24.11 and 24.05.
   - Replace `SMALL` with any supported cluster size. This
     determines how many concurrent jobs and compute nodes can be managed by the AWS PCS
     cluster. It can only be set when the cluster is created. For more information on sizing,
     see [Cluster size in AWS PCS](working-with_clusters_size.md "working-with_clusters_size.md").
   - Replace the value for `subnetIds` with your own. We recommend you select
     a private subnet to avoid exposing your scheduler endpoints to the public internet.
   - Specify the `securityGroupIds` that you want AWS PCS to associate with
     the network interfaces it creates for your cluster. The security groups must be in the
     same VPC as the cluster. You must select at least one security
     group that allows communication between your cluster and its compute nodes. For more
     information, see [Security group requirements
     and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements "working-with_networking_sg.md#working-with_networking_sg-requirements").

```
aws pcs create-cluster --region `region` \
    --cluster-name `my-cluster` \
    --scheduler type=SLURM,version=`25.05` \
    --size `SMALL` \
    --networking subnetIds=`subnet-ExampleId1`,securityGroupIds=`sg-ExampleId1`
```

    * to use IPv6, add `networkType=IPV6` to the `--networking` configuration.



    ```
      --networking **networkType=IPV6**,subnetIds=`subnet-ExampleId1`,securityGroupIds=`sg-ExampleId1`
    ```


    * Optionally, you can add the `--slurm-configration` option
     to customize the Slurm behavior and specify Slurm configuration options.
     The following example sets the scale-down idle time to 60 minutes (3600 seconds),
     enables Slurm accounting, and specifies `slurm.conf` settings as
     the value for `slurmCustomSettings`.
     For more information, see [Slurm accounting in AWS PCS](slurm-accounting.md "slurm-accounting.md").


    ###### Note

    Accounting is supported for Slurm 24.11 or later.



    ```
    aws pcs create-cluster --region `region` \
        --cluster-name `my-cluster` \
        --scheduler type=SLURM,version=`25.05` \
        --size `SMALL` \
        --networking subnetIds=`subnet-ExampleId1`,securityGroupIds=`sg-ExampleId1`
        **--slurm-configuration scaleDownIdleTimeInSeconds=3600,accounting='{mode=STANDARD}',slurmCustomSettings='[{parameterName=SelectTypeParameters,parameterValue=CR\_CPU\_Memory}]'**
    ```

2. It can take several minutes to provision the cluster. You can query the status of your
   cluster with the following command. Don’t proceed to creating queues or compute node groups
   until the cluster’s status field is `ACTIVE`.

```
aws pcs get-cluster --region `region` --cluster-identifier `my-cluster`
```

###### Important

There can only be 1 cluster in a `Creating` state per AWS Region
per AWS account.
AWS PCS returns an error if there is already a cluster in a `Creating`
state when you try to create a cluster.

###### Recommended next steps for your cluster

- Add compute node groups.
- Add queues.
- Enable logging.
