# Deny access to AWS based on the requested

AWS Region

*This control is commonly referred to as the Region deny control,
or *landing zone* Region deny control.*

This control disallows access to unlisted operations in global and regional services
outside of the specified Regions. That includes all Regions where AWS Control Tower is not available,
as well as all Regions not selected for governance in the **Landing zone
settings** page. Actions are allowed as usual in Regions with
**Governed** status.

You may wish to review the information at [Configure the Region deny
control](../userguide/region-deny.md "../userguide/region-deny.md") in the _AWS Control Tower User Guide_ before you enable this
control.

###### Note

Certain global AWS services, such as AWS Identity and Access Management (IAM) and AWS Organizations, are exempt from
data residency controls. Those services are specified in the SCP example code that
follows.

This is an elective control with preventive guidance. It is the top-level control
associated with the **Region deny** action.

The format for this control is based on the following SCP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRREGIONDENY",
 "Effect": "Deny",
 "NotAction": [
 "a4b:*",
 "access-analyzer:*",
 "account:*",
 "acm:*",
 "activate:*",
 "artifact:*",
 "aws-marketplace-management:*",
 "aws-marketplace:*",
 "aws-portal:*",
 "billing:*",
 "billingconductor:*",
 "budgets:*",
 "ce:*",
 "chatbot:*",
 "chime:*",
 "cloudfront:*",
 "cloudtrail:LookupEvents",
 "compute-optimizer:*",
 "config:*",
 "consoleapp:*",
 "consolidatedbilling:*",
 "cur:*",
 "datapipeline:GetAccountLimits",
 "devicefarm:*",
 "directconnect:*",
 "ec2:DescribeRegions",
 "ec2:DescribeTransitGateways",
 "ec2:DescribeVpnGateways",
 "ecr-public:*",
 "fms:*",
 "freetier:*",
 "globalaccelerator:*",
 "health:*",
 "iam:*",
 "importexport:*",
 "invoicing:*",
 "iq:*",
 "kms:*",
 "license-manager:ListReceivedLicenses",
 "lightsail:Get*",
 "mobileanalytics:*",
 "networkmanager:*",
 "notifications-contacts:*",
 "notifications:*",
 "organizations:*",
 "payments:*",
 "pricing:*",
 "quicksight:DescribeAccountSubscription",
 "resource-explorer-2:*",
 "route53-recovery-cluster:*",
 "route53-recovery-control-config:*",
 "route53-recovery-readiness:*",
 "route53:*",
 "route53domains:*",
 "s3:CreateMultiRegionAccessPoint",
 "s3:DeleteMultiRegionAccessPoint",
 "s3:DescribeMultiRegionAccessPointOperation",
 "s3:GetAccountPublicAccessBlock",
 "s3:GetBucketLocation",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetMultiRegionAccessPoint",
 "s3:GetMultiRegionAccessPointPolicy",
 "s3:GetMultiRegionAccessPointPolicyStatus",
 "s3:GetStorageLensConfiguration",
 "s3:GetStorageLensDashboard",
 "s3:ListAllMyBuckets",
 "s3:ListMultiRegionAccessPoints",
 "s3:ListStorageLensConfigurations",
 "s3:PutAccountPublicAccessBlock",
 "s3:PutMultiRegionAccessPointPolicy",
 "savingsplans:*",
 "shield:*",
 "sso:*",
 "sts:*",
 "support:*",
 "supportapp:*",
 "supportplans:*",
 "sustainability:*",
 "tag:GetResources",
 "tax:*",
 "trustedadvisor:*",
 "vendor-insights:ListEntitledSecurityProfiles",
 "waf-regional:*",
 "waf:*",
 "wafv2:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:RequestedRegion": []
 },
 "ArnNotLike": {
 "aws:PrincipalARN": [
 "arn:aws:iam::*:role/AWSControlTowerExecution"
 ]
 }
 }
 }
 ]
}`

```

Based on this example SCP format, AWS Control Tower adds your governed Regions into the
`aws:RequestedRegion` statement. You cannot exclude your home Region. Actions
not listed in the SCP are not permitted.

###### Limitations

The OU Region deny control is subject to limitations of the [`aws:RequestedRegion`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion") global condition key and [Service Control
Policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in general.
