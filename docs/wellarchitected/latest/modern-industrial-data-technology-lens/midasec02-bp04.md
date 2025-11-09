# MIDASEC02-BP04 Develop a mechanism for regular review of IAM roles and policies

Establish processes to regularly review IAM roles and permissions to help prevent
privilege creep and maintain access integrity over time.

**Desired outcome:** Stale or over-permissive access is
detected and remediated proactively.

**Benefits of establishing this best practice:** Improves
compliance posture, reduces operational risk, and enforces clean access policies aligned to
least privilege.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use tools like IAM Access Analyzer, AWS Config, and custom automation to audit and
report access configuration regularly.

### Implementation steps

- Establish a schedule for IAM access reviews.
- Use AWS IAM Access Analyzer to identify unused or overly broad permissions.
- Log and track review outcomes for auditing purposes.
- Automate revocation or modification of unneeded permissions using AWS Lambda or
  AWS Systems Manager.

## Resources

- [Using IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer.md "../../../IAM/latest/UserGuide/access-analyzer.md")
- [`iam-user-policy-check`](../../../config/latest/developerguide/iam-user-policy-check.md "../../../config/latest/developerguide/iam-user-policy-check.md")
