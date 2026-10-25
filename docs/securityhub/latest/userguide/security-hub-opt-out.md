

# Opting out of using your data for service improvement
<a name="security-hub-opt-out"></a>

**Note**  
 This documentation page is only applicable to the enhanced AWS Security Hub launched on December 2, 2025. If you are a customer of the original AWS Security Hub (now AWS Security Hub CSPM), the data usage described below will apply only after you have enabled the enhanced AWS Security Hub. 

 You can choose to opt out of having your data (defined as "Security Hub Content" in the Security Hub service terms) used to develop and improve AWS Security Hub and other AWS security services by using the AWS Organizations opt-out policy. For more information about how to opt out, see [AI services opt-out policies](orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*. 

**Note**  
For you to use the opt-out policy, your AWS accounts must be centrally managed by AWS Organizations. If you haven't already created an organization for your AWS accounts, see [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.

Opting out has the following effects:
+ Security Hub will delete the Content that it collected and stored for service improvement purposes prior to your opt out (if any).
+ After you opt out, Security Hub will no longer collect or store this Content for service improvement purposes.

The following section explains how Security Hub uses your Content for service improvement.

## AWS Security Hub data usage
<a name="security-hub-data-usage"></a>

AWS Security Hub collects and uses the following categories of Security Hub Content to develop and improve exposure findings and resource criticality inference:
+ Third-party security findings that you aggregate in Security Hub from partner products or external integrations
+ Resource configuration data for resources in other cloud environments, such as Microsoft Azure, that you integrate with Security Hub
+ Software inventory data for your resources, such as the software bill of materials (SBOM) that Amazon Inspector collects and that is available in Security Hub

For information about how Security Hub uses data to provide the capabilities that you enable, see [How Security Hub uses data to provide the capabilities you enable](securityhub-v2-data-use.md).

Your trust, privacy, and the security of your Content are our highest priority. You can opt out of this Security Hub Content collection at any time using the AWS Organizations opt-out policy described above. For more information about AWS data privacy practices, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).

## References
<a name="security-hub-opt-out-references"></a>

For similar opt-out procedures in other AWS security services, see:
+  [Opting out of using your data for service improvement ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-opting-out-using-data.html)in the *Amazon GuardDuty User Guide*.
+  [Opting out of using your data for service improvement ](https://docs.aws.amazon.com/security-lake/latest/userguide/opting-out-of-using-your-data.html)in the *Amazon Security Lake User Guide*.