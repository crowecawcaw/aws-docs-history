**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Managed DDoS event response with Shield Response Team (SRT) support

This page describes the function of the Shield Response Team (SRT).

The SRT provides added support for Shield Advanced customers. The SRT are security
engineers who specialize in DDoS event response. As an additional layer of support to your
AWS Support plan, you can work directly with the SRT, leveraging their expertise as part of
your event response workflow. For information about the options and for configuration
guidance, see the topics that follow.

###### Note

To use the services of the Shield Response Team (SRT), you must be subscribed to the [Business Support
plan](https://aws.amazon.com/premiumsupport/business-support/ "https://aws.amazon.com/premiumsupport/business-support/") or the [Enterprise Support
plan](https://aws.amazon.com/premiumsupport/enterprise-support/ "https://aws.amazon.com/premiumsupport/enterprise-support/").

###### SRT support activities

The primary goal in an engagement with the SRT is to protect the availability and
performance of your application. Depending on the type of DDoS event and the
architecture of your application, the SRT may take one or more of the following
actions:

- **AWS WAF log analysis and rules** – For resources
  that use an AWS WAF web ACL, the SRT can analyze your AWS WAF logs to identify
  attack characteristics in your application web requests. With your approval during
  engagement, the SRT can apply changes to your web ACL to block the attacks that
  they've identified.
- **Build custom network mitigations** – The SRT can
  write custom mitigations for you for infrastructure layer attacks. The SRT can
  work with you to understand traffic that's expected for your application, to block
  unexpected traffic, and to optimize packet per second rate limits. For more
  information, see [Setting up custom mitigations against DDoS attacks with the SRT](ddos-srt-custom-mitigations.md "ddos-srt-custom-mitigations.md").
- **Network traffic engineering** – The
  SRT works closely with AWS networking teams to protect Shield Advanced customers.
  When required, AWS can change how internet traffic arrives on the AWS
  network in order to allocate more mitigation capacity to your application.
- **Architectural recommendations** – The
  SRT may determine that the best mitigation for an attack requires
  architectural changes to better align with the AWS best practices, and they will help support your implementation of these practices. For information, see [AWS
  Best Practices for DDoS Resiliency](../../../whitepapers/latest/aws-best-practices-ddos-resiliency.md "../../../whitepapers/latest/aws-best-practices-ddos-resiliency.md").
  The following sections provide instructions for engaging with the SRT

###### Topics

- [Granting access for the SRT](ddos-srt-access.md "ddos-srt-access.md")
- [Setting up proactive engagement for the SRT to contact you directly](ddos-srt-proactive-engagement.md "ddos-srt-proactive-engagement.md")
- [Contacting the SRT for help with a suspected DDoS event](ddos-srt-contacting.md "ddos-srt-contacting.md")
- [Setting up custom mitigations against DDoS attacks with the SRT](ddos-srt-custom-mitigations.md "ddos-srt-custom-mitigations.md")
