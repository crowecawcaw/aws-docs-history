# Trust data sent to Verified Access from trust providers

Trust data is data sent to AWS Verified Access from a trust provider. Trust data is also referred to
as "user claims" or "trust context." The data generally includes information about either a user
or a device. Examples of trust data include user email, group membership, device operating
system version, device security state, and so on. The information that's sent varies depending
on the trust provider, so you should refer to your trust provider’s documentation for a complete
and updated list of trust data.

However, by using the Verified Access logging capabilities, you can also see what trust data is
being sent from your trust provider. This can be useful when defining policies that allow or
deny access to your applications. For information on including trust context in your logs, see
[Enable or disable Verified Access trust context](include-trust-context.md "include-trust-context.md").

This section contains sample trust data and examples to help you get started with policy
writing. The information provided here is intended for illustrative purposes only and not as an
official reference.

###### Contents

- [Default context](trust-data-default-context.md "trust-data-default-context.md")
- [AWS IAM Identity Center context](trust-data-iam.md "trust-data-iam.md")
- [Third-party context](trust-data-third-party-trust.md "trust-data-third-party-trust.md")
- [User claims passing](user-claims-passing.md "user-claims-passing.md")
