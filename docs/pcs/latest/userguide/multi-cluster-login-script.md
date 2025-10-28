# Connecting a standalone login node to multiple

clusters in AWS PCS

The `pcs-multi-cluster-login-configure.sh` script provides an automated way to
configure multiple Slurm `sackd` daemons on a single standalone login node. It enables the
login node to communicate with multiple clusters. The script automates the following
operations:

- Uses AWS PCS API actions to get cluster information
- Prompts for the base64-encoded Slurm authentication key
- Creates a Slurm JWKS file with cluster authentication key
- Configures the `sackd` service with cluster endpoints and ports
- Creates a `systemd` service file for a cluster-specific `sackd` daemon
- Generates an activation script for cluster environment setup
- Enables and starts the `sackd` service

###### Note

This script requires Slurm version 25.05 or later.

Slurm must already be installed on the instance (equivalent to
[step 3](working-with_login-nodes_standalone_install-slurm.md "working-with_login-nodes_standalone_install-slurm.md") in the manual process).
The instance must be able to reach the target cluster's endpoints. The script performs the
equivalent operations of [step 4](working-with_login-nodes_standalone_get-secret.md "working-with_login-nodes_standalone_get-secret.md")
and [step 5](working-with_login-nodes_standalone_configure-connection.md "working-with_login-nodes_standalone_configure-connection.md") in the manual
configuration process. It automatically gets the cluster information, configures the `sackd` service,
creates the necessary `systemd` service files, and creates an activation script
that users can use to configure their shell environment for cluster interaction.

###### Topics

- [Prerequisites for the AWS PCS
  multi-cluster login node configuration script](multi-cluster-login-script-prerequisites.md "multi-cluster-login-script-prerequisites.md")
- [AWS PCS multi-cluster login node configuration
  script code](multi-cluster-login-script-code.md "multi-cluster-login-script-code.md")
- [Using the AWS PCS multi-cluster login
  node configuration script](multi-cluster-login-script-usage.md "multi-cluster-login-script-usage.md")
