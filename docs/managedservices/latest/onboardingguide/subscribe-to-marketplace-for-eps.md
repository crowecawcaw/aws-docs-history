# Subscribe to AWS Marketplace for EPS

Recent changes to AMS endpoint security (EPS) require you to subscribe to TrendMicro Deep Security through the AWS Marketplace and accept the software terms.

TrendMicro offers two license models: Per Protected Instance Hour and Bring your own License (BYOL).

- **BYOL**:
  1.  You use your own license that you have purchased through external channels.
  2.  You must provide all the license keys to AMS to build the EPS infrastructure. You can provide an activation code that licenses all modules, or individual
      activation codes that license a certain set of modules. AMS creates only the license files that correspond with the activation codes you provide. Since the license
      activation occurs during onboarding, in the presence of an AMS lead engineer and CSDM, you can share that information then.
  3.  Additionally, you must subscribe to BYOL TrendMicro Market Place AMI Subscription. See
      [Trend Micro Deep Security (BYOL)](https://aws.amazon.com/marketplace/pp/B00OCI4H82/ref=dtl_recsim_B00OCI4J0I_B00OCI4H82_2 "https://aws.amazon.com/marketplace/pp/B00OCI4H82/ref=dtl_recsim_B00OCI4J0I_B00OCI4H82_2").

- **Per Protected Instance Hour**:

      1. In this subscription, you are not required to have any previously-procured Trend license.
      2. However, you must subscribe to the Marketplace subscription.
      3. No license key sharing with AMS is required in this model, as the Trend usage is metered automatically including the software license + EC2 infrastructure usage. See
       [Trend Micro Deep Security](https://aws.amazon.com/marketplace/pp/B01AVYHVHO "https://aws.amazon.com/marketplace/pp/B01AVYHVHO").

  To subscribe to Trend Micro, follow these steps:

1. Login into your AWS account.
2. Navigate to Trend Micro Deep Security ([BYOL](https://aws.amazon.com/marketplace/pp/B00OCI4H82/ref=dtl_recsim_B00OCI4J0I_B00OCI4H82_2 "https://aws.amazon.com/marketplace/pp/B00OCI4H82/ref=dtl_recsim_B00OCI4J0I_B00OCI4H82_2")
   or [Per Protected Instance Hour](https://aws.amazon.com/marketplace/pp/B01AVYHVHO "https://aws.amazon.com/marketplace/pp/B01AVYHVHO")) product page.
3. Click **Continue to Subscribe** in the right panel.
4. Click **Accept Terms** in the upper right corner.
   Next step: [Secure the new account with multi-factor authentication (MFA) for the root user in AMS](sog-secure-new-account-with-mfa.md "sog-secure-new-account-with-mfa.md")
