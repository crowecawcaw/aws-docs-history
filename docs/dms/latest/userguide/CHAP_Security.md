# Opting out of using your data

for service improvement in AWS Database Migration Service

You can choose to opt out of having your data used to develop and improve AWS DMS by
using the AWS Organizations opt-out policy. You can choose to opt out even if
AWS DMS does not currently collect any such data. For more information, see [AI services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User Guide_.

Presently, AWS Database Migration Service (AWS DMS) does not collect any of the data that it processes on
your behalf. To develop and improve DMS and the functionalities of other AWS
services, DMS may collect such data in the future. We will update this documentation
page when DMS is configured to collect any data. You will have an option to opt out
at any time.

###### Note

For you to use the opt-out policy, your AWS accounts must be centrally
managed by AWS Organizations. If you have not created an organization for your
AWS accounts, see [Managing an
organization with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User Guide_.

Opting out has the following effects:

- AWS DMS deletes the data that it collected and stored for service
  improvement purposes prior to your opt out (if any).
- After you opt out, AWS DMS no longer collect or store this data for service
  improvement purposes.
