# Install NVIDIA public drivers

If the AWS Marketplace AMIs described in [Use AMIs that include NVIDIA drivers](preinstalled-nvidia-driver.md "preinstalled-nvidia-driver.md") don't fit your use case, you can
install the public drivers and bring your own license. Installation options include
the following:

- [Option 1: Driver-only install](#public-nvidia-driver-only-install "#public-nvidia-driver-only-install")
- [Option 2: Install with the CUDA toolkit](#public-nvidia-driver-cuda-install "#public-nvidia-driver-cuda-install")
  (recommended for Linux distributions)

 

###### P6-B200 instance type considerations

The P6-B200 platform is unique in that it exposes Mellanox ConnectX 7 network
interface cards (NICs) to the instance as PCIe devices. These CX7 NICs do not act as
typical network interfaces but instead function as NVSwitch bridges providing a control
path to initialize and configure the NVFabric, which is the NVLink topology of the GPU
interconnect.

To fully initialize the system, the NVIDIA Fabric Manager must configure
`NVFabric` and establish the NVSwitch topology. This enables
InfiniBand kernel modules to communicate with the CX7 devices.

NVIDIA Fabric Manager is included in the CUDA toolkit. We recommend [Option 2: Install with the CUDA toolkit](#public-nvidia-driver-cuda-install "#public-nvidia-driver-cuda-install")
for this instance type.

## Option 1: Driver-only install

To install a specific driver, log on to your instance and download the 64-bit
NVIDIA public driver for the instance type from [http://www.nvidia.com/Download/Find.aspx](http://www.nvidia.com/Download/Find.aspx "http://www.nvidia.com/Download/Find.aspx"). For **Product
Type**, **Product Series**, and
**Product**, use the options shown in the following
table.

Then follow the **Local Repository Installation** instructions in the [NVIDIA Driver Installation Guide](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/index.html "https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/index.html").

###### Note

P6-B200 instance types require installation and configuration of additional
packages that come bundled with the NVIDIA CUDA Toolkit. For more information, see
instructions for your Linux distribution in [Option 2: Install with the CUDA toolkit](#public-nvidia-driver-cuda-install "#public-nvidia-driver-cuda-install").

| Instance  | Product type | Product series | Product    | Minimum driver version |
| --------- | ------------ | -------------- | ---------- | ---------------------- |
| G3        | Tesla        | M-Class        | M60        | --                     |
| G4dn      | Tesla        | T-Series       | T4         | --                     |
| G5        | Tesla        | A-Series       | A10        | 470.00 or later        |
| G5g1      | Tesla        | T-Series       | NVIDIA T4G | 470.82.01 or later     |
| G6        | Tesla        | L-Series       | L4         | 525.0 or later         |
| G6e       | Tesla        | L-Series       | L40S       | 535.0 or later         |
| Gr6       | Tesla        | L-Series       | L4         | 525.0 or later         |
| P2        | Tesla        | K-Series       | K80        | --                     |
| P3        | Tesla        | V-Series       | V100       | --                     |
| P4d       | Tesla        | A-Series       | A100       | --                     |
| P4de      | Tesla        | A-Series       | A100       | --                     |
| P5        | Tesla        | H-Series       | H100       | 530 or later           |
| P5e       | Tesla        | H-Series       | H200       | 550 or later           |
| P5en      | Tesla        | H-Series       | H200       | 550 or later           |
| P6-B2002  | Tesla        | HGX-Series     | B200       | 570 or later           |
| P6e-GB200 | Tesla        | HGX-Series     | B200       | 570 or later           |

1 The operating system for G5g instances is Linux aarch64.

2 For P6-B200 instance types, there are additional installation
requirements to configure NVIDIA Fabric Manager.

## Option 2: Install with the CUDA toolkit

Install instructions vary slightly by operating system. To install public drivers on your
instance with the NVIDIA CUDA toolkit, follow the instructions for your instance operating system.
For instance operating systems that aren't shown here, follow the instructions for your operating
system and instance type architecture on the NVIDIA Developer website. For more information, see
[CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads "https://developer.nvidia.com/cuda-downloads").

For instance type architecture or other specifications, see the [Accelerated computing](../../../ec2/latest/instancetypes/ac.md "../../../ec2/latest/instancetypes/ac.md") specifications in the
_Amazon EC2 Instance Types_ reference.

This section covers an NVIDIA CUDA toolkit install on an Amazon Linux 2023
instance. The command examples in this section are based on an `x86_64`
architecture.

For `arm64-sbsa` commands, see [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=arm64-sbsa "https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=arm64-sbsa") and select the options that apply to your
distribution. Instructions appear after you've made your final selection.

###### Prerequisite

Before installing the toolkit and drivers, run the following command to
ensure that you have the correct version of the kernel headers and
development packages.

```
`[ec2-user ~]$` sudo dnf install kernel-devel-$(uname -r) kernel-headers-$(uname -r) -y
```

###### Download the toolkit and drivers

Choose the type of installation to use for your instance, and follow the
associated steps.

RPM local installation
You can follow these instructions to download the CUDA toolkit
installer repository bundle to your instance, then extract and register
the specified bundle.

To view instructions on the NVIDIA developer website, see [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Amazon-Linux&target_version=2023&target_type=rpm_local "https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Amazon-Linux&target_version=2023&target_type=rpm_local").

```
`[ec2-user ~]$` wget https://developer.download.nvidia.com/compute/cuda/`13.0.0`/local_installers/`cuda-repo-amzn2023-13-0-local-13.0.0_580.65.06-1.x86_64.rpm`
`[ec2-user ~]$` sudo rpm -i `cuda-repo-amzn2023-13-0-local-13.0.0_580.65.06-1.x86_64.rpm`
```

RPM network installation
You can follow these instructions to register the CUDA repository with the
package manager on your instance. When you run the install steps, the package
manager downloads only the packages that are required.

To view instructions on the NVIDIA developer website, see [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Amazon-Linux&target_version=2023&target_type=rpm_network "https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Amazon-Linux&target_version=2023&target_type=rpm_network").

```
`[ec2-user ~]$` wget https://developer.download.nvidia.com/compute/cuda/repos/`ubuntu2404`/x86_64/`cuda-keyring_1.1-1_all.deb`
`[ec2-user ~]$` sudo dpkg -i `cuda-keyring_1.1-1_all.deb`
```

Remaining steps are the same for both local and network installation.

1. Complete the CUDA toolkit install

```
`[ec2-user ~]$` sudo dnf clean all
`[ec2-user ~]$` sudo dnf install cuda-toolkit -y
```

2. Install the open kernel module variant of the driver

```
`[ec2-user ~]$` sudo dnf module install nvidia-driver:open-dkms -y
```

3. Install GPUDirect Storage and Fabric Manager

```
`[ec2-user ~]$` sudo dnf install nvidia-gds -y
`[ec2-user ~]$` sudo dnf install nvidia-fabric-manager -y
```

4. Enable Fabric Manager and driver persistence

```
`[ec2-user ~]$` sudo systemctl enable nvidia-fabricmanager
`[ec2-user ~]$` sudo systemctl enable nvidia-persistenced
```

5. Additional configuration for P6-B200 instance types:

P6-B200 instance types require installation and configuration of additional
packages that come bundled with the NVIDIA CUDA Toolkit.

    1. Install NVIDIA Link Subnet Manager and `ibstat`.



    ```
    `[ec2-user ~]$` sudo dnf install nvlink5
    ```
    2. Enable automatic loading of the Infiniband module on startup.



    ```
    `[ec2-user ~]$` echo "ib_umad" | sudo tee -a /etc/modules-load.d/modules.conf
    ```

6. Reboot the instance

```
`[ec2-user ~]$` sudo reboot
```

This section covers an NVIDIA CUDA toolkit install on an Ubuntu 24.04 instance.
The command examples in this section are based on an `x86_64`
architecture.

For `arm64-sbsa` commands, see [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=arm64-sbsa "https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=arm64-sbsa") and select the options that apply to your
distribution. Instructions appear after you've made your final selection.

###### Prerequisite

Before installing the toolkit and drivers, run the following command to
ensure that you have the correct version of the kernel headers and
development packages.

```
`$` apt install linux-headers-$(uname -r)
```

###### Download the toolkit and drivers

Choose the type of installation to use for your instance, and follow the
associated steps.

RPM local installation
You can follow these instructions to download the CUDA toolkit
installer repository bundle to your instance, then extract and register
the specified bundle.

To view instructions on the NVIDIA developer website, see [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local "https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local").

```
`$` wget https://developer.download.nvidia.com/compute/cuda/repos/`ubuntu2404`/x86_64/`cuda-ubuntu2404.pin`
`$` sudo mv `cuda-ubuntu2404.pin` /etc/apt/preferences.d/cuda-repository-pin-600
`$` wget https://developer.download.nvidia.com/compute/cuda/`13.0.0`/local_installers/`cuda-repo-ubuntu2404-13-0-local_13.0.0-580.65.06-1_amd64.deb`
`$` sudo dpkg -i `cuda-repo-ubuntu2404-13-0-local_13.0.0-580.65.06-1_amd64.deb`
`$` sudo cp /var/`cuda-repo-ubuntu2404-13-0-local`/cuda-*-keyring.gpg /usr/share/keyrings/
```

RPM network installation
You can follow these instructions to register the CUDA repository with the
package manager on your instance. When you run the install steps, the package
manager downloads only the packages that are required.

To view instructions on the NVIDIA developer website, see [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_network "https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_network").

```
`$` wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
`$` sudo dpkg -i cuda-keyring_1.1-1_all.deb
```

Remaining steps are the same for both local and network installation.

1. Complete the CUDA toolkit install

```
`$` sudo apt update
`$` sudo apt install cuda-toolkit -y
```

2. Install the open kernel module variant of the driver

```
`$` sudo apt install nvidia-open -y
```

3. Install GPUDirect Storage and Fabric Manager

```
`$` sudo apt install nvidia-gds -y
`$` sudo apt install nvidia-fabricmanager -y
```

4. Enable Fabric Manager and driver persistence

```
`$` sudo systemctl enable nvidia-fabricmanager
`$` sudo systemctl enable nvidia-persistenced
```

5. Additional configuration for P6-B200 instance types:

P6-B200 instance types require installation and configuration of additional
packages that come bundled with the NVIDIA CUDA Toolkit.

    1. Install the latest InfiniBand-specific device driver (`mlx5_ib`) and
     diagnostic utilities.



    ```
    `$` sudo apt install linux-modules-extra-$(uname -r) -y
    `$` sudo apt install infiniband-diags -y
    ```
    2. Install NVIDIA Link Subnet Manager.



    ```
    `$` sudo apt install nvlsm -y
    ```

6. Reboot the instance

```
sudo reboot
```

7. Update your path and add the following environment variable.

```
`$` export PATH=${PATH}:/usr/local/`cuda-13.0`/bin
`$` export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/`cuda-13.0`/lib64
```

To install the NVIDIA driver on Windows, follow these steps:

1. Open the folder where you downloaded the driver and launch the
   installation file. Follow the instructions to install the driver and
   reboot your instance as required.
2. Disable the display adapter named **Microsoft Basic Display
   Adapter** that is marked with a warning icon using Device
   Manager. Install these Windows features: **Media
   Foundation** and **Quality Windows Audio Video
   Experience**.

###### Important

Don't disable the display adapter named **Microsoft Remote
Display Adapter**. If **Microsoft Remote
Display Adapter** is disabled your connection might be
interrupted and attempts to connect to the instance after it has
rebooted might fail. 3. Check Device Manager to verify that the GPU is working
correctly. 4. To achieve the best performance from your GPU, complete the
optimization steps in [Optimize GPU settings on Amazon EC2 instances](optimize_gpu.md "optimize_gpu.md").
