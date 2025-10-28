# SCSEC02-BP01 Track cloud resources and enforce compliance with automation

Implement automated monitoring systems to continuously track and
inventory all cloud resources throughout your supply chain
environment. Establish compliance guardrails with automated
enforcement mechanisms that validate configurations against
security and regulatory requirements before deployment.

Use automation to regularly audit existing resources, detect drift
from approved configurations, and remediate non-compliant
resources without manual intervention. This approach maintains
consistent governance across your supply chain while reducing the
operational burden of compliance management.

**Desired outcome:** Continuous
compliance tracking and automated remediation across multiple
accounts and regions.

**Benefits of establishing this best
practice:** Real-time detection, automated fixing of
non-compliant configurations, reduced risk of non-compliance and
improved efficiency in managing regulatory requirements.

**Level of risk exposed if this best
practice is not established:** high

## Implementation guidance

Configure AWS Config rules to evaluate resources on a periodic
or real-time basis for continuous compliance monitoring, while
utilizing AWS Config and its proactive mode to automatically
track and remediate resource configurations for continuous
compliance across accounts and regions.

Enable AWS Security Hub standards and controls to continuously
evaluate if security requirements are met across your supply
chain environments, and Implement automated workflows to route
security findings from AWS Security Hub to your incident
response and remediation processes.

### Implementation steps

1. Deploy AWS Config across the accounts and regions in your
   supply chain environment, configuring both periodic and
   change-triggered evaluation rules to monitor resource
   configurations against compliance standards.
2. Activate AWS Config's proactive mode to automatically
   remediate non-compliant resources, making sure
   configurations consistently meet security requirements
   without manual intervention.
3. Enable relevant AWS Security Hub standards (such as CIS
   AWS Foundations, AWS Foundational Security Best Practices,
   and industry-specific frameworks) to comprehensively
   evaluate security posture across your supply chain
   accounts.
4. Create custom Security Hub insights that focus
   specifically on supply chain-critical resources and
   configurations to prioritize security findings relevant to
   your business operations.
5. Implement automated workflows using EventBridge and Lambda
   to route Security Hub findings to appropriate teams,
   ticketing systems, and remediation processes based on
   severity and resource type.
6. Establish dashboards and regular reporting mechanisms that
   provide visibility into compliance status, trends, and
   remediation effectiveness across your supply chain
   environment.
