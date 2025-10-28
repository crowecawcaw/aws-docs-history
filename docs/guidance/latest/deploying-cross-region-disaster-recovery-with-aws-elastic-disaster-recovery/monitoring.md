# Monitoring AWS Elastic Disaster Recovery

## Monitoring resources

Monitoring will play a critical role when defining a DR strategy. The ability to observe, monitor, and alert on resources and system performance at multiple levels is required to operationalize your plan.

### Configure replication monitoring and alerting

Elastic Disaster Recovery can utilize [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to assist with monitoring. CloudWatch is a monitoring service that helps you monitor AWS resources as they are being consumed within your account. When these two services are integrated, you can monitor Elastic Disaster Recovery events with CloudWatch to build a customizable and detailed dashboard for Elastic Disaster Recovery. These services can be extended further with [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") and [Amazon Simple Notification Service](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") (Amazon SNS), to get real-time alerts and automate responses.

**Creating CloudWatch dashboards to monitor Elastic Disaster Recovery**

You can visualize and share your metrics using CloudWatch dashboards.There are many metrics available within CloudWatch to help you monitor and manage the state of your disaster recovery operations. With CloudWatch, you can include metrics to monitor your source server count,
time since last successful test, and lag of source servers (when the Elastic Disaster Recovery service is no longer in continuous data protection mode and should be investigated for root cause). We recommend using CloudWatch to setup dashboards and notifications to alert you on any possible replication issues. Follow the steps below:

1. Navigate to the Amazon CloudWatch dashboard.
2. Under Dashboards, select **Automatic dashboards**
3. Filter for and select **Elastic Recovery Service**
   1. You will be taken to a default dashboard that monitors several aspects of Elastic Disaster Recovery. These metrics are based on the replication instances you have running in the AWS Region you currently have selected:
      1. LagDuration: Average
         1. This is the average time of "Lag" on your replication severs.
            Anything higher than 0 should be investigated for possible issues, but
            we recommend monitoring for lags larger than an hour (or your RPO if close to an hour).

      2. Backlog: Average
         1. This is the average amount of "backlog". Backlog is generated when the service is unhealthy, but is still seeing data being written to source, that it is unable to replicate

      3. DurationSinceLastSuccessfulRecoveryLaunch: Maximum
         1. This is the maximum amount of time since the last successful launch of DRS machines

      4. ElapsedReplicationDuration: Maximum
         1. This is the amount of time Elastic Disaster Recovery has been replicating data

      5. ActiveSourceServerCount: Average
         1. This is how many source servers have Elastic Disaster Recovery installed

      6. TotalSourceServerCount: Average
         1. This is how many source servers have Elastic Disaster Recovery installed

      7. ProtectedSourceServerCount: Average
         1. This is how many source servers have Elastic Disaster Recovery installed excluding disconnected and stopped servers

4. Choose **Add to dashboard**
   1. You can either select an existing dashboard, or choose **Create new**
      1. If you decide to create a new dashboard, you will be taken to the next screen to enter a name and select **Create**

   2. Select **Add to dashboard**

You will now have a dashboard monitoring Elastic Disaster Recovery under your **Custom dashboards** section in CloudWatch.

**Configuring your Amazon Simple Notification Service Topic**

Amazon SNS will be used to alert a specific inbox or distribution list when any AWS Elastic Disaster Recovery source machines are experiencing a stalled replication that must be addressed. Doing so will help to identify and remediate issues quicker, so that your RPO goals can be
maintained. Stalled replication is the main indicator of replication issues and can indicate multiple issues.

1.  Navigate to Amazon Simple Notification Service.
2.  Choose **Create Topic**.
    1.  Under **Details** and **Type**, choose **Standard**.
    2.  Under **Name** enter a name for this topic. (for example:
        drs-replication-monitoring)

            * *Optional:* Enter a display name for SMS messages to mobile devices.




            	+ Note: As of June 1, 2021, US telecom providers no longer support person-to-person long codes for applications-to-person communications.
            	See the [Amazon SNS Developer Guide](../../../sns/latest/dg/sms_publish-to-phone.md "../../../sns/latest/dg/sms_publish-to-phone.md")for more information.
            * *Optional:* For Tags, enter a key-value pair for easy identification later.




            	+ Select **Create topic**.
            	+ Once the topic is created, select *drs-replication-monitoring* from the list.
            	+ Choose **Create subscription**.
            	+ Validate that the Topic ARN under **Details** is the same as drs-in-lag.
            	+ From the Protocol dropdown, choose **email**.
            	+ Under Endpoint add the email or distribution list to receive these alerts.
            	+ Choose **Create subscription**.

**Create a rule using the console**

The next step is to configure Amazon EventBridge to monitor for specific Elastic Disaster Recovery events related to replication health. Should EventBridge receive an event for unhealthy replication status for Elastic Disaster Recovery, it will notify the Amazon SNS topic. This, in turn, notifies the subscribers of that topic.

1. Open Amazon EventBridge
2. Choose **Create rule**.
3. Under **Name** and **Description**, enter the name for this rule (we use "drs-replication-monitoring" for this step).
4. Under Define pattern, choose **Event pattern**.
5. Select Pre-defined pattern by service.
6. From the dropdown menu for Service provider, choose **AWS**.
7. Under the Service name dropdown, choose **Elastic Disaster Recovery Service**.
8. Under Event type, choose **DRS Source Server Data Replication Stalled Change**.
9. Under Select targets and Target, choose **SNS topic**.
10. For Topic, choose the SNS topic created earlier: **drs-replication-monitoring**.
11. Choose **Create**.

You have now created a dashboard that will monitor your Elastic Disaster Recovery replication infrastructure, and notify you if there are any stalled replication servers that would cause you to miss your RPO.

## Monitoring Costs

### Configure cost monitoring

There are several configuration strategies possible with Elastic Disaster Recovery. Understanding what makes up the associated costs of using Elastic Disaster Recovery is an important consideration when deciding how to further optimize the system for performance vs cost while maintaining your resilience objectives. This may include decisions on retention periods, Region selection, network design, and infrastructure configurations.

The following section provides the steps to activate cost allocation tags, creating and saving a custom report, and exporting the report data. This will provide insight into the overall costs of the Amazon EC2, Amazon EBS, and EBS snapshot resources provisioned by Elastic Disaster Recovery.

**Activate cost allocation tags** This section walks through the process of enabling user-defined cost allocation tags for Elastic Disaster Recovery. Once enabled, you can use these tags on your cost allocation report to track costs.

1. Log in to the AWS Management Console and search for **Billing and Cost Management**.
2. Locate and select **Cost Allocation Tags**.
3. Under **User-defined cost allocation tags**, find the AWSElasticDisasterRecoveryManaged tag.
4. Select the checkbox for this tag, and choose **Activate**.
5. Choose **Activate** from the pop up. It may take a couple of hours before the tags are available.

Where to optimize

- Use default instance types for replication servers unless source servers are often in lag
- Use automated disk type
- Lower snapshot retention to minimal needs

_Elastic Disaster Recovery should not be used for long term
retention; use a backup solution for long term storage and archiving_

**Create cost categories**

This section walks through the process of creating cost categories. This allows you to map Elastic Disaster
Recovery costs and usage into meaningful categories using a rules-based engine.

**Add rule**

1. Log in to the AWS Management Console and search for **Billing and Cost Management**.
2. Locate and select **Cost Categories** and select **Create cost category**.
3. Provide a Name (for example, DRSCost) to the cost category and select **Next**.
4. Choose Rule type as Inherited value, and Dimension as Cost Allocation Tag, Tag key as AWSElasticDisasterRecoveryManaged, and select **Add rule**.

**Modify rule**

1. Choose **Rule type** as **Regular** and **DRSCost _Value_** as **License**.
2. Under **Dimension 1**, choose **Service**. For **Operator**
   select **Is** and for **Service Code** choose **AWSElasticDisasterRecovery**.
3. Select **Next**.
4. Select **Create cost category**. It will take up to 24 hours for the cost category to be available in AWS Cost Explorer.

**Create a Cost Explorer report**

This section walks through the steps to create a customized Cost Explorer report for Elastic Disaster Recovery. It uses the filters and cost categories created in the preceding section.

Create report

1. Log in to the AWS Management Console and search for AWS Cost Explorer.
2. Open the AWS Cost Management dashboard and select **Cost Explorer**.
3. Locate **Cost Organization** and select Cost Category.
4. Select the cost category (for example: DRSCost) which was created in the Create Cost Categories section.
5. Select two checkboxes: License and drs.amazonaws.com
6. Select **Apply Filters**.

Select filters
. On the top left, select the **Group by: Usage Type**.
. Locate time ranges and select the time for which you would like to see the data. In the following example, we set it to **Last 7 Days** with the time granularity as **Daily**.
. Select **Bar** style type for the chart. You will see the cost breakdown of the staging area. This includes the cost of replication servers, Amazon EBS volumes, Amazon EBS snapshots, as well as other services and AWS resources.
. Locate and select **Save as** and assign the new report a name. For example,
`–0—`.
. Select **Save Report**.

**View and export saved Cost Explorer report**

This section walks through the steps to view the Cost Explorer report and export it to a CSV file.

1. Log in to the AWS Management Console.
2. Search for AWS Cost Explorer and open the **AWS Cost Management** dashboard.
3. Select **Reports**.
4. Select the report that was previously saved. The total cost of Elastic Disaster Recovery is included in that report.
   1. The report can be further customized by using the **Group by** options near the top or any of the other filters available in AWS Cost Explorer.

5. Select **Download CSV** to export your data for further analysis.

**How can you optimize costs?**

- Utilize the default replication server instance types at first. Allow Elastic Disaster Recovery to replicate your initial dataset, then ensure no Source servers are stating that they are in "Lag". If there are any
  source servers that are in lag, follow the **Advanced Topics** section at the end of this userguide. This section may conclude that you need to increase the size and performance of the replication server or provide a dedicated replication server.
- Use the "Auto volume type selection" option for your replication servers
- When choosing **Auto volume type selection**, the service will dynamically switch between performance or cost optimized volume type according to the replicated disk write throughput.
- Lower snapshot retention to minimal length requirements. Based on the changed rate of your dataset, this can have a large impact on overall Elastic Disaster Recovery costs.

_Note that if you have compliance requirements and require your snapshots for long-term retention, you should use a long-term storage and backup solution like [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/"). Elastic Disaster Recovery is not intended to act as a backup or archive storage service, and hence is not a suitable solution for long-term retention of your snapshots and other data_

**Cost Optimization**

There are multiple configuration strategies possible with Elastic Disaster Recovery. Understanding what makes up the associated costs of using Elastic Disaster Recovery is a key step in targeting efforts to reduce cost without sacrificing resilience. This includes things like using the most relevant resilience strategy and retention periods, driving redundancy, selecting the Region, and right-sizing your infrastructure.

The method to reduce operational costs when using Elastic Disaster Recovery is to perform a combination of the following:

- ❏ Evaluate the retention period required for point-in-time snapshots. How far into the past do you need to retain the ability to do a full server restore, as opposed to restoring from a backup? Make sure
  to consider applicable compliance and regulatory requirements.
- ❏ For those servers being covered by Elastic Disaster Recovery, consider whether there are redundant drives mounted that are no longer in use and do not need to be replicated. These can either be unmounted
  or excluded when installing the replication agent.
- ❏ Right-size the target failover infrastructure by selecting the appropriate Amazon EC2 instance type in the EC2 launch template. You can use the instance right-sizing feature to map to an instance type that closely follows the source infrastructure, however you should use
  operational data in the source environment to right size these resources.

The size of the underlying disks (for example, the entire disk and not just partitions) directly dictates the amount of data that is replicated over into AWS during the initial sync process. As a result, right sizing and
being selective of workloads, as per RPO and RTO objectives, gives the benefit of both monetary and saving time.

### Resources:

- [AWS Well-Architected Framework: Cost Optimization Pillar](../../../wellarchitected/latest/cost-optimization-pillar/welcome.md "../../../wellarchitected/latest/cost-optimization-pillar/welcome.md")
- [AWS Well Architected Framework: Performance Efficiency](../../../wellarchitected/latest/performance-efficiency-pillar/welcome.md "../../../wellarchitected/latest/performance-efficiency-pillar/welcome.md")
