# Mail Manager for Amazon SES

Mail Manager is a set of Amazon SES email gateway features designed to help you strengthen your
organization's email infrastructure, simplify email workflow management, and streamline
email compliance control. It integrates with your existing infrastructure, can connect
different business applications, and automates inbound email
processing. Mail Manager also acts as a first line of defense
in maintaining a healthy email system by efficiently managing your email traffic and
enhancing compliance with its email archival capability.

Along with current Amazon SES capabilities, Mail Manager consists of the following features that
support inbound traffic:

- Ingress endpoint – A key infrastructure component
  that utilizes filtering polices and rules that you can configure to determine which
  emails should be allowed into your organization and which ones should be
  rejected.
- Traffic policies and rule sets – Enable email
  administrators to define and enforce rules for managing inbound
  email traffic with highly customizable polices and rules that
  can sort, categorize, prioritize, and perform actions on emails based on a rich set
  of conditions and exceptions you define. This intelligent filtering combined with
  automated workflows helps to streamline email management, enhance efficiency, and
  ensure compliance with your organizational email policies.
- SMTP relay – Redirects email traffic to
  other SMTP servers based on criteria you define in
  rules
  by connecting internal email
  systems, and streamlines
  email management with automatic forwarding. Being able to distribute traffic across
  multiple servers and gateways enables your organization to manage high volume email
  traffic effectively, even in hybrid environments.
- Email archiving – Saves and protects your emails by
  storing data in persistent and secure long-term storage, and gives you a way to
  quickly search and archive email. It provides full-time, enterprise-level archiving
  without increasing the storage requirements of your mailbox server.
- Email Add Ons – A collection of specialized
  security tools from SES approved providers that can be used to manage email
  coming into your ingress endpoint as well as providing routing options based on
  security results. These tools are certified security intelligence and enforcement
  solutions that are ready to be integrated into your email workflow and can be
  activated directly from the Mail Manager console.

###### Getting started with Mail Manager

To start using Mail Manager, an onboarding wizard in the Amazon SES console will walk you through
the steps of enabling Mail Manager for your account. See [Getting started with Mail Manager](eb-getting-started.md "eb-getting-started.md").

###### Topics

- [Getting started with Mail Manager](eb-getting-started.md "eb-getting-started.md")
- [Ingress endpoints](eb-ingress.md "eb-ingress.md")
- [Traffic policies and policy statements](eb-filters.md "eb-filters.md")
- [Rule sets and rules](eb-rules.md "eb-rules.md")
- [SMTP relay](eb-relay.md "eb-relay.md")
- [Address Lists](eb-addlist.md "eb-addlist.md")
- [Email archiving](eb-archiving.md "eb-archiving.md")
- [Email Add Ons](eb-addons.md "eb-addons.md")
- [Permission policies for Mail Manager](eb-policies.md "eb-policies.md")
- [Mail Manager logging](eb-logging.md "eb-logging.md")
