

# REL08-BP01 Use runbooks for standard activities such as deployment

 A runbook is a documented procedure that produces a specific, predictable outcome for a routine operation. Runbooks make standard activities such as deployments, patching, and DNS changes repeatable across people and teams. When a procedure is written down and validated, the result no longer depends on who runs it or whether they remember every step. 

 **Desired outcome:** 
+  Your standard operational activities have documented runbooks with defined success criteria and validation checkpoints. 
+  Your deployment runbooks include rollback procedures that you have tested, not just documented. 
+  Your runbooks are stored under version control, so changes are tracked and previous versions can be restored. 
+  Teams run high-value procedures through automation, and keep validated manual runbooks for game days and audit evidence. 

 **Common anti-patterns:** 
+  Teams make manual or unplanned configuration changes directly in production. 
+  Teams skip documented steps to deploy faster, which leads to failed or partial deployments. 
+  Teams apply changes without ever testing the reversal of those changes. 
+  Teams treat runbooks and playbooks as the same artifact, so routine procedures and incident response blur together. 

 **Benefits of establishing this best practice:** 
+  Change succeeds more often because the people running it know which systems are affected and in what order. 
+  Human error drops because validated procedures replace improvised steps. 
+  Recovery is faster because rollback is a rehearsed step rather than an improvised reaction. 
+  Operational maturity grows as manual procedures become automation and audit evidence. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Runbooks and playbooks solve different problems. A *runbook* is for routine work with a known outcome, such as deploying a release or rotating a certificate. A *playbook* is for investigating and responding to non-routine events, where the outcome is unknown at the start. A team that documents deployments in a playbook format tends to leave out the precise, ordered steps that make the procedure repeatable. A team that tries to handle an incident with a rigid runbook tends to follow steps that no longer apply. Keep the two artifacts distinct. 

 Runbooks mature in stages. Most procedures start as manual steps that you follow and validate. As you gain confidence, encode those steps and then automate them. Manual validation catches broken logic before you encode it. Automating a broken procedure only makes the failure faster and harder to see. Automate a procedure once it is stable and you understand its failure modes. 

 Teams most often neglect rollback. Write rollback steps and test them, because a rollback you have never run might not work when you need it. The same applies to validation. Each runbook needs explicit checkpoints that confirm the system reached the expected state, so operators know whether to continue or reverse. 

 When you place runbooks and their supporting infrastructure definitions in a source repository, every change is reviewable, attributable, and reversible. This simplifies audits and helps you identify and revert changes that cause regressions. Self-service access scoped by permissions lets workload owners run approved procedures without waiting on a central operations team. 

 Pair runbooks with drift detection to catch unplanned changes. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) continuously records the configuration of your AWS resources and detects drift from your expected state. It alerts you when production diverges from what your runbooks and infrastructure as code define. 

 A deployment runbook covers both what is deployed and how it reaches production. Techniques such as canary deployments, blue/green deployments, and progressive rollouts limit the blast radius of a bad change. They reduce the chance you need to roll back. For deployment-strategy guidance, see [REL08-BP05 Deploy changes with automation](rel08-bp05.md). 

 Keep runbooks even in fully automated environments. They serve as the script for game days (see [REL12-BP05 Conduct game days regularly](rel12-bp05.md)), as the reference during audits, and as the fallback when automation is unavailable. Review runbooks as the workload and environment evolve, and update them with lessons from each incident and deployment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Document baseline procedures:** Capture the operational procedures you run today, such as deployments, patching, and configuration changes. For each one, record the ordered steps, the points where reliability could be affected, and the success criteria that confirm the procedure worked. 

1.  **Add validation and rollback to each runbook:** Define validation checkpoints that confirm the system reached the expected state at each stage. Write explicit rollback steps and the criteria that trigger them, so a person or automation knows when to reverse rather than proceed. 

1.  **Store runbooks under version control:** Keep runbooks and any infrastructure as code definitions in a source control system such as Git. Track changes over time so procedures can be reviewed, attributed, and reverted. 

1.  **Automate validated procedures progressively:** Convert stable manual runbooks into automation once you understand their failure modes. Use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to build and version runbooks. Systems Manager provides a first-class [Automation runbook](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) document type that pairs the concept of a runbook with executable automation. Define reversible infrastructure changes with [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). 

1.  **Enable self-service with access controls:** Publish reusable runbook templates for common procedures, and scope access with [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html). Define approval workflows for procedures that carry higher risk. 

1.  **Measure and improve:** Track deployment success and failure rates, recovery time when issues occur, and automation adoption. Run post-deployment reviews, and update runbooks as the environment evolves and as incidents reveal gaps. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL08-BP05 Deploy changes with automation](rel08-bp05.md) 
+  [REL08-BP02 Integrate functional testing as part of your deployment](rel08-bp02.md) 
+  [REL12-BP01 Use playbooks to investigate failures](rel12-bp01.md) 
+  [OPS05-BP01 Develop and test runbooks to perform procedures](ops05-bp01.md) 

 **Related documents:** 
+  [Ensuring rollback safety during deployments](https://builder.aws.com/content/3F04j2yRAAMBuPSPs50xwXZqg01/ensuring-rollback-safety-during-deployments) 
+  [Change Enablement in the Cloud - Change Enablement in the Cloud](https://docs.aws.amazon.com/wellarchitected/latest/change-enablement-in-the-cloud/change-enablement-in-the-cloud.html) 
+  [Building your Cloud Operating Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/introduction.html) 
+  [Infrastructure as code - Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) 
+  [Control CloudFormation access with AWS Identity and Access Management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html) 
+  [Creating your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 

 **Related tools:** 
+  [AWS Systems Manager change management tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-actions-and-change.html) 
+  [What is CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) 
+  [AWS Config](https://aws.amazon.com/config/) 