# Best practices for using

Amazon Inspector policies

When implementing Amazon Inspector policies across your organization, following established best
practices helps ensure successful deployment and maintenance.

## Start simply and make small changes

Begin by enabling Amazon Inspector policies at a limited organizational unit (for example,
"Security Pilot") to validate expected behavior before rolling out to all accounts. This
incremental approach allows you to identify and resolve potential issues in a controlled
environment before broader deployment.

## Establish review processes

Regularly monitor for new accounts joining your organization and confirm they inherit
Amazon Inspector enablement automatically. Review policy attachment scopes quarterly to ensure
your security coverage remains aligned with your organizational structure and security
requirements.

## Validate changes using DescribeEffectivePolicy

After attaching or modifying a policy, run `DescribeEffectivePolicy` for
representative accounts to ensure that Amazon Inspector enablement is reflected properly. This
validation step helps you confirm that your policy changes have the intended effect across
your organization.

## Communicate and train

Educate account owners that Amazon Inspector will be enabled automatically and findings may
appear in their Security Hub CSPM or Amazon Inspector dashboards once they are linked to the Amazon Inspector delegated
administrator. Clear communication helps ensure that account owners understand the security
monitoring in place and can respond appropriately to findings.

## Plan your delegated administrator strategy

Designate a security or compliance account as the delegated administrator for
Amazon Inspector. Set the delegated administrator from the Amazon Inspector console or via AWS Organizations APIs.
This approach enables consistent security monitoring and management across your
organization.

## Handle regional considerations

Enable Amazon Inspector in Regions where your workloads run. Consider your compliance
requirements and operational needs when determining which Regions require Amazon Inspector
coverage. Document your region-specific requirements to maintain consistent security
monitoring across your infrastructure.
