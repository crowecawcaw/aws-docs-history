# Opting out of using your data for service improvement

###### Note

This documentation page is only applicable to the enhanced AWS Security Hub launched on December 2, 2025.
If you are a customer of the original AWS Security Hub (now AWS Security Hub CSPM), the data usage described below will apply only after you have enabled the enhanced AWS Security Hub.

You can choose to opt out of having your data (defined as "Security Hub Content" in the Security Hub service terms) used to develop and improve AWS Security Hub and other AWS security services by using the AWS Organizations opt-out policy.
You can choose to opt out even if Security Hub doesn't currently collect any such Content.
For more information about how to opt out, see [AI services opt-out policies](orgs_manage_policies_ai-opt-out.md "orgs_manage_policies_ai-opt-out.md") in the .

###### Note

For you to use the opt-out policy, your AWS accounts must be centrally managed by AWS Organizations.
If you haven't already created an organization for your AWS accounts, see [Creating and managing an organization](orgs_manage_org.md "orgs_manage_org.md") in the .

Opting out has the following effects:

- Security Hub will delete the Content that it collected and stored for service improvement purposes prior to your opt out (if any).
- After you opt out, Security Hub will no longer collect or store this Content for service improvement purposes.
  The following section explains how Security Hub will handle your content for service improvement.

## AWS Security Hub data usage

Currently, AWS Security Hub does not collect or store any Security Hub Content for service improvement purposes.
However, in the future, Security Hub may collect and use third-party security findings that you aggregate in Security Hub and other forms of Security Hub Content (that Security Hub receives from you or upstream services for purposes of providing Security Hub capabilities) to improve Security Hub and other AWS security service capabilities.

Your trust, privacy, and the security of your Content are our highest priority.
If Security Hub begins collecting Security Hub Content for service improvement purposes in the future, this page will be updated to reflect those changes and provide details about what data is collected and how it is used.
You can opt out of this Security Hub Content collection at any time using the AWS Organizations opt-out policy described above.
For more information about AWS data privacy practices, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

## References

For similar opt-out procedures in other AWS security services, see:

- [Opting out of using your data for service improvement](../../../guardduty/latest/ug/guardduty-opting-out-using-data.md "../../../guardduty/latest/ug/guardduty-opting-out-using-data.md") in the _Amazon GuardDuty User Guide_.
- [Opting out of using your data for service improvement](../../../security-lake/latest/userguide/opting-out-of-using-your-data.md "../../../security-lake/latest/userguide/opting-out-of-using-your-data.md") in the _Amazon Security Lake User Guide;_.
