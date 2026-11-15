

# Run Nitro Sandboxes with Firecracker
<a name="nitro-sandboxes-run-firecracker"></a>

You can run Nitro Sandboxes on an Amazon EC2 instance with your own orchestrator and Firecracker. For a container-focused flow in which Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS) runs each pod or task in its own Nitro Sandbox, see [Sandboxing on Amazon EKS with isolated and confidential pods](https://docs.aws.amazon.com/eks/latest/userguide/sandboxing.html) in the *Amazon EKS User Guide* and [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in the *Amazon Elastic Container Service Developer Guide*. The operating system that runs in a Nitro Sandbox is called the *guest*. Your orchestrator operates the parent instance, and you are responsible for the following tasks:
+ Building guest images with the settings that your workload needs.
+ Running the device backends, and treating all data from a Nitro Sandbox as untrusted input.
+ Accounting for the memory and CPU that each Nitro Sandbox uses.
+ Limiting the shared network resources and the instance metadata access of each Nitro Sandbox.
+ Stopping each Nitro Sandbox before you stop or reboot the parent instance, which terminates them.
+ Relaying attestation traffic between a Nitro Sandbox and the external verifier.

For the limits that apply, see [Considerations and limitations](amazon-ec2-nitro-sandboxes.md#nitro-sandboxes-considerations). To release secrets to a Nitro Sandbox, see [Attest a Nitro Sandbox](nitro-sandboxes-attestation.md).

**Topics**
+ [How Firecracker runs a Nitro Sandbox](#nitro-sandboxes-firecracker)
+ [Prerequisites](#nitro-sandboxes-prerequisites)
+ [Prepare the parent instance](#nitro-sandboxes-prepare-parent)
+ [Prepare a guest image](#nitro-sandboxes-guest-image)
+ [Launch a Nitro Sandbox](#nitro-sandboxes-launch)
+ [Nitro Sandbox settings in the Firecracker configuration](#nitro-sandboxes-settings)
+ [Set the size of a Nitro Sandbox](#nitro-sandboxes-resize)
+ [Attach storage to a Nitro Sandbox](#nitro-sandboxes-attach-storage)
+ [Clean up](#nitro-sandboxes-clean-up)
+ [Nitro Sandboxes on instances with multiple NUMA nodes](nitro-sandboxes-numa.md)

## How Firecracker runs a Nitro Sandbox
<a name="nitro-sandboxes-firecracker"></a>

Firecracker can launch a Nitro Sandbox instead of a KVM microVM. It uses the AWS Nitro Enclaves driver on the parent instance to create, configure, and start the Nitro Sandbox. Firecracker provides the API socket and the device backends, and manages the lifecycle of the Nitro Sandbox. To launch a Nitro Sandbox, Firecracker does the following:

1. Creates the Nitro Sandbox in the mode that you choose.

1. Adds the vCPUs.

1. Allocates the memory from the memory pool of the parent instance, writes the guest image into it, and gives the memory to the Nitro Sandbox.

1. Adds each configured device, such as block, network, and vsock devices.

1. Starts the Nitro Sandbox. The Nitro System boots the image through UEFI firmware and presents a PCIe topology to the guest.

The guest sees standard virtio-pci devices. In direct mode, the devices move data through guest memory. In confidential mode, each device moves data through its own buffer, called a *device memory buffer* (DMB), and the guest kernel must support DMB.

Because Nitro Sandboxes build on Nitro Enclaves, the Firecracker configuration uses the `enclave` key for Nitro Sandbox settings.

## Prerequisites
<a name="nitro-sandboxes-prerequisites"></a>

To launch a Nitro Sandbox, you must meet the following requirements:
+ An instance type that supports Nitro Sandboxes. For the list, see [Considerations and limitations](amazon-ec2-nitro-sandboxes.md#nitro-sandboxes-considerations).
+ An operating system on the parent instance with the Nitro Enclaves driver support for Nitro Sandboxes. Amazon Linux 2023 (AL2023) includes this support in the `kernel6.18` package, version `6.18.51-120.162.amzn2023` or later, together with the guest support that confidential mode needs. The following procedures use AL2023.
+ Firecracker version 1.18 or later. For more information, see the [Firecracker project](https://github.com/firecracker-microvm/firecracker) on the GitHub website.
+ Root access on the parent instance. The `/dev/nitro_enclaves` device belongs to `root:root` with mode `0660`, so run Firecracker as `root` or give its user access to the device.
+ A guest kernel with an EFI stub. In confidential mode, the guest kernel must also support DMB. The AL2023 kernel that the parent instance runs meets both requirements. To hot plug devices, the guest kernel must also support PCIe native hot plug.

**Note**  
Ubuntu support is available as a personal package archive (PPA).

## Prepare the parent instance
<a name="nitro-sandboxes-prepare-parent"></a>

Nitro Sandbox memory comes only from a memory pool that the parent instance reserves at boot. Without a pool, you can't launch Nitro Sandboxes.

The parent instance and any Amazon EBS volumes that you create in these procedures incur the standard charges for those resources until you delete them.

**To launch and prepare a parent instance**

1. Launch the parent instance with Nitro Enclaves enabled. Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command with the `--enclave-options Enabled=true` option.

   ```
   aws ec2 run-instances \
       --image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.18-{{x86_64}} \
       --instance-type {{m7i.4xlarge}} \
       --key-name {{my-key-pair}} \
       --iam-instance-profile Name={{my-instance-profile}} \
       --enclave-options Enabled=true
   ```

   To use attestation with AWS Key Management Service (AWS KMS), the parent instance needs an instance profile with an AWS Identity and Access Management (IAM) role. The role provides the credentials for the AWS KMS requests, and its ARN is part of the attestation document.

1. Connect to the instance. For more information, see [Connect to your EC2 instance](connect.md).

1. Check that the kernel version is `6.18.51-120.162.amzn2023` or later.

   ```
   uname -r
   ```

1. Add the memory pool to the kernel command line. Size the pool for the memory of all the Nitro Sandboxes that you plan to run at the same time, plus their overhead. For the overhead, see [Considerations and limitations](amazon-ec2-nitro-sandboxes.md#nitro-sandboxes-considerations). On an instance with more than one NUMA node, see [Nitro Sandboxes on instances with multiple NUMA nodes](nitro-sandboxes-numa.md).

   ```
   sudo grubby --update-kernel=ALL --args="nitro_enclaves.mempool={{8G}}@0"
   ```

1. Reboot the instance.

   ```
   sudo reboot
   ```

1. Check that the parent instance reserved the pool.

   ```
   sudo dmesg | grep "nitro_enclaves: CMA pool"
   ```

   The following is example output.

   ```
   nitro_enclaves: CMA pool: 8192 MiB reserved in 16 region(s), 8192 MiB requested
   ```

**To install Firecracker on the parent instance**

1. Download Firecracker from the [Firecracker releases](https://github.com/firecracker-microvm/firecracker/releases) on the GitHub website, and install it in `/usr/local/bin`. Replace {{version}} with version 1.18.0 or later.

   ```
   VERSION={{version}}
   ARCH=$(uname -m)
   curl -sSfL -o firecracker.tgz \
       https://github.com/firecracker-microvm/firecracker/releases/download/v${VERSION}/firecracker-v${VERSION}-${ARCH}.tgz
   tar -xzf firecracker.tgz
   sudo install -m 755 release-v${VERSION}-${ARCH}/firecracker-v${VERSION}-${ARCH} /usr/local/bin/firecracker
   ```

1. Check the installed version.

   ```
   firecracker --version
   ```

Each running Nitro Sandbox uses one Nitro Sandbox slot. With a memory pool, the parent instance has 4 slots. Without a pool, it has 0. When all slots are in use, launching another Nitro Sandbox fails with a `No space left on device` error.

**To run more than four Nitro Sandboxes at the same time**

1. View the current number of slots and the maximum for the instance.

   ```
   cat /sys/class/misc/nitro_enclaves/pcie_slots /sys/class/misc/nitro_enclaves/pcie_slots_total
   ```

1. Raise the number of slots before you launch the additional Nitro Sandboxes.

   ```
   echo {{12}} | sudo tee /sys/class/misc/nitro_enclaves/pcie_slots
   ```

The number of slots grows from 4 in steps of 8 (12, 20, 28, and so on). The parent instance rounds other values up to the next step. You can only raise the value, up to the value of `pcie_slots_total`. Each step of 8 slots uses 128 MiB of the memory pool until the next reboot.

To check the remaining capacity before you launch, read `pcie_slots_in_use`, `mem_pool/free`, and `cpu_pool/free` in the same directory.

## Prepare a guest image
<a name="nitro-sandboxes-guest-image"></a>

A guest image consists of an EFI-stub kernel, an initial RAM disk, and a kernel command line. In confidential mode, the Nitro System measures all three, so a guest that runs entirely from its initial RAM disk is fully measured. Your applications run unmodified in the guest.

The following procedure builds a guest image from the AL2023 kernel of the parent instance with **dracut**. The image has no root drive. Its init script configures the network interface and then starts your workload. The AL2023 kernel builds the network driver as a module, so the `ip=` kernel parameter can't configure the interface, and the init script configures it instead.

**To build a guest image**

1. Create a file named `sandbox-init` with the following content. The Nitro Sandbox runs it as its first process.

   ```
   #!/bin/bash
   export PATH=/usr/local/bin:/usr/sbin:/usr/bin
   mount -t proc proc /proc
   mount -t sysfs sysfs /sys
   mount -t devtmpfs devtmpfs /dev
   modprobe -a virtio_pci virtio_net vmw_vsock_virtio_transport nsm
   
   # Configure eth0 with a static address and the TAP device of the parent
   # instance as the default gateway.
   ip link set lo up
   ip addr add {{192.0.2.2/24}} dev eth0
   ip link set eth0 up
   ip route add default via {{192.0.2.1}}
   echo "nameserver 169.254.169.253" > /etc/resolv.conf
   
   # Start your workload here.
   exec sleep infinity
   ```

1. Make the file executable. The kernel does not start an init script without the execute permission.

   ```
   chmod +x sandbox-init
   ```

1. Copy the kernel of the parent instance.

   ```
   cp /boot/vmlinuz-$(uname -r) vmlinuz
   ```

1. Build the initial RAM disk. The `--install` option lists the programs that the init script calls, and **dracut** adds the libraries that they need.

   ```
   sudo dracut --force --no-hostonly --reproducible --no-early-microcode \
       --modules bash \
       --add-drivers "virtio_pci virtio_net vmw_vsock_virtio_transport nsm" \
       --install "mount modprobe ip sleep" \
       --include "$PWD/sandbox-init" /init \
       --kver $(uname -r) initrd.img
   sudo chown "$(id -un):" initrd.img
   ```

   Do not add the `base` **dracut** module. It installs its own `/init`, which replaces your init script. Builds from the same files produce the same `initrd.img`.

You can launch the kernel and the initial RAM disk directly, and Firecracker builds the image at launch. To use attestation, add the attestation steps to this image and build the image in advance, as described in [Add attestation to a guest image](nitro-sandboxes-attestation.md#nitro-sandboxes-attestation-image).

## Launch a Nitro Sandbox
<a name="nitro-sandboxes-launch"></a>

You launch a Nitro Sandbox by passing a configuration to Firecracker, either as a file or through its API socket. First, set up the network connection of the Nitro Sandbox on the parent instance. The following example then launches a Nitro Sandbox in confidential mode from a kernel and an initial RAM disk, with a network interface and a vsock device, and without block devices.

**To set up networking for a Nitro Sandbox**

1. Create a TAP device for the network interface of the Nitro Sandbox, give it the address of the default gateway of the guest, and turn on IP forwarding.

   ```
   sudo ip tuntap add dev {{tap0}} mode tap
   sudo ip addr add {{192.0.2.1/24}} dev {{tap0}}
   sudo ip link set {{tap0}} up
   sudo sysctl -w net.ipv4.ip_forward=1
   ```

1. Install **nftables**.

   ```
   sudo dnf install -y nftables
   ```

1. Route the traffic of the Nitro Sandbox through the primary network interface of the parent instance with NAT. The `reject` rule blocks the access of the Nitro Sandbox to the instance metadata service (IMDS) of the parent instance. Without it, the Nitro Sandbox can read the instance metadata and the IAM role credentials of the parent instance.

   ```
   IFACE=$(ip route show default | awk '{print $5; exit}')
   sudo nft -f - <<EOF
   table ip sandbox {
       chain forward {
           type filter hook forward priority filter; policy accept;
           iifname "{{tap0}}" ip daddr 169.254.169.254 reject
       }
       chain postrouting {
           type nat hook postrouting priority srcnat; policy accept;
           iifname "{{tap0}}" oifname "$IFACE" masquerade
       }
   }
   EOF
   ```

   With `reject`, a request to the IMDS fails immediately. With `drop`, it waits for a timeout. Keep `169.254.169.253` reachable if the guest uses the Amazon DNS server.

   The TAP device, the IP forwarding setting, and the **nftables** rules do not persist after a reboot of the parent instance. In the Nitro Sandbox, configure an address in the same subnet with the address of the TAP device as the default gateway, as the init script in [Prepare a guest image](#nitro-sandboxes-guest-image) does.

**To launch a Nitro Sandbox**

1. Create the directory for the vsock socket, and remove a socket that an earlier launch left behind. Firecracker does not create the directory and does not remove the socket when it stops. Use a different socket path and a different TAP device for each Nitro Sandbox that runs at the same time.

   ```
   sudo mkdir -p {{/run/sandbox}}
   sudo rm -f {{/run/sandbox/v.sock}}
   ```

1. Save the following configuration as `sandbox.json`.

   ```
   {
       "boot-source": {
           "kernel_image_path": "{{vmlinuz}}",
           "initrd_path": "{{initrd.img}}"
       },
       "machine-config": {
           "vcpu_count": {{2}},
           "mem_size_mib": {{2048}}
       },
       "drives": [],
       "network-interfaces": [
           {
               "iface_id": "eth0",
               "host_dev_name": "{{tap0}}"
           }
       ],
       "vsock": {
           "guest_cid": 3,
           "uds_path": "{{/run/sandbox/v.sock}}"
       },
       "enclave": {
           "cpu_overcommit": true
       }
   }
   ```

   The configuration must contain the `drives` key, even if the Nitro Sandbox has no block devices. For the other settings, see [Nitro Sandbox settings in the Firecracker configuration](#nitro-sandboxes-settings).

1. Run the following command in the directory that contains the guest image files.

   ```
   sudo firecracker --no-api --config-file sandbox.json
   ```

   The `--no-api` option runs Firecracker without an API socket. Every Firecracker process otherwise uses the same default socket path. If you need the API socket, for example for hot plug or to resize a block device, give each process its own path with the `--api-sock` option.

1. In another terminal, check that the Nitro Sandbox runs.

   ```
   cat /sys/class/misc/nitro_enclaves/pcie_slots_in_use
   ```

   The file shows the number of running Nitro Sandboxes. With one Nitro Sandbox, the output is `1`. Firecracker does not show the guest console unless you set `debug_mode`.

A Nitro Sandbox stops when it powers off or reboots, when its init process exits, or when you stop the Firecracker process, for example with the **kill** command or with Ctrl\+C in the foreground. A reboot from the guest does not restart the Nitro Sandbox. Its vCPUs, memory, and slot then return to the pools of the parent instance.

Before you launch a Nitro Sandbox with the same `uds_path` again, remove the socket file. Otherwise, Firecracker fails with an `Address in use` error.

## Nitro Sandbox settings in the Firecracker configuration
<a name="nitro-sandboxes-settings"></a>

You can use the following settings in the Firecracker configuration of a Nitro Sandbox:

`kernel_image_path`, `initrd_path`  
In the `boot-source` object, an EFI-stub kernel and an optional initial RAM disk. Firecracker builds the measured image from these files at launch. Instead of a kernel, `kernel_image_path` can name an image that you built with `eif_build`. Firecracker then launches that image unchanged, and you omit `initrd_path`.

`boot_args`  
In the `boot-source` object, an optional kernel command line. It replaces the default command line, `panic=1 initcall_blacklist=i8042_init`. If a drive has `is_root_device` set to `true`, Firecracker adds `root=/dev/vda rw` to the command line, or `root=/dev/vda ro` if the drive is read-only. For an image that you built with `eif_build`, the command line in the image applies instead.

`vsock`  
A local socket between the Nitro Sandbox and the parent instance. Firecracker connects it to the Unix socket in `uds_path` on the parent instance. For more information, see the [Firecracker vsock documentation](https://github.com/firecracker-microvm/firecracker/blob/main/docs/vsock.md) on the GitHub website.

`enclave`  
Makes the virtual machine a Nitro Sandbox. A Nitro Sandbox runs in confidential mode by default, so an empty `enclave` object is enough.

`cpu_overcommit`  
In the `enclave` object, lets the vCPUs of the Nitro Sandbox share the vCPUs of the parent instance. For the alternative, see [Set the size of a Nitro Sandbox](#nitro-sandboxes-resize).

`direct_mode`  
In the `enclave` object, set to `true` to run the Nitro Sandbox in direct mode. For the difference between the modes, see [Confidential and direct modes](amazon-ec2-nitro-sandboxes.md#nitro-sandboxes-modes).

`hotplug_mode`  
In the `enclave` object, set to `true` to add block and network devices while the Nitro Sandbox runs. You add them through the API socket with `PUT /drives` and `PUT /network-interfaces` requests. Treat every device that the parent instance adds as untrusted input. For the effect on attestation, see [Nitro Sandbox measurements](nitro-sandboxes-attestation.md#nitro-sandboxes-attestation-pcrs).

`debug_mode`  
In the `enclave` object, set to `true` while you develop. Firecracker then shows the guest console on its standard output. When Firecracker builds the image at launch, it also adds `console=ttyS0` to the kernel command line. For an image that you build with `eif_build`, include `console=ttyS0` in its command line, or the console shows no guest output.  
The boot measurements in the attestation document read as zero, so do not use debug mode in production. For more information, see [Nitro Sandbox measurements](nitro-sandboxes-attestation.md#nitro-sandboxes-attestation-pcrs).

Firecracker rejects a Nitro Sandbox configuration that uses a memory balloon, virtio-mem, virtio-pmem, vhost-user block devices, huge pages, CPU templates, simultaneous multithreading (`smt`), or dirty page tracking.

## Set the size of a Nitro Sandbox
<a name="nitro-sandboxes-resize"></a>

You set the size of a Nitro Sandbox when you launch it, in the `machine-config` object.

```
"machine-config": {
    "vcpu_count": {{4}},
    "mem_size_mib": {{4096}}
}
```

`vcpu_count`  
The number of vCPUs. With `cpu_overcommit` set to `true`, the vCPUs share the vCPUs of the parent instance, and a Nitro Sandbox can have up to as many vCPUs as the parent instance.  
Without CPU overcommit, each vCPU uses a dedicated hardware thread of the parent instance, and the Nitro System assigns whole cores. On instances with two threads per core, use an even number of vCPUs, or the launch fails.  
The Nitro Enclaves driver keeps the first core of the parent instance for the parent, and the other cores form the CPU pool. A Nitro Sandbox can use up to all free vCPUs of the CPU pool, which `cpu_pool/free` in `/sys/class/misc/nitro_enclaves` shows. You don't need to provision a CPU pool, because the Nitro Enclaves driver discovers the available cores.

`mem_size_mib`  
The memory in MiB, as a multiple of 2 MiB. The memory comes from the memory pool of the parent instance. For the minimum, see [Considerations and limitations](amazon-ec2-nitro-sandboxes.md#nitro-sandboxes-considerations).

To change the size, terminate the Nitro Sandbox and launch a new one.

## Attach storage to a Nitro Sandbox
<a name="nitro-sandboxes-attach-storage"></a>

Each entry in the `drives` array gives the Nitro Sandbox a block device. Firecracker reads raw images, not qcow2 images. You can back a block device with one of the following:
+ A raw image file on the parent instance
+ An [instance store](InstanceStorage.md) volume of the parent instance
+ An Amazon Elastic Block Store (Amazon EBS) volume that is attached to the parent instance

**To add an Amazon EBS volume as a data drive**

1. If the volume has no file system yet, create one on the parent instance. Then make sure that the parent instance does not mount the volume.

   ```
   sudo dnf install -y e2fsprogs
   sudo mkfs.ext4 {{/dev/nvme1n1}}
   ```

1. In `sandbox.json`, replace the `drives` array with the following.

   ```
   "drives": [
       {
           "drive_id": "data",
           "path_on_host": "{{/dev/nvme1n1}}",
           "is_root_device": false,
           "is_read_only": false
       }
   ]
   ```

1. Add the block device driver and the file system to the guest image from [Prepare a guest image](#nitro-sandboxes-guest-image). In `sandbox-init`, add the following lines before the line that starts your workload. The guest sees the first drive as `/dev/vda`.

   ```
   modprobe -a virtio_blk ext4
   mkdir -p /data
   mount /dev/vda /data
   ```

1. Build the initial RAM disk again, with the additional drivers and programs.

   ```
   sudo dracut --force --no-hostonly --reproducible --no-early-microcode \
       --modules bash \
       --add-drivers "virtio_pci virtio_net vmw_vsock_virtio_transport nsm virtio_blk ext4" \
       --install "mount modprobe ip sleep mkdir" \
       --include "$PWD/sandbox-init" /init \
       --kver $(uname -r) initrd.img
   sudo chown "$(id -un):" initrd.img
   ```

Do not mount the volume on the parent instance while a Nitro Sandbox uses it. To mount one volume from more than one Nitro Sandbox, use a file system that supports multiple writers. Otherwise, the file system gets corrupted.

To resize a block device while the Nitro Sandbox runs, launch Firecracker with an API socket (the `--api-sock` option) instead of `--no-api`. Grow the backing file or volume, and then send a `PATCH /drives/{{drive_id}}` request to the API socket.

The parent instance can read the data on every block device that it presents. For how to keep data confidential, see [Considerations and limitations](amazon-ec2-nitro-sandboxes.md#nitro-sandboxes-considerations).

## Clean up
<a name="nitro-sandboxes-clean-up"></a>

When you no longer need the Nitro Sandboxes, stop them, and then terminate the parent instance with the [terminate-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/terminate-instances.html) command. Delete any Amazon EBS volumes that you created for data drives with the [delete-volume](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-volume.html) command.

```
aws ec2 terminate-instances --instance-ids {{i-1234567890abcdef0}}
aws ec2 delete-volume --volume-id {{vol-1234567890abcdef0}}
```