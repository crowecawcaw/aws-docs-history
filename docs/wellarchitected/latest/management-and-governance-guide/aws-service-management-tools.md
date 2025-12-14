# AWS service management tools

The AWS Management & Governance product suite allows you to
enable, provision, and operate AWS resources to determine the
health and predictability of your cloud workloads. The following
AWS services can be used to help you meet the prescribed benefits
of the M&G Guide, establish a cloud operational baseline, and
align to your ITSM solution implementation:

[AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") is a management service
that helps you automatically collect software inventory, apply operating system patches,
create system images, and configure Windows and Linux operating systems. These capabilities
help you define and track system configurations, prevent drift, and maintain software
compliance of your Amazon EC2 and on-premises configurations. By providing a management approach
that is designed for the scale and agility of the cloud but extends into your on-premises data
center, Systems Manager makes it easier for you to seamlessly bridge your existing infrastructure with
AWS.

[AWS Systems Manager Explorer](https://aws.amazon.com/systems-manager/features/ "https://aws.amazon.com/systems-manager/features/") is a customizable
dashboard providing key insights and analysis into the operational health and performance of
your AWS environments. Systems Manager Explorer aggregates operational data from across AWS accounts and
AWS Regions to help you prioritize and identify where action might be required.

[AWS Systems Manager
Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") allows you to safely automate common and repetitive IT operations and
management tasks. With Systems Manager Automation, you can use predefined runbooks, or you can build,
run, and share wiki-style automated playbooks to enable AWS resource management across
multiple accounts and AWS Regions. The runbooks can also be used to remediate issues such as
AWS Systems Manager OpsCenter OpsItems.

[AWS Systems Manager OpsCenter and Incident Manager](../../../systems-manager/latest/userguide/OpsCenter-getting-started.md "../../../systems-manager/latest/userguide/OpsCenter-getting-started.md") provide an
issue management mechanism that you can enable across your AWS accounts. This service provides a central location where
operations engineers and IT professionals can view, investigate,
and resolve operational issues related to any AWS resource.
OpsCenter aggregates and standardizes operational issues, referred
to as OpsItems, while providing contextually-relevant data that
helps with diagnosis and remediation.

[AWS Systems Manager Change Manager](https://aws.amazon.com/systems-manager/features/ "https://aws.amazon.com/systems-manager/features/") simplifies the way you request,
approve, implement, and report on operational changes to your
application configuration and infrastructure in the AWS Cloud and
on premises. With Change Manager, you can use pre-approved change
workflows to help avoid unintentional results when making
operational changes. Change Manager helps you safely implement
changes, while detecting schedule conflicts with important business
events and automatically notifying impacted approvers. Using
Change Manager’s change reports, you can monitor progress and
operational changes across your organization, providing improved
visibility and accountability.

[AWS Config](https://aws.amazon.com/config "https://aws.amazon.com/config") is a service that enables detective
controls to assess, monitor, and evaluate the configurations of supported AWS resources.
AWS Config monitors and records AWS resource configurations and allows you to automate the
evaluation of recorded configurations against desired configurations. With AWS Config, you are
able to not only track the relationships among resources and quickly review the history of the
resource's configuration but you can also identify the compliance of resources based on
defined config rules. Use [AWS Config](https://aws.amazon.com/config "https://aws.amazon.com/config") to view
status, compliance, and the relationships of your provisioned AWS resources. [Getting started
with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md") entails turning on recording and establishing the right detective
controls based on your governance and compliance requirements.

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") is a service that gives you a comprehensive view
of your security alerts and security posture across your AWS accounts. With Security Hub CSPM, you have a single place that
aggregates, organizes, and prioritizes your security alerts, or
findings. Security Hub CSPM findings can also enable your organization
to create incidents within ITSM tooling via integrations depending
on the finding’s severity level.

[Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/") allows you to centrally manage
commonly deployed AWS services and provisioned software products. The curated products are
vetted and enable end users to request services and resources as needed without having direct
permissions enabling segregation of duty. Service Catalog also helps your organization achieve consistent
governance and compliance requirements, while enabling users to quickly deploy only the
approved AWS services they need.
