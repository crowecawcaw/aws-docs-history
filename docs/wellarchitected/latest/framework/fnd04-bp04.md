

# FND04-BP04 Implement mechanisms for patch management

 Effective patch management helps keep systems across your cloud environment secure and running well. As a foundation practice, you need mechanisms that operate patch management across accounts and hybrid infrastructure at scale. Automation applies updates consistently and on time, and cuts manual work. 

 **Desired outcome:** 
+  You have a scalable, automated patch management solution that supports consistent patching across multiple AWS accounts and different types of compute resources across cloud and hybrid environments. 
+  Your solution gives you visibility into patch compliance and supports customized patch schedules. 
+  Your patch management fits into your existing IT service management processes. 

 **Common anti-patterns:** 
+  Relying on manual patching that is error-prone and does not scale. 
+  Lacking visibility into patch compliance across accounts. 
+  Using different patch schedules and baselines across teams. 
+  Skipping patching on on-premises systems that work with cloud workloads. 

 **Benefits of establishing this best practice:** 
+  Automated, central patch management applies security updates consistently and on time, which cuts vulnerability exposure across all systems. 
+  Consistent patching across accounts and environments closes the gaps that outside parties target in unpatched systems. 
+  Full patch compliance reporting supports risk management and effective security governance. 
+  Automation replaces manual patching and reduces human error, which also improves consistency. 
+  Central reporting supports compliance audits and shows adherence to security standards. 
+  Integration with IT service management processes and scheduled maintenance windows coordinates patching across cloud and hybrid environments and keeps business disruption low. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Unpatched systems are one of the most common sources of cloud security issues. Without central patch management, teams patch on their own schedules or not at all, which leads to inconsistent security across accounts and Regions. In multi-account environments with hundreds of instances at different patch levels, you cannot easily see your organization's exposure to a newly disclosed vulnerability. 

 Cloud scale, distribution, and rate of change require automated patch management. Manual or account-by-account patching falls behind on compliance and cannot respond to critical vulnerabilities in time. 

 The architectural foundation rests on central orchestration, standard baselines, and broad visibility. Use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to automate patching consistently across multiple AWS accounts and Regions. Extend it to on-premises and other cloud environments with [hybrid node management](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html). In multi-account environments, use [Quick Setup patch policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-patch-manager.html) to deploy patch management configurations across AWS Organizations with central governance and the option for account-level customization. 

 Use [custom patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-manage-patch-baselines.html) to encode security and compliance rules as policy. Different application tiers and risk profiles need different patch approval rules. Production payment systems have different requirements than development sandboxes. Define these requirements as baselines and pair them with a tagging strategy so auditable rules apply automatically based on how resources are categorized. 

 Patch can operations check compliance without making changes and can run often without business impact, which gives continuous visibility into patch status. Patch installation operations need careful scheduling to reduce disruption. Run scanning continuously across all environments, and run installation inside approved maintenance windows. 

 Bring patch compliance data from all managed instances across accounts into a central location for organization-wide visibility, reporting, and alerting. Integrate with existing IT service management tools to keep patch activity inside established change control. Central visibility supports automated change records, notifications about non-compliant instances, and reporting for compliance audits. 

 For zero-day exploits and critical security updates that cannot wait for standard patch cycles, set up expedited approval processes and dedicated maintenance windows. Document procedures for quick assessment, testing, and deployment of emergency patches, and keep audit trails and change management in place. 

 Organizations that lack automation fall behind on security patches and build up vulnerability debt. Those that automate without proper testing and rollback hit downtime from bad patches. Those that patch without coordinating maintenance windows disrupt operations. Effective patch management combines automation for scale and consistency, testing to help prevent service disruption, and scheduling that respects business needs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure Systems Manager in all target accounts:** [Set up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) and the [IAM roles and permissions](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) Systems Manager needs to manage instances across your AWS accounts and on-premises environments. For hybrid environments, follow the guidance for [managing nodes in hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html). 

1.  **Enable organization-wide patch management:** For multi-account environments, configure [Quick Setup patch policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-patch-manager.html) to deploy patch management across accounts and Regions in your AWS Organization. This gives you central governance and supports account-level customization where needed. 

1.  **Create custom patch baselines and patch groups:** [Define patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-manage-patch-baselines.html) that set which patches are applied automatically and which need approval. Use [tags to create patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-groups.html) that match your application environments and criticality levels. 

1.  **Define maintenance windows using tags:** Use a [tagging strategy for maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html) to set when different groups of instances can be patched. This supports staggered patch deployments that reduce business impact. 

1.  **Configure automated patching schedules:** Create [Systems Manager maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html) to automate patch scanning and installation on your defined schedules and patch groups. For custom orchestration needs beyond native Systems Manager capabilities, such as integrating with external approval workflows or running pre- or post-patching validation, use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions with the [Systems Manager APIs](https://docs.aws.amazon.com/systems-manager/latest/APIReference/Welcome.html) and [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) to trigger them. 

1.  **Set up resource data sync to centralize compliance data:** Configure [Systems Manager Inventory resource data sync](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html) to bring patch compliance data from all managed instances into a central [Amazon S3](https://aws.amazon.com/s3/) bucket for unified reporting. 

1.  **Create patch compliance dashboards and reports:** Use [AWS Quick](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) or other business intelligence tools to build [dashboards and reports](https://aws.amazon.com/blogs/mt/visualize-aws-systems-manager-patch-manager-information-using-amazon-quicksight/) that show patch compliance across your environment. 

1.  **Integrate with ITSM tools for change management:** Build integrations between your patch management solution and ITSM tools using APIs and webhooks to automate change request creation and keep an auditable record of patching activities. 

1.  **Develop processes for testing and rolling out patches:** Set up a systematic approach for testing patches in lower environments before deploying to production. Include steps to validate application function after patching and procedures to roll back problem patches if needed. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND03-BP01 Define observability standards and policies](fnd03-bp01.md) 
+  [FND03-BP02 Establish central, cross-account observability capabilities](fnd03-bp02.md) 
+  [FND04-BP05 Establish service quota management](fnd04-bp05.md) 
+  [FND05-BP08 Employ vulnerability and patch management controls](fnd05-bp08.md) 

 **Related documents:** 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [Managing nodes in hybrid and multicloud environments with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html) 
+  [Working with custom patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-manage-patch-baselines.html) 
+  [Creating a resource data sync for Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html) 
+  [Visualize AWS Systems Manager Patch Manager information using Quick](https://aws.amazon.com/blogs/mt/visualize-aws-systems-manager-patch-manager-information-using-amazon-quicksight/) 
+  [Creating your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [AWS Systems Manager Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager.html) 
+  [Configure patching for instances in an organization using a Quick Setup patch policy](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-patch-manager.html) 
+  [Troubleshooting AWS Systems Manager patching made easy with Amazon Bedrock's automated recommendations](https://aws.amazon.com/blogs/mt/troubleshooting-aws-systems-manager-patching-made-easy-with-amazon-bedrocks-automated-recommendations/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Best practices for operating on AWS (COP321)](https://www.youtube.com/watch?v=XBKq2JXWsS4) 
+  [AWS re:Invent 2023 - Centralize hybrid & multicloud management with AWS (COP324)](https://www.youtube.com/watch?v=D90CbElOQ5g) 