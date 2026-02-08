# Design principles

Refer to design principles in the Well-Architected Framework Security Pillar for core
security concepts. Additionally, consider these Microsoft-specific security aspects:

- **Microsoft-specific security configurations:** Use Microsoft
  security baselines, Active Directory Group Policies, and Windows-specific security
  features like Windows Defender, AppLocker, and BitLocker for enhanced workload protection.
- **Identity integration patterns:** Implement proper
  integration between AWS IAM and Microsoft Active Directory services (either
  AWS Managed Microsoft AD or self-managed AD) for secure authentication across hybrid environments.
