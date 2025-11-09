# MIDASEC09-BP02 Perform regular vulnerability scans and penetration tests

Identify and mitigate vulnerabilities in applications and environments by conducting
recurring scans and authorized penetration testing.

**Desired outcome:** Exposed vulnerabilities are proactively
identified and mitigated before exploitation.

**Benefits of establishing this best practice:** Enhances
visibility into system weaknesses and builds resilience against external and internal threats.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use Amazon Inspector and integrate third-party scanning tools for deep and layered
assessments.

### Implementation steps

- Schedule recurring scans using Amazon Inspector across EC2 and container
  workloads.
- Perform black-box and white-box pen tests with third-party experts.
- Integrate findings with AWS Security Hub for centralized visibility.
- Remediate critical vulnerabilities through prioritized CI/CD updates.

## Resources

- [Getting started with Amazon Inspector](../../../inspector/latest/user/getting-started.md "../../../inspector/latest/user/getting-started.md")
- [Penetration Testing](https://aws.amazon.com/security/penetration-testing/ "https://aws.amazon.com/security/penetration-testing/")
