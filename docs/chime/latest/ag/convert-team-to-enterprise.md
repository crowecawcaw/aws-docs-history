**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Converting a Team account to an Enterprise

account

To convert an existing Team account to an Enterprise account, claim one or more email
domains in the Amazon Chime console. For more information about the differences between Team
and Enterprise accounts, see [Choosing between an Amazon Chime Team account
or Enterprise account](choose-team-enterprise-account.md "choose-team-enterprise-account.md"). For more information about
claiming a domain, see [Claiming a domain](claim-domain.md "claim-domain.md").

###### To convert a Team account to an Enterprise account

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. For **Accounts**, choose the name of the
   account.
3. For **Identity**, choose **Getting Started**.
4. Follow the steps in the console to claim your domain.
5. (Optional) Follow the steps in the console to set up your identity
   provider and configure your directory group.
   After your account is converted to an Enterprise account, you can decide whether to
   connect an Active Directory instance through AWS Directory Service. Connecting to an Active Directory
   instance allows your users to sign in to Amazon Chime using their Active Directory credentials.
   For more information, see [Connecting to your Active Directory](active_directory.md "active_directory.md").

If you don't connect to an Active Directory instance, your users can continue to sign
in to Amazon Chime using Login with Amazon (LWA) or their Amazon.com account
credentials.
