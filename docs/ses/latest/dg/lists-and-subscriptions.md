# Managing lists and subscriptions in

Amazon Simple Email Service

You can manage your own lists for mailing and subscriptions as well as for email
suppression in Amazon SES. To help you maintain your sender reputation, SES offers
account-level and configuration set-level suppression that prevents you from sending to
invalid recipients and harming your sender reputation. As another measure against bounced
emails and complaints, SES can automatically add unsubscribe links to all outgoing
mail through subscription management.

Each of these types of lists is discussed in detail in the sections listed in this
chapter's topics; however, an overview of suppression lists is presented here to understand
how they differ as well as a key change with global suppression list management. It's
suggested that you read this overview before working with any of the lists discussed in this
chapter.

###### Overview of suppression lists and suppression

override mechanism

The global suppression list removal feature is no longer customer facing and you no
longer interact with it to manage suppression. The global suppression list operates and
is managed in the background by SES. As a customer, you now have available to you
an account-level suppression list and configuration set-level suppression overrides that
offer you more customized control over how you handle email suppression for your own
account.

The different types of suppression lists, their scope, and what advantages they offer is
explained below.

- Global suppression list – Owned and managed
  by SES to protect the reputation of addresses in the SES shared IP
  pool.
- Account-level suppression list – Owned and
  managed by the customer to protect their account reputation - _overrides
  the global suppression list_.

      + Configuration set-level suppression –
       An override mechanism to provide conditional or fine-grained control of the
       account-level suppression list through the use of overrides specified in a
       configuration set.

  _The global suppression list_ was the only type of suppression list
  until account-level and configuration set-level suppression was introduced in the new Amazon SES
  console and API v2. The global suppression list is owned and managed by SES to
  protect the reputation of SES. This is needed because all SES customers are
  sharing the same pool of IP addresses (unless they have dedicated IPs), it’s important for
  SES to ensure that customers aren’t sending spam or anything that would negatively
  impact the reputation of those IP addresses in the SES shared IP pool. While you no
  longer directly interact with the global suppression list, it still operates in the
  background and the general tenets of how the global suppression list works can also be
  applied to explain the overall principles of how the other types of suppression work. See
  [Amazon SES global suppression
  list](sending-email-global-suppression-list.md "sending-email-global-suppression-list.md").

###### Note

The global suppression list removal request form is no longer in the Amazon SES console
because the account-level suppression list has superseded it for all the advantages
explained in this section.

_The account-level suppression list_ was introduced so that customers
can create and control their own suppression list and reputation, thus, the account-level
suppression list applies to your account only. The account-level suppression list interface
in the new console provides an easy way to manage addresses in your account-level
suppression list, including bulk actions to add or remove addresses. If
an address is on the global suppression list, but not on your account level suppression list
_(which means you want to send to it)_, and you do send to it, Amazon SES
will still attempt delivery, but if it bounces, the bounce will affect your own reputation,
but no one else will get bounces because they can’t send to that email address if they
aren’t using their own account level suppression list; therefore, the account-level
suppression list overrides the global suppression list for your account only. See [Using the Amazon SES account-level suppression
list](sending-email-suppression-list.md "sending-email-suppression-list.md").

_Configuration set-level suppression_, while not a list per se, but a
mechanism that enables you to configure suppression customizations and overrides to your
account-level suppression list through the use of configuration sets specifically created
for different email sending scenarios. For example, if your account-level suppression list
is configured for both bounce and complaint addresses to be added, but you have a particular
email demographic defined in a configuration set for which you're only interested in
complaint addresses being added - you would achieve this by enabling this configuration
set's suppression overrides so that email addresses are added to your account-level
suppression list only for complaints (not bounces and complaints like is set in your
account-level suppression list) from email sent with this configuration set. With
configuration set-level suppression, there are different levels of overriding your
account-level suppression, including not using any suppression at all. See [Using configuration set-level
suppression to override your account-level suppression list](sending-email-suppression-list-config-level.md "sending-email-suppression-list-config-level.md").

###### Topics in this section

- [Amazon SES global suppression
  list](sending-email-global-suppression-list.md "sending-email-global-suppression-list.md")
- [Using the Amazon SES account-level suppression
  list](sending-email-suppression-list.md "sending-email-suppression-list.md")
- [Using configuration set-level
  suppression to override your account-level suppression list](sending-email-suppression-list-config-level.md "sending-email-suppression-list-config-level.md")
- [Using list management](sending-email-list-management.md "sending-email-list-management.md")
- [Using subscription
  management](sending-email-subscription-management.md "sending-email-subscription-management.md")
