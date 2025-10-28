# Editing the default EC2

launch template

To edit the default EC2 launch template, follow these steps:

1. Select **Default launch** from the
   left-hand navigation menu (under **Settings**).
2. select **Edit** in the **Default EC2 launch template** section.
3. Change the settings according to your preferences.
4. select **Save**.

## Amazon EC2 launch template

parameters

AWS Elastic Disaster Recovery (AWS DRS) Amazon EC2 launch settings are divided into basic and
advanced settings.

The basic settings include:

- **Subnet –** When you specify a
  subnet, this field defines where the instance is launched. When
  selecting a subnet, only the default network interface is updated.
  If you do not include a subnet, the launched instance uses the
  Region’s default subnet.
- **Security groups –** The selected
  security groups to assign to the instance, applied to the subnet
  selected for the default network interface. If no security group is
  selected, there is no default value and no group is used. Security
  groups can only be selected if a subnet is included.
- **Instance type –** The default
  instance type to use when launching. If instance type right-sizing
  is active, the system disregards this setting. If no instance type
  is included, a default value is used. You can either select an
  instance type, or you can specify instance attributes and let Amazon
  EC2 identify the instance types with those attributes.
- **EBS volume type –** Applies to all
  volumes for which this type is relevant. If an unmatching type
  exists, the default type (GP3) is used instead. Some volume types
  require setting additional values such as IOPS or throughput.

**Instance type attributes:**

- **Number of vCPUs:** Enter the minimum
  and maximum number of vCPUs for your compute requirements. To
  indicate no limits, mark the no minimum or no maximum checkboxes.
- **Amount of memory (MiB):** Enter the
  minimum and maximum amount of memory, in MiB, for your compute
  requirements. To indicate no limits, mark the no minimum or no
  maximum checkboxes.
- Expand **Optional instance type
  attributes** and choose **Add
  attribute** to express your compute requirements in
  more detail. For information about each attribute, see [InstanceRequirementsRequest](../../../AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.md "../../../AWSEC2/latest/APIReference/API_InstanceRequirementsRequest.md") in the Amazon EC2 API
  Reference.
- **Preview matching instance types:**
  You can preview the instance types that match the specified
  attributes. To exclude instance types, you can select the instance
  types you want to exclude from the previewed list of instance types,
  but only if you did not allow list instance types, as you can either
  exclude or allowlist instance types but not both.

See more about these attributes here: [How attribute-based instance type selection works](../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-how-it-works "../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-how-it-works"). EC2 uses
fleets to launch your instances, and applies price protection to ensure the
fleet does not pick expensive instance types for you. We use the default
protection settings, so we protect against selecting instance types that are
20% more expensive than the lowest cost instance type. To learn more about
price protection using fleets, visit: [Price protection](../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-price-protection "../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md#ec2fleet-abs-price-protection").

To learn more about using instance type attributes in DRS, visit [Flexible
Instance Types](flexible-instance-types.md "flexible-instance-types.md")

Advanced settings include additional parameters that add specific features
to the EC2 template. If you choose not to include these parameters in the
template, the specific capabilities are be added.

The advanced settings include:

- **IAM instance profile –** Attach a
  specific profile to the instance that will be launched. Make sure
  the instance profile has the
  AWSElasticDisasterRecoveryRecoveryInstancePolicy IAM policy attached
  in addition to any other policy.
- **Auto assign public IP –**
  Automatically assign a public IP to the launched instance.
- **Termination protection –** Protect
  the launched instance from accidental termination using the EC2
  console.
- **Tenancy –** Set tenancy information,
  such as dedicated host needed in conjunction with setting BYOL for
  Windows servers and Windows Home.
- **Capacity reservation –** Apply
  reservation consideration to the launched instances.
- **Key pair –** Associate a key pair
  with launched instances that are based on EC2 instances.

###### Note

AWS DRS only supports major EC2 template parameters. If you want to
change values that are not supported by this feature, you can still do
so by editing the EC2 launch template via the Amazon EC2 console:

- Create a new EC2 template version with the required
  changes.
- Mark it as default.

###### Important

Every time you modify an EC2 launch template on the Amazon EC2 console, a
new version is created. AWS DRS uses the version that is marked as the
default. if you prefer to use the EC2 launch template you just modified,
make sure to mark it as the default. Changes made through the AWS DRS
console are automatically set as the default version.

**EC2 launch template tags –** In addition to
the basic and advanced settings, you can also add up to 50 tags. These are
transferred to EC2 launch template created by AWS Elastic Disaster Recovery
(AWS DRS) service.

Learn more about EC2 launch template settings and configuration options in
[this EC2 article](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md").

## Amazon EC2 template

considerations

1. **Revert to previous version –** The
   right-sizing mechanism can fix issues such as an incorrect instance
   type, but other issues may still occur. If you encounter any issues
   with the launch template, you can quickly address them by choosing
   the original default launch template that was created by AWS DRS
   when the agent was installed. Alternatively, you can edit the
   relevant fields from the AWS DRS console.
2. **IOPS –** If needed, set the number
   of I/O operations per second that the volume can support via the
   Amazon EC2 console. You can select any number as long as it matches the
   Amazon EBS guidelines.
   - Provisioned IOPS SSD (io1): 50 IOPS per GiB of storage
   - Provisioned IOPS SSD (io2): 500 IOPS per GiB of storage
   - General Purpose SSD (gp3): 500 IOPS per GiB of storage
