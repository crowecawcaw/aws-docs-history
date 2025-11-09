# Get started with EFA and MPI for HPC workloads on Amazon EC2

This tutorial helps you to launch an EFA and MPI-enabled instance cluster for HPC workloads.

###### Note

The `u7i-12tb.224xlarge`, `u7in-16tb.224xlarge`, `u7in-24tb.224xlarge`,
and `u7in-32tb.224xlarge` instances can run up to 128 parallel MPI processes with Open MPI
or up to 256 parallel MPI processes with Intel MPI.

###### Tasks

- [Step 1: Prepare an EFA-enabled security group](#efa-start-security "#efa-start-security")
- [Step 2: Launch a temporary instance](#efa-start-tempinstance "#efa-start-tempinstance")
- [Step 3: Install the EFA software](#efa-start-enable "#efa-start-enable")
- [Step 4: (Optional) Enable Open MPI 5](#efa-start-ompi5 "#efa-start-ompi5")
- [Step 5: (Optional) Install Intel MPI](#efa-start-impi "#efa-start-impi")
- [Step 6: Disable ptrace protection](#efa-start-ptrace "#efa-start-ptrace")
- [Step 7. Confirm installation](#efa-start-test "#efa-start-test")
- [Step 8: Install your HPC application](#efa-start-hpc-app "#efa-start-hpc-app")
- [Step 9: Create an EFA-enabled AMI](#efa-start-ami "#efa-start-ami")
- [Step 10: Launch EFA-enabled instances into a cluster
  placement group](#efa-start-instances "#efa-start-instances")
- [Step 11: Terminate the temporary instance](#efa-start-terminate "#efa-start-terminate")
- [Step 12: Enable passwordless SSH](#efa-start-passwordless "#efa-start-passwordless")

## Step 1: Prepare an EFA-enabled security group

An EFA requires a security group that allows all inbound and outbound traffic to and from the
security group itself. The following procedure creates a security group that allows all inbound and outbound traffic to
and from itself, and that allows inbound SSH traffic from any IPv4 address for SSH connectivity.

###### Important

This security group is intended for testing purposes only. For your production environments, we recommend that you create
an inbound SSH rule that allows traffic only from the IP address from which you are connecting, such as the IP address of your computer, or
a range of IP addresses in your local network.

For other scenarios, see [Security group rules for different use cases](security-group-rules-reference.md "security-group-rules-reference.md").

###### To create an EFA-enabled security group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security Groups** and then
   choose **Create security group**.
3. In the **Create security group** window, do the following:
   1. For **Security group name**, enter a descriptive
      name for the security group, such as `EFA-enabled security
group`.
   2. (Optional) For **Description**, enter a brief description
      of the security group.
   3. For **VPC**, select the VPC into which you intend to
      launch your EFA-enabled instances.
   4. Choose **Create security group**.

4. Select the security group that you created, and on the **Details** tab,
   copy the **Security group ID**.
5. With the security group still selected, choose **Actions**, **Edit inbound rules**,
   and then do the following:
   1. Choose **Add rule**.
   2. For **Type**, choose **All traffic**.
   3. For **Source type**, choose **Custom** and paste the security group ID that
      you copied into the field.
   4. Choose **Add rule**.
   5. For **Type**, choose **SSH**.
   6. For **Source type**, choose **Anywhere-IPv4**.
   7. Choose **Save rules**.

6. With the security group still selected, choose **Actions**, **Edit outbound rules**,
   and then do the following:
   1. Choose **Add rule**.
   2. For **Type**, choose **All traffic**.
   3. For **Destination type**, choose **Custom** and paste the security group ID that you copied into the field.
   4. Choose **Save rules**.

## Step 2: Launch a temporary instance

Launch a temporary instance that you can use to install and configure the EFA software
components. You use this instance to create an EFA-enabled AMI from which you
can launch your EFA-enabled instances.

###### To launch a temporary instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and then choose
   **Launch Instances** to open the new launch instance wizard.
3. (_Optional_) In the **Name and tags** section,
   provide a name for the instance, such as `EFA-instance`. The name is assigned
   to the instance as a resource tag (`Name=`EFA-instance``).
4. In the **Application and OS Images** section, select an AMI for
   one of the [supported operating systems](efa.md#efa-os "efa.md#efa-os").
5. In the **Instance type** section, select a
   [supported instance type](efa.md#efa-instance-types "efa.md#efa-instance-types").
6. In the **Key pair** section, select the key pair to use for the
   instance.
7. In the **Network settings** section, choose **Edit**,
   and then do the following:
   1. For **Subnet**, choose the subnet in which to launch the
      instance. If you do not select a subnet, you can't enable the instance for EFA.
   2. For **Firewall (security groups)**, choose **Select
      existing security group**, and then select the security group that you
      created in the previous step.
   3. Expand the **Advanced network configuration** section.

   For **Network interface 1**, select **Network card index = 0**,
   **Device index = 0**, and **Interface type = EFA with ENA**.

   (Optional) If you are using a multi-card instance type, such as `p4d.24xlarge`
   or `p5.48xlarge`, for each additional network interface required, choose
   **Add network interface**, for **Network card index**
   select the next unused index, and then select **Device index = 1**
   and **Interface type = EFA with ENA** or **EFA-only**.

8. In the **Storage** section, configure the volumes as needed.
9. In the **Summary** panel on the right, choose **Launch
   instance**.

###### Note

Consider requiring the use of IMDSv2 for the temporary instance as well as the AMI that you will create in [Step 9](#efa-start-ami "#efa-start-ami")
unless you have already [set IMDSv2 as the default for the account](configuring-IMDS-new-instances.md#set-imdsv2-account-defaults "configuring-IMDS-new-instances.md#set-imdsv2-account-defaults"). For more information about IMDSv2 configuration
steps, see [Configure instance metadata options
for new instances](configuring-IMDS-new-instances.md "configuring-IMDS-new-instances.md").

## Step 3: Install the EFA software

Install the EFA-enabled kernel, EFA drivers, Libfabric, and Open MPI stack that is
required to support EFA on your temporary instance.

The steps differ depending on whether you intend to use EFA with Open MPI, with Intel MPI, or
with Open MPI and Intel MPI.

###### Note

Some operating systems might not be supported with Intel MPI. If you are using Intel MPI,
refer to the [Intel MPI documentation](https://www.intel.com/content/www/us/en/developer/articles/system-requirements/mpi-library-system-requirements.html "https://www.intel.com/content/www/us/en/developer/articles/system-requirements/mpi-library-system-requirements.html") to verify support for your operating system.

###### To install the EFA software

1. Connect to the instance you launched. For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").
2. To ensure that all of your software packages are up to date, perform a quick software update
   on your instance. This process may take a few minutes.
   - Amazon Linux 2023, Amazon Linux 2, RHEL 8/9, Rocky Linux 8/9

   ```
   `$` sudo yum update -y
   ```

   - Ubuntu and Debian

   ```
   `$` sudo apt-get update && sudo apt-get upgrade -y
   ```

   - SUSE Linux Enterprise

   ```
   `$` sudo zypper update -y
   ```

3. Reboot the instance and reconnect to it.
4. Download the EFA software installation files. The software installation files are packaged into a compressed tarball (`.tar.gz`) file.
   To download the latest _stable_ version, use the following command.

You can also get the latest version by replacing the version number with `latest` in the preceding command.

```
`$` curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.44.0.tar.gz
```

5. (_Optional_) Verify the authenticity and integrity of the EFA tarball (`.tar.gz`) file.

We recommend that you do this to verify the identity of the software publisher and to check that the file
has not been altered or corrupted since it was published. If you do not want to verify the tarball file, skip
this step.

###### Note

Alternatively, if you prefer to verify the tarball file by using an MD5 or SHA256 checksum instead, see
[Verify the EFA installer using a checksum](efa-verify.md "efa-verify.md").

    1. Download the public GPG key and import it into your keyring.



    ```
    `$` wget https://efa-installer.amazonaws.com/aws-efa-installer.key && gpg --import aws-efa-installer.key
    ```

    The command should return a key value. Make a note of the key value, because you need it in the next step.
    2. Verify the GPG key's fingerprint. Run the following command and specify the key
     value from the previous step.



    ```
    `$` gpg --fingerprint `key_value`
    ```

    The command should return a fingerprint that is identical to `4E90 91BC BB97 A96B 26B1 5E59 A054 80B1 DD2D 3CCC`. If
     the fingerprint does not match, don't run the EFA installation script, and contact
     Support.
    3. Download the signature file and verify the signature of the EFA tarball file.



    ```
    `$` wget https://efa-installer.amazonaws.com/aws-efa-installer-1.44.0.tar.gz.sig && gpg --verify ./aws-efa-installer-1.44.0.tar.gz.sig
    ```

    The following shows example output.



    ```
    gpg: Signature made Wed 29 Jul 2020 12:50:13 AM UTC using RSA key ID DD2D3CCC
    gpg: **Good signature** from "Amazon EC2 EFA <ec2-efa-maintainers@amazon.com>"
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    **Primary key fingerprint: 4E90 91BC BB97 A96B 26B1 5E59 A054 80B1 DD2D 3CCC**
    ```

    If the result includes `Good signature`, and the fingerprint matches the fingerprint returned in the
     previous step, proceed to the next step. If not, don't run the EFA installation script, and contact Support.

[Show moreShow less](# "#") 6. Extract the files from the compressed `.tar.gz` file and navigate into
the extracted directory.

```
`$` tar -xf aws-efa-installer-1.44.0.tar.gz && cd aws-efa-installer
```

7. Install the EFA software. Do one of the following depending on your use case.

###### Note

**EFA does not support NVIDIA GPUDirect with SUSE Linux**.
If you are using SUSE Linux, you must additionally specify the `--skip-kmod`
option to prevent kmod installation. By default, SUSE Linux does not allow out-of-tree
kernel modules.

Open MPI and Intel MPI
If you intend to use EFA with Open MPI and Intel MPI, you must install
the EFA software with Libfabric and Open MPI, and you **must complete Step 5: Install Intel MPI**.

To install the EFA software with Libfabric and Open MPI, run the following
command.

###### Note

From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default.
You can optionally specify the version of Open MPI that you want to install.
To install only Open MPI 4.1, include `--mpi=openmpi4`. To install only
Open MPI 5, include `--mpi=openmpi5`. To install both, omit the
`--mpi` option.

```
`$` sudo ./efa_installer.sh -y
```

Libfabric is installed to `/opt/amazon/efa`. Open MPI 4.1 is installed
to `/opt/amazon/openmpi`. Open MPI 5 is installed to
`/opt/amazon/openmpi5`.

Open MPI only
If you intend to use EFA with Open MPI only, you must install the EFA software
with Libfabric and Open MPI, and you can **skip Step 5: Install
Intel MPI**. To install the EFA software with Libfabric and Open MPI,
run the following command.

###### Note

From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default.
You can optionally specify the version of Open MPI that you want to install.
To install only Open MPI 4.1, include `--mpi=openmpi4`. To install only
Open MPI 5, include `--mpi=openmpi5`. To install both, omit the
`--mpi` option.

```
`$` sudo ./efa_installer.sh -y
```

Libfabric is installed to `/opt/amazon/efa`. Open MPI 4.1 is installed
to `/opt/amazon/openmpi`. Open MPI 5 is installed to
`/opt/amazon/openmpi5`.

Intel MPI only
If you intend to use EFA with Intel MPI only, you can install the EFA software
without Libfabric and Open MPI. In this case, Intel MPI uses its embedded Libfabric.
If you choose to do this, you **must complete Step 5: Install Intel
MPI**.

To install the EFA software without Libfabric and Open MPI, run the following
command.

```
`$` sudo ./efa_installer.sh -y --minimal
```

8. If the EFA installer prompts you to reboot the instance, do so and then reconnect
   to the instance. Otherwise, log out of the instance and then log back in to complete
   the installation.
9. Delete the uncompressed tarball and the tarball itself. Otherwise, these will be
   included in the EFA-enabled AMI that you create, increasing its size.

## Step 4: (_Optional_) Enable Open MPI 5

###### Note

Perform this step only if you intend to use Open MPI 5.

From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default. Alternatively, you can
choose to install only Open MPI 4.1 or Open MPI 5.

If you chose to install Open MPI 5 in **Step 3: Install the EFA software**,
and you intend to use it, you must perform the following steps to enable it.

###### To enable Open MPI 5

1. Add Open MPI 5 to the PATH environment variable.

```
`$` module load openmpi5
```

2. Verify that Open MPI 5 is enabled for use.

```
`$` which mpicc
```

The command should return the Open MPI 5 installation directory - `/opt/amazon/openmpi5`. 3. (_Optional_) To ensure that Open MPI 5 is added to PATH environment variable
each time the instance starts, do the following:

bash shell
Add `module load openmpi5` to `/home/`username`/.bashrc`
and `/home/`username`/.bash_profile`.

csh and tcsh shells
Add `module load openmpi5` to `/home/`username`/.cshrc`.

If you need to remove Open MPI 5 from the PATH environment variable, run the following command
and remove the command from the shell startup scripts.

```
`$` module unload openmpi5
```

## Step 5: (_Optional_) Install Intel MPI

###### Important

Perform this step only if you intend to use Intel MPI. If you intend to only use Open MPI, skip this step.

Intel MPI requires an additional installation and environment variable configuration.

###### Prerequisite

Ensure that the user performing the following steps has sudo permissions.

###### To install Intel MPI

1. To download the Intel MPI installation script, do the following
   1. Visit the [Intel website](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#mpi "https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#mpi").
   2. In the **Intel MPI Library** section of the webpage,
      choose the link for the **Intel MPI Library for Linux**
      **Offline** installer.

2. Run the installation script that you downloaded in the previous step.

```
`$` sudo bash `installation_script_name`.sh
```

3. In the installer, choose **Accept & install**.
4. Read the Intel Improvement Program, choose the appropriate option, and then choose
   **Begin Installation**.
5. When the installation completes, choose **Close**.
6. By default, Intel MPI uses its embedded (internal) Libfabric. You can configure Intel MPI to use the
   Libfabric that ships with the EFA installer instead. Typically, the EFA installer ships with a
   later version of Libfabric than Intel MPI. In some cases, the Libfabric that ships with the EFA
   installer is more performant than that of Intel MPI. To configure Intel MPI to use the Libfabric that
   ships with the EFA installer, do one of the following depending on your shell.

bash shells
Add the following statement to `/home/`username`/.bashrc`
and `/home/`username`/.bash_profile`.

```
export I_MPI_OFI_LIBRARY_INTERNAL=0
```

csh and tcsh shells
Add the following statement to `/home/`username`/.cshrc`.

```
setenv I_MPI_OFI_LIBRARY_INTERNAL 0
```

7. Add the following **source** command to your shell script to source
   the `vars.sh` script from the installation directory to set up the compiler
   environment each time the instance starts. Do one of the following depending on your shell.

bash shells
Add the following statement to `/home/`username`/.bashrc`
and `/home/`username`/.bash_profile`.

```
source /opt/intel/oneapi/mpi/latest/env/vars.sh
```

csh and tcsh shells
Add the following statement to `/home/`username`/.cshrc`.

```
source /opt/intel/oneapi/mpi/latest/env/vars.csh
```

8. By default, if EFA is not available due to a misconfiguration, Intel MPI defaults to the TCP/IP
   network stack, which might result in slower application performance. You can prevent this by setting
   `I_MPI_OFI_PROVIDER` to `efa`. This causes Intel MPI to fail with the following
   error if EFA is not available:

```
Abort (XXXXXX) on node 0 (rank 0 in comm 0): Fatal error in PMPI_Init: OtherMPI error,
MPIR_Init_thread (XXX)........:
MPID_Init (XXXX)..............:
MPIDI_OFI_mpi_init_hook (XXXX):
open_fabric (XXXX)............:
find_provider (XXXX)..........:
OFI fi_getinfo() failed (ofi_init.c:2684:find_provider:
```

Do one of the following depending on your shell.

bash shells
Add the following statement to
`/home/`username`/.bashrc` and
`/home/`username`/.bash_profile`.

```
export I_MPI_OFI_PROVIDER=efa
```

csh and tcsh shells
Add the following statement to
`/home/`username`/.cshrc`.

```
setenv I_MPI_OFI_PROVIDER efa
```

9. By default, Intel MPI doesn't print debugging information. You can specify different verbosity
   levels to control the debugging information. Possible values (in order of the amount of detail they
   provide) are: `0` (default), `1`, `2`, `3`, `4`,
   `5`. Level `1` and higher prints the `libfabric version` and
   `libfabric provider`. Use `libfabric version` to check whether Intel MPI is
   using the internal Libfabric or the Libfabric that ships with the EFA installer. If it's using
   the internal Libfabric, the version is suffixed with `impi`. Use `libfabric provider`
   to check with Intel MPI is using EFA or the TCP/IP network. If it's using EFA, the value is
   `efa`. If it's using TCP/IP, the value is `tcp;ofi_rxm`.

To enable debugging information, do one of the following depending on your shell.

bash shells
Add the following statement to
`/home/`username`/.bashrc` and
`/home/`username`/.bash_profile`.

```
export I_MPI_DEBUG=`value`
```

csh and tcsh shells
Add the following statement to
`/home/`username`/.cshrc`.

```
setenv I_MPI_DEBUG `value`
```

10. By default, Intel MPI uses the operating system’s shared memory (`shm`) for intra-node
    communication, and it uses Libfabric (`ofi`) only for inter-node communication. Generally, this
    configuration provides the best performance. However, in some cases the Intel MPI shm fabric can cause
    certain applications to hang indefinitely.

To resolve this issue, you can force Intel MPI to use Libfabric for both intra-node and inter-node
communication. To do this, do one of the following depending on your shell.

bash shells
Add the following statement to
`/home/`username`/.bashrc` and
`/home/`username`/.bash_profile`.

```
export I_MPI_FABRICS=ofi
```

csh and tcsh shells
Add the following statement to
`/home/`username`/.cshrc`.

```
setenv I_MPI_FABRICS ofi
```

###### Note

The EFA Libfabric provider uses the operating system's shared memory for intra-node communication.
This means that setting `I_MPI_FABRICS` to `ofi` yields similar performance to
the default `shm:ofi` configuration. 11. Log out of the instance and then log back in.

If you no longer want to use Intel MPI, remove the environment variables from the shell
startup scripts.

## Step 6: Disable ptrace protection

To improve your HPC application's performance, Libfabric uses the instance's local memory
for interprocess communications when the processes are running on the same instance.

The shared memory feature uses Cross Memory Attach (CMA), which is not supported with
_ptrace protection_. If you are using a Linux distribution that has ptrace
protection enabled by default, such as Ubuntu, you must disable it. If your Linux distribution does not have
ptrace protection enabled by default, skip this step.

###### To disable ptrace protection

Do one of the following:

- To temporarily disable ptrace protection for testing purposes, run the following command.

```
`$` sudo sysctl -w kernel.yama.ptrace_scope=0
```

- To permanently disable ptrace protection, add `kernel.yama.ptrace_scope = 0` to
  `/etc/sysctl.d/10-ptrace.conf` and reboot the instance.

## Step 7. Confirm installation

###### To confirm successful installation

1. To confirm that MPI was successfully installed, run the following command:

```
`$` which mpicc
```

    * For Open MPI, the returned path should include `/opt/amazon/`
    * For Intel MPI, the returned path should include `/opt/intel/`.
     If you do not get the expected output, ensure that you have sourced the
     Intel MPI `vars.sh` script.

2. To confirm that the EFA software components and Libfabric were successfully installed,
   run the following command.

```
`$` fi_info -p efa -t FI_EP_RDM
```

The command should return information about the Libfabric EFA interfaces. The following
example shows the command output.

```
provider: efa
    fabric: EFA-fe80::94:3dff:fe89:1b70
    domain: efa_0-rdm
    version: 2.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
```

## Step 8: Install your HPC application

Install the HPC application on the temporary instance. The installation procedure varies
depending on the specific HPC application. For more information,
see [Manage software on your AL2 instance](../../../linux/al2/ug/managing-software.md "../../../linux/al2/ug/managing-software.md") in the _Amazon Linux 2 User Guide_.

###### Note

Refer to your HPC application’s documentation for installation instructions.

## Step 9: Create an EFA-enabled AMI

After you have installed the required software components, you create an AMI that
you can reuse to launch your EFA-enabled instances.

###### To create an AMI from your temporary instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the temporary instance that you created and choose **Actions**,
   **Image**, **Create image**.
4. For **Create image**, do the following:
   1. For **Image name**, enter a descriptive name for the
      AMI.
   2. (Optional) For **Image description**, enter a brief
      description of the purpose of the AMI.
   3. Choose **Create image**.

5. In the navigation pane, choose **AMIs**.
6. Locate the AMI tht you created in the list. Wait for the status to change from
   `pending` to `available` before continuing to the next
   step.

## Step 10: Launch EFA-enabled instances into a cluster

placement group

Launch your EFA-enabled instances into a cluster placement group using the EFA-enabled
AMI that you created in **Step 7**, and the
EFA-enabled security group that you created in **Step
1**.

###### Note

- It is not an absolute requirement to launch your EFA-enabled instances into
  a cluster placement group. However, we do recommend running your EFA-enabled
  instances in a cluster placement group as it launches the instances into a
  low-latency group in a single Availability Zone.
- To ensure that capacity is available as you scale your cluster’s instances, you
  can create a Capacity Reservation for your cluster placement group. For more information, see
  [Use Capacity Reservations with cluster placement groups](cr-cpg.md "cr-cpg.md").

###### To launch an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and then choose
   **Launch Instances** to open the new launch instance wizard.
3. (_Optional_) In the **Name and tags** section,
   provide a name for the instance, such as `EFA-instance`. The name is assigned
   to the instance as a resource tag (`Name=`EFA-instance``).
4. In the **Application and OS Images** section, choose **My
   AMIs**, and then select the AMI that you created in the previous step.
5. In the **Instance type** section, select a
   [supported instance type](efa.md#efa-instance-types "efa.md#efa-instance-types").
6. In the **Key pair** section, select the key pair to use for the
   instance.
7. In the **Network settings** section, choose **Edit**,
   and then do the following:
   1. For **Subnet**, choose the subnet in which to launch the
      instance. If you do not select a subnet, you can't enable the instance for EFA.
   2. For **Firewall (security groups)**, choose **Select
      existing security group**, and then select the security group that you
      created in the previous step.
   3. Expand the **Advanced network configuration** section.

   For **Network interface 1**, select **Network card index = 0**,
   **Device index = 0**, and **Interface type = EFA with ENA**.

   (_Optional_) If you are using a multi-card instance type, such as `p4d.24xlarge`
   or `p5.48xlarge`, for each additional network interface required, choose
   **Add network interface**, for **Network card index**
   select the next unused index, and then select **Device index = 1**
   and **Interface type = EFA with ENA** or **EFA-only**.

8. (_Optional_) In the **Storage** section, configure the
   volumes as needed.
9. In the **Advanced details** section, for **Placement group name**,
   select the cluster placement group into which to launch the instances. If you need to
   create a new cluster placement group, choose **Create new placement group**.
10. In the **Summary** panel on the right, for **Number of
    instances**, enter the number of EFA-enabled instances that you want to launch,
    and then choose **Launch instance**.

## Step 11: Terminate the temporary instance

At this point, you no longer need the instance that you launched in [Step 2](#efa-start-tempinstance "#efa-start-tempinstance"). You can terminate the instance
to stop incurring charges for it.

###### To terminate the temporary instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the temporary instance that you created and then choose **Actions**,
   **Instance state**, **Terminate (delete) instance**.
4. When prompted for confirmation, choose **Terminate (delete)**.

## Step 12: Enable passwordless SSH

To enable your applications to run across all of the instances in your cluster,
you must enable passwordless SSH access from the leader node to the member nodes. The leader
node is the instance from which you run your applications. The remaining instances in the
cluster are the member nodes.

###### To enable passwordless SSH between the instances in the cluster

1. Select one instance in the cluster as the leader node, and connect to it.
2. Disable `strictHostKeyChecking` and enable
   `ForwardAgent` on the leader node. Open `~/.ssh/config`
   using your preferred text editor and add the following.

```
Host *
    ForwardAgent yes
Host *
    StrictHostKeyChecking no
```

3. Generate an RSA key pair.

```
`$` ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
```

The key pair is created in the `$HOME/.ssh/` directory. 4. Change the permissions of the private key on the leader node.

```
`$` chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/config
```

5. Open `~/.ssh/id_rsa.pub` using your preferred text editor and copy
   the key.
6. For each member node in the cluster, do the following:
   1. Connect to the instance.
   2. Open `~/.ssh/authorized_keys` using your preferred text
      editor and add the public key that you copied earlier.

7. To test that the passwordless SSH is functioning as expected, connect to your leader node
   and run the following command.

```
`$` ssh `member_node_private_ip`
```

You should connect to the member node without being prompted for a key or password.
