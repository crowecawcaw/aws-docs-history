**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create an EKS Auto Mode Cluster with the eksctl CLI

This topic shows you how to create an Amazon EKS Auto Mode cluster using the eksctl command line interface (CLI). You can create an Auto Mode cluster either by running a single CLI command or by applying a YAML configuration file. Both methods provide the same functionality, with the YAML approach offering more granular control over cluster settings.

The eksctl CLI simplifies the process of creating and managing EKS Auto Mode clusters by handling the underlying AWS resource creation and configuration. Before proceeding, ensure you have the necessary AWS credentials and permissions configured on your local machine. This guide assumes you’re familiar with basic Amazon EKS concepts and have already installed the required CLI tools.

###### Note

You must install version `0.195.0` or greater of eksctl. For more information, see [eksctl releases](https://github.com/eksctl-io/eksctl/releases "https://github.com/eksctl-io/eksctl/releases") on GitHub.

## Create an EKS Auto Mode cluster with a CLI command

You must have the `aws` and `eksctl` tools installed. You must be logged into the AWS CLI with sufficent permissions to manage AWS resources including: EC2 instances, EC2 networking, EKS clusters, and IAM roles. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").

Run the following command to create a new EKS Auto Mode cluster with

```
 eksctl create cluster --name=<cluster-name> --enable-auto-mode
```

## Create an EKS Auto Mode cluster with a YAML file

You must have the `aws` and `eksctl` tools installed. You must be logged into the AWS CLI with sufficent permissions to manage AWS resources including: EC2 instances, EC2 networking, EKS clusters, and IAM roles. For more information, see [Set up to use Amazon EKS](setting-up.md "setting-up.md").

Review the EKS Auto Mode configuration options in the sample ClusterConfig resource below. For the full ClusterConfig specification, see the [eksctl documentation](https://eksctl.io/usage/creating-and-managing-clusters/ "https://eksctl.io/usage/creating-and-managing-clusters/").

AWS suggests enabling EKS Auto Mode. If this is your first time creating an EKS Auto Mode cluster, leave the `nodeRoleARN` unspecified to create a Node IAM Role for EKS Auto Mode. If you already have a Node IAM Role in your AWS account, AWS suggests reusing it.

AWS suggests not specifying any value for `nodePools`. EKS Auto Mode will create default node pools. You can use the Kubernetes API to create additional node pools.

```
 # cluster.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: <cluster-name>
  region: <aws-region>

iam:
  # ARN of the Cluster IAM Role
  # optional, eksctl creates a new role if not supplied
  # suggested to use one Cluster IAM Role per account
  serviceRoleARN: <arn-cluster-iam-role>

autoModeConfig:
  # defaults to false
  enabled: boolean
  # optional, defaults to [general-purpose, system].
  # suggested to leave unspecified
  # To disable creation of nodePools, set it to the empty array ([]).
  nodePools: []string
  # optional, eksctl creates a new role if this is not supplied
  # and nodePools are present.
  nodeRoleARN: string
```

Save the `ClusterConfig` file as `cluster.yaml`, and use the following command to create the cluster:

```
 eksctl create cluster -f cluster.yaml
```
