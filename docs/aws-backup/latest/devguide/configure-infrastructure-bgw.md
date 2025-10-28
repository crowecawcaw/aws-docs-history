# Configure your infrastructure to use Backup

gateway

Backup gateway requires the following network, firewall, and hardware configurations
to back up and restore your virtual machines.

## Network configuration

Backup gateway requires certain ports to be allowed for its operation. Allow the
following ports:

1. **TCP 443 Outbound**
   - Source: Backup gateway
   - Destination: AWS
   - Use: Allows Backup gateway to communicate with AWS.

2. **TCP 80 Inbound**
   - Source: The host you use to connect to the AWS Management Console
   - Destination: Backup gateway
   - Use: By local systems to obtain the Backup gateway activation key. Port 80
     is only used during activation of Backup gateway. AWS Backup does not require port
     80 to be publicly accessible. The required level of access to port 80 depends on
     your network configuration. If you activate your gateway from the AWS Management Console, the
     host from which you connect to the console must have access to your gateway's
     port 80.

3. **UDP 53 Outbound**
   - Source: Backup gateway
   - Destination: Domain Name Service (DNS) server
   - Use: Allows Backup gateway to communicate with the DNS.

4. **TCP 22 Outbound**
   - Source: Backup gateway
   - Destination: Support
   - Use: Allows Support to access your gateway to help you with issues. You don't
     need to open this port for the normal operation of your gateway, but you must
     open it for troubleshooting.

5. **UDP 123 Outbound**
   - Source: NTP client
   - Destination: NTP server
   - Use: Used by local systems to synchronize virtual machine time to the host
     time.

6. **TCP 443 Outbound**
   - Source: Backup gateway
   - Destination: VMware vCenter
   - Use: Allows Backup gateway to communicate with VMware vCenter.

7. **TCP 443 Outbound**
   - Source: Backup gateway
   - Destination: ESXi hosts
   - Use: Allows Backup gateway to communicate with ESXi hosts.

8. **TCP 902 Outbound**
   - Source: Backup gateway
   - Destination: VMware ESXi hosts
   - Use: Used for data transfer via Backup gateway.

The above ports are necessary for Backup gateway. See [Create a VPC
endpoint](backup-network.md#backup-privatelink "backup-network.md#backup-privatelink") for more information on how to configure Amazon VPC endpoints for
AWS Backup.

## Firewall configuration

Backup gateway requires access to the following service endpoints to communicate
with Amazon Web Services. If you use a firewall or router to filter or limit network traffic, you
must configure your firewall and router to allow these service endpoints for outbound
communication to AWS. Use of an HTTP proxy in between Backup gateway and service points is not supported.

```
proxy-app.backup-gateway.`region`.amazonaws.com:443
dp-1.backup-gateway.`region`.amazonaws.com:443
anon-cp.backup-gateway.`region`.amazonaws.com:443
client-cp.backup-gateway.`region`.amazonaws.com:443
```

## Configure your gateway for multiple NICs in VMware

You can maintain separate networks for your internal and external traffic by
attaching multiple virtual network interface connections (NICs) to your gateway and
then directing internal traffic (gateway to hypervisor) and external traffic
(gateway to AWS) separately.

By default, virtual machines connected to AWS Backup gateway have one network adapter
(`eth0`). This network includes the hypervisor, the virtual machines, and
network gateway (Backup gateway) which communicates with the broader Internet.

Here is an example of a setup with multiple virtual network interfaces:

```

            eth0:
            - IP: 10.0.3.83
            - routes: 10.0.3.0/24

            eth1:
            - IP: 10.0.0.241
            - routes: 10.0.0.0/24
            - default gateway: 10.0.0.1
```

- In this example, the connection is to a hypervisor with IP
  `10.0.3.123`, the gateway
  will use `eth0` as the hypervisor IP is part of the `10.0.3.0/24`
  block
- To connect to a hypervisor with IP `10.0.0.234`, the gateway
  will use `eth1`
- To connect to an IP outside of the local networks
  (ex. `34.193.121.211`), the gateway will fall back to the default gateway,
  `10.0.0.1`, which is in the `10.0.0.0/24` block and thus go
  through `eth1`

The first sequence to add an additional network adapter occurs in the vSphere client:

1. In the VMware vSphere client, open the context menu (with a right-click)
   for your gateway virtual machine, and choose **Edit Settings**.
2. On the **Virtual Hardware** tab of the
   **Virtual Machine Properties** dialog box, open the
   **Add New Device** menu, and select
   **Network Adapter** to add a new network adapter.
3. 1. Expand the **New Networ**k details to configure
      the new adapter.
   2. Ensure that **Connect At Power On** is selected.
   3. For **Adapter Type**, see
      Network Adapter Types in the
      [ESXi and vCenter Server Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html "https://docs.vmware.com/en/VMware-vSphere/index.html").
4. Click **Okay** to save the new network adapter settings.

The next sequence of steps to configure an additional adapter occurs in the AWS Backup gateway console
(note this is not the same interface as the AWS management console where backups and other services are
managed).

Once the new NIC is added to the gateway VM, you need to

- Go to `Command Prompt` and turn on the new adapters
- Configure static IPs for each new NIC
- Set the preferred NIC as the default

To do these:

1. In the VMware vSphere client, select your gateway virtual machine and
   **Launch Web Console** to access the Backup gateway local console.
   1. For more information on accessing a local console, see
      [Accessing the Gateway Local Console with VMware ESXi](../../../storagegateway/latest/tgw/accessing-local-console.md#MaintenanceConsoleWindowVMware-common "../../../storagegateway/latest/tgw/accessing-local-console.md#MaintenanceConsoleWindowVMware-common")

2. Exit Command Prompt and go to Network Configuration > Configure Static IP
   and follow the setup instructions to update the routing table.
   1. Assign a static IP within the network adapter’s subnet.
   2. Set up a network mask.
   3. Enter the IP address of the default gateway. This is the network
      gateway that connects to all traffic outside of the local network.

3. Select **Set Default Adapter** to designate the adapter that
   will be connected to the cloud as the default device.
4. All IP addresses for the gateway can be displayed in both the local
   console and on the VM summary page in VMware vSphere.

## Hardware requirements

You must be able to dedicate the following minimum resources on a virtual machine
host for the Backup gateway:

- 4 virtual processors
- 8 GB of reserved RAM
- 80 GB disk space

## VMware permissions

This section lists the minimum VMware permissions required to use AWS Backup gateway.
These permissions are necessary for Backup gateway to discover, backup, and restore
virtual machines.

To use Backup gateway with VMware Cloud™ on AWS or VMware Cloud™ on AWS Outposts, you must use
the default admin user `cloudadmin@vmc.local` or assign the CloudAdmin
role to your dedicated user.

To use Backup gateway with VMware on-premises virtual machines,
create a dedicated user with the permissions listed below.

###### Global

- Disable methods
- Enable methods
- Licenses
- Log event
- Manage custom attributes
- Set custom attributes

###### vSphere Tagging

- Assign or Unassign vSphere Tag

###### DataStore

- Allocate space
- Browse datastore
- Configure datastore (for vSAN datastore)
- Low level file operations
- Update virtual machine files

###### Host

- Configuration
  - Advanced settings
  - Storage partition configuration

###### Folder

- Create folder

###### Network

- Assign network

###### dvPort Group

- Create
- Delete

###### Resource

- Assign virtual machine to resource pool

###### Virtual Machine

- Change Configuration
  - Acquire disk lease
  - Add existing disk
  - Add new disk
  - Advanced configuration
  - Change settings
  - Configure raw device
  - Modify device settings
  - Remove disk
  - Set annotation
  - Toggle disk change tracking

- Edit Inventory
  - Create from existing
  - Create new
  - Register
  - Remove
  - Unregister

- Interaction
  - Power Off
  - Power On

- Provisioning
  - Allow disk access
  - Allow read-only disk access
  - Allow virtual machine download

- Snapshot Management
  - Create snapshot
  - Remove Snapshot
  - Revert to snapshot
