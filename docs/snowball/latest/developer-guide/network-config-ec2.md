AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Network configurations for compute instances on Snowball Edge

After you launch your compute instance on a Snowball Edge, you must provide it with an IP
address by creating a network interface. Snowball Edges support two kinds of network interfaces,
a virtual network interface and a direct network interface.

**Virtual network interface (VNI)** – A virtual network interface is the standard network interface for connecting to an EC2-compatible
instance on your Snowball Edge. You must create a VNI for each of your EC2-compatible instances regardless
of whether you also use a direct network interface or not. The traffic passing through a
VNI is protected by the security groups that you set up. You can only associate VNIs
with the physical network port you use to control your Snowball Edge.

###### Note

VNI will use the same physical interface (RJ45, SFP+, or QSFP) that is used to managed the Snowball Edge. Creating a VNI on a different physical interface than the one being used for device management could lead to unexpected results.

**Direct network interface (DNI)** – A direct network interface (DNI) is an advanced network feature that enables use cases
like multicast streams, transitive routing, and load balancing. By providing instances
with layer 2 network access without any intermediary translation or filtering, you can
gain increased flexibility over the network configuration of your Snowball Edge and improved
network performance. DNIs support VLAN tags and customizing the MAC
address. Traffic on DNIs is not protected by security groups.

On Snowball Edge devices, DNIs can be associated with the RJ45, SFP, or QSFP ports. Each physical port supports a maximum of 63 DNIs. DNIs do not have to be associated to the same physical network port that you use to manage the Snowball Edge.

###### Note

Snowball Edge storage optimized (with EC2 compute functionality) devices don't support DNIs.

###### Topics

- [Prerequisites for DNIs or VNIs on Snowball Edge](#snowcone-configuration-prerequisites "#snowcone-configuration-prerequisites")
- [Setting up a Virtual Network Interface
  (VNI) on a Snowball Edge](#setup-vni "#setup-vni")
- [Setting Up a Direct Network Interface
  (DNI) on a Snowball Edge](#snowcone-setup-dni "#snowcone-setup-dni")

## Prerequisites for DNIs or VNIs on Snowball Edge

Before you configure a VNI or a DNI, be sure that you've done the following
prerequisites.

######

1. Make sure there's power to your device and that one of your physical
   network interfaces, like the RJ45 port, is connected with an IP
   address.
2. Get the IP address associated with the physical network interface that
   you're using on the Snowball Edge.
3. Configure the Snowball Edge client. For more information, see [Configuring a profile for the Snowball Edge
   Client](using-client-commands.md#client-configuration "using-client-commands.md#client-configuration").
4. Configure the AWS CLI. For more information, see [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the AWS Command Line Interface User Guide.
5. Unlock the device.
   - Use AWS OpsHub to unlock the device. For more information, see [Unlocking a Snowball Edge with AWS OpsHub](connect-unlock-device.md "connect-unlock-device.md").
   - Use the Snowball Edge Client to unlock the device. For more information, see [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md").

6. Launch an EC2-compatible instance on the device. You will associate the VNI with this
   instance.
7. Use the Snowball Edge Client to run the `describe-device` command. The output of the command will provide a list
   of physical network interface IDs. For more information, see [Viewing status of a Snowball Edge](using-client-commands.md#client-status "using-client-commands.md#client-status").
8. Identify the ID for the physical network interface that you want to use,
   and make a note of it.

## Setting up a Virtual Network Interface

(VNI) on a Snowball Edge

After you have identified the ID of the physical network interface, you can set
up a virtual network interface (VNI) with that physical interface. Use the following procedure set up a VNI. Make
sure that you perform the prerequisite tasks before you create a VNI.

###### Create a VNI and associate an IP address

1. Use the Snowball Edge Client to run the `create-virtual-network-interface`
   command. The following examples show running this command with the two
   different IP address assignment methods, either `DHCP` or
   `STATIC`. The `DHCP` method uses Dynamic Host
   Configuration Protocol (DHCP).

```
snowballEdge create-virtual-network-interface \
--physical-network-interface-id s.ni-`abcd1234` \
--ip-address-assignment DHCP \
--profile `profile-name`
        //OR//

snowballEdge create-virtual-network-interface \
--physical-network-interface-id s.ni-`abcd1234` \
--ip-address-assignment STATIC \
--static-ip-address-configuration IpAddress=`192.0.2.0`,Netmask=`255.255.255.0` \
--profile `profile-name`

```

The command returns a JSON structure that includes the IP address. Make a
note of that IP address to use with the `ec2 associate-address`
AWS CLI command later in the process.

Anytime you need this IP address, you can use the Snowball Edge Client command `describe-virtual-network-interfaces` Snowball Edge client command,
or the AWS CLI command `aws ec2 describe-addresses` to get
it. 2. Use the AWS CLI to associate the IP address with the EC2-compatible instance, replacing the red text with your values:

```
aws ec2 associate-address --public-ip `192.0.2.0` --instance-id `s.i-01234567890123456` --endpoint http://`Snowball Edge physical IP address`:8008
```

## Setting Up a Direct Network Interface

(DNI) on a Snowball Edge

###### Note

The direct network interface feature is available on or after January 12,
2021 and is available in all AWS Regions where Snowball Edges are
available.

### Prerequisites for a DNI on a Snowball Edge

Before you set up a direct network interface (DNI), you must perform the tasks
in the prerequisites section.

1. Perform the prerequisite tasks before setting up the DNI. For
   instructions, see [Prerequisites for DNIs or VNIs on Snowball Edge](#snowcone-configuration-prerequisites "#snowcone-configuration-prerequisites").
2. Additionally, you must launch an instance on your device, create a
   VNI, and associate it with the instance. For instructions, see [Setting up a Virtual Network Interface
   (VNI) on a Snowball Edge](#setup-vni "#setup-vni").

###### Note

If you added direct networking to your existing device by
performing an in-the-field software update, you must restart the
device twice to fully enable the feature.

###### Create a DNI and associate IP address

1. Create a direct network interface and attach it to the Amazon EC2-compatible instance by
   running the following command. You will need the MAC address of the device
   for the next step.

```
create-direct-network-interface [--endpoint `endpoint`] [--instance-id `instanceId`] [--mac `macAddress`]
                                [--physical-network-interface-id `physicalNetworkInterfaceId`]
                                [--unlock-code `unlockCode`] [--vlan `vlanId`]

```

OPTIONS

`--endpoint <endpoint>` The endpoint to send this
request to. The endpoint for your devices will be a URL using the
`https` scheme followed by an IP address. For example, if the
IP address for your device is 123.0.1.2, the endpoint for your device would
be https://123.0.1.2.

`--instance-id <instanceId>` The EC2-compatible instance ID
to attach the interface to (optional).

`--mac <macAddress>` Sets the MAC address of the
network interface (optional).

`--physical-network-interface-id
 <physicalNetworkInterfaceId>` The ID for the physical
network interface on which to create a new virtual network interface. You
can determine the physical network interfaces available on your Snowball
Edge using the `describe-device` command.

`--vlan <vlanId>` Set the assigned VLAN for the
interface (optional). When specified, all traffic sent from the interface is
tagged with the specified VLAN ID. Incoming traffic is filtered for the
specified VLAN ID, and has all VLAN tags stripped before being passed to the
instance. 2. After you create a DNI and associate it with your EC2-compatible instance, you must
make two configuration changes inside your Amazon EC2-compatible instance.

    * The first is to change ensure that packets meant for the VNI
     associated with the EC2-compatible instance are sent through eth0.
    * The second change configures your direct network interface to use
     either DCHP or static IP when booting.

The following are examples of shell scripts for Amazon Linux 2 and CentOS Linux that make these
configuration changes.

Amazon Linux 2

```
# Mac address of the direct network interface.
# You got this when you created the direct network interface.
DNI_MAC=[`MAC ADDRESS FROM CREATED DNI`]

# Configure routing so that packets meant for the VNI always are sent through eth0.
PRIVATE_IP=$(curl -s http://169.254.169.254/latest/meta-data/local-ipv4)
PRIVATE_GATEWAY=$(ip route show to match 0/0 dev eth0 | awk '{print $3}')
ROUTE_TABLE=10001
echo "from $PRIVATE_IP table $ROUTE_TABLE" > /etc/sysconfig/network-scripts/rule-eth0
echo "default via $PRIVATE_GATEWAY dev eth0 table $ROUTE_TABLE" > /etc/sysconfig/network-scripts/route-eth0
echo "169.254.169.254 dev eth0" >> /etc/sysconfig/network-scripts/route-eth0

# Query the persistent DNI name, assigned by udev via ec2net helper.
#   changable in /etc/udev/rules.d/70-persistent-net.rules
DNI=$(ip --oneline link | grep -i $DNI_MAC | awk -F ': ' '{ print $2 }')

# Configure DNI to use DHCP on boot.
cat << EOF > /etc/sysconfig/network-scripts/ifcfg-$DNI
DEVICE="$DNI"
NAME="$DNI"
HWADDR=$DNI_MAC
ONBOOT=yes
NOZEROCONF=yes
BOOTPROTO=dhcp
TYPE=Ethernet
MAINROUTETABLE=no
EOF

# Make all changes live.
systemctl restart network

```

CentOS Linux

```
# Mac address of the direct network interface. You got this when you created the direct network interface.
DNI_MAC=[`MAC ADDRESS FROM CREATED DNI`]
# The name to use for the direct network interface. You can pick any name that isn't already in use.
DNI=eth1

# Configure routing so that packets meant for the VNIC always are sent through eth0
PRIVATE_IP=$(curl -s http://*169.254.169.254*/latest/meta-data/local-ipv4)
PRIVATE_GATEWAY=$(ip route show to match 0/0 dev eth0 | awk '{print $3}')
ROUTE_TABLE=10001
echo from $PRIVATE_IP table $ROUTE_TABLE > /etc/sysconfig/network-scripts/rule-eth0
echo default via $PRIVATE_GATEWAY dev eth0 table $ROUTE_TABLE > /etc/sysconfig/network-scripts/route-eth0

# Configure your direct network interface to use DHCP on boot.
cat << EOF > /etc/sysconfig/network-scripts/ifcfg-$DNI
DEVICE="$DNI"
NAME="$DNI"
HWADDR="$DNI_MAC"
ONBOOT=yes
NOZEROCONF=yes
BOOTPROTO=dhcp
TYPE=Ethernet
EOF

# Rename DNI device if needed.
CURRENT_DEVICE_NAME=$(LANG=C ip -o link | awk -F ': ' -vIGNORECASE=1 '!/link\/ieee802\.11/ && /'"$DNI_MAC"'/ { print $2 }')
ip link set $CURRENT_DEVICE_NAME name $DNI

# Make all changes live.
systemctl restart network
```
