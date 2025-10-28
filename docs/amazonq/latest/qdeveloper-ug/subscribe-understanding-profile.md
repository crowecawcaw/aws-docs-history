# What is the Amazon Q Developer profile?

###### Note

This section does not apply to personal accounts (Builder IDs).

An _Amazon Q Developer profile_, also known as a _settings
profile_, a collection of Amazon Q Developer settings associated with a set of IAM Identity Center
workforce user Pro tier subscriptions. The profile is also associated with an Amazon Q Developer managed
application which ties the user's identity in IAM Identity Center to their subscription in Amazon Q Developer.

The very first time you subscribe users, you will be prompted to create this profile. Creating
the profile causes several pages to appear in the side navigation of the Amazon Q Developer console where
you can configure Amazon Q Developer Pro features. All subscriptions that you add to your account (during the
initial subscription process, and later) will be associated with this profile.

Other characteristics of the Amazon Q Developer profile are:

- The profile is mandatory for use with IAM Identity Center workforce users. You cannot subscribe
  workforce users without it. It must be created in the AWS account where you want to
  subscribe users to Amazon Q Developer Pro.
- The profile can be created once per supported AWS Region, per AWS account. For a
  list of AWS Regions supported by the Amazon Q Developer profile, see [Supported Regions for the Q Developer
  console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").
