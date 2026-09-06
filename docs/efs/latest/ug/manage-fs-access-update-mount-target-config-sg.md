

# Changing mount target security groups
<a name="manage-fs-access-update-mount-target-config-sg"></a>

Security groups define inbound and outbound access. When you change security groups associated with a mount target, make sure that you authorize necessary inbound and outbound access. Doing so enables your EC2 instance to communicate with the file system. For more information about security groups, see [Using VPC security groups](network-access.md).

You can add or remove security groups for a file system's mount target by using the AWS Management Console, AWS CLI, or programmatically by using the AWS SDKs.

## Using the console
<a name="mount-target-"></a>

**To modify security groups for mount targets**

Use the following procedure to add or remove mount target security groups for an existing EFS file system.

1. Open the Amazon Elastic File System console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. In the left navigation pane, choose **File systems**, and then select the file system for which you want to manage mount targets.

1. Choose **Network** and then choose **Manage** to display the mount targets for the file system.

1. To remove a security group from a mount target, choose **X** next to the security group ID.

1. To add a security group to a mount target, choose the security from the **Security groups** list. 

1. Choose **Save**.

## Using the AWS CLI
<a name="modify-mount-target-sg-cli"></a>

To modify security groups that are in effect for a mount target, use the `modify-mount-target-security-group` AWS CLI command (the corresponding operation is [ModifyMountTargetSecurityGroups](https://docs.aws.amazon.com/efs/latest/APIReference/API_ModifyMountTargetSecurityGroups.html)) to replace any existing security groups, as shown following.

```
$ aws efs modify-mount-target-security-groups \
--mount-target-id {{mount-target-ID-whose-configuration-to-update}} \
--security-groups  {{security-group-ids-separated-by-space}} \
--region {{aws-region-where-mount-target-exists}} \
--profile adminuser
```

The following is an example with sample data.

```
$ aws efs modify-mount-target-security-groups \
--mount-target-id {{fsmt-5751852e}} \
--security-groups  {{sg-1004395a sg-1114433a}} \
--region {{us-east-2}}
```