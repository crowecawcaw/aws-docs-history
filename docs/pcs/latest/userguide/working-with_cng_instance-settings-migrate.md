

# Migrating a compute node group from a custom launch template to instance settings in AWS PCS

Existing compute node groups that use a custom launch template continue to work. You don't have to migrate them. To manage a compute node group without a custom launch template, switch it from launch template configuration (`CUSTOM`) to standard configuration (`MANAGED`). In the same update, specify the AMI, security groups, and SSH key pair as instance settings.

**Contents**
+ [Prerequisites](#working-with_cng_instance-settings-migrate_prereq)
+ [Find the settings to move](#working-with_cng_instance-settings-migrate_settings)
+ [Migrate a compute node group](#working-with_cng_instance-settings-migrate_steps)
+ [Migrate a compute node group that you manage with CloudFormation](#working-with_cng_instance-settings-migrate_cfn)

## Prerequisites
<a name="working-with_cng_instance-settings-migrate_prereq"></a>
+ Check that standard configuration supports the settings that you need. If the compute node group uses an On-Demand Capacity Reservation (ODCR), an interruptible ODCR (I-ODCR), or a Capacity Block, keep the custom launch template. Also keep it if the compute node group needs other settings that only a launch template provides.
+ With standard configuration, compute nodes require Instance Metadata Service Version 2 (IMDSv2). If your AMI, scripts, or applications use IMDSv1, update them to use IMDSv2 before you migrate. For more information, see [Use the Instance Metadata Service to access instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.
+ When you change the configuration type, AWS PCS replaces the compute nodes in the compute node group after their running jobs finish. For more information, see [Updating a compute node group in AWS PCS](working-with_cng_update.md).
+ If you specify an SSH key pair, the IAM identity that updates the compute node group needs permission for `ec2:DescribeKeyPairs`. For more information, see [Minimum permissions to use API actions](security-min-permissions.md#security-min-permissions_api).

## Find the settings to move
<a name="working-with_cng_instance-settings-migrate_settings"></a>

Get the contents of the custom launch template version that the compute node group uses. The AWS PCS console and the `GetComputeNodeGroup` operation don't show values from the launch template.

In the commands on this page, make these replacements:
+ Replace {{region}} with the ID of the AWS Region where your cluster is, such as `us-east-1`.
+ Replace {{my-cluster}} with the name or `clusterId` of your cluster.
+ Replace {{my-node-group}} with the name or `computeNodeGroupId` of your compute node group.
+ Replace {{ami-ExampleID1}}, {{sg-ExampleID1}}, {{sg-ExampleID2}}, and {{my-key-pair}} with the values that you find in the launch template.

**To get the launch template settings (AWS CLI)**

1. Get the details of the compute node group. Note the values of `amiId`, `securityGroupIds`, `sshKeyName`, and `customLaunchTemplate` in the output.

   ```
   aws pcs get-compute-node-group --region {{region}} \
       --cluster-identifier {{my-cluster}} \
       --compute-node-group-identifier {{my-node-group}}
   ```

1. Get the contents of the launch template version. Replace {{lt-ExampleID1}} and {{launch-template-version}} with the `id` and `version` values in `customLaunchTemplate` from the previous step.

   ```
   aws ec2 describe-launch-template-versions --region {{region}} \
       --launch-template-id {{lt-ExampleID1}} \
       --versions {{launch-template-version}} \
       --query 'LaunchTemplateVersions[0].LaunchTemplateData'
   ```

Decide how to handle each setting in the launch template data:
+ `ImageId`, `SecurityGroupIds`, and `KeyName` – Use these values for the AMI, security groups, and SSH key pair, unless the compute node group already has instance settings for them. Standard configuration requires an AMI and at least one security group.
+ `NetworkInterfaces` – If the launch template defines one network interface only to set its security groups (`Groups`), specify those security groups on the compute node group. If it defines more than one network interface, or any Elastic Fabric Adapter (EFA) network interfaces, keep the custom launch template.
+ `UserData` – Move the scripts to node lifecycle actions. For more information, see [Node lifecycle actions](cng-node-lifecycle-actions.md).
+ `MetadataOptions` – With standard configuration, compute nodes require IMDSv2. If the launch template allows IMDSv1, update your AMI, scripts, and applications to use IMDSv2 before you migrate. For more information, see [Prerequisites](#working-with_cng_instance-settings-migrate_prereq).
+ Other settings, such as `BlockDeviceMappings`, `Placement`, and `CapacityReservationSpecification` – Standard configuration doesn't support these settings. If you need them, keep the custom launch template.

## Migrate a compute node group
<a name="working-with_cng_instance-settings-migrate_steps"></a>

------
#### [ AWS Management Console ]

**To migrate a compute node group (console)**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Choose the cluster that has the compute node group.

1. Choose **Compute node groups**, choose the compute node group, and then choose **Edit**.

1. Choose **Standard configuration**.

1. Enter or choose the AMI and security groups, and optionally the SSH key pair, that you found in the launch template.

1. Choose **Update**. The **Status** field shows `Updating` while AWS PCS applies the changes. Updates can take several minutes.

------
#### [ AWS CLI ]

**To migrate a compute node group (AWS CLI)**

1. Update the compute node group. Specify the instance settings and `--launch-template-mode MANAGED` in the same request. Don't specify `--custom-launch-template`.

   ```
   aws pcs update-compute-node-group --region {{region}} \
       --cluster-identifier {{my-cluster}} \
       --compute-node-group-identifier {{my-node-group}} \
       --ami-id {{ami-ExampleID1}} \
       --security-group-ids {{sg-ExampleID1}} {{sg-ExampleID2}} \
       --ssh-key-name {{my-key-pair}} \
       --launch-template-mode MANAGED
   ```

1. Run the `get-compute-node-group` command from [Find the settings to move](#working-with_cng_instance-settings-migrate_settings) again. Confirm that `launchTemplateMode` is `MANAGED` and that the instance settings have the values that you specified.

------

Removing the custom launch template from the compute node group doesn't delete the launch template from your AWS account. If no other compute node group uses the launch template, you can delete it. For more information, see [Delete a launch template or a launch template version](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-launch-template.html) in the *Amazon EC2 User Guide*.

## Migrate a compute node group that you manage with CloudFormation
<a name="working-with_cng_instance-settings-migrate_cfn"></a>

In your template, add the `AmiId`, `SecurityGroupIds`, and `SshKeyName` properties to the `AWS::PCS::ComputeNodeGroup` resource. Set `LaunchTemplateMode` to `MANAGED`, and remove the `CustomLaunchTemplate` property. Then update the stack. For more information, see [AWS::PCS::ComputeNodeGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcs-computenodegroup.html) in the *CloudFormation Template Reference*.