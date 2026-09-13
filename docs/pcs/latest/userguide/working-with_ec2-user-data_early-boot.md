

# Example: Run early boot operations with a cloud-init boothook
<a name="working-with_ec2-user-data_early-boot"></a>

 Provide this script as the value of `"userData"` in your launch template. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md). 

Some configuration must run at the very beginning of the boot sequence, before the AWS PCS bootstrap starts and before any service uses the hardware. Typical cases are GPU configuration commands that can't take effect while processes hold the GPUs, such as enabling NVIDIA Multi-Instance GPU (MIG) mode, and operations that require a reboot to take effect, such as changing the GPU ECC mode. A reboot at this stage is safe, because the AWS PCS bootstrap hasn't started yet. Don't reboot later in the boot process, such as from a node lifecycle action script: a reboot there interrupts the AWS PCS bootstrap sequence. For more information, see [Best practices for node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-best-practices.md).

To create the boot hook, add a block with content type `text/cloud-boothook` to your user data. The block contains the script itself. A boothook is the earliest hook available in user data: `cloud-init` runs it as soon as it processes the block, before `cloud-config` directives such as `bootcmd` and before the AWS PCS user data blocks that register the node. A boothook runs on *every* boot, including the reboot it might itself trigger, so the script must be idempotent: check the current state first and skip work that is already done. For more information, see the [cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/explanation/format.html).

The following example enables MIG mode on all GPUs and creates the MIG instances at every boot. Because no GPU client has started yet, the mode change takes effect immediately and no reboot is needed.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-boothook; charset="us-ascii"

#!/bin/bash
if ! nvidia-smi -i 0 -q | grep -A1 'MIG Mode' | grep -q 'Current.*Enabled'; then
    nvidia-smi -mig 1
fi
if [ -z "$(nvidia-smi -L | grep MIG)" ]; then
    for i in 0 1 2 3 4 5 6 7; do
        nvidia-smi mig -i $i -cgi 9,14,19,19 -C
    done
fi

--==MYBOUNDARY==--
```

If your operation prints that a reboot is required, reboot from the same boothook after the state change. On the next boot the idempotency checks find the work already done, so the node continues into the AWS PCS bootstrap normally.