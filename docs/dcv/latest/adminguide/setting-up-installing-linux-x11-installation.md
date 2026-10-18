

# Installing the Amazon DCV Server on Linux with X11
<a name="setting-up-installing-linux-x11-installation"></a>

The Amazon DCV server is installed using a series of RPM or .deb packages, depending on your host server's operating system. The packages install all required packages and their dependencies, and perform the required server configuration.

**Note**  
You must be signed in as the root user to install the Amazon DCV server.

## Install the Amazon DCV Server
<a name="linux-server-install"></a>

------
#### [ Amazon Linux 2023 ]

The Amazon DCV server is available for Amazon Linux 2023 servers based on the 64-bit x86 and 64-bit ARM architectures.

**Important**  
The `nice-dcv-gl` and `nice-dcv-gltest` packages aren't available for servers based on the 64-bit ARM architecture.

**To install the Amazon DCV server on Amazon Linux 2023**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The RPM packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.
   + 64-bit x86

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-amzn2023-x86_64.tgz
     ```
   + 64-bit ARM

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-amzn2023-aarch64.tgz
     ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  
64-bit x86  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-amzn2023-x86_64.tgz
     ```
64-bit ARM  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-amzn2023-aarch64.tgz
     ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.
   + 64-bit x86

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-amzn2023-x86_64.tgz && cd nice-dcv-2026.0-24952-amzn2023-x86_64
     ```
   + 64-bit ARM

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-amzn2023-aarch64.tgz && cd nice-dcv-2026.0-24952-amzn2023-aarch64
     ```

1. Install the Amazon DCV server.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.amzn2023.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.amzn2023.aarch64.rpm
     ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.amzn2023.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.amzn2023.aarch64.rpm
     ```

1. (Optional) If you plan to use virtual sessions, install the `nice-xdcv` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-xdcv-2026.0.714-1.amzn2023.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-xdcv-2026.0.714-1.amzn2023.aarch64.rpm
     ```

1. (Optional) If you plan to use GPU sharing, install the `nice-dcv-gl` package. 
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-gl-2026.0.1122-1.amzn2023.x86_64.rpm
     ```
**Note**  
You can optionally install the `nice-dcv-gltest` package. This package includes a simple OpenGL application that can be used to determine if your virtual sessions are properly configured to use hardware-based OpenGL.

1. (Optional) If you plan to use Amazon DCV [external authenticator](https://docs.aws.amazon.com/dcv/latest/adminguide/external-authentication.html), use the `nice-dcv-simple-external-authenticator` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-simple-external-authenticator-2026.0.300-1.amzn2023.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-simple-external-authenticator-2026.0.300-1.amzn2023.aarch64.rpm
     ```

1. (Optional) If you plan to support specialized USB devices using USB remotization, install the DCV USB drivers. 

   To install the DCV USB drivers, you must have Dynamic Kernel Module Support (DKMS) installed on your server. Use the following commands to install DKMS.

   ```
   $ sudo dnf install dkms
   ```

   After you installed DKMS, run the following command to install the DCV USB drivers:

   ```
   $ sudo dcvusbdriverinstaller
   ```

1. (Optional) If you plan to support the microphone redirection, verify that the `pulseaudio-utils` package is installed on your system. Use the following command to install it.

   ```
   $ sudo dnf install pulseaudio-utils
   ```

------
#### [ RHEL, CentOS, and Rocky Linux 8 ]

The Amazon DCV server is available for RHEL, CentOS, and Rocky Linux 8 servers based on the 64-bit x86 and 64-bit ARM architectures.

**Important**  
The `nice-dcv-gl` and `nice-dcv-gltest` packages aren't available for servers based on the 64-bit ARM architecture.

**To install the Amazon DCV server on RHEL, CentOS, and Rocky Linux 8**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The RPM packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.
   + 64-bit x86

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-el8-x86_64.tgz
     ```
   + 64-bit ARM

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-el8-aarch64.tgz
     ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  
64-bit x86  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-el8-x86_64.tgz
     ```
64-bit ARM  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-el8-aarch64.tgz
     ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.
   + 64-bit x86

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-el8-x86_64.tgz && cd nice-dcv-2026.0-24952-el8-x86_64
     ```
   + 64-bit ARM

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-el8-aarch64.tgz && cd nice-dcv-2026.0-24952-el8-aarch64
     ```

1. Install the Amazon DCV server.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.el8.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.el8.aarch64.rpm
     ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.el8.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.el8.aarch64.rpm
     ```

1. (Optional) If you plan to use virtual sessions, install the `nice-xdcv` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-xdcv-2026.0.714-1.el8.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-xdcv-2026.0.714-1.el8.aarch64.rpm
     ```

1. (Optional) If you plan to use GPU sharing, install the `nice-dcv-gl` package. 
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-gl-2026.0.1122-1.el8.x86_64.rpm
     ```
**Note**  
You can optionally install the `nice-dcv-gltest` package. This package includes a simple OpenGL application that can be used to determine if your virtual sessions are properly configured to use hardware-based OpenGL.

1. (Optional) If you plan to use Amazon DCV with Amazon DCV EnginFrame, install the `nice-dcv-simple-external-authenticator` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-simple-external-authenticator-2026.0.300-1.el8.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-simple-external-authenticator-2026.0.300-1.el8.aarch64.rpm
     ```

1. (Optional) If you plan to support specialized USB devices using USB remotization, install the DCV USB drivers. 

   To install the DCV USB drivers, you must have Dynamic Kernel Module Support (DKMS) installed on your server. Use the following commands to install DKMS.

   DKMS can be installed from the Extra Packages for Enterprise Linux (EPEL) repository. Run the following command to enable the EPEL repository:

   ```
   $ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
   ```

   After you enabled the EPEL repository, run the following command to install DKMS:

   ```
   $ sudo dnf install dkms
   ```

   After you installed DKMS, run the following command to install the DCV USB drivers:

   ```
   $ sudo dcvusbdriverinstaller
   ```

1. (Optional) If you plan to support the microphone redirection, verify that the `pulseaudio-utils` package is installed on your system. Use the following command to install it.

   ```
   $ sudo dnf install pulseaudio-utils
   ```

------
#### [ RHEL, CentOS, and Rocky Linux 9 ]

The Amazon DCV server is available for RHEL, CentOS, and Rocky Linux 9 servers based on the 64-bit x86 and 64-bit ARM architectures.

**Important**  
The `nice-dcv-gl` and `nice-dcv-gltest` packages aren't available for servers based on the 64-bit ARM architecture.

**To install the Amazon DCV server on RHEL, CentOS, and Rocky Linux 9**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The RPM packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.
   + 64-bit x86

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-el9-x86_64.tgz
     ```
   + 64-bit ARM

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-el9-aarch64.tgz
     ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  
64-bit x86  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-el9-x86_64.tgz
     ```
64-bit ARM  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-el9-aarch64.tgz
     ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.
   + 64-bit x86

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-el9-x86_64.tgz && cd nice-dcv-2026.0-24952-el9-x86_64
     ```
   + 64-bit ARM

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-el9-aarch64.tgz && cd nice-dcv-2026.0-24952-el9-aarch64
     ```

1. Install the Amazon DCV server.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.el9.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.el9.aarch64.rpm
     ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.el9.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.el9.aarch64.rpm
     ```

1. (Optional) If you plan to use virtual sessions, install the `nice-xdcv` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-xdcv-2026.0.714-1.el9.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-xdcv-2026.0.714-1.el9.aarch64.rpm
     ```

1. (Optional) If you plan to use GPU sharing, install the `nice-dcv-gl` package. 
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-gl-2026.0.1122-1.el9.x86_64.rpm
     ```
**Note**  
You can optionally install the `nice-dcv-gltest` package. This package includes a simple OpenGL application that can be used to determine if your virtual sessions are properly configured to use hardware-based OpenGL.

1. (Optional) If you plan to use Amazon DCV with Amazon DCV EnginFrame, install the `nice-dcv-simple-external-authenticator` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-simple-external-authenticator-2026.0.300-1.el9.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-simple-external-authenticator-2026.0.300-1.el9.aarch64.rpm
     ```

1. (Optional) If you plan to support specialized USB devices using USB remotization, install the DCV USB drivers. 

   To install the DCV USB drivers, you must have Dynamic Kernel Module Support (DKMS) installed on your server. Use the following commands to install DKMS.

   DKMS can be installed from the Extra Packages for Enterprise Linux (EPEL) repository. Run the following command to enable the EPEL repository:

   ```
   $ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
   ```

   After you enabled the EPEL repository, run the following command to install DKMS:

   ```
   $ sudo dnf install dkms
   ```

   After you installed DKMS, run the following command to install the DCV USB drivers:

   ```
   $ sudo dcvusbdriverinstaller
   ```

1. (Optional) If you plan to support the microphone redirection, verify that the `pulseaudio-utils` package is installed on your system. Use the following command to install it.

   ```
   $ sudo dnf install pulseaudio-utils
   ```

------
#### [ SLES 15 ]

The Amazon DCV server is available for SUSE Linux Enterprise Server (SLES) 15 servers based on the 64-bit x86 architecture only.

**To install the Amazon DCV server on SLES 15**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The RPM packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.

   ```
   $ curl -O https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-sles15-x86_64.tgz
   ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  

   ```
   $ curl -O https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-sles15-x86_64.tgz
   ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.

   ```
   $ tar -xvzf nice-dcv-2026.0-24952-sles15-x86_64.tgz && cd nice-dcv-2026.0-24952-sles15-x86_64
   ```

1. Install the Amazon DCV server.

   ```
   $ sudo zypper install nice-dcv-server-2026.0.24952-1.sles15.x86_64.rpm
   ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.

   ```
   $ sudo zypper install nice-dcv-web-viewer-2026.0.24952-1.sles15.x86_64.rpm
   ```

1. (Optional) If you plan to use virtual sessions, install the `nice-xdcv` package.

   ```
   $ sudo zypper install nice-xdcv-2026.0.714-1.sles15.x86_64.rpm
   ```

1. (Optional) If you plan to use GPU sharing, install the `nice-dcv-gl` package. 

   ```
   $ sudo zypper install nice-dcv-gl-2026.0.1122-1.sles15.x86_64.rpm
   ```
**Note**  
You can optionally install the `nice-dcv-gltest` package. This package includes a simple OpenGL application that can be used to determine whether your virtual sessions are properly configured to use hardware-based OpenGL. 

1. (Optional) If you plan to use Amazon DCV with Amazon DCV EnginFrame, install the `nice-dcv-simple-external-authenticator` package. 

   ```
   $ sudo zypper install nice-dcv-simple-external-authenticator-2026.0.300-1.sles15.x86_64.rpm
   ```

1. (Optional) If you plan to support specialized USB devices using USB remotization, install the DCV USB drivers. 

   To install the DCV USB drivers, you must have Dynamic Kernel Module Support (DKMS) installed on your server. Use the following commands to install DKMS.

   Enable the PackageHub repository.

   ```
   $ sudo SUSEConnect -p PackageHub/{{15}}/x86_64
   ```
**Note**  
If you're using SLES 15 SP1 or SP2, replace {{15}} in the command above with either `15.1` or `15.2`. 

   Install DKMS.

   ```
   $ sudo zypper refresh
   ```

   ```
   $ sudo zypper install dkms
   ```

   Install the kernel source.

   ```
   $ sudo zypper install -y kernel-source
   ```

   Reboot the instance.

   ```
   $ sudo reboot
   ```

   After you installed DKMS, run the following command to install the DCV USB drivers:

   ```
   $ sudo dcvusbdriverinstaller
   ```

1. (Optional) If you plan to support the microphone redirection, verify that the `pulseaudio-utils` package is installed on your system. Use the following command to install it.

   ```
   $ sudo zypper install pulseaudio-utils
   ```

------
#### [ Ubuntu 22.04/24.04 ]

The Amazon DCV server is available for Ubuntu 22.04/24.04 servers based on the 64-bit x86 and 64-bit ARM architectures.

**Important**  
The `nice-dcv-gl` and `nice-dcv-gltest` packages aren't available for servers based on the 64-bit ARM architecture.

**To install the Amazon DCV server on Ubuntu 22.04/24.04**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ wget https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   ```
   $ gpg --import NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The deb packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-ubuntu2204-x86_64.tgz
     ```
   + Ubuntu 22.04 (64-bit ARM)

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-ubuntu2204-aarch64.tgz
     ```
   + Ubuntu 24.04 (64-bit x86)

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-ubuntu2404-x86_64.tgz
     ```
   + Ubuntu 24.04 (64-bit ARM)

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-ubuntu2404-aarch64.tgz
     ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  
Ubuntu 22.04 (64-bit x86)  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-ubuntu2204-x86_64.tgz
     ```
Ubuntu 22.04 (64-bit ARM)  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-ubuntu2204-aarch64.tgz
     ```
Ubuntu 24.04 (64-bit x86)  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-ubuntu2404-x86_64.tgz
     ```
Ubuntu 24.04 (64-bit ARM)  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-ubuntu2404-aarch64.tgz
     ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-ubuntu2204-x86_64.tgz && cd nice-dcv-2026.0-24952-ubuntu2204-x86_64
     ```
   + Ubuntu 22.04 (64-bit ARM)

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-ubuntu2204-aarch64.tgz && cd nice-dcv-2026.0-24952-ubuntu2204-aarch64
     ```
   + Ubuntu 24.04 (64-bit x86)

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-ubuntu2404-x86_64.tgz && cd nice-dcv-2026.0-24952-ubuntu2404-x86_64
     ```
   + Ubuntu 24.04 (64-bit ARM)

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-ubuntu2404-aarch64.tgz && cd nice-dcv-2026.0-24952-ubuntu2404-aarch64
     ```

1. Install the Amazon DCV server.
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-server_2026.0.24952-1_amd64.ubuntu2204.deb
     ```
   + Ubuntu 22.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-dcv-server_2026.0.24952-1_arm64.ubuntu2204.deb
     ```
   + Ubuntu 24.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-server_2026.0.24952-1_amd64.ubuntu2404.deb
     ```
   + Ubuntu 24.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-dcv-server_2026.0.24952-1_arm64.ubuntu2404.deb
     ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-web-viewer_2026.0.24952-1_amd64.ubuntu2204.deb
     ```
   + Ubuntu 22.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-dcv-web-viewer_2026.0.24952-1_arm64.ubuntu2204.deb
     ```
   + Ubuntu 24.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-web-viewer_2026.0.24952-1_amd64.ubuntu2404.deb
     ```
   + Ubuntu 24.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-dcv-web-viewer_2026.0.24952-1_arm64.ubuntu2404.deb
     ```

1. Add the `dcv` user to the `video` group.

   ```
   $ sudo usermod -aG video dcv
   ```

1. (Optional) If you plan to use virtual sessions, install the `nice-xdcv` package.
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-xdcv_2026.0.714-1_amd64.ubuntu2204.deb
     ```
   + Ubuntu 22.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-xdcv_2026.0.714-1_arm64.ubuntu2204.deb
     ```
   + Ubuntu 24.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-xdcv_2026.0.714-1_amd64.ubuntu2404.deb
     ```
   + Ubuntu 24.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-xdcv_2026.0.714-1_arm64.ubuntu2404.deb
     ```

1. (Optional) If you plan to use GPU sharing, install the `nice-dcv-gl` package. 
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-gl_2026.0.1122-1_amd64.ubuntu2204.deb
     ```
**Note**  
You can optionally install the `nice-dcv-gltest` package. This package includes a simple OpenGL application that can be used to determine if your virtual sessions are properly configured to use hardware-based OpenGL.

1. (Optional) If you plan to use Amazon DCV with Amazon DCV EnginFrame, install the `nice-dcv-simple-external-authenticator` package. 
   + Ubuntu 22.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-simple-external-authenticator_2026.0.300-1_amd64.ubuntu2204.deb
     ```
   + Ubuntu 22.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-dcv-simple-external-authenticator_2026.0.300-1_arm64.ubuntu2204.deb
     ```
   + Ubuntu 24.04 (64-bit x86)

     ```
     $ sudo apt install ./nice-dcv-simple-external-authenticator_2026.0.300-1_amd64.ubuntu2404.deb
     ```
   + Ubuntu 24.04 (64-bit ARM)

     ```
     $ sudo apt install ./nice-dcv-simple-external-authenticator_2026.0.300-1_arm64.ubuntu2404.deb
     ```

1. (Optional) If you plan to support specialized USB devices using USB remotization, install the DCV USB drivers. 

   To install the DCV USB drivers, you must have Dynamic Kernel Module Support (DKMS) installed on your server. Use the following commands to install DKMS.

   DKMS is available in the official Ubuntu repository. Run the following command to install DKMS:

   ```
   $ sudo apt install dkms
   ```

   After you installed DKMS, run the following command to install the DCV USB drivers:

   ```
   $ sudo dcvusbdriverinstaller
   ```

1. (Optional) If you plan to support the microphone redirection, verify that the `pulseaudio-utils` package is installed on your system. Use the following command to install it.

   ```
   $ sudo apt install pulseaudio-utils
   ```

1. (Optional) If you need to use SSO with system auth, use the following command to install it.
   + Ubuntu 22.04

     ```
     $ sudo apt install ./nice-dcv-gnome-shell-extension_2026.0.80-1_all.ubuntu2204.deb
     ```
   + Ubuntu 24.04

     ```
     $ sudo apt install ./nice-dcv-gnome-shell-extension_2026.0.80-1_all.ubuntu2404.deb
     ```

------