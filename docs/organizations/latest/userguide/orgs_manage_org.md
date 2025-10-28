# Managing an organization with AWS Organizations

An _organization_ is a collection of AWS accounts that you can manage centrally and organize into a hierarchical,
tree-like structure with a root at the top and organizational units nested under the root. Each account can be
directly in the root, or placed in one of the OUs in the hierarchy.

Each organization consists of:

- A management account
- Zero or more member accounts
- Zero or more organizational units (OUs)
- Zero or more policies.
  An organization has the functionality that is determined by the [feature set](orgs_getting-started_concepts.md#feature-set "orgs_getting-started_concepts.md#feature-set") that you enable.

###### Topics

- [Creating an organization](orgs_manage_org_create.md "orgs_manage_org_create.md")
- [Verifying your email address](about-email-verification.md "about-email-verification.md")
- [Resending the verification email](about-email-verification-resend.md "about-email-verification-resend.md")
- [Changing your email address](about-email-verification-change-email.md "about-email-verification-change-email.md")
- [Enabling all features](orgs_manage_org_support-all-features.md "orgs_manage_org_support-all-features.md")
- [Viewing details of an organization](orgs_view_org.md "orgs_view_org.md")
- [Deleting an organization](orgs_manage_org_delete.md "orgs_manage_org_delete.md")
