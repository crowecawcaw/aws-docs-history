# Using subscription

management

Amazon SES provides a subscription management capability, in which Amazon SES automatically enables
the unsubscribe links in every outgoing email when you specify the
`contactListName` and `topicName` within [`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") in the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation request.

If a contact unsubscribes from a particular topic or list, Amazon SES does not allow email
sending to the contact for that topic or list in the future.

###### Note

- Amazon SES subscription management supports _Bulk Sender
  Requirements_ as enforced by many email service providers, see
  _Section 2_ in [An
  Overview of Bulk Sender Changes](https://aws.amazon.com//blogs/messaging-and-targeting/an-overview-of-bulk-sender-changes-at-yahoo-gmail/ "https://aws.amazon.com//blogs/messaging-and-targeting/an-overview-of-bulk-sender-changes-at-yahoo-gmail/") for more information.
- Subscription management is available for those using [Easy DKIM in Amazon SES](send-email-authentication-dkim-easy.md "send-email-authentication-dkim-easy.md"), but it’s not possible
  for Amazon SES to add the unsubscribe links to your email for senders who are signing
  emails themselves before calling Amazon SES.
  For information about list management and how to use it, including retrieving a list of
  all your contacts who have subscribed to a particular topic, see [Using list management](sending-email-list-management.md "sending-email-list-management.md").

## Subscription management

overview

You should consider the following factors when you use subscription management:

- Subscription management will be fully managed by Amazon SES. This means that Amazon SES
  receives unsubscribe emails and requests from the unsubscribe webpage and then
  updates the contact’s preference in your list. You can receive unsubscribe
  notifications using configuration set notifications. For more information about
  configuration sets, see [Using configuration sets in Amazon SES](using-configuration-sets.md "using-configuration-sets.md").
- You need to specify the contact list while sending the email. Subscription
  management via the `List-Unsubscribe` header and
  `ListManagementOptions` footer links will be handled accordingly.
- Amazon SES adds support for the `List-Unsubscribe` header standards,
  which will enable email clients and inbox providers to display an unsubscribe
  link at the top of the email _if they support it_ - not all
  email service providers support these headers.
- `List-Unsubscribe` headers follow the following behavior:
  - If a contact clicks the unsubscribe link in an email which has both
    the contact list and topic specified, then the contact will be
    unsubscribed only from that specific topic.
  - If the topic is not specified, then the contact will be unsubscribed
    from all the topics in the list.

- Contacts will be taken to an unsubscribe landing page when they click an
  unsubscribe link in the email footer.
- The unsubscribe landing page will give contacts an option to update their
  preferences, meaning `OPT_IN` or `OPT_OUT`, for all the
  topics in a particular list. The landing page also gives an option to
  unsubscribe from all topics in the list.
- If using [`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md"), you must include the
  `{{amazonSESUnsubscribeUrl}}` placeholder in your emails to
  indicate where Amazon SES needs to insert the unsubscribe URL. You can include the
  placeholder two times maximum. If used more than two times, only the first two
  occurrences are replaced.
- The `List-Unsubscribe` header and
  `ListManagementOptions` footer links are added only if the email
  is being sent to a single recipient.
- For transactional emails where you don't want contacts to be able to
  unsubscribe, you can omit the [`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") field with your [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") request.

## Unsubscribe header

considerations

Subscription management through an unsubscribe link is enabled when the email contains
the following headers:

`List-Unsubscribe`

`List-Unsubscribe-Post`

When you use Amazon SES's subscription management, [`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md"), Amazon SES will override these headers
if they are present in the email.

Recipients who unsubscribe by clicking the link produced by these headers will have a
different experience depending on their email client or inbox provider because some
providers do not recognize the `List-Unsubscribe` and
`List-Unsubscribe-Post` headers; email sent to recipients using such
providers will not see the Unsubscribe link.

Recipients whose email client recognizes these headers will see the Unsubscribe link
and will be able to unsubscribe via the link but will not have the option of choosing
which topics they unsubscribe from, and will simply be unsubscribed from the topic to
which the email was sent.

For more information about the `List-Unsubscribe` header, see [RFC 2369](https://tools.ietf.org/html/rfc2369 "https://tools.ietf.org/html/rfc2369"), and for the
`List-Unsubscribe-Post` header, see [RFC 8058](https://tools.ietf.org/html/rfc8058 "https://tools.ietf.org/html/rfc8058").

###### Note

Amazon SES supports _one-click unsubscribe_ in accordance with
_Bulk Sender Requirements_ as enforced by many email service
providers, see [Using
one-click unsubscribe with Amazon SES](https://aws.amazon.com//blogs/messaging-and-targeting/using-one-click-unsubscribe-with-amazon-ses/ "https://aws.amazon.com//blogs/messaging-and-targeting/using-one-click-unsubscribe-with-amazon-ses/") for more information.

## Adding an unsubscribe footer link

You will need to use the `{{amazonSESUnsubscribeUrl}}` placeholder in
templated and non-templated emails to specify where Amazon SES needs to insert the
unsubscribe URL.

Placeholder replacement is supported only for HTML and TEXT content types.

You can include the placeholder two times maximum. If used more than two times, only
the first two occurrences are replaced.

###### Note

The `{{amazonSESUnsubscribeUrl}}` placeholder can only be used if
[`ListManagementOptions`](../APIReference-V2/API_ListManagementOptions.md "../APIReference-V2/API_ListManagementOptions.md") is specified as a header while
using the [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md") operation or X-SES-LIST-MANAGEMENT-OPTIONS
is specified as a header while using the SMTP interface. (Not to be confused with
the `List-Unsubscribe` or `List-Unsubscribe-Post` headers
which are not dependent on `ListManagementOptions` and can be used by
themselves.)
