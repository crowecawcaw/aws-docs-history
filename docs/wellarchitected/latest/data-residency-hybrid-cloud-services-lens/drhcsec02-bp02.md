

# DRHCSEC02-BP02 Manage workloads with similar data residency requirements efficiently
<a name="drhcsec02-bp02"></a>

 When there are at least some control policies applicable to more than one account, configuring those accounts to be with the same Organizational Units (OUs) then applying the Service control policies (SCPs) at the OU level is more efficient than applying to each account, and much better than duplicating the policy statements into multiple SCPs. 

 **Desired outcome:** Service control policies (SCPs) for data residency are deployed without unnecessary duplication. 

 **Common anti-patterns:** 
+  SCPs are attached directly to multiple accounts 
+  You have duplicated statements in multiple SCPs 

 **Benefits of establishing this best practice**: Lowers cost of development and testing of preventative controls by minimizing duplication 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-19"></a>

1.  Identify accounts with overlapping data residency requirements. The most relevant details are requirements that can be enforced with SCPs. 

1.  If there are relevant requirements that apply to a smaller subset than others, then it may be appropriate to create nested Organizational Units (OUs). However, when you create a nesting like this, you should factor in other business requirements for OU nesting, as well as AWS Organizations' service limit of five nested OU levels under a root. 

1.  Create OUs that match your grouping of overlapping data residency requirements. 

1.  Move your accounts into the relevant OU. 

1.  Attach SCPs at the OU level to minimize the overhead of applying them at account level, which also reduces risk of failing to apply the policies to new accounts. 

## Resources
<a name="resources-5"></a>

 **Related best practices:** 
+  [SEC01-BP01 Separate workloads using accounts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_multi_accounts.htmltest/framework/a-identity-and-access-management.html) 

 **Related documentation:** 
+  [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 
+  [Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/) 
+  [Identity and Access Management](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-identity-and-access-management.html) 