# Updating the root user email address for a member account with AWS Organizations

For increased security and administrative resilience, IAM principals in the management
account (that have the necessary IAM permissions) can centrally update a root user email address (also referred to as the primary email address) for any of their member
accounts without having to sign into each account individually. This gives administrators in
the management account (or in a delegated administrator account) more control over their
member accounts. It also ensures that root user email
addresses from any
member accounts across your AWS Organizations can be kept up to date, even when you may have lost
access to the original root user email address or administrative credentials.

When the root user email address is changed centrally by a management account administrator, both
the password and MFA configuration will remain the same as they were before the change. Note
that MFA can be bypassed by a user with control of an account’s root user
email address and primary
contact phone number.

To update the root user email address of a member account in your organization, your
organization must have previously enabled [all
features](orgs_getting-started_concepts.md#feature-set-all "orgs_getting-started_concepts.md#feature-set-all") mode. AWS Organizations in consolidated billing mode or accounts that are not
part of an organization, cannot update their root user email
address centrally. Users
that want to change the root user email address for accounts that are unsupported by the
API should continue to use the Billing Console to manage their root user
email address.

For step-by-step instructions on how to update your member account's root user email address, see
[Update the root user email for any AWS account in your organization](../../../accounts/latest/reference/manage-acct-update-root-user-email.md#root-user-email-orgs "../../../accounts/latest/reference/manage-acct-update-root-user-email.md#root-user-email-orgs") in the
_AWS Account Management Reference Guide_.
