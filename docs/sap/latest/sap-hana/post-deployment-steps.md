

# Post Deployment Steps
<a name="post-deployment-steps"></a>

1. Complete the steps required to connect your instance to your corporate directory service, such as Microsoft Active Directory, if needed.

1. Set up any monitoring required for your environment.

1. Set up a CloudWatch alarm and Amazon EC2 automatic recovery to automatically recover your instance from hardware failures. For details, see [Recover Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) in the AWS documentation. You can also refer to the Knowledge Center [video](https://aws.amazon.com/premiumsupport/knowledge-center/automatic-recovery-ec2-cloudwatch/) for detailed instructions.
**Note**  
Automatic recovery is not supported for Amazon EC2 instances running in dedicated hosts.

1. Create an AMI of your newly deployed system to take a full backup of your instance. For details, see [Create an AMI from an Amazon EC2 Instance](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html) in the AWS documentation.

1. If you have deployed an SAP HANA scale-out cluster, consider adding additional elastic network interfaces and security groups to logically separate network traffic for client, inter-node, and optional SAP HANA System Replication (HSR) communications. For details, see the [SAP HANA on AWS Operations Guide](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-operations.html).