# Aggregating AWS Health events across accounts

By default, you can use AWS Health to view the AWS Health events of a single AWS
account. If you use AWS Organizations, you can also view AWS Health events centrally across your
organization. This feature provides access to the same information as single account
operations. You can use filters to view events in specific AWS Regions, accounts, and
services.

You can aggregate events to identify accounts in your organization that are affected by an
operational event or get notified for security vulnerabilities. You can then use this
information to proactively manage and automate resource maintenance events across your
organization. Use this feature to stay informed of upcoming changes to AWS services that
might require updates or code changes.

It's a best practice to use the [Delegated Administrator](delegated-administrator-organizational-view.md "delegated-administrator-organizational-view.md")
feature to delegate access to the AWS Health Organizational view to a member account. This
makes it easier for operational teams to access the AWS Health events in your organization.
The Delegated Administrator feature allows you to keep your management account restricted,
while providing teams with the visibility that they need to act on AWS Health
events.

###### Important

- AWS Health events that were sent for accounts in your organization will
  appear in organizational view as long as the event is available, up to 90 days,
  even if one or more of those accounts leave your organization.
- Organizational events are available for 90 days before they're deleted. This
  quota can't be increased.

## Prerequisites

Before you use organizational view, you must:

- Be part of an organization with [all features](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set-all "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#feature-set-all") enabled.
- Sign in to the management account as an AWS Identity and Access Management (IAM) user or assume an
  IAM role.

You can also sign in as the root user (not recommended) in your organization's
management account. For more information, see [Lock away your AWS account root user access
keys](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials") in the _IAM User Guide_.

- If you sign in as an IAM user, use an IAM policy that grants access to the
  AWS Health and Organizations actions, such as the [AWSHealthFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess") policy. For more
  information, see [AWS Health identity-based
  policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### Topics

- [Enabling organizational view](enable-organizational-view.md "enable-organizational-view.md")
- [Viewing organizational view](view-organizational-view-events.md "view-organizational-view-events.md")
- [Disabling organizational view](disable-organizational-view.md "disable-organizational-view.md")
- [Managing delegated administrator
  views for an organization](delegated-administrator-organizational-view.md "delegated-administrator-organizational-view.md")
