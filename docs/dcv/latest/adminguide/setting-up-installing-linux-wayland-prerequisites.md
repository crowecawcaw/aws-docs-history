

# Prerequisites for the Amazon DCV server on Linux with Wayland
<a name="setting-up-installing-linux-wayland-prerequisites"></a>

Amazon DCV enables clients to access a remote graphical session on a Linux server. This provides access to the corresponding Linux desktop. With Wayland, Amazon DCV supports virtual sessions only. For more information about virtual sessions, see [Managing Amazon DCV sessions](managing-sessions.md).

This topic describes how to install the prerequisites required to use Amazon DCV on a Linux server.

**Topics**
+ [Install a desktop environment and desktop manager](#linux-prereq-gui)
+ [Ensure the graphical session is running](#linux-prereq-graphical)
+ [Install the eglinfo utility](#linux-prereq-tools)
+ [Verify OpenGL software rendering](#linux-prereq-opengl)
+ [Install GPU drivers for graphics instances](#linux-prereq-gpu)

## Install a desktop environment and desktop manager
<a name="linux-prereq-gui"></a>

Install a desktop environment and desktop manager to improve your experience with Amazon DCV on a Linux server.

A desktop environment is a graphical user interface (GUI) that helps you to interact with the Linux operating system. A desktop manager is a program that manages the user login screen, and starts and stops the desktop environment sessions.

**Note**  
With the Wayland display protocol, Amazon DCV works only with the GNOME desktop environment and the GDM desktop manager.

The following tabbed content shows the steps for installing the default desktop environment and desktop manager on the supported operating systems.

------
#### [ RHEL, CentOS, and Rocky Linux 10 ]

The default desktop environment for RHEL, CentOS, and Rocky Linux 10 is GNOME and the default desktop manager is GDM.

**To install and configure the desktop environment and desktop manager on RHEL, CentOS, and Rocky Linux**

1. Install the desktop environment and the desktop manager packages.

   ```
   $ sudo dnf group install "Server with GUI"
   ```

1. Update the software packages to ensure that the Linux server is up to date.

   ```
   $ sudo dnf upgrade
   ```

1. Reboot the Linux server.

   ```
   $ sudo reboot
   ```

------
#### [ Ubuntu 26.04 ]

The default desktop environment for Ubuntu 26.04 is GNOME and the default desktop manager is GDM.

**To install and configure the desktop environment and desktop manager on Ubuntu 26.04**

1. Install the desktop environment and the desktop manager packages.

   ```
   $ sudo apt update
   ```

   ```
   $ sudo apt install ubuntu-desktop
   ```

1. Update the software packages to ensure that the Linux server is up to date.

   ```
   $ sudo apt upgrade
   ```

1. Reboot the Linux server.

   ```
   $ sudo reboot
   ```

------

## Ensure the graphical session is running
<a name="linux-prereq-graphical"></a>

Ensure that your Linux server boots into a graphical session and that the display manager is running.

We recommend that you configure your Linux server to start the graphical session automatically when it boots.

**To configure and start the graphical session on Linux:**

1. Configure the graphical session to start automatically when the Linux server boots.

   ```
   $ sudo systemctl set-default graphical.target
   ```

1. Start the graphical session.

   ```
   $ sudo systemctl isolate graphical.target
   ```

1. Verify that the graphical session is running.

   ```
   $ sudo systemctl status graphical.target
   ```

   The graphical session is running if the command reports that `graphical.target` is `active`.

## Install the eglinfo utility
<a name="linux-prereq-tools"></a>

The eglinfo utility provides information about your Linux server's OpenGL configuration. The utility can be used to determine whether your Linux server is configured to support OpenGL hardware or software rendering. It provides information about the drivers and supported extensions.

------
#### [ RHEL, CentOS, and Rocky Linux 10 ]

**To install the eglinfo utility**  
Run the following command:

```
$ sudo dnf install egl-utils
```

------
#### [ Ubuntu 26.04 ]

**To install the eglinfo utility**  
Run the following command:

```
$ sudo apt install mesa-utils
```

------

## Verify OpenGL software rendering
<a name="linux-prereq-opengl"></a>

On non-GPU Linux servers, OpenGL is only supported in software rendering mode using the Mesa drivers. If you're using a non-GPU Linux server and intend to use OpenGL, ensure that the Mesa drivers are installed and properly configured on your Linux server.

**Note**  
This applies to non-GPU Linux servers only.

**To verify that OpenGL software rendering is available**  
Use the following command:

```
$ sudo eglinfo -p surfaceless | grep -i "opengl.*version"
```

The following shows example output if OpenGL software rendering is available:

```
OpenGL core profile version: 4.5 (Core Profile) Mesa 25.2.7
OpenGL core profile shading language version: 4.50
OpenGL compatibility profile version: 4.5 (Compatibility Profile) Mesa 25.2.7
OpenGL compatibility profile shading language version: 4.50
OpenGL ES profile version: OpenGL ES 3.2 Mesa 25.2.7
OpenGL ES profile shading language version: OpenGL ES GLSL ES 3.20
```

## Install GPU drivers for graphics instances
<a name="linux-prereq-gpu"></a>

**Topics**
+ [Install and configure NVIDIA drivers](#gpu-nvidia)
+ [Install and configure AMD drivers](#gpu-amd)

### Install and configure NVIDIA drivers
<a name="gpu-nvidia"></a>

With Linux servers that have a dedicated NVIDIA GPU, ensure that the appropriate NVIDIA drivers are installed and properly configured. For instructions on how to install the NVIDIA drivers on an Amazon EC2 Linux instance, see [Installing the NVIDIA Driver on Linux Servers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html) in the *Amazon EC2 User Guide*.

**Note**  
This applies to Linux servers with NVIDIA GPUs only.
The GRID drivers support up to four 4K displays for each GPU installed. The gaming drivers support only one 4K display for each GPU installed.

**To verify that your NVIDIA GPU supports hardware-based video encoding**  
Make sure that it supports NVENC encoding and that it has compute capabilities greater than or equal to 3.5.

To verify NVENC support, see the [ NVIDIA Video Encode and Decode GPU Support Matrix](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new#Encoder). To check the compute capabilities, see the [NVIDIA Compute Capacility tables](https://developer.nvidia.com/cuda-gpus). 

If your NVIDIA GPU doesn't support NVENC encoding or if it doesn't have the required compute capabilities, software-based video encoding is used.

**To verify that OpenGL hardware rendering is available**  
Use the following command:

```
$ sudo eglinfo -p gbm | grep -i "opengl.*version"
```

The following shows example output if OpenGL hardware rendering is available.

```
OpenGL core profile version: 4.6.0 NVIDIA 595.91.07
OpenGL core profile shading language version: 4.60 NVIDIA
OpenGL compatibility profile version: 4.6.0 NVIDIA 595.91.07
OpenGL compatibility profile shading language version: 4.60 NVIDIA
OpenGL ES profile version: OpenGL ES 3.2 NVIDIA 595.91.07
OpenGL ES profile shading language version: OpenGL ES GLSL ES 3.20
```

### Install and configure AMD drivers
<a name="gpu-amd"></a>

An instance with an attached AMD GPU, such as a G4ad instance, must have the appropriate AMD driver installed. For instructions on how to install the AMD GPU drivers on a compatible Amazon EC2 instance, see [ Install AMD drivers on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-amd-driver.html).

For more information about Amazon EC2 G4ad instances, see the [Deep dive on the new Amazon EC2 G4ad instances ](https://aws.amazon.com/blogs/compute/deep-dive-on-the-new-amazon-ec2-g4ad-instances/) blog post.