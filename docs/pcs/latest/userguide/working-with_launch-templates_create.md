# Create a basic launch template

You can create a launch template using the AWS Management Console or the AWS CLI.

AWS Management Console

###### To create a launch template

1. Open the [Amazon EC2
   console](https://console.aws.amazon.com/ec2/home "https://console.aws.amazon.com/ec2/home") and select **Launch templates**.
2. Choose **Create launch template**.
3. Under **Launch template name and description** enter a unique,
   distinctive name for **Launch template name**
4. Under Key pair (login) at Key pair name, select the SSH key pair that will be used
   to log into EC2 instances managed by AWS PCS. This is optional, but recommended.
5. Under **Network settings**, then **Firewall (security
   groups)**, choose security groups to attach to the network interface. All
   security groups in the launch template must be from your AWS PCS cluster VPC. At
   minimum, choose:
   - A security group that allows communication with the AWS PCS cluster
   - A security group that allows communication between EC2 instances launched by
     AWS PCS
   - (Optional) A security group that allows inbound SSH access to interactive
     instances
   - (Optional) A security group that allows compute nodes to make outgoing
     connections to the Internet
   - (Optional) Security group(s) that allow access to networked resources such as
     shared file systems or a database server.

6. Your new launch template ID will be accessible in the Amazon EC2 console under
   **Launch templates**. The launch template ID will have the form
   `lt-0123456789abcdef01`.

###### Recommended next step

- Use the new launch template to create or update an AWS PCS compute node
  group.

AWS CLI

###### To create a launch template

Create your launch template with the command that follows.

- Before running the command, make the following replacements:
  1.  Replace `region-code` with the AWS Region where you
      are working with AWS PCS
  2.  Replace `my-launch-template-name` with a name for
      your template. It must be unique to the AWS account and AWS Region you are
      using.
  3.  Replace `my-ssh-key-name` with name of your preferred
      SSH key.
  4.  Replace `sg-ExampleID1` and
      `sg-ExampleID2` with security group IDs that allow
      communication between your EC2 instances and the scheduler and communication
      between EC2 instances. If you only have one security group that enables all this
      traffic, you can remove `sg-ExampleID2` and its preceding comma
      character. You can also add more security group IDs. All security groups you
      include in the launch template must be from your AWS PCS cluster VPC.

```
aws ec2 create-launch-template --region `region-code` \
    --launch-template-name `my-template-name` \
    --launch-template-data '{"KeyName":"my-ssh-key-name","SecurityGroupIds": ["`sg-ExampleID1`","`sg-ExampleID2`"]}'
```

The AWS CLI will output text resembling the following. The launch template ID is found
in `LaunchTemplateId`.

```
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

###### Recommended next step

- Use the new launch template to create or update an AWS PCS compute node
  group.
