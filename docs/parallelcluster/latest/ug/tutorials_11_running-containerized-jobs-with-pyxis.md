# Running containerized

jobs with Pyxis

Learn how to create a cluster that is able to run containerized jobs using Pyxis, which is
a SPANK plugin to manage containerized jobs in SLURM. Containers in Pyxis are managed by
Enroot, which is tool to turn traditional container/OS images into unprivileged sandboxes.
For more information, see [NVIDIA Pyxis](https://github.com/NVIDIA/pyxis "https://github.com/NVIDIA/pyxis")
and [NVIDIA Enroot](https://github.com/NVIDIA/enroot "https://github.com/NVIDIA/enroot").

###### Note

- This feature is available with AWS ParallelCluster v3.11.1
- The scripts in this tutorial move (`mv`) some files, which deletes them
  from their original locations. If you want to keep copies of these files in their
  original locations, change the scripts to use the copy (`cp`) command
  instead.
  When using AWS ParallelCluster, you only pay for
  the AWS resources that are created when you create or update AWS ParallelCluster images and clusters. For more information,
  see [AWS services used by AWS ParallelCluster](aws-services-v3.md "aws-services-v3.md").

###### Prerequisites:

- The AWS CLI is [installed and configured.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- An [Amazon EC2 key pair.](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").
- An IAM role with the [permissions](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") that are required to run the[pcluster CLI.](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md")

## Create the cluster

Starting with AWS ParallelCluster 3.11.1, all official AMIs comes with Pyxis and Enroot
pre-installed. In particular, SLURM is recompiled with Pyxis support and Enroot is
installed as a binary in the system. However, you must to configure them according to
your specific needs. The folders used by Enroot and Pyxis will have a critical impact on cluster performance. For more
information, see [Pyxis
documentation](https://github.com/NVIDIA/pyxis/wiki/Setup#slurm-plugstack-configuration "https://github.com/NVIDIA/pyxis/wiki/Setup#slurm-plugstack-configuration") and [Enroot
documentation.](https://github.com/NVIDIA/pyxis/wiki/Setup#enroot-configuration-example "https://github.com/NVIDIA/pyxis/wiki/Setup#enroot-configuration-example")

For your convenience, you can find sample configurations for both Pyxis, Enroot and
SPANK within `/opt/parallelcluster/examples/`.

To deploy a cluster using the sample configurations we have provided, complete the
following tutorial.

To create the cluster with sample configuration

Pyxis and Enroot must be configured on the head node by first creating the
persistent and volatile directories for Enroot, then creating the runtime directory
for Pyxis, and finally enabling Pyxis as SPANK plugin in the whole cluster.

1. Execute the below script as [OnNodeConfigured](HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeConfigured "HeadNode-v3.md#yaml-HeadNode-CustomActions-OnNodeConfigured")
   custom action in the head node to configure Pyxis and Enroot on the head node.

```

#!/bin/bash
set -e

echo "Executing $0"

# Configure Enroot
ENROOT_PERSISTENT_DIR="/var/enroot"
ENROOT_VOLATILE_DIR="/run/enroot"

sudo mkdir -p $ENROOT_PERSISTENT_DIR
sudo chmod 1777 $ENROOT_PERSISTENT_DIR
sudo mkdir -p $ENROOT_VOLATILE_DIR
sudo chmod 1777 $ENROOT_VOLATILE_DIR
sudo mv /opt/parallelcluster/examples/enroot/enroot.conf /etc/enroot/enroot.conf
sudo chmod 0644 /etc/enroot/enroot.conf

# Configure Pyxis
PYXIS_RUNTIME_DIR="/run/pyxis"

sudo mkdir -p $PYXIS_RUNTIME_DIR
sudo chmod 1777 $PYXIS_RUNTIME_DIR

sudo mkdir -p /opt/slurm/etc/plugstack.conf.d/
sudo mv /opt/parallelcluster/examples/spank/plugstack.conf /opt/slurm/etc/
sudo mv /opt/parallelcluster/examples/pyxis/pyxis.conf /opt/slurm/etc/plugstack.conf.d/
sudo -i scontrol reconfigure

```

2. Pyxis and Enroot must be configured on the compute fleet by creating the
   persistent and volatile directories for Enroot and the runtime directory for
   Pyxis. Execute the below script as [OnNodeStart](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart")
   custom action in compute nodes to configure Pyxis and Enroot on the compute fleet.

```

#!/bin/bash
set -e

echo "Executing $0"

# Configure Enroot
ENROOT_PERSISTENT_DIR="/var/enroot"
ENROOT_VOLATILE_DIR="/run/enroot"
ENROOT_CONF_DIR="/etc/enroot"

sudo mkdir -p $ENROOT_PERSISTENT_DIR
sudo chmod 1777 $ENROOT_PERSISTENT_DIR
sudo mkdir -p $ENROOT_VOLATILE_DIR
sudo chmod 1777 $ENROOT_VOLATILE_DIR
sudo mkdir -p $ENROOT_CONF_DIR
sudo chmod 1777 $ENROOT_CONF_DIR
sudo mv /opt/parallelcluster/examples/enroot/enroot.conf /etc/enroot/enroot.conf
sudo chmod 0644 /etc/enroot/enroot.conf

# Configure Pyxis
PYXIS_RUNTIME_DIR="/run/pyxis"

sudo mkdir -p $PYXIS_RUNTIME_DIR
sudo chmod 1777 $PYXIS_RUNTIME_DIR

# In Ubuntu24.04 Apparmor blocks the creation of unprivileged user namespaces,
# which is required by Enroot. So to run Enroot, it is required to disable this restriction.
# See https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces
source /etc/os-release
if [ "${ID}${VERSION_ID}" == "ubuntu24.04" ]; then
    echo "kernel.apparmor_restrict_unprivileged_userns = 0" | sudo tee /etc/sysctl.d/99-pcluster-disable-apparmor-restrict-unprivileged-userns.conf
    sudo sysctl --system
fi
```

## Submit jobs

Now that Pyxis is configured in your cluster, you can submit containerized jobs using
the sbatch and srun command, that are now enriched with container specific
options.

```

# Submitting an interactive job
srun -N 2 --container-image docker://ubuntu:22.04 hostname

# Submitting a batch job
sbatch -N 2 --wrap='srun --container-image docker://ubuntu:22.04 hostname'

```
