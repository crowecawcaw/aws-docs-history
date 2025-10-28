# Prepare

As the threat landscape evolves, AMS continues to expand detection and response capabilities. As new detections are added, AMS incorporates the alerts
from these new detections into the detection and response
platform. AMS security responders are trained to investigate and partner with you throughout the Security Incident Response lifecycle.

Because of this partnership approach, it's important that your security and application teams are prepared to engage with AMS
to handle security events as these events occur. This documentation explains what to expect during a security
event and helps you prepare for rapid response when a security incident occurs.

This documentation uses the NIST 800-61 definition of an **event** as any observable
occurrence in a system or network and an **incident** as a violation or
imminent threat of violation of policies, acceptable use policies, or standard security practices.

## Preparation checklist

Work through the following checklist with your AMS cloud solution delivery manager (CSDM) and AMS cloud architect (CA):

- Understand what workloads are running in which accounts.
- Understand what internal teams are responsible for the various workloads and tag them appropriately in the workloads.
- Maintain contact details internally for other teams who might be required during a security event investigation and for containment decisions.
- Confirm that security contacts are up to date and added to all managed AWS accounts. The contacts are managed on a per account basis.
- Know how to raise security incident to AMS, and be familiar with the severity and expected response times.
- Make sure that when security notifications are received, they are routed to the appropriate people and systems such as pagers or your security operations center.
- Understand what log sources are available to you, where these are stored in your accounts and who has access to them.
- Understand how to use CloudWatch Insights to Query Logs during investigations.
- Understand the containment options available to you by resource (EC2, IAM, S3, and son on) and the consequences on your workload availability when in containment.
