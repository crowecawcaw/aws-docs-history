

# Working with AWS DRS and AWS Outposts
<a name="outposts"></a>

AWS Elastic Disaster Recovery supports AWS Outpost racks. AWS Outposts require specific configurations in the default replication settings, individual source server replication settings, default launch templates and source server launch templates to work. The following sections explain how to use AWS Outpost racks with DRS, how to troubleshoot key AWS Outpost issues, and how to monitor AWS Outposts with DRS. [Learn more about AWS Outposts. ](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) 

**Note**  
AWS Elastic Disaster Recovery does not support AWS Outpost servers.

Considerations when using AWS Outposts:


+ To use an AWS Outpost, you need to have a subnet within the Outpost selected to be used for replication or recovery. If you select an Outpost subnet for replication, a subnet in the same Outpost must be selected for recovery. 
+ Your Outpost must be in direct VPC routing mode. For more information see [Direct VPC routing](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#direct-vpc-routing) in the * AWS Outposts user guide*. 
+ Once a subnet within an AWS Outpost is selected for replication, all replication resources (including replication servers, conversion servers, EBS volumes, and snapshots) will be created and saved within the Outpost. 
+ If a subnet within an AWS Outpost is selected for launch, then the recovery instances, EBS volumes and snapshots used for recovery are created and saved within the Outpost. 
+ Your S3 storage must be locally deployed on the Outpost rack. Remote S3 storage is not supported. 

## Default Replication Settings
<a name="default-replication-settings-outposts"></a>

Selecting an Outpost subnet on the *Settings: default replication* page means that newly added source servers will automatically start replicating to the Outpost. 

Subnets that are within Outposts will have the word "Outpost" appended after the subnet name in the subnet selector drop down.

Once the Subnet is chosen, you will have to select the replication server instance type. Only instance types that are supported by the chosen Outpost will be shown. 

![EBS volume type dropdown menu showing Faster, general purpose SSD (gp2) selected.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-replicationsettings-outposts.png)


Outposts only support GP2 disks. As such, you will not be able to change the default disk type in the replication settings. 

 All Outpost volumes must be encrypted, and so you must select an encryption key when a subnet within an Outpost is selected. You will not be able to select not to encrypt. Ensure that you choose the correct volume encryption key you want to use. You can use the default KMS key for your account, or select a customer managed key (CMK). 

 Other replication settings can be set normally. [ Learn more about default replication settings. ](https://docs.aws.amazon.com/drs/latest/userguide/replication-settings-template.html) 

**Note**  
 When selecting an Outpost subnet in your replication settings, ensure that your launch template specifies a subnet on the same Outpost. Not doing so may result in an error during recovery. 

## Source Server Replication Settings
<a name="source-server-replication-settings"></a>

Use these settings to have a specific source server or multiple source servers replicate into an AWS Outpost by selecting a subnet within an AWS Outpost. 

Subnets that are within Outposts will have the word "Outpost" appended after the subnet name in the subnet selector drop down.

Once the Subnet is chosen, you will have to select the replication server instance type. Only instance types that are supported by the chosen Outpost will be shown. 

![Replication server instance type dropdown showing r5.large selected.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-replicationsettingsmultipleservers-outposts.png)


Outposts only support GP2 disks. As such, you will not be able to change the default disk type in the replication settings. 

 All Outpost volumes must be encrypted and you must select an encryption key when a subnet within an Outpost is selected. You will not be able to select *not to encrypt*. Ensure that you choose the correct volume encryption key you want to use. You can use the default KMS key for your account or select a customer managed key (CMK). 

 Other replication settings can be set normally. [ Learn more about replication settings. ](https://docs.aws.amazon.com/drs/latest/userguide/replication-settings.html) 

**Note**  
You cannot edit the replication settings of multiple source servers if some of the source servers are replicating to Outpost subnets and others are replicating to non-Outpost subnets. 

**Note**  
 When selecting an Outpost subnet in your replication settings, ensure that your launch template specifies a subnet on the same Outpost. Not doing so may result in an error during recovery. 

## Default Launch Template
<a name="default-launch-template"></a>

 Selecting an Outpost subnet in the default launch template means that newly added source servers will launch into the Outpost. You must select the instance type from the list of available instance types on your Outpost. 

**Note**  
 When working with Outposts, if you selected a subnet within an AWS Outpost in the default replication settings, you must also choose a subnet within the same Outpost in the default launch template. Otherwise, newly added source servers will replicate into an Outpost but launch outside of an Outpost which may result in an error. 

**Note**  
 Network replication and recovery does not create a subnet within the Outpost. 

 Outposts only support GP2 disks. As such, you will not be able to change the default disk type per volume in the default launch template. 

![Instance type and EBS volume type fields highlighted in the EC2 launch template settings.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-launchtemplate-default-outposts.png)


## Source Server Launch Templates
<a name="source-server-launch-templates"></a>

 When working with Outposts, if you selected a subnet within an AWS Outpost in the replication settings for any source server, you must also choose a subnet within the same Outpost in the launch template of that source server. You must select the instance type to launch into from the list of available instance types on your Outpost. Not doing so may result in an error during recovery. 

**Note**  
 Network replication and recovery does not create a subnet within the Outpost. 

 Outposts only support GP2 disks. As such, you will not be able to change the default disk type per volume in the default launch template. 

![Instance type dropdown menu expanded showing options such as c5d.4xlarge and r5.large.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-launchtemplatemultipleservers-outposts.png)


**Note**  
 You cannot edit the launch templates of multiple source servers if some of the source servers are configured to launch to Outpost subnets and the others are configured to launch to non-Outpost subnets. 

## Source Server Page
<a name="source-server-pages"></a>

 You can find which of your servers are replicating into an AWS Outpost rack, as these are marked with the value (Outpost) in the **Replicating to** field. The following are search options for source servers replicating to an Outpost: 
+  You can enter the text "*Outpost*" in the search field to only display source servers that are replicating to an AWS Outpost rack.   
![Source servers search field with Outposts entered as the search term.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-sourceservers-keyword-outposts.png)
+  You can enter the text "*\!Outpost*" to only display source servers that are not replicating to an AWS Outpost rack.   
![Source servers search field with exclamation mark Outposts filter text entered.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-sourceservers-keyword-notoutposts.png)
+  You can enter "*Replicating to: Outpost*" in the search field to only display source servers that are replicating to an AWS Outpost rack.   
![Search field with Replicating to : Outposts entered as the filter text.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-sourceservers-replicatingto-field-outposts.png)
+  You can enter "*Replicating to \!: Outpost*" in the search field to only display source servers that are not replicating to an AWS Outpost rack.   
![Search field with text Replicating to !: Outposts in the Source servers interface.](http://docs.aws.amazon.com/drs/latest/userguide/images/drs-sourceservers-replicatingto-field-notoutposts.png)

## Important Outpost Notes
<a name="outpost-notes"></a>

### Outpost Storage
<a name="outpost-storage"></a>

 AWS Outposts have a certain storage capacity. You should actively monitor available storage capacity in your Outpost. **If you run out of storage capacity, you may not be able to use DRS with that Outpost environment.** For example, if S3 runs out of capacity on the Outpost then DRS won’t be able to create any new snapshots, so no new points in time will be created. 

Be aware of EBS storage capacity on the Outpost. **DRS requires storage capacity roughly on a 2:1 ratio (excluding any launched instances on the Outpost).** For example, if you have source volumes amounting to a total of 1 TiB of storage, then DRS will require at least 1 TiB for replication resources, and another 1 TiB for conversion or recovery instance creation. 

### Replication and Launch Subnets
<a name="replicating-launch-subnet"></a>

 When using DRS with Outposts it is imperative that the subnet in replication settings and launch settings are on the same Outpost. If the subnets are not on the same Outpost, it may result in a failure during recovery. 

### Instance Types and Operating Systems (OSs)
<a name="instance-types-and-oss"></a>

**Note**  
 AWS Outposts only support [ Nitro instance types. ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) 
+  **Linux** - RHEL 7.0\+ and CentOS 7.0\+ 
+  **Windows** - Windows Server 2008 R2, Windows Server 2012 R2, Windows Server 2016, and higher. 

### Monitoring
<a name="monitoring-outposts"></a>

 You can monitor Outpost metrics for S3, EC2, and EBS capacity through CloudWatch. You can create a dashboard with these metrics: 


+ EBS Metrics: EBSVolumeTypeCapacityAvailability, EBSVolumeTypeCapacityUtilization 
+ EC2 Metrics: InstanceTypeCapacityUtilization, AvailableInstanceType\_Count 
+  S3 Metrics: OutpostTotalBytes, OutpostFreeBytes 

 [ Learn more about CloudWatch S3 monitoring. ](https://docs.aws.amazon.com/AmazonS3/latest/dev/cloudwatch-monitoring.html) 

 [ Learn more about CloudWatch Metrics for AWS Outposts. ](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) 