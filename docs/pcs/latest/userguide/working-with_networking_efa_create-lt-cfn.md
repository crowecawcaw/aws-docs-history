# (Optional) Use a CloudFormation

template to create an EFA-enabled launch template

Because there are several dependencies to setting up EFA, a CloudFormation template has been
provided that you can use to configure a compute node group. It supports instances with up to
four network cards. To learn more about instances with multiple network cards, see [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md#network-cards "../../../AWSEC2/latest/UserGuide/using-eni.md#network-cards") in the _Amazon Elastic Compute Cloud User Guide_.

Download the CloudFormation template from the following URL, then upload it to the
CloudFormation console in the AWS Region where you use AWS PCS.

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/enable_efa/assets/pcs-lt-efa.yaml
```

With the template open in the AWS CloudFormation console, enter the following values. Note that the
template will provide some default parameter values—you can leave them as
their default values.

- Under **Provide a stack name**
  - Under **Stack name**, enter a descriptive name. We recommend
    incorporating the name you will choose for your AWS PCS compute node group, such as
    ``NODEGROUPNAME`-efa-lt`.

- Under **Parameters**
  - Under **NumberOfNetworkCards**, choose the number of network cards in
    the instances that will be in your node group.
  - Under **VpcId**, choose the VPC where your AWS PCS cluster is
    deployed.
  - Under **NodeGroupSubnetId**, choose the subnet in your cluster VPC
    where EFA-enabled instances will be launched.
  - Under **PlacementGroupName**, leave the field blank to create a new
    cluster placement group for the node group. If you have an existing placement group you want
    to use, enter its name here.
  - Under **ClusterSecurityGroupId**, choose the security group you are
    using to allow access to other instances in the cluster and to the AWS PCS API. Many
    customers choose the default security group from their cluster VPC.
  - Under **SshSecurityGroupId**, provide the ID for a security group you
    are using to allow inbound SSH access to nodes in your cluster.
  - For **SshKeyName**, select the SSH keypair for access to nodes in your
    cluster.
  - For **LaunchTemplateName**, enter a descriptive name for the launch
    template such as ``NODEGROUPNAME`-efa-lt`. The name must
    be unique to your AWS account in the AWS Region where you will use AWS PCS.

- Under **Capabilities**
  - Check the box for **I acknowledge that AWS CloudFormation might create IAM
    resources**.
    Monitor the status of the CloudFormation stack. When it reaches
    `CREATE_COMPLETE` the launch template is ready to be used. Use it with an AWS PCS
    compute node group, as described above in [Create or update compute node
    groups for EFA](working-with_networking_efa_create-cng.md "working-with_networking_efa_create-cng.md").
