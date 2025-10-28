# Security for your AWS Support cases

When you create a support case, you own the information that you include in your support
case. AWS doesn't access your
AWS account
data without your permission. AWS doesn't share your information with third parties.

When you create a support case, note the following:

- AWS Support uses the permissions defined in the
  `AWSServiceRoleForSupport` service-linked role to call other
  AWS services
  that troubleshoot customer issues
  for
  you. For more information, see [Using
  service-linked roles for AWS Support](using-service-linked-roles-sup.md "using-service-linked-roles-sup.md") and [AWS managed policy: AWSSupportServiceRolePolicy](aws-managed-policies-aws-support.md#security-iam-awsmanpol-AWSSupportServiceRolePolicy "aws-managed-policies-aws-support.md#security-iam-awsmanpol-AWSSupportServiceRolePolicy").
- You
  can view API calls to AWS Support that occurred in your AWS account. For example,
  you can view log information when someone in your account creates or resolves a
  support case. For more information, see [Logging AWS Support API
  calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- You can use the AWS Support API to call the `DescribeCases` API. This API
  returns support case information, such as the case ID, the create and resolve date,
  and correspondences with the support agent. You can view case details for up to 24
  months after the case was created. For more information, see [DescribeCases](../APIReference/API_DescribeCases.md "../APIReference/API_DescribeCases.md") in the _AWS Support API Reference_.
- Your support cases follow [Compliance validation for
  AWS Support](support-compliance.md "support-compliance.md").
- When
  you create a support case, AWS doesn't gain access your
  account. If necessary, support agents use a screen-sharing tool to view
  your
  screen remotely and identify and troubleshoot problems. This tool is view-only.
  AWS Support can't act for you during the screen-share session. You must give consent
  to share a screen with a support agent. For more information, see the [AWS Support FAQs](https://aws.amazon.com/premiumsupport/faqs/ "https://aws.amazon.com/premiumsupport/faqs/").
- You can change your AWS Support plan to get the help that you need for your account.
  For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/") and [Changing your AWS Support
  plan](changing-support-plans.md "changing-support-plans.md").
