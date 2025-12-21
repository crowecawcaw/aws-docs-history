# Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization

The following code example shows how to This permission-based policy grants read-only access to Compute Optimizer Automation for a management account of an organization

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aco-automation:GetEnrollmentConfiguration",
 "aco-automation:GetAutomationEvent",
 "aco-automation:GetAutomationRule",
 "aco-automation:ListAccounts",
 "aco-automation:ListAutomationEvents",
 "aco-automation:ListAutomationEventSteps",
 "aco-automation:ListAutomationEventSummaries",
 "aco-automation:ListAutomationRules",
 "aco-automation:ListAutomationRulePreview",
 "aco-automation:ListAutomationRulePreviewSummaries",
 "aco-automation:ListRecommendedActions",
 "aco-automation:ListRecommendedActionSummaries",
 "aco-automation:ListTagsForResource",
 "ec2:DescribeVolumes"
 ],
 "Resource": "*"
 }
 ]
}`

```

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Organizations with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
