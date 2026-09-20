

# Sample Amazon Linux 2023 image description
<a name="al2023-isolated-compute-recipe"></a>

The sample Amazon Linux 2023 image description has the following characteristics: 

1. **Unified Kernel Image (UKI) boot** — Boot using a single, signed binary that combines the kernel, `initrd`, and boot parameters into one immutable image.

1. **Read-only root filesystem** — Use Enhanced Read-Only File System (`erofs`) with dm-verity protection to ensure that the root filesystem cannot be modified and maintains cryptographic integrity verification.

1. **Ephemeral overlay filesystem** — Create a temporary overlay filesystem that allows temporary writes to directories like `/etc`, `/run`, and `/var`. Since this overlay filesystem exists only in memory, all changes are automatically lost when the instance reboots, ensuring the system returns to its original trusted state.

1. **Disabled remote access methods** — Remove the following remote access mechanisms to prevent remote access:


<table>
<thead>
  <tr><th>Access Method</th><th>Description</th><th>Image description implementation</th></tr>
</thead>
<tbody>
  <tr><td>SSH</td><td>Excludes OpenSSH server. Makes the instance inherently incapable of handling SSH traffic.</td><td>Ignore the <code>openssh-server</code> package *</td></tr>
  <tr><td>User Data</td><td>Removes Cloud-init. Eliminates the ability for operators to provide user data to instances and run boot-time scripts.</td><td>Ignore the <code>cloud-init</code> and <code>cloud-init-cfg-ec2</code> packages *</td></tr>
  <tr><td>Chrony</td><td>Disables the chrony command port. Prevents operators from running chrony commands on running instances.</td><td>Ignore the <code>amazon-chrony-config</code> package *</td></tr>
  <tr><td>MOTD</td><td>Removes MOTD package. Eliminates the ability for operators to change messages or functionality on running instances.</td><td>Ignore the <code>update-motd</code> package *</td></tr>
  <tr><td>AWS SSM</td><td>Removes the AWS SSM agent. Prevents remote access to running instances using AWS SSM.</td><td>Ignore the <code>amazon-ssm-agent</code> package *</td></tr>
  <tr><td>EC2 Instance Connect</td><td>Removes EC2 Instance Connect package. Disables SSH access using this tool.</td><td>Ignore the <code>ec2-instance-connect</code> package *</td></tr>
  <tr><td>Serial Console</td><td>Disables serial console. Ensures that console access is unavailable for running instances and removes the operators' ability to login to the serial console.</td><td>Disabled through kernel command line parameter</td></tr>
</tbody>
</table>


   \* For more information, see [ Image Description Elements](https://osinside.github.io/kiwi/image_description/elements.html#packages-ignore).