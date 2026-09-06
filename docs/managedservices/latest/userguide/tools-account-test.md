

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Testing AMS Tools account connectivity and end-to-end setup
<a name="tools-account-test"></a>

1. Start with configuring CloudEndure and installing the CloudEndure agent on a server that will replicate to AMS.

1. Create a project in CloudEndure.

1. Enter the AWS credentials shared when you performed the prerequisites, though secrets manager.

1. In **Replication settings**:

   1. Select both AMS "Sentinel" security groups (Private Only and EgressAll) for the **Choose the Security Groups to apply to the Replication Servers** option.

   1. Define cutover options for the machines (instances). For information, see [Step 5. Cut over](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step5.html)

   1. **Subnet**: Private subnet.

1. **Security Group**:

   1. Select both AMS "Sentinel" security groups (Private Only and EgressAll).

   1. Cutover instances have to communicate to the AMS-managed Active Directory (MAD) and to AWS public endpoints:

      1. **Elastic IP**: None

      1. **Public IP**: no

      1. **IAM role**: customer-mc-ec2-instance-profile

   1. Set tags as per your internal tagging convention.

1. Install the CloudEndure agent on the machine and look for the replication instance to come up in your AMS account in the EC2 console.

The AMS ingestion process:

![Flowchart showing AMS ingestion steps from data center replication through AMI creation.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/Ingestion_Process_v1.png)
