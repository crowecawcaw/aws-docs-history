**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Email best practices

Even when you have your customers' best interests in mind, you might still encounter
situations that impact the deliverability of your messages. The following sections contain
recommendations to help make sure that your email communications reach your intended
audience.

###### Topics

- [General recommendations](#channels-email-best-practices-general "#channels-email-best-practices-general")
- [Domain and "from" address
  considerations](#channels-email-best-practices-domain-from "#channels-email-best-practices-domain-from")
- [Building and maintaining your
  lists](#channels-email-best-practices-lists "#channels-email-best-practices-lists")
- [Compliance](#channels-email-best-practices-compliance "#channels-email-best-practices-compliance")
- [Sending a high volume of
  email](#channels-email-best-practices-highvolume "#channels-email-best-practices-highvolume")
- [Bounces](#channels-email-best-practices-bounce-rate "#channels-email-best-practices-bounce-rate")
- [Complaints](#channels-email-best-practices-complaints "#channels-email-best-practices-complaints")
- [Message quality](#channels-email-best-practices-quality "#channels-email-best-practices-quality")

## General recommendations

- Put yourself in your customer's shoes. Ask yourself if the message that you're
  sending is something that you would want to receive in your own inbox. If the
  answer is anything less than an enthusiastic "yes!" then you probably shouldn't
  send it.
- Some industries have a reputation for poor quality or even malicious email
  practices. If you're involved in the following industries, you must monitor your
  reputation very closely and resolve issues immediately:
  - Home mortgage
  - Credit
  - Pharmaceuticals and supplements
  - Alcohol and tobacco
  - Adult entertainment
  - Casinos and gambling
  - Work-from-home programs

## Domain and "from" address

considerations

- Carefully consider the addresses that you send email from. The _From_ address is one of the first pieces of
  information your recipients see, and therefore can leave a lasting first
  impression. Additionally, some ISPs associate your reputation with your
  _From_ address.
- Consider using subdomains for different types of communications. For example,
  assume you're sending email from the domain _example.com_,
  and you plan to send both marketing and transactional messages. Rather than
  sending all of your messages from _example.com_, send your
  marketing messages from a subdomain such as
  _marketing.example.com_, and your transactional messages
  from a subdomain such as _orders.example.com_. Unique
  subdomains develop their own reputations. Using subdomains reduces the risk of
  damage to your reputation if, for example, your marketing communications land in
  a spam trap or trigger a content filter.
- If you plan to send a large number of messages, don't send those messages from
  an ISP-based address such as *sender@hotmail.com*. If an ISP
  notices a large volume of messages coming from
  *sender@hotmail.com*, that email is treated differently
  than an email that comes from an outbound email sending domain that you
  own.
- Work with your domain registrar to make sure that the WHOIS information for
  your domain is accurate. Maintaining an honest and up-to-date WHOIS record
  demonstrates that you value transparency, and allows users to quickly identify
  whether your domain is legitimate.
- Avoid using a no-reply address, such as no-reply@example.com, as your
  _From_ or _Reply-to_ address. Using a _no-reply@_ email
  address sends your recipients a clear message: that you aren't offering them a
  way to contact you, and that you're not interested in their feedback.

## Building and maintaining your

lists

- Implement a double opt-in strategy. When users sign up to receive email from
  you, send them a message with a confirmation link, and don't start sending them
  email until they confirm their address by selecting that link. A double opt-in
  strategy helps reduce the number of hard bounces resulting from typographical
  errors.
- When collecting email addresses with a web-based form, perform minimal
  validation on those addresses upon submission. For example, make sure that the
  addresses you collect are well-formed (that is, they are in the format
  recipient@example.com), and that they refer to domains with valid MX
  records.
- Use caution when allowing user-defined input to be passed to Amazon Pinpoint unchecked.
  Forums registrations and form submissions present unique risks because the
  content is completely user-generated, and spammers can fill out forms with their
  own content. It's your responsibility to make sure that you only send email with
  high-quality content.
- It's highly unlikely that a standard alias (such as
  _postmaster@_, _abuse@_, or
  _noc@_) will ever sign up for your email intentionally.
  Make sure that you only send messages to real people who actually want to
  receive them. This rule is especially true for standard aliases, which are
  customarily reserved for email watchdogs.

## Compliance

- Be aware of the email marketing and anti-spam laws and regulations in the
  countries and regions that you send email to. You're responsible for making sure
  that the email you send complies with these laws. This guide doesn't cover these
  laws, so it's important that you research them. For a list of laws, see [Email
  spam legislation by country](https://en.wikipedia.org/wiki/Email_spam_legislation_by_country "https://en.wikipedia.org/wiki/Email_spam_legislation_by_country") on Wikipedia.
- Always consult an attorney to obtain legal advice.

## Sending a high volume of

email

Consistency is important when sending email. When increasing email volume, it's
important to steadily increase sending volume each day, with similar types of messages
being sent at around the same time every day. However, situations might arise that
require you to send an especially large volume of email to your customers. An example
might be a Terms of Service update. There are several steps that you can take to protect
your sender reputation and achieve high deliverability rates when increasing volume.

- Organize your recipient list to create segments of those customers who are
  most likely to open your email, and those who are most likely to mark your
  message as spam or unsubscribe.

Build a foundation of trust with email providers by sending messages to the
most engaged portion of the segment first.

- Spread out your campaign over several hours throughout the day, rather than
  sending all of your messages at once.

Mimic your normal sending cadence when possible. For example, if on a normal
day you send your list of 1M an email but split them into two distributions, one
beginning at 8 AM and one at Noon, but if you needed to send 5M out one day,
send in splits like your normal sending day.

- When you send volumes of email that are larger than your normal volumes, try
  to send in multiples of your typical volume.

For example, if you send 250,000 emails on a normal day, try to limit
higher-volume events to a multiple of that amount, such as 500,000 or 750,000.
Limiting your sending volume in this way demonstrates to email providers that
although you’re sending more email than normal, you’re still carefully
maintaining your volume.

## Bounces

A _bounce_ occurs when an email can't be delivered to the intended
recipient. There are two types of bounces: _hard bounces_ and
_soft bounces_. A hard bounce occurs when the email can't be
delivered because of a persistent issue, such as when an email address doesn't exist. A
soft bounce occurs when a temporary issue prevents the delivery of an email. Soft
bounces can occur when a recipient's inbox is full, or when the receiving server is
temporarily unavailable. Amazon Pinpoint handles soft bounces by attempting to re-deliver soft
bounced emails for a certain period of time.

It's essential that you monitor the number of hard bounces in your email program, and
that you remove hard-bouncing email addresses from your recipient lists. When email
receivers detect a high rate of hard bounces, they assume that you don't know your
recipients well. As a result, a high hard bounce rate can negatively impact the
deliverability of your email messages.

The following guidelines can help you avoid bounces and improve your sender
reputation:

- Try to keep your hard bounce rate below 5%. The fewer hard bounces in your
  email program, the more likely ISPs will see your messages as legitimate and
  valuable. This rate should be considered a reasonable and attainable goal, but
  isn't a universal rule across all ISPs.
- Never rent or buy email lists. These lists can contain large numbers of
  invalid addresses, which could cause your hard bounce rates to increase
  dramatically. Furthermore, these lists could contain spam traps—email
  addresses specifically used to catch illegitimate senders. If your messages land
  in a spam trap, your delivery rates and sender reputation could be irrevocably
  damaged.
- Keep your list up to date. If you haven't emailed your recipients in a long
  time, try to validate your customers' statuses through some other means (such as
  website login activity or purchase history).
- If you don't have a method of verifying your customers' statuses, consider
  sending a _win-back_ email. A typical win-back email mentions
  that you haven't heard from the customer in a while, and encourages the customer
  to confirm that they still want to receive your email. After sending a win-back
  email, purge all of the recipients who didn't respond from your lists.

When you receive bounces, it's important that you immediately remove that address from
your lists. Don't attempt to re-send messages to hard-bouncing addresses. Repeated hard
bounces can ultimately harm your reputation with the recipient's ISP.

If you receive a _hard bounce_, you should note the
following:

- The recipient's email address is added to a global suppression list for a
  period of 14 days. When you send an email and the recipient's address is on the
  global suppression list, the message is still accepted. However, Amazon Pinpoint doesn't
  attempt to deliver the message to the recipient.
- When an email _hard bounces_, it's important to remove the
  recipient's email address from your mailing lists. When you send email to an
  address that's on the global suppression list, Amazon Pinpoint generates bounce events,
  even though the email isn't sent. These bounce events count against your
  account's bounce rate. If your bounce rate gets too high, we might place your
  account under review in order to protect your reputation as a sender.

For more information about the global suppression list, see [Amazon SES global suppression list](../../../ses/latest/dg/sending-email-global-suppression-list.md "../../../ses/latest/dg/sending-email-global-suppression-list.md").

## Complaints

A complaint occurs when an email recipient selects the "Mark as Spam" (or equivalent)
button in their web-based email client. If you accumulate a large number of these
complaints, the ISP assumes that you're sending spam. This has a negative impact on your
deliverability rate and sender reputation. Some, but not all, ISPs will notify you when
a complaint is reported, which is known as a _feedback loop_. Amazon Pinpoint
automatically forwards complaints from ISPs that offer feedback loops to you.

The following guidelines can help you avoid complaints and improve your sender
reputation:

- Try to keep your complaint rate below 0.1%. The fewer complaints in your email
  program, the more likely ISPs will see your messages as legitimate and valuable.
  This rate should be considered a reasonable and attainable goal, but isn't a
  universal rule across all ISPs.
- If a customer complains about a marketing email, you should immediately stop
  sending that customer marketing emails. However, if your email program also
  includes other types of emails (such as notification or transactional emails),
  it might be acceptable to continue to send those types of messages to the
  recipient who issued the complaint.
- As with hard bounces, if you have a list that you haven't sent email to in a
  while, make sure that your recipients understand why they're receiving your
  messages. We recommend that you send a welcome message reminding them of who you
  are and why you're contacting them.

When you receive complaints, it's vital that you respond to them appropriately by
observing the following rules:

- Make sure that the address you use to receive complaint notifications is able
  to receive email.
- Make sure that your complaint notifications aren't being marked as spam by
  your ISP or mail system.
- Complaint notifications usually contain the body of the email. This is
  different from bounce notifications, which only include the email headers.
  However, in complaint notifications, the email address of the individual who
  issued the complaint is removed. Use custom X-headers or special identifiers
  embedded in the email body so that you can identify the email address that
  issued the complaint. This technique makes it easier to identify addresses that
  complained so that you can remove them from your recipient lists.

## Message quality

Email receivers use _content filters_ to detect certain
characteristics of messages and determine whether a message is legitimate. These content
filters automatically review the content of messages to identify common traits of
unwanted to malicious messages. Amazon Pinpoint uses content filtering technologies to help detect
and block messages that contain malware before they are sent.

If an email receiver's content filters determine that your message has characteristics
of spam or malicious email, your message will most likely be flagged and diverted from
recipients' inboxes.

Remember the following when designing your email:

- Modern content filters are intelligent, continuously adapting and changing.
  They don't rely on a predefined set of rules. Third-party services such as
  [ReturnPath](https://www.validity.com/everest/returnpath/ "https://www.validity.com/everest/returnpath/")
  or [Litmus](https://www.litmus.com/ "https://www.litmus.com/") can help identify content
  in your email that might trigger content filters.
- If your email contains links, check the URLs for those links against
  denylists, such as those found at [URIBL.com](https://uribl.com/ "https://uribl.com/") and [SURBL.org](https://www.surbl.org/ "https://www.surbl.org/").
- Avoid using link shorteners. Malicious senders might use link shorteners to
  hide the actual destination of a link. When ISPs notice that link shortening
  services—even the most reputable ones—are being used for nefarious
  purposes, they might denylist those services altogether. If your email contains
  a link to a denylisted link shortening service, it won't reach your customers'
  inboxes, and the success of your email campaign suffers.
- Test every link in your email to verify that it points to the intended
  page.
- Make sure that your website includes Privacy Policy and Terms of Use
  documents, and that these documents are up to date. It's a good practice to link
  to these documents from each email you send. Providing links to these documents
  demonstrates that you have nothing to hide from your customers, which can help
  build a relationship of trust.
- If you plan to send high-frequency content (such as "daily deals" messages),
  make sure that the content of your email is different with each deployment. When
  you send messages with high frequency, you must make sure that those messages
  are timely and relevant, rather than repetitive and annoying.
