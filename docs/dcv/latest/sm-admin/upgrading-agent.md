# Upgrading the Amazon DCV Session Manager agent

Amazon DCV Session Manager agents receive instructions from the broker and run them on their respective Amazon DCV servers. As part of routine maintenance,
agents need to be upgraded to meet new standards and requirements. This section walks you through the upgrading process of your Session Manager agents.

Linux host

###### Note

The following instructions are for installing the agent on 64-bit x86 hosts. To install the agent on
64-bit ARM hosts, for Amazon Linux, RHEL, and Centos, replace `x86_64`
with `aarch64`, and for Ubuntu, replace `amd64` with
`arm64`.

###### To update the agent on a Linux host

1. Run the following command to stop the agent.

```
`$`  sudo systemctl stop dcv-session-manager-agent
```

2. Download the installation package.
   - Amazon Linux 2 and RHEL 7.x

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent-2024.0.852-1.el7.`x86_64`.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent-2024.0.852-1.el8.`x86_64`.rpm
   ```

   - Ubuntu 20.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent_2024.0.852-1_`amd64`.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent_2024.0.852-1_`amd64`.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent_2024.0.852-1_`amd64`.ubuntu2404.deb
   ```

   - SUSE Linux Enterprise 12

   ```
   `$`  curl -O https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent-2024.0.852-1.sles12.x86_64.rpm
   ```

   - SUSE Linux Enterprise 15

   ```
   `$`  curl -O https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent-2024.0.852-1.sles15.x86_64.rpm
   ```

3. Install the package.
   - Amazon Linux 2 and RHEL 7.x

   ```
   `$`  sudo yum install -y nice-dcv-session-manager-agent-2024.0.852-1.el7.`x86_64`.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$`  sudo yum install -y nice-dcv-session-manager-agent-2024.0.852-1.el8.`x86_64`.rpm
   ```

   - Ubuntu 20.04

   ```
   `$`  sudo apt install ./nice-dcv-session-manager-agent_2024.0.852-1_`amd64`.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$`  sudo apt install ./nice-dcv-session-manager-agent_2024.0.852-1_`amd64`.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$`  sudo apt install ./nice-dcv-session-manager-agent_2024.0.852-1_`amd64`.ubuntu2404.deb
   ```

   - SUSE Linux Enterprise 12

   ```
   `$`  sudo zypper install nice-dcv-session-manager-agent-2024.0.852-1.sles12.`x86_64`.rpm
   ```

   - SUSE Linux Enterprise 15

   ```
   `$`  sudo zypper install nice-dcv-session-manager-agent-2024.0.852-1.sles15.`x86_64`.rpm
   ```

4. Run the following command to start the agent.

```
`$`  sudo systemctl start dcv-session-manager-agent
```

Windows host

###### To update the agent on a Windows host

1. Stop the agent service. Run the following commands at the command prompt.

```
`C:\>`  sc stop DcvSessionManagerAgentService
```

2. Download the [agent installer](https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent-x64-Release-2024.0-852.msi "https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerAgents/nice-dcv-session-manager-agent-x64-Release-2024.0-852.msi").
3. Run the installer. On the Welcome screen, choose **Next**.
4. On the EULA screen, carefully read the license agreement, and if you agree, select
   **I accept the terms** and choose **Next**.
5. To begin the installation, choose **Install**.
6. Restart the agent service. Run the following commands
   at the command prompt.

```
`C:\>`  sc start DcvSessionManagerAgentService
```
