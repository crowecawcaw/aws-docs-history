# Prerequisites for Windows Amazon DCV server on

Amazon EC2 instances

This topic describes how to configure your Windows Amazon EC2 instance before you install
the Amazon DCV server. If you're not installing the Amazon DCV server on an Amazon EC2 Windows instance, skip
these prerequisites.

###### Topics

- [Prerequisites for all
  instances](#setting-up-installing-all "#setting-up-installing-all")
- [Prerequisites for accelerated computing
  instances](#setting-up-installing-graphics "#setting-up-installing-graphics")
- [Prerequisites for other instance
  families](#setting-up-installing-general "#setting-up-installing-general")

## Prerequisites for all

instances

From version 2024.0 the Windows version of Amazon DCV has as a requirement Microsoft Visual C++
Redistributable for Visual Studio 2022 instead of Microsoft Visual C++ Redistributable for Visual
Studio 2017.

The best practice is that Microsoft Visual C++ Redistributable for Visual Studio are
installed before the Amazon DCV Server installation by the server administrator. The 2024.0 Amazon
DCV MSI installer checks for the dependency and if they are not found, will attempt to install the
requirement before the Amazon DCV installation. This behavior is a fallback mechanism which will be
removed in future release. Administrators that use automation for the installation should work towards
updating their automations to install Microsoft Visual C++ Redistributable for Visual Studio before the
Amazon DCV server. Also please note that Microsoft Visual C++ Redistributable may reboot the host as
part of the installation.

## Prerequisites for accelerated computing

instances

### Prerequisites for GPU graphics

instances

If you're using a GPU graphics instance (for example, a G2, G3, G4dn, G4ad, or G5
instance), we recommend that you install and configure the appropriate NVIDIA or AMD
GPU drivers. The GPU drivers allow for the following:

- DirectX and OpenGL hardware acceleration for applications
- Hardware acceleration for H.264 video streaming encoding
- Customizable server monitor resolutions
- Increased maximum resolution for server monitors— up to 4096x2160
- Increased number of server monitors

For instructions on how to install NVIDIA GPU drivers on your GPU graphics
instance, see the following topics in the _Amazon EC2 User
Guide_.

- For instances with an NVIDIA GPU (for example, a G2, G3, G4dn, or G5 instance),
  see [Installing the
  NVIDIA Driver on Windows](../../../AWSEC2/latest/WindowsGuide/install-nvidia-driver.md "../../../AWSEC2/latest/WindowsGuide/install-nvidia-driver.md").
- For instances with an AMD GPU (for example, a G4ad instance), see [Install AMD drivers on Windows instances](../../../AWSEC2/latest/WindowsGuide/install-amd-driver.md "../../../AWSEC2/latest/WindowsGuide/install-amd-driver.md").

For more information about Amazon EC2 G4ad instances, see the [Deep dive on the
new Amazon EC2 G4ad instances](https://aws.amazon.com/blogs/compute/deep-dive-on-the-new-amazon-ec2-g4ad-instances/ "https://aws.amazon.com/blogs/compute/deep-dive-on-the-new-amazon-ec2-g4ad-instances/") blog post.

### Prerequisites for other

accelerated computing instances

If you're using an accelerated computing instance that isn't a GPU graphics
instance (for example a P2, P3, or P3dn instance), we recommend that you install and
configure the appropriate NVIDIA GPU drivers. The NVIDIA GPU drivers enable
hardware acceleration for H.264 video streaming encoding.

For instructions on how to install NVIDIA GPU drivers on your accelerated
computing instance, see [Public NVIDIA Drivers](../../../AWSEC2/latest/WindowsGuide/install-nvidia-driver.md#public-nvidia-driver "../../../AWSEC2/latest/WindowsGuide/install-nvidia-driver.md#public-nvidia-driver") in the
_Amazon EC2 User Guide_.

Installing the NVIDIA GPU drivers on an accelerated computing instance doesn't
enhance server monitor limits or resolutions. To add the additional server monitor
resolution support, you can install the NVIDIA GRID drivers. For more information,
see [NVIDIA vGPU
Software](https://www.nvidia.com/object/vGPU-software-driver.html "https://www.nvidia.com/object/vGPU-software-driver.html") on the NVIDIA website.

## Prerequisites for other instance

families

For instances other than accelerated computing instances, we recommend that you install the Amazon DCV
Virtual Display driver if you are on Windows 2016 or are running a Amazon DCV server version before 2023.1.
This includes instances in the general purpose, compute-optimized, memory-optimized, and storage-optimized
instance families.

Installing the Amazon DCV Virtual Display driver enables the following:

- Support for up to four monitors
- Support for custom resolutions
- Support for 4K UHD resolution

You can't manage server monitors attached by the Amazon DCV server using Windows Control
Panel.

###### Note

The Amazon DCV Virtual Display driver is supported on Windows Server 2016 and later. The driver is not needed
if you are on Windows Server 2019 or later with DCV server 2023.1 or later since the Indirect Display Driver
(IDD) is packaged with DCV server. IDD is recommended, but the
[GetConsoleScreenshot](../../../AWSEC2/latest/APIReference/API_GetConsoleScreenshot.md "../../../AWSEC2/latest/APIReference/API_GetConsoleScreenshot.md")
functionality will not work as expected.

###### Important

Installing the Amazon DCV Virtual Display driver with any other GPU drivers, such as
NVIDIA GPU drivers, might cause conflicts. To avoid conflicts, we recommend that you
don't install the Amazon DCV Virtual Display driver in combination with any other GPU
drivers.

###### To install the Amazon DCV Virtual Display driver on your instance

1. Download the Amazon DCV Virtual Display driver installer from the
   [Amazon DCV website](http://download.amazondcv.com "http://download.amazondcv.com").
2. Install the driver by doing one of the following:
   - Run the installation wizard
   - Double-click the installation file
   - Use the following command to run an unattended installation

   ```
   `C:\>` nice-dcv-virtual-display-x64-Release-88.msi /quiet /norestart
   ```

3. Reboot the instance.
4. Reconnect to the instance.
