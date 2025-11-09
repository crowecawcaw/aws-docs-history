# MIDASEC03-BP02 Implement industrial data classifications and protection policies

Define classification tiers for industrial data (for example, public, internal,
confidential, and restricted), and apply policies to control access, visibility, and
protection levels accordingly.

**Desired outcome:** Manufacturing data is systematically
classified and protected based on its criticality and sensitivity.

**Benefits of establishing this best practice:** Reduces risk
of data leakage, safeguards sensitive data, and supports scalable governance models.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS tools like Amazon Macie and AWS IAM policies to tag, monitor, and restrict
access to classified data.

### Implementation steps

- Define classification categories based on business needs and risk.
- Tag data assets using AWS resource tags or AWS AWS Glue Data Catalog.
- Use Amazon Macie to identify and monitor sensitive data types.
- Enforce access controls and monitoring based on classification tags.

## Resources

- [What is Amazon Macie?](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md")
- [Populating the AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md")
