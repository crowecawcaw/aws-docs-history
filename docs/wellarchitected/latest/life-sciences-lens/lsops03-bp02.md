# LSOPS03-BP02 Limit available services to improve regulatory

adherence

Use infrastructure tooling to allow only services that fit into
required regulatory frameworks.

**Desired outcome:** Only approved
services will be available for use.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Verify components and services used as available to comply with
identified frameworks. Check vendor documentation to confirm that
the products you use are approved at the vendor level.

### Implementation steps

1. Identify the available services by referring to
   [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").
2. Review audit guides for the available services.
3. Setup an AWS Organization to be able to centrally manage
   policies and controls.
4. Implement service control policies (SCP) limiting access to
   only the available services.

## Resources

**Related guides, videos, and
documentation:**

- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/")
- [What
  is AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
- [Service
  control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md")

**Related tools:**

- [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/")
- [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
