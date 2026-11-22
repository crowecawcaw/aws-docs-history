

# Create a basic launch template

You need a custom launch template only if a compute node group needs Amazon EC2 settings that aren't available as instance settings, such as network interfaces or capacity reservations. If you need only an AMI, security groups, and an SSH key pair, use standard configuration instead. For more information, see [Creating a compute node group in AWS PCS](working-with_cng_create.md).

The procedures in this topic create a launch template that specifies an SSH key pair and security groups. You can add other settings to it. You can create a launch template by using the AWS Management Console or the AWS CLI.

------
#### [ AWS Management Console ]

**To create a launch template (console)**

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/home). In the navigation pane, choose **Launch templates**.

1. Choose **Create launch template**.

1. Under **Launch template name and description**, for **Launch template name**, enter a unique name.

1. (Optional) Under **Key pair (login)**, for **Key pair name**, choose the SSH key pair to use to log in to compute nodes. We recommend that you specify a key pair. You can also specify the key pair on the compute node group. If you do, AWS PCS uses that key pair instead of the one in the launch template.

1. Under **Network settings**, for **Firewall (security groups)**, choose security groups to attach to the network interface. All security groups in the launch template must be in your cluster VPC. At minimum, choose security groups that allow the following traffic:
   + Communication between compute nodes and the AWS PCS cluster
   + Communication between compute nodes
   + (Optional) Inbound SSH access to interactive compute nodes, such as login nodes
   + (Optional) Outgoing connections from compute nodes to the internet
   + (Optional) Access to networked resources such as shared file systems or a database server

   For more information, see [Security group requirements and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements). You can also specify security groups on the compute node group. If you do, AWS PCS uses only those security groups instead of the ones in the launch template. It doesn't add the security groups in the launch template.

1. Choose **Create launch template**. The new launch template appears in the Amazon EC2 console under **Launch templates**. Its ID has the form `lt-0123456789abcdef01`.

**Recommended next step**
+ Use the new launch template to create or update a compute node group with launch template configuration. For more information, see [Creating a compute node group in AWS PCS](working-with_cng_create.md) and [Updating a compute node group in AWS PCS](working-with_cng_update.md).

------
#### [ AWS CLI ]

**To create a launch template (AWS CLI)**
+ Create your launch template with the command that follows. Before you run the command, make the following replacements:

  1. Replace {{region}} with the ID of the AWS Region where your cluster is, such as `us-east-1`.

  1. Replace {{my-launch-template-name}} with a name for your launch template. It must be unique in your AWS account and AWS Region.

  1. Replace {{my-key-pair}} with the name of an Amazon EC2 key pair for SSH connections to compute nodes. To omit a key pair, remove `"KeyName":"{{my-key-pair}}",` from the command.

  1. Replace {{sg-ExampleID1}} and {{sg-ExampleID2}} with security group IDs that allow communication between compute nodes and the cluster, and between compute nodes. If one security group allows all this traffic, remove `sg-ExampleID2` and the comma before it. You can also add more security group IDs. All security groups in the launch template must be in your cluster VPC.

  ```
  aws ec2 create-launch-template --region {{region}} \
      --launch-template-name {{my-launch-template-name}} \
      --launch-template-data '{"KeyName":"{{my-key-pair}}","SecurityGroupIds": ["{{sg-ExampleID1}}","{{sg-ExampleID2}}"]}'
  ```

The AWS CLI output resembles the following. The launch template ID is in `LaunchTemplateId`.

```json
{
    "LaunchTemplate": {
        "LatestVersionNumber": 1,
        "LaunchTemplateId": "lt-0123456789abcdef01",
        "LaunchTemplateName": "my-launch-template-name",
        "DefaultVersionNumber": 1,
        "CreatedBy": "arn:aws:iam::123456789012:user/Bob",
        "CreateTime": "2019-04-30T18:16:06.000Z"
    }
}
```

**Recommended next step**
+ Use the new launch template to create or update a compute node group with launch template configuration. For more information, see [Creating a compute node group in AWS PCS](working-with_cng_create.md) and [Updating a compute node group in AWS PCS](working-with_cng_update.md).

------