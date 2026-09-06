

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# EC2 launch template
<a name="ec2-launch"></a>

AWS Transform MGN uses EC2 launch templates to launch test and cutover EC2 instances for each source server.

The EC2 launch template is created automatically for each source server that is added to MGN upon the installation of the AWS Replication Agent. 

**Note**  
MGN selects defaults to provide the best performance while migrating your servers to AWS. We recommend you review the EC2 launch template to ensure the selected templates are suitable for your use case.
You cannot use the same template for multiple servers.
The Launch template can only be edited from the Amazon EC2 console.
Many EC2 launch template settings can be changed, but some may not be used by the AWS MGN launch process and some may interfere with IT. [Learn more about individual launch template settings.](detailed-considerations.md)

**Important**  
You must set the EC2 launch template you want to use with MGN as the **default** launch template.
The EC2 launch template does not automatically set a specific subnet. As such, EC2 attempts to launch in a subnet within the default VPC. If you have removed your default VPC, EC2 fails to launch any instance for which there is no valid subnet specified. Ensure that you specify a subnet if that is the case, or MGN instance launch fails. 

The MGN EC2 launch template panel shows a summary of the key template values. To view all the values or to change any of them:

1. Choose **Modify**.

1. When the **About modifying EC2 launch templates** dialog appears, choose **Modify**. 

   This redirects you to **EC2 > Launch templates > Modify template** in a new tab, where you'll be able to make any necessary changes. 

Learn more about EC2 launch template settings and configuration options in [this EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html). 