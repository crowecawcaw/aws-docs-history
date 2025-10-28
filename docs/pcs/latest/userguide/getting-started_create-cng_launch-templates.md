# Create launch templates for AWS PCS

When you create a compute node group, you provide an EC2 launch template that AWS PCS uses
to configure EC2 instances it launches. This includes settings such as security groups and scripts
that run when the instance launches.

In this step, one CloudFormation template will be used to create two EC2 launch templates.
One template will be used to create login nodes, and the other will be used to create compute
nodes. The key difference between them is that the login nodes can be configured to allow inbound
SSH access.

## Access the

CloudFormation template

Use the following URL to download the CloudFormation template, then upload the template in
the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home#/stacks/create "https://console.aws.amazon.com/cloudformation/home#/stacks/create") to
create a new CloudFormation stack. For more information, see [Using the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md "../../../AWSCloudFormation/latest/UserGuide/cfn-using-console.md")
in the _AWS CloudFormation User Guide_.

```
https://aws-hpc-recipes.s3.amazonaws.com/main/recipes/pcs/getting_started/assets/pcs-lt-efs-fsxl.yaml
```

## Use the

CloudFormation template to create EC2 launch templates

Use the following procedure to complete the CloudFormation template in the
AWS CloudFormation console

- Under **Provide a stack name**:
  - Under **Stack name**, enter `getstarted-lt`.

- Under **Parameters**:
  - Under **Security**
    - For **VpcSecurityGroupId**, select the security group named
      `default` in your cluster VPC.
    - For **ClusterSecurityGroupId**, select the group named
      `cluster-getstarted-sg`
    - For **SshSecurityGroupId**, select the group named
      `inbound-ssh-getstarted-sg`
    - For **SshKeyName**, select your preferred SSH key pair.

  - Under **File systems**
    - For **EfsFilesystemId**, enter the file system ID from the EFS
      file system you created earlier in the tutorial.
    - For **FSxLustreFilesystemId**, enter the file system ID from the
      FSx for Lustre file system you created earlier in the tutorial.
    - For **FSxLustreFilesystemMountName**, enter the mount name for that
      same FSx for Lustre file system.

- Choose **Next**, then choose **Next** again.
- Choose **Submit**.

Monitor the status of the CloudFormation stack. When it reaches
`CREATE_COMPLETE` the launch template is ready to be used.

###### Note

To see all the resources the CloudFormation template created, open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation"). Choose the
`getstarted-lt` stack and then choose the **Resources** tab.
