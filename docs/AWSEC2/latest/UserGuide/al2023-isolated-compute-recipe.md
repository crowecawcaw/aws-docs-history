# Sample Amazon Linux 2023 image description

The sample Amazon Linux 2023 image description has the following characteristics:

1. **Unified Kernel Image (UKI) boot** — Boot using a single, signed binary
   that combines the kernel, `initrd`, and boot parameters into one immutable image.
2. **Read-only root filesystem** — Use Enhanced Read-Only File System
   (`erofs`) with dm-verity protection to ensure that the root filesystem cannot be modified and maintains
   cryptographic integrity verification.
3. **Ephemeral overlay filesystem** — Create a temporary overlay filesystem
   that allows temporary writes to directories like `/etc`, `/run`, and `/var`. Since
   this overlay filesystem exists only in memory, all changes are automatically lost when the instance reboots,
   ensuring the system returns to its original trusted state.
4. **Disabled remote access methods** — Remove the following remote access
   mechanisms to prevent remote access:

| Access Method        | Description                                                                                                                                                  | Image description implementation                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSH                  | Excludes OpenSSH server. Makes the instance inherently incapable of handling SSH traffic.                                                                    | Ignore the `openssh-server` package \*                       |
| User Data            | Removes Cloud-init. Eliminates the ability for operators to provide user data to instances and run boot-time scripts.                                        | Ignore the `cloud-init` and `cloud-init-cfg-ec2` packages \* |
| Chrony               | Disables the chrony command port. Prevents operators from running chrony commands on running instances.                                                      | Ignore the `amazon-chrony-config` package \*                 |
| MOTD                 | Removes MOTD package. Eliminates the ability for operators to change messages or functionality on running instances.                                         | Ignore the `update-motd` package \*                          |
| AWS SSM              | Removes the AWS SSM agent. Prevents remote access to running instances using AWS SSM.                                                                        | Ignore the `amazon-ssm-agent` package \*                     |
| EC2 Instance Connect | Removes EC2 Instance Connect package. Disables SSH access using this tool.                                                                                   | Ignore the `ec2-instance-connect` package \*                 |
| Serial Console       | Disables serial console. Ensures that console access is unavailable for running instances and removes the operators' ability to login to the serial console. | Disabled via kernel command line parameter                   | \* For more information, see [Image Description Elements](https://osinside.github.io/kiwi/image_description/elements.html#packages-ignore "https://osinside.github.io/kiwi/image_description/elements.html#packages-ignore"). |
