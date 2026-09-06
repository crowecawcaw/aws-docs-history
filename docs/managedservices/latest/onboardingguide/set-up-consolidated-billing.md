

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Set up consolidated billing–link new account to Payer account
<a name="set-up-consolidated-billing"></a>

If you'd like your new AMS-managed AWS account bill to be rolled into a payment for an existing AWS Organizations management account, you need to set up consolidated billing and link the accounts. For details on doing this, see
+  [Consolidated billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) and [AWS Multi-Account Billing Strategy](https://d0.awsstatic.com/aws-answers/AWS_Multi_Account_Billing_Strategy.pdf).
+  [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html)

**Note**  
You can perform these steps before doing the account handover to AMS. After the handover, the steps for joining your organization (provided above) can be done through the change management process. Consult with your cloud service deliver manager (CSDM) or cloud architect (CA) if you need assistance.

For general billing information including managing consolidated billing, see [What is AWS Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html). For general AWS Organizations information about how accounts can work together, see [What is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). For prescriptive guidance on AWS Organizations management accounts, see [The management account, trusted access, and delegated administrators](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/management-account.html)