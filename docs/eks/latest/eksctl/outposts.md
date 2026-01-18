# AWS Outposts Support

###### Warning

EKS Managed Nodegroups are not supported on Outposts.

## Extending existing clusters to AWS Outposts

You can extend an existing EKS cluster running in an AWS region to
AWS Outposts by setting `nodeGroup.outpostARN` for new nodegroups to
create nodegroups on Outposts, as in:

```
 # extended-cluster.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: existing-cluster
  region: us-west-2

nodeGroups:
  # Nodegroup will be created in an AWS region.
  - name: ng

  # Nodegroup will be created on the specified Outpost.
  - name: outpost-ng
    privateNetworking: true
    outpostARN: "arn:aws:outposts:us-west-2:1234:outpost/op-1234"
```

```
 eksctl create nodegroup -f extended-cluster.yaml
```

In this setup, the EKS control plane runs in an AWS region while
nodegroups with `outpostARN` set run on the specified Outpost. When a
nodegroup is being created on Outposts for the first time, eksctl
extends the VPC by creating subnets on the specified Outpost. These
subnets are used to create nodegroups that have `outpostARN` set.

Customers with a pre-existing VPC are required to create the subnets on
Outposts and pass them in `nodeGroup.subnets`, as in:

```
 # extended-cluster-vpc.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: extended-cluster-vpc
  region: us-west-2

vpc:
  id: vpc-1234
    subnets:
      private:
        outpost-subnet-1:
          id: subnet-1234

nodeGroups:
  # Nodegroup will be created in an AWS region.
  - name: ng

  # Nodegroup will be created on the specified Outpost.
  - name: outpost-ng
    privateNetworking: true
    # Subnet IDs for subnets created on Outpost.
    subnets: [subnet-5678]
    outpostARN: "arn:aws:outposts:us-west-2:1234:outpost/op-1234"
```

## Creating a local cluster on AWS Outposts

###### Note

Local clusters support Outpost racks only.

###### Note

Only Amazon Linux 2 is supported for nodegroups when the
control plane is on Outposts. Only EBS gp2 volume types are supported
for nodegroups on Outposts.

[AWS Outposts](../userguide/eks-outposts.md "../userguide/eks-outposts.md") support in eksctl lets you create local clusters with the
entire Kubernetes cluster, including the EKS control plane and worker
nodes, running locally on AWS Outposts. Customers can either create a
local cluster with both the EKS control plane and worker nodes running
locally on AWS Outposts, or they can extend an existing EKS cluster
running in an AWS region to AWS Outposts by creating worker nodes on
Outposts.

To create the EKS control plane and nodegroups on AWS Outposts, set
`outpost.controlPlaneOutpostARN` to the Outpost ARN, as in:

```
 # outpost.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: outpost
  region: us-west-2

outpost:
  # Required.
  controlPlaneOutpostARN: "arn:aws:outposts:us-west-2:1234:outpost/op-1234"
  # Optional, defaults to the smallest available instance type on the Outpost.
  controlPlaneInstanceType: m5d.large
```

```
 eksctl create cluster -f outpost.yaml
```

This instructs eksctl to create the EKS control plane and subnets on the
specified Outpost. Since an Outposts rack exists in a single
availability zone, eksctl creates only one public and private subnet.
eksctl does not associate the created VPC with a
[local gateway](../../../outposts/latest/userguide/outposts-local-gateways.md "../../../outposts/latest/userguide/outposts-local-gateways.md") and, as such, eksctl will lack connectivity to the API server
and will be unable to create nodegroups. Therefore, if the
`ClusterConfig` contains any nodegroups during cluster creation, the
command must be run with `--without-nodegroup`, as in:

```
 eksctl create cluster -f outpost.yaml --without-nodegroup
```

It is the customer’s responsibility to associate the eksctl-created VPC
with the local gateway after cluster creation to enable connectivity to
the API server. After this step, nodegroups can be created using
`eksctl create nodegroup`.

You can optionally specify the instance type for the control plane nodes
in `outpost.controlPlaneInstanceType` or for the nodegroups in
`nodeGroup.instanceType`, but the instance type must exist on Outpost
or eksctl will return an error. By default, eksctl attempts to choose
the smallest available instance type on Outpost for the control plane
nodes and nodegroups.

When the control plane is on Outposts, nodegroups are created on that
Outpost. You can optionally specify the Outpost ARN for the nodegroup in
`nodeGroup.outpostARN` but it must match the control plane’s Outpost
ARN.

```
 # outpost-fully-private.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: outpost-fully-private
  region: us-west-2

privateCluster:
  enabled: true

outpost:
  # Required.
  controlPlaneOutpostARN: "arn:aws:outposts:us-west-2:1234:outpost/op-1234"
  # Optional, defaults to the smallest available instance type on the Outpost.
  controlPlaneInstanceType: m5d.large
```

```
 # outpost.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: outpost
  region: us-west-2

outpost:
  # Required.
  controlPlaneOutpostARN: "arn:aws:outposts:us-west-2:1234:outpost/op-1234"
  # Optional, defaults to the smallest available instance type on the Outpost.
  controlPlaneInstanceType: m5d.large

  controlPlanePlacement:
    groupName: placement-group-name
```

### Existing VPC

Customers with an existing VPC can create local clusters on AWS Outposts
by specifying the subnet configuration in `vpc.subnets`, as in:

```
 # outpost-existing-vpc.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: outpost
  region: us-west-2

vpc:
  id: vpc-1234
  subnets:
    private:
      outpost-subnet-1:
        id: subnet-1234

nodeGroups:
  - name: outpost-ng
    privateNetworking: true

outpost:
    # Required.
    controlPlaneOutpostARN: "arn:aws:outposts:us-west-2:1234:outpost/op-1234"
    # Optional, defaults to the smallest available instance type on the Outpost.
    controlPlaneInstanceType: m5d.large
```

```
 eksctl create cluster -f outpost-existing-vpc.yaml
```

The subnets must exist on the Outpost specified in
`outpost.controlPlaneOutpostARN` or eksctl will return an error. You
can also specify nodegroups during cluster creation if you have access
to the local gateway for the subnet, or have connectivity to VPC
resources.

## Features unsupported on local clusters

- [Addons](addons.md "addons.md")
- [IAM Roles for Service Accounts](iamserviceaccounts.md "iamserviceaccounts.md")
- [IPv6](vpc-ip-family.md "vpc-ip-family.md")
- [Identity Providers](https://github.com/eksctl-io/eksctl/blob/main/examples/27-oidc-provider.yaml "https://github.com/eksctl-io/eksctl/blob/main/examples/27-oidc-provider.yaml")
- [Fargate](fargate.md "fargate.md")
- [KMS Encryption](kms-encryption.md "kms-encryption.md")
- [Local Zones](https://github.com/eksctl-io/eksctl/blob/main/examples/33-local-zones.yaml "https://github.com/eksctl-io/eksctl/blob/main/examples/33-local-zones.yaml")
- [Karpenter](eksctl-karpenter.md "eksctl-karpenter.md")
- [Instance Selector](instance-selector.md "instance-selector.md")
- Availability Zones cannot be specified as it defaults to the Outpost
  availability zone.
- `vpc.publicAccessCIDRs` and `vpc.autoAllocateIPv6` are not
  supported.
- Public endpoint access to the API server is not supported as a local
  cluster can only be created with private-only endpoint access.

## Further information

- [Amazon EKS on AWS Outposts](../userguide/eks-outposts.md "../userguide/eks-outposts.md")
- [Local clusters for Amazon EKS on AWS Outposts](../userguide/eks-outposts-local-cluster-overview.md "../userguide/eks-outposts-local-cluster-overview.md")
- [Creating local clusters](../userguide/eks-outposts-local-cluster-create.md "../userguide/eks-outposts-local-cluster-create.md")
- [Launching self-managed Amazon Linux nodes on an Outpost](../userguide/eks-outposts-self-managed-nodes.md "../userguide/eks-outposts-self-managed-nodes.md")
