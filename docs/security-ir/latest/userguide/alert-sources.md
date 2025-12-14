# Alert sources

You should consider using the following sources to define alerts:

- **Findings** – AWS services such as [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/"), [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/"), [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/"), [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/"), [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/"), [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md"), and [Network Access Analyzer](../../../vpc/latest/network-access-analyzer/what-is-vaa.md "../../../vpc/latest/network-access-analyzer/what-is-vaa.md") generate findings that can be used to craft alerts.
- **Logs** – AWS service, infrastructure, and application
  logs stored in Amazon S3 buckets and CloudWatch log groups can be parsed and correlated to
  generate alerts.
- **Billing activit**y – A sudden change in billing
  activity can indicate a security event. Follow the documentation on [Creating a billing alarm to monitor your estimated AWS charges](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md") to monitor for
  this.
- **Cyber threat intelligence** – If you subscribe to a
  third-party cyber threat intelligence feed, you can correlate that information with
  other logging and monitoring tools to identify potential indicators of events.
- **Partner tools** – Partners in the AWS Partner Network
  (APN) offer top-tier products that can help you meet your security objectives. For
  incident response, partner products with endpoint detection and response (EDR) or SIEM
  can help support your incident response objectives. For more information, see [Security Partner
  Solutions](https://aws.amazon.com/security/partner-solutions/ "https://aws.amazon.com/security/partner-solutions/") and [Security Solutions in the
  AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security "https://aws.amazon.com/marketplace/solutions/security").
- **AWS trust and safety** – Support might contact
  customers if we identify abusive or malicious activity.
- **One-time contact** – Because it can be your customers,
  developers, or other staff in your organization who notice something unusual, it’s
  important to have a well-known, well-publicized method of contacting your security team.
  Popular choices include ticketing systems, contact email addresses, and web forms. If
  your organization works with the general public, you might also need a public-facing
  security contact mechanism.

For more information about cloud capabilities that you can use during your investigations, refer to
[Appendix A: Cloud capability definitions](appendix-a-cloud-capability-definitions.md "appendix-a-cloud-capability-definitions.md") in this document.
