

# FND05-BP10 Prepare forensic capabilities

 Ahead of a security incident, prepare forensics accounts, tooling, and documented procedures so responders can collect and analyze evidence quickly and preserve chain of custody. 

 **Desired outcome:** 
+  You have established a fully automated forensics capability that can rapidly collect, preserve, and analyze evidence during security incidents. 
+  You maintain forensically sound data collection and analysis processes that preserve chain of custody. 
+  You have created dedicated forensics environments with proper isolation and access controls. 
+  You adhere to legal and regulatory requirements for digital evidence handling. 

 **Common anti-patterns:** 
+  Mixing forensics resources with production workloads or failing to properly isolate forensics accounts and Regions. 
+  Collecting evidence through manual processes or leaving gaps in logging configurations that result in inadequate or incomplete data. 
+  Operating without documented processes for forensics procedures, capabilities, playbooks, and tools. 
+  Overlooking regulatory requirements for evidence handling, retention periods, and chain of custody controls. 

 **Benefits of establishing this best practice:** 
+  Pre-established forensic environments, tools, and processes are ready for immediate use, so you can investigate security incidents faster and preserve evidence integrity and chain of custody. 
+  Automated evidence collection produces consistent, forensically sound data gathering during high-pressure incident scenarios. 
+  Proper isolation of forensics accounts and resources helps protect production workloads and supports complete investigations. 
+  Strengthened compliance with legal and regulatory requirements for digital evidence handling and retention. 
+  Well-documented forensics procedures and playbooks support consistent investigation practices across security teams, support knowledge transfer, and build confidence in the ability to conduct post-incident analysis and support legal proceedings. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Forensic capabilities must be established in advance as opposed to during an incident. Concepts from traditional on-premises forensics apply to AWS, but cloud forensics benefits from automation capabilities that improve both speed and consistency of evidence collection. For architectural patterns and prescriptive guidance, see the [AWS Security Reference Architecture (AWS SRA) – Cyber forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-cyber-forensics/introduction.html) guide. 

 After you set up your environment and AWS account structure, define the technologies for each forensics phase: 
+  **Collection:** Collect relevant AWS logs (CloudTrail, AWS Config, VPC Flow Logs, host-level logs), snapshots, backups, and memory dumps of affected resources. 
+  **Examination:** Extract and assess relevant information from the collected data. 
+  **Analysis:** Analyze the data to understand the incident and draw conclusions. 
+  **Reporting:** Present the information resulting from the analysis phase. 

 Isolate forensics accounts from production workloads. Use either a single dedicated account or one account per Region, depending on your data sovereignty requirements. With per-Region accounts, you can apply SCPs that block resources from being copied outside the intended Region. Because provisioning accounts takes time, create forensics accounts before you need them. Figure 1 shows an example per-Region forensics account structure alongside a security OU. <a name="fnd05-bp10-fig1"></a>

![AWS Organizations hierarchy with an organization root over two organizational units: a Security OU containing a security tooling account and a log archival account, and a Forensics OU containing forensics accounts for two Regions.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/region-account-structure.png)

*Organization structure with separate security and forensics organizational units*


 Manual evidence collection is slow, error-prone, and can break chain of custody. Use [AWS Step Functions](https://aws.amazon.com/step-functions/), [AWS Lambda](https://aws.amazon.com/lambda/), and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to orchestrate collection workflows. When triggered, these workflows automatically capture logs, create snapshots, and perform memory dumps. For reference architectures, see [Automate incident response and forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-incident-response-and-forensics.html) and [Automated Forensics Orchestrator for Amazon EC2](https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/welcome.html). 

**Important**  
 Provision forensics accounts and configure automation before an incident occurs. During an active event, responders focus on containment and recovery, not on requesting new accounts, designing workflows, or troubleshooting permissions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Prepare your forensics environment:** Use [AWS Organizations](https://aws.amazon.com/organizations/) to centrally manage the accounts required for incident response. Create an account structure with a *security OU* and a *forensics OU*. See [Creating an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html). 

1.  **Set up a log archival account within the security OU:** Aggregate logs in a [log archival AWS account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) with limited permissions. 

1.  **Set up a security tools account within the security OU:** Centralize security services in a [security tooling AWS account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html). This account operates as the delegated administrator for security services. 

1.  **Set up your forensics OU accounts:** In the forensics OU, implement either a single forensics account or accounts for each Region you operate in, following the structure in [Figure 1](#fnd05-bp10-fig1). If you create a forensics account per Region, use [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to block resource creation outside that Region, reducing the risk of resources being copied to unintended Regions. Create and instrument forensics accounts well ahead of an incident so responders can use them during response. 

1.  **Capture backups and snapshots:** Set up backups of key systems and databases. These are critical for recovering from a security incident and for forensics purposes. Use services like [AWS Backup](https://aws.amazon.com/backup/) and [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) for point-in-time backups. For detailed guidance, see [Backup and Recovery Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/storageandbackup-pattern-list.html) and [Use backups to recover from security incidents](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/). Secure your backups, particularly important for ransomware scenarios, following [Resilience by design: Building an effective ransomware recovery strategy](https://aws.amazon.com/blogs/storage/resilience-by-design-building-an-effective-ransomware-recovery-strategy/). Regularly test backup and restore processes to verify they work as expected. 

1.  **Automate forensics:** Develop and implement automation for forensics using services like [AWS Step Functions](https://aws.amazon.com/step-functions/), [AWS Lambda](https://aws.amazon.com/lambda/), and [AWS Systems Manager](https://aws.amazon.com/systems-manager/). AWS offers a number of forensics automation resources as reference architectures. See [Automate incident response and forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-incident-response-and-forensics.html) and [Automated Forensics Orchestrator for Amazon EC2](https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/welcome.html). Modify them or create new patterns based on your environment, requirements, and forensics processes. 

1.  **Document forensics procedures and maintain playbooks:** Create detailed documentation of your forensics procedures, including evidence handling protocols, chain of custody requirements, and escalation paths. Develop incident-specific playbooks for common scenarios such as compromised EC2 instances, suspicious IAM activity, or data exfiltration events. Each playbook must reference the relevant automated workflows, explain when to trigger them, and describe the manual fallbacks if automation fails. Store playbooks where the incident response team can reach them even during a disruption affecting your primary systems. See the [AWS customer playbook framework](https://github.com/aws-samples/aws-customer-playbook-framework) and [AWS incident response playbook samples](https://github.com/aws-samples/aws-incident-response-playbooks) for starting points. 

1.  **Test forensics capabilities regularly:** Exercise your forensics capability through tabletop exercises and [SEC10-BP04 Run simulations](sec10-bp04.md). Validate that automated workflows function end-to-end, that responders can access forensics accounts and retrieve evidence, and that logging and backup configurations cover the scenarios you care about. Include multi-account and multi-Region scenarios so you confirm the architecture works at scale. Feed the findings from each exercise back into your automation, documentation, and account configuration. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP06 Establish centralized backup standards and mechanisms](fnd04-bp06.md) 
+  [FND04-BP08 Establish resilience testing tooling](fnd04-bp08.md) 
+  [FND05-BP09 Establish security tooling for investigating incidents](fnd05-bp09.md) 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 
+  [SEC10-BP03 Develop and test security incident response playbooks](sec10-bp03.md) 

 **Related documents:** 
+  [Develop forensics capabilities](https://docs.aws.amazon.com/security-ir/latest/userguide/) 
+  [Appendix B: AWS incident response resources](https://docs.aws.amazon.com/security-ir/latest/userguide/) 
+  [AWS Security Reference Architecture (AWS SRA) – Cyber forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-cyber-forensics/introduction.html) 
+  [A framework for securely collecting forensic artifacts into S3 buckets](https://aws.amazon.com/blogs/security/a-framework-for-securely-collecting-forensic-artifacts-into-s3-buckets/) 
+  [Automate incident response and forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-incident-response-and-forensics.html) 
+  [Use backups to recover from security incidents](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/) 
+  [Resilience by design: Building an effective ransomware recovery strategy](https://aws.amazon.com/blogs/storage/resilience-by-design-building-an-effective-ransomware-recovery-strategy/) 

 **Related examples:** 
+  [Automated Incident Response and Forensics Framework](https://github.com/awslabs/aws-automated-incident-response-and-forensics) 
+  [Automated Forensics Orchestrator for Amazon EC2](https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/welcome.html) 
+  [Automate forensic memory acquisition of Amazon EC2 instances](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/) 

 **Related services:** 
+  [AWS Backup](https://aws.amazon.com/backup/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 