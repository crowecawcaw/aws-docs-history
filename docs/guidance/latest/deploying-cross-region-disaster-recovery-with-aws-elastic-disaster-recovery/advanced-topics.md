# Advanced topics

## Recovery Plans: AWS Step Functions + Elastic Disaster Recovery API + AWS Lambda

When performing a disaster recovery at scale, there are often servers that have dependencies on other servers in the environment. For example, application servers that connect to a database on boot or servers that require authentication and need to connect to a domain controller on boot to start services. With AWS Lambda, AWS Step Functions, and Elastic Disaster Recovery API you can sequence your disaster recovery launch.

You can sequence your disaster recovery launch to work based on a single API call to execute the state machine. On this architecture, Lambda functions are used to call on the Elastic Disaster Recovery API and launch the recovery instances. Tagged servers being protected by Elastic Disaster Recovery are used by Step Functions to trigger the launch sequence.

Step Functions is a serverless orchestration service that lets you combine AWS Lambda functions and other AWS services to build business-critical applications. Through the graphical Step Functions console, you see your application’s workflow as a series of event-driven
steps.

### Network Replication

The network replication feature in AWS Elastic Disaster Recovery automatically tracks and replicates changes to your network configurations, such as security groups, network ACLs, and routing tables, between your source and recovery environments. This helps prevent configuration mismatches during recovery, ensuring your recovery
instances are launched with the correct network settings.

For example, if you update a security group to allow additional access, the network replication feature will automatically apply that change to the corresponding security group in your recovery environment. This maintains consistency between your source and recovery environments, enhancing security and reducing the risk of issues during failover. Beyond security groups, the feature also replicates changes to other network resources, like network ACLs and routing tables. By automating these updates, AWS Elastic Disaster Recovery helps you maintain compliance and avoid the need to manually configure individual launch templates for your recovery instances. Steps to implement the
replication of your source network can be found in the [Adding source networks to Elastic Disaster Recovery](../../../drs/latest/userguide/adding-source-network-page.md "../../../drs/latest/userguide/adding-source-network-page.md") part of the user guide.

### Post Launch Validation Automation

[Post-launch Actions](../../../drs/latest/userguide/post-launch-action-settings-overview.md "../../../drs/latest/userguide/post-launch-action-settings-overview.md") in Elastic Disaster Recovery allow you to automate actions after a Drill or Recovery instance is launched. These settings are based on the Default post-launch actions. Available post-launch actions include:

- [Process status validation](../../../drs/latest/userguide/predefined-post-launch-actions-default.md#process-status-validation "../../../drs/latest/userguide/predefined-post-launch-actions-default.md#process-status-validation"): Helps ensure critical processes (such as database and application services) are in a running state after the instance is launched. You can specify a list of processes to verify; you can also specify how long the system should wait before testing.
- [EC2 connectivity checks](../../../drs/latest/userguide/post-launch-action-settings-overview.md#ec2-connectivity-checks "../../../drs/latest/userguide/post-launch-action-settings-overview.md#ec2-connectivity-checks"): Conducts network connectivity checks to a predefined list of ports and hosts to ensure the instance can communicate as expected.
- [Volume integrity validation:](../../../drs/latest/userguide/predefined-post-launch-actions-default.md#volume-integrity-validation "../../../drs/latest/userguide/predefined-post-launch-actions-default.md#volume-integrity-validation") Helps ensure the launched EBS volumes are the same size as the source (rounded up), properly mounted on the EC2 instance, and accessible.

You can also run any available SSM document, including public, custom, or shared documents. To create, edit, or delete custom actions, make sure post-launch actions are activated for the source server. Custom actions are automatically added to new source servers.

### Network Design using VPC Peering

If you want your disaster recovery setup to operate within a private and secure network, VPC peering is an excellent option. VPC peering enables secure, high-bandwidth, low-latency communication between VPCs in different AWS Regions without traversing the public internet. This design ensures that data replication for AWS Elastic Disaster Recovery is efficient and secure. Using VPC peering enhances disaster recovery capabilities, maintains compliance, and provides seamless failover and failback operations, ensuring robust protection for EC2 instances across Regions.

To set up VPC peering for your VPCs, visit the
[AWS VPC Peering Guide](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md").

For more insights, refer to these blogs:

1. [Cross-Region AWS Elastic Disaster Recovery agent installation in a secured network](https://aws.amazon.com/blogs/storage/cross-region-aws-elastic-disaster-recovery-agent-installation-in-a-secured-network/ "https://aws.amazon.com/blogs/storage/cross-region-aws-elastic-disaster-recovery-agent-installation-in-a-secured-network/")
2. [Private cross-Region disaster recovery with AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/storage/private-cross-region-disaster-recovery-with-aws-elastic-disaster-recovery/ "https://aws.amazon.com/blogs/storage/private-cross-region-disaster-recovery-with-aws-elastic-disaster-recovery/")

### Network Design using Transit Gateway

For a scalable and centralized network design, AWS Transit Gateway offers a powerful solution. Transit Gateway enables you to connect multiple VPCs across different AWS Regions through a single gateway, streamlining your network architecture.

By using Transit Gateway, your disaster recovery setup benefits from a simplified, hub-and-spoke topology that reduces complexity and enhances security. This design ensures that data replication for AWS Elastic Disaster Recovery is efficient and secure, with the added flexibility to manage and scale your network easily. Using Transit Gateway also provides seamless connectivity and failover capabilities across multiple AWS accounts and Regions, delivering a robust disaster recovery
protection for your critical workloads.

To learn more about setting up and configuring Transit Gateway, visit the [AWS Transit Gateway Guide](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md").
