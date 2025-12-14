# ADVREL08-BP03 Implement secure and privacy-preserving

recovery mechanisms for collaboration workloads

Ad data requires security and preservation of privacy. Implement tooling and systems that preserve secure data and avoid privacy breaches when collaborating with first and third parties, and verify that you have disaster recovery and automated backup mechanisms in place.

## Implementation guidance

- Design recovery procedures that maintain data encryption
  throughout the process.
- Implement point-in-time recovery for privacy-protected
  datasets.
- Configure automated backup verification with privacy
  controls intact.
- Set up secure backup encryption key rotation policies.
- Establish recovery time objectives (RTOs) aligned with
  privacy requirements. This is because privacy requirements
  can significantly extend RTOs by adding mandatory
  verification and security steps.
- Implement secure state management for interrupted privacy
  computations. For example, if encryption fails during
  recovery, then halt the process rather than expose data;
  if privacy controls can't be verified then deny access
  until controls are restored; If secure state can't be
  maintained then terminate the computation safely
- Create automated disaster recovery testing procedures.

## Key AWS services

- AWS Backup
- AWS KMS
- AWS Secrets Manager
- Amazon S3

## Resources

- [Data protection](../../../whitepapers/latest/aws-caf-security-perspective/data-protection.md "../../../whitepapers/latest/aws-caf-security-perspective/data-protection.md")
