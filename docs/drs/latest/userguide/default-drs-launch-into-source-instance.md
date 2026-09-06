

# Launch into source instance
<a name="default-drs-launch-into-source-instance"></a>

 This setting is only valid when the replication and recovery are done in-AWS, between 2 AWS regions or availability zones. This default setting applies to newly added source servers. Such servers have their **Launch into instance ID** field in the Launch Settings set to the EC2 instance ID of the source instance, that was the source of the data in the same region or availability zone. See the examples below for more details. 

## Pre-requisites
<a name="launch-into-source-instance-pre-requisites"></a>

 **Start reversed replication** or **Protect recovered instance** fails to create a source server if this setting is active and one of these conditions is not met: 

1. The instance to launch into must have the required tag with key *AWSDRS* and value *AllowLaunchingIntoThisInstance*. 

1. The instance to launch into must have the same operating system platform (Linux or Windows) as that of the recovery instance the **Start reversed replication** or **Protect recovered instance** was called on. 

1. If the instance to launch into is Linux, it must have the BIOS boot mode, and if this is Windows, it must have the same boot mode as that of the recovery instance the **Start reversed replication** or **Protect recovered instance** was called on. 

1. The instance to launch into must have the x86\_64 architecture, HVM virtualization and an EBS root device.

1. **OS licensing** in **Default DRS launch settings** can only be **Bring Your Own License (BYOL)** if the instance’s platform is Linux or if the instance’s **tenancy** is **dedicated host**. 

1. **Transfer server tags** and **Copy private IP** must be deactivated in **Default DRS launch settings**. 

## Cross-region
<a name="launch-into-source-instance-cross-region"></a>

 With this setting active, customers who replicate their EC2 instances between two AWS regions, launch in the second region from an instance in the first region, and call **Start reversed replication** to go back to the first region will have their source servers in the first region automatically set **Launch into instance ID** to the instance ID of the instance in the first region they initially launched from. 

 Using the diagram below as an example, the setting applies to source servers such as Source Server **S1** and automatically sets the **Launch into instance ID** to the instance ID of EC2 instance **EI1** (marked by the dotted green arrow in the diagram). 

This only happens if:

1. **Launch into source instance** was set to be active in the **Default DRS launch settings** on region 1. 

1. EC2 instance **EI1** (on AWS region 1) replicated into region 2 (replication handled through source server **S2** on AWS region 2), and was launched in AWS region 2 (launch handled through source server **S2** on AWS region 2), creating recovery instance **RI2**. 

1.  Source server **S1** was created by calling **Start reversed replication** in region 2 on recovery instance **RI2** (marked by the solid green arrow), replicating the data of EC2 instance **EI2**. 

![DRS replication from EC2 instance in Region 1 to source and recovery servers in Region 2.](http://docs.aws.amazon.com/drs/latest/userguide/images/recover-into-source-instance-cross-regions.png)


## Cross Availability Zone
<a name="launch-into-source-instance-cross-az"></a>

 With this setting active, customers who replicate their EC2 instances into the same region (and if following our recommendation, into a different availability zone within that region), launch in the region (recommended to launch into the other availability zone) from an instance in the first availability zone, and perform **Protect recovered instance** on the source server after this launch, will have the source server automatically set **Launch into instance ID** to the instance ID of the instance in the first availability zone. 

 Using the diagram below as an example, the setting applies to source servers such as Source Server **S** and automatically sets the **Launch into instance ID** to the instance ID of EC2 instance **EI1** (marked by the dotted green arrow in the diagram). 

This only happens if:

1. **Launch into source instance** was set to be active in the **Default DRS launch settings** on this region. 

1. EC2 instance **EI1** (on AWS region 1) replicated into availability zone 2 (replication handled through source server **S**), and was launched in availability zone 2 (launch handled through source server **S**), creating recovery instance **RI**. 

1.  Source server **S** was then updated to protect recovery instance **RI** (marked by the solid green arrow), by calling Protect recovered instance, replicating the data of EC2 instance EI2. 

![DRS replication between source server in Availability Zone 1 and recovery instance in Zone 2.](http://docs.aws.amazon.com/drs/latest/userguide/images/recover-into-source-instance-cross-az.png)
