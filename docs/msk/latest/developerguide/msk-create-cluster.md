# Create an MSK Provisioned cluster

###### Important

You can't change the VPC for an MSK Provisioned cluster after you create the cluster.

Before you can create an MSK Provisioned cluster, you need to have an
Amazon Virtual Private Cloud (VPC) and set up subnets within that VPC.

For Standard brokers in the US West (N. California) Region, you need two subnets
in two different Availability Zones. In all other Regions where Amazon MSK is available, you
can specify either two or three subnets. Your subnets must all be in different
Availability Zones. For Express brokers, you need three subnets in three different Availability Zones. When you create an MSK Provisioned cluster, Amazon MSK distributes the broker nodes evenly
over the subnets that you specify.

###### Topics

- [Create an MSK Provisioned cluster using the AWS Management Console](create-cluster-console.md "create-cluster-console.md")
- [Create a provisioned Amazon MSK cluster using the AWS CLI](create-cluster-cli.md "create-cluster-cli.md")
- [Create an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI](create-cluster-cli-custom-config.md "create-cluster-cli-custom-config.md")
- [Create an MSK Provisioned cluster using the Amazon MSK
  API](create-cluster-api.md "create-cluster-api.md")
