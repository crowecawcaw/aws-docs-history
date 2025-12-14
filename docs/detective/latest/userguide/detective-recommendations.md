# Recommendations to enable Detective

Consider following these recommendations before enabling Detective

## Recommended alignment with GuardDuty and

AWS Security Hub CSPM

If you are enrolled in GuardDuty and AWS Security Hub CSPM, we recommend that your account be an
administrator account for those services. If the administrator accounts are the same for all
three services, then the following integration points work seamlessly.

- In GuardDuty or Security Hub CSPM, when viewing details for a GuardDuty finding, you can pivot from the
  finding details to the Detective finding profile.
- In Detective, when investigating a GuardDuty finding, you can choose the option to archive
  that finding.

If you have different administrator accounts for GuardDuty and Security Hub CSPM, we recommend that you
align the administrator accounts based on the service you use more frequently.

- If you use GuardDuty more frequently, then enable Detective using the GuardDuty administrator
  account.

If you use AWS Organizations to manage accounts, designate the GuardDuty administrator account as
the Detective administrator account for the organization.

- If you use Security Hub CSPM more frequently, then enable Detective using the Security Hub CSPM administrator
  account.

If you use Organizations to manage accounts, designate the Security Hub CSPM administrator account as the
Detective administrator account for the organization.

If you cannot use the same administrator accounts across all of the services, then after
you enable Detective, you can optionally create a cross-account role. This role grants an
administrator account access to other accounts.

For information about how IAM supports this type of role, see [Providing access to an
IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md") in the
_IAM User Guide_.

## Recommended update to the GuardDuty CloudWatch

notification frequency

In GuardDuty, detectors are configured with an Amazon CloudWatch notification frequency for reporting
subsequent occurrences of a finding. This includes sending notifications to Detective.

By default, the frequency is six hours. This means that even if a finding recurs many
times, the new occurrences are not reflected in Detective until up to six hours later.

To reduce the amount of time it takes for Detective to receive these updates, we recommend
that the GuardDuty administrator account changes the setting on their detectors to 15 minutes.
Note that changing the configuration has no effect on the cost of using GuardDuty.

For information about setting the notification frequency, see [Monitoring GuardDuty Findings with
Amazon CloudWatch Events](../../../guardduty/latest/ug/guardduty_findings_cloudwatch.md "../../../guardduty/latest/ug/guardduty_findings_cloudwatch.md") in the _Amazon GuardDuty User Guide_.
