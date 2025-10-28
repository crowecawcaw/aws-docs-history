# Failback with AWS Elastic Disaster Recovery

## Prerequisites

1. To ensure operational continuity,
   [initialize the AWS DRS](../../../drs/latest/userguide/getting-started-initializing.md "../../../drs/latest/userguide/getting-started-initializing.md") in advance in both the source and target AWS Regions, and conduct regular failover and failback drills.
2. Assign _AWSElasticDisasterRecoveryRecoveryInstancePolicy_ to the IAM Role of our EC2 Instances. This IAM Policy is used to secure the permission policies needed to communicate with _Elastic Disaster Recovery Service_ API during failback.
3. Before starting a failback, make sure the EC2 recovered instances have a network interface while meeting the specified [network requirements](../../../drs/latest/userguide/Network-Requirements.md "../../../drs/latest/userguide/Network-Requirements.md").
4. Access to EC2 instance metadata is required. If you have a custom network setup that modifies the operating system route, ensure that access to the metadata is intact. Learn how to verify metadata access for [Linux](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md")
   and for [Windows](../../../AWSEC2/latest/WindowsGuide/instancedata-data-retrieval.md "../../../AWSEC2/latest/WindowsGuide/instancedata-data-retrieval.md").
5. EC2 Instances that have failed over must resolve through DNS the Regional DRS endpoint of the failback Region. The resolved endpoint must be accessible from the EC2 Instance through TCP 443.

## Initializing Failback

To initialize failback, you need to **start reverse replication** process from the DR Region by following the below steps:

1. Go to the recovery AWS Region.
2. Choose the **AWS Elastic Disaster Recovery** service.
3. Navigate to the **Recovery instances** page.
4. Select the servers that you want to protect and select **Start reversed replication**.
5. You should now see a new Source server in the DRS Console in the source Region.

**Note:**
. All server data is transferred over the wire during this step, resulting in
[cross-Region data transfer costs](https://aws.amazon.com/disaster-recovery/pricing/ "https://aws.amazon.com/disaster-recovery/pricing/").
. Starting a reversed replication creates additional replication resources. To avoid double billing, you can stop replicating the source instances by navigating to the AWS DRS source server in the recovery Region and selecting **Stop replication** in the replication drop-down menu.
. **If replication is stopped, all previous points in time are deleted.** This is done to minimize costs.

## Complete Failback

After the **Reversed direction launch state** is marked as **Ready**, take the following steps to complete the failback:

1. Find the relevant source servers by selecting the **Replicating to source server** link in the recovery instance **(or)** by directly navigating to the **Source servers** page in AWS DRS console at the source
   Region.
2. If the state is **Ready** (or **Ready with lag**), select **Launch for failback** under **Initiate recovery job**.
3. Redirect traffic to failed back instances, which will now become your new primary instances. Traffic redirection is not conducted using DRS.
4. Choose a service according to your preferences (consider using Amazon Route 53).

**Note**:

1. Make sure that your applications are working as expected. If you run into any issues, you can relaunch the instances and try again. Until you opt to failback, your recovery instances will continue to run in your
   recovery AWS Region to ensure business continuity.

## Protect new Failed back instances

**Do not perform** this step when performing a **drill**. This step **replaces** the instances that AWS DRS replicates (from the Source instances to the failed back instances). In a drill, the source instances are still your production environment.

The newly launched failed-back instances are not protected. In order to protect them, follow these steps:

1. Navigate to the recovery instance in the source Region.
2. Select **Start reversed replication**. This step will replace the Instances that the Source Server protects.
