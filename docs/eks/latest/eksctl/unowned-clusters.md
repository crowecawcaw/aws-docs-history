# Non eksctl-created clusters

You can run `eksctl` commands against clusters which were
not created by `eksctl`.

###### Note

Eksctl can only support unowned clusters with names which are compatible with AWS CloudFormation. Any cluster names which do not match this will fail CloudFormation API validation check.

## Supported commands

The following commands can be used against clusters created by any means other than `eksctl`.
The commands, flags and config file options can be used in exactly the same way.

If we have missed some functionality, please [let us know](https://github.com/eksctl-io/eksctl/issues "https://github.com/eksctl-io/eksctl/issues").

- ✓ Create:
  - ✓ `eksctl create nodegroup` ([see note below](#create-nodegroup "#create-nodegroup"))
  - ✓ `eksctl create fargateprofile`
  - ✓ `eksctl create iamserviceaccount`
  - ✓ `eksctl create iamidentitymapping`

- ✓ Get:
  - ✓ `eksctl get clusters/cluster`
  - ✓ `eksctl get fargateprofile`
  - ✓ `eksctl get nodegroup`
  - ✓ `eksctl get labels`

- ✓ Delete:
  - ✓ `eksctl delete cluster`
  - ✓ `eksctl delete nodegroup`
  - ✓ `eksctl delete fargateprofile`
  - ✓ `eksctl delete iamserviceaccount`
  - ✓ `eksctl delete iamidentitymapping`

- ✓ Upgrade:
  - ✓ `eksctl upgrade cluster`
  - ✓ `eksctl upgrade nodegroup`

- ✓ Set/Unset:
  - ✓ `eksctl set labels`
  - ✓ `eksctl unset labels`

- ✓ Scale:
  - ✓ `eksctl scale nodegroup`

- ✓ Drain:
  - ✓ `eksctl drain nodegroup`

- ✓ Enable:
  - ✓ `eksctl enable profile`
  - ✓ `eksctl enable repo`

- ✓ Utils:
  - ✓ `eksctl utils associate-iam-oidc-provider`
  - ✓ `eksctl utils describe-stacks`
  - ✓ `eksctl utils install-vpc-controllers`
  - ✓ `eksctl utils nodegroup-health`
  - ✓ `eksctl utils set-public-access-cidrs`
  - ✓ `eksctl utils update-cluster-endpoints`
  - ✓ `eksctl utils update-cluster-logging`
  - ✓ `eksctl utils write-kubeconfig`
  - ✓ `eksctl utils update-coredns`
  - ✓ `eksctl utils update-aws-node`
  - ✓ `eksctl utils update-kube-proxy`

## Creating nodegroups

`eksctl create nodegroup` is the only command which requires specific input from the user.

Since users can create their clusters with any networking configuration they like,
for the time-being, `eksctl` will not attempt to retrieve or guess these values. This
may change in the future as we learn more about how people are using this command on non eksctl-created clusters.

This means that in order to create nodegroups or managed nodegroups on a cluster which was
not created by `eksctl`, a config file containing VPC details must be provided. At a minimum:

```
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: non-eksctl-created-cluster
  region: us-west-2

vpc:
  id: "vpc-12345"
  securityGroup: "sg-12345"    # this is the ControlPlaneSecurityGroup
  subnets:
    private:
      private1:
          id: "subnet-12345"
      private2:
          id: "subnet-67890"
    public:
      public1:
          id: "subnet-12345"
      public2:
          id: "subnet-67890"

...
```

Fore more information on VPC configuration options, see [Networking](networking.md "networking.md").
