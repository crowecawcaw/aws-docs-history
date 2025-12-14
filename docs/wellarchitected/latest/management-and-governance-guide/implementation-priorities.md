# Implementation priorities

Using a centralized mechanism like AWS Control Tower to create
accounts that are pre-configured for compliance can help you
adjust to your changing scale needs. Having a multi-account
strategy helps raise your security posture with the necessary
separation of workloads and networks through logical and physical
boundaries. As such, the following controls
solutions should be prioritized:

## Define a multi-account strategy

AWS recommends that you define a multi-account strategy that
considers scale and operational efficiency concerns. This means that
you should separate out your workloads into a logical pattern that
best meets your operational needs. AWS provides
[prescriptive
guidance](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/ "https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/") that suggests you start with a foundational set of
accounts to accommodate centralized and decentralized capabilities
in your enterprise. You can centralize governance for distributed
and autonomous teams using multiple AWS accounts, which lets you
delineate at security, financial, and operational levels.

## Start with AWS Control Tower

[Enable
a landing zone using AWS Control Tower](../../../controltower/latest/userguide/getting-started-with-control-tower.md "../../../controltower/latest/userguide/getting-started-with-control-tower.md") in a new or existing
management account. AWS Control Tower creates a secure,
multi-account environment with an embedded set of default
guardrails. AWS Control Tower automatically enables AWS Config in
the AWS Control Tower Regions, with configuration history and
snapshots delivered to an Amazon S3 bucket located in a
centralized Log Archive account. It also provides the ability to
add guardrails for each organizational unit (OU) in your AWS
Organization. The landing zone includes a preconfigured security
OU with an audit and log archive account provisioned. This
includes guardrails to prevent unauthorized changes to the
security baseline in your audit account. CloudTrail logs are
encrypted (using AWS KMS) and enabled in all provisioned accounts
with SCPs to prevent their modification. By default, a sandbox OU
is provisioned for your use. Review the
[best
practices for organization unit](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/ "https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/") guidance to determine the
multi-account strategy and OU structure that will support your
unique enterprise needs.

Separating OUs by regulatory and SDLC environments is a commonly
used pattern. Workload OUs are used for accounts that host your
AWS resources to support your applications with the right policies
applied. AWS Control Tower allows you to allow or deny the use of
AWS Regions across your environments.

## Review and add preventive and detective controls

AWS Control Tower uses AWS Organizations service control policies
(SCPs) to provide preventive guardrails. SCPs define the
guardrails or limits that IAM roles and users can have in the
accounts located within the OU. Review the
_[strongly
recommended](../../../controltower/latest/userguide/strongly-recommended-guardrails.md "../../../controltower/latest/userguide/strongly-recommended-guardrails.md")_ and
_[elective](../../../controltower/latest/userguide/elective-guardrails.md "../../../controltower/latest/userguide/elective-guardrails.md")_
detective guardrails AWS Control Tower provides, and choose which
guardrails to apply. Use the AWS Security Foundations best
practices in AWS Security Hub CSPM to identify controls that apply to
your enterprise, and add any specific open standard controls
required for your workloads. Create additional preventive controls
as required, and group them by OUs to align them to your
multi-account strategy.

###### Note

SCPs have
[service quotas](../../../organizations/latest/userguide/orgs_reference_limits.md#min-max-values "../../../organizations/latest/userguide/orgs_reference_limits.md#min-max-values")
in the size and number that can be applied. Carefully consider
these quotas as you design your controls strategy.

Package your detective controls such that they can be deployed
easily as you create or update your accounts. There are a variety
of AWS Config Conformance Packs available to apply common sets of
AWS Config rules to meet open standards and best practices. For
instance, there is a sample pack that includes the
[Best
Practices for the Well-Architected Security Pillar](../../../config/latest/developerguide/operational-best-practices-for-wa-Security-Pillar.md "../../../config/latest/developerguide/operational-best-practices-for-wa-Security-Pillar.md"), which
can provide a starting list of best practice rules to provision.
Use these conformance packs to choose and add further guardrails
to your environments.

Annotate and prioritize your detective guardrail findings so that
they can be remediated in accordance with your security and
compliance frameworks. Use automation to detect out of policy
provisioning of resources. In addition, set and measure service
level objectives alongside updating your runbooks and playbooks.

## Select an aggregated view of your guardrails and findings

Centrally view the resource configuration and compliance data
recorded in your observability findings. AWS Security Hub CSPM is a
security and compliance service that provides security and
compliance posture management, as a service. It uses AWS Config
and AWS Config rules as its primary mechanism to evaluate the
configuration of AWS resources. AWS Config rules can also be used
to aggregate and evaluate resource configuration. Other AWS
services, such as AWS Control Tower and AWS Firewall Manager, also
provide an aggregated view of controls in their console view.
Regularly review aggregated views of guardrails to alert you on
any deviation of expected controls in your environments.

## Create a base foundation of capabilities for each of your accounts

You can [provision
AWS Control Tower accounts in an automated, batch fashion](https://www.youtube.com/watch?v=LxxQTPdSFgw "https://www.youtube.com/watch?v=LxxQTPdSFgw")
by calling the Service Catalog APIs. As you provision new
accounts, use
[Customizations
for AWS Control Tower](../../../controltower/latest/userguide/customize-landing-zone.md "../../../controltower/latest/userguide/customize-landing-zone.md") to add in a base set of services and
functions required for each account. This will include
capabilities across each of the eight M&G
Guide functions as well as tagging and support information. For
example:

From a networking perspective, determine which VPC structure is
provisioned and associate it to a central hub-spoke pattern. Add
in any necessary network constructs that vary by account type
(firewall, NAT gateway, etc.)

For identity management, after Control Tower is configured for
single sign-on integrated with your federated user solution, you
can provision additional roles and policies. These mighty include
permissions boundaries to be distributed to member accounts.

Make sure that your monitoring and observability capabilities are
updated as new accounts are provisioned. Workloads should be
aligned to the environment logging strategies that describe which
logs to locate where, and how to appropriately integrate log
aggregation.

You might need to register new accounts with your security tools
(SIEM, GuardDuty, Security Hub CSPM, etc.), or deploy security
capabilities to specific accounts (XDR, CSPM, etc.).

As you create new accounts, it is important to align them with
your service and incident management capabilities. New accounts
should be integrated with your service management solution using
native connectors configured to integrate those solutions with
AWS. Update your playbooks and runbooks as appropriate.

[Tag
policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") and tag libraries help create consistent tagging
and can be used for common processes including Cloud Financial
Management (CFM). Consider distributing new financial guardrails
to detect deviations from expected budgets in spoke accounts.
Allocate appropriate support levels for each account using the
[AWS Support API](../../../awssupport/latest/user/Welcome.md "../../../awssupport/latest/user/Welcome.md").

Software assets managed in Service Catalog as portfolios can
be shared with users in one or more AWS accounts in a hub and
spoke pattern. Using Private Marketplace and private offers,
curate an assortment of third-party solutions and distribute them
alongside your infrastructure as code templates. Define which base
set of resources should be directly provisioned or made available
as a self-service model in each of your spoke accounts as they are
created with solutions such as the Customization Framework for
Control Tower.
