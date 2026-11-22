

# Multi-account environment

 A well-structured multi-account environment is the starting point for a secure, well-governed cloud. Accounts are the strongest isolation boundary AWS provides, so how you structure them shapes your security posture, your ability to apply policy at scale, and how clearly costs and ownership map to the people responsible. This capability covers the best practices for setting up and managing that structure. 


|  FND01: How do you structure and govern multiple accounts across teams and environments?  | 
| --- | 
|  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md)  | 
|  [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md)  | 
|  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md)  | 
|  [FND01-BP04 Establish a strategy for experimental and temporary environments](fnd01-bp04.md)  | 

## Capability intent
<a name="fnd01-intent"></a>
+  Accounts are grouped so that isolation boundaries match security, operational, and lifecycle needs rather than reporting lines, and the management account is used only for governance. 
+  Administrative capabilities are delegated from the management account to an appropriate member account wherever the service supports it. 
+  Guardrails applied at the organization and organizational unit level reach every account beneath them through inheritance, so controls are applied consistently and can be managed from one place. 
+  New accounts arrive with consistent baselines for security and compliance logging, identity, networking, and cost controls, and those baselines are applied by automation rather than by a runbook. 
+  Every account and significant resource has a current, named owner for billing, security, and operational response, recorded in account and resource tags as a role or team rather than an individual, so automation and incident response can rely on it. 
+  Experimentation, pre-production, and production sit in clearly separated environments with progressively tighter access restrictions, expressed as permission sets in IAM Identity Center, so teams can try new services and run destructive tests without endangering customer-facing workloads or the shape of the organization itself. 
+  Controls are applied consistently across the lifecycle environments of a workload, so a change that deploys successfully in a lower environment does not fail in production because the controls differ. 

## Common issues to watch for
<a name="fnd01-issues"></a>
+  Production workloads run in the management account, expanding the scope of impact of any mistake or unintended access to the whole organization and entangling billing administration with day-to-day engineering. 
+  OU structure mirrors the organization chart rather than security and operational boundaries, so policy inheritance does not match the risk profile of the accounts beneath it and restructuring is needed every time the business reorganizes. 
+  Alternate contacts point to individuals rather than distribution lists, so when those individuals move on, AWS abuse reports, security notifications, and billing warnings go to unattended inboxes. 
+  Tagging is inconsistent or enforced only by convention, which quietly breaks cost allocation, tag-based access controls, and incident routing long before anyone notices the tags are wrong. 
+  New accounts are created by hand, producing a long tail of accounts with missing logging, drifted network configuration, or inconsistent identity setup that remediation programs then have to chase. 
+  There is no first-class path for experimentation or short-lived work, so teams either test in shared development accounts and production or stand up shadow accounts outside governance to move faster. 