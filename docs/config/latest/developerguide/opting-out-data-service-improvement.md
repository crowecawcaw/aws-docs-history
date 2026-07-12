# Opting out of using your data for service improvement

You can choose to opt out of having your data (defined as "Config Content" in the AWS Config
service terms) used to develop and improve AWS Config and related AWS security and observability
services by using the AWS Organizations opt-out policy. You can choose to opt out even if
AWS Config doesn't currently collect any such Content. For more information about how to opt out,
see [AI
services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User
Guide_.

###### Note

For you to use the opt-out policy, your AWS accounts must be centrally managed by
AWS Organizations. If you haven't already created an organization for your AWS accounts,
see [Creating
and managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User
Guide_.

Opting out has the following effects:

- AWS Config will delete the Content that it collected and stored for service improvement
  purposes prior to your opt out (if any).
- After you opt out, AWS Config will no longer collect or store this Content for service
  improvement purposes.
  The following section explains how AWS Config will handle your Content for service
  improvement.

## AWS Config data usage

Currently, AWS Config does not collect or store any Config Content for service improvement
purposes. However, in the future, AWS Config may collect and use third-party resource
configuration data processed by Config in connection with third-party recorders to
improve AWS Config and other related AWS security and observability service
capabilities.

Your trust, privacy, and the security of your Content are our highest priority. If
AWS Config begins collecting Config Content for service improvement purposes in the future,
this page will be updated to reflect those changes and provide details about what data is
collected and how it is used. You can opt out of this Config Content collection at any
time using the AWS Organizations opt-out policy described above. For more information
about AWS data privacy practices, see [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

## References

For similar opt-out procedures in other AWS security services, see:

- [Opting out of using your data for service improvement](../../../guardduty/latest/ug/guardduty-opting-out-using-data.md "../../../guardduty/latest/ug/guardduty-opting-out-using-data.md") in the
  _Amazon GuardDuty User Guide_.
- [Opting out of using your data for service improvement](../../../security-lake/latest/userguide/opting-out-of-using-your-data.md "../../../security-lake/latest/userguide/opting-out-of-using-your-data.md") in the
  _Amazon Security Lake User Guide_.
- [Opting out of using your data for service improvement](../../../securityhub/latest/userguide/security-hub-opt-out.md "../../../securityhub/latest/userguide/security-hub-opt-out.md") in the
  _AWS Security Hub User Guide_.
