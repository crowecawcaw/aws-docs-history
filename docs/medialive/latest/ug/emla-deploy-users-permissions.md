# Create users and assign

permissions

If you haven't set up users who will run channels on on-premises hardware, you should
do that now. If your organization is a current user of MediaLive and you are now deploying
MediaLive Anywhere, you must modify the permissions for your existing users. See [Identity and Access Management for
AWS Elemental MediaLive](security-iam.md "security-iam.md") and [Setting up IAM permissions for
users](setting-up-for-production.md "setting-up-for-production.md").

In both scenarios, there are two guidelines:

- When you create or modify your users, you might want to create a role and policies
  that are designed specifically for using MediaLive Anywhere.
- You must include permissions that the users need to work with MediaLive Anywhere. See [Requirements for MediaLive Anywhere](requirements-for-emla.md "requirements-for-emla.md").
