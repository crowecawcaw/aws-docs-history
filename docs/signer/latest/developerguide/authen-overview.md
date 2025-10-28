# Identity and Access Management for AWS Signer

An AWS account owner or an authorized administrator can attach permissions policies
to IAM identities (users, groups, and roles) that were created in the account. When
managing permissions, an account owner or administrator decides who gets the permissions
and what specific actions are allowed.

A _permissions policy_ describes who has access to what.
Administrators can use IAM to create policies that apply permissions to IAM users,
groups, and roles. The following types of _identity-based policies_
can grant permission for AWS Signer resources:

- **Customer managed policies** – Policies that
  an administrator creates and manages in an AWS account and which can be
  attached to multiple users, groups, and roles.
- **Inline policies** – Policies that an
  administrator creates and manages for a single IAM entity and which can be
  embedded directly into a single user, group, or role.
  For more information, see:

- [Customer managed policies for
  Signer](authen-custmanagedpolicies.md "authen-custmanagedpolicies.md")
- [Inline policies for Signer](authen-inlinepolicies.md "authen-inlinepolicies.md")
- [Use Signer actions in IAM](authen-apipermissions.md "authen-apipermissions.md")
- [Managed
  policies and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the IAM
  documentation.
