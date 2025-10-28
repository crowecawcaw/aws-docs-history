# Deploying IAM resources in AMS Advanced

AMS deploys IAM resources in your multi-account landing zone (MALZ) Application and single-account landing zone (SALZ) accounts in two ways:

- Automated IAM Provisioning: This capability in AMS lets you submit create, update, or
  delete change types for IAM role or policy provisioning, without operator review, and with IAM and AMS validation checks run automatically.

This capability must be explicitly enabled with the Management | Managed account | AMS Automated IAM Provisioning with read-write permissions | [Enable (managed automation)](../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.md "../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.md")
change type (ct-1706xvvk6j9hf). To learn more, see [Automated IAM Provisioning AMS](auto-iam-provisioning.md "auto-iam-provisioning.md"). After AMS Automated IAM Provisioning is enabled, you have access to Create, Update, and Delete change types to manage your IAM resources.

- managed automation IAM change type: This change type, Deployment | Advanced stack components | Identity and Access Management (IAM) |
  [Create entity or policy (managed automation)](../ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy-review-required.md "../ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy-review-required.md") (ct-3dpd8mdd9jn1r), requires an AMS operator review, which can sometimes take a few days to complete if clarifications are needed.

###### Note

Whichever method is used, an IAM role is provisioned to the relevant account or accounts and, after the role is provisioned,
you must onboard the role in your federation solution.
