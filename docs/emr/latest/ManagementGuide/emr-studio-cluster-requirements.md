# Amazon EMR cluster requirements

**Amazon EMR Clusters Running on Amazon EC2**

All Amazon EMR clusters running on Amazon EC2 that you create for an EMR Studio
Workspace must meet the following requirements. Clusters that you create using the
EMR Studio interface automatically meet these requirements.

- The cluster must use Amazon EMR versions 5.32.0 (Amazon EMR 5.x series) or 6.2.0 (Amazon EMR 6.x
  series) or later. You can create a cluster using the Amazon EMR console, AWS Command Line Interface, or SDK, and
  then attach it to an EMR Studio Workspace. Studio users can also
  provision and attach clusters when creating or working in an Amazon EMR Workspace. For
  more information, see [Attach a compute to an EMR Studio
  Workspace](emr-studio-create-use-clusters.md "emr-studio-create-use-clusters.md").
- The cluster must be within an Amazon Virtual Private Cloud. The EC2-Classic platform isn't
  supported.
- The cluster must have Spark, Livy, and Jupyter Enterprise Gateway installed. If you
  plan to use the cluster for SQL Explorer, you should install both Presto and
  Spark.
- To use SQL Explorer, the cluster must use Amazon EMR version 5.34.0 or later or
  version 6.4.0 or later and have Presto installed. If you want to specify the AWS Glue Data Catalog
  as the Hive metastore for Presto, you must configure it on the cluster. For more
  information, see [Using Presto with the
  AWS Glue Data Catalog](../ReleaseGuide/emr-presto-glue.md "../ReleaseGuide/emr-presto-glue.md").
- The cluster must be in a private subnet with network address translation (NAT) to use
  publicly-hosted Git repositories with EMR Studio.
  We recommend the following cluster configurations when you work with
  EMR Studio.

- Set deploy mode for Spark sessions to cluster mode. Cluster mode places the
  application master processes on the core nodes and not on the primary node of a cluster.
  Doing so relieves the primary node of potential memory pressures. For more information,
  see [Cluster Mode
  Overview](https://spark.apache.org/docs/latest/cluster-overview.html "https://spark.apache.org/docs/latest/cluster-overview.html") in the Apache Spark documentation.
- Change the Livy timeout from the default of one hour to six hours as in the following
  example configuration.

```
{
    "classification":"livy-conf",
        "Properties":{
            "livy.server.session.timeout":"6h",
            "livy.spark.deploy-mode":"cluster"
        }
}
```

- Create diverse instance fleets with up to 30 instances, and select multiple instance
  types in your Spot Instance fleet. For example, you might specify the following
  memory-optimized instance types for Spark workloads: r5.2x, r5.4x, r5.8x, r5.12x, r5.16x,
  r4.2x, r4.4x, r4.8x, r4.12, etc. For more information, see [Planning and configuring instance fleets for your Amazon EMR cluster](emr-instance-fleet.md "emr-instance-fleet.md").
- Use the capacity-optimized allocation strategy for Spot Instances to help Amazon EMR make
  effective instance selections based on real-time capacity insights from Amazon EC2. For more
  information, see [Allocation strategy for instance
  fleets](emr-instance-fleet.md#emr-instance-fleet-allocation-strategy "emr-instance-fleet.md#emr-instance-fleet-allocation-strategy").
- Enable managed scaling on your cluster. Set the maximum core nodes parameter to the
  minimum persistent capacity that you plan to use, and configure scaling on a
  well-diversified task fleet that runs on Spot Instances to save on costs. For more
  information, see [Using managed scaling in Amazon EMR](emr-managed-scaling.md "emr-managed-scaling.md").
  We also urge you to keep Amazon EMR Block Public Access enabled, and that to restrict inbound
  SSH traffic to trusted sources. Inbound access to a cluster lets users run notebooks on the
  cluster. For more information, see [Using Amazon EMR block public access](emr-block-public-access.md "emr-block-public-access.md") and [Control network traffic with security groups for your Amazon EMR cluster](emr-security-groups.md "emr-security-groups.md").

**Amazon EMR on EKS Clusters**

In addition to EMR clusters running on Amazon EC2, you can set up and manage Amazon EMR on EKS
clusters for EMR Studio using the AWS CLI. Set up Amazon EMR on EKS clusters using the following
guidelines:

- Create a managed HTTPS endpoint for the Amazon EMR on EKS cluster. Users attach a
  Workspace to a managed endpoint. The Amazon Elastic Kubernetes Service (EKS) cluster that you use to
  register a virtual cluster must have a private subnet to support managed endpoints.
- Use an Amazon EKS cluster with at least one private subnet and network address translation
  (NAT) when you want to use publicly-hosted Git repositories.
- Avoid using [Amazon EKS optimized Arm Amazon Linux
  AMIs](../../../eks/latest/userguide/eks-optimized-ami.md#arm-ami "../../../eks/latest/userguide/eks-optimized-ami.md#arm-ami"), which aren't supported for Amazon EMR on EKS managed endpoints.
- Avoid using AWS Fargate-only Amazon EKS clusters, which aren't supported.
