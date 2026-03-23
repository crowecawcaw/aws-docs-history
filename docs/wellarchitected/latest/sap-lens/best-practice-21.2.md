# Best Practice 21.2 - Implement sustainability improvements for SAP software and underlying infrastructure

After the business requirements and criteria for sustainability improvements have
been defined, the SAP architect team must implement them. Given that in most cases with
standard SAP architectural patterns (except for those called out in the following sections),
the recommendations in the SAP Lens cost optimization pillar directly align with
sustainability best practices. We will not duplicate those suggestions here and refer you to
the cost optimization pillar for guidance.

**Suggestion 21.2.1 - Develop or redevelop your SAP code with
sustainability in mind**

Highly customized SAP systems require more resources to run as a general rule.
Complex, bespoke programs can lead to statements, transactions, and reports that require
additional CPU and memory beyond optimized native SAP transactions. Adopting sustainable
development best practices, despite the additional development time, can notably improve
the code performance and reduce infrastructure usage. This impact can be magnified for
frequently run code.

Avoiding bespoke development entirely and staying with standard, well-tuned SAP
transactions is one approach. Where development is required, optimize queries or use tools
such as the ABAP Test Cockpit to improve the performance of your code. As mentioned in
Suggestion 21.2.2, keep your SAP software version as current as is feasible. This helps
reduce the need for specialized development, which otherwise would not be necessary due to
newly introduced or improved functionality.

Well-Architected Framework [Sustainability]: [Optimize areas of code that consume the most time or resources](../sustainability-pillar/optimize-areas-of-code-that-consume-the-most-time-or-resources.md "../sustainability-pillar/optimize-areas-of-code-that-consume-the-most-time-or-resources.md")

SAP Documentation: [ABAP Test Cockpit](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/491aa66f87041903e10000000a42189c.html?locale=en-US "https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/491aa66f87041903e10000000a42189c.html?locale=en-US")

**Suggestion 21.2.2 – Perform regular patch
management**

Performing regular patch management ensures that your system will benefit from the
latest SAP performance enhancements while avoiding unnecessary development (see Suggestion
21.2.1). By keeping your SAP systems and related software up-to-date, SAP operations teams
can avoid more intensive patching and upgrade activities. These activities can require
additional temporary hardware, which would add to measurable environmental impact. This
suggestion is in direct alignment with the SAP Lens security and operational excellence
pillars suggestions regarding SAP patching activities.

- SAP Lens [Operational Excellence]: [Best Practice 4.2 –
  Regularly perform patch management for software currency](best-practice-4-2.md "best-practice-4-2.md")
- SAP Lens [Security]: [Best Practice 6.4 –
  Establish a plan for upgrading and patching all applicable software](best-practice-6-4.md "best-practice-6-4.md")
  **Suggestion 21.2.3 - Implement data classification and
  tiering**

As mentioned in the [cost optimization section of
this lens](cost-optimization.md "cost-optimization.md"), storage optimization should be a focus for reducing costs but can also
be justified from a sustainability perspective. By default, data and objects in SAP
systems are not archived nor moved to more energy efficient storage classes (or out of
memory, in the case of HANA-based systems) as the data ages. Options such as HANA NSE Data
Tiering, HANA extension nodes, Data Tiering Optimization, and data archiving or deletion
should be evaluated. In addition, using lifecycle policies for database backups and
snapshots can automate maintaining a more sustainable data footprint, as can evaluating
whether the number of backups to retain is appropriate given the SLA. The use of tools
such as SAP TDMS can also reduce the footprint of non-production systems by reducing the
overall database footprint and associated storage.

- Well-Architected Framework [Sustainability]: [Implement a data classification policy](../sustainability-pillar/implement-a-data-classification-policy.md "../sustainability-pillar/implement-a-data-classification-policy.md")
- SAP Lens [Cost Optimization]: [Best Practice
  19.5 – Consider tiering options for live data](best-practice-19-5.md "best-practice-19-5.md")
- Well-Architected Framework [Sustainability]: [Use lifecycle policies to delete unnecessary data](../sustainability-pillar/use-lifecycle-policies-to-delete-unnecessary-data.md "../sustainability-pillar/use-lifecycle-policies-to-delete-unnecessary-data.md")
- SAP Documentation: [SAP Test Data
  Migration Server](https://help.sap.com/docs/SAP_TEST_DATA_MIGRATION_SERVER "https://help.sap.com/docs/SAP_TEST_DATA_MIGRATION_SERVER")
  **Suggestion 21.2.4 - Favor scale-out architectures where
  possible**

As described in the [Cost optimization](cost-optimization.md "cost-optimization.md") and [Performance efficiency](performance-efficiency.md "performance-efficiency.md") pillars of this lens, scale-out architectures can
mitigate the risk of over-provisioning by adding smaller compute capacity whenever
required. SAP application servers inherently are scale-out, so plan to use this capability
most efficiently for the demand required. For databases, scale-out may or may not be
possible. In situations where it is, the sustainability characteristics of incremental
growth may outweigh the operational overhead of managing a scale-out environment.

- Well-Architected Framework [Sustainability]: [Scale infrastructure with user load](../sustainability-pillar/scale-infrastructure-with-user-load.md "../sustainability-pillar/scale-infrastructure-with-user-load.md")
- SAP Lens [Performance Efficiency]: [Best
  Practice 13.3 – Select architectures that allow for independent scaling of systems
  or components](best-practice-13-3.md "best-practice-13-3.md")
- SAP Lens [Cost Optimization]: [Best Practice
  17.4 – Review the size, granularity, and latest available EC2 instances for SAP
  components](best-practice-17-4.md "best-practice-17-4.md")
  **Suggestion 21.2.5 - Shut down or terminate EC2 instances covered
  by Reserved Instances or Savings Plans even when there are no additional cost
  savings**

Amazon EC2 Reserved Instances (RI) and Savings Plans provide lower prices compared to On-Demand
pricing in exchange for specific usage commitments. The possibility exists that your
compute usage could drop below this commitment at times, presenting the rare case for SAP
systems where a more sustainable architecture is not directly tied to reducing your AWS
spend. In such cases, your sustainability posture might still be improved despite no
additional cost savings when following standard cost optimization best practices. This
guidance includes shutting down unused non-production systems, scaling in application
servers during periods of low utilization, transitioning EC2 instances to the latest
generation to improve CPU utilization, and minimizing the size of pilot-light HA/DR
systems.

- SAP Lens [Cost Optimization]: [Best Practice 18.1 –
  Understand the payment and commitment options available for Amazon EC2](best-practice-18-1.md "best-practice-18-1.md")
- SAP Lens [Cost Optimization]: [Best Practice 17.4 –
  Review the size, granularity, and latest available EC2 instances for SAP
  components](best-practice-17-4.md "best-practice-17-4.md")
- Well-Architected Framework [Sustainability]: [Use the minimum amount of hardware to meet your needs](../sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.md "../sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.md")
  **Suggestion 21.2.6 – Consider sustainability when choosing
  AWS Regions**

SAP landscapes are frequently deployed in AWS based on such factors as proximity to
end users, data residency requirements, infrastructure cost, and compliance with specific
governmental regulations. In a business that prioritizes sustainability, the environmental
impact of deploying SAP workloads should also be considered when choosing the appropriate
AWS Region. Regions that are near an Amazon renewable energy project may be more
desirable in such cases.

- SAP Lens [Performance efficiency]: [Best Practice 13.4 –
  Choose Regions and Availability Zones to minimize latency](best-practice-13-4.md "best-practice-13-4.md")
- SAP Lens [Security]: [Best Practice 5.2 –
  Classify the data within your SAP workloads](best-practice-5-2.md "best-practice-5-2.md")
- Well-Architected Framework [Sustainability]: [Region
  selection](../sustainability-pillar/region-selection.md "../sustainability-pillar/region-selection.md")
  **Suggestion 21.2.7 - Leverage managed services whenever
  possible**

A number of non-NetWeaver SAP products can be installed on AWS services that are
managed above the infrastructure layer in a more sustainable fashion. One such example is
the use of Amazon RDS for SAP BusinessObjects BI Platform. The use of managed services for
common SAP-related functions is also advisable. Some examples include using AWS Backup for
AMI and Amazon EBS snapshot management or using Amazon AppFlow for bidirectional data flow with your
Amazon S3-based data lake.

Using managed services can reduce capacity guesswork and allow for AWS internal
provisioning mechanisms to maximize underlying resource efficiency. As an example, where
the option exists for your SAP systems, use Amazon Elastic File System (Amazon EFS) instead of Amazon EBS. Amazon EFS
allows for the use of only the precise amount of storage required, while EBS uses
allocated space that can leave a portion unused. As another example, Amazon EC2 instances may
be removed from your environment and replaced by managed services, such as removing
bastion hosts in public subnets and instead using AWS Systems Manager Session Manager for direct
access.

- Well-Architected Framework [Sustainability]: [Use
  managed services](../sustainability-pillar/use-managed-services.md "../sustainability-pillar/use-managed-services.md")
- AWS Documentation: [CMS and Audit Database Architecture Options](../../../sap/latest/sap-businessobjects/bobi-linux-architecture-options.md#bobi-linux-cms-and-audit-database-architecture-options "../../../sap/latest/sap-businessobjects/bobi-linux-architecture-options.md#bobi-linux-cms-and-audit-database-architecture-options")
- AWS Documentation: [SAP NetWeaver on AWS Backup
  and Recovery](../../../sap/latest/sap-netweaver/backup-and-recovery.md "../../../sap/latest/sap-netweaver/backup-and-recovery.md")
- AWS Documentation: [Amazon AppFlow
  Integrations](https://aws.amazon.com/appflow/integrations/ "https://aws.amazon.com/appflow/integrations/")
