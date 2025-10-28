# Design Guidance

## Cross-Region

When deploying Elastic Disaster Recovery as a cross-Region approach, you will be protecting applications that are hosted in your primary Region by replicating data to a secondary Region that would also be used for recovery during a drill or disaster. When used for a drill, there will be no impact to the resources in your primary Region. You will continue to serve all users with your production resources with no changes.

However, when failing over during an actual disaster, your production resources will be active in the recovery Region, and you will have to adjust your network path through routing and DNS to redirect all requests to this new recovery Region. During this time, all new writes
or changes to the data will occur in the recovery Region.

Once the disaster has been remediated, you may choose to failback to the primary Region. In order to support this failback operation, it is required that the Elastic Disaster Recovery service be initialized in the primary Region. We recommend that the primary Region be initialized for this operation when you are in the processes of setting up and initializing Elastic Disaster Recovery service in the recovery Region. This is so there is no added delay to the failback process. In the situation where you choose to maintain operations in the recovery Region, we still recommend that you identify a new Region that would be used to replicate data and protect this recovery region from any possible failures.

## Security

Security needs to be a high priority, especially when it comes to your disaster recovery approach. Elastic Disaster Recovery has several options built directly into the service, however it does not provide a full security solution, and you should work with your security teams to validate your security posture.

## Encryption In Transit

All data replicated by Elastic Disaster Recovery is encrypted in transit using [TLS 1.2 or later](../../../drs/latest/userguide/infrastructure-security.md "../../../drs/latest/userguide/infrastructure-security.md").

### Encryption at Rest

When AWS Elastic Disaster Recovery replicates data to the target AWS Region, it creates Amazon Elastic Block Store(EBS) volumes in a staging area. These volumes are automatically encrypted using an AWS Key Management Service (AWS KMS) encryption key that the service creates in your AWS account by default, providing data protection at rest. You can also choose an existing [Customer Managed Key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") (CMK) or create one for this purpose if needed. The chosen key must be selected in the EBS encryption section of the replication settings for Elastic Disaster Recovery to use it. EBS volumes that are launched during a Drill or Recovery will be encrypted using the same key, unless otherwise specified in the EC2 Launch Template.

If you have specific compliance requirements, you can also use [Customer Managed Keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") instead of the default keys created by Elastic Disaster Recovery to handle the encryption of the staging volumes, as well as the volumes of Drill or Recovery instances.

### Separate DR account

A best practice for Elastic Disaster Recovery is to use
[separate AWS accounts](../../../drs/latest/userguide/multi-account.md "../../../drs/latest/userguide/multi-account.md") for the Elastic Disaster Recovery staging network (VPC and subnet) and recovery network. Using a separate AWS account specifically for your disaster recovery solution allows for better segmentation and separation of your critical replicated data.

### Networking

**Network Connectivity**

Elastic Disaster Recovery can utilize multiple networking options when supporting a cross-Region use case. These options can include VPC peering, Transit Gateway, and Internet routing. Of these options, we only recommend that you consider VPC peering or Transit Gateway, as both of these networking solutions can support connecting VPCs together while providing access to services across Regions with better performance and greater security. Of these options, we recommend VPC peering as a simpler and low-cost way to connect your primary Region to the recovery Region while allowing replication traffic to travel between the source server and staging environment.

#### Network bandwidth

AWS Elastic Disaster Recovery will utilize as much of the network as possible when replicating the data from your source environment. Due to this, you will want to ensure you have enough bandwidth to support your source change rate (ensuring you can maintain Continuous Data
Protection). You will want to monitor your network to ensure there is no congestion being caused by the replication process. If you need to throttle the Elastic Disaster Recovery service, you can do so at the service or machine level. In order to calculate the bandwidth required
for your particular workloads, refer to Elastic Disaster Recovery
[Calculating Bandwidth](../../../drs/latest/userguide/Troubleshooting-Communication-Errors.md#Calculating-Bandwidth "../../../drs/latest/userguide/Troubleshooting-Communication-Errors.md#Calculating-Bandwidth").
