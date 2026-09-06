

# Understanding Amazon DCV Servers
<a name="servers"></a>

Amazon DCV is installed on a dedicated server that creates user sessions. The Amazon DCV server software is available for Windows, Linux, and Amazon EC2 Mac instances. The servers offer similar features, but there are some differences. Choose the Amazon DCV server that best meets your needs. The following table compares the features supported by the Windows, Linux, and macOS Amazon DCV servers.

**Topics**
+ [Requirements](#requirements)
+ [Supported Features](#features)

## Requirements
<a name="requirements"></a>

For a good user experience with Amazon DCV, ensure that your server meets the following minimum requirements. Keep in mind that your users' experience is largely dependent on the number of pixels streamed from the Amazon DCV server to the Amazon DCV client.

If you are installing the Amazon DCV server on an Amazon EC2 instance, we recommend that you use an Amazon EC2 G3, G4dn, G4ad, G5, or G6 instance type. These instance types offer GPUs that support hardware-based OpenGL and GPU sharing. For more information, see [Amazon EC2 G3 Instances](https://aws.amazon.com/ec2/instance-types/g3/), [Amazon EC2 G4 instances](https://aws.amazon.com/ec2/instance-types/g4/), [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/), and [Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/). 

You can install the Amazon DCV server on any other instance type, but there might be screen resolution limitations. To bypass this limitation on Windows Server 2016, download and install the [ Amazon DCV Virtual Display Driver for EC2](https://d1uj6qtbmh3dt5.cloudfront.net/Drivers/nice-dcv-virtual-display-x64-Release-88.msi). On Windows Server 2019 or later running DCV 2023.1 or later, no additional action is needed.

Your server must meet the minimum requirements listed in the following table.


<table>
<thead>
  <tr><th></th><th>Windows server</th><th>Linux server</th><th>macOS server</th></tr>
</thead>
<tbody>
  <tr><td><b>Operating system</b></td><td> <ul><li>Windows 10</li><li>Windows 11</li><li>Windows Server 2016</li><li>Windows Server 2019</li><li>Windows Server 2022</li><li>Windows Server 2025</li></ul> All supported Windows operating systems require .NET Framework 4.5 and must support the x86-64 architecture. </td><td> <ul><li>Amazon Linux 2</li><li>Amazon Linux 2023</li><li>CentOS Stream 9</li><li>RHEL 8.x</li><li>RHEL 9.x</li><li>SUSE Linux Enterprise 15 with SP6 or later</li><li>Rocky Linux 8.5 or later</li><li>Rocky Linux 9</li><li>Ubuntu 22.04</li><li>Ubuntu 24.04</li></ul> </td><td> <ul><li>macOS Ventura 13.7.8 or later</li><li>macOS Sonoma 14.7.8 or later</li><li>macOS Sequoia 15.6.1 or later</li><li>macOS Tahoe 26.3.1 or later</li></ul> </td></tr>
  <tr><td><b>Supported architecture</b></td><td>64-bit x86</td><td> <ul><li> 64-bit x86 </li><li> 64-bit ARM (supported with Amazon EC2 instances running Amazon Linux 2, Amazon Linux 2023, RHEL 8.x/9.x, CentOS 9, Rocky Linux 8/9, Ubuntu 22.04, and Ubuntu 24.04 only) </li></ul> </td><td>64-bit ARM (DCV server is supported only on <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html">Amazon EC2 Apple silicon instances</a>)</td></tr>
  <tr><td rowspan="2"><b>GPU</b></td><td colspan="2">(Optional) An NVIDIA or AMD GPU is required for hardware-based video encoding. If your server does not have a GPU, software-based video encoding is used. <ul><li> NVIDIA GPUs require NVENC for hardware-based video encoding. An NVIDIA GPU with compute capabilities &gt;= <code>3.5</code> is required. </li><li> AMD GPUs require Advanced Media Framework (AMF) for Linux or Windows, or Rapidfire for Windows only, for hardware-based video encoding. For Linux, the AMF encoder can be used on Ubuntu instances by installing the additional package <code>amf-amdgpu-pro</code> provided by the AMD driver. </li></ul> </td><td>Amazon EC2 Apple silicon instances support hardware-based video encoding.</td></tr>
  <tr><td></td><td>An NVIDIA GPU is required for GPU sharing across virtual sessions. Only console sessions are supported on Linux servers with AMD GPUs. </td><td></td></tr>
  <tr><td><b>Network</b></td><td colspan="3">By default, the Amazon DCV server communicates over port 8443. The port is configurable but must be greater than 1024. Ensure that the server allows communication over the required port.</td></tr>
</tbody>
</table>


**Note**  
If you are running an operating system that has reached end of life, such as CentOS 7 or RHEL 7, Amazon DCV still offers support until the [End of Life](eosl.md) of that supported DCV version. Amazon DCV does not support operating systems that have reached end of life. Contact your vendor regarding your operating system.

For more information about the Amazon DCV Client requirements, see [ Amazon DCV Client requirements](https://docs.aws.amazon.com/dcv/latest/userguide/client.html#requirements) in the *Amazon DCV User Guide*.

## Supported Features
<a name="features"></a>

The following table compares the features that are supported by the Windows, Linux, and macOS Amazon DCV servers.


| Feature | [Windows Amazon DCV server](setting-up-installing-windows.md) | [Linux Amazon DCV server](setting-up-installing-linux.md) | [macOS Amazon DCV server](setting-up-installing-macos.md) | 
| --- | --- | --- | --- | 
| [Console sessions](managing-sessions.md) | ✓ | ✓ | ✓ | 
| [Virtual sessions](managing-sessions.md) | ✗ | ✓ | ✗ | 
| [QUIC (UDP) transport protocol](disable-quic.md) | ✓ | ✓ | ✓ | 
| [Configurable TCP/UDP ports and addresses](manage-port-addr.md) | ✓ | ✓ | ✓ | 
| [Custom TLS certificates](manage-cert.md) | ✓ | ✓ | ✓ | 
| [Idle client disconnection](manage-disconnect.md) | ✓ | ✓ | ✓ | 
| [GPU sharing](manage-gpu.md) | ✗ | ✓ | ✗ | 
| [USB remotization](manage-usb-remote.md) | ✓ | ✓ | ✗ | 
| [Smart card support](manage-smart-card.md) | ✓ | ✓ | ✗ | 
| Webcam support | ✓ (Windows 10 and Server 2016 and later) | ✗ | ✗ | 
| [Session storage and file transfer](manage-storage.md) | ✓ | ✓ | ✓ | 
| [Copying and pasting](manage-clipboard.md) | ✓ | ✓ | ✓ | 
| [Custom HTTP headers](manage-headers.md) | ✓ | ✓ | ✗ | 
| [Printing from sessions](manage-printer.md) | ✓ | ✓ | ✗ | 
| [Stereo 2.0 audio playback](manage-audio.md) | ✓ | ✓ | ✓ | 
| [Surround sound audio playback](manage-audio.md) | ✓ (up to 7.1) | ✓ (up to 5.1) | ✗ | 
| [Stereo 2.0 audio recording](manage-audio.md) | ✓ | ✓ | ✗ | 
| [Touchscreen support](enable-stylus.md) | ✓ (Windows 10 and Server 2016 and later) | ✓ | ✗ | 
| [Stylus support](enable-stylus.md) | ✓ (Windows 10 and Server 2019) | ✓ | ✗ | 
| [Gamepad support](enable-gamepad.md) | ✓ (Windows 10 and Server 2016 and later) | ✗ | ✗ | 
| Full screen selected monitors | ✓ | ✗ | ✓ | 
| Time zone redirection | ✓ | ✓ | ✓ | 
| WebAuthn redirection | ✓ | ✓ | ✗ | 
| Extensions SDK | ✓ | ✓ | ✗ | 

For more information about the Amazon DCV Client features, see [ Amazon DCV Client features](https://docs.aws.amazon.com/dcv/latest/userguide/client.html#client-features) in the *Amazon DCV User Guide*.