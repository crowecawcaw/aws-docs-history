

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# AWS Firewall Manager integration with AWS Security Hub CSPM
<a name="fms-findings"></a>

This page explains how to use Firewall Manager and Security Hub CSPM together.

AWS Firewall Manager creates findings for resources that are out of compliance and for attacks that it detects, and it sends them to AWS Security Hub CSPM. For information about Security Hub CSPM findings, see [Findings in AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings.html).

When you use Security Hub CSPM and Firewall Manager, Firewall Manager automatically sends your findings to Security Hub CSPM. For information about getting started with Security Hub CSPM, see [Setting Up AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the [AWS Security Hub CSPM User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html).

**Note**  
Firewall Manager only updates findings for policies that are under its management and for resources that it's monitoring.   
Firewall Manager doesn't resolve findings for the following:   
Policies that have been deleted.
Resources that have been deleted.
Resources that have gone out of scope of the Firewall Manager policy, for example due to tag change or policy definition change.

**How do I view my Firewall Manager findings?**  
To view your Firewall Manager findings in Security Hub CSPM, follow the guidance at [Working with Findings in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings.html#securityhub-managing-findings) and create a filter using the following settings: 
+ Attribute set to **Product Name**.
+ Operator set to **EQUALS**.
+ Value set to `Firewall Manager`. This setting is case sensitive.

**Can I disable this?**  
You can disable the integration of AWS Firewall Manager findings with Security Hub CSPM through the Security Hub CSPM console. Choose **Integrations** in the navigation bar, then in the Firewall Manager pane, choose **Disable Integration**. For more information, see the [AWS Security Hub CSPM User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html).

**Topics**
+ [AWS WAF policy Firewall Manager findings](waf-policy-findings.md)
+ [AWS Shield Advanced policy Firewall Manager findings](shield-policy-findings.md)
+ [Security group common policy Firewall Manager findings](security-group-common-policy-findings.md)
+ [Security group content audit policy Firewall Manager findings](security-group-content-audit-policy-findings.md)
+ [Security group usage audit policy Firewall Manager findings](security-group-usage-audit-policy-findings.md)
+ [Amazon Route 53 Resolver DNS Firewall policy Firewall Manager findings](dns-firewall-policy-findings.md)
+ [AWS Config Firewall Manager findings](aws-config-firewall-manager-findings.md)