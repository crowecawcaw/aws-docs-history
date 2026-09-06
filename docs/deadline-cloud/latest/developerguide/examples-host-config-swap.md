

# Enable swap on Deadline Cloud Linux workers
<a name="examples-host-config-swap"></a>

The [swap\_for\_smf](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/swap_for_smf) host configuration script on the GitHub website creates and enables a swap file on Deadline Cloud Linux service-managed fleet workers. Use this script for memory-intensive workloads that temporarily exceed physical RAM, such as ComfyUI.

Some workloads need to memory-map large files through CPU RAM before loading them onto the GPU. For example, loading a 16 GB diffusion model on a `g6.xlarge` instance (16 GB RAM) can OOM-kill the process without swap. A swap file provides overflow capacity so that these loads succeed.

The script does the following:

1. Creates a 32 GB swap file at `/swapfile` (skips if one already exists).

1. Enables the swap file immediately.

1. Adds an `/etc/fstab` entry so that swap persists across reboots.

To change the swap size, edit `linux.sh` and update the `SWAP_SIZE` variable.

For an alternative that changes the kernel's overcommit behavior instead of adding swap, see the [overcommit\_override\_for\_smf](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/overcommit_override_for_smf) script on the GitHub website.