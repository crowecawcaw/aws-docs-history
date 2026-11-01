

# EC2 launch template
<a name="ec2-launch"></a>

AWS Transform MGN uses EC2 launch templates to launch test and cutover EC2 instances for each source server.

The EC2 launch template is created automatically for each source server that is added to MGN upon the installation of the AWS Replication Agent. 

MGN selects defaults to provide the best performance while migrating your servers to AWS. We recommend that you review the EC2 launch template to make sure that the settings suit your use case.
+ You can't use the same template for multiple servers.
+ You can edit the launch template only from the Amazon EC2 console.
+ Some EC2 launch template settings aren't used by the MGN launch process, and some might interfere with it.

[Learn more about individual launch template settings.](detailed-considerations.md)

**Important**  
Set the EC2 launch template that you want to use with MGN as the **default** launch template. The template doesn't specify a subnet, so EC2 launches into a subnet in your default VPC. If you deleted your default VPC, specify a subnet in the template, or the launch fails.

The MGN EC2 launch template panel shows a summary of the key template values. To view all the values or to change any of them:

1. Choose **Modify**.

1. When the **About modifying EC2 launch templates** dialog appears, choose **Modify**. 

   This redirects you to **EC2 > Launch templates > Modify template** in a new tab, where you'll be able to make any necessary changes. 

Learn more about EC2 launch template settings and configuration options in [this EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html). 