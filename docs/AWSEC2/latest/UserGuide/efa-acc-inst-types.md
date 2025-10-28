# Maximize network bandwidth on Amazon EC2 instances with multiple network cards

Many instances types that support EFA also have multiple network cards. For more information,
see [Network cards](using-eni.md#network-cards "using-eni.md#network-cards"). If you plan to use EFA with
one of these instance types, we recommend the following basic configuration:

- For the primary network interface (network card index `0`, device index
  `0`), create an EFA (EFA with ENA) interface. You can't use an EFA-only network
  interface as the primary network interface.
- For each additional network interface, use the next unused network card index, device
  index `1`, and either an EFA (EFA with ENA) or EFA-only network interface,
  depending on your usecase, such as ENA bandwidth requirements or IP address space. For
  example use cases, see [EFA configuration for a P5 and P5e instances](#efa-for-p5 "#efa-for-p5").

###### Note

P5 instances require network interfaces to be configured in a specific manner to
enable maximum network bandwidth. For more information, see [EFA configuration for a P5 and P5e instances](#efa-for-p5 "#efa-for-p5").

The following examples show how to launch an instance based on these recommendations.

Instance launch

###### To specify EFAs during instance launch using the launch instance wizard

1. In the **Network settings** section, choose
   **Edit**.
2. Expand **Advanced network configuration**.
3. For the primary network interface (**Network interface 1**), select
   **Network card index = 0**, **Device index = 0**,
   and **Interface type = EFA with ENA**.
4. For each additional network interface required, choose **Add network interface**.
   For **Network card index** select the next unused index, and then select
   **Device index = 1**, and **Interface type = EFA with ENA**
   or **EFA-only**.

###### To specify EFAs during instance launch using the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")

command

For `--network-interfaces`, specify the required number of network interfaces.
For the primary network interface, specify `NetworkCardIndex=0`, `DeviceIndex=0`,
and `InterfaceType=efa`. For any additional network interfaces, for
`NetworkCardIndex` specify the next unused index, `DeviceIndex=1`,
and `InterfaceType=efa` or `efa-only`.

The following example command snippet shows a request with 32 EFA devices and one ENA device.

```
`$` aws ec2 run-instances \
 --instance-type p5.48xlarge \
 --count 1 \
 --key-name `key_pair_name` \
 --image-id `ami-0abcdef1234567890` \
 --network-interfaces "NetworkCardIndex=**0**,DeviceIndex=**0**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**1**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**2**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**3**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**4**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**5**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**6**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**7**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**8**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**9**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**10**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**11**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**12**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**13**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**14**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**15**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**16**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**17**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**18**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**19**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**20**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**21**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**22**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**23**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**24**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**25**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**26**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**27**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**28**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**29**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**30**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**" \
"NetworkCardIndex=**31**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**`efa or efa-only`**"
...
```

Launch templates

###### To add EFAs to a launch template using the Amazon EC2 console

1. In the **Network settings** section, expand **Advanced
   network configuration**.
2. To add the primary network interface (Network interface 1), choose **Add network interface**
   and then select **Network card index = 0**, **Device index = 0**, and
   **Interface type = EFA with ENA**.
3. To add additional network interfaces, choose **Add network interface**.
   For **Network card index**, select the next unused index, and then select
   **Device index = 1**, and **Interface type = EFA with ENA**
   or **EFA-only**.

###### To add EFAs to a launch template using the [create-launch-template](../../../cli/latest/reference/ec2/create-launch-template.md "../../../cli/latest/reference/ec2/create-launch-template.md")

command

For `NetworkInterfaces`, specify the required number of network interfaces.
For the primary network interface, specify `NetworkCardIndex=0`, `DeviceIndex=0`,
and `InterfaceType=efa`. For any additional network interfaces, for
`NetworkCardIndex` specify the next unused index, `DeviceIndex=1`,
and `InterfaceType=efa` or `efa-only`.

The following snippet shows an example with 3 network interfaces out of the possible 32 network
interfaces.

```
"NetworkInterfaces":[
{
  "NetworkCardIndex":**0**,
  "DeviceIndex":**0**,
  "InterfaceType": "**efa**",
  "AssociatePublicIpAddress":false,
  "Groups":[
    "`security_group_id`"
  ],
  "DeleteOnTermination":true
},
{
  "NetworkCardIndex": **1**,
  "DeviceIndex": **1**,
  "InterfaceType": "**`efa or efa-only`**",
  "AssociatePublicIpAddress":false,
  "Groups":[
    "`security_group_id`"
  ],
  "DeleteOnTermination":true
},
{
  "NetworkCardIndex": **2**,
  "DeviceIndex": **1**,
  "InterfaceType": "**`efa or efa-only`**",
  "AssociatePublicIpAddress":false,
  "Groups":[
    "`security_group_id`"
  ],
  "DeleteOnTermination":true
},
{
  "NetworkCardIndex": **3**,
  "DeviceIndex": **1**,
  "InterfaceType": "**`efa or efa-only`**",
  "AssociatePublicIpAddress":false,
  "Groups":[
    "`security_group_id`"
  ],
  "DeleteOnTermination":true
}
...

```

## EFA configuration for a P5 and P5e instances

`p5.48xlarge` and `p5e.48xlarge` instances support 32 network
cards and have a total network bandwidth capacity of 3,200 Gbps, of which up to 800
Gbps can be utilized for IP network traffic. Because EFA and IP network traffic share
the same underlying resources, bandwidth used by one will reduce the bandwidth that
is available to the other. This means that you can distribute the network bandwidth
between EFA traffic and IP traffic in any combination, as long as the total bandwidth
does not exceed 3,200 Gbps and IP bandwidth does not exceed 800 Gbps. For example, if
you use 400 Gbps for IP bandwidth, you can achieve up to 2,800 Gbps of EFA bandwidth
at the same time.

###### Use case 1: Save IP addresses and avoid potential Linux IP issues

This configuration provides up to 3200 Gbps of EFA networking bandwidth
and up to 100 Gbps of IP networking bandwidth with one private IP address.
This configuration also helps to avoid potential Linux IP issues, such as
disallowed auto-assignment of public IP addresses and IP routing challenges
(hostname to IP address mapping issues and source IP address mismatches),
that can arise if an instance has multiple network interfaces.

- For the primary network interface (network card index 0, device index 0),
  use an EFA (EFA with ENA) network interface.
- For the remaining network interfaces (network card indexes 1-31, device
  index 1), use EFA-only network interfaces.

###### Use case 2: Maximum EFA and IP network bandwidth

This configuration provides up to 3200 Gbps of EFA networking bandwidth and up to
800 Gbps of IP networking bandwidth with 8 private IP address. You can't auto-assign
public IP addresses with this configuration. However, you can attach an Elastic IP
address to the primary network interface (network card index 0, device index 0) after
launch for internet connectivity.

- For the primary network interface (network card index 0, device index 0),
  use an EFA (EFA with ENA) network interface.
- For the remaining interfaces, do the following:
  - Specify EFA-only network interfaces on network card indexes 1, 2, and 3,
    and use device index 1.
  - Specify one EFA (EFA with ENA) network interface and three EFA-only network
    interfaces **in each** of the following network
    card index subsets, and use device index 1 for all of them:
    - [4,5,6,7]
    - [8,9,10,11]
    - [12,13,14,15]
    - [16,17,18,19]
    - [20,21,22,23]
    - [24,25,26,27]
    - [28,29,30,31]

The following example illustrates this configuration:

```
$ aws --region $REGION ec2 run-instances \
 --instance-type p5.48xlarge \
 --count 1 \
 --key-name key_pair_name \
 --image-id ami_id \
 --network-interfaces "NetworkCardIndex=**0**,DeviceIndex=**0**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**1**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**2**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**3**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**4**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**5**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**6**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**7**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**8**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**9**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**10**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**11**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**12**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**13**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**14**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**15**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**16**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**17**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**18**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**19**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**20**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**21**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**22**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**23**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**24**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**25**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**26**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**27**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**28**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa**" \
"NetworkCardIndex=**29**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**30**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**" \
"NetworkCardIndex=**31**,DeviceIndex=**1**,Groups=`security_group_id`,SubnetId=`subnet_id`,InterfaceType=**efa-only**"
...
```

## EFA configuration for a P6-B200 instances

P6-B200 instances have a total network bandwidth capacity of 3,200 Gbps, of which up to 1600 Gbps can be
utilized for ENA. They have 8 GPUs and 8 network cards, where each network card supports up to 400 Gbps EFA
bandwidth and 200 Gbps ENA bandwidth. Since EFA and ENA traffic share the same underlying resources, bandwidth
used by one will reduce the bandwidth that is available to the other.

###### Use case 1: Save IP addresses

This configuration consumes at least one private IP address per instance and supports up to 3200 Gbps
of EFA bandwidth and 200 Gbps of ENA bandwidth.

- For the primary network interface (network card index 0, device index 0), use an EFA (EFA with ENA)
  network interface.
- For the remaining 7 network cards (network card indexes 1-7, device index 1), use EFA-only network
  interfaces.

###### Use case 2: Maximum EFA and ENA bandwidth

This configuration consumes at least 8 private IP address per instance and supports up to 3200 Gbps
of EFA bandwidth and 1600 Gbps of ENA bandwidth.

- For the primary network interface (network card index 0, device index 0) and the remaining 7 network
  cards (network card indexes 1-7, device index 1), use EFA (EFA with ENA) network interfaces.

## EFA configuration for a P6e-GB200 instances

P6e-GB200 instances can be configured with up to 17 network cards. The following image
shows the physical network interface card (NIC) layout for P6e-GB200 instances, along with
the mapping of network card indexes (NCIs).

![Physical network interface card (NIC) and network card index (NCI) mapping for P6e-GB200 instances.](images/p6e.png)

The primary NCI (index 0) supports up to 100 Gbps of ENA bandwidth. NCIs with the following
indexes support EFA-only network interfaces and 400 Gbps EFA bandwidth: [1, 3, 5, 7, 9, 11,
13, 15]. NCIs with the following indexes support up to 200 Gbps ENA or EFA bandwidth: [2, 4,
6, 8, 10, 12, 14, 16].

The NCIs in the following groups share an underlying physical NIC on the host:

- [1 and 2]
- [3 and 4]
- [5 and 6]
- [7 and 8]
- [9 and 10]
- [11 and 12]
- [13 and 14]
- [15 and 16]

Each physical NIC supports up 400 Gbps of bandwidth. Because the NCIs in these groups
share the same underlying physical NIC, bandwidth used by one will reduce the bandwidth
that is available to the other. For example, if NCI 2 uses 200 Gbps of ENA bandwidth,
NCI 1 can use up to 200 Gbps of EFA bandwidth at the same time.

Each underlying GPU on the host can send traffic directly over the following pairs of
NCIs:

- [1 and 3]
- [5 and 7]
- [9 and 11]
- [13 and 15]

Each GPU supports up to 400 Gbps of EFA bandwidth. Because the network cards in these
groups share the same GPU, bandwidth used by one will reduce the bandwidth that is
available to the other. For example, if NCI 1 uses 200 Gbps of EFA bandwidth, NCI 3 can
use up to 200 Gbps of EFA bandwidth at the same time. Therefore, to achieve maximum EFA
performance, we recommend that you do **one of the following**
to achieve a total of 1,600 Gbps EFA bandwidth:

- Add an EFA-only network interface to only one NCI in each group to achieve 400
  Gbps per network interface (_4 EFA network interfaces x 400 Gbps_).
- Add an EFA-only network interface to each NCI in each group to achieve 200 Gbps
  per network interface (_8 EFA network interfaces x 200 Gbps_).

For example, the following configuration provides up to 1,600 Gbps of EFA bandwidth
using a single EFA-only network interface in each NCI group, and up to 100 Gbps of ENA
networking bandwidth using only the primary NCI (index 0).

- For the primary NCI (network card index 0, device index 0), use an ENA network
  interface.
- Add EFA-only network interfaces to the following:
  - NCI 1, device index 0
  - NCI 5, device index 0
  - NCI 9, device index 0
  - NCI 13, device index 0
