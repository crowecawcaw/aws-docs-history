

# EC2 launch template
<a name="ec2-launch"></a>

AWS Elastic Disaster Recovery (AWS DRS) utilizes EC2 launch templates to launch drill and recovery EC2 instances for each source server. You can edit those templates for each source server directly from the AWS DRS console.

The EC2 launch template is created automatically for each source server that is added to AWS DRS upon the installation of the AWS Replication Agent.

![EC2 launch template info page showing subnet-1, lt-1 template, and right-sizing instance type.](http://docs.aws.amazon.com/drs/latest/userguide/images/ec2launchtemplate.png)


**Topics**
+ [EC2 launch template parameters](#server-ec2-launch-template-parameters)
+ [Key considerations for EC2 launch templates](ec2-key-considerations.md)
+ [Full launch template setting review](ec2-full-setting-review.md)

**Note**  
In most use cases, the EC2 launch template does not need to be edited.
You cannot use the same template for multiple servers.
Many EC2 launch template parameters can be changed, but some may not be used by the AWS DRS launch process and some may interfere with the AWS Elastic Disaster Recovery launch process.
You must set the EC2 launch template you want to use with AWS DRS as the **default** launch template. 

 To edit the EC2 template for a single server, take the following steps:

1. Go to the **Source servers** page.

1. Select a source server to update.

1. Under the **Actions** menu, select **Edit EC2 launch settings** and you will be navigated to the **Edit EC2 launch template** page within the AWS DRS console.

1. Change the settings according to your preferences.

1. Click **Save settings**.

Alternatively:
+ Go to the **Source servers** page.
+ Select a specific source server.
+ Go to the **Launch settings** tab.
+ Click **Edit** in the EC2 launch template section.

## EC2 launch template parameters
<a name="server-ec2-launch-template-parameters"></a>

AWS Elastic Disaster Recovery (AWS DRS) EC2 launch settings are divided into basic and advanced settings.

The basic settings include:
+ **Subnet –** When you specify a subnet, this field defines where the instance will be launched. When selecting a subnet, only the default network interface will be updated. If you do not include a subnet, the launched instance will use the Region’s default subnet located in the default VPC.
**Note**  
If you do not have a default VPC, you must modify the EC2 launch template and explicitly define the subnet in which to launch. Failure to do so will result in errors when launching drill or recovery instances. 
For cross-AZ recovery, ensure that the staging area subnet and the subnets that you configure your recovery instances to launch in are not in the same AZ as your source EC2 instances.
If you have multiple on-premises servers that represent the same resources you can use different AZs for recovery instances to increase resiliency.
+  **Security groups –** The selected security groups to assign to the instance, applied to the subnet selected for the default network interface. If no security group is selected, there is no default value and no group will be used. Security groups can only be selected if a subnet is included.
+  **Instance type –** The default instance type to use when launching. If instance type right-sizing is active, the system will disregard this setting. If no instance type is included, a default value will be used. You can either select an instance type, or you can specify instance attributes and let Amazon EC2 identify the instance types with those attributes.

 **Instance type attributes: ** 
+  **Number of vCPUs:** Enter the minimum and maximum number of vCPUs for your compute requirements. To indicate no limits, mark the no minimum or no maximum checkboxes, or leave them blank. 
+  **Amount of memory (MiB):** Enter the minimum and maximum amount of memory, in MiB, for your compute requirements. To indicate no limits, mark the no minimum or no maximum checkboxes or leave the fields blank. 
+  Expand **Optional instance type attributes**: Select an attribute from the **Choose attribute** dropdown and press **Add attribute** to express your compute requirements in more detail. For information about each attribute, see [InstanceRequirementsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.html) in the *Amazon EC2 API Reference*. 
+  **Preview matching instance types:** You can preview the instance types that match the specified attributes. To exclude instance types, you can select the instance types you want to exclude from the previewed list of instance types, but only if you did not allow instance types, as you can either exclude or allow instance types but not both. 

 See more about these attributes here: [How attribute-based instance type selection works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abs-how-it-works). EC2 uses fleets to launch your instances and applies default price protection settings to avoid selecting expensive instance types. For current price protection defaults, see [Price Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abs-price-protection). 

 To learn more about using instance type attributes in DRS, visit [Flexible Instance Types](https://docs.aws.amazon.com/drs/latest/userguide/flexible-instance-types.html). 

Advanced settings include additional parameters that add specific features to the EC2 template. If you choose not to include these parameters in the template, the specific capabilities will not be added. 

The advanced settings include:
+ **IAM instance profile –** Attach a specific profile to the instance that will be launched. Make sure the instance profile has the AWSElasticDisasterRecoveryRecoveryInstancePolicy IAM policy attached in addition to any other policy.
+ **Auto assign public IP –** Automatically assign a public IP to the launched instance.
+ **Termination protection –** Protect the launched instance from accidental termination using the EC2 console.
+  **Tenancy –** Set tenancy information, such as dedicated host needed in conjunction with setting BYOL for Windows servers and Windows Home.
+ **Capacity reservation –** Apply reservation consideration to the launched instances.
+ **Key pair –** Associate a key pair with launched instances that are based on EC2 instances.

**Note**  
AWS DRS only supports major EC2 template parameters. If you want to change values that are not supported by this feature, you can still do so by editing the EC2 launch template via the Amazon EC2 console:  
Create a new EC2 template version with the required changes.
Mark it as default.

**Important**  
Every time you modify an EC2 launch template on the Amazon EC2 console, a new version is created. AWS DRS uses the version that is marked as the default. If you prefer to use the EC2 launch template you just modified, make sure to mark it as the default. Changes made through the AWS DRS console are automatically set as the default version.

 **Amazon EBS volume initialization rate –** You can set a `VolumeInitializationRate` on Amazon EBS block device mappings in the EC2 launch template to accelerate volume initialization during drill and recovery launches. Set this value directly on the launch template through the Amazon EC2 console or the AWS Command Line Interface (AWS CLI). AWS Elastic Disaster Recovery preserves the rate across its own launch template updates and passes it to volume creation at recovery time. If volume creation fails because of the specified rate, AWS Elastic Disaster Recovery retries without the rate to prevent the rate from blocking recovery.

**Note**  
This feature is available only in AWS Regions and environments that support Amazon EBS volume initialization rate. You are charged per GB based on the full snapshot size and the initialization rate you specified. For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-initialize.html) and [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).

 **EC2 launch template tags –** In addition to the basic and advanced settings, you can also add up to 50 tags. These will be transferred to your drill and recovery instances. Note that these tags may interfere with other tags that have already been added to the source server. Launch template tags always take precedence over tags set in the AWS DRS Console or tags manually added to the server. 

Learn more about EC2 launch template settings and configuration options in [this EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html).