**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Getting started with AWS Firewall Manager to enable AWS WAF Classic

rules

###### Warning

AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

###### Note

This is **AWS WAF Classic** documentation. You should only
use this version if you created AWS WAF
resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not
migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md "waf-migrating-from-classic.md").

**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md "waf-chapter.md").

You can use AWS Firewall Manager to enable AWS WAF rules, AWS WAF Classic rules, AWS Shield Advanced
protections, and Amazon VPC security groups. The steps for getting set up are slightly different for
each:

- To use Firewall Manager to enable rules using the latest version of AWS WAF, don't use this topic.
  Instead, follow the steps in [Setting up AWS Firewall Manager​ AWS WAF policies](getting-started-fms.md "getting-started-fms.md").
- To use Firewall Manager to enable AWS Shield Advanced protections, follow the steps in [Setting up AWS Firewall Manager​ AWS Shield Advanced policies](getting-started-fms-shield.md "getting-started-fms-shield.md").
- To use Firewall Manager to enable Amazon VPC security groups, follow the steps in [Setting up AWS Firewall Manager​ Amazon VPC security
  group policies](getting-started-fms-security-group.md "getting-started-fms-security-group.md").
  To use Firewall Manager to enable AWS WAF Classic rules, perform the following steps in sequence.

###### Topics

- [Step 1: Complete the prerequisites](classic-complete-prereq.md "classic-complete-prereq.md")
- [Step 2: Create rules](classic-get-started-fms-create-rules.md "classic-get-started-fms-create-rules.md")
- [Step 3: Create a rule group](classic-get-started-fms-create-rule-group.md "classic-get-started-fms-create-rule-group.md")
- [Step 4: Create and apply an AWS Firewall ManagerAWS WAF Classic policy](classic-get-started-fms-create-security-policy.md "classic-get-started-fms-create-security-policy.md")
