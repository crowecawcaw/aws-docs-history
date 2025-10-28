# Cluster upgrades

An _`eksctl`-managed_ cluster can be upgraded in 3 easy steps:

1. upgrade control plane version with `eksctl upgrade cluster`
2. upgrade nodegroups
3. update the default networking add-ons (For more information, see [Default add-on updates](addon-upgrade.md "addon-upgrade.md")):
   Carefully review cluster upgrade related resources:

- [Update existing cluster to new Kubernetes version](../userguide/update-cluster.md "../userguide/update-cluster.md") in the Amazon EKS User Guide
- [Best Practices for Cluster Upgrades](../best-practices/cluster-upgrades.md "../best-practices/cluster-upgrades.md") in the EKS Best Practices Guide

###### Note

The old `eksctl update cluster` will be deprecated. Use `eksctl upgrade cluster` instead.

## Updating control plane version

Control plane version upgrades must be done for one minor version at a time.

To upgrade control plane to the next available version run:

```
eksctl upgrade cluster --name=<clusterName>
```

This command will not apply any changes right away, you will need to re-run it with
`--approve` to apply the changes.

The target version for the cluster upgrade can be specified both with the CLI flag:

```
eksctl upgrade cluster --name=<clusterName> --version=1.16
```

or with the config file

```
cat cluster1.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: cluster-1
  region: eu-north-1
  version: "1.16"

eksctl upgrade cluster --config-file cluster1.yaml
```

###### Warning

The only values allowed for the `--version` and `metadata.version` arguments are the current version of the cluster
or one version higher. Upgrades of more than one Kubernetes version are not supported.
