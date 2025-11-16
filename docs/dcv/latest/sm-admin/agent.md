# Step 3: Set up the Amazon DCV Session Manager agent

The agent must be installed on all of the Amazon DCV server hosts in the fleet. The agent can be installed
on both Windows and Linux servers. For more information about the supported operating
systems, see [Amazon DCV Session Manager requirements](requirements.md "requirements.md").

###### Prerequisites

The Amazon DCV server must be installed on the host before installing the agent.

Linux host

###### Note

The Session Manager agent is available for the Linux distributions and
architectures listed in [Requirements](requirements.md "requirements.md"):

The following instructions are for installing the agent on 64-bit x86 hosts. To install
the agent on 64-bit ARM hosts replace `x86_64` with `aarch64`.
For Ubuntu, replace `amd64` with
`arm64`.

###### To install the agent on a Linux host

1. The packages are digitally signed with a secure GPG signature. To allow the
   package manager to verify the package signature, you must import the
   Amazon DCV GPG key. Run the following command to import the Amazon DCV GPG key.
   - Amazon Linux 2, RHEL, CentOS, and SUSE Linux Enterprise

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

2. Download the installation package.
   - Amazon Linux 2

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-2025.0.801-1.el7.`x86_64`.rpm
   ```

   - Amazon Linux 2023

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-2025.0.886-1.amzn2023.`x86_64`.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-2025.0.886-1.el8.`x86_64`.rpm
   ```

   - CentOS 9.x, RHEL 9.x, and Rocky Linux 9.x

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-2025.0.886-1.el9.`x86_64`.rpm
   ```

   - Ubuntu 20.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent_2025.0.886-1_`amd64`.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent_2025.0.886-1_`amd64`.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent_2025.0.886-1_`amd64`.ubuntu2404.deb
   ```

   - SUSE Linux Enterprise 12

   ```
   `$` curl -O https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-2025.0.886-1.sles12.x86_64.rpm
   ```

   - SUSE Linux Enterprise 15

   ```
   `$` curl -O https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-2025.0.886-1.sles15.x86_64.rpm
   ```

3. Install the package.
   - Amazon Linux 2

   ```
   `$`  sudo yum install -y ./nice-dcv-session-manager-agent-2025.0.886-1.el7.`x86_64`.rpm
   ```

   - Amazon Linux 2023

   ```
   `$`  sudo yum install -y ./nice-dcv-session-manager-agent-2025.0.886-1.amzn2023.`x86_64`.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$`  sudo yum install -y ./nice-dcv-session-manager-agent-2025.0.886-1.el8.`x86_64`.rpm
   ```

   - CentOS 9.x, RHEL 9.x, and Rocky Linux 9.x

   ```
   `$`  sudo yum install -y ./nice-dcv-session-manager-agent-2025.0.886-1.el9.`x86_64`.rpm
   ```

   - Ubuntu 20.04

   ```
   `$`  sudo apt install ./nice-dcv-session-manager-agent_2025.0.886-1_`amd64`.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$`  sudo apt install ./nice-dcv-session-manager-agent_2025.0.886-1_`amd64`.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$`  sudo apt install ./nice-dcv-session-manager-agent_2025.0.886-1_`amd64`.ubuntu2404.deb
   ```

   - SUSE Linux Enterprise 12

   ```
   `$` sudo zypper install ./nice-dcv-session-manager-agent-2025.0.886-1.sles12.x86_64.rpm
   ```

   - SUSE Linux Enterprise 15

   ```
   `$` sudo zypper install ./nice-dcv-session-manager-agent-2025.0.886-1.sles15.x86_64.rpm
   ```

4. Place a copy of the broker's self-signed certificate (that you copied in the previous
   step) in the `/etc/dcv-session-manager-agent/` directory on the agent.
5. Open `/etc/dcv-session-manager-agent/agent.conf` using your preferred
   text editor and do the following.
   - For `broker_host`, specify the DNS name of
     the host on which the broker is installed.

   ###### Important

   If the broker is running on an Amazon EC2 instance, for `broker_host`
   you must specify the instance's private Ipv4 address.
   - (Optional) For `broker_port`, specify the port over which to
     communicate with the broker. By default the agent and the broker communicate
     over port `8445`. Only change this if you need to use a different
     port. If you do change it, ensure that the broker is configured to use the same
     port.
   - For `ca_file`, specify the full path the certificate file that you copied
     in the previous step. For example:

   ```
   ca_file = '/etc/dcv-session-manager-agent/`broker_cert`.pem'
   ```

   Alternatively, if you want to disable TLS verification, set `tls_strict`
   to `false`.

6. Save and close the file.
7. Run the following command to start the agent.

```
`$` sudo systemctl start dcv-session-manager-agent
```

Windows host

###### To install the agent on a Windows host

1. Download the [agent installer](https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-x64-Release-2025.0-886.msi "https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerAgents/nice-dcv-session-manager-agent-x64-Release-2025.0-886.msi").
2. Run the installer. On the Welcome screen, choose **Next**.
3. On the EULA screen, carefully read the license agreement, and if you agree, select
   **I accept the terms** and choose **Next**.
4. To begin the installation, choose **Install**.
5. Place a copy of the broker's self-signed certificate (that you copied in the previous
   step) in the `C:\Program Files\NICE\DCVSessionManagerAgent\conf\`
   folder on the agent.
6. Open `C:\Program Files\NICE\DCVSessionManagerAgent\conf\agent.conf` using
   your preferred text editor, and then do the following:
   - For `broker_host`, specify the DNS name of
     the host on which the broker is installed.

   ###### Important

   If the broker is running on an Amazon EC2 instance, for `broker_host`
   you must specify the instance's private IPv4 address.
   - (Optional) For `broker_port`, specify the port over which to
     communicate with the broker. By default the agent and the broker communicate
     over port `8445`. Only change this if you need to use a different
     port. If you do change it, ensure that the broker is configured to use the same
     port.
   - For `ca_file`, specify the full path the certificate file that you copied
     in the previous step. For example:

   ```
   ca_file = 'C:\Program Files\NICE\DCVSessionManagerAgent\conf\`broker_cert`.pem'
   ```

   Alternatively, if you want to disable TLS verification, set `tls_strict`
   to `false`.

7. Save and close the file.
8. Stop and restart the agent service for the changes to take effect. Run the following commands
   at the command prompt.

```
`C:\>` sc stop DcvSessionManagerAgentService
```

```
`C:\>` sc start DcvSessionManagerAgentService
```
