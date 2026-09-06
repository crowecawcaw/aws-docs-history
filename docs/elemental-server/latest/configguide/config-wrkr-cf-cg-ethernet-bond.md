

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Bond Ethernet Devices
<a name="config-wrkr-cf-cg-ethernet-bond"></a>

You can bond Ethernet devices to suit your networking requirements. For example, you might set up two Ethernet devices as an active/redundant pair. 

**Topics**
+ [Step A: Create the Bond](config-wrkr-cf-cg-ethernet-bond-create.md)
+ [Step B: Assign the Devices](config-wrkr-cf-cg-ethernet-bond-assign.md)

**Important**  
We recommend that you set up both eth0 and eth1 with static IP addresses. Eth0, eth1 and bond0 should also all on the same subnet.

**Prerequisites**  
Before you begin this process, make sure that you've done the following:
+ [Added to AWS Elemental Server the Ethernet devices](config-wrkr-cf-cg-ethernet-add.md) that you're bonding.