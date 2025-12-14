**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Responding to DDoS events in AWS

This page explains how AWS responds to DDoS attacks, and provides options for how you can further respond.

AWS automatically mitigates network and transport layer (layer 3 and layer 4)
DDoS attacks. If you use Shield Advanced to protect your Amazon EC2 instances, during an
attack Shield Advanced automatically deploys your Amazon VPC network ACLs to the border of the AWS
network. This allows Shield Advanced to provide protection against larger DDoS events. For more
information about network ACLs, see [Network
ACLs](../../../AmazonVPC/latest/UserGuide/VPC_ACLs.md "../../../AmazonVPC/latest/UserGuide/VPC_ACLs.md").

For application layer (layer 7) DDoS attacks, AWS attempts to detect and notify
AWS Shield Advanced customers through CloudWatch alarms. By default, it doesn't automatically apply
mitigations, to avoid inadvertently blocking valid user traffic.

For application layer (layer 7) resources, you have the following options available for
responding to an attack.

- **Provide your own mitigations** – You can investigate
  and mitigate the attack on your own. For information, see [Manually mitigating an application layer DDoS attack](ddos-responding-manual.md "ddos-responding-manual.md").
- **Contact support** – If you're a Shield Advanced customer,
  you can contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to get help with mitigations. Critical
  and urgent cases are routed directly to DDoS experts. For information, see [Contacting the support center during an application layer DDoS
  attack](ddos-responding-contact-support.md "ddos-responding-contact-support.md").
  Additionally, before an attack occurs, you can proactively enable the following mitigation
  options:

- **Automatic mitigations on Amazon CloudFront distributions** –
  With this option, Shield Advanced defines and manages mitigating rules for you in your web
  ACL. For information about automatic application layer mitigation, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .
- **Proactive engagement** – When AWS Shield Advanced detects a
  large application layer attack against one of your applications, the SRT can
  proactively contact you. The SRT triages the DDoS event and creates AWS WAF
  mitigations. The SRT contacts you and, with your consent, can apply the AWS WAF
  rules. For more information about this option, see [Setting up proactive engagement for the SRT to contact you directly](ddos-srt-proactive-engagement.md "ddos-srt-proactive-engagement.md").
