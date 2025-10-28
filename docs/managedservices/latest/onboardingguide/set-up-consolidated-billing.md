# Set up consolidated billing–link new account to Payer account

If you'd like your new AMS-managed AWS account bill to be rolled into a payment for an existing AWS Organizations management account, you need to set up
consolidated billing and link the accounts. For details on doing this, see

- [Consolidated billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md") and
  [AWS Multi-Account Billing Strategy](https://d0.awsstatic.com/aws-answers/AWS_Multi_Account_Billing_Strategy.pdf "https://d0.awsstatic.com/aws-answers/AWS_Multi_Account_Billing_Strategy.pdf").
- [Inviting an AWS account to join your organization](../../../organizations/latest/userguide/orgs_manage_accounts_invites.md "../../../organizations/latest/userguide/orgs_manage_accounts_invites.md")

###### Note

You can perform these steps before doing the account handover to AMS. After the handover, the steps for joining your organization (provided above) can be
done through the change management process. Consult with your cloud service deliver manager (CSDM) or cloud architect (CA) if you need assistance.

For general billing information including managing consolidated billing, see
[What is AWS Billing](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
For general AWS Organizations information about how accounts can work together, see
[What is AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").
For prescriptive guidance on AWS Organizations management accounts, see
[The management account, trusted access, and delegated administrators](../../../prescriptive-guidance/latest/security-reference-architecture/management-account.md "../../../prescriptive-guidance/latest/security-reference-architecture/management-account.md")
