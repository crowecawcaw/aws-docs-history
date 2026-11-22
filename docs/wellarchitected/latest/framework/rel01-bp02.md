

# REL01-BP02 Manage service quotas across accounts and regions

 Workloads that span multiple accounts or Regions carry a separate set of quota values in each space. A resilience design that fails over to a secondary location depends on that location holding enough quota to absorb the shifted load. Request and reconcile quotas in every environment where production traffic runs or could run after a failover. 

 **Desired outcome:** 
+  Your quotas are set consistently across every account and Region a workload uses, including secondary and failover locations. 
+  Your secondary Regions hold enough quota to run peak production load if the primary Region becomes unavailable. 
+  You have an automated process that detects when a quota changes in one Region but not others and flags it for reconciliation. 
+  You apply quota changes to multiple accounts and Regions through a repeatable mechanism rather than one location at a time. 

 **Common anti-patterns:** 
+  Teams let usage grow in one Region without keeping matching capacity in the Regions they would fail over to. 
+  Teams set quotas independently in each Region, with no process to keep them aligned. 
+  Teams ignore how an active/passive or active/active design changes quota needs during a failure in a non-primary Region. 
+  Teams review quotas in the primary Region only and never revisit the others. 
+  Teams avoid raising quotas because they wrongly believe an increase carries a cost, as a capacity reservation would. 

 **Benefits of establishing this best practice:** 
+  Secondary Regions can absorb full production load during a Regional failure, reducing errors and degradation. 
+  Consistent quotas across locations remove a class of failover surprises that testing rarely catches. 
+  Automated drift detection keeps environments aligned as individual quotas change over time. 
+  Repeatable multi-Region requests reduce the manual effort of maintaining many accounts. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Quotas are per account and, in most cases, per Region, but resilience is a property of the whole system. When you design for *active/active*, *active/passive – hot*, *active/passive – cold*, or *pilot light*, the secondary location must carry traffic when the primary cannot. This requirement can break if the secondary sits at default quotas while the primary has been raised over months of growth. 

 Past traffic is a poor guide to the quota a failover Region needs. A passive Region may have handled almost no load, so its usage history suggests small quotas are fine. The moment it becomes the primary, it must serve peak demand for the entire workload. Size failover Regions to peak production demand. For the detailed approach to calculating failover headroom, see [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md). 

 *Service quota drift* occurs when a named quota is changed in one Region but not in the others. An engineer raises a quota in the primary Region to unblock a launch, the change never propagates, and the drift only becomes visible during a failover or a game day. Because the same quota name can hold different values across Regions, drift is not always an error, but it needs ongoing tracking. Any Region that carries traffic, or could carry it after a failover, belongs in the reconciliation set. 

 Testing rarely solves this problem. Failover exercises are seldom scaled to the peak capacity the secondary Region would see, so a table-top or game-day test can pass while a real event fails. Treat quota reconciliation across Regions as a separate control from testing. For organizations structured under [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), [Service Quotas request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) apply the same increase across chosen Regions and accounts. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select the accounts and Regions in scope:** Base the set on your service, latency, regulatory, and disaster recovery requirements. Include every account and Region that runs traffic today and every one that could run traffic after a failover. 

1.  **Compare quotas across the in-scope locations:** Read the applicable quotas in each account and Region and record the differences. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) reports usage that has breached the 80 percent and 90 percent thresholds for supported services. 

1.  **Size failover Regions to peak load:** For an active/passive design, verify that each passive Region holds enough quota to run peak production demand, not the light load it carries today. Confirm the workload would start and scale there during a primary-Region failure. 

1.  **Automate quota drift detection:** Run a scheduled check that compares each named quota across Regions in the same account and reports any divergence. Act on the report by raising the lagging quota where traffic warrants it. 

1.  **Apply changes through request templates:** Where your accounts are organized under AWS Organizations, use [Service Quotas request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) to apply an increase across the associated Regions and accounts at once. Create a template, associate the target Regions, and record the intended value. 

1.  **Review templates on a cadence:** Revisit existing request templates when Regions, quotas, or accounts change, so the templates continue to reflect the quotas your resilience design depends on. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL01-BP01 Aware of service quotas and constraints](rel01-bp01.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 
+  [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md) 
+  [REL01-BP05 Automate quota management](rel01-bp05.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 

 **Related documents:** 
+  [Availability and recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [Using Service Quotas request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) 
+  [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) 
+  [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) 
+  [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) 
+  [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) 
+  [Availability with redundancy](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html) 
+  [Automating Service Limit Increases and Enterprise Support with AWS Control Tower](https://aws.amazon.com/blogs/mt/automating-service-limit-increases-enterprise-support-aws-control-tower/) 

 **Related videos:** 
+  [How do I manage my service quotas for my AWS services?](https://www.youtube.com/watch?v=Ddf5WG5I0Qo) 

 **Related tools:** 
+  [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 