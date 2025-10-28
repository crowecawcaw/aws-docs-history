**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Choosing between an Amazon Chime Team account

or Enterprise account

When you create an Amazon Chime administrator account, you choose whether to create a Team
account or an Enterprise account. For more information about creating an Amazon Chime
administrator account, see [Getting started](getting-started.md "getting-started.md").

###### Team account

With a Team account, you can invite users and grant them Amazon Chime Pro permissions
without claiming an email domain. For more information about Pro and Basic
permissions, see [Plans and
pricing](https://aws.amazon.com/chime/pricing "https://aws.amazon.com/chime/pricing").

You can invite users from any email domain that hasn't been claimed by another
organization. You only pay for users when they host meetings. Users in your Team account
can use the Amazon Chime app to search for and contact other Amazon Chime users who are registered to
the same account. We also recommend a Team account for paying for Pro users outside of
your organization.

###### Enterprise account

With an Enterprise account, you have more control over the users from your
organization's domains. You can choose to connect to your own identity provider or
Okta SSO to authenticate and assign Pro or Basic permissions. Amazon Chime also supports
Microsoft Active Directory.

To create an Enterprise account, you must claim at least one email domain. This
ensures that all users who sign in to Amazon Chime using your claimed domains are included in
your centrally managed Amazon Chime account. Enterprise accounts are required for managing your
users through a supported directory integration. For more information, see [Claiming a domain](claim-domain.md "claim-domain.md") and [Connecting to your Active Directory](active_directory.md "active_directory.md").

You can also manage user activation and suspension from your Enterprise account. For
more information, see [Managing user permissions and access](manage-access.md "manage-access.md").
