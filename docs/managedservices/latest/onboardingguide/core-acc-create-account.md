# Create an AWS multi-account landing zone core account in AMS

AMS multi-account landing zone requires the provisioning of a new Amazon Web Services (AWS) account to act as the management account in the AMS multi-account landing zone
environment. To create an AWS account, follow these step-by-step instructions:
[How do I create and activate a new Amazon Web Services account?](https://aws.amazon.com//premiumsupport/knowledge-center/create-and-activate-aws-account/ "https://aws.amazon.com//premiumsupport/knowledge-center/create-and-activate-aws-account/")

The simple steps are:
Go to [Create Account](https://aws.amazon.com/resources/create-account/ "https://aws.amazon.com/resources/create-account/"), and click **Sign Up Now** and, on the page that opens, click
**Create a new AWS account**. Follow the on-screen instructions, which include receiving a phone call and entering a PIN using your phone keypad.
You'll also need to enter a credit card. AMS uses this account as the management account, or payer account, for your new multi-account landing zone.

###### Note

Once you are onboarded, talk to your cloud service delivery manager (CSDM) about moving billing off of your credit card and onto an invoice system.
The following information will be required:

- Billing Company Name
- Billing Contact Name
- Billing Contact Phone Number
- Billing Contact Email
- Billing Address
  Your CSDM will help you with this update. Once completed, and to change the payment method, see
  [Managing your AWS payment methods](../../../awsaccountbilling/latest/aboutv2/manage-payment-method.md "../../../awsaccountbilling/latest/aboutv2/manage-payment-method.md").

###### Note

Do not link your new account to an existing management account, or payer account.

Ensure that your account is not part of an existing AWS Organizations; for information, see
[What Is AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")

###### Important

It is very important that you ensure that an **email address** (a distribution list, not an individual's email address)
and **phone number** are associated with the account so that you receive responses to potential security incidents. The phone number and
email address for the account cannot be changed without resetting the account password, which is a significant undertaking for an AMS
root account. To ensure that these values are stable, _it is critical to select contact information not associated with individuals_, which
can change. Choose an email alias that can point to a group. Follow this same practice in selecting a phone number: choose a number
that can point to a group or to a number owned by the company and not an individual.

For details on the questions you will be asked to onboard your Core account to AMS multi-account landing zone, see
[Appendix: multi-account landing zone (MALZ) onboarding consideration list](apx-malz-questions.md "apx-malz-questions.md").
