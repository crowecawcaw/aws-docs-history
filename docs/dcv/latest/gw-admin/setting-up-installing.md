# Installing the Amazon DCV Connection Gateway

This section describes how to install the latest version of the Amazon DCV Connection Gateway on a Linux host.
You can use multiple hosts to improve scalability and performance. For more information,
see [Scaling the Amazon DCV Connection Gateway](scaling.md "scaling.md").

###### Note

The Amazon DCV Connection Gateway is available for the Linux distributions and architectures listed in [System requirements](system-requirements.md "system-requirements.md").

The following instructions are for installing the Connection Gateway on 64-bit x86 hosts. To install the Connection Gateway on
64-bit ARM hosts, for Amazon Linux, RHEL, and CentOS, replace `x86_64`
with `aarch64`, and for Ubuntu, replace `amd64` with
`arm64`.

###### To install the Connection Gateway on a Linux host

1. The Amazon DCV Connection Gateway packages are digitally signed with a secure GPG signature. To allow the
   package manager to verify the package signature, you must import the
   Amazon DCV GPG key. Run the following command to import the Amazon DCV GPG key.
   - Amazon Linux 2, Amazon Linux 2023, RHEL, CentOS, and SUSE Linux Enterprise

   ```
   `$` sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   - Ubuntu

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   ```
   `$` gpg --import NICE-GPG-KEY
   ```

2. Download the Amazon DCV Connection Gateway installation package for your distribution from the [Amazon DCV download website](http://download.amazondcv.com "http://download.amazondcv.com").
   - Amazon Linux 2 (64-bit x86)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.el7.x86_64.rpm
   ```

   - Amazon Linux 2 (64-bit x86 ARM)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.el7.aarch64.rpm
   ```

   - Amazon Linux 2023 (64-bit x86)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.amzn2023.x86_64.rpm
   ```

   - Amazon Linux 2023 (64-bit x86 ARM)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.amzn2023.aarch64.rpm
   ```

   - RHEL 8.x, and Rocky Linux 8.x (64-bit x86)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.el8.x86_64.rpm
   ```

   - RHEL 8.x, and Rocky Linux 8.x (64-bit x86 ARM)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.el8.aarch64.rpm
   ```

   - RHEL 9.x, CentOS 9, and Rocky Linux 8.x (64-bit x86)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.el9.x86_64.rpm
   ```

   - RHEL 9.x, CentOS 9, and Rocky Linux 8.x (64-bit x86 ARM)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway-2025.0.870.el9.aarch64.rpm
   ```

   - Ubuntu 22.04 (64-bit x86)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway_2025.0.870_amd64.ubuntu2204.deb
   ```

   - Ubuntu 22.04 (64-bit ARM)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway_2025.0.870_arm64.ubuntu2204.deb
   ```

   - Ubuntu 24.04 (64-bit x86)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway_2025.0.870_amd64.ubuntu2404.deb
   ```

   - Ubuntu 24.04 (64-bit ARM)

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/Gateway/nice-dcv-connection-gateway_2025.0.870_arm64.ubuntu2404.deb
   ```
