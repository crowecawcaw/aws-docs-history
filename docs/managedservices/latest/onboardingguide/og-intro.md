# AWS Managed Services Onboarding Introduction

Welcome to AWS Managed Services (AMS). AMS is an enterprise service that provides ongoing
management of your AWS infrastructure. This guide is designed to help you get started using
AMS, including how to set up a new account for AMS, set up networking and access to
AMS, and validate your onboarding setup.

It is intended for IT administrators tasked with preparing for and carrying out the tasks
required to onboard the AMS service to a new AWS account. Onboarding the AMS service
requires special privileges to set up Active Directory trusts and complete other
networking-level tasks. To get help in deciding whether to use multi-account landing zone accounts or single-account landing zone accounts, visit
[Choosing single MALZ or multiple MALZs](../userguide/malz-single-or-multi.md "../userguide/malz-single-or-multi.md") .

###### Important

This guide is divided into two parts after this introduction: One for multi-account landing zone accounts and one for
single-account landing zone accounts. The onboarding is quite different for the two, please go next to the section of the guide that
applies to your situation.

###### Topics

- [Learning about AMS](#learning-about-sent "#learning-about-sent")
- [AMS key terms](key-terms.md "key-terms.md")
- [AMS modes](ams-modes-og.md "ams-modes-og.md")
- [AMS post-account prescriptive guidance](ams-ob-prescriptive-guidance.md "ams-ob-prescriptive-guidance.md")
- [What we do, what we do not do](ams-do-not-do.md "ams-do-not-do.md")
- [AMS egress traffic management](egress-traffic-mgmt.md "egress-traffic-mgmt.md")
- [IAM user role in AMS](defaults-user-role.md "defaults-user-role.md")
- [Default Access Firewall Rules](firewall-default-access-rules.md "firewall-default-access-rules.md")

## Learning about AMS

To understand AMS better, refer to these [AMS User Guide](../userguide/index.md "../userguide/index.md") sections:

- [What Is AWS Managed Services](../userguide/what-is-sent.md "../userguide/what-is-sent.md") introduces the AMS service and
  describes the key features, operations, and interfaces as well as a typical AMS-managed network architecture. This
  chapter also provides
  information on access management including how to access your AMS-managed resources and using bastions.
- [Key Terms](../userguide/key-terms.md "../userguide/key-terms.md") provides definitions and explanations for AMS
  terminology.
- [Understanding AMS Defaults](understanding-sent-defaults.md "understanding-sent-defaults.md") provides the
  default values AMS uses, including the defaults for basic environment components, IAM and EC2, proxies, monitored
  metrics,
  logging, endpoint security (EPS), backups, and patching.
- [Change Management](../userguide/change-mgmt.md "../userguide/change-mgmt.md") provides details on how requests for
  change (RFCs) and change types (CTs) work
  and includes examples of using AMS RFCs.
- Several additional chapters cover accessing the AWS console, the AMS CLI, using the AMS change management
  system,
  the AMS SKMS, security, service requests, incidents, monitoring, logs, EPS, backups, and patch management.

To learn more about AMS multi-account landing zone architecture, see
[Multi-Account Landing Zone network architecture](../userguide/malz-net-arch.md "../userguide/malz-net-arch.md")

To learn more about AMS single-account landing zone architecture, see
[Single-Account Landing Zone network architecture](../userguide/ams-net-arch.md "../userguide/ams-net-arch.md")
