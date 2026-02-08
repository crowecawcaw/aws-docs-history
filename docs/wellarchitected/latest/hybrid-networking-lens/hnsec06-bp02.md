# HNSEC06-BP02 Automate incident response

Implement automated response capabilities to enhance incident
containment speed and reliability while reducing manual intervention
requirements. This approach ensures consistent execution of response
procedures while minimizing human error during critical security
events.

**Desired outcome:** Faster, more
reliable containment and recovery from incidents with reduced
operational burden.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Shortens response times and limits damage
- Reduces alert fatigue and manual workload
- Ensures consistent, repeatable incident handling

## Implementation guidance

- Automate incident response by configuring security findings
  with response actions. For example, you can achieve this by
  integrating AWS Security Hub CSPM findings with AWS Lambda for
  automated actions.
- Test and tune automation playbooks in non-production
  environments.

## Resources

- [Using
  EventBridge for automated response and remediation PDF
  RSS](../../../securityhub/latest/userguide/securityhub-cloudwatch-events.md "../../../securityhub/latest/userguide/securityhub-cloudwatch-events.md")
- [AWS Lambda](../../../lambda/latest/dg/automating-security-responses.md "../../../lambda/latest/dg/automating-security-responses.md")
