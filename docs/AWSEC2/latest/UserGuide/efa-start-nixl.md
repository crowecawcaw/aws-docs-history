

# Get started with EFA and NIXL for inference workloads on Amazon EC2
<a name="efa-start-nixl"></a>

The NVIDIA Inference Xfer Library (NIXL) is a high-throughput, low-latency communication library designed specifically for disaggregated inference workloads. NIXL can be used together with EFA and Libfabric to support KV-cache transfer between prefill and decode nodes, and it enables efficient KV-cache movement between various storage layers. For more information, see the [NIXL](https://github.com/ai-dynamo/nixl) website.

**Requirements**
+ Only Ubuntu 24.04 and Ubuntu 22.04 base AMIs are supported.
+ EFA supports only NIXL 1.0.0 and later.

**Topics**

## Step 1: Prepare an EFA-enabled security group
<a name="nixl-start-base-setup"></a>

An EFA requires a security group that allows all inbound and outbound traffic to and from the security group itself. The following procedure creates a security group that allows all inbound and outbound traffic to and from itself, and that allows inbound SSH traffic from any IPv4 address for SSH connectivity.

**Important**  
This security group is intended for testing purposes only. For your production environments, we recommend that you create an inbound SSH rule that allows traffic only from the IP address from which you are connecting, such as the IP address of your computer, or a range of IP addresses in your local network.

For other scenarios, see [Security group rules for different use cases](security-group-rules-reference.md).

**To create an EFA-enabled security group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Security Groups** and then choose **Create security group**.

1. In the **Create security group** window, do the following:

   1. For **Security group name**, enter a descriptive name for the security group, such as `EFA-enabled security group`.

   1. (Optional) For **Description**, enter a brief description of the security group.

   1. For **VPC**, select the VPC into which you intend to launch your EFA-enabled instances.

   1. Choose **Create security group**.

1. Select the security group that you created, and on the **Details** tab, copy the **Security group ID**.

1. With the security group still selected, choose **Actions**, **Edit inbound rules**, and then do the following:

   1. Choose **Add rule**.

   1. For **Type**, choose **All traffic**.

   1. For **Source type**, choose **Custom** and paste the security group ID that you copied into the field.

   1. Choose **Add rule**.

   1. For **Type**, choose **SSH**.

   1. For **Source type**, choose **Anywhere-IPv4**.

   1. Choose **Save rules**.

1. With the security group still selected, choose **Actions**, **Edit outbound rules**, and then do the following:

   1. Choose **Add rule**.

   1. For **Type**, choose **All traffic**.

   1. For **Destination type**, choose **Custom** and paste the security group ID that you copied into the field.

   1. Choose **Save rules**.

**Important**  
The self-referencing inbound and outbound rules (allowing all traffic to and from the security group itself) are mandatory for EFA to function. Without these rules, EFA traffic between instances will be blocked.

## Step 2: Launch a temporary instance
<a name="nixl-start-base-temp"></a>

Launch a temporary instance that you can use to install and configure the EFA software components. You use this instance to create an EFA-enabled AMI from which you can launch your EFA-enabled instances.

**To launch a temporary instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**, and then choose **Launch Instances** to open the new launch instance wizard.

1. (*Optional*) In the **Name and tags** section, provide a name for the instance, such as `EFA-instance`. The name is assigned to the instance as a resource tag (`Name={{EFA-instance}}`).

1. In the **Application and OS Images** section, select an AMI for one of the supported operating systems. You can also select a supported DLAMI found on the [DLAMI Release Notes Page](https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes).

1. In the **Instance type** section, select a supported instance type.

1. In the **Key pair** section, select the key pair to use for the instance.

1. In the **Network settings** section, choose **Edit**, and then do the following:

   1. For **Subnet**, choose the subnet in which to launch the instance. If you do not select a subnet, you can't enable the instance for EFA.

   1. For **Firewall (security groups)**, choose **Select existing security group**, and then select the security group that you created in the previous step.

   1. Expand the **Advanced network configuration** section.

      For **Network interface 1**, select **Network card index = 0**, **Device index = 0**, and **Interface type = EFA with ENA**.

      (*Optional*) If you are using a multi-card instance type, such as `p4d.24xlarge` or `p5.48xlarge`, for each additional network interface required, choose **Add network interface**, for **Network card index** select the next unused index, and then select **Device index = 1** and **Interface type = EFA with ENA** or **EFA-only**.

1. In the **Storage** section, configure the volumes as needed.
**Note**  
You must provision an additional 10 to 20 GiB of storage for the Nvidia CUDA Toolkit. If you do not provision enough storage, you will receive an `insufficient disk space` error when attempting to install the Nvidia drivers and CUDA toolkit.

1. In the **Summary** panel on the right, choose **Launch instance**.

**Important**  
Skip Step 3 if your AMI already includes Nvidia GPU drivers, the CUDA toolkit, and cuDNN, or if you are using a non-GPU instance.

## Step 3: Install Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN
<a name="nixl-start-base-drivers"></a>

**To install the Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN**

1. To ensure that all of your software packages are up to date, perform a quick software update on your instance.

   ```
   $ sudo apt-get update && sudo apt-get upgrade -y
   ```

1. Install the utilities that are needed to install the Nvidia GPU drivers and the Nvidia CUDA toolkit.

   ```
   $ sudo apt-get install build-essential -y
   ```

1. To use the Nvidia GPU driver, you must first disable the `nouveau` open source drivers.

   1. Install the required utilities and the kernel headers package for the version of the kernel that you are currently running.

      ```
      $ sudo apt-get install -y gcc make linux-headers-$(uname -r)
      ```

   1. Add `nouveau` to the `/etc/modprobe.d/blacklist.conf `deny list file.

      ```
      $ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf
      blacklist vga16fb
      blacklist nouveau
      blacklist rivafb
      blacklist nvidiafb
      blacklist rivatv
      EOF
      ```

   1. Open `/etc/default/grub` using your preferred text editor and add the following.

      ```
      GRUB_CMDLINE_LINUX="rdblacklist=nouveau"
      ```

   1. Rebuild the Grub configuration.

      ```
      $ sudo update-grub
      ```

1. Reboot the instance and reconnect to it.

1. Add the CUDA repository and install the Nvidia GPU drivers, NVIDIA CUDA toolkit, and cuDNN.

   ```
   $ sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub \
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

1. Reboot the instance and reconnect to it.

1. (`p4d.24xlarge` and `p5.48xlarge` only) Install the Nvidia Fabric Manager.

   1. You must install the version of the Nvidia Fabric Manager that matches the version of the Nvidia kernel module that you installed in the previous step.

      Run the following command to determine the version of the Nvidia kernel module.

      ```
      $ cat /proc/driver/nvidia/version | grep "Kernel Module"
      ```

      The following is example output.

      ```
      NVRM version: NVIDIA UNIX x86_64 Kernel Module  450.42.01  Tue Jun 15 21:26:37 UTC 2021
      ```

      In the example above, major version `450` of the kernel module was installed. This means that you need to install Nvidia Fabric Manager version `450`.

   1. Install the Nvidia Fabric Manager. Run the following command and specify the major version identified in the previous step.

      ```
      $ sudo apt install -o Dpkg::Options::='--force-overwrite' nvidia-fabricmanager-{{major_version_number}}
      ```

      For example, if major version `450` of the kernel module was installed, use the following command to install the matching version of Nvidia Fabric Manager.

      ```
      $ sudo apt install -o Dpkg::Options::='--force-overwrite' nvidia-fabricmanager-450
      ```

   1. Start the service, and ensure that it starts automatically when the instance starts. Nvidia Fabric Manager is required for NV Switch Management.

      ```
      $ sudo systemctl start nvidia-fabricmanager && sudo systemctl enable nvidia-fabricmanager
      ```

1. Ensure that the CUDA paths are set each time that the instance starts.
   + For *bash* shells, add the following statements to `/home/{{username}}/.bashrc` and `/home/{{username}}/.bash_profile`.

     ```
     export PATH=/usr/local/cuda/bin:$PATH
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
     ```
   + For *tcsh* shells, add the following statements to `/home/{{username}}/.cshrc`.

     ```
     setenv PATH=/usr/local/cuda/bin:$PATH
     setenv LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
     ```

1. To confirm that the Nvidia GPU drivers are functional, run the following command.

   ```
   $ nvidia-smi -q | head
   ```

   The command should return information about the Nvidia GPUs, Nvidia GPU drivers, and Nvidia CUDA toolkit.

**Important**  
Skip Step 4 if your AMI already includes GDRCopy, or if you are using a non-GPU instance.

## Step 4: Install GDRCopy
<a name="nixl-start-base-gdrcopy"></a>

Install GDRCopy to improve the performance of Libfabric on GPU-based platforms. For more information about GDRCopy, see the [GDRCopy repository](https://github.com/NVIDIA/gdrcopy).

**To install GDRCopy**

1. Install the required dependencies.

   ```
   $ sudo apt -y install build-essential devscripts debhelper check libsubunit-dev fakeroot pkg-config dkms
   ```

1. Download and extract the GDRCopy package.

   ```
   $ wget https://github.com/NVIDIA/gdrcopy/archive/refs/tags/v2.4.tar.gz \
   && tar xf v2.4.tar.gz \
   && cd gdrcopy-2.4/packages
   ```

1. Build the GDRCopy DEB packages.

   ```
   $ CUDA=/usr/local/cuda ./build-deb-packages.sh
   ```

1. Install the GDRCopy DEB packages.

   ```
   $ sudo dpkg -i gdrdrv-dkms_2.4-1_amd64.*.deb \
   && sudo dpkg -i libgdrapi_2.4-1_amd64.*.deb \
   && sudo dpkg -i gdrcopy-tests_2.4-1_amd64.*.deb \
   && sudo dpkg -i gdrcopy_2.4-1_amd64.*.deb
   ```

**Important**  
Skip Step 5 if your AMI already includes the latest EFA installer.

## Step 5: Install the EFA software
<a name="nixl-start-base-enable"></a>

Install the EFA-enabled kernel, EFA drivers, and Libfabric stack that is required to support EFA on your instance.

**To install the EFA software**

1. Connect to the instance you launched. For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md).

1. Download the EFA software installation files. The software installation files are packaged into a compressed tarball (`.tar.gz`) file. To download the latest *stable* version, use the following command.

   ```
   $ curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.50.0.tar.gz
   ```

1. Extract the files from the compressed `.tar.gz` file, delete the tarball, and navigate into the extracted directory.

   ```
   $ tar -xf aws-efa-installer-1.50.0.tar.gz && rm -rf aws-efa-installer-1.50.0.tar.gz && cd aws-efa-installer
   ```

1. (*Optional*) Verify individual package signatures during installation.

   Starting with EFA installer 1.48.0, the installer includes GPG-signed individual RPM and DEB packages. To verify the authenticity and integrity of each individual package during installation, use the `--check-signatures` flag. When you enable this flag, the installer verifies all package signatures first, and only proceeds with installation if every package passes verification. If any package fails verification, the installer exits immediately without installing anything.

   1. Download the GPG public key.

      ```
      $ wget https://efa-installer.amazonaws.com/aws-efa-installer.key
      ```

   1. Export the key path. Then, in the next step, append `--check-signatures` to the installation command and use `sudo -E` instead of `sudo` to preserve the environment variable.

      ```
      $ export EFA_INSTALLER_KEY=$(pwd)/aws-efa-installer.key
      ```

   On RPM-based systems (Amazon Linux, RHEL, Rocky Linux, and SUSE), the installer verifies each RPM using `rpm --checksig`. On DEB-based systems (Ubuntu, Debian), the installer verifies each DEB using GPG signature verification.

   If verification of any package fails, the installation immediately aborts, protecting your system against broken or malicious packages.
**Note**  
The `--check-signatures` flag is optional. Without it, the installer does not perform individual signature verification.

1. Run the EFA software installation script.
**Note**  
If you completed the previous optional step to set up package signature verification, append `--check-signatures` to the installation command and use `sudo -E` instead of `sudo`. For example: `sudo -E ./efa_installer.sh -y --check-signatures`.

   ```
   $ sudo ./efa_installer.sh -y
   ```

   **Libfabric** is installed in the `/opt/amazon/efa` directory.

1. If the EFA installer prompts you to reboot the instance, do so and then reconnect to the instance. Otherwise, log out of the instance and then log back in to complete the installation.

1. Confirm that the EFA software components were successfully installed.

   ```
   $ fi_info -p efa -t FI_EP_RDM
   ```

   The command should return information about the Libfabric EFA interfaces. The following example shows the command output.
   + `p3dn.24xlarge` with single network interface

     ```
     provider: efa
     fabric: EFA-fe80::94:3dff:fe89:1b70
     domain: efa_0-rdm
     version: 2.0
     type: FI_EP_RDM
     protocol: FI_PROTO_EFA
     ```
   + `p4d.24xlarge` and `p5.48xlarge` with multiple network interfaces

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

## Step 6: Install NIXL
<a name="nixl-start-base-nixl"></a>

Install NIXL. For more information about NIXL, see the [NIXL repository](https://github.com/ai-dynamo/nixl).

------
#### [ Pre-built distributions ]

**To install NIXL using PyPI**

1. Install the required dependencies.

   ```
   $ sudo apt install pip
   ```

1. Install NIXL.

   ```
   $ pip install nixl
   ```

------
#### [ Build from source ]

**To build and install NIXL from source**

1. Install the required dependencies.

   ```
   $ sudo apt install cmake pkg-config meson pybind11-dev libaio-dev nvidia-cuda-toolkit pip libhwloc-dev \
   && pip install meson ninja pybind11
   ```

1. Navigate to your home directory.

   ```
   $ cd $HOME
   ```

1. Clone the official NIXL repository to the instance and navigate into the local cloned repository.

   ```
   $ sudo git clone https://github.com/ai-dynamo/nixl.git && cd nixl
   ```

1. Build and install NIXL and specify the path to the Libfabric installation directory.

   ```
   $ sudo meson setup . nixl --prefix=/usr/local/nixl -Dlibfabric_path=/opt/amazon/efa
   $ cd nixl && sudo ninja && sudo ninja install
   ```

------

## Step 7: Install NIXL Benchmark and test your EFA and NIXL configuration
<a name="nixl-start-base-tests"></a>

Install the NIXL Benchmark and run a test to ensure that your temporary instance is properly configured for EFA and NIXL. The NIXL Benchmark enables you to confirm that NIXL is properly installed and that it is operating as expected. For more information, see the [nixlbench repository](https://github.com/ai-dynamo/nixl/tree/main/benchmark/nixlbench).

NIXL Benchmark (nixlbench) requires ETCD for coordination between client and server. To use ETCD with NIXL requires ETCD Server and Client, and ETCD CPP API.

------
#### [ Build from Docker ]

**To install and test NIXL Benchmark using Docker**

1. Clone the official NIXL repository to the instance and navigate to the nixlbench build directory.

   ```
   $ git clone https://github.com/ai-dynamo/nixl.git
   $ cd nixl/benchmark/nixlbench/contrib
   ```

1. Build the container.

   ```
   $ ./build.sh
   ```

   For more information about Docker build options, see the [nixlbench repository](https://github.com/ai-dynamo/nixl/tree/main/benchmark/nixlbench).

1. Install Docker.

   ```
   $ sudo apt install docker.io -y
   ```

1. Start the ETCD server for coordination.

   ```
   $ docker run -d --name etcd-server \
       -p 2379:2379 -p 2380:2380 \
       quay.io/coreos/etcd:v3.5.18 \
       /usr/local/bin/etcd \
       --data-dir=/etcd-data \
       --listen-client-urls=http://0.0.0.0:2379 \
       --advertise-client-urls=http://0.0.0.0:2379 \
       --listen-peer-urls=http://0.0.0.0:2380 \
       --initial-advertise-peer-urls=http://0.0.0.0:2380 \
       --initial-cluster=default=http://0.0.0.0:2380
   ```

1. Validate that the ETCD server is running.

   ```
   $ curl -L http://localhost:2379/health
   ```

   Expected output:

   ```
   {"health":"true"}
   ```

1. Open two terminals for the instance. On both terminals, run the following command to verify the installation. The command uses the ETCD server on the same instance, uses Libfabric as the backend, and operates using GPU memory.

   ```
   $ docker run -it --gpus all --network host nixlbench:latest \
       nixlbench --etcd_endpoints http://localhost:2379 \
       --backend LIBFABRIC \
       --initiator_seg_type VRAM \
       --target_seg_type VRAM
   ```
**Note**  
Use the value `DRAM` instead of `VRAM` for non-GPU instances.

------
#### [ Build from source ]

**Important**  
Follow this tab only if you chose **Build from source** in Step 6.

**To install NIXL Benchmark**

1. Install the required system dependencies.

   ```
   $ sudo apt install libgflags-dev
   ```

1. Install ETCD Server and Client.

   ```
   $ sudo apt install -y etcd-server etcd-client
   ```

1. Install the ETCD CPP API.

   1. Install the required dependencies for ETCD CPP API.

      ```
      $ sudo apt install libboost-all-dev libssl-dev libgrpc-dev libgrpc++-dev libprotobuf-dev protobuf-compiler-grpc libcpprest-dev
      ```

   1. Clone and install ETCD CPP API.

      ```
      $ cd $HOME
      $ git clone https://github.com/etcd-cpp-apiv3/etcd-cpp-apiv3.git
      $ cd etcd-cpp-apiv3
      $ mkdir build && cd build
      $ cmake ..
      $ sudo make -j$(nproc) && sudo make install
      ```

1. Build and install nixlbench.

   ```
   $ sudo meson setup . $HOME/nixl/benchmark/nixlbench -Dnixl_path=/usr/local/nixl/
   $ sudo ninja && sudo ninja install
   ```

**To test your EFA and NIXL configuration**

1. Start the ETCD server on the instance.

   ```
   $ etcd --listen-client-urls "http://0.0.0.0:2379" \
       --advertise-client-urls "http://localhost:2379" &
   ```

1. Validate that the ETCD server is running.

   ```
   $ curl -L http://localhost:2379/health
   ```

   Expected output:

   ```
   {"health":"true"}
   ```

1. Open two terminals for the instance. On both terminals, complete the following steps to run nixlbench.

   1. Navigate to the directory where nixlbench is installed.

      ```
      $ cd /usr/local/nixlbench/bin/
      ```

   1. Run the test and specify the backend, address of the ETCD server, and initiator segment type. The following command uses the ETCD server on the same instance, uses Libfabric as the backend, and operates using GPU memory. The environment variables configure the following:
      + `NIXL_LOG_LEVEL=INFO` — Enables detailed debugging output. You can also specify `WARN` to receive only error messages.
      + `LD_LIBRARY_PATH` — Sets the path for the NIXL library.

      For more information about the NIXL Benchmark arguments, see the [NIXLbench README](https://github.com/ai-dynamo/nixl/blob/main/benchmark/nixlbench/README.md) in the official nixlbench repository.

      ```
      $ export NIXL_LOG_LEVEL=INFO
      $ export LD_LIBRARY_PATH=/usr/local/nixl/lib/$(gcc -dumpmachine):$LD_LIBRARY_PATH
      
      $ nixlbench --etcd-endpoints 'http://localhost:2379' \
          --backend 'LIBFABRIC' \
          --initiator_seg_type 'VRAM' \
          --target_seg_type 'VRAM'
      ```
**Note**  
Use the value `DRAM` instead of `VRAM` for non-GPU instances.

------

## Step 8: Install your machine learning applications
<a name="nixl-start-base-app"></a>

Install the machine learning applications on the temporary instance. The installation procedure varies depending on the specific machine learning application.

**Note**  
Refer to your machine learning application's documentation for installation instructions.

## Step 9: Create an EFA and NIXL-enabled AMI
<a name="nixl-start-base-ami"></a>

After you have installed the required software components, you create an AMI that you can reuse to launch your EFA-enabled instances.

**To create an AMI from your temporary instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the temporary instance that you created and choose **Actions**, **Image**, **Create image**.

1. For **Create image**, do the following:

   1. For **Image name**, enter a descriptive name for the AMI.

   1. (Optional) For **Image description**, enter a brief description of the purpose of the AMI.

   1. Choose **Create image**.

1. In the navigation pane, choose **AMIs**.

1. Locate the AMI that you created in the list. Wait for the status to change from `pending` to `available` before continuing to the next step.

## Step 10: Terminate the temporary instance
<a name="nixl-start-base-terminate"></a>

At this point, you no longer need the temporary instance that you launched. You can terminate the instance to stop incurring charges for it.

**To terminate the temporary instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select the temporary instance that you created and then choose **Actions**, **Instance state**, **Terminate instance**.

1. When prompted for confirmation, choose **Terminate**.

## Step 11: Launch EFA and NIXL-enabled instances
<a name="nixl-start-base-cluster"></a>

Launch your EFA and NIXL-enabled instances using the EFA-enabled AMI that you created in **Step 9**, and the EFA-enabled security group that you created in **Step 1**.

**To launch EFA and NIXL-enabled instances**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**, and then choose **Launch Instances** to open the new launch instance wizard.

1. (*Optional*) In the **Name and tags** section, provide a name for the instance, such as `EFA-instance`. The name is assigned to the instance as a resource tag (`Name={{EFA-instance}}`).

1. In the **Application and OS Images** section, choose **My AMIs**, and then select the AMI that you created in the previous step.

1. In the **Instance type** section, select a supported instance type.

1. In the **Key pair** section, select the key pair to use for the instance.

1. In the **Network settings** section, choose **Edit**, and then do the following:

   1. For **Subnet**, choose the subnet in which to launch the instance. If you do not select a subnet, you can't enable the instance for EFA.

   1. For **Firewall (security groups)**, choose **Select existing security group**, and then select the security group that you created in **Step 1**.

   1. Expand the **Advanced network configuration** section.

      For **Network interface 1**, select **Network card index = 0**, **Device index = 0**, and **Interface type = EFA with ENA**.

      (*Optional*) If you are using a multi-card instance type, such as `p4d.24xlarge` or `p5.48xlarge`, for each additional network interface required, choose **Add network interface**, for **Network card index** select the next unused index, and then select **Device index = 1** and **Interface type = EFA with ENA** or **EFA-only**.

1. (*Optional*) In the **Storage** section, configure the volumes as needed.

1. In the **Summary** panel on the right, for **Number of instances**, enter the number of EFA-enabled instances that you want to launch, and then choose **Launch instance**.

## Step 12: Enable passwordless SSH
<a name="nixl-start-base-passwordless"></a>

To enable your applications to run across all of the instances in your cluster, you must enable passwordless SSH access from the leader node to the member nodes. The leader node is the instance from which you run your applications. The remaining instances in the cluster are the member nodes.

**To enable passwordless SSH between the instances in the cluster**

1. Select one instance in the cluster as the leader node, and connect to it.

1. Disable `strictHostKeyChecking` and enable `ForwardAgent` on the leader node. Open `~/.ssh/config` using your preferred text editor and add the following.

   ```
   Host *
       ForwardAgent yes
   Host *
       StrictHostKeyChecking no
   ```

1. Generate an RSA key pair.

   ```
   $ ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
   ```

   The key pair is created in the `$HOME/.ssh/` directory.

1. Change the permissions of the private key on the leader node.

   ```
   $ chmod 600 ~/.ssh/id_rsa
   chmod 600 ~/.ssh/config
   ```

1. Open `~/.ssh/id_rsa.pub` using your preferred text editor and copy the key.

1. For each member node in the cluster, do the following:

   1. Connect to the instance.

   1. Open `~/.ssh/authorized_keys` using your preferred text editor and add the public key that you copied earlier.

1. To test that the passwordless SSH is functioning as expected, connect to your leader node and run the following command.

   ```
   $ ssh {{member_node_private_ip}}
   ```

   You should connect to the member node without being prompted for a key or password.

**Important**  
Follow Step 13 only if you followed Step 7.

## Step 13: Test your EFA and NIXL configuration across instances
<a name="nixl-start-base-test-multi"></a>

Run a test to ensure that your instances are properly configured for EFA and NIXL.

------
#### [ Build from Docker ]

**To test your EFA and NIXL configuration across instances using Docker**

1. Select two hosts to run the nixlbench benchmark. Use the IP address of the first host as the ETCD server IP for metadata exchange.

1. Start the ETCD server on host 1.

   ```
   $ docker run -d --name etcd-server \
       -p 2379:2379 -p 2380:2380 \
       quay.io/coreos/etcd:v3.5.18 \
       /usr/local/bin/etcd \
       --data-dir=/etcd-data \
       --listen-client-urls=http://0.0.0.0:2379 \
       --advertise-client-urls=http://0.0.0.0:2379 \
       --listen-peer-urls=http://0.0.0.0:2380 \
       --initial-advertise-peer-urls=http://0.0.0.0:2380 \
       --initial-cluster=default=http://0.0.0.0:2380
   ```

1. Validate that the ETCD server is running.

   ```
   $ curl -L http://localhost:2379/health
   ```

   ```
   {"health":"true"}
   ```

1. Run the nixlbench benchmark on host 1.

   ```
   $ docker run -it --gpus all --network host nixlbench:latest \
       nixlbench --etcd_endpoints http://localhost:2379 \
       --backend LIBFABRIC \
       --initiator_seg_type VRAM
   ```

1. Run the nixlbench benchmark on host 2.

   ```
   $ docker run -it --gpus all --network host nixlbench:latest \
       nixlbench --etcd_endpoints http://{{ETCD_SERVER_IP}}:2379 \
       --backend LIBFABRIC \
       --initiator_seg_type VRAM
   ```

------
#### [ Build from source ]

**Important**  
Follow this tab only if you chose **Build from source** in Step 6.

**To test your EFA and NIXL configuration across instances**

1. Select two hosts to run the nixlbench benchmark. Use the IP address of the first host as the ETCD server IP for metadata exchange.

1. Launch the ETCD server on host 1.

   ```
   $ etcd --listen-client-urls "http://0.0.0.0:2379" \
       --advertise-client-urls "http://localhost:2379" &
   ```

1. Validate that the ETCD server is running.

   ```
   $ curl -L http://localhost:2379/health
   ```

   ```
   {"health":"true"}
   ```

1. Run the nixlbench benchmark on host 1.

   ```
   $ export NIXL_LOG_LEVEL=INFO
   $ export LD_LIBRARY_PATH=$HOME/nixl/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
   
   $ nixlbench \
       --etcd-endpoints http://localhost:2379 \
       --backend LIBFABRIC \
       --initiator_seg_type VRAM
   ```

1. Run the nixlbench benchmark on host 2.

   ```
   $ export NIXL_LOG_LEVEL=INFO
   $ export LD_LIBRARY_PATH=$HOME/nixl/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
   
   $ nixlbench \
       --etcd-endpoints http://{{ETCD_SERVER_IP}}:2379 \
       --backend LIBFABRIC \
       --initiator_seg_type VRAM
   ```

------

## Step 14: Test disaggregated inference serving over vLLM (*Optional*)
<a name="nixl-start-base-serve"></a>

After NIXL is installed, you can use NIXL through LLM inference and serving frameworks such as vLLM, SGLang, and TensorRT-LLM.

**To serve your inference workload using vLLM**

1. Install vLLM.

   ```
   $ pip install vllm
   ```

1. Start the vLLM server with NIXL. The following sample commands create one prefill (producer) and one decode (consumer) instance for NIXL handshake connection, KV connector, KV role, and transport backend. For detailed examples and scripts, see the [NIXLConnector Usage Guide](https://github.com/vllm-project/vllm/blob/2d977a7a9ead3179fde9ed55d69393ef7b6cec47/docs/features/nixl_connector_usage.md).

   To use NIXL with EFA, set the environment variables based on your setup and use case.
   + Producer (Prefiller) configuration

     ```
     $ vllm serve {{your-application}} \
         --port 8200 \
         --enforce-eager \
         --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda","kv_connector_extra_config":{"backends":["LIBFABRIC"]}}'
     ```
   + Consumer (Decoder) configuration

     ```
     $ vllm serve {{your-application}} \
         --port 8200 \
         --enforce-eager \
         --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda","kv_connector_extra_config":{"backends":["LIBFABRIC"]}}'
     ```

   The preceding sample configuration sets the following:
   + `kv_role` to `kv_both`, which enables symmetric functionality where the connector can act as both producer and consumer. This provides flexibility for experimental setups and scenarios where the role distinction is not predetermined.
   + `kv_buffer_device` to `cuda`, which enables using GPU memory.
   + NIXL backend to `LIBFABRIC`, which enables NIXL traffic to go over EFA.