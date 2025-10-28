**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS Firewall Manager integration with AWS Security Hub

This page explains how to use Firewall Manager and Security Hub together.

AWS Firewall Manager creates findings for resources that are out of compliance and for attacks that it
detects, and it sends them to AWS Security Hub. For information about Security Hub findings, see [Findings in AWS Security Hub](../../../securityhub/latest/userguide/securityhub-findings.md "../../../securityhub/latest/userguide/securityhub-findings.md").

When you use Security Hub and Firewall Manager, Firewall Manager automatically sends your findings to Security Hub. For
information about getting started with Security Hub, see [Setting Up
AWS Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the [AWS Security Hub User
Guide](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md").

###### Note

Firewall Manager only updates findings for policies that are under its management and for resources that it's monitoring.

Firewall Manager doesn't resolve findings for the following:

- Policies that have been deleted.
- Resources that have been deleted.
- Resources that have gone out of scope of the Firewall Manager policy, for example due to tag change or policy definition change.

###### How do I view my Firewall Manager findings?

To view your Firewall Manager findings in Security Hub, follow the guidance at [Working with Findings in Security Hub](../../../securityhub/latest/userguide/securityhub-findings.md#securityhub-managing-findings "../../../securityhub/latest/userguide/securityhub-findings.md#securityhub-managing-findings") and create a filter using the
following settings:

- Attribute set to **Product Name**.
- Operator set to **EQUALS**.
- Value set to `Firewall Manager`. This setting is case sensitive.

###### Can I disable this?

You can disable the integration of AWS Firewall Manager findings with Security Hub through the Security Hub console. Choose **Integrations** in the navigation bar, then in the Firewall Manager pane, choose **Disable Integration**. For more information, see the [AWS Security Hub User
Guide](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md").

###### AWS Firewall Manager finding types

- [AWS WAF policy Firewall Manager findings](waf-policy-findings.md "waf-policy-findings.md")
- [AWS Shield Advanced policy Firewall Manager findings](shield-policy-findings.md "shield-policy-findings.md")
- [Security group common policy Firewall Manager findings](security-group-common-policy-findings.md "security-group-common-policy-findings.md")
- [Security group content audit policy Firewall Manager findings](security-group-content-audit-policy-findings.md "security-group-content-audit-policy-findings.md")
- [Security group usage audit policy Firewall Manager findings](security-group-usage-audit-policy-findings.md "security-group-usage-audit-policy-findings.md")
- [Amazon Route 53 Resolver DNS Firewall policy Firewall Manager findings](dns-firewall-policy-findings.md "dns-firewall-policy-findings.md")
- [AWS Config Firewall Manager findings](aws-config-firewall-manager-findings.md "aws-config-firewall-manager-findings.md")
