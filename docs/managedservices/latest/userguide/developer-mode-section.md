# AMS Advanced Developer mode

###### Topics

- [Getting started with AMS Advanced Developer mode](developer-mode-implement.md "developer-mode-implement.md")
- [Security and compliance in Developer mode](developer-mode-security-and-compliance.md "developer-mode-security-and-compliance.md")
- [Change management in Developer mode](developer-mode-change-management.md "developer-mode-change-management.md")
- [Provisioning infrastructure in AMS Developer mode](developer-mode-provisioning.md "developer-mode-provisioning.md")
- [Detective controls in AMS Developer mode](developer-mode-detective-controls.md "developer-mode-detective-controls.md")
- [Logging, monitoring, and event management in AMS Developer mode](developer-mode-logging.md "developer-mode-logging.md")
- [Incident management in AMS Developer mode](developer-mode-incident-management.md "developer-mode-incident-management.md")
- [Patch management in AMS Developer mode](developer-mode-patch-management.md "developer-mode-patch-management.md")
- [Continuity management in AMS Developer mode](developer-mode-continuity.md "developer-mode-continuity.md")
- [Security and access management in AMS Developer mode](developer-mode-security-and-access.md "developer-mode-security-and-access.md")
  AWS Managed Services (AMS) Developer mode uses elevated permissions in AMS Advanced Plus and Premium accounts to
  provision and update AWS resources outside of the AMS Advanced change management process. AMS Advanced
  Developer mode does this by leveraging native AWS API calls within the AMS Advanced Virtual Private
  Cloud (VPC), enabling you to design and implement infrastructure and applications in your managed environment.

When using an account that has Developer mode enabled, continuity management, patch
management, and change management are provided for resources provisioned through the AMS Advanced
change management process or by using an AMS Amazon Machine Image (AMI). However, these
AMS management features are not offered for resources provisioned through native AWS APIs.

You are responsible for monitoring infrastructure resources that are provisioned outside
of the AMS Advanced change management process. Developer mode is compatible with both production and
non-production workloads. With elevated permissions, you have an increased responsibility to
ensure adherence to internal controls.

###### Important

Resources that you create using Developer mode can be managed by AMS Advanced only if they are
created using AMS Advanced change management processes.

Developer mode is one of the AMS Advanced modes you can employ. For more information,
see [Modes overview](ams-modes-ug.md "ams-modes-ug.md").
