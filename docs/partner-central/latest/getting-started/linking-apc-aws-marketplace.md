# Linking AWS Partner Central and AWS

accounts

The following steps explain how to use AWS Partner Central to link your accounts. You must be
an alliance lead or cloud admin to complete these steps. Also, the IAM permissions policy listed earlier in
this guide controls the linking and role mapping tasks you and other AWS Partner Central users
can perform. For more information about those tasks, refer to [Granting IAM permissions](linking-prerequisites.md#grant-iam-permissions "linking-prerequisites.md#grant-iam-permissions").

For more information about account linking, refer to the [Account Linking User Guide](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources "https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources") in Partner Central.

###### Note

- AWS Partner Central uses the term _AWS Marketplace Account Linking_, but all
  partners can link accounts, including partners without AWS Marketplace accounts.
- Partners in Amazon Web Services India Private Limited (AWS India) can link without
  registering a business name.

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as an alliance lead or cloud admin.

###### Note

If your organization uses single sign-on (SSO), use those credentials to sign in to
your AWS account first, then sign in to AWS Partner Central. 2. In the **AWS Marketplace** section of the AWS Partner Central home page, choose
**Link Account**. 3. On the **AWS Marketplace Account linking** page, choose **Link
Account**. 4. On the AWS account sign-in page, choose **IAM user**. 5. Enter the ID of the AWS account and sign in.

###### Note

    * If you need account information, contact the administrator who completed the
     prerequisites listed above.
    * SSO users automatically skip to the next step.

6.  Navigate through the self-service linking experience:

        1. Review the AWS account ID and the associated AWS Marketplace seller profile legal name and
         choose **Next**.


        ###### Note

        If your AWS account is not registered as a seller, provide your legal business
         name to be registered on AWS Marketplace.

        Partners in Amazon Web Services India Private Limited (AWS India) can link without registering a business name. Proceed by choosing **Next**.
        2. Review the IAM roles and the managed policies attached to them, then choose
         **Next**.
        3. (Optional) To bulk map the IAM roles to the partner users with Alliance team and
         ACE partner roles, select the checkbox under each role section.


        A partner user cannot access AWS Marketplace features, such as linking private offers to ACE
         opportunities, without an IAM role mapped to their partner user account. If you
         choose not to bulk assign, you must manually map an IAM role to a partner user after
         linking the accounts.
        4. Review the information, then choose **Submit**.

    You are directed to AWS Partner Central with your account successfully linked and the
    default IAM roles created in your account.

7.  (Optional) To use custom policies that enable access to AWS Marketplace features within
    AWS Partner Central, refer to the next topic, [Using custom policies to map users](user-role-mapping.md "user-role-mapping.md").
