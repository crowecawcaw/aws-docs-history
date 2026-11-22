

# OPS05-BP01 Develop and test runbooks to perform procedures

 A runbook is a documented procedure that produces the same outcome every time, no matter who runs it. Teams use runbooks for routine and high-stakes work, from onboarding an engineer to deploying a release or recovering from an incident. Without them, operations depend on memory and habit, which produces inconsistent results and more errors. 

 **Desired outcome:** 
+  Your team maintains a library of step-by-step runbooks, each stating a desired outcome, the required tools and permissions, and the error-handling and escalation path. 
+  Your runbooks live in a central, version-controlled location that all team members can find and use. 
+  Your runbook content stays current because updates follow your change management process as procedures evolve. 
+  You automate your frequently used runbooks, so routine work runs consistently with little manual effort. 

 **Common anti-patterns:** 
+  Team members rely on memory to complete each step of a recurring process. 
+  Engineers deploy changes manually without a checklist or documented procedure. 
+  Two people perform the same task and produce different results because the steps are undocumented. 
+  Runbooks drift out of sync with the systems and automation they describe. 

 **Benefits of establishing this best practice:** 
+  Manual tasks produce fewer errors because every step is written down and validated. 
+  Operations run consistently no matter who performs them. 
+  New team members become productive sooner by following documented procedures. 
+  Automating runbooks reduces repetitive manual work and frees engineers for higher-value tasks. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When you create a runbook, state the desired outcome first, then list the tools, permissions, and steps needed to reach it. Name an owner so responsibility for keeping the runbook current is clear. 

 Start with text runbooks and plan to automate. Every manual run is a chance for a skipped or misread step, so automating short, frequently used procedures first returns the investment quickly and builds the skill to automate harder cases. Keep judgment calls, rare procedures, and steps that need human approval manual while you automate the repetitive core. 

 Drift is common, as the system and automation might change while the runbook does not and someone follows the stale version during an incident. Tie runbook updates to your change management process to keep them current. Include error handling for when a step fails and an escalation path for when the procedure cannot resolve the problem. 

 Runbooks and playbooks pair together but solve different problems. A runbook executes a known procedure to reach a known outcome. A playbook guides investigation when the outcome is not yet known, such as diagnosing why a deployment failed. When a playbook identifies a root cause, it points to the runbook that resolves it. Keep the two separate so a runbook does not become an open-ended troubleshooting guide. 

 On AWS, use [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to turn documented procedures into automation runbooks that run against your workload, on demand or in response to events. Use the low-code [visual design experience](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-visual-designer.html) to build them. For common operational issues, Support maintains [Support self-service runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-support-runbooks.html) that troubleshoot resources, monitor for network issues, and collect logs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose a central repository:** Use your existing documentation wiki or version control system as the home for your runbook library. Version control gives you history, review, and rollback for procedures, and a single known location stops copies from drifting apart. Create a new repository only if no suitable store exists. 

1.  **Select a procedure to document first:** Pick a process that runs semi-regularly, has a small number of steps, and fails with low impact. Starting small builds the habit and the template before you tackle recovery or deployment procedures where mistakes are costly. 

1.  **Draft the runbook from a standard template:** Create a document from a shared template so every runbook records the same structure and metadata. Fill in the title, the runbook info, and each step in order. Keeping the runbook in Markdown makes it portable across most automation systems. 

   ```markdown
   # Runbook title
   ## Runbook info
   | Runbook ID | Description | Tools used | Special permissions | Author | Last updated | Escalation contact |
   |---|---|---|---|---|---|---|
   | RUN001 | What is this runbook for and what outcome does it produce? | Tools | Permissions | Your name | 2026-01-01 | Escalation name |
   ## Steps
   1. Step one
   2. Step two
   ```

1.  **Validate the runbook with a peer:** Give the draft to a team member who did not write it and have them perform the procedure using only the written steps. Update anything that is missing, ambiguous, or out of order. This confirms the runbook works without the author present. 

1.  **Publish and announce the runbook:** Publish the validated runbook to your central store and tell your team and stakeholders where to find it. Record the owner so responsibility for keeping it current is clear. 

1.  **Automate mature runbooks:** As your library grows, convert stable, frequently used text runbooks into automation with [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). The low-code [visual design experience](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-visual-designer.html) helps you build automation runbooks, and you can run them in response to events to reduce manual effort. Keep the automated version and its documentation in sync. [Kiro](https://kiro.dev/) can be used accelerate the development of runbooks and help to keep the documentation consistent. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) 
+  [OPS06-BP02 Automate responses to events](ops06-bp02.md) 
+  [OPS07-BP03 Perform knowledge management](ops07-bp03.md) 

 **Related documents:** 
+  [AWS Systems Manager: Working with runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [Use Automation runbooks to remediate application issues](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-runbooks.html) 
+  [Support self-service runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-support-runbooks.html) 
+  [Migration playbook for AWS large migrations - Task 4: Improving your migration runbooks](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-migration-playbook/task-four-migration-runbooks.html) 
+  [Use AWS Systems Manager Automation runbooks to resolve operational tasks](https://aws.amazon.com/blogs/mt/use-aws-systems-manager-automation-runbooks-to-resolve-operational-tasks/) 
+  [Achieving operational excellence using automated playbook and runbook](https://aws.amazon.com/blogs/mt/achieving-operational-excellence-using-automated-playbook-and-runbook/) 
+  [Generating Operational Runbooks with Kiro: A Practical Guide for SREs](https://builder.aws.com/content/3BwfBZFrDhkdkreoBmmTQsP0z2D/generating-operational-runbooks-with-kiro-a-practical-guide-for-sres) 

 **Related examples:** 
+  [AWS Systems Manager: Automation walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorials.html) 
+  [AWS Systems Manager: Restore a root volume from the latest snapshot runbook](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-instance-recovery-example.html) 
+  [Build AWS Systems Manager Automation runbooks using AWS CDK](https://aws.amazon.com/blogs/mt/build-aws-systems-manager-automation-runbooks-using-aws-cdk/) 
+  [Using Document Builder to create a custom runbook](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-builder.html) 
+  [GitLab - Runbooks](https://gitlab.com/gitlab-com/runbooks) 
+  [Rubix - a Python library for building runbooks in Jupyter notebooks](https://github.com/Nurtch/rubix) 

 **Related services:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [Kiro](https://kiro.dev/) 