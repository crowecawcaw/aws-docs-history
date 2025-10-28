# Suggested controls to disable in Security Hub CSPM

We recommend disabling some AWS Security Hub CSPM controls to reduce finding noise and usage
costs.

## Controls that use global resources

Some AWS services support global resources, which means that you can access the resource from any AWS Region. To save on the cost of AWS Config, you can disable recording of global resources in all but one
Region. After you do this, however, Security Hub CSPM stills run security checks in all Regions where a control is enabled and charges you based on the
number of checks per account per Region. Accordingly, to reduce finding noise and save on the cost of Security Hub CSPM, you should also disable controls that involve global resources in all Regions except
the Region that records global resources.

If a control involves global resources but is available in only one Region, disabling
it in that Region prevents you from getting any findings for the underlying resource. In
this case, we recommend keeping the control enabled. When using cross-Region
aggregation, the Region in which the control is available should be the aggregation
Region or one of the linked Regions. The following controls involve global resources but
are available in only a single Region:

- **All CloudFront controls** – Available only in the
  US East (N. Virginia) Region
- **GlobalAccelerator.1** – Available only in the
  US West (Oregon) Region
- **Route53.2** – Available only in the US East (N. Virginia)
  Region
- **WAF.1, WAF.6, WAF.7, WAF.8** – Available only in the
  US East (N. Virginia) Region

###### Note

If you use central configuration, Security Hub CSPM automatically disables
controls that involve global resources in all Regions except the home Region. Other controls that you choose to enable
though a configuration policy are enabled in all
Regions where they are available. To limit findings for these controls to just one Region, you can update your AWS Config recorder settings and
turn off global resource recording in all Regions except the home Region.

If an enabled control that involves global resources isn't supported in the home Region, Security Hub CSPM tries to
enable the control in one linked Region where the control is supported. With central configuration, you lack coverage for a control
that isn't available in the home Region or any of the linked Regions.

For more information about central configuration, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").

For controls that have a _periodic_ schedule type, disabling them in
Security Hub CSPM is required to prevent billing. Setting the AWS Config parameter
`includeGlobalResourceTypes` to `false` doesn't affect
periodic Security Hub CSPM controls.

The following Security Hub CSPM controls use global resources:

- [[Account.1] Security contact information should be provided for an AWS account](account-controls.md#account-1 "account-controls.md#account-1")
- [[Account.2] AWS accounts should be part of an AWS Organizations organization](account-controls.md#account-2 "account-controls.md#account-2")
- [[CloudFront.1] CloudFront distributions should have a default
  root object configured](cloudfront-controls.md#cloudfront-1 "cloudfront-controls.md#cloudfront-1")
- [[CloudFront.3] CloudFront distributions should require
  encryption in transit](cloudfront-controls.md#cloudfront-3 "cloudfront-controls.md#cloudfront-3")
- [[CloudFront.4] CloudFront distributions should have origin
  failover configured](cloudfront-controls.md#cloudfront-4 "cloudfront-controls.md#cloudfront-4")
- [[CloudFront.5] CloudFront distributions should have logging
  enabled](cloudfront-controls.md#cloudfront-5 "cloudfront-controls.md#cloudfront-5")
- [[CloudFront.6] CloudFront distributions should have WAF
  enabled](cloudfront-controls.md#cloudfront-6 "cloudfront-controls.md#cloudfront-6")
- [[CloudFront.7] CloudFront distributions should use custom
  SSL/TLS certificates](cloudfront-controls.md#cloudfront-7 "cloudfront-controls.md#cloudfront-7")
- [[CloudFront.8] CloudFront distributions should use SNI to serve
  HTTPS requests](cloudfront-controls.md#cloudfront-8 "cloudfront-controls.md#cloudfront-8")
- [[CloudFront.9] CloudFront distributions should encrypt traffic
  to custom origins](cloudfront-controls.md#cloudfront-9 "cloudfront-controls.md#cloudfront-9")
- [[CloudFront.10] CloudFront distributions should not use
  deprecated SSL protocols between edge locations and custom origins](cloudfront-controls.md#cloudfront-10 "cloudfront-controls.md#cloudfront-10")
- [[CloudFront.12] CloudFront distributions should not point to
  non-existent S3 origins](cloudfront-controls.md#cloudfront-12 "cloudfront-controls.md#cloudfront-12")
- [[CloudFront.13] CloudFront distributions should use origin
  access control](cloudfront-controls.md#cloudfront-13 "cloudfront-controls.md#cloudfront-13")
- [[CloudFront.15] CloudFront distributions should use the
  recommended TLS security policy](cloudfront-controls.md#cloudfront-15 "cloudfront-controls.md#cloudfront-15")
- [[CloudFront.16] CloudFront distributions should use origin
  access control for Lambda function URL origins](cloudfront-controls.md#cloudfront-16 "cloudfront-controls.md#cloudfront-16")
- [[GlobalAccelerator.1] Global Accelerator accelerators should be tagged](globalaccelerator-controls.md#globalaccelerator-1 "globalaccelerator-controls.md#globalaccelerator-1")
- [[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")
- [[IAM.2] IAM users should not have IAM policies attached](iam-controls.md#iam-2 "iam-controls.md#iam-2")
- [[IAM.3] IAM users' access keys should be rotated every 90 days or less](iam-controls.md#iam-3 "iam-controls.md#iam-3")
- [[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")
- [[IAM.5] MFA should be enabled for all IAM users that have a console password](iam-controls.md#iam-5 "iam-controls.md#iam-5")
- [[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")
- [[IAM.7] Password policies for IAM users should have strong configurations](iam-controls.md#iam-7 "iam-controls.md#iam-7")
- [[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")
- [[IAM.9] MFA should be enabled for the root user](iam-controls.md#iam-9 "iam-controls.md#iam-9")
- [[IAM.10] Password policies for IAM users should have strong
  configurations](iam-controls.md#iam-10 "iam-controls.md#iam-10")
- [[IAM.11] Ensure IAM password policy requires at least one uppercase letter](iam-controls.md#iam-11 "iam-controls.md#iam-11")
- [[IAM.12] Ensure IAM password policy requires at least one lowercase letter](iam-controls.md#iam-12 "iam-controls.md#iam-12")
- [[IAM.13] Ensure IAM password policy requires at least one symbol](iam-controls.md#iam-13 "iam-controls.md#iam-13")
- [[IAM.14] Ensure IAM password policy requires at least one number](iam-controls.md#iam-14 "iam-controls.md#iam-14")
- [[IAM.15] Ensure IAM password policy requires minimum password length of 14 or greater](iam-controls.md#iam-15 "iam-controls.md#iam-15")
- [[IAM.16] Ensure IAM password policy prevents password reuse](iam-controls.md#iam-16 "iam-controls.md#iam-16")
- [[IAM.17] Ensure IAM password policy expires passwords within 90 days or less](iam-controls.md#iam-17 "iam-controls.md#iam-17")
- [[IAM.18] Ensure a support role has been created to manage incidents with
  AWS Support](iam-controls.md#iam-18 "iam-controls.md#iam-18")
- [[IAM.19] MFA should be enabled for all IAM users](iam-controls.md#iam-19 "iam-controls.md#iam-19")
- [[IAM.21] IAM customer managed policies that you create should not allow wildcard actions for services](iam-controls.md#iam-21 "iam-controls.md#iam-21")
- [[IAM.22] IAM user credentials unused for 45 days should be removed](iam-controls.md#iam-22 "iam-controls.md#iam-22")
- [[IAM.24] IAM roles should be tagged](iam-controls.md#iam-24 "iam-controls.md#iam-24")
- [[IAM.25] IAM users should be tagged](iam-controls.md#iam-25 "iam-controls.md#iam-25")
- [[IAM.26] Expired SSL/TLS certificates managed in IAM should be removed](iam-controls.md#iam-26 "iam-controls.md#iam-26")
- [[IAM.27] IAM identities should not have the AWSCloudShellFullAccess policy attached](iam-controls.md#iam-27 "iam-controls.md#iam-27")
- [[KMS.1] IAM customer managed policies should not allow decryption actions on all KMS keys](kms-controls.md#kms-1 "kms-controls.md#kms-1")
- [[KMS.2] IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys](kms-controls.md#kms-2 "kms-controls.md#kms-2")
- [[Route53.2] Route 53 public hosted zones should log DNS queries](route53-controls.md#route53-2 "route53-controls.md#route53-2")
- [[WAF.1] AWS WAF Classic Global Web ACL logging should be enabled](waf-controls.md#waf-1 "waf-controls.md#waf-1")
- [[WAF.6] AWS WAF Classic global rules should have at least one condition](waf-controls.md#waf-6 "waf-controls.md#waf-6")
- [[WAF.7] AWS WAF Classic global rule groups should have at least one rule](waf-controls.md#waf-7 "waf-controls.md#waf-7")
- [[WAF.8] AWS WAF Classic global web ACLs should have at least one rule or rule group](waf-controls.md#waf-8 "waf-controls.md#waf-8")

## CloudTrail logging controls

The [CloudTrail.2](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2") control evaluates the use of AWS Key Management Service (AWS KMS)
to encrypt AWS CloudTrail trail logs. If you log these trails in a centralized logging
account, you need to enable this control only in the account and AWS Region where
centralized logging takes place.

If you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"),
the enablement status of a control is aligned across the home Region and linked Regions.
You can't disable a control in some Regions and enable it in others. In this case, you
can suppress findings from the CloudTrail.2 control to reduce finding noise.

## CloudWatch alarm controls

If you prefer to use Amazon GuardDuty for anomaly detection instead of Amazon CloudWatch alarms, you can disable the following controls, which
focus on CloudWatch alarms:

- [[CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user](cloudwatch-controls.md#cloudwatch-1 "cloudwatch-controls.md#cloudwatch-1")
- [[CloudWatch.2] Ensure a log metric filter and alarm exist for unauthorized API calls](cloudwatch-controls.md#cloudwatch-2 "cloudwatch-controls.md#cloudwatch-2")
- [[CloudWatch.3] Ensure a log metric filter and alarm exist for Management Console sign-in without MFA](cloudwatch-controls.md#cloudwatch-3 "cloudwatch-controls.md#cloudwatch-3")
- [[CloudWatch.4] Ensure a log metric filter and alarm exist for IAM policy changes](cloudwatch-controls.md#cloudwatch-4 "cloudwatch-controls.md#cloudwatch-4")
- [[CloudWatch.5] Ensure a log metric filter and alarm exist for CloudTrail
  configuration changes](cloudwatch-controls.md#cloudwatch-5 "cloudwatch-controls.md#cloudwatch-5")
- [[CloudWatch.6] Ensure a log metric filter and alarm exist for AWS Management Console authentication failures](cloudwatch-controls.md#cloudwatch-6 "cloudwatch-controls.md#cloudwatch-6")
- [[CloudWatch.7] Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer managed keys](cloudwatch-controls.md#cloudwatch-7 "cloudwatch-controls.md#cloudwatch-7")
- [[CloudWatch.8] Ensure a log metric filter and alarm exist for S3 bucket policy changes](cloudwatch-controls.md#cloudwatch-8 "cloudwatch-controls.md#cloudwatch-8")
- [[CloudWatch.9] Ensure a log metric filter and alarm exist for AWS Config configuration changes](cloudwatch-controls.md#cloudwatch-9 "cloudwatch-controls.md#cloudwatch-9")
- [[CloudWatch.10] Ensure a log metric filter and alarm exist for security group changes](cloudwatch-controls.md#cloudwatch-10 "cloudwatch-controls.md#cloudwatch-10")
- [[CloudWatch.11] Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL)](cloudwatch-controls.md#cloudwatch-11 "cloudwatch-controls.md#cloudwatch-11")
- [[CloudWatch.12] Ensure a log metric filter and alarm exist for changes to network gateways](cloudwatch-controls.md#cloudwatch-12 "cloudwatch-controls.md#cloudwatch-12")
- [[CloudWatch.13] Ensure a log metric filter and alarm exist for route table changes](cloudwatch-controls.md#cloudwatch-13 "cloudwatch-controls.md#cloudwatch-13")
- [[CloudWatch.14] Ensure a log metric filter and alarm exist for VPC changes](cloudwatch-controls.md#cloudwatch-14 "cloudwatch-controls.md#cloudwatch-14")
