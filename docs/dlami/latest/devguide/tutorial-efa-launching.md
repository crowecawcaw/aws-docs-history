# Launching a AWS Deep Learning AMIs Instance With EFA

The latest Base DLAMI is ready to use with EFA and comes with the required drivers, kernel modules,
libfabric, openmpi and the [NCCL OFI plugin](https://github.com/aws/aws-ofi-nccl/tree/aws "https://github.com/aws/aws-ofi-nccl/tree/aws") for GPU instances.

You can find the supported CUDA versions of a Base DLAMI in the [release notes](appendix-ami-release-notes.md#appendix-ami-release-notes-base "appendix-ami-release-notes.md#appendix-ami-release-notes-base").

Note:

- When running a NCCL Application using `mpirun` on EFA, you will have to specify the full path to the EFA supported installation as:

```
/opt/amazon/openmpi/bin/mpirun <command>
```

- To enable your application to use EFA, add `FI_PROVIDER="efa"` to the
  `mpirun` command as shown in [Using EFA on the DLAMI](tutorial-efa-using.md "tutorial-efa-using.md").

###### Topics

- [Prepare an EFA Enabled Security Group](#tutorial-efa-security-group "#tutorial-efa-security-group")
- [Launch Your Instance](#tutorial-efa-launch "#tutorial-efa-launch")
- [Verify EFA Attachment](#tutorial-efa-verify-attachment "#tutorial-efa-verify-attachment")

## Prepare an EFA Enabled Security Group

EFA requires a security group that allows all inbound and outbound traffic to and from
the security group itself. For more information, see the [EFA Documentation](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security").

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Security Groups** and then choose **Create Security
   Group**.
3. In the **Create Security
   Group** window, do the following:
   - For **Security group
     name**, enter a descriptive name for the security group, such as
     `EFA-enabled security group`.
   - (Optional) For **Description**, enter a brief description of the security group.
   - For **VPC**, select the
     VPC into which you intend to launch your EFA-enabled instances.
   - Choose **Create**.

4. Select the security group that you created, and on the
   **Description** tab, copy the **Group ID**.
5. On the **Inbound** and
   **Outbound** tabs, do the following:
   - Choose **Edit**.
   - For **Type**, choose
     **All traffic**.
   - For **Source**, choose
     **Custom**.
   - Paste the security group ID that you copied into the
     field.
   - Choose **Save**.

6. Enable inbound traffic referring to [Authorizing Inbound Traffic for Your Linux Instances](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md"). If you skip this step,
   you won't be able to communicate with your DLAMI instance.

## Launch Your Instance

EFA on the AWS Deep Learning AMIs is currently supported with the following instance types and operating
systems:

- P3dn: Amazon Linux 2, Ubuntu 20.04
- P4d, P4de: Amazon Linux 2, Amazon Linux 2023, Ubuntu 20.04, Ubuntu 22.04
- P5, P5e, P5en: Amazon Linux 2, Amazon Linux 2023, Ubuntu 20.04, Ubuntu 22.04

The following section shows how to launch an EFA enabled DLAMI instance. For more
information on launching an EFA enabled instance, see [Launch EFA-Enabled Instances into a Cluster Placement Group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-instances "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-instances").

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch Instance**.
3. On the **Choose an
   AMI** page, select a supported DLAMI found on the
   [DLAMI Release Notes Page](appendix-ami-release-notes.md "appendix-ami-release-notes.md")
4. On the **Choose an Instance
   Type** page, select one of the following supported instance types and then
   choose **Next: Configure Instance Details.** Refer to
   this link for the list of supported instances: [Get started with EFA and MPI](../../../AWSEC2/latest/UserGuide/efa-start.md "../../../AWSEC2/latest/UserGuide/efa-start.md")
5. On the **Configure Instance
   Details** page, do the following:
   - For **Number of
     instances**, enter the number of EFA-enabled instances that you want to
     launch.
   - For **Network** and
     **Subnet**, select the VPC and subnet into which to
     launch the instances.
   - [Optional] For **Placement
     group**, select **Add instance to placement
     group**. For best performance, launch the instances within a placement
     group.
   - [Optional] For **Placement group
     name**, select **Add to a new placement
     group**, enter a descriptive name for the placement group, and then for
     **Placement group strategy**, select **cluster**.
   - Make sure to enable the **“Elastic Fabric Adapter”** on this page. If this option is disabled,
     change the subnet to one that supports your selected instance type.
   - In the **Network
     Interfaces** section, for device **eth0**,
     choose **New network interface**. You can optionally
     specify a primary IPv4 address and one or more secondary IPv4 addresses. If you're
     launching the instance into a subnet that has an associated IPv6 CIDR block, you can
     optionally specify a primary IPv6 address and one or more secondary IPv6 addresses.
   - Choose **Next: Add
     Storage**.

6. On the **Add Storage**
   page, specify the volumes to attach to the instances in addition to the volumes
   specified by the AMI (such as the root device volume), and then choose **Next: Add Tags**.
7. On the **Add Tags** page,
   specify tags for the instances, such as a user-friendly name, and then choose **Next: Configure Security Group**.
8. On the **Configure Security
   Group** page, for **Assign a security group**,
   select **Select an existing security group**, and then
   select the security group that you created previously**.**
9. Choose **Review and
   Launch**.
10. On the **Review Instance
    Launch** page, review the settings, and then choose **Launch** to choose a key pair and to launch your instances.

## Verify EFA Attachment

### From the Console

After launching the instance, check the instance details in the AWS Console. To do this,
select the instance in the EC2 console and look at the Description Tab in the lower pane on
the page. Find the parameter ‘Network Interfaces: eth0’ and click on eth0 which opens a
pop-up. Make sure that ‘Elastic Fabric Adapter’ is enabled.

If EFA is not enabled, you can fix this by either:

- Terminating the EC2 instance and launching a new one with the same steps. Make sure the EFA is attached.
- Attach EFA to an existing instance.
  1.  In the EC2 Console, go to Network Interfaces.
  2.  Click on Create a Network Interface.
  3.  Select the same subnet that your instance is in.
  4.  Make sure to enable the ‘Elastic Fabric Adapter’ and click on Create.
  5.  Go back to the EC2 Instances Tab and select your instance.
  6.  Go to Actions: Instance State and stop the instance before you attach EFA.
  7.  From Actions, select Networking: Attach Network Interface.
  8.  Select the interface you just created and click on attach.
  9.  Restart your instance.

### From the Instance

The following test script is already present on the DLAMI. Run it to ensure that the
kernel modules are loaded correctly.

```
$ fi_info -p efa
```

Your output should look similar to the following.

```
provider: efa
    fabric: EFA-fe80::e5:56ff:fe34:56a8
    domain: efa_0-rdm
    version: 2.0
    type: FI_EP_RDM
    protocol: FI_PROTO_EFA
provider: efa
    fabric: EFA-fe80::e5:56ff:fe34:56a8
    domain: efa_0-dgrm
    version: 2.0
    type: FI_EP_DGRAM
    protocol: FI_PROTO_EFA
provider: efa;ofi_rxd
    fabric: EFA-fe80::e5:56ff:fe34:56a8
    domain: efa_0-dgrm
    version: 1.0
    type: FI_EP_RDM
    protocol: FI_PROTO_RXD
```

### Verify Security Group Configuration

The following test script is already present on the DLAMI. Run it to ensure that the
security group you created is configured correctly.

```
$ cd /opt/amazon/efa/test/
$ ./efa_test.sh
```

Your output should look similar to the following.

```
Starting server...
Starting client...
bytes   #sent   #ack     total       time     MB/sec    usec/xfer   Mxfers/sec
64      10      =10      1.2k        0.02s      0.06    1123.55       0.00
256     10      =10      5k          0.00s     17.66      14.50       0.07
1k      10      =10      20k         0.00s     67.81      15.10       0.07
4k      10      =10      80k         0.00s    237.45      17.25       0.06
64k     10      =10      1.2m        0.00s    921.10      71.15       0.01
1m      10      =10      20m         0.01s   2122.41     494.05       0.00
```

If it stops responding or does not complete, ensure that your security group has the correct
inbound/outbound rules.
