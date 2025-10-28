# Best Practice 20.5 – Review usage for opportunities

to optimize

Review your SAP workload periodically to identify opportunities to optimize cost.
Regular reviews should focus on: minimizing the differences and anomalies found between your
AWS bill and your SAP workload budget, checking that all your SAP cloud resources are
appropriately sized and not over-provisioned, and understanding any new AWS service
releases or cost reductions that could improve the cost effectiveness of your SAP
workload.

**Suggestion 20.5.1 – Minimize additional cost where your usage has
been higher than initially planned**

Your cloud usage might have grown outside of your estimated cost model due to
unplanned business events or additional performance required. Analyze these changes with a
view to optimizing the new cost. Consider additional Savings Plan commitments or Reserved
Instances if this is a sustained change.

Where additional capacity is required for only short periods, consider horizontal
scaling mechanisms (for example, additional SAP application servers) using automatic
scaling or scheduled On-Demand Instance capacity to minimize cost further.

**Suggestion 20.5.2 – Review SAP workload usage metrics and further
right-size where possible**

Regularly review the components supporting your SAP system to ensure they are
right-sized. Use CloudWatch metrics to consider:

- Is the SAP EC2 compute the right size? Is CPU or memory utilization low? Could you
  move to a smaller EC2 instance size?
- Is SAP storage the right size? Is there excess space provisioned but unused? Could
  you reduce volume sizes?
- Is SAP storage appropriately performant? Is there excess IOPS or MBPS provisioned
  which could be reduced?
- Are backup and snapshots being managed appropriately? Do you have too many backup
  copies on S3 Standard which could be archived to Amazon S3 Infrequently Accessed or
  Amazon Glacier?
- Use tools such as [AWS
  Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") and [AWS
  Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/") to identify additional areas for optimization. Be aware of
  SAP specific compute and storage restrictions as per SAP note: [1656099 - SAP Applications
  on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") [Requires SAP Portal
  Access].
  Use your findings to continually right-size your SAP workload components on a regular
  basis and maximize your use of Savings Plans and Reserved Instances.

**Suggestion 20.5.3 – Understand new AWS services and plan to
implement where further cost optimization can be achieved**

AWS regularly releases new services and periodically reduces prices. Review new SAP
on AWS service announcements and plan to take advantage of these in your architecture at
a minimum every 12 months. If you have a technical account manager (TAM) as part of an
Enterprise Support agreement with AWS, they can assist you in a regular new service
briefing and optimization discussion.

Subscribe to the [SAP on AWS
blog](https://aws.amazon.com/blogs/awsforsap/ "https://aws.amazon.com/blogs/awsforsap/") and the [What’s New](https://aws.amazon.com/new/ "https://aws.amazon.com/new/") feed
for the latest announcements and news.

See [Operational Excellence]: [Best Practice 4.4 -
Perform regular workload reviews to optimize for resiliency, performance, agility, and
cost](best-practice-4-4.md "best-practice-4-4.md") for further information on continued optimization of your SAP workload.
