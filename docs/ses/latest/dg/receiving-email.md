# Email receiving with Amazon SES

Besides using Amazon SES to manage your email sending, you can also configure SES to
receive email on behalf of one or more of your domains. As the email receiver, SES
handles underlying mail-receiving operations, such as communicating with other mail servers,
scanning for spam and viruses, blocking mail from untrusted sources (addresses on the block
lists of either [Spamhaus](https://www.spamhaus.org/ "https://www.spamhaus.org/") or SES), and
accepting mail for recipients in your domain.

The extent of processing on your received email is determined by the custom instructions
you specify. These instructions come in two forms:

- **Receipt rules**
  _(recipient-based control)_ provide the finest granularity of
  control over incoming email. Receipt rules can do advanced processing such as
  deliver incoming mail to an Amazon S3 bucket, publish it to an Amazon SNS topic, send it to
  Amazon WorkMail, or automatically send bounce messages when messages are to specific
  email addresses, and more.
- **IP address filters**
  _(IP-based control)_ provide a broad level of control and are
  simple to setup. These filters allow you to explicitly block or allow all messages
  from specific IP addresses or IP address ranges.
  To get started with learning about email receiving, setting it up, and implementation
  using either _receipt rules_ or _IP address filters_,
  first read through [Email receiving concepts & use
  cases](receiving-email-concepts.md "receiving-email-concepts.md") to get an overview of how it works and
  the different ways you can use it. Next, [Setting up email
  receiving](receiving-email-setting-up.md "receiving-email-setting-up.md") will guide you through the email
  receiving set up prerequisites. Then, the [Email receiving console
  walkthroughs](receiving-email-walkthroughs.md "receiving-email-walkthroughs.md") will guide you through the wizards
  used for configuring _receipt rules_ and _IP address
  filters_.

###### Note

Email receiving can only be used if your account is in an AWS Region where
SES supports email receiving. The [Email Receiving endpoints](../../../general/latest/gr/ses.md#ses_inbound_endpoints "../../../general/latest/gr/ses.md#ses_inbound_endpoints")
table in the AWS General Reference lists all of the AWS Regions where SES supports
email receiving.

###### Topics in this section:

- [Amazon SES email receiving concepts and use
  cases](receiving-email-concepts.md "receiving-email-concepts.md")
- [Setting up Amazon SES email receiving](receiving-email-setting-up.md "receiving-email-setting-up.md")
- [Amazon SES email receiving console
  walkthroughs](receiving-email-walkthroughs.md "receiving-email-walkthroughs.md")
- [Viewing metrics for Amazon SES email receiving](receiving-email-metrics.md "receiving-email-metrics.md")
