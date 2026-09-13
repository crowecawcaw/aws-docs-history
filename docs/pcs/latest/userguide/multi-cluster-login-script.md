

# Connecting a standalone login node to multiple clusters in AWS PCS
<a name="multi-cluster-login-script"></a>

The `pcs-multi-cluster-login-configure.sh` script provides an automated way to configure multiple Slurm `sackd` daemons on a single standalone login node. It enables the login node to communicate with multiple clusters. The script automates the following operations:
+ Uses AWS PCS API actions to get cluster information
+ Prompts for the base64-encoded Slurm authentication key
+ Creates a Slurm JWKS file with cluster authentication key
+ Configures the `sackd` service with cluster endpoints and ports
+ Creates a `systemd` service file for a cluster-specific `sackd` daemon
+ Generates an activation script for cluster environment setup
+ Enables and starts the `sackd` service

**Note**  
This script requires Slurm version 25.05 or later.

**Note**  
For Slurm 25.11 or later, you can use `sackd --jwks-file <path>` and `sackd --key-file <path>` to specify authentication key paths instead of the `SLURM_SACK_JWKS` environment variable. The `SLURM_SACK_JWKS` approach remains supported for backward compatibility with Slurm 25.05 clusters.

Slurm must already be installed on the instance (equivalent to [step 3](working-with_login-nodes_standalone_install-slurm.md) in the manual process). The instance must be able to reach the target cluster's endpoints. The script performs the equivalent operations of [step 4](working-with_login-nodes_standalone_get-secret.md) and [step 5](working-with_login-nodes_standalone_configure-connection.md) in the manual configuration process. It automatically gets the cluster information, configures the `sackd` service, creates the necessary `systemd` service files, and creates an activation script that users can use to configure their shell environment for cluster interaction.

By default, the script calls the AWS PCS API to look up the cluster's details. To skip that call, supply the details directly on the command line with the `--cluster-name`, `--cluster-id`, `--slurm-version`, and `--endpoints` options. When you provide all four, the script makes no AWS PCS API call. This is useful for a login node that has no route to the AWS PCS API endpoint or no AWS credentials. The `--fetch-secret` option is an exception: It always calls the AWS PCS API to read the secret's ARN.

You run the script once for each cluster, so a single standalone login node can connect to several clusters at the same time. The login node must be able to reach each cluster's `slurmctld` controller. If two clusters have the same name, use the `--alias` option to give each one a distinct local identifier on the login node. For clusters in different AWS Regions, use the `--region` option to specify each cluster's Region. The login node must have a private network path to that Region's `slurmctld` controller. For example, you can use a VPC peering connection or a transit gateway.

**Topics**
+ [Prerequisites for the AWS PCS multi-cluster login node configuration script](multi-cluster-login-script-prerequisites.md)
+ [AWS PCS multi-cluster login node configuration script code](multi-cluster-login-script-code.md)
+ [Using the AWS PCS multi-cluster login node configuration script](multi-cluster-login-script-usage.md)