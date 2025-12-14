**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up AWS Shield Advanced

This tutorial walks you through getting started with AWS Shield Advanced using the Shield Advanced console.

###### Note

Shield Advanced requires a subscription, while AWS Shield Standard does not. The protections provided by Shield Standard are available free of charge to all
AWS customers.

Shield Advanced provides advanced
DDoS detection and mitigation protection for network layer (layer 3), transport layer (layer
4), and application layer (layer 7) attacks. For more information about Shield Advanced, see [AWS Shield Advanced overview](ddos-advanced-summary.md "ddos-advanced-summary.md").

The AWS technical community has published an example of an automated process for configuring Shield Advanced using the infrastructure as code (IaC) tools, AWS CloudFormation and Terraform. You can use AWS Firewall Manager with this solution if your accounts are part of an organization in AWS Organizations and if you're protecting any resource types except for Amazon Route 53 or AWS Global Accelerator.
To explore this option, see the code repository at [aws-samples
/ aws-shield-advanced-one-click-deployment](https://github.com/aws-samples/aws-shield-advanced-one-click-deployment "https://github.com/aws-samples/aws-shield-advanced-one-click-deployment")
and the tutorial at
[One-click deployment of Shield Advanced](https://youtu.be/LCA3FwMk_QE "https://youtu.be/LCA3FwMk_QE").

###### Note

It's important that you fully configure Shield Advanced prior to a Distributed Denial of Service (DDoS) event. Complete the
configuration to help ensure that your application is protected and that you are ready
to respond if your application is affected by a DDoS attack.

Perform the following steps in sequence to get started using Shield Advanced.

###### Contents

- [Subscribing to AWS Shield Advanced](enable-ddos-prem.md "enable-ddos-prem.md")
- [Adding and configuring resource protections with Shield Advanced](ddos-choose-resources.md "ddos-choose-resources.md")
  - [Configuring application layer (layer 7) DDoS
    protections with AWS WAF](ddos-get-started-web-acl-rbr.md "ddos-get-started-web-acl-rbr.md")
  - [Configuring health-based detection
    for your protections with Shield Advanced and Route 53](ddos-get-started-health-checks.md "ddos-get-started-health-checks.md")
  - [Configuring alarms and
    notifications with Shield Advanced and Amazon SNS](ddos-get-started-create-alarms.md "ddos-get-started-create-alarms.md")
  - [Reviewing and finishing your
    protection configuration in Shield Advanced](ddos-get-started-review-and-configure.md "ddos-get-started-review-and-configure.md")

- [Setting up AWS Shield Response Team (SRT) support for DDoS event response](authorize-srt.md "authorize-srt.md")
- [Creating a DDoS dashboard in CloudWatch and setting CloudWatch alarms](deploy-waf-dashboard.md "deploy-waf-dashboard.md")
