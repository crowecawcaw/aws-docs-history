# MIDASEC05-BP01 Define access permissions

Establish clear and granular access permissions to control who can access industrial
data, based on job roles and operational responsibilities.

**Desired outcome:** Only authorized personnel can access
specific data resources, reducing the risk of data leakage or misuse.

**Benefits of establishing this best practice:** Supports
principle of least privilege, improves accountability, and reduces insider threats.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use IAM policies and resource tagging strategies to enforce fine-grained permissions
aligned to user roles.

### Implementation steps

- Inventory data assets and define roles for access control.
- Apply IAM roles and permissions based on job functions.
- Use resource tags to apply conditional access policies.
- Review and refine permissions regularly using AWS IAM Access Analyzer.

## Resources

- [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
- [Using IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer.md "../../../IAM/latest/UserGuide/access-analyzer.md")
