# AWS managed policy:

AmazonDataZoneSageMakerManageAccessRolePolicy

This policy gives Amazon DataZone permissions to publish Amazon SageMaker assets to the
catalog. It also gives Amazon DataZone permissions to grant access or revoke access to
the Amazon SageMaker published assets in the catalog.

This policy includes permissions to do the following:

- cloudtrail – retrieve information about CloudTrail trails.
- cloudwatch – retrieve the current CloudWatch alarms.
- logs – retrieve the metric filters for CloudWatch logs.
- sns – retrieve the list of subscriptions to an SNS topic.
- config – retrieve information about configuration recorders, resources,
  and AWS Config rules. Also allows the service-linked role to create and
  delete AWS Config rules, and to run evaluations against the rules.
- iam – get and generate credential reports for accounts.
- organizations – retrieve account and organizational unit (OU) information
  for an organization.
- securityhub – retrieve information about how the Security Hub service,
  standards, and controls are configured.
- tag – retrieve information about resource tags.
  To view the permissions for this policy, see [AmazonDataZoneSageMakerManageAccessRolePolicy](../../../aws-managed-policy/latest/reference/AmazonDataZoneSageMakerManageAccessRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonDataZoneSageMakerManageAccessRolePolicy.md") in the _AWS Managed Policy Reference_.
