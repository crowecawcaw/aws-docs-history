# Cost Optimization Hub and AWS Organizations trusted access

When you opt in using your organization's management account and include all member
accounts within the organization, trusted access for Cost Optimization Hub is automatically enabled in your
organization account. Every time that you access recommendations for member accounts, Cost Optimization Hub
verifies that trusted access is enabled in your organization account. If you disable Cost Optimization Hub
trusted access after you opt in, Cost Optimization Hub denies access to recommendations for your
organization's member accounts. Moreover, the member accounts within the organization aren't
opted in to Cost Optimization Hub. To re-enable trusted access, opt in to Cost Optimization Hub again using your
organization's management account and include all the member accounts within the organization.
For more information, see [Opting in your account](coh-getting-started.md#coh-access "coh-getting-started.md#coh-access"). For more information about AWS
Organizations trusted access, see [Using AWS Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the _AWS Organizations User Guide_.

## Management account policy

This policy provides all the permissions necessary for a management account to opt in to
Cost Optimization Hub and have full access to the service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CostOptimizationHubAdminAccess",
 "Effect": "Allow",
 "Action": [
 "cost-optimization-hub:ListEnrollmentStatuses",
 "cost-optimization-hub:UpdateEnrollmentStatus",
 "cost-optimization-hub:GetPreferences",
 "cost-optimization-hub:UpdatePreferences",
 "cost-optimization-hub:GetRecommendation",
 "cost-optimization-hub:ListRecommendations",
 "cost-optimization-hub:ListRecommendationSummaries",
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowCreationOfServiceLinkedRoleForCostOptimizationHub",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/cost-optimization-hub.bcm.amazonaws.com/AWSServiceRoleForCostOptimizationHub"
 ],
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "cost-optimization-hub.bcm.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowAWSServiceAccessForCostOptimizationHub",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "organizations:ServicePrincipal": [
 "cost-optimization-hub.bcm.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Member account policy

This policy provides the permissions necessary for a member account to have full access
to Cost Optimization Hub.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CostOptimizationHubAdminAccess",
 "Effect": "Allow",
 "Action": [
 "cost-optimization-hub:ListEnrollmentStatuses",
 "cost-optimization-hub:UpdateEnrollmentStatus",
 "cost-optimization-hub:GetPreferences",
 "cost-optimization-hub:UpdatePreferences",
 "cost-optimization-hub:GetRecommendation",
 "cost-optimization-hub:ListRecommendations",
 "cost-optimization-hub:ListRecommendationSummaries"
 ],
 "Resource": "*"
 }
 ]
}`

```
