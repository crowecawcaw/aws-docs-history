# Amazon EMR AWS GovCloud (US-West) errors

The AWS GovCloud (US-West) region differs from other regions in its security, configuration,
and default settings. As a result, use the following checklist to troubleshoot Amazon EMR errors
that are specific to the AWS GovCloud (US-West) region before using more general troubleshooting
recommendations.

- Verify that your IAM roles are correctly configured. For more information, see [Configure IAM service roles for Amazon EMR permissions to AWS
  services and resources](emr-iam-roles.md "emr-iam-roles.md").
- Ensure that your VPC configuration has correctly configured DNS resolution/hostname support, Internet Gateway, and DHCP Option Set parameters. For more information, see [VPC errors during Amazon EMR cluster operations](emr-troubleshoot-error-vpc.md "emr-troubleshoot-error-vpc.md").
  If these steps do not solve the problem, continue with the steps for troubleshooting common Amazon EMR errors.
  For more information, see [Collections of common errors in Amazon EMR](emr-troubleshoot-errors.md "emr-troubleshoot-errors.md").
