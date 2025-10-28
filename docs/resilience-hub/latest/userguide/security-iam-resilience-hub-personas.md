# AWS Resilience Hub personas and IAM permissions reference

You can grant the IAM permissions to personas that are required to work with AWS Resilience Hub by using
`AWSResilienceHubAsssessmentExecutionPolicy` AWS managed policy and one
of the following persona-specific policies. For more information about AWS managed
policy, see [AWSResilienceHubAsssessmentExecutionPolicy](security-iam-awsmanpol.md#security_iam_aws-assessment-policy "security-iam-awsmanpol.md#security_iam_aws-assessment-policy").

###### Policies for personas suggested by AWS Resilience Hub:

- [IAM permissions for Infrastructure application manager persona](#iam-infra-continuity-manager "#iam-infra-continuity-manager")
- [IAM permissions for Business continuity manager persona](#iam-business-continuity-manager "#iam-business-continuity-manager")
- [IAM permissions for Application owner persona](#iam-application-owner "#iam-application-owner")
- [IAM permissions for granting read-only access](#iam-read-only-access "#iam-read-only-access")

## IAM permissions for Infrastructure application manager persona

The following policy grants necessary permissions required for the Infrastructure
application manager persona.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "InfrastructureApplicationManager",
 "Effect": "Allow",
 "Action": [
 "resiliencehub:AddDraftAppVersionResourceMappings",
 "resiliencehub:CreateAppVersionAppComponent",
 "resiliencehub:CreateAppVersionResource",
 "resiliencehub:CreateRecommendationTemplate",
 "resiliencehub:DeleteAppAssessment",
 "resiliencehub:DeleteAppInputSource",
 "resiliencehub:DeleteAppVersionAppComponent",
 "resiliencehub:DeleteAppVersionResource",
 "resiliencehub:DeleteRecommendationTemplate",
 "resiliencehub:Describe*",
 "resiliencehub:List*",
 "resiliencehub:PublishAppVersion",
 "resiliencehub:PutDraftAppVersionTemplate",
 "resiliencehub:RemoveDraftAppVersionResourceMappings",
 "resiliencehub:ResolveAppVersionResources",
 "resiliencehub:StartAppAssessment",
 "resiliencehub:TagResource",
 "resiliencehub:UntagResource",
 "resiliencehub:UpdateAppVersion",
 "resiliencehub:UpdateAppVersionAppComponent",
 "resiliencehub:UpdateAppVersionResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAM permissions for Business continuity manager persona

The following policy grants necessary permissions required for the Business
continuity manager persona.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BusinessContinuityManager",
 "Effect": "Allow",
 "Action": [
 "resiliencehub:CreateResiliencyPolicy",
 "resiliencehub:DeleteResiliencyPolicy",
 "resiliencehub:Describe*",
 "resiliencehub:List*",
 "resiliencehub:ResolveAppVersionResources",
 "resiliencehub:TagResource",
 "resiliencehub:UntagResource",
 "resiliencehub:UpdateAppVersion",
 "resiliencehub:UpdateAppVersionAppComponent",
 "resiliencehub:UpdateAppVersionResource",
 "resiliencehub:UpdateResiliencyPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAM permissions for Application owner persona

The following policy grants necessary permissions required for the Application
owner persona.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ApplicationOwner",
 "Effect": "Allow",
 "Action": [
 "resiliencehub:AddDraftAppVersionResourceMappings",
 "resiliencehub:BatchUpdateRecommendationStatus",
 "resiliencehub:CreateApp",
 "resiliencehub:CreateAppVersionAppComponent",
 "resiliencehub:CreateAppVersionResource",
 "resiliencehub:CreateRecommendationTemplate",
 "resiliencehub:CreateResiliencyPolicy",
 "resiliencehub:DeleteApp",
 "resiliencehub:DeleteAppAssessment",
 "resiliencehub:DeleteAppInputSource",
 "resiliencehub:DeleteAppVersionAppComponent",
 "resiliencehub:DeleteAppVersionResource",
 "resiliencehub:DeleteRecommendationTemplate",
 "resiliencehub:DeleteResiliencyPolicy",
 "resiliencehub:Describe*",
 "resiliencehub:ImportResourcesToDraftAppVersion",
 "resiliencehub:List*",
 "resiliencehub:PublishAppVersion",
 "resiliencehub:PutDraftAppVersionTemplate",
 "resiliencehub:RemoveDraftAppVersionResourceMappings",
 "resiliencehub:ResolveAppVersionResources",
 "resiliencehub:StartAppAssessment",
 "resiliencehub:TagResource",
 "resiliencehub:UntagResource",
 "resiliencehub:UpdateApp",
 "resiliencehub:UpdateAppVersion",
 "resiliencehub:UpdateAppVersionAppComponent",
 "resiliencehub:UpdateAppVersionResource",
 "resiliencehub:UpdateResiliencyPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAM permissions for granting read-only access

The following policy grants necessary permissions required for read-only access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadOnly",
 "Effect": "Allow",
 "Action": [
 "resiliencehub:Describe*",
 "resiliencehub:List*",
 "resiliencehub:ResolveAppVersionResources"
 ],
 "Resource": "*"
 }
 ]
}`

```
