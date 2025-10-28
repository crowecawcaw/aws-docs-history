# Security management

Security plays a key role and is foundational to all functions of
the M&G Guide. Security management is the process of setting up,
measuring, and improving security processes and tools. The M&G
Guide focuses on cloud-ready environments so that you are well
prepared to host your workloads. We recommend following the security
best practices described in the
[Well-Architected
Security Pillar](../security-pillar/welcome.md "../security-pillar/welcome.md") whitepaper for each type of workload you run
on AWS. You will find that the same principles for well-architected
workloads apply for how you effectively secure and manage
cloud-ready environments. Specifically, the security pillar includes
a comprehensive view of the best practices for management and
governance of security capabilities, some of which are highlighted
later in this guide. Further information on cloud adoption best
practices that align with the Security Pillar can also be found in
[AWS CAF](https://aws.amazon.com/professional-services/CAF/ "https://aws.amazon.com/professional-services/CAF/").

To scale with AWS, it is important to continually address and refine
your security capabilities alongside the rest of your management and
governance functions. This includes the identification, management,
and resolution of security issues and findings across all your
environments. As your scale increases with AWS, it is essential to
adapt your security management to the dynamic nature and ephemeral
lifespan of cloud resources. This adaptation includes response
mechanisms as well as ownership. In some cases, ownership of
security might merge with, and in other cases require new,
accountability and responsibility models.

The M&G Guide recommends standard ways to address AWS security across the eight
management and governance functions. For instance, in the [Controls](controls.md "controls.md") section, we demonstrate the need for security controls to be included
across your management and governance tooling. In this Security Management section, we outline
security tools and functions that are equally important to operating and scaling efficiently.
Each area of your cloud operations is responsible for implementing appropriate security
controls. These should include capabilities to identify, protect, detect, respond, and recover
from security issues and events.

## Security architecture

The
[AWS Security Reference Architecture (AWS SRA)](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md") is a holistic set
of guidelines for deploying the full complement of AWS security
services in a multi-account environment that is aligned to the
[Well-Architected
Security Pillar](../security-pillar/welcome.md "../security-pillar/welcome.md"). This overall architectural guidance
complements detailed, service-specific recommendations, such as
those found in
the [AWS Security Documentation](../../../security.md "../../../security.md"). For example, AWS SRA recommends
complementing the security architecture implemented in your
environments with a specific OU and account for security tooling.
Where services support this, delegate administration of
security-related services to the security tooling account. The
security tooling account will then serve as a central pane of glass
to the member accounts, providing insights for extended detection
and response (XDR) activities. Where required, also provide for
engineering and builder teams to create specialized or localized
security capabilities that are specific to their workloads. Note
that this reference architecture can be extended to include AWS
Partner solutions following the same patterns.

## Automated findings and campaigns

Following the prescriptive guidance in the [Controls](controls.md "controls.md") section of this guide, after you have detective controls in place
across your multi-account strategy, deviations from the controls should result in security
findings. A _finding_ is a specific deviation from a control associated
with a specific AWS account, AWS Region, environment, or resource. For each detective
mechanism you have, you should also have a clearly defined process in the form of a runbook or
playbook to investigate. Tickets should be automatically created based on findings with
information about the deviation, remediation guidance, and deadlines. Tickets are assigned to
the resource, account, or environment owner.

A _campaign_ is a way to aggregate issues around
a particular control or set of controls and drive action towards
remediation. Campaigns include the development of campaign metrics
to measure progress. You can also use campaigns and tickets to drive
action to have account owners put preventive controls in place.

Note that both campaigns and findings will need to be tuned along
with your threat detection tools. This tuning will allow you to
remove any noise created from false positives or negatives. In
contrast, any patterns from campaigns or findings will need to be
translated to additional controls.

## Security metrics

A mature internal security metrics program is crucial for managing
security in the cloud. In general, this is completed by following
the guidance of “what gets measured, gets done”. After you have
controls in place, security metrics are the primary way to assess
whether your security posture is improving, and whether your
controls are adequate. You should have metrics for each part of your
security organization, and these metrics should be reviewed
regularly to verify that they have the right level of organizational
buy-in and attention. For
example, mean time to identify (MTTI) root cause and mean time to
respond (MTTR) provide insights into your security incident response
effectiveness. Make sure that you have good processes and continuous
improvement around capturing, reviewing, and remediating insights
gained from them.

## Security response management

Enterprises are mandated to protect their digital infrastructure
from a wide range of threats and require in-depth visibility into
their infrastructure and applications to make faster data-driven
decisions. Enterprises need to take proactive actions to ensure
timely threat intelligence. Security solutions must monitor
workloads in real-time, identify security issues, and expedite
root-cause analysis. Essential elements of these tools allow you to
Identify, prioritize, and mitigate threats, gain visibility into
suspicious activities, and acknowledge risks. The Security Pillar
outlines specific recommendations for building your workloads while
thinking proactively about security. This is the foundation for
helping ensure that you can respond effectively to security insights
you are gathering.

Security management functions are responsible for analyzing and
responding to security events. Where in the past this was done with
human-powered processes, we recommend you automate these
identification and remediation systems. This automation will help
increase your security posture along with your ability to scale. At
cloud scale, use automated workflows wherever possible to investigate
events of interest and gather information on unexpected changes.
Require that these workflows be tested in development environments to
ensure operational resilience. Detect advanced security threats by
combining monitoring from network, firewall, identity, control
plane, vulnerability and patch management, workloads, and data
protection processes with your existing threat detection
capabilities. Threat detection can be used to determine the expected
pattern of API calls per role, application, or service, and
determine the levels that indicate an unexpected deviation. This
activity will allow you to maximize your telemetry by layering
behavioral analytics with your log analytics. The Security Pillar
outlines how to build a comprehensive detective capability with
options that include automated remediation and AWS Partner
solutions. This capability is enabled through the
[configuration
of environments](../security-pillar/configure.md "../security-pillar/configure.md") with centralized analysis of logs, findings,
and metrics. Automating aspects of your incident management process
also improves reliability and increases the speed of your response,
which creates an environment easier to assess in after-action
reviews.
