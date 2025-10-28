# Best Practice 4.4 – Perform regular

workload reviews to optimize for resiliency, performance, agility, and cost

When running SAP on AWS, plan and dedicate time and resources for continual
incremental improvement to evolve the effectiveness and efficiency of your workload. AWS
regularly releases new services, approaches, improved SLAs, and price reductions that you
can take advantage of to optimize your SAP workload. Understand and validate whether new
service releases are applicable to your SAP workload and, where appropriate, implement
them in your production environment to evolve your workload.

**Suggestion 4.4.1 - Plan regular reviews of your SAP
workload**

Work with your AWS team, AWS Partner, or internal experts to periodically review
your SAP workload using the Well-Architected Framework SAP Lens (this document). Plan to
review your workload at least every once a year. Identify, validate, and prioritize
improvement activities and issue remediation and incorporate this into your
backlog.

Consider harvesting your learnings from operational incidents into curated questions
with best practices guidance. Create Operational Readiness Review (ORR) runbooks to assist
when deploying new SAP landscapes, applications, or workloads.

- AWS Whitepaper (this document): [SAP
  Lens for Well-Architected](sap-lens.md "sap-lens.md")
- AWS Whitepaper: [Operational Readiness Reviews (ORR)](../operational-readiness-reviews/wa-operational-readiness-reviews.md "../operational-readiness-reviews/wa-operational-readiness-reviews.md")

**Suggestion 4.4.2 - Review Amazon EC2 instance sizing and
performance**

Review the CPU usage and memory utilization of your SAP workload by validating
historical CloudWatch metrics. Review each SAP component for low CPU or memory utilization
and consider right sizing EC2 instances to better match workload requirements. Consider
newly released and SAP-certified EC2 instance types for performance fit and cost
optimization. Plan to take advantage of new improvements in your operational
backlog.

See [Cost Optimization](cost-optimization.md "cost-optimization.md") for Amazon EC2 usage
in SAP workloads.

- AWS Documentation: [Amazon EC2 instance types for SAP](../../../sap/latest/general/ec2-instance-types-sap.md "../../../sap/latest/general/ec2-instance-types-sap.md")

**Suggestion 4.4.3 - Review Amazon EBS sizing and
performance**

Review storage usage across your SAP workload by validating volume consumption,
throughput and IOPS usage from CloudWatch historical metrics. Review each SAP component
for oversized storage or low throughput/IOPS utilization and consider right sizing
Amazon EBS storage sizes and types in order to better match workload requirements. Consider newly
released and SAP certified Amazon EBS types for performance fit and cost optimization.
Plan to take advantage of new improvements in your operational backlog

- AWS Documentation: [Right Sizing](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/ "https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/")
- SAP Lens [Cost Optimization]: [Best Practice
  18.4 - Evaluate the cost impact of storage options based on the required
  characteristics](best-practice-18-4.md "best-practice-18-4.md")

**Suggestion 4.4.4 - Review new services that improve agility or
improve efficiency in your SAP workload operations**

Review new supporting service releases that could improve operations in your SAP
workload. If you have a technical account manager (TAM) as part of an AWS Support
agreement, they can assist you in a new service briefing and optimization
discussion.

Consider new releases such as shared file storage, interface services (for example,
AWS Transfer, API Gateway), security services (for example, Amazon GuardDuty, AWS
Firewall), backup tools (for example, AWS Backint) and automation tools (for example,
Launch Wizard for SAP).

Plan to take advantage of new improvements in your operational backlog.

- AWS Documentation: [“What’s New”
  Feed](https://aws.amazon.com/new/ "https://aws.amazon.com/new/")
- AWS Documentation: [Proactive Services from Support](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/ "https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/")

**Suggestion 4.4.5 - Monitor SAP on AWS blogs and
announcements**

Consider subscribing to the SAP on AWS Blog feed and AWS “What’s New” feed to
stay up to date with newly released service announcements, innovation approaches and price
reductions.

- [SAP on AWS Blog Feed](https://aws.amazon.com/blogs/awsforsap/ "https://aws.amazon.com/blogs/awsforsap/")

**Suggestion 4.4.6 - Plan periodic enhancement work to take advantage
of new and improved AWS services**

Ensure that your operational budget allows for planned support team effort for
implementation and testing of new AWS services and workload evolution on a periodic
basis.
