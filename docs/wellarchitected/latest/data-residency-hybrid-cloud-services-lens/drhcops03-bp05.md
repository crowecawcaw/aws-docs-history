

# DRHCOPS03-BP05 Keep your monitoring, alerting, and documentation up to date and in-line with your RTO and RPO targets
<a name="drhcops03-bp05"></a>

 Implement monitoring and alerting in line with your failover strategy, security and operations strategy, and data residency requirements. 

 **Desired outcome:** Maintain comprehensive monitoring, alerting, and documentation systems that are aligned with the organization's defined RTO and RPO targets and key performance indicators (KPIs). For more information on RTO and RPO see DRHCOPS03-BP01 best practice in DRHCOPS03. 

 **Benefits of establishing this best practice:** Keeping monitoring, alerting, and documentation up to date and in sync with RTO, RPO, KPIs, and your data residency requirements enables proactive identification of potential issues, timely incident response, and accurate tracking of recovery progress. This practice helps your organization meet its business continuity and data protection goals. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-7"></a>

 **Monitoring and alerting** 
+  Implement comprehensive monitoring and alerting mechanisms to promptly detect failures or issues that may initiate a failover or recovery process. 
+  Especially on Outposts, monitor key metrics related to replication, network connectivity, and resource utilization to proactively address potential issues. You can implement a set of metrics that use AWS CloudWatch and the AWS Health API. Familiarize yourself with notifications that provide warnings for business-critical impact, including service link down and EC2 retirement notices. 

 **Documentation and training** 
+  Maintain up to date documentation for your DR strategies, including failover and recovery procedures. 
+  Provide regular training to relevant personnel to ensure they are prepared to execute DR plans effectively during an outage or disaster. 

## Resources
<a name="resources"></a>
+  [Architecting for Disaster Recovery on AWS Outposts racks with AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/compute/architecting-for-disaster-recovery-on-aws-outposts-racks-with-aws-elastic-disaster-recovery/) 
+  [Recovery objectives](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/recovery-objectives.html) 
+  [Plan for Disaster Recovery (DR)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html) 
+  [Resilience in AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/disaster-recovery-resiliency.html) 
+  [Automate data synchronization between AWS Outposts racks and Amazon S3 with AWS DataSync](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/) 
+  [Monitoring best practices for Outposts](https://aws.amazon.com/blogs/mt/monitoring-best-practices-for-aws-outposts/) 