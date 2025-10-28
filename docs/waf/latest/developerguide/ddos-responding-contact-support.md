**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Contacting the support center during an application layer DDoS

attack

This page provides instructions for contacting the support center during an application layer DDoS
attack.

If you're an AWS Shield Advanced customer, you can contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to
get help with mitigations. Critical and urgent cases are routed directly to DDoS
experts. With AWS Shield Advanced, complex cases can be escalated to the AWS Shield Response Team (SRT),
which has deep experience in protecting AWS, Amazon.com, and its subsidiaries. For
more information about the SRT, see [Managed DDoS event response with Shield Response Team (SRT) support](ddos-srt-support.md "ddos-srt-support.md").

To get Shield Response Team (SRT) support, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). The response time
for your case depends on the severity that you select and the response times, which are
documented on the [AWS Support Plans](https://aws.amazon.com/premiumsupport/compare-plans/ "https://aws.amazon.com/premiumsupport/compare-plans/") page.

Select the following options:

- Case type: Technical Support
- Service: Distributed Denial of Service (DDoS)
- Category: Inbound to AWS
- Severity: _Choose an appropriate option_
  When discussing with our representative, explain that you're an AWS Shield Advanced customer
  experiencing a possible DDoS attack. Our representative will direct your call to the
  appropriate DDoS experts. If you open a case with the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") using the
  **Distributed Denial of Service (DDoS)** service type, you can speak
  directly with a DDoS expert by chat or telephone. DDoS support engineers can help you
  identify attacks, recommend improvements to your AWS architecture, and provide guidance in
  the use of AWS services for DDoS attack mitigation.

For application layer attacks, the SRT can help you analyze the suspicious activity. If you have
automatic mitigation enabled for your resource, the SRT can review the
mitigations that Shield Advanced is automatically placing against the attack. In any case, the
SRT can assist you to review and mitigate the issue. Mitigations that the SRT recommends
often require the SRT to create or update AWS WAF web access control lists (web ACLs) in
your account. The SRT will need your permission to do this work.

###### Important

We recommend that as part of enabling AWS Shield Advanced, you follow the steps in [Granting access for the SRT](ddos-srt-access.md "ddos-srt-access.md") to proactively provide the SRT with the
permissions that they need to assist you during an attack. Providing permission
ahead of time helps to prevent any delays in the event of an actual attack.

The SRT helps you triage the DDoS attack to identify attack signatures and patterns.
With your consent, the SRT creates and deploys AWS WAF rules to mitigate the
attack.

You can also contact the SRT before or during a possible attack to review mitigations and
to develop and deploy custom mitigations. For example, if you're running a web application
and need only ports 80 and 443 open, you can work with the SRT to preconfigure a web ACL
to "allow" only ports 80 and 443.

You authorize and contact the SRT at the account level. That is, if you use Shield Advanced within
a Firewall Manager Shield Advanced policy, the account owner, not the Firewall Manager administrator, must
contact the SRT for support. The Firewall Manager administrator can contact the SRT only for
accounts that they own.
