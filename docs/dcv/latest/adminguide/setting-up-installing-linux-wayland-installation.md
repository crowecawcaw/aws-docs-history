

# Installing the Amazon DCV Server on Linux with Wayland
<a name="setting-up-installing-linux-wayland-installation"></a>

The Amazon DCV server is installed using a series of RPM or .deb packages, depending on your host server's operating system. The packages install all required packages and their dependencies, and perform the required server configuration.

**Note**  
You must be signed in as the root user to install the Amazon DCV server.

## Install the Amazon DCV Server
<a name="linux-server-install"></a>

------
#### [ RHEL, CentOS, and Rocky Linux 10 ]

The Amazon DCV server is available for RHEL, CentOS, and Rocky Linux 10 servers based on the 64-bit x86 and 64-bit ARM architectures.

**To install the Amazon DCV server on RHEL, CentOS, and Rocky Linux 10**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The RPM packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.
   + 64-bit x86

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-el10-x86_64.tgz
     ```
   + 64-bit ARM

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-el10-aarch64.tgz
     ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  
64-bit x86  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-el10-x86_64.tgz
     ```
64-bit ARM  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-el10-aarch64.tgz
     ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.
   + 64-bit x86

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-el10-x86_64.tgz && cd nice-dcv-2026.0-24952-el10-x86_64
     ```
   + 64-bit ARM

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-el10-aarch64.tgz && cd nice-dcv-2026.0-24952-el10-aarch64
     ```

1. Install the Amazon DCV server.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.el10.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-server-2026.0.24952-1.el10.aarch64.rpm
     ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.
   + 64-bit x86

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.el10.x86_64.rpm
     ```
   + 64-bit ARM

     ```
     $ sudo dnf install nice-dcv-web-viewer-2026.0.24952-1.el10.aarch64.rpm
     ```

1. (Optional) If you plan to support specialized USB devices using USB remotization, install the DCV USB drivers. 

   To install the DCV USB drivers, you must have Dynamic Kernel Module Support (DKMS) installed on your server. Use the following commands to install DKMS.

   DKMS can be installed from the Extra Packages for Enterprise Linux (EPEL) repository. Run the following command to enable the EPEL repository:

   ```
   $ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
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

1. (Optional) If you need to use SSO with system auth, use the following command to install it.

   ```
   $ sudo dnf install nice-dcv-gnome-shell-extension-2026.0.80-1.el10.noarch.rpm
   ```

------
#### [ Ubuntu 26.04 ]

The Amazon DCV server is available for Ubuntu 26.04 servers based on the 64-bit x86 and 64-bit ARM architectures.

**To install the Amazon DCV server on Ubuntu 26.04**

1. Launch and connect to the server where you intend to install the Amazon DCV server.

1. The Amazon DCV server packages are digitally signed with a secure GPG signature. To allow the package manager to verify the package signature, you must import the Amazon DCV GPG key. To do so, open a terminal window and import the Amazon DCV GPG key.

   ```
   $ wget https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   ```
   $ gpg --import NICE-GPG-KEY
   ```

1. Download the packages from the [Amazon DCV download website](http://download.amazondcv.com). The deb packages are packaged into a `.tgz` archive. Make sure that you download the correct archive for your operating system.
   + 64-bit x86

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-ubuntu2604-x86_64.tgz
     ```
   + 64-bit ARM

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/2026.0/Servers/nice-dcv-2026.0-24952-ubuntu2604-aarch64.tgz
     ```
**Tip**  
The [latest packages](http://download.amazondcv.com/latest.html) page of the download website contains links that point to the newest available version. You can use these links to automatically retrieve the newest Amazon DCV packages.  
64-bit x86  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-ubuntu2604-x86_64.tgz
     ```
64-bit ARM  

     ```
     $ wget https://d1uj6qtbmh3dt5.cloudfront.net/nice-dcv-ubuntu2604-aarch64.tgz
     ```

1. Extract the contents of the `.tgz` archive and navigate into the extracted directory.
   + 64-bit x86

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-ubuntu2604-x86_64.tgz && cd nice-dcv-2026.0-24952-ubuntu2604-x86_64
     ```
   + 64-bit ARM

     ```
     $ tar -xvzf nice-dcv-2026.0-24952-ubuntu2604-aarch64.tgz && cd nice-dcv-2026.0-24952-ubuntu2604-aarch64
     ```

1. Install the Amazon DCV server.
   + 64-bit x86

     ```
     $ sudo apt install ./nice-dcv-server_2026.0.24952-1_amd64.ubuntu2604.deb
     ```
   + 64-bit ARM

     ```
     $ sudo apt install ./nice-dcv-server_2026.0.24952-1_arm64.ubuntu2604.deb
     ```

1. (Optional) If you plan to use the web client, install the `nice-dcv-web-viewer` package.
   + 64-bit x86

     ```
     $ sudo apt install ./nice-dcv-web-viewer_2026.0.24952-1_amd64.ubuntu2604.deb
     ```
   + 64-bit ARM

     ```
     $ sudo apt install ./nice-dcv-web-viewer_2026.0.24952-1_arm64.ubuntu2604.deb
     ```

1. Add the `dcv` user to the `video` group.

   ```
   $ sudo usermod -aG video dcv
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

   ```
   $ sudo apt install ./nice-dcv-gnome-shell-extension_2026.0.80-1_all.ubuntu2604.deb
   ```

------