

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

**Topics**
+ [Prerequisites for the AWS PCS multi-cluster login node configuration script](multi-cluster-login-script-prerequisites.md)
+ [AWS PCS multi-cluster login node configuration script code](multi-cluster-login-script-code.md)
+ [Using the AWS PCS multi-cluster login node configuration script](multi-cluster-login-script-usage.md)