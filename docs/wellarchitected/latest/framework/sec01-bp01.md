

# SEC01-BP01 Separate workloads using accounts

 An account is the strongest isolation boundary available to you. When you group unrelated workloads in a single account, a mistake or unauthorized access in one workload can reach the others. Separating workloads by environment and business criticality limits how far that reach extends, clarifies ownership, and makes cost and access boundaries explicit. 

 **Desired outcome:** 
+  Your workloads run in separate accounts organized by environment and business criticality, so a failure or unauthorized access in one cannot reach another. 
+  You create accounts through a repeatable vending process that applies a security baseline before any workload is deployed. 
+  Your cost, access, and operational boundaries follow account lines, which makes ownership and reporting unambiguous. 
+  You know which organization-level controls apply to each account type, and you have validated your workload against them. 

 **Common anti-patterns:** 
+  Teams host multiple unrelated workloads in a single account. 
+  Development, staging, and production share one account, so a change in one environment affects the others. 
+  New accounts are created manually, bypassing the standard vending process and its baseline controls. 
+  One account is shared across several application teams or business units, which blurs ownership. 
+  Workload teams rebuild capabilities such as logging or identity that a central foundation already provides. 

 **Benefits of establishing this best practice:** 
+  A security incident in one workload stays contained, because the account boundary limits what a credential under unauthorized control can reach. 
+  Sensitive data and business-critical applications gain a hard boundary that separates them from lower-trust workloads. 
+  Cost tracking and chargeback become straightforward, because spend maps directly to an account and its owner. 
+  Compliance scope narrows per account, which simplifies auditing and evidence collection. 
+  Consistent baseline controls apply automatically to every new account. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The account is the highest-order isolation boundary in AWS. Resources in one account cannot access resources in another unless you deliberately grant that access. This property makes the account the natural unit for separating things that should not affect each other, such as production from development, a regulated workload from an experimental one, one business unit from another. Identity, network, and policy boundaries reinforce the account boundary, so a design that starts from accounts gives you defense in depth. 

 When you have too few accounts, you lose isolation, blur cost ownership, and force conflicting controls onto the same set of resources. On the other hand, too many accounts creates management overhead that a small team cannot sustain. Group accounts by environment (for example, development, testing, staging, and production) and by business criticality or data sensitivity. Each account then holds resources with similar security and operational requirements. This is the pattern described in [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html), which maps accounts to organizational units under [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html). 

 When someone manually creates an account, the baseline controls that protect every other account, such as centralized logging, guardrails, and network configuration, are easy to forget. *Account vending* replaces manual creation with a repeatable, governed process that applies an approved baseline before the account is handed to a team. [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) provisions accounts with pre-approved configurations your organization sets. An infrastructure or security team typically owns the vending process and the baseline, while workload teams request accounts and operate within the controls they inherit. 

 Different account types carry different controls. A production account that holds confidential data might enforce restrictions a sandbox account does not. These organization-level controls affect what your workload can do, so you cannot assume an application behaves identically across environments. Understand which controls apply to each account type and data classification, and validate your workload in each environment. Where a central foundation already provides a capability such as log aggregation or a security information and event management (SIEM) feed, integrate with it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess your workload requirements:** Review your workload characteristics and classify its data according to your organization's data classification standards. Document application dependencies and shared resources, and determine which environments the workload needs based on your account strategy. 

1.  **Request accounts through the vending process:** Submit account requests through your organization's vending process, specifying environment type, data classification, and compliance requirements. Review the baseline configuration that each account type applies so you know which controls you inherit. 

1.  **Integrate with centralized tooling:** Connect the workload to the centralized logging and monitoring solutions your organization provides, and confirm that your logging feeds any SIEM or security analytics systems it manages. 

1.  **Establish ownership and cost management:** Apply your required resource tagging strategy, and configure budget alerts for each account so owners stay aware of spend against plan. 

1.  **Test and validate across environments:** Deploy and test the workload in each environment to confirm it behaves as intended, and identify where organization-level controls change its behavior. 

1.  **Review and communicate on a cadence:** Review account configurations against your organization's evolving standards on a regular schedule, and share feedback and new requirements with the teams that own shared dependencies. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP04 Reduce security management scope](sec01-bp04.md) 
+  [SEC01-BP05 Automate deployment of standard security controls](sec01-bp05.md) 
+  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md) 

 **Related documents:** 
+  [AWS multi-account strategy for your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html) 
+  [Benefits of using multiple AWS accounts](https://docs.aws.amazon.com/accounts/latest/reference/welcome-multiple-accounts.html) 
+  [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/) 

 **Related videos:** 
+  [Multi Account Structure in AWS with AWS Organizations](https://www.youtube.com/watch?v=6CBfz0ZdbQM) 
+  [Back to Basics: Design Patterns for Building AWS Multi-Account Organization](https://www.youtube.com/watch?v=ubdJlHrxlXE) 