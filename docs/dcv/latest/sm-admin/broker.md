# Step 2: Set up the Amazon DCV Session Manager broker

The broker must be installed on a Linux host. For more information about the supported Linux
distributions, see [Amazon DCV Session Manager requirements](requirements.md "requirements.md"). Install
the broker on a host that is separate from the agent and the Amazon DCV server host. The host can
be installed on a different private network, but it must be able to connect to and
communicate with the agent.

###### To install and start the broker

1. Connect to the host on which you intend to install the broker.
2. The packages are digitally signed with a secure GPG signature. To allow the
   package manager to verify the package signature, you must import the
   Amazon DCV GPG key. Run the following command to import the Amazon DCV GPG key.
   - Amazon Linux 2, RHEL, CentOS, and Rocky Linux

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

3. Download the installation package.
   - Amazon Linux 2

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2025.0.539-1.el7.noarch.rpm
   ```

   - Amazon Linux 2023

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2025.0.539-1.amzn2023.noarch.rpm
   ```

   - RHEL 8.x, and Rocky Linux 8.x

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2025.0.539-1.el8.noarch.rpm
   ```

   - CentOS 9.x, RHEL 9.x, and Rocky Linux 9.x

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2025.0.539-1.el9.noarch.rpm
   ```

   - Ubuntu 20.04

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker_2025.0.539-1_all.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker_2025.0.539-1_all.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/2025.0/SessionManagerBrokers/nice-dcv-session-manager-broker_2025.0.539-1_all.ubuntu2404.deb
   ```

4. Install the package.
   - Amazon Linux 2

   ```
   `$` sudo yum install -y ./nice-dcv-session-manager-broker-2025.0.539-1.el7.noarch.rpm
   ```

   - Amazon Linux 2023

   ```
   `$` sudo yum install -y ./nice-dcv-session-manager-broker-2025.0.539-1.amzn2023.noarch.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$` sudo yum install -y ./nice-dcv-session-manager-broker-2025.0.539-1.el8.noarch.rpm
   ```

   - CentOS 9.x, RHEL 9.x, and Rocky Linux 9.x

   ```
   `$` sudo yum install -y ./nice-dcv-session-manager-broker-2025.0.539-1.el9.noarch.rpm
   ```

   - Ubuntu 20.04

   ```
   `$` sudo apt install -y ./nice-dcv-session-manager-broker_2025.0.539-1_all.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$` sudo apt install -y ./nice-dcv-session-manager-broker_2025.0.539-1_all.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$` sudo apt install -y ./nice-dcv-session-manager-broker_2025.0.539-1_all.ubuntu2404.deb
   ```

5. Check that the default Java environment version is _11_

```
`$` java -version
```

If not, you can explicitly set the Java home directory that the broker will use to target the right Java version.
This is done setting the parameter `broker-java-home` in the broker configuration file. For more information, see
[broker Configuration File](broker-file.md "broker-file.md"). 6. Start the broker service and ensure that it starts automatically every time the instance starts.

```
`$`  sudo systemctl start dcv-session-manager-broker && sudo systemctl enable dcv-session-manager-broker
```

7. Place a copy of the broker's self-signed certificate in your user directory. You'll need it
   when you install the agents in the next step.

```
sudo cp /var/lib/dcvsmbroker/security/dcvsmbroker_ca.pem $HOME
```
