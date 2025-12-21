# Get started with EFA and NCCL for ML workloads on Amazon EC2

The NVIDIA Collective Communications Library (NCCL) is a library of standard collective
communication routines for multiple GPUs across a single node or multiple nodes. NCCL
can be used together with EFA, Libfabric, and MPI to support various machine learning
workloads. For more information, see the [NCCL](https://developer.nvidia.com/nccl "https://developer.nvidia.com/nccl") website.

###### Requirements

- Only accelerated computing P series instance types are supported. For more
  information, see [Amazon EC2 accelerated computing instances](../../../ec2/latest/instancetypes/ac.md#ac-sizes "../../../ec2/latest/instancetypes/ac.md#ac-sizes").
- Only Amazon Linux 2023, Amazon Linux 2, Ubuntu 24.04, and Ubuntu 22.04 base AMIs are supported.
- Only NCCL 2.4.2 and later is supported with EFA.
  For more information about running machine learning workloads with EFA and
  NCCL using an AWS Deep Learning AMIs, see [Using EFA on the DLAMI](../../../dlami/latest/devguide/tutorial-efa-using.md "../../../dlami/latest/devguide/tutorial-efa-using.md") in the _AWS Deep Learning AMIs Developer Guide_.

###### Steps

- [Step 1: Prepare an EFA-enabled security group](#nccl-start-base-setup "#nccl-start-base-setup")
- [Step 2: Launch a temporary instance](#nccl-start-base-temp "#nccl-start-base-temp")
- [Step 3: Install Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN](#nccl-start-base-drivers "#nccl-start-base-drivers")
- [Step 4: Install GDRCopy](#nccl-start-base-gdrcopy "#nccl-start-base-gdrcopy")
- [Step 5: Install the EFA software](#nccl-start-base-enable "#nccl-start-base-enable")
- [Step 6: Install NCCL](#nccl-start-base-nccl "#nccl-start-base-nccl")
- [Step 7: Install the NCCL tests](#nccl-start-base-tests "#nccl-start-base-tests")
- [Step 8: Test your EFA and NCCL configuration](#nccl-start-base-test "#nccl-start-base-test")
- [Step 9: Install your machine learning applications](#nccl-start-base-app "#nccl-start-base-app")
- [Step 10: Create an EFA and NCCL-enabled AMI](#nccl-start-base-ami "#nccl-start-base-ami")
- [Step 11: Terminate the temporary instance](#nccl-start-base-terminate "#nccl-start-base-terminate")
- [Step 12: Launch EFA and NCCL-enabled instances into a cluster
  placement group](#nccl-start-base-cluster "#nccl-start-base-cluster")
- [Step 13: Enable passwordless SSH](#nccl-start-base-passwordless "#nccl-start-base-passwordless")

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
   one of the supported operating systems.
5. In the **Instance type** section, select a supported instance
   type.
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

8. In the **Storage** section, configure the volumes as needed.

###### Note

You must provision an additional 10 to 20 GiB of storage for the Nvidia CUDA Toolkit.
If you do not provision enough storage, you will receive an `insufficient disk 
 space` error when attempting to install the Nvidia drivers and CUDA
toolkit. 9. In the **Summary** panel on the right, choose **Launch
instance**.

## Step 3: Install Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN

Amazon Linux 2023 and Amazon Linux 2

###### To install the Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN

1. To ensure that all of your software packages are up to date,
   perform a quick software update on your instance.

```
`$` sudo yum upgrade -y && sudo reboot
```

After the instance has rebooted, reconnect to it. 2. Install the utilities that are needed to install the Nvidia GPU drivers and the Nvidia
CUDA toolkit.

```
`$` sudo yum groupinstall 'Development Tools' -y
```

3. Disable the `nouveau` open source drivers.
   1. Install the required utilities and the kernel headers package for the version of
      the kernel that you are currently running.

   ```
   `$` sudo yum install -y wget kernel-devel-$(uname -r) kernel-headers-$(uname -r)
   ```

   2. Add `nouveau` to the `/etc/modprobe.d/blacklist.conf` deny list
      file.

   ```
   `$` cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf
   blacklist vga16fb
   blacklist nouveau
   blacklist rivafb
   blacklist nvidiafb
   blacklist rivatv
   EOF
   ```

   3. Append `GRUB_CMDLINE_LINUX="rdblacklist=nouveau"` to the `grub` file and rebuild the Grub configuration.

   ```
   `$` echo 'GRUB_CMDLINE_LINUX="rdblacklist=nouveau"' | sudo tee -a /etc/default/grub \
   && sudo grub2-mkconfig -o /boot/grub2/grub.cfg
   ```

4. Reboot the instance and reconnect to it.
5. Prepare the required repositories
   1. Enable the EPEL repository and set the distribution to `rhel7`.

   ```
   `$` sudo amazon-linux-extras install epel \
   && distribution='rhel7'
   ```

   2. Set up the CUDA network repository and update the repository cache.

   ```
   `$` ARCH=$( /bin/arch ) \
   && sudo yum-config-manager --add-repo http://developer.download.nvidia.com/compute/cuda/repos/$distribution/${ARCH}/cuda-$distribution.repo \
   && sudo yum clean expire-cache
   ```

   3. (_Kernel version 5.10 only_) Perform these steps only if you are using Amazon Linux 2 with
      kernel version 5.10. If you are using Amazon Linux 2 with kernel version 4.12, skip these steps. To check your
      kernel version, run **uname -r**.
      1. Create the Nvidia driver configuration file named `/etc/dkms/nvidia.conf`.

      ```
      `$` sudo mkdir -p /etc/dkms \
      && echo "MAKE[0]=\"'make' -j2 module SYSSRC=\${kernel_source_dir} IGNORE_XEN_PRESENCE=1 IGNORE_PREEMPT_RT_PRESENCE=1 IGNORE_CC_MISMATCH=1 CC=/usr/bin/gcc10-gcc\"" | sudo tee /etc/dkms/nvidia.conf
      ```

      2. (`p4d.24xlarge` and `p5.48xlarge` only) Copy the Nvidia driver configuration file.

      ```
      `$` sudo cp /etc/dkms/nvidia.conf /etc/dkms/nvidia-open.conf
      ```

6. Install the Nvidia GPU drivers, NVIDIA CUDA toolkit, and cuDNN.

```
`$` sudo yum clean all \
&& sudo yum -y install nvidia-driver-latest-dkms \
&& sudo yum -y install cuda-drivers-fabricmanager cuda libcudnn8-devel
```

7. Reboot the instance and reconnect to it.
8. (`p4d.24xlarge` and `p5.48xlarge` only) Start the Nvidia Fabric Manager service, and ensure that it starts
   automatically when the instance starts. Nvidia Fabric Manager is required for NV Switch Management.

```
`$` sudo systemctl enable nvidia-fabricmanager && sudo systemctl start nvidia-fabricmanager
```

9. Ensure that the CUDA paths are set each time that the instance starts.
   - For _bash_ shells, add the following statements to
     `/home/`username`/.bashrc` and
     `/home/`username`/.bash_profile`.

   ```
   export PATH=/usr/local/cuda/bin:$PATH
   export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
   ```

   - For _tcsh_ shells, add the following statements to
     `/home/`username`/.cshrc`.

   ```
   setenv PATH=/usr/local/cuda/bin:$PATH
   setenv LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
   ```

10. To confirm that the Nvidia GPU drivers are functional, run the following command.

```
`$` nvidia-smi -q | head
```

The command should return information about the Nvidia GPUs, Nvidia
GPU drivers, and Nvidia CUDA toolkit.

Ubuntu 24.04 and Ubuntu 22.04

###### To install the Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN

1. To ensure that all of your software packages are up to date,
   perform a quick software update on your instance.

```
`$` sudo apt-get update && sudo apt-get upgrade -y
```

2. Install the utilities that are needed to install the Nvidia GPU drivers and the Nvidia
   CUDA toolkit.

```
`$` sudo apt-get update && sudo apt-get install build-essential -y
```

3. To use the Nvidia GPU driver, you must first disable the `nouveau` open
   source drivers.
   1. Install the required utilities and the kernel headers package for the version of
      the kernel that you are currently running.

   ```
   `$` sudo apt-get install -y gcc make linux-headers-$(uname -r)
   ```

   2. Add `nouveau` to the `/etc/modprobe.d/blacklist.conf` deny list
      file.

   ```
   `$` cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf
   blacklist vga16fb
   blacklist nouveau
   blacklist rivafb
   blacklist nvidiafb
   blacklist rivatv
   EOF
   ```

   3. Open `/etc/default/grub` using your preferred text editor and add the following.

   ```
   GRUB_CMDLINE_LINUX="rdblacklist=nouveau"
   ```

   4. Rebuild the Grub configuration.

   ```
   `$` sudo update-grub
   ```

4. Reboot the instance and reconnect to it.
5. Add the CUDA repository and install the Nvidia GPU drivers, NVIDIA CUDA toolkit, and cuDNN.
   - `p3dn.24xlarge`

   ```
   `$` sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub \
   && wget -O /tmp/deeplearning.deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/nvidia-machine-learning-repo-ubuntu2004_1.0.0-1_amd64.deb \
   && sudo dpkg -i /tmp/deeplearning.deb \
   && wget -O /tmp/cuda.pin https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin \
   && sudo mv /tmp/cuda.pin /etc/apt/preferences.d/cuda-repository-pin-600 \
   && sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub \
   && sudo add-apt-repository 'deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /' \
   && sudo apt update \
   && sudo apt install nvidia-dkms-535 \
   && sudo apt install -o Dpkg::Options::='--force-overwrite' cuda-drivers-535 cuda-toolkit-12-3 libcudnn8 libcudnn8-dev -y
   ```

   - `p4d.24xlarge` and `p5.48xlarge`

   ```
   `$` sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub \
   && wget -O /tmp/deeplearning.deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/nvidia-machine-learning-repo-ubuntu2004_1.0.0-1_amd64.deb \
   && sudo dpkg -i /tmp/deeplearning.deb \
   && wget -O /tmp/cuda.pin https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin \
   && sudo mv /tmp/cuda.pin /etc/apt/preferences.d/cuda-repository-pin-600 \
   && sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub \
   && sudo add-apt-repository 'deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /' \
   && sudo apt update \
   && sudo apt install nvidia-kernel-open-535 \
   && sudo apt install -o Dpkg::Options::='--force-overwrite' cuda-drivers-535 cuda-toolkit-12-3 libcudnn8 libcudnn8-dev -y
   ```

6. Reboot the instance and reconnect to it.
7. (`p4d.24xlarge` and `p5.48xlarge` only) Install the Nvidia Fabric Manager.
   1. You must install the version of the Nvidia Fabric Manager that matches the version of the
      Nvidia kernel module that you installed in the previous step.

   Run the following command to determine the version of the Nvidia kernel module.

   ```
   `$` cat /proc/driver/nvidia/version | grep "Kernel Module"
   ```

   The following is example output.

   ```
   NVRM version: NVIDIA UNIX x86_64 Kernel Module  **450**.42.01  Tue Jun 15 21:26:37 UTC 2021
   ```

   In the example above, major version `450` of the kernel module was installed. This means that you need
   to install Nvidia Fabric Manager version `450`. 2. Install the Nvidia Fabric Manager. Run the following command and specify the major version
   identified in the previous step.

   ```
   `$` sudo apt install -o Dpkg::Options::='--force-overwrite' nvidia-fabricmanager-`major_version_number`
   ```

   For example, if major version `450` of the kernel module was installed, use the following command to
   install the matching version of Nvidia Fabric Manager.

   ```
   `$` sudo apt install -o Dpkg::Options::='--force-overwrite' nvidia-fabricmanager-450
   ```

   3. Start the service, and ensure that it starts automatically when the instance starts.
      Nvidia Fabric Manager is required for NV Switch Management.

   ```
   `$` sudo systemctl start nvidia-fabricmanager && sudo systemctl enable nvidia-fabricmanager
   ```

8. Ensure that the CUDA paths are set each time that the instance starts.
   - For _bash_ shells, add the following statements to
     `/home/`username`/.bashrc` and
     `/home/`username`/.bash_profile`.

   ```
   export PATH=/usr/local/cuda/bin:$PATH
   export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
   ```

   - For _tcsh_ shells, add the following statements to
     `/home/`username`/.cshrc`.

   ```
   setenv PATH=/usr/local/cuda/bin:$PATH
   setenv LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
   ```

9. To confirm that the Nvidia GPU drivers are functional, run the following command.

```
`$` nvidia-smi -q | head
```

The command should return information about the Nvidia GPUs, Nvidia
GPU drivers, and Nvidia CUDA toolkit.

## Step 4: Install GDRCopy

Install GDRCopy to improve the performance of Libfabric. For more information about
GDRCopy, see the [GDRCopy repository](https://github.com/NVIDIA/gdrcopy "https://github.com/NVIDIA/gdrcopy").

Amazon Linux 2023 and Amazon Linux 2

###### To install GDRCopy

1. Install the required dependencies.

```
`$` sudo yum -y install dkms rpm-build make check check-devel subunit subunit-devel
```

2. Download and extract the GDRCopy package.

```
`$` wget https://github.com/NVIDIA/gdrcopy/archive/refs/tags/v2.4.tar.gz \
&& tar xf v2.4.tar.gz ; cd gdrcopy-2.4/packages
```

3. Build the GDRCopy RPM package.

```
`$` CUDA=/usr/local/cuda ./build-rpm-packages.sh
```

4. Install the GDRCopy RPM package.

```
`$` sudo rpm -Uvh gdrcopy-kmod-2.4-1dkms.noarch*.rpm \
&& sudo rpm -Uvh gdrcopy-2.4-1.x86_64*.rpm \
&& sudo rpm -Uvh gdrcopy-devel-2.4-1.noarch*.rpm
```

Ubuntu 24.04 and Ubuntu 22.04

###### To install GDRCopy

1. Install the required dependencies.

```
`$` sudo apt -y install build-essential devscripts debhelper check libsubunit-dev fakeroot pkg-config dkms
```

2. Download and extract the GDRCopy package.

```
`$` wget https://github.com/NVIDIA/gdrcopy/archive/refs/tags/v2.4.tar.gz \
&& tar xf v2.4.tar.gz \
&& cd gdrcopy-2.4/packages
```

3. Build the GDRCopy RPM package.

```
`$` CUDA=/usr/local/cuda ./build-deb-packages.sh
```

4. Install the GDRCopy RPM package.

```
`$` sudo dpkg -i gdrdrv-dkms_2.4-1_amd64.*.deb \
&& sudo dpkg -i libgdrapi_2.4-1_amd64.*.deb \
&& sudo dpkg -i gdrcopy-tests_2.4-1_amd64.*.deb \
&& sudo dpkg -i gdrcopy_2.4-1_amd64.*.deb
```

## Step 5: Install the EFA software

Install the EFA-enabled kernel, EFA drivers, Libfabric, aws-ofi-nccl plugin, and Open
MPI stack that is required to support EFA on your instance.

###### To install the EFA software

1. Connect to the instance you launched. For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").
2. Download the EFA software installation files. The software installation files are packaged into a compressed tarball (`.tar.gz`) file.
   To download the latest _stable_ version, use the following command.

You can also get the latest version by replacing the version number with `latest` in the preceding command.

```
`$` curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.46.0.tar.gz
```

3. (_Optional_) Verify the authenticity and integrity of the EFA tarball (`.tar.gz`) file.

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
    `$` wget https://efa-installer.amazonaws.com/aws-efa-installer-1.46.0.tar.gz.sig && gpg --verify ./aws-efa-installer-1.46.0.tar.gz.sig
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

[Show moreShow less](# "#") 4. Extract the files from the compressed `.tar.gz` file and navigate into
the extracted directory.

```
`$` tar -xf aws-efa-installer-1.46.0.tar.gz && cd aws-efa-installer
```

5. Run the EFA software installation script.

###### Note

From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default.
Unless you need Open MPI 5, we recommend that you install only Open MPI 4.1. The
following command installs Open MPI 4.1 only. If you want to install Open MPI
4.1 and Open MPI 5, remove `--mpi=openmpi4`.

```
`$` sudo ./efa_installer.sh -y --mpi=openmpi4
```

**Libfabric** is installed in the `/opt/amazon/efa`
directory. The **aws-ofi-nccl plugin** is installed in the
`/opt/amazon/ofi-nccl` directory. **Open MPI**
is installed in the `/opt/amazon/openmpi` directory. 6. If the EFA installer prompts you to reboot the instance, do so and then reconnect
to the instance. Otherwise, log out of the instance and then log back in to complete
the installation. 7. Confirm that the EFA software components were successfully installed.

```
`$` fi_info -p efa -t FI_EP_RDM
```

The command should return information about the Libfabric EFA interfaces. The following
example shows the command output.

    * `p3dn.24xlarge` with single network interface



    ```
    provider: efa
    fabric: EFA-fe80::94:3dff:fe89:1b70
    domain: efa_0-rdm
    version: 2.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
    ```
    * `p4d.24xlarge` and `p5.48xlarge` with multiple network interfaces



    ```
    provider: efa
    fabric: EFA-fe80::c6e:8fff:fef6:e7ff
    domain: efa_0-rdm
    version: 111.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
    provider: efa
    fabric: EFA-fe80::c34:3eff:feb2:3c35
    domain: efa_1-rdm
    version: 111.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
    provider: efa
    fabric: EFA-fe80::c0f:7bff:fe68:a775
    domain: efa_2-rdm
    version: 111.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
    provider: efa
    fabric: EFA-fe80::ca7:b0ff:fea6:5e99
    domain: efa_3-rdm
    version: 111.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA

    ```

## Step 6: Install NCCL

Install NCCL. For more information about NCCL, see the
[NCCL repository](https://github.com/NVIDIA/nccl "https://github.com/NVIDIA/nccl").

###### To install NCCL

1. Navigate to the `/opt` directory.

```
`$` cd /opt
```

2. Clone the official NCCL repository to the instance and navigate into the local
   cloned repository.

```
`$` sudo git clone https://github.com/NVIDIA/nccl.git -b v2.23.4-1 && cd nccl
```

3. Build and install NCCL and specify the CUDA installation directory.

```
`$` sudo make -j src.build CUDA_HOME=/usr/local/cuda
```

## Step 7: Install the NCCL tests

Install the NCCL tests. The NCCL tests enable you to confirm that NCCL is properly
installed and that it is operating as expected. For more information about the
NCCL tests, see the [nccl-tests
repository](https://github.com/NVIDIA/nccl-tests "https://github.com/NVIDIA/nccl-tests").

###### To install the NCCL tests

1. Navigate to your home directory.

```
`$` cd $HOME
```

2. Clone the official nccl-tests repository to the instance and navigate into the
   local cloned repository.

```
`$` git clone https://github.com/NVIDIA/nccl-tests.git && cd nccl-tests
```

3. Add the Libfabric directory to the `LD_LIBRARY_PATH` variable.
   - Amazon Linux 2023 and Amazon Linux 2

   ```
   `$` export LD_LIBRARY_PATH=`/opt/amazon/efa/lib64`:$LD_LIBRARY_PATH
   ```

   - Ubuntu 24.04 and Ubuntu 22.04

   ```
   `$` export LD_LIBRARY_PATH=`/opt/amazon/efa/lib`:$LD_LIBRARY_PATH
   ```

4. Install the NCCL tests and specify the MPI, NCCL, and CUDA installation directories.

```
`$` make MPI=1 MPI_HOME=`/opt/amazon/openmpi` NCCL_HOME=`/opt/nccl/build` CUDA_HOME=`/usr/local/cuda`
```

## Step 8: Test your EFA and NCCL configuration

Run a test to ensure that your temporary instance is properly configured for EFA and NCCL.

###### To test your EFA and NCCL configuration

1. Create a host file that specifies the hosts on which to run the tests. The following command creates a
   host file named `my-hosts` that includes a reference to the instance itself.

IMDSv2

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/local-ipv4 >> my-hosts`
```

IMDSv1

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/local-ipv4 >> my-hosts`
```

2.  Run the test and specify the host file (`--hostfile`) and the number of GPUs to use
    (`-n`). The following command runs the `all_reduce_perf` test on 8
    GPUs on the instance itself, and specifies the following environment variables.

        * `FI_EFA_USE_DEVICE_RDMA=1`—(`p4d.24xlarge` only) uses the device's RDMA functionality for
         one-sided and two-sided transfer.
        * `NCCL_DEBUG=INFO`—enables detailed debugging output. You can also
         specify `VERSION` to print only the NCCL version at the start of the test, or
         `WARN` to receive only error messages.

    For more information about the NCCL test arguments, see the
    [NCCL Tests README](https://github.com/NVIDIA/nccl-tests/blob/master/README.md "https://github.com/NVIDIA/nccl-tests/blob/master/README.md")
    in the official nccl-tests repository.

        * `p3dn.24xlarge`



        ```
        `$` /opt/amazon/openmpi/bin/mpirun \
        -x LD_LIBRARY_PATH=/opt/nccl/build/lib:/usr/local/cuda/lib64:/opt/amazon/efa/lib:/opt/amazon/openmpi/lib:/opt/amazon/ofi-nccl/lib:$LD_LIBRARY_PATH \
        -x NCCL_DEBUG=INFO \
        --hostfile my-hosts -n 8 -N 8 \
        --mca pml ^cm --mca btl tcp,self --mca btl_tcp_if_exclude lo,docker0 --bind-to none \
        $HOME/nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1 -c 1 -n 100
        ```
        * `p4d.24xlarge` and `p5.48xlarge`



        ```
        `$` /opt/amazon/openmpi/bin/mpirun \
        -x FI_EFA_USE_DEVICE_RDMA=1 \
        -x LD_LIBRARY_PATH=/opt/nccl/build/lib:/usr/local/cuda/lib64:/opt/amazon/efa/lib:/opt/amazon/openmpi/lib:/opt/amazon/ofi-nccl/lib:$LD_LIBRARY_PATH \
        -x NCCL_DEBUG=INFO \
        --hostfile my-hosts -n 8 -N 8 \
        --mca pml ^cm --mca btl tcp,self --mca btl_tcp_if_exclude lo,docker0 --bind-to none \
        $HOME/nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1 -c 1 -n 100
        ```

3.  You can confirm that EFA is active as the underlying provider for NCCL when
    the `NCCL_DEBUG` log is printed.

```
ip-192-168-2-54:14:14 [0] NCCL INFO NET/OFI Selected Provider is efa*
```

The following additional information is displayed when using a `p4d.24xlarge` instance.

```
ip-192-168-2-54:14:14 [0] NCCL INFO NET/OFI Running on P4d platform, Setting NCCL_TOPO_FILE environment variable to /home/ec2-user/install/plugin/share/aws-ofi-nccl/xml/p4d-24xl-topo.xml
```

## Step 9: Install your machine learning applications

Install the machine learning applications on the temporary instance. The installation procedure varies
depending on the specific machine learning application. For more information about installing
software on your Linux instance, see [Manage software on your Amazon Linux 2 instance](../../../linux/al2/ug/managing-software.md "../../../linux/al2/ug/managing-software.md").

###### Note

Refer to your machine learning application’s documentation for installation
instructions.

## Step 10: Create an EFA and NCCL-enabled AMI

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

## Step 11: Terminate the temporary instance

At this point, you no longer need the temporary instance that you launched.
You can terminate the instance to stop incurring charges for it.

###### To terminate the temporary instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the temporary instance that you created and then choose **Actions**,
   **Instance state**, **Terminate instance**.
4. When prompted for confirmation, choose **Terminate**.

## Step 12: Launch EFA and NCCL-enabled instances into a cluster

placement group

Launch your EFA and NCCL-enabled instances into a cluster placement group using the EFA-enabled
AMI and the EFA-enabled security group that you created earlier.

###### Note

- It is not an absolute requirement to launch your EFA-enabled instances into
  a cluster placement group. However, we do recommend running your EFA-enabled
  instances in a cluster placement group as it launches the instances into a
  low-latency group in a single Availability Zone.
- To ensure that capacity is available as you scale your cluster’s instances, you
  can create a Capacity Reservation for your cluster placement group. For more information, see
  [Use Capacity Reservations with cluster placement groups](cr-cpg.md "cr-cpg.md").

New console

###### To launch a temporary instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and then choose
   **Launch Instances** to open the new launch instance wizard.
3. (_Optional_) In the **Name and tags** section,
   provide a name for the instance, such as `EFA-instance`. The name is assigned
   to the instance as a resource tag (`Name=`EFA-instance``).
4. In the **Application and OS Images** section, choose **My
   AMIs**, and then select the AMI that you created in the previous step.
5. In the **Instance type** section, select either `p3dn.24xlarge`
   or `p4d.24xlarge`.
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
   and **Interface type = EFA eith ENA** or **EFA-only**.

8. (_Optional_) In the **Storage** section, configure the
   volumes as needed.
9. In the **Advanced details** section, for **Placement group name**,
   select the cluster placement group into which to launch the instance. If you need to
   create a new cluster placement group, choose **Create new placement group**.
10. In the **Summary** panel on the right, for **Number of
    instances**, enter the number of EFA-enabled instances that you want to launch,
    and then choose **Launch instance**.

Old console

###### To launch your EFA and NCCL-enabled instances into a cluster placement group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch Instance**.
3. On the **Choose an AMI** page, choose **My AMIs**,
   find the AMI that you created earlier, and then choose **Select**.
4. On the **Choose an Instance Type** page, select
   **p3dn.24xlarge** and then choose **Next: Configure
   Instance Details**.
5. On the **Configure Instance Details** page, do the following:
   1. For **Number of instances**, enter the number of EFA and
      NCCL-enabled instances that you want to launch.
   2. For **Network** and **Subnet**, select the VPC
      and subnet into which to launch the instances.
   3. For **Placement group**, select **Add instance to
      placement group**.
   4. For **Placement group name**, select **Add to a new
      placement group**, and then enter a descriptive name for the placement group.
      Then for **Placement group strategy**, select
      **cluster**.
   5. For **EFA**, choose **Enable**.
   6. In the **Network Interfaces** section, for device
      **eth0**, choose **New network interface**. You
      can optionally specify a primary IPv4 address and one or more secondary IPv4
      addresses. If you are launching the instance into a subnet that has an associated
      IPv6 CIDR block, you can optionally specify a primary IPv6 address and one or more
      secondary IPv6 addresses.
   7. Choose **Next: Add Storage**.

6. On the **Add Storage** page, specify the volumes to attach to the instances in
   addition to the volumes specified by the AMI (such as the root device volume). Then choose
   **Next: Add Tags**.
7. On the **Add Tags** page, specify tags for the instances, such as a
   user-friendly name, and then choose **Next: Configure Security
   Group**.
8. On the **Configure Security Group** page, for **Assign a
   security group**, select **Select an existing security
   group**, and then select the security group that you created earlier.
9. Choose **Review and Launch**.
10. On the **Review Instance Launch** page, review the settings, and then
    choose **Launch** to choose a key pair and to launch your
    instances.

## Step 13: Enable passwordless SSH

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
