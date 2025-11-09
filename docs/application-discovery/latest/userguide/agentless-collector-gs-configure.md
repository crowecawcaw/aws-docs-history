AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Configuring

Agentless Collector

Application Discovery Service Agentless Collector (Agentless Collector) is an Amazon Linux 2
based virtual machine (VM). The following section describes how to configure a collector
VM on the Agentless Collector console's **Configure
Agentless Collector** page.

###### To configure a collector VM on the \*\*Configure

Agentless Collector\*\* page

1. For **Collector name**, enter a name for the collector to
   identify it. The name can contain spaces but it cannot contain special
   characters.
2. Under **Data synchronization**, enter the AWS access key
   and secret key for the AWS account IAM user to specify as the destination
   account to receive the data discovered by the collector. For information about
   the requirements for the IAM user, see [Deploying
   Application Discovery Service Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-iam-user "agentless-collector-deploying.md#agentless-collector-gs-iam-user").
   1. For **AWS access-key**, enter the access key of the
      AWS account IAM user that you're specifying as the destination
      account.
   2. For **AWS secret-key**, enter the secret key of the
      AWS account IAM user that you are you're specifying as the
      destination account.
   3. (Optional) If your network requires the use of a proxy to access
      AWS, enter the proxy host, proxy port, and, optionally, the
      credentials needed to authenticate with your existing proxy
      server.

3. Under **Agentless Collector password**, set up a
   password to use to authenticate access to Agentless Collector.
   - Passwords are case-sensitive
   - Passwords must be between 8 and 64 characters in length
   - Passwords must contain at least one character from each of the
     following four categories:
     - Lowercase letters (a-z)
     - Uppercase letters (A-Z)
     - Numbers (0-9)
     - Non-alphanumeric characters (@$!#%\*?&)

   - Passwords cannot contain special characters other than the following
     ones: @$!#%\*?&
   1. For **Agentless Collector password**, enter
      a password to use to authenticate access to the collector.
   2. For **Re-enter Agentless Collector
      password**, for verification, enter the password
      again.

4. Under **Other settings**, read the **License
   Agreement**. If you agree to accept it, select the check
   box.
5. To enable automatic updates for Agentless Collector, under
   **Other settings**, select **Automatically update
   Agentless Collector**. If you do not select this checkbox,
   you'll need to manually update Agentless Collector as described in
   [Manually updating
   Application Discovery Service Agentless Collector](agentless-collector-update.md "agentless-collector-update.md").
6. Choose **Save configurations**.
   The following topics describe optional collector configuration tasks.

###### Optional Configuration Tasks

- [(Optional) Configure a static
  IP address for the Agentless Collector VM](#agentless-collector-gs-configure-ip "#agentless-collector-gs-configure-ip")
- [(Optional) Reset the
  Agentless Collector VM back to using DHCP](#agentless-collector-gs-configure-dhcp "#agentless-collector-gs-configure-dhcp")
- [(Optional) Configure the
  Kerberos authentication protocol](#agentless-collector-gs-configure-kerberos "#agentless-collector-gs-configure-kerberos")

## (Optional) Configure a static

IP address for the Agentless Collector VM

The following steps describe how to configure a static IP address for the
Application Discovery Service Agentless Collector (Agentless Collector) VM. When first
installed, the collector VM is configured to use the Dynamic Host Configuration
Protocol (DHCP).

###### Note

The Agentless Collector supports IPv4. It does not support
IPv6.

Agentless Collector version 2

###### To configure a static IP address for the collector VM

1. Collect the following network information from VMware
   vCenter:
   - **Static IP address**
     – An unsigned IP address in the subnet. For
     example, 192.168.1.138.
   - **CIDR netmask** –
     To get the CIDR netmask, check the IP address setting of
     the VMware vCenter host that hosts the collector VM. For
     example, /24.
   - **Default Gateway**
     – To get the default gateway, check the IP
     address setting of the VMware vCenter host that hosts
     the collector VM. For example, 192.168.1.1.
   - **Primary DNS** –
     To get the primary DNS, check the IP address setting of
     the VMware vCenter host that hosts the collector VM. For
     example, 192.168.1.1.
   - (Optional) **Secondary
     DNS**
   - (Optional) **Local domain
     name** – This allows the collector
     to reach the vCenter host URL without the domain
     name.

2. Open the collector’s VM console and sign in as
   `ec2-user` using the password
   `collector` as shown in the following
   example.

```
username: ec2-user
password: collector
```

3. Disable the network interface, by entering the following
   command in the remote terminal.

```
sudo ip link set ens192 down
```

4. ######

Update the interface configuration by using the following
steps.

    1. Open 10-cloud-init-ens192.network in the vi editor by
     using the following command.



    ```
    sudo vi /etc/systemd/network/10-cloud-init-ens192.network
    ```
    2. Update the values, as shown in the following example,
     with the information that you collected in the **Collect network information**
     step.



    ```
    [Match]
    Name=ens192

    [Network]
    DHCP=no
    Address=`static-ip-value/CIDR-netmask`
    Gateway=`gateway-value`
    DNS=`dnsserver-value`
    ```

5. Update the Domain Name System (DNS) using the following
   steps.
   1. Open the `resolv.conf` file in vi
      using the following command.

   ```
   sudo vi /etc/resolv.conf
   ```

   2. Update the `resolv.conf` file in vi
      using the following command.

   ```
   search `localdomain-name`
   options timeout:2 attempts:5
   nameserver `dnsserver-value`
   ```

   The following example shows an edited
   `resolv.conf` file.

   ```
   search vsphere.local
   options timeout:2 attempts:5
   nameserver 192.168.1.1
   ```

6. Enable the network interface, by entering the following
   command.

```
sudo ip link set ens192 up
```

7. Reboot the VM as shown in the following example.

```
sudo reboot
```

8. Verify your network settings using the following steps.
   1. Check if the IP address is configured correctly, by
      entering the following commands.

   ```
   ifconfig
   ip addr show
   ```

   2. Check that the gateway was added correctly, by
      entering the following command.

   ```
   route -n
   ```

   The output should be similar to the following
   example.

   ```
   Kernel IP routing table
   Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
   0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth0
   172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
   192.168.1.0     0.0.0.0         255.255.255.0   U     0      0
   ```

   3. Verify that you can ping a public URL, by entering the
      following command.

   ```
   ping www.google.com
   ```

   4. Verify that you can ping the vCenter IP address or
      host name as shown in the following example.

   ```
   ping `vcenter-host-url`
   ```

Agentless Collector version 1

###### To configure a static IP address for the collector VM

1. Collect the following network information from VMware
   vCenter:
   - **Static IP address**
     – An unsigned IP address in the subnet. For
     example, 192.168.1.138.
   - **Network mask** –
     To get the network mask, check the IP address setting of
     the VMware vCenter host that hosts the collector VM. For
     example, 255.255.255.0.
   - **Default Gateway**
     – To get the default gateway, check the IP
     address setting of the VMware vCenter host that hosts
     the collector VM. For example, 192.168.1.1.
   - **Primary DNS** –
     To get the primary DNS, check the IP address setting of
     the VMware vCenter host that hosts the collector VM. For
     example, 192.168.1.1.
   - (Optional) **Secondary
     DNS**
   - (Optional) **Local domain
     name** – This allows the collector
     to reach the vCenter host URL without the domain
     name.

2. Open the collector’s VM console and sign in as
   `ec2-user` using the password
   `collector` as shown in the following
   example.

```
username: ec2-user
password: collector
```

3. Disable the network interface, by entering the following
   command in the remote terminal.

```
sudo /sbin/ifdown eth0
```

4. ######

Update the interface eth0 configuration using the following
steps.

    1. Open ifcfg-eth0 in the vi editor using the following
     command.



    ```
    sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
    ```
    2. Update the interface values, as shown in the following
     example, with the information that you collect in the
     **Collect network
     information** step.



    ```
    DEVICE=eth0
    BOOTPROTO=static
    ONBOOT=yes
    IPADDR=`static-ip-value`
    NETMASK=`netmask-value`
    GATEWAY=`gateway-value`
    TYPE=Ethernet
    USERCTL=yes
    PEERDNS=no
    RES_OPTIONS="timeout:2 attempts:5"
    ```

5. Update the Domain Name System (DNS) using the following
   steps.
   1. Open the `resolv.conf` file in vi
      using the following command.

   ```
   sudo vi /etc/resolv.conf
   ```

   2. Update the `resolv.conf` file in vi
      using the following command.

   ```
   search `localdomain-name`
   options timeout:2 attempts:5
   nameserver `dnsserver-value`
   ```

   The following example shows an edited
   `resolv.conf` file.

   ```
   search vsphere.local
   options timeout:2 attempts:5
   nameserver 192.168.1.1
   ```

6. Enable the network interface, by entering the following
   command.

```
sudo /sbin/ifup eth0
```

7. Reboot the VM as shown in the following example.

```
sudo reboot
```

8. Verify your network settings using the following steps.
   1. Check if the IP address is configured correctly, by
      entering the following commands.

   ```
   ifconfig
   ip addr show
   ```

   2. Check that the gateway was added correctly, by
      entering the following command.

   ```
   route -n
   ```

   The output should be similar to the following
   example.

   ```
   Kernel IP routing table
   Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
   0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth0
   172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
   192.168.1.0     0.0.0.0         255.255.255.0   U     0      0
   ```

   3. Verify that you can ping a public URL, by entering the
      following command.

   ```
   ping www.google.com
   ```

   4. Verify that you can ping the vCenter IP address or
      host name as shown in the following example.

   ```
   ping `vcenter-host-url`
   ```

## (Optional) Reset the

Agentless Collector VM back to using DHCP

The following steps describe how to reconfigure the Agentless Collector
VM to use DHCP.

Agentless Collector version 2

###### To configure the collector VM to use DHCP

1. Disable the network interface by running the following command
   in the remote terminal.

```
sudo ip link set ens192 down
```

2. Update the interface configuration by using the following
   steps.
   1. Open the
      `10-cloud-init-ens192.network`
      file in the vi editor by using the following
      command.

   ```
   sudo vi /etc/systemd/network/10-cloud-init-ens192.network
   ```

   2. Update the values as shown in the following
      example.

   ```
   [Match]
   Name=ens192

   [Network]
   DHCP=yes

   [DHCP]
   ClientIdentifier=mac
   ```

3. Reset the DNS setting, by entering the following
   command.

```
echo "" | sudo tee /etc/resolv.conf
```

4. Enable the network interface, by entering the following
   command.

```
sudo ip link set ens192 up
```

5. Reboot the collector VM as shown in the following
   example.

```
sudo reboot
```

Agentless Collector version 1

###### To configure the collector VM to use DHCP

1. Disable the network interface by running the following command
   in the remote terminal.

```
sudo /sbin/ifdown eth0
```

2. Update the network configuration by using the following
   steps.
   1. Open the `ifcfg-eth0` file in the
      vi editor using the following command.

   ```
   sudo /sbin/ifdown eth0
   ```

   2. Update the values in the `ifcfg-eth0` file as shown in the following
      example.

   ```
   DEVICE=eth0
   BOOTPROTO=dhcp
   ONBOOT=yes
   TYPE=Ethernet
   USERCTL=yes
   PEERDNS=yes
   DHCPV6C=yes
   DHCPV6C_OPTIONS=-nw
   PERSISTENT_DHCLIENT=yes
   RES_OPTIONS="timeout:2 attempts:5"
   ```

3. Reset the DNS setting by entering the following
   command.

```
echo "" | sudo tee /etc/resolv.conf
```

4. Enable the network interface by entering the following
   command.

```
sudo /sbin/ifup eth0
```

5. Reboot the collector VM as shown in the following
   example.

```
sudo reboot
```

## (Optional) Configure the

Kerberos authentication protocol

If your OS server supports the Kerberos authentication protocol, then you can use
this protocol to connect to your server. To do so, you must configure the
Application Discovery Service Agentless Collector VM.

The following steps describe how to configure the Kerberos authentication protocol
on your Application Discovery Service Agentless Collector VM.

###### To configure the Kerberos authentication protocol on your collector

VM

1. Open the collector’s VM console and sign in as
   `ec2-user` using the password
   `collector` as shown in the following
   example.

```
username: ec2-user
password: collector
```

2. Open the `krb5.conf` configuration file in the
   `/etc` folder. To do so, you can use the following code
   example.

```
cd /etc
sudo nano krb5.conf
```

3. Update the `krb5.conf` configuration file with the
   following information.

```
[libdefaults]
    forwardable = true
    dns_lookup_realm = true
    dns_lookup_kdc = true
    ticket_lifetime = 24h
    renew_lifetime = 7d
    default_realm = `default_Kerberos_realm`

[realms]
 `default_Kerberos_realm` = {
     kdc = `KDC_hostname`
     server_name = `server_hostname`
     default_domain = `domain_to_expand_hostnames`
 }

[domain_realm]
 .`domain_name` = `default_Kerberos_realm`
 `domain_name` = `default_Kerberos_realm`
```

Save the file and exit the text editor. 4. Reboot the collector VM as shown in the following example.

```
sudo reboot
```
