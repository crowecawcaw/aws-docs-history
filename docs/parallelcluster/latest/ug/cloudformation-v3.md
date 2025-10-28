# AWS CloudFormation custom resource

Starting with AWS ParallelCluster version 3.6.0, you can use an AWS ParallelCluster CloudFormation custom resource in an AWS CloudFormation stack. The custom
resource is an AWS ParallelCluster hosted stack. This way, you can use CloudFormation to configure and manage your clusters. For example, you can
configure cluster external resources such as network, shared storage, and security group infrastructure in a CloudFormation stack. Furthermore, you can
manage your cluster with a CloudFormation infrastructure as code pipeline.

Add an AWS ParallelCluster custom resource to your CloudFormation template by doing the following:

1. Add a custom resource provider stack that is owned and hosted by AWS ParallelCluster.
2. Reference the provider stack in your CloudFormation template as a custom resource.
   The custom resource provider stack handles and responds to CloudFormation requests. For example, when you deploy your CloudFormation stack,
   you also configure and create a cluster. To update a cluster, you update your CloudFormation stack. You delete a cluster when you delete your stack. For more information about
   CloudFormation custom resources, see [Custom resources](../../../AWSCloudFormation/latest/UserGuide/template-custom-resources.md "../../../AWSCloudFormation/latest/UserGuide/template-custom-resources.md") in the
   _AWS CloudFormation User Guide_.

###### Warning

CloudFormation doesn't detect custom resource drift. Only use CloudFormation to update the cluster configuration and to delete a cluster.

You can use the [pcluster](pcluster-v3.md "pcluster-v3.md") CLI or the [AWS ParallelCluster UI](pcui-using-v3.md "pcui-using-v3.md") to monitor
the state of the cluster or to update the compute fleet, but you must not use them to update the cluster configuration or to delete the cluster.

###### Note

We recommend that you add [termination
protection](../../../AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.md") to your stack to avoid accidental removal.
