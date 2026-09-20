

# Patch the operating system of a cluster
<a name="patching-cluster-v3"></a>

This tutorial shows how to apply operating system updates to the nodes of a running AWS ParallelCluster cluster by building a patched AMI and updating the cluster to use it, without recreating the cluster from scratch.

The procedure has three steps:

1. Build a patched AMI that includes the OS updates.

1. Update the compute and login fleet to use the patched AMI.

   This launches new instances from the patched AMI to replace the existing nodes.

1. Apply the same patching strategy to the head node.

   The head node AMI can't be replaced, so the head node must be patched in place and then rebooted.

Steps 1 and 3 both apply OS updates to a node with the same commands, defined in [Patch a node](#patch-a-node-v3).

**Cluster downtime**  
This procedure implies cluster downtime due to compute and login nodes replacement and head node reboot.

## Step 1: Build a patched AMI
<a name="patching-cluster-build-ami-v3"></a>

Build a custom AMI that includes the OS updates:

1. Launch an instance from the AMI your cluster currently uses.

1. Patch the instance by running the commands in [Patch a node](#patch-a-node-v3).

1. Create a new AMI from the patched instance.

Note the ID of the resulting patched AMI, for example `ami-123456789`, as you will use it in the next step.

## Step 2: Update the compute and login nodes to the patched AMI
<a name="patching-cluster-update-fleet-v3"></a>

**Note**  
Login nodes must be stopped for their image change to take effect. Set the login pool [`Count`](LoginNodes-v3.md#yaml-LoginNodes-Pools-Count) to `0`, apply the update, then restore `Count` to its original value and apply the update again.

1. To replace the compute and login nodes without stopping the compute fleet, set [`SlurmSettings`](Scheduling-v3.md#Scheduling-v3-SlurmSettings) / [`QueueUpdateStrategy`](Scheduling-v3.md#yaml-Scheduling-SlurmSettings-QueueUpdateStrategy) to `DRAIN` in your cluster configuration.

1. In your cluster configuration, set the patched AMI as the custom AMI for the compute queues and the login node pools:
   + [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`Image`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Image) / [`CustomAmi`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Image-CustomAmi)
   + [`Pools`](LoginNodes-v3.md#LoginNodes-v3-Pools) / [`Image`](LoginNodes-v3.md#yaml-LoginNodes-Pools-Image) / [`CustomAmi`](LoginNodes-v3.md#yaml-LoginNodes-Pools-Image-CustomAmi)

1. Apply the changes with the [`pcluster update-cluster`](pcluster.update-cluster-v3.md) command.

1. This update replaces the compute nodes with instances that run the patched AMI and recreates the login nodes from the patched AMI.

## Step 3: Patch the head node
<a name="patching-cluster-head-node-v3"></a>

The head node is a static instance, so you patch it in place and then reboot it.

1. Connect to the head node.

1. Patch the head node by running the commands in [Patch a node](#patch-a-node-v3).

1. Wait for the head node to become reachable over SSH again.

## Patch a node
<a name="patch-a-node-v3"></a>

Apply all available OS updates with the node's package manager, using the commands for the node's operating system. These commands are used both when building a patched AMI ([Step 1: Build a patched AMI](#patching-cluster-build-ami-v3)) and when patching the head node ([Step 3: Patch the head node](#patching-cluster-head-node-v3)).

**Kernel compatibility with the Lustre client**  
Upgrading the kernel past the newest version that the FSx for Lustre client supports breaks FSx mounts after the reboot.  
To prevent this, cap the kernel at the newest version the Lustre client supports. The commands below assume that version; set `kernel_cap` to the newest kernel your Lustre client supports. Amazon Linux 2023 ships the Lustre module in-tree with the kernel, so no cap is needed.   
For more information, see [Installing the Lustre client](https://docs.aws.amazon.com/fsx/latest/LustreGuide/install-lustre-client.html) in the *FSx for Lustre User Guide*.

**Amazon Linux 2023**

```
# Refresh the package manager cache.
sudo dnf clean all
sudo dnf makecache --refresh -y

# No kernel cap needed: the Lustre module ships in-tree with the kernel.

# Apply all available updates.
sudo dnf upgrade -y
```

**RHEL 8, RHEL 9, Rocky Linux 8, and Rocky Linux 9**

```
# Refresh the package manager cache.
sudo dnf clean all
sudo dnf makecache --refresh -y

# Determine the kernel cap: the newest kernel version supported by the FSx for Lustre client.
# We assume 5.14.0-503.11.1.el9_5.x86_64; set kernel_cap to the newest kernel your Lustre client supports.
kernel_cap=5.14.0-503.11.1.el9_5.x86_64

# Cap the kernel at that version and version-lock it.
sudo dnf install -y python3-dnf-plugin-versionlock
sudo dnf versionlock add "kernel-${kernel_cap}" "kernel-core-${kernel_cap}" "kernel-modules-${kernel_cap}" "kernel-modules-core-${kernel_cap}" "kernel-tools-${kernel_cap}"

# Apply all available updates.
sudo dnf upgrade -y

# Refresh the Lustre client for the kernel about to boot.
new_kernel=$(rpm -q kernel --qf '%{VERSION}-%{RELEASE}.%{ARCH}\n' | sort -V | tail -n1)
if ! modinfo -k "$new_kernel" lustre >/dev/null 2>&1; then
  sudo sed -i -E "s#(/el/)[0-9]+(\.[0-9]+)?#\1$(. /etc/os-release && echo "$VERSION_ID")#" /etc/yum.repos.d/aws-fsx.repo
  sudo dnf clean metadata
  sudo dnf upgrade -y kmod-lustre-client lustre-client
fi
```

**Ubuntu 22.04 and 24.04**

```
# Refresh the package manager cache.
sudo DEBIAN_FRONTEND=noninteractive apt-get update -y

# Determine the kernel cap: the newest kernel version supported by the FSx for Lustre client.
# We assume 6.8.0-1021-aws; set kernel_cap to the newest kernel your Lustre client supports.
kernel_cap=6.8.0-1021-aws

# Cap the kernel at that version and version-lock it.
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y "linux-image-${kernel_cap}" "linux-headers-${kernel_cap}" "linux-modules-${kernel_cap}"
# linux-modules-extra carries the InfiniBand/RDMA modules and ships separately only up to
# the 6.17 series; from the 7.0.0 series those modules are folded into linux-modules (installed above)
# and linux-modules-extra is no longer published.
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y "linux-modules-extra-${kernel_cap}" \
    || echo "WARNING: linux-modules-extra-${kernel_cap} is not available; continuing without it"
sudo apt-mark hold linux-aws linux-image-aws linux-headers-aws

# Apply all available updates. The dpkg options keep locally-modified config files
# (e.g. efs-utils.conf); without them dpkg prompts and aborts on EOF, and
# DEBIAN_FRONTEND=noninteractive does not cover this.
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -o Dpkg::Options::="--force-confold" -o Dpkg::Options::="--force-confdef"

# Refresh the Lustre client for the kernel about to boot.
new_kernel=$(dpkg-query -W -f='${Package}\n' 'linux-image-*-aws' | sed 's/^linux-image-//' | grep -E '^[0-9]' | sort -V | tail -n1)
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y "lustre-client-modules-${new_kernel}" lustre-client-modules-aws
```

After applying the updates, on any operating system, reboot the node to activate them. A reboot is required when the update installs a new kernel:

```
$ sudo reboot
```