# MIDASEC02-BP02 Enable multi-factor authentication (MFA) and token authorization

(TA)

Strengthen identity verification by enforcing MFA for human users and implementing
token-based authorization for machines and services.

**Desired outcome:** Stronger authentication for both human
users and industrial systems accessing AWS resources.

**Benefits of establishing this best practice:** Reduces risks
associated with credential theft and replay attacks across IT/OT boundaries.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Enable MFA across all accounts, and integrate token services for secure, time-bound
access.

### Implementation steps

- Require MFA for all AWS accounts and IAM users using virtual or hardware devices.
- Implement SSO with MFA enforcement using AWS IAM Identity Center.
- Use temporary credentials and tokens through AWS Security Token Service for
  federated and service access.
- Enable and monitor MFA usage compliance with AWS Config rules.

## Resources

- [Using multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md")
- [What is AWS Identity and Access Management Access Analyzer?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")
- [Welcome to the AWS Security Token Service API Reference](../../../STS/latest/APIReference/welcome.md "../../../STS/latest/APIReference/welcome.md")
