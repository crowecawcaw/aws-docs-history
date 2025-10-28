# Best practices for PCI

compliance in Amazon Connect

Following this list of best practices can help you ensure your Amazon Connect contact center is
PCI-compliant.

- Conduct compliance eligibility audits for all services used in your contact
  center, as well as any third party integration points.
- Payment card information (PCI) should be collected using encrypted DTMF. You
  can also use Amazon Lex to gather PCI information using speech input. Amazon Lex is [PCI compliant](../../../lexv2/latest/dg/compliance.md "../../../lexv2/latest/dg/compliance.md").
- If PCI is captured in call recordings, the PCI data must be scrubbed from the
  recording and obfuscated from any logs or transcriptions. We recommend working
  with an Amazon Solution Architect if you need help doing this.
- Use encryption in transit and at rest for any downstream integration
  points.
- Enable multi-factor authentication (MFA) for any access to PCI as Amazon Connect is a
  public endpoint.
- AWS Key Management Service (KMS) encrypts Amazon S3 contents at the object level, which covers
  recordings, logs, and saved reports by default for Amazon S3. Make sure encryption in
  transit and at rest rules apply downstream or to third party apps.
- Use encryption in the **Store customer input** block for
  sensitive DTMF information.
- Use your own KMS key when ingesting data in Amazon Connect Customer Profile
  domains.
- For more information, see [https://www.pcisecuritystandards.org](https://www.pcisecuritystandards.org " https://www.pcisecuritystandards.org").
