# HNSEC06-BP01 Monitor your environment for malicious

behavior

Responding to any cyber incident requires the ability to detect
threats and establish a baseline for normal operations in a hybrid
environment. Continuously monitors your environment for malicious
behavior to protect your accounts and workloads.

**Desired outcome:** Quick detection
of malicious activity enables fast containment and limits the impact
of ransomware and other security incidents.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Early identification of threats and abnormal behaviors
- Reduces containment and remediation time
- Enhances overall security posture with automated, continuous
  monitoring

## Implementation guidance

- Monitor flow logs, API activity, and DNS logs for threats,
  such as using Amazon GuardDuty that monitors and reports
  findings from these sources.
- Regularly review and baseline findings to distinguish normal
  from abnormal activity.

## Resources

- [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md")
