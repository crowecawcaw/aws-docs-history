# Post Deployment Steps

1. Complete the steps required to connect your instance to your corporate directory service, such as Microsoft Active Directory, if needed.
2. Set up any monitoring required for your environment.
3. Set up a CloudWatch alarm and Amazon EC2 automatic recovery to automatically recover your instance from hardware failures. For details, see [Recover Your Instance](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md") in the AWS documentation. You can also refer to the Knowledge Center [video](https://aws.amazon.com/premiumsupport/knowledge-center/automatic-recovery-ec2-cloudwatch/ "https://aws.amazon.com/premiumsupport/knowledge-center/automatic-recovery-ec2-cloudwatch/") for detailed instructions.

###### Note

Automatic recovery is not supported for Amazon EC2 instances running in dedicated hosts. 4. Create an AMI of your newly deployed system to take a full backup of your instance. For details, see [Create an AMI from an Amazon EC2 Instance](../../../toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.md "../../../toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.md") in the AWS documentation. 5. If you have deployed an SAP HANA scale-out cluster, consider adding additional elastic network interfaces and security groups to logically separate network traffic for client, inter-node, and optional SAP HANA System Replication (HSR) communications. For details, see the [SAP HANA on AWS Operations Guide](sap-hana-on-aws-operations.md "sap-hana-on-aws-operations.md").
