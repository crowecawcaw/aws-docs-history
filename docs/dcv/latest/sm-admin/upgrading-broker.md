# Upgrading the Amazon DCV Session Manager broker

Amazon DCV Session Manager brokers pass API requests to their relevant agents. They are installed on a host
separate from the Amazon DCV servers. As part of routine maintenance, brokers need to be
upgraded to meet new standards and requirements. This section walks you through the
upgrading process of your Session Manager brokers.

###### To upgrade the broker

1. Connect to the host on which you intend to upgrade the broker.
2. Stop the broker service.

```
`$`  sudo systemctl stop dcv-session-manager-broker
```

3. Download the installation package.
   - Amazon Linux 2 and RHEL 7.x

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2024.0.531-1.el7.noarch.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2024.0.531-1.el8.noarch.rpm
   ```

   - Ubuntu 20.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2024.0.531-1_all.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2024.0.531-1_all.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$`  wget https://d1uj6qtbmh3dt5.cloudfront.net/2024.0/SessionManagerBrokers/nice-dcv-session-manager-broker-2024.0.531-1_all.ubuntu2404.deb
   ```

4. Install the package.
   - Amazon Linux 2 and RHEL 7.x

   ```
   `$`  sudo yum install -y nice-dcv-session-manager-broker-2024.0.531-1.el7.noarch.rpm
   ```

   - RHEL 8.x and Rocky Linux 8.x

   ```
   `$`  sudo yum install -y nice-dcv-session-manager-broker-2024.0.531-1.el8.noarch.rpm
   ```

   - Ubuntu 20.04

   ```
   `$`  sudo apt install -y nice-dcv-session-manager-broker-2024.0.531-1_all.ubuntu2004.deb
   ```

   - Ubuntu 22.04

   ```
   `$`  sudo apt install -y nice-dcv-session-manager-broker-2024.0.531-1_all.ubuntu2204.deb
   ```

   - Ubuntu 24.04

   ```
   `$`  sudo apt install -y nice-dcv-session-manager-broker-2024.0.531-1_all.ubuntu2404.deb
   ```

5. Start the broker service and ensure that it starts automatically every time the instance starts.

```
`$`  sudo systemctl start dcv-session-manager-broker && sudo systemctl enable dcv-session-manager-broker
```
