# NVIDIA drivers for your Amazon EC2 instance

An instance with an attached NVIDIA GPU, such as a P- or G- series instance types, must
have the appropriate NVIDIA driver installed. Depending on the instance type, you can either
download a public NVIDIA driver, download a driver from Amazon S3 that is available only to
AWS customers, or use an AWS AMI with the driver pre-installed.

To install AMD drivers on an instance with an attached AMD GPU, such as a G4ad
instance, see [AMD drivers](install-amd-driver.md "install-amd-driver.md")
instead.

###### Topics

- [Types of NVIDIA drivers](#nvidia-driver-types "#nvidia-driver-types")
- [Available drivers by instance
  type](#nvidia-driver-instance-type "#nvidia-driver-instance-type")
- [Installation options](#nvidia-installation-options "#nvidia-installation-options")
- [Use AMIs that include NVIDIA drivers](preinstalled-nvidia-driver.md "preinstalled-nvidia-driver.md")
- [Install NVIDIA public drivers](public-nvidia-driver.md "public-nvidia-driver.md")
- [Install NVIDIA GRID drivers (G6, Gr6, G6e, G6f, Gr6f, G5,
  G4dn, and G3 instances)](nvidia-GRID-driver.md "nvidia-GRID-driver.md")
- [Install NVIDIA gaming drivers (G6, G6e, G5, and G4dn
  instances)](nvidia-gaming-driver.md "nvidia-gaming-driver.md")

## Types of NVIDIA drivers

The following are the main types of NVIDIA drivers that can be used with GPU-based
instances.

Tesla drivers

These drivers are intended primarily for compute workloads, which use
GPUs for computational tasks such as parallelized floating-point
calculations for machine learning and fast Fourier transforms for high
performance computing applications.

GRID drivers

These drivers are certified to provide optimal performance for
professional visualization applications that render content such as 3D
models or high-resolution videos. You can configure GRID drivers to
support two modes. Quadro Virtual Workstations provide access to four 4K
displays per GPU. GRID vApps provide RDSH App hosting
capabilities.

Gaming drivers

These drivers contain optimizations for gaming and are updated
frequently to provide performance enhancements. They support a single 4K
display per GPU.

###### Configured mode

On Windows, the Tesla drivers are configured to run in Tesla Compute Cluster
(TCC) mode. The GRID and gaming drivers are configured to run in Windows Display
Driver Model (WDDM) mode. In TCC mode, the card is dedicated to compute
workloads. In WDDM mode, the card supports both compute and graphics
workloads.

###### NVIDIA control panel

The NVIDIA control panel is supported with GRID and Gaming drivers. It is not
supported with Tesla drivers.

###### Supported APIs for Tesla, GRID, and gaming drivers

- OpenCL, OpenGL, and Vulkan
- NVIDIA CUDA and related libraries (for example, cuDNN, TensorRT, nvJPEG,
  and cuBLAS)
- NVENC for video encoding and NVDEC for video decoding
- Windows-only APIs: DirectX, Direct2D, DirectX Video Acceleration, DirectX Raytracing

## Available drivers by instance

type

The following table summarizes the supported NVIDIA drivers for each GPU instance
type.

| Instance type | Tesla driver | GRID driver | Gaming driver |
| ------------- | ------------ | ----------- | ------------- |
| G3            | Yes          | Yes         | No            |
| G4dn          | Yes          | Yes         | Yes           |
| G5            | Yes          | Yes         | Yes           |
| G5g           | Yes ¹        | No          | No            |
| G6            | Yes          | Yes         | Yes           |
| G6e           | Yes          | Yes         | Yes           |
| G6f           | No           | Yes         | No            |
| Gr6           | Yes          | Yes         | No            |
| Gr6f          | No           | Yes         | No            |
| P2            | Yes          | No          | No            |
| P3            | Yes          | No          | No            |
| P4d           | Yes          | No          | No            |
| P4de          | Yes          | No          | No            |
| P5            | Yes          | No          | No            |
| P5e           | Yes          | No          | No            |
| P5en          | Yes          | No          | No            |
| P6-B200       | Yes          | No          | No            |
| P6e-GB200     | Yes          | No          | No            |

¹ This Tesla driver also supports optimized graphics applications specific to
the ARM64 platform

## Installation options

Use one of the following options to get the NVIDIA drivers required for your GPU
instance.

**Options**

1. [Use AMIs that include NVIDIA drivers](preinstalled-nvidia-driver.md "preinstalled-nvidia-driver.md")
2. [Install NVIDIA public drivers](public-nvidia-driver.md "public-nvidia-driver.md")
3. [Install NVIDIA GRID drivers (G6, Gr6, G6e, G6f, Gr6f, G5,
   G4dn, and G3 instances)](nvidia-GRID-driver.md "nvidia-GRID-driver.md")
4. [Install NVIDIA gaming drivers (G6, G6e, G5, and G4dn
   instances)](nvidia-gaming-driver.md "nvidia-gaming-driver.md")
